"""Machine-readable validation receipt for one change packet.

`ng validate <packet> --json` prints this receipt instead of the OK/FAILED lines.
It binds the structural verdict to the exact bytes that were checked (a SHA-256
per packet file plus one digest over the set), to the repository commit and
working-tree state, and to the validator and interpreter versions, so a later
reader or an out-of-band rerun can tell whether it is looking at the same
evidence. It also counts the evidence statuses declared in status columns, so a
structurally passing packet that still carries open gaps is not mistaken for a
gap-free one.

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
)

RECEIPT_SCHEMA = "nuclear-grade.validation-receipt"
RECEIPT_SCHEMA_VERSION = 1
OPEN_STATUSES = ("fail", "gap", "deferred", "planned")
BOUNDARY = (
    "Structural check only. The digests show which bytes were checked; they do not show the "
    "evidence is adequate, independent, or true, and this receipt is not a signature."
)
_GIT_TIMEOUT_SECONDS = 5
_STATUS_TOKEN = re.compile(r"(?<!\bno )\b(not applicable|pass|fail|gap|deferred|planned)\b", re.IGNORECASE)
_STATUS_DECLARATION = re.compile(
    r"\bstatus\**[ \t]*:\**[ \t]*`?(not applicable|pass|fail|gap|deferred|planned)\b`?(?![ \t]*/)",
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
    for match in _STATUS_DECLARATION.finditer(text):
        value = _normalize_table_label(match.group(1))
        if value in counts:
            counts[value] += 1
    for headers, rows in _markdown_tables(text):
        columns = [i for i, header in enumerate(headers) if "status" in _normalize_table_label(header)]
        for row in rows:
            for column in columns:
                if column >= len(row):
                    continue
                # A cell may declare several statuses: "pass (local); gap (review pending)".
                # A template choice list ("pass / fail / gap") is not a declaration.
                cell = _normalize_table_label(row[column])
                if re.search(r"\b(pass|fail|gap|deferred|planned)\b\s*/\s*\w", row[column], re.IGNORECASE):
                    continue
                for match in _STATUS_TOKEN.finditer(cell):
                    counts[match.group(1).lower()] += 1
    return counts


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
        "messages": list(result.messages),
        "strict": {"custody": strict_custody, "authority": strict_authority},
        "evidence_statuses": statuses,
        "open_evidence_items": sum(statuses[status] for status in OPEN_STATUSES),
        "inputs": {"algorithm": "sha256", "files": files, "digest": _set_digest(files)},
        "provenance": {
            "validator_version": validator_version or None,
            "python_version": platform.python_version(),
            "git": _git_state(packet),
        },
        "boundary": BOUNDARY,
    }
