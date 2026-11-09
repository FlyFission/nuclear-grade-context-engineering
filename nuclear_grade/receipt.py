"""Machine-readable validation receipt for one change packet.

`ng validate <packet> --json` prints this receipt instead of the OK/FAILED lines.
It binds the structural verdict to the exact bytes that were checked (a SHA-256
per packet file plus one digest over the set), to the repository commit and
working-tree state, and to the validator and interpreter versions, so a later
reader or an out-of-band rerun can tell whether it is looking at the same
evidence. It also counts the evidence statuses declared in status columns, so a
structurally passing packet that still carries open gaps is not mistaken for a
gap-free one.

Schema version 2 adds an ``acceptance`` block that keeps different propositions
apart instead of collapsing them into one pass/fail: record structure, evidence
status, per-row claim support, which declared-independence checks ran, release
eligibility, whether an authorized decision is recorded, and whether permission to
apply is recorded. There is deliberately no overall "trusted" boolean. The
validator cannot authenticate a decision or an apply permission, so those two
always read ``not_assessed``; release eligibility can say ``blocked`` or
``undetermined`` or "open to a decision", and never "approved". ``ok`` keeps its
old meaning (record structure only).

``verify_receipt`` checks a stored receipt against the packet as it is now, so a
receipt for other bytes, or from another commit, reads ``stale`` and not ``bound``.
``read_acceptance`` reads any receipt and treats a version 1 receipt as
``undetermined``, never as eligible.

The receipt is integrity and provenance metadata about a structural check. It
does not prove the evidence is adequate, independent, or true, and it is not a
signature: anyone who can edit the packet can regenerate it.
"""

from __future__ import annotations

import hashlib
import json
import platform
import re
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from nuclear_grade.ng_validate import (
    EVIDENCE_STATUSES,
    QUICK_MODE,
    STANDARD_MODE,
    UNSPECIFIED_MODE,
    ValidationResult,
    _declared_mode,
    _detect_mode,
    _markdown_tables,
    _normalize_table_label,
    validate_packet,
)
from nuclear_grade.propagation import (
    check_promotion,
    claim_id,
    effective_status,
    parse_claim_statuses,
)

RECEIPT_SCHEMA = "nuclear-grade.validation-receipt"
RECEIPT_SCHEMA_VERSION = 2
ACCEPTANCE_CONTRACT = "nuclear-grade.acceptance/1"
NOT_ASSESSED = "not_assessed"
OPEN_STATUSES = ("fail", "gap", "deferred", "planned")
BOUNDARY = (
    "Structural check only. The digests show which bytes were checked; they do not show the "
    "evidence is adequate, independent, or true, and this receipt is not a signature."
)
ACCEPTANCE_NOTE = (
    "A positive structural result is not approval. Release eligibility only says whether recorded "
    "evidence leaves the change open to a human decision; the validator does not authenticate "
    "who decides or who may apply."
)
_GIT_TIMEOUT_SECONDS = 5
# A negated status ("no gap", "not planned") declares nothing.
_STATUS_TOKEN = re.compile(
    r"(?<!\bno )(?<!\bnot )\b(not applicable|pass|fail|gap|deferred|planned)\b", re.IGNORECASE
)
_STATUS_DECLARATION = re.compile(
    r"\bstatus\**[ \t]*:\**[ \t]*(?P<value>`?(not applicable|pass|fail|gap|deferred|planned)\b[^\n]*)",
    re.IGNORECASE,
)
# Parenthetical notes explain a status ("not applicable (no release planned)"); they declare none.
_PARENTHETICAL = re.compile(r"\([^()]*\)")
# A declared value ends where its explanation starts: an em dash, " -- ", " - ", or a sentence stop.
_DECLARATION_END = re.compile(r"\s+(—|--?)\s|—|\.(\s|$)")
# An unfilled choice list is not a declaration: "pass / fail / gap" or "`pass`, `fail`, `gap`, ...".
_STATUS_WORD = r"`?\b(?:pass|fail|gap|deferred|planned|not applicable)\b`?"
_CHOICE_LIST = re.compile(
    rf"\b(?:pass|fail|gap|deferred|planned|not applicable)\b`?\s*/\s*\w"
    rf"|{_STATUS_WORD}\s*,\s*{_STATUS_WORD}\s*,\s*(?:or\s+)?{_STATUS_WORD}",
    re.IGNORECASE,
)


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _packet_files(packet: Path) -> list[dict[str, str]]:
    if not packet.is_dir():
        return []
    files = []
    for path in sorted(p for p in packet.rglob("*") if p.is_file()):
        files.append(
            {
                "path": path.relative_to(packet).as_posix(),
                "sha256": _sha256_bytes(path.read_bytes()),
            }
        )
    return files


def _set_digest(files: list[dict[str, str]]) -> str:
    canonical = json.dumps(files, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return _sha256_bytes(canonical.encode("utf-8"))


def _git(packet: Path, *args: str) -> str | None:
    cwd = packet if packet.is_dir() else packet.parent
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
            timeout=_GIT_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout.strip()


def _git_state(packet: Path) -> dict[str, Any]:
    commit = _git(packet, "rev-parse", "HEAD")
    if commit is None:
        return {"commit": None, "packet_dirty": None}
    # Dirty is scoped to the packet: unrelated edits elsewhere do not change what was checked.
    porcelain = _git(packet, "status", "--porcelain", "--untracked-files=all", "--", ".")
    return {"commit": commit, "packet_dirty": None if porcelain is None else bool(porcelain)}


def _is_result_column(header: str) -> bool:
    # "Result", "Test result", "Outcome" often carry the status ("planned (CI)") instead of a
    # Status column. They also carry prose, so only a cell that opens with a status counts.
    return "status" not in header and (header in ("result", "outcome") or header.endswith((" result", " outcome")))


def _status_counts(packet: Path, mode: str) -> dict[str, int]:
    counts = dict.fromkeys(EVIDENCE_STATUSES, 0)
    if mode == UNSPECIFIED_MODE:
        return counts
    evidence_file = packet / ("proof.md" if mode == QUICK_MODE else "verification.md")
    if not evidence_file.is_file():
        return counts
    text = evidence_file.read_text(encoding="utf-8")
    # Statuses are also declared inline, as Quick bullets (`- Status: gap`) or mid-sentence
    # (`... Status: deferred — ...`). An unfilled template (`pass / fail / gap`) is not counted.
    # Table rows are counted by the table pass below; scan only prose lines here so a
    # `Status: gap` inside a cell is not counted twice.
    prose = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("|"))
    for match in _STATUS_DECLARATION.finditer(prose):
        # "Status: pass (local); gap (review pending)" declares two statuses, like a table cell.
        value = _PARENTHETICAL.sub(" ", _DECLARATION_END.split(match.group("value"), maxsplit=1)[0])
        if _CHOICE_LIST.search(value):
            continue
        for token in _STATUS_TOKEN.finditer(value):
            counts[token.group(1).lower()] += 1
    for headers, rows in _markdown_tables(text):
        labels = [_normalize_table_label(header) for header in headers]
        status_columns = [i for i, label in enumerate(labels) if "status" in label]
        result_columns = [i for i, label in enumerate(labels) if _is_result_column(label)]
        for row in rows:
            for column in status_columns + result_columns:
                if column >= len(row):
                    continue
                # A cell may declare several statuses: "pass (local); gap (review pending)".
                # A template choice list ("pass / fail / gap") is not a declaration.
                if _CHOICE_LIST.search(row[column]):
                    continue
                # The explanation after a dash or sentence stop declares nothing ("pass — prior gap
                # is closed"); a composite joined by ";" stays whole.
                raw = _DECLARATION_END.split(row[column].strip(), maxsplit=1)[0]
                if column in result_columns and not _STATUS_TOKEN.match(_normalize_table_label(raw)):
                    continue
                cell = _normalize_table_label(_PARENTHETICAL.sub(" ", raw))
                for match in _STATUS_TOKEN.finditer(cell):
                    counts[match.group(1).lower()] += 1
    return counts


def _declared_claim_ids(packet: Path) -> list[str]:
    """Claim ids a Standard packet declares under basis.md "Derived requirements or claims"."""
    basis = packet / "basis.md"
    if not basis.is_file():
        return []
    in_section = False
    ids: list[str] = []
    for line in basis.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            in_section = "derived requirements or claims" in line.lower()
            continue
        if in_section and line.lstrip().startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            declared = claim_id(cells[0]) if cells else None
            if declared and declared not in ids:
                ids.append(declared)
    return ids


def _claim_support(packet: Path, mode: str) -> dict[str, Any]:
    """Per-row status from verification.md. Not a score: a row is evidence status, not truth."""
    if mode != STANDARD_MODE:
        return {"state": "not_applicable", "rows": []}
    verification = packet / "verification.md"
    rows: list[tuple[str, str]] = []
    advisory: list[str] = []
    if verification.is_file():
        rows = parse_claim_statuses(verification.read_text(encoding="utf-8"))
        check_promotion(packet, advisory)
    seen = {row_id for row_id, _ in rows}
    return {
        "state": "recognized" if rows else "unrecognized",
        "rows": [{"id": row_id, "status": status} for row_id, status in rows],
        "weakest_status": effective_status([status for _, status in rows]) if rows else None,
        "declared_without_verification_row": [i for i in _declared_claim_ids(packet) if i not in seen],
        "propagation_advisories": advisory,
    }


def _release_eligibility(
    result: ValidationResult, mode: str, statuses: dict[str, int], support: dict[str, Any]
) -> dict[str, Any]:
    blocked: list[str] = []
    undetermined: list[str] = []
    if not result.ok:
        blocked.append("record structure is invalid")
    if mode == UNSPECIFIED_MODE:
        undetermined.append("the packet mode could not be determined")
    for status in ("fail", "gap", "planned"):
        if statuses.get(status):
            blocked.append(f"{statuses[status]} evidence item(s) declared '{status}'")
    if support["state"] == "unrecognized":
        undetermined.append("no claim-to-evidence rows keyed by claim id were recognized in verification.md")
    if support["state"] == "recognized":
        for missing in support.get("declared_without_verification_row", []):
            blocked.append(f"claim {missing} is declared in basis.md but has no verification row")
    if blocked:
        state, reasons = "blocked", blocked + undetermined
    elif undetermined:
        state, reasons = "undetermined", undetermined
    elif statuses.get("deferred"):
        state = "open_to_decision_with_open_items"
        reasons = [f"{statuses['deferred']} evidence item(s) deferred; a human decides whether that is acceptable"]
    else:
        state, reasons = "open_to_decision", []
    return {"state": state, "reasons": reasons}


def build_acceptance(
    packet: Path,
    result: ValidationResult,
    mode: str,
    statuses: dict[str, int],
    *,
    strict_custody: bool,
    strict_authority: bool,
    strict_two_party: bool,
) -> dict[str, Any]:
    """Typed acceptance propositions. Each one is separate; none implies another."""
    support = _claim_support(packet, mode)
    open_items = sum(statuses[status] for status in OPEN_STATUSES)
    return {
        "contract": ACCEPTANCE_CONTRACT,
        "structural_validity": {"state": "valid" if result.ok else "invalid", "scope": "record structure only"},
        "evidence_integrity": {"state": "digests_recorded", "verify_with": "ng validate --verify-receipt"},
        "evidence_status": {"state": "open" if open_items else "complete", "open_items": open_items},
        "claim_support": support,
        "independence": {
            "state": "declared_checks_run"
            if (strict_custody or strict_authority or strict_two_party)
            else "not_checked",
            "checks": {
                "custody": strict_custody,
                "authority": strict_authority,
                "two_party": strict_two_party,
            },
            "note": "Declared identities and coupling only; not proof of independence.",
        },
        "release_eligibility": _release_eligibility(result, mode, statuses, support),
        "authorized_decision": {"state": NOT_ASSESSED},
        "apply_permission": {"state": NOT_ASSESSED},
        "note": ACCEPTANCE_NOTE,
    }


def read_acceptance(receipt: dict[str, Any]) -> dict[str, Any]:
    """The acceptance block of any receipt. A version 1 or malformed receipt is never eligible."""
    block = receipt.get("acceptance") if isinstance(receipt, dict) else None
    if (
        isinstance(block, dict)
        and block.get("contract") == ACCEPTANCE_CONTRACT
        and isinstance(block.get("release_eligibility"), dict)
    ):
        return block
    return {
        "contract": None,
        "release_eligibility": {
            "state": "undetermined",
            "reasons": ["the receipt predates or lacks the acceptance contract"],
        },
        "authorized_decision": {"state": NOT_ASSESSED},
        "apply_permission": {"state": NOT_ASSESSED},
    }


def is_open_to_decision(receipt: dict[str, Any]) -> bool:
    return read_acceptance(receipt)["release_eligibility"].get("state", "").startswith("open_to_decision")


def acceptance_summary(acceptance: dict[str, Any]) -> str:
    """One line a person or a client reads instead of a bare ok."""
    eligibility = acceptance["release_eligibility"]
    parts = [
        f"structure {acceptance['structural_validity']['state']}",
        f"evidence {acceptance['evidence_status']['state']}"
        + (f" ({acceptance['evidence_status']['open_items']} open)" if acceptance["evidence_status"]["open_items"] else ""),
        f"release eligibility {eligibility['state'].replace('_', ' ')}",
        "decision and apply permission not assessed",
    ]
    line = "Acceptance: " + "; ".join(parts) + ". Not an approval."
    reasons = eligibility.get("reasons") or []
    return line + "".join(f"\n  - {reason}" for reason in reasons)


def verify_receipt(
    receipt: dict[str, Any], packet: Path, *, expected_commit: str | None = None
) -> dict[str, Any]:
    """Check a stored receipt against the packet as it is now.

    ``bound``: the receipt describes these exact bytes (and the named commit, if given).
    ``stale``: it describes other bytes or another commit. ``invalid``: it is not a receipt
    or contradicts itself. A ``bound`` result shows which bytes were checked; it does not
    show they were adequate, and anyone who can edit the packet can regenerate a receipt.
    """
    reasons: list[str] = []
    if not isinstance(receipt, dict) or receipt.get("schema") != RECEIPT_SCHEMA:
        return {"state": "invalid", "reasons": ["not a nuclear-grade validation receipt"], "checked": []}
    inputs = receipt.get("inputs")
    recorded = inputs.get("files") if isinstance(inputs, dict) else None
    digest = inputs.get("digest") if isinstance(inputs, dict) else None
    if not isinstance(recorded, list) or not all(
        isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("sha256"), str)
        for item in recorded
    ):
        return {"state": "invalid", "reasons": ["receipt inputs are missing or malformed"], "checked": []}
    checked = ["inputs.files", "inputs.digest"]
    if _set_digest(recorded) != digest:
        return {
            "state": "invalid",
            "reasons": ["receipt digest does not match its own file list; it was edited after it was issued"],
            "checked": checked,
        }
    current = {item["path"]: item["sha256"] for item in _packet_files(packet)}
    previous = {item["path"]: item["sha256"] for item in recorded}
    for path in sorted(previous.keys() - current.keys()):
        reasons.append(f"{path} was in the receipt and is no longer in the packet")
    for path in sorted(current.keys() - previous.keys()):
        reasons.append(f"{path} is in the packet and was not in the receipt")
    for path in sorted(previous.keys() & current.keys()):
        if previous[path] != current[path]:
            reasons.append(f"{path} changed after the receipt was issued")
    if expected_commit is not None:
        checked.append("provenance.git.commit")
        provenance = receipt.get("provenance")
        git = provenance.get("git") if isinstance(provenance, dict) else None
        recorded_commit = git.get("commit") if isinstance(git, dict) else None
        if recorded_commit != expected_commit:
            reasons.append(
                f"receipt was issued at commit {recorded_commit or 'unknown'}, not {expected_commit}"
            )
    if reasons:
        return {"state": "stale", "reasons": reasons, "checked": checked}
    # The bytes match. The acceptance block sits outside the digest, so recompute it from these
    # bytes and the strict flags the receipt records, and refuse a block someone edited.
    block = receipt.get("acceptance")
    if isinstance(block, dict):
        checked.append("acceptance")
        strict = receipt.get("strict") if isinstance(receipt.get("strict"), dict) else {}
        fresh = validate_packet(
            packet,
            require_custody=bool(strict.get("custody")),
            require_authority=bool(strict.get("authority")),
            require_two_party=bool(strict.get("two_party")),
            before_review=bool(receipt.get("before_review")),
        )
        mode = _effective_mode(packet)
        expected = build_acceptance(
            packet,
            fresh,
            mode,
            _status_counts(packet, mode),
            strict_custody=bool(strict.get("custody")),
            strict_authority=bool(strict.get("authority")),
            strict_two_party=bool(strict.get("two_party")),
        )
        for key in ("structural_validity", "evidence_status", "release_eligibility"):
            if block.get(key) != expected[key]:
                return {
                    "state": "invalid",
                    "reasons": [f"acceptance.{key} does not match what these bytes yield; the block was edited"],
                    "checked": checked,
                }
    return {"state": "bound", "reasons": [], "checked": checked}


def _effective_mode(packet: Path) -> str:
    if not packet.is_dir():
        return UNSPECIFIED_MODE
    detected = _detect_mode(packet)
    return detected if detected != UNSPECIFIED_MODE else _declared_mode(packet)


def build_receipt(
    packet: Path,
    result: ValidationResult,
    *,
    strict_custody: bool,
    strict_authority: bool,
    strict_two_party: bool = False,
    validator_version: str,
    now: datetime | None = None,
) -> dict[str, Any]:
    mode = _effective_mode(packet)
    files = _packet_files(packet)
    statuses = _status_counts(packet, mode)
    return {
        "schema": RECEIPT_SCHEMA,
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "generated_at": (now or datetime.now(UTC)).isoformat(timespec="seconds"),
        "packet": str(packet),
        "mode": mode if mode in (QUICK_MODE, STANDARD_MODE) else None,
        "ok": result.ok,
        "ok_scope": "record structure only; see acceptance for release eligibility",
        "messages": list(result.messages),
        "strict": {
            "custody": strict_custody,
            "authority": strict_authority,
            "two_party": strict_two_party,
        },
        "evidence_statuses": statuses,
        "open_evidence_items": sum(statuses[status] for status in OPEN_STATUSES),
        "acceptance": build_acceptance(
            packet,
            result,
            mode,
            statuses,
            strict_custody=strict_custody,
            strict_authority=strict_authority,
            strict_two_party=strict_two_party,
        ),
        "inputs": {"algorithm": "sha256", "files": files, "digest": _set_digest(files)},
        "provenance": {
            "validator_version": validator_version or None,
            "python_version": platform.python_version(),
            "git": _git_state(packet),
        },
        "boundary": BOUNDARY,
    }
