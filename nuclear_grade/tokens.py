"""Token-cost audit for Nuclear-grade skills, commands, templates, and docs.

What this measures
------------------
The token weight the repo's own prose carries, separated into the two costs an
agent actually pays:

- **always-loaded** -- a skill's frontmatter ``description``, which a routing
  agent reads for every skill whether or not the skill fires; and
- **on-invocation** -- a skill's body, read only when that one skill is selected.

It also reports a **redundancy index** (identical boilerplate blocks and how many
files each spans) and **tokens-per-decision-signal** for skills that back a worked
example, by joining onto the ``ng eval`` efficacy harness. Together these turn
"the skills feel bloated / already lean" into measured numbers, and back a CI
gate so the cost cannot silently regress.

What this does NOT measure
--------------------------
Whether a skill is correct, useful, or worth its tokens in judgment terms. A high
token count is not proof of waste, and a low one is not proof of value; the audit
reports cost so a human can weigh it against the decision signals the artifact
covers. The counter is a deterministic approximation, not a model tokenizer (see
``count_tokens``); use ``tiktoken_count`` for an optional accuracy cross-check.

Design constraints
------------------
Stdlib-only and deterministic: the same text yields the same count on CI (which
installs only pytest + ruff) and on every developer machine, so the gate is
reproducible rather than dependent on an optional package.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# --- Deterministic, dependency-free token counter --------------------------------

# Segment text the way a byte-pair tokenizer roughly does: runs of letters, runs of
# digits, runs of symbols, and whitespace, kept separate. Stdlib ``re`` has no
# \p{L}, so [^\W\d_] stands in for "unicode letter" and \d for "digit".
_SEGMENT_RE = re.compile(r"[^\W\d_]+|\d+|\s+|[^\s\w]+", re.UNICODE)

# Average characters a BPE merge consumes, per segment kind. Letters merge into
# ~4-char subwords; digits and symbols tokenize finer. These are approximations,
# documented as such; what matters for the gate is that they are fixed.
_ALPHA_CHARS_PER_TOKEN = 4
_DIGIT_CHARS_PER_TOKEN = 3
_SYMBOL_CHARS_PER_TOKEN = 2


def _ceil_div(value: int, divisor: int) -> int:
    return -(-value // divisor)


def _read_text(path: Path) -> str:
    """Read a file and normalize line endings to ``\\n``.

    A CRLF checkout (e.g. Windows with ``core.autocrlf``) would otherwise leave
    ``\\r`` in the text, which both inflates symbol-token counts and breaks the
    ``---\\n`` frontmatter check -- making counts differ by platform. Normalizing
    on read keeps every count reproducible across the machines the gate supports.
    """

    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def count_tokens(text: str) -> int:
    """Estimate token count deterministically, without any third-party tokenizer.

    A byte-pair tokenizer splits text into subword pieces; this approximates that
    by segmenting into letter, digit, and symbol runs and dividing each by a fixed
    characters-per-token factor. It is intentionally not exact -- it is the
    *canonical* number the gate uses precisely because it is reproducible
    everywhere. ``tiktoken_count`` offers an exact cross-check when the optional
    package is installed.
    """

    total = 0
    for match in _SEGMENT_RE.finditer(text):
        segment = match.group()
        first = segment[0]
        if first.isspace():
            continue
        if first.isdigit():
            total += _ceil_div(len(segment), _DIGIT_CHARS_PER_TOKEN)
        elif segment.isalpha():
            total += _ceil_div(len(segment), _ALPHA_CHARS_PER_TOKEN)
        else:
            total += _ceil_div(len(segment), _SYMBOL_CHARS_PER_TOKEN)
    return total


def tiktoken_count(text: str, encoding: str = "o200k_base") -> int | None:
    """Exact token count via ``tiktoken`` when installed, else ``None``.

    Optional accuracy cross-check only. The gate never depends on this so that CI
    and developer machines produce identical numbers without an extra dependency.
    """

    try:
        import tiktoken  # type: ignore
    except ImportError:
        return None
    return len(tiktoken.get_encoding(encoding).encode(text))


# --- Frontmatter / body split ----------------------------------------------------


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return ``(description, body)`` for a skill file.

    ``description`` is the frontmatter ``description`` value (the always-loaded
    cost); ``body`` is everything after the closing ``---`` (the on-invocation
    cost). Files without frontmatter return ``("", whole-text)``.
    """

    if not text.startswith("---\n"):
        return "", text
    try:
        end = text.index("\n---", 4)
    except ValueError:
        return "", text
    front = text[4:end]
    body = text[end + len("\n---") :]
    description = ""
    for line in front.splitlines():
        if line.startswith("description:"):
            description = line.split(":", 1)[1].strip().strip('"')
            break
    return description, body


# --- Per-file measurement --------------------------------------------------------


@dataclass(frozen=True)
class FileTokens:
    """Token measurement for one prose file."""

    path: str  # repo-relative
    kind: str  # "skill" | "command" | "template" | "doc"
    name: str  # skill/command short name, or file name
    description_tokens: int  # always-loaded cost (skills only; 0 otherwise)
    body_tokens: int  # on-invocation cost
    total_tokens: int


# Directories of self-contained prose, by kind. Skill/command names are derived
# from the tree (never hardcoded) so the audit stays correct across renames and
# additions such as the 23rd skill.
def _iter_skill_files(root: Path):
    yield from sorted((root / "skills").glob("*/SKILL.md"))


def _iter_command_files(root: Path):
    yield from sorted((root / "commands").glob("*.md"))


def _iter_template_files(root: Path):
    yield from sorted((root / "templates").rglob("*.md"))


def _iter_doc_files(root: Path):
    """Top-level docs plus the full ``docs/`` tree (deduplicated, sorted).

    Recurses ``docs/`` so reference pages an agent or reader actually opens --
    including ones this audit discusses by token count, e.g.
    ``docs/00-standards-foundation/core-source-rationale.md`` -- are measured,
    not silently excluded from "All measured prose".
    """

    seen = set()
    for path in sorted([*root.glob("*.md"), *(root / "docs").rglob("*.md")]):
        if path not in seen:
            seen.add(path)
            yield path


def measure_file(path: Path, root: Path, kind: str) -> FileTokens:
    text = _read_text(path)
    rel = path.relative_to(root).as_posix()
    if kind == "skill":
        description, body = split_frontmatter(text)
        name = path.parent.name
        desc_tokens = count_tokens(description)
        body_tokens = count_tokens(body)
    else:
        name = path.name
        desc_tokens = 0
        body_tokens = count_tokens(text)
    return FileTokens(
        path=rel,
        kind=kind,
        name=name,
        description_tokens=desc_tokens,
        body_tokens=body_tokens,
        total_tokens=desc_tokens + body_tokens,
    )


# --- Redundancy index ------------------------------------------------------------


def _normalize_block(block: str) -> str:
    """Collapse a block to a comparison key: lowercased, whitespace-squeezed."""

    return re.sub(r"\s+", " ", block.strip().lower())


def _strip_code_fences(text: str) -> str:
    """Remove fenced code blocks so redundancy targets prose, not shared snippets.

    A repeated ``ng validate`` command across verification sections is a legitimate
    shared reference, not boilerplate waste; only recurring prose is a finding.
    """

    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


@dataclass(frozen=True)
class RepeatedBlock:
    """A boilerplate paragraph that recurs near-identically across files."""

    excerpt: str
    files: tuple[str, ...]
    block_tokens: int

    @property
    def file_count(self) -> int:
        return len(self.files)

    @property
    def wasted_tokens(self) -> int:
        # Tokens spent on every copy after the first.
        return self.block_tokens * (self.file_count - 1)


def find_repeated_blocks(
    files: list[Path], root: Path, *, min_tokens: int = 12, min_files: int = 3
) -> list[RepeatedBlock]:
    """Find paragraph-sized blocks repeated near-identically across ``files``.

    Splits each file on blank lines, normalizes each block, and reports blocks of
    at least ``min_tokens`` that appear in at least ``min_files`` distinct files --
    the source-lineage notes and "does not create ..." disclaimers surface here as
    hard counts rather than estimates.
    """

    seen: dict[str, set[str]] = {}
    sample: dict[str, str] = {}
    for path in files:
        rel = path.relative_to(root).as_posix()
        prose = _strip_code_fences(_read_text(path))
        for raw_block in re.split(r"\n\s*\n", prose):
            block = raw_block.strip()
            if count_tokens(block) < min_tokens:
                continue
            key = _normalize_block(block)
            seen.setdefault(key, set()).add(rel)
            sample.setdefault(key, block)

    blocks = [
        RepeatedBlock(
            excerpt=" ".join(sample[key].split())[:120],
            files=tuple(sorted(files_set)),
            block_tokens=count_tokens(sample[key]),
        )
        for key, files_set in seen.items()
        if len(files_set) >= min_files
    ]
    blocks.sort(key=lambda b: b.wasted_tokens, reverse=True)
    return blocks


def phrase_frequency(root: Path, fragment: str) -> tuple[int, int]:
    """Count occurrences of ``fragment`` across the markdown tree.

    Returns ``(total_occurrences, files_containing)``. The "does not create ..."
    assurance disclaimer recurs with varied surrounding wording, so a substring
    fragment captures the family that paragraph-hashing (which needs near-identical
    blocks) misses -- the cross-file repetition shows up here as a hard count.
    """

    fragment_l = fragment.lower()
    total = 0
    files = 0
    for path in sorted(root.rglob("*.md")):
        text = _read_text(path).lower()
        count = text.count(fragment_l)
        if count:
            total += count
            files += 1
    return total, files


# --- Cost per decision signal ----------------------------------------------------


@dataclass(frozen=True)
class Report:
    files: list[FileTokens] = field(default_factory=list)
    repeated_blocks: list[RepeatedBlock] = field(default_factory=list)

    def of_kind(self, kind: str) -> list[FileTokens]:
        return [f for f in self.files if f.kind == kind]

    @property
    def skill_description_total(self) -> int:
        return sum(f.description_tokens for f in self.of_kind("skill"))

    @property
    def skill_body_total(self) -> int:
        return sum(f.body_tokens for f in self.of_kind("skill"))

    @property
    def total(self) -> int:
        return sum(f.total_tokens for f in self.files)


def build_report(root: Path) -> Report:
    """Measure every prose surface under ``root`` and index repeated boilerplate."""

    files: list[FileTokens] = []
    for path in _iter_skill_files(root):
        files.append(measure_file(path, root, "skill"))
    for path in _iter_command_files(root):
        files.append(measure_file(path, root, "command"))
    for path in _iter_template_files(root):
        files.append(measure_file(path, root, "template"))
    for path in _iter_doc_files(root):
        files.append(measure_file(path, root, "doc"))

    # Redundancy is scanned across the self-contained prose corpus: skills,
    # commands, and docs (templates are intentionally repetitive form scaffolds).
    corpus = (
        list(_iter_skill_files(root))
        + list(_iter_command_files(root))
        + list(_iter_doc_files(root))
    )
    repeated = find_repeated_blocks(corpus, root)
    return Report(files=files, repeated_blocks=repeated)


def cost_per_signal(root: Path) -> dict[str, float]:
    """Map each worked-example artifact to body-tokens-per-decision-signal.

    Joins ``build_report`` onto the efficacy harness so "is the prose worth its
    tokens" gets an evidence-based answer. Artifacts that are not skills (most
    worked examples are trial records) are measured whole. Returns an empty dict
    when no eval cases are present.
    """

    from nuclear_grade.efficacy import run_all

    results = run_all(root)
    out: dict[str, float] = {}
    for result in results:
        artifact = root / result.case.artifact
        if not artifact.exists():
            continue
        tokens = count_tokens(_read_text(artifact))
        signals = result.total or 1
        out[result.case.id] = tokens / signals
    return out


# --- Budget gate -----------------------------------------------------------------

# Default budgets, overridable from nuclear-grade.yaml `token_budgets:`. Seeded
# from the measured baseline with headroom so the gate starts green and only fires
# on genuine regression, not on ordinary edits. Kept in step with the catalog so
# the defaults remain a true safety net if a key is dropped.
# Skill bodies now carry a `## Prompt` section (commands are generated from it), so
# the measured skill-body max is 3239 (organizing-project-folders); skill_body_max
# sits above it. Earlier basis, pre-single-sourcing: desc 138, skill body 2489,
# command 1295.
DEFAULT_BUDGETS = {
    "description_max": 200,
    "skill_body_max": 3600,
    "command_max": 1600,
    "repeated_block_max_files": 8,
}


def load_budgets(root: Path) -> dict[str, int]:
    """Read `token_budgets:` from nuclear-grade.yaml, falling back to defaults.

    Parsed with a tiny stdlib reader (the repo carries no YAML dependency); only
    the flat integer keys under ``token_budgets:`` are read.
    """

    budgets = dict(DEFAULT_BUDGETS)
    catalog = root / "nuclear-grade.yaml"
    if not catalog.exists():
        return budgets
    in_block = False
    for line in _read_text(catalog).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            in_block = line.strip() == "token_budgets:"
            continue
        if in_block and ":" in line:
            key, _, value = line.strip().partition(":")
            value = value.strip()
            if value.lstrip("-").isdigit():
                budgets[key.strip()] = int(value)
    return budgets


def check_budgets(report: Report, budgets: dict[str, int]) -> list[str]:
    """Return human-readable budget violations; empty means the gate passes."""

    violations: list[str] = []
    for skill in report.of_kind("skill"):
        if skill.description_tokens > budgets["description_max"]:
            violations.append(
                f"{skill.path}: description {skill.description_tokens} tokens "
                f"> description_max {budgets['description_max']}"
            )
        if skill.body_tokens > budgets["skill_body_max"]:
            violations.append(
                f"{skill.path}: body {skill.body_tokens} tokens "
                f"> skill_body_max {budgets['skill_body_max']}"
            )
    for command in report.of_kind("command"):
        if command.body_tokens > budgets["command_max"]:
            violations.append(
                f"{command.path}: {command.body_tokens} tokens "
                f"> command_max {budgets['command_max']}"
            )
    for block in report.repeated_blocks:
        if block.file_count > budgets["repeated_block_max_files"]:
            violations.append(
                f"boilerplate repeated in {block.file_count} files "
                f"> repeated_block_max_files {budgets['repeated_block_max_files']}: "
                f"\"{block.excerpt[:60]}...\""
            )
    return violations
