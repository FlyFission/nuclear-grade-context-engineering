"""Required mode for a diff: the consequence policy, applied mechanically.

`ng required-mode` reads what a change touches (a git diff between a base and a head)
and a consequence policy (``.nuclear/consequence-policy.json``), and answers three
questions:

1. What mode does each changed path require? (``none`` < ``quick`` < ``standard`` <
   ``standard+authority``; the highest matching rule wins per path.)
2. Is that requirement covered? Coverage means a change record *added in this diff*,
   not closed, that declares a high enough mode, names the paths it covers in its
   ``risk.md``, and passes ``validate_packet`` with the flags that mode needs. Editing
   an older record never covers new work (the same rule ``challenge/score.py`` applies
   to its seeded record).
3. Does the requirement need a human? ``standard+authority`` changes and policy
   overrides pass only with an APPROVED review from an account that is neither the PR
   author nor a configured bot identity. Reviews are read by CI from the GitHub API and
   passed in with ``--approvals-json``; a label or an "approved by" line is never
   enough on its own.

The result is a mechanical *minimum*. Judgment (the router skill, `rating-change-risk`,
archetype floors) can raise a change's mode; nothing here lowers it. The checks are
structural: they show the expected record and approval exist, not that the change or
its evidence is adequate.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

from nuclear_grade.globmatch import glob_regex, match_any
from nuclear_grade.ng_validate import (
    MODE_DECLARATION_PATTERN,
    PARAPHRASE_PATTERNS,
    PROHIBITED_CLAIMS,
    has_closure_note,
    validate_packet,
)

SCHEMA = "nuclear-grade.required-mode-receipt"
SCHEMA_VERSION = 1
POLICY_PATH = ".nuclear/consequence-policy.json"
WORKTREE = "WORKTREE"
MODES = ("none", "quick", "standard", "standard+authority")
RANK = {mode: index for index, mode in enumerate(MODES)}
CLAIM_KINDS = ("general", "efficacy", "assurance")
BOUNDARY = (
    "Structural check only: it shows that the change record and approval this policy "
    "requires exist and validate. It does not show the change, its evidence, or the "
    "approval is adequate, and it creates no compliance or assurance claim."
)
# Declared packet modes the validator accepts, mapped onto the policy lattice.
DECLARED_RANK = {
    "quick": "quick",
    "standard": "standard",
    "incident": "standard",
    "research board": "standard",
    "nuclear": "standard+authority",
    "release": "standard+authority",
}

# Claim detectors. Assurance reuses the validator's prohibited-claim lists so there is
# one source for what an assurance claim looks like.
_EFFICACY = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:%|pp\b|percent\b|x\b)[^.\n]{0,60}?\b("
    r"improv|increas|reduc|faster|better|fewer|more|lift|gain|accura|success|"
    r"effective|efficacy|outperform)"
    r"|\b(improv\w*|increas\w*|reduc\w*|faster|better|lift\w*|gain\w*|"
    r"outperform\w*)\b[^.\n]{0,60}?\b\d+(?:\.\d+)?\s?(?:%|pp\b|percent\b|x\b)"
    r"|\b(statistically significant|proven (?:to|effective)|clinically proven)\b",
    re.IGNORECASE,
)
# Positive claim forms only: bare nouns ("compliance", "certification") appear in
# boundary lists and citation titles far more often than in claims.
_ASSURANCE_WORDS = re.compile(
    r"\b(compliant|certified|accredited|regulator[- ]?approved|SOC ?2(?: Type (?:I|II|1|2))?|"
    r"endorsed by|approved by the|meets? (?:all )?(?:regulatory|compliance) requirements)\b",
    re.IGNORECASE,
)
_GENERAL = re.compile(
    r"\b(proven|guarantee[sd]?|best[- ]in[- ]class|industry[- ]leading|world[- ]class|"
    r"endorse[sd]?|outperform\w*|bulletproof|secure by design|safe by design)\b",
    re.IGNORECASE,
)
_NEGATIONS = (
    " not ", "no ", "never ", "without ", "n't ", "does not", "do not", "is not",
    "cannot", "can't", "neither", "nor ", "inspired by", "influenced by",
)
_SHA = re.compile(r"\b[0-9a-f]{40}\b")
_VERSION_SPEC = re.compile(r"(?:[=<>~!^]=?\s*v?\d+(?:\.\d+)*|\bv?\d+\.\d+(?:\.\d+)?\b)")


class PolicyError(ValueError):
    """The policy file is malformed. Callers exit 2: the gate fails closed."""


class GitError(RuntimeError):
    """A git command failed (bad ref, not a repository, shallow history)."""


@dataclass(frozen=True)
class Rule:
    id: str
    mode: str
    paths: tuple[str, ...]
    exclude: tuple[str, ...] = ()
    content: re.Pattern[str] | None = None
    claims: str | None = None
    overridable: bool = True
    reason: str = ""
    skills: tuple[str, ...] = ()


@dataclass(frozen=True)
class Policy:
    default: str
    rules: tuple[Rule, ...]
    records_root: str = ".nuclear/changes"
    record_edit_mode: str = "quick"
    record_delete_mode: str = "standard"
    bot_identities: tuple[str, ...] = ()
    dependency_lane_authors: tuple[str, ...] = ()
    dependency_lane_paths: tuple[str, ...] = ()
    source: str = "built-in"
    digest: str = ""


@dataclass
class PathResult:
    path: str
    status: str
    required: str
    rules: list[str] = field(default_factory=list)
    covered_by: list[str] = field(default_factory=list)


# Applied when a repository has no policy file: only the gate's own trust surfaces.
BUILTIN_POLICY: dict = {
    "version": 1,
    "default": "none",
    "rules": [
        {
            "id": "ci",
            "mode": "standard+authority",
            "paths": [".github/workflows/**"],
            "overridable": False,
            "reason": "CI is the out-of-band gate",
        },
        {
            "id": "gate",
            "mode": "standard+authority",
            "paths": ["hooks/**", ".claude/**", ".nuclear/gate-policy.json", ".nuclear/charter.md"],
            "overridable": False,
            "reason": "the in-session gate and its charter",
        },
    ],
}


# ---------------------------------------------------------------- policy loading


def parse_policy(data: object, *, source: str = "built-in", digest: str = "") -> Policy:
    if not isinstance(data, dict):
        raise PolicyError("policy must be a JSON object")
    default = data.get("default", "none")
    if default not in RANK:
        raise PolicyError(f"unknown default mode {default!r}")
    raw_rules = data.get("rules", [])
    if not isinstance(raw_rules, list):
        raise PolicyError("'rules' must be a list")
    rules: list[Rule] = []
    seen: set[str] = set()
    for raw in raw_rules:
        if not isinstance(raw, dict):
            raise PolicyError("each rule must be an object")
        rule_id = raw.get("id")
        if not isinstance(rule_id, str) or not rule_id:
            raise PolicyError("each rule needs a non-empty 'id'")
        if rule_id in seen:
            raise PolicyError(f"duplicate rule id {rule_id!r}")
        seen.add(rule_id)
        mode = raw.get("mode")
        if mode not in RANK:
            raise PolicyError(f"rule {rule_id!r}: unknown mode {mode!r}")
        paths = raw.get("paths")
        if not isinstance(paths, list) or not paths or not all(isinstance(p, str) and p for p in paths):
            raise PolicyError(f"rule {rule_id!r}: 'paths' must be a non-empty list of globs")
        exclude = raw.get("exclude", [])
        if not isinstance(exclude, list) or not all(isinstance(p, str) and p for p in exclude):
            raise PolicyError(f"rule {rule_id!r}: 'exclude' must be a list of globs")
        content = raw.get("content")
        pattern = None
        if content is not None:
            if not isinstance(content, str) or not content:
                raise PolicyError(f"rule {rule_id!r}: 'content' must be a regex string")
            try:
                pattern = re.compile(content)
            except re.error as error:
                raise PolicyError(f"rule {rule_id!r}: bad 'content' regex: {error}") from None
        claims = raw.get("claims")
        if claims is not None and claims not in CLAIM_KINDS:
            raise PolicyError(f"rule {rule_id!r}: 'claims' must be one of {', '.join(CLAIM_KINDS)}")
        if pattern is not None and claims is not None:
            raise PolicyError(f"rule {rule_id!r}: use 'content' or 'claims', not both")
        overridable = raw.get("overridable", True)
        if not isinstance(overridable, bool):
            raise PolicyError(f"rule {rule_id!r}: 'overridable' must be true or false")
        skills = raw.get("skills", [])
        if not isinstance(skills, list) or not all(isinstance(s, str) for s in skills):
            raise PolicyError(f"rule {rule_id!r}: 'skills' must be a list of skill names")
        rules.append(Rule(rule_id, mode, tuple(paths), tuple(exclude), pattern, claims, overridable,
                          str(raw.get("reason", "")), tuple(skills)))
    lane = data.get("dependency_lane", {}) or {}
    if not isinstance(lane, dict):
        raise PolicyError("'dependency_lane' must be an object")
    for key in ("record_edit_mode", "record_delete_mode"):
        if data.get(key, "quick" if key == "record_edit_mode" else "standard") not in RANK:
            raise PolicyError(f"unknown {key} {data.get(key)!r}")
    return Policy(
        default=default,
        rules=tuple(rules),
        records_root=str(data.get("records_root", ".nuclear/changes")).strip("/"),
        record_edit_mode=data.get("record_edit_mode", "quick"),
        record_delete_mode=data.get("record_delete_mode", "standard"),
        bot_identities=tuple(_string_list(data.get("bot_identities", []), "bot_identities")),
        dependency_lane_authors=tuple(_string_list(lane.get("authors", []), "dependency_lane.authors")),
        dependency_lane_paths=tuple(_string_list(lane.get("paths", []), "dependency_lane.paths")),
        source=source,
        digest=digest,
    )


def _string_list(value: object, name: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
        raise PolicyError(f"'{name}' must be a list of strings")
    return value


def policy_text(repo: Path, ref: str) -> str | None:
    """The policy file's text at ``ref`` (or on disk for WORKTREE), or None if absent."""

    if ref == WORKTREE:
        path = repo / POLICY_PATH
        return path.read_text(encoding="utf-8") if path.is_file() else None
    result = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{POLICY_PATH}"],
                            capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None


def load_policy(repo: Path, ref: str, policy_file: Path | None = None) -> Policy:
    if policy_file is not None:
        text, source = policy_file.read_text(encoding="utf-8"), str(policy_file)
    else:
        text, source = policy_text(repo, ref), f"{ref}:{POLICY_PATH}"
    if text is None:
        return parse_policy(BUILTIN_POLICY, source="built-in (no policy file at the policy ref)")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise PolicyError(f"{source}: not valid JSON: {error}") from None
    return parse_policy(data, source=source, digest="sha256:" + hashlib.sha256(text.encode()).hexdigest())


# ---------------------------------------------------------------- git helpers


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise GitError(f"git {' '.join(args)}: {result.stderr.strip() or 'failed'}")
    return result.stdout


def changed_paths(repo: Path, base: str, head: str | None) -> dict[str, str]:
    """Map each changed path to A/M/D. Renames count as delete plus add.

    With ``head=None`` the working tree is the head, and untracked files count as added,
    as in ``challenge/score.py``.
    """

    refs = [base] if head is None else [base, head]
    out = _git(repo, "diff", "--name-status", "--no-renames", "-z", *refs)
    fields = [f for f in out.split("\0") if f]
    status: dict[str, str] = {}
    for code, path in zip(fields[0::2], fields[1::2], strict=True):
        status[path] = "A" if code.startswith("A") else "D" if code.startswith("D") else "M"
    if head is None:
        for path in _git(repo, "ls-files", "--others", "--exclude-standard", "-z").split("\0"):
            if path:
                status[path] = "A"
    return status


@dataclass
class Diff:
    """One path's changed lines, plus the hunks as they read before and after the change.

    ``after`` hunks hold (text, added) pairs for context and added lines; ``before``
    hunks hold (text, removed) pairs for context and removed lines. Claim detection
    reads whole sentences across them, so a negation on an unchanged line still counts.
    """

    added: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    after: list[list[tuple[str, bool]]] = field(default_factory=list)
    before: list[list[tuple[str, bool]]] = field(default_factory=list)


def diff_lines(repo: Path, base: str, head: str | None, path: str, status: str) -> Diff:
    """The diff for one path. Binary or oversized content yields an empty diff."""

    if head is None and status == "A" and not _tracked_at(repo, base, path):
        try:
            lines = (repo / path).read_text(encoding="utf-8").splitlines()[:20000]
        except (OSError, UnicodeDecodeError):
            return Diff()
        return Diff(added=lines, after=[[(line, True) for line in lines]])
    refs = [base] if head is None else [base, head]
    out = subprocess.run(["git", "-C", str(repo), "diff", "-U3", "--no-color", "--no-renames", *refs, "--", path],
                         capture_output=True, text=True, errors="replace")
    diff = Diff()
    for line in out.stdout.splitlines()[:60000]:
        if line.startswith(("+++", "---", "diff ", "index ", "new file", "deleted file", "Binary files")):
            continue
        if line.startswith("@@"):
            diff.after.append([])
            diff.before.append([])
            continue
        if not diff.after:
            continue
        if line.startswith("+"):
            diff.added.append(line[1:])
            diff.after[-1].append((line[1:], True))
        elif line.startswith("-"):
            diff.removed.append(line[1:])
            diff.before[-1].append((line[1:], True))
        elif line.startswith(" "):
            diff.after[-1].append((line[1:], False))
            diff.before[-1].append((line[1:], False))
    return diff


def _tracked_at(repo: Path, ref: str, path: str) -> bool:
    return subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"{ref}:{path}"],
                          capture_output=True).returncode == 0


# ---------------------------------------------------------------- claim detection


_LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s")
_SENTENCE_END = re.compile(r"[.!?](?:\s|$)|\n\s*\n")


def _negated(context: str) -> bool:
    lowered = " " + re.sub(r"[*_]+", "", context).lower() + " "
    return any(marker in lowered for marker in _NEGATIONS)


def _quoted(context: str) -> bool:
    """True when the text before a hit leaves a quote or code span open."""

    return (context.count('"') % 2 == 1 or context.count("`") % 2 == 1
            or context.count("\u201c") > context.count("\u201d"))


def _claim_spans(kind: str, text: str) -> list[tuple[int, int]]:
    if kind == "efficacy":
        return [m.span() for m in _EFFICACY.finditer(text)]
    if kind == "general":
        return [m.span() for m in _GENERAL.finditer(text)]
    spans = [m.span() for pattern in (*PARAPHRASE_PATTERNS, _ASSURANCE_WORDS) for m in pattern.finditer(text)]
    lowered = text.lower()
    for phrase in PROHIBITED_CLAIMS:
        start = lowered.find(phrase.lower())
        while start != -1:
            spans.append((start, start + len(phrase)))
            start = lowered.find(phrase.lower(), start + 1)
    return spans


def _claims_in(kind: str, hunks: list[list[tuple[str, bool]]]) -> list[str]:
    """Affirmative claims that fall on changed lines, read sentence by sentence.

    Each hunk is joined into paragraphs; a hit counts only if it sits on a changed line,
    is not inside quotes or a code span, and its sentence has no negation or boundary
    wording before it ("does not create compliance, certification, ...").
    """

    found = []
    for hunk in hunks:
        paragraph: list[tuple[str, bool]] = []
        lead_in = ""  # a sentence ending in ":" carries over to the list that follows it
        for item in [*hunk, ("", False)]:
            if item[0].strip():
                paragraph.append(item)
                continue
            if paragraph:
                is_list = bool(_LIST_ITEM.match(paragraph[0][0]))
                text = lead_in + " " if is_list and lead_in else ""
                spans, offset = [], len(text)
                for line, changed in paragraph:
                    if changed:
                        spans.append((offset, offset + len(line)))
                    text += line + " "
                    offset = len(text)
                for start, end in _claim_spans(kind, text):
                    if not any(a <= start < b for a, b in spans):
                        continue
                    before = text[:start]
                    ends = list(_SENTENCE_END.finditer(before))
                    sentence = before[ends[-1].end():] if ends else before
                    if _negated(sentence) or _quoted(sentence):
                        continue
                    found.append(text[start:end].strip())
                stripped = text.rstrip()
                if stripped.endswith(":"):
                    ends = list(_SENTENCE_END.finditer(stripped))
                    lead_in = stripped[ends[-1].end():] if ends else stripped
                elif not is_list:
                    lead_in = ""
            paragraph = []
    return found


def net_new_claims(kind: str, diff: Diff) -> list[str]:
    """Claims the change adds: on added lines, and not already made by removed lines."""

    before = {hit.lower() for hit in _claims_in(kind, diff.before)}
    return [hit for hit in _claims_in(kind, diff.after) if hit.lower() not in before]


# ---------------------------------------------------------------- evaluation


def _rule_fires(rule: Rule, path: str, diff: Diff | None) -> bool:
    if not match_any(path, rule.paths) or match_any(path, rule.exclude):
        return False
    if rule.content is None and rule.claims is None:
        return True
    diff = diff or Diff()
    if rule.content is not None:
        return any(rule.content.search(line) for line in (*diff.added, *diff.removed))
    return bool(net_new_claims(rule.claims, diff))


def _record_slug(path: str, records_root: str) -> str | None:
    parts = PurePosixPath(path).parts
    root = PurePosixPath(records_root).parts
    if len(parts) > len(root) + 1 and parts[: len(root)] == root:
        return parts[len(root)]
    return None


def _max_mode(*modes: str) -> str:
    return max(modes, key=lambda mode: RANK[mode]) if modes else "none"


def _human_approvers(approvals: list[dict], pr_author: str | None, bots: tuple[str, ...]) -> list[str]:
    """Logins with an APPROVED review who are neither the PR author nor a bot identity."""

    latest: dict[str, str] = {}
    for review in approvals:
        login = str((review.get("user") or {}).get("login") or review.get("login") or "")
        state = str(review.get("state", "")).upper()
        if login and state in {"APPROVED", "CHANGES_REQUESTED", "DISMISSED"}:
            latest[login] = state
    excluded = {pr_author.lower()} if pr_author else set()
    excluded |= {bot.lower() for bot in bots}
    return sorted(login for login, state in latest.items()
                  if state == "APPROVED" and login.lower() not in excluded and not login.lower().endswith("[bot]"))


def _policy_overrides(packet: Path) -> list[str]:
    """Rule ids listed under a `## Policy override` heading in the packet's risk.md."""

    risk = packet / "risk.md"
    if not risk.is_file():
        return []
    match = re.search(r"^##\s*Policy override\s*$([\s\S]*?)(?=^##\s|\Z)", risk.read_text(encoding="utf-8"),
                      re.MULTILINE | re.IGNORECASE)
    if not match:
        return []
    return re.findall(r"\*\*Rule:\*\*\s*`?([A-Za-z0-9_.+-]+)`?", match.group(1))


def _names_path(risk_text: str, path: str) -> bool:
    """True when risk.md names ``path``: exactly, by a parent directory, or by a glob."""

    if path in risk_text:
        return True
    parts = PurePosixPath(path).parts
    for index in range(1, len(parts)):
        if "/".join(parts[:index]) + "/" in risk_text:
            return True
    for token in re.findall(r"`([^`\s]+)`", risk_text):
        if ("*" in token or "?" in token) and glob_regex(token).match(path):
            return True
    return False


def _dependency_lane(policy: Policy, pr_author: str | None, changes: dict[str, str],
                     lines: dict[str, Diff]) -> bool:
    """A bot dependency PR that only moves version pins or action SHAs."""

    if not pr_author or pr_author not in policy.dependency_lane_authors or not changes:
        return False
    for path, status in changes.items():
        if status != "M" or not match_any(path, policy.dependency_lane_paths):
            return False
        diff = lines.get(path, Diff())
        added, removed = diff.added, diff.removed
        # Once versions and SHAs are masked, the changed lines must be identical: the diff
        # may move pins, nothing else (no new package, step, or option).
        if not added or sorted(map(_mask_pins, added)) != sorted(map(_mask_pins, removed)):
            return False
    return True


def _mask_pins(line: str) -> str:
    return _VERSION_SPEC.sub("<v>", _SHA.sub("<sha>", line)).strip()


def evaluate(
    repo: Path,
    base: str,
    head: str | None,
    policy: Policy,
    *,
    head_policy_text: str | None = None,
    base_policy_text: str | None = None,
    approvals: list[dict] | None = None,
    pr_author: str | None = None,
) -> dict:
    """Evaluate a diff against a policy and return the receipt (a JSON-ready dict)."""

    changes, lines, results, new_slugs, skills = classify(repo, base, head, policy)
    root = policy.records_root
    rule_by_id = {rule.id: rule for rule in policy.rules}
    _evaluate_policy_self(results, base_policy_text, head_policy_text)
    return _cover(repo, base, head, policy, changes, lines, results, new_slugs, skills, rule_by_id, root,
                  approvals, pr_author)


def classify(repo: Path, base: str, head: str | None, policy: Policy):
    """Per-path requirements for a diff, before any coverage or approval is considered.

    Returns (changes, lines, results, new_record_slugs, skills). Backtests use this
    directly so that historical commits are classified without reading today's records.
    """

    changes = changed_paths(repo, base, head)
    lines = {path: diff_lines(repo, base, head, path, status) for path, status in changes.items()}
    root = policy.records_root
    results: dict[str, PathResult] = {}
    skills: set[str] = set()

    new_slugs: set[str] = set()
    for path in changes:
        slug = _record_slug(path, root)
        if slug and not _tracked_at(repo, base, f"{root}/{slug}"):
            new_slugs.add(slug)

    for path, status in sorted(changes.items()):
        fired: list[str] = []
        required = policy.default
        slug = _record_slug(path, root)
        if slug and slug in new_slugs:
            required = "none"
        elif slug:
            required = policy.record_delete_mode if status == "D" else policy.record_edit_mode
            fired.append("record-delete" if status == "D" else "record-edit")
        for rule in policy.rules:
            if _rule_fires(rule, path, lines.get(path)):
                fired.append(rule.id)
                required = _max_mode(required, rule.mode)
                skills.update(rule.skills)
        results[path] = PathResult(path, status, required, fired)
    return changes, lines, results, new_slugs, skills


def _evaluate_policy_self(results: dict[str, PathResult], base_text: str | None, head_text: str | None) -> None:
    # Built-in, not removable by the policy: changing the policy itself needs the top mode.
    if head_text != base_text and (head_text is not None or base_text is not None):
        entry = results.setdefault(POLICY_PATH, PathResult(POLICY_PATH, "M", "none"))
        entry.required = "standard+authority"
        entry.rules.append("policy-self")


def _cover(repo, base, head, policy, changes, lines, results, new_slugs, skills, rule_by_id, root,
           approvals, pr_author) -> dict:
    approvers = _human_approvers(approvals or [], pr_author, policy.bot_identities)
    failures: list[str] = []
    overrides_used: list[dict] = []
    lane = _dependency_lane(policy, pr_author, changes, lines)

    # Candidate cover: records added in this diff, open, with a declared mode.
    packets: list[dict] = []
    for slug in sorted(new_slugs):
        packet = repo / root / slug
        if not packet.is_dir():
            continue
        text = "\n".join(md.read_text(encoding="utf-8") for md in sorted(packet.glob("*.md")))
        risk_path = packet / "risk.md"
        risk_text = risk_path.read_text(encoding="utf-8") if risk_path.is_file() else ""
        match = MODE_DECLARATION_PATTERN.search(risk_text)
        declared = match.group(1).lower() if match else "unspecified"
        packets.append({
            "slug": slug, "path": f"{root}/{slug}", "closed": has_closure_note(text),
            "declared_mode": declared, "rank_mode": DECLARED_RANK.get(declared, "none"),
            "risk_text": risk_text, "overrides": _policy_overrides(packet), "validations": {},
        })

    def validation(packet: dict, mode: str) -> tuple[bool, list[str]]:
        custody = RANK[mode] >= RANK["standard"]
        authority = mode == "standard+authority"
        key = f"custody={custody},authority={authority}"
        if key not in packet["validations"]:
            result = validate_packet(repo / packet["path"], require_custody=custody, require_authority=authority)
            packet["validations"][key] = (result.ok, result.messages)
        return packet["validations"][key]

    for entry in results.values():
        if entry.required == "none":
            continue
        if lane:
            entry.covered_by.append("dependency-lane")
            continue
        required = entry.required
        # An override lowers an overridable rule's requirement to Quick, never to none.
        overridden = sorted({rule_id for packet in packets if not packet["closed"] for rule_id in packet["overrides"]})
        fired_rules = [rule_by_id[r] for r in entry.rules if r in rule_by_id]
        if fired_rules and overridden:
            remaining = [r.mode for r in fired_rules if not (r.id in overridden and r.overridable)]
            builtin = [policy.record_edit_mode for r in entry.rules if r == "record-edit"]
            builtin += [policy.record_delete_mode for r in entry.rules if r == "record-delete"]
            builtin += ["standard+authority" for r in entry.rules if r == "policy-self"]
            lowered = _max_mode("quick", *remaining, *builtin)
            if RANK[lowered] < RANK[required]:
                used = [r.id for r in fired_rules if r.id in overridden and r.overridable]
                overrides_used.append({"path": entry.path, "rules": used, "from": required, "to": lowered,
                                       "approved_by": approvers})
                required = lowered
            for rule_id in overridden:
                rule = rule_by_id.get(rule_id)
                if rule is not None and rule.id in entry.rules and not rule.overridable:
                    failures.append(f"{entry.path}: rule {rule.id} is not overridable")
        # The "+authority" is the strict authority validation and the human approval, so a
        # declared Standard record is eligible; validation below applies the stricter flags.
        eligible = "standard" if required == "standard+authority" else required
        for packet in packets:
            if packet["closed"] or RANK[packet["rank_mode"]] < RANK[eligible]:
                continue
            if not _names_path(packet["risk_text"], entry.path):
                continue
            ok, _ = validation(packet, required)
            if ok:
                entry.covered_by.append(packet["path"])
        if not entry.covered_by:
            failures.append(f"{entry.path}: requires {required} ({', '.join(entry.rules) or 'default'}); "
                            "no change record added in this diff covers it")
        entry.required = required

    required_mode = _max_mode(*(entry.required for entry in results.values()))
    needs_human = required_mode == "standard+authority" or lane or bool(overrides_used)
    if needs_human and not approvers:
        why = ("dependency lane" if lane else "standard+authority" if required_mode == "standard+authority"
               else "policy override")
        failures.append(f"{why}: needs an APPROVED review from a human account other than the PR author "
                        "and the bot identities (none found)")

    if required_mode == "none" and not failures:
        verdict = "pass-floor"
    else:
        verdict = "fail" if failures else "pass"
    for packet in packets:
        packet.pop("risk_text", None)
        packet["validations"] = {key: {"ok": ok, "messages": messages[:20]}
                                 for key, (ok, messages) in packet["validations"].items()}
    return {
        "schema": SCHEMA,
        "schema_version": SCHEMA_VERSION,
        "base": base,
        "head": head or WORKTREE,
        "policy": {"source": policy.source, "digest": policy.digest},
        "required_mode": required_mode,
        "verdict": verdict,
        "paths": [entry.__dict__ for entry in sorted(results.values(), key=lambda e: e.path)],
        "packets": packets,
        "approvals": {"human_approvers": approvers, "pr_author": pr_author, "dependency_lane": lane},
        "overrides": overrides_used,
        "skills": sorted(skills),
        "failures": failures,
        "boundary": BOUNDARY,
    }


def mode_table(policy: Policy) -> str:
    """Markdown table of the policy's rules, for docs that must not drift from it."""

    rows = ["| Rule | Minimum mode | Paths | Trigger | Overridable | Why |", "|---|---|---|---|---|---|"]
    for rule in sorted(policy.rules, key=lambda r: (-RANK[r.mode], r.id)):
        trigger = "content match" if rule.content else f"net-new {rule.claims} claim" if rule.claims else "any change"
        paths = ", ".join(f"`{p}`" for p in rule.paths)
        rows.append(f"| `{rule.id}` | {rule.mode} | {paths} | {trigger} | {'yes' if rule.overridable else 'no'} | "
                    f"{rule.reason} |")
    return "\n".join(rows)
