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
    _markdown_h2_sections,
    _markdown_tables,
    _normalize_table_label,
    validate_packet,
)
from nuclear_grade.propagation import (
    check_promotion,
    claim_id,
    effective_status,
)

RECEIPT_SCHEMA = "nuclear-grade.validation-receipt"
RECEIPT_SCHEMA_VERSION = 2
SUPPORTED_RECEIPT_VERSIONS = (1, RECEIPT_SCHEMA_VERSION)
ACCEPTANCE_CONTRACT = "nuclear-grade.acceptance/1"
NOT_ASSESSED = "not_assessed"
ELIGIBLE_STATES = ("open_to_decision", "open_to_decision_with_open_items")
ELIGIBILITY_STATES = ("blocked", "undetermined", *ELIGIBLE_STATES)
OPEN_STATUSES = ("fail", "gap", "deferred", "planned")
BOUNDARY = (
    "Structural check only. The digests show which bytes were checked; they do not show the "
    "evidence is adequate, independent, or true, and this receipt is not a signature."
)
# Fields of a version 2 receipt that are derived from the packet bytes and the strict flags, and so
# can be rebuilt and compared. The rest record where and when the receipt was made.
_DERIVED_FIELDS = (
    "schema",
    "schema_version",
    "mode",
    "ok",
    "ok_scope",
    "messages",
    "strict",
    "evidence_statuses",
    "open_evidence_items",
    "acceptance",
    "inputs",
    "boundary",
)
_CONTEXT_FIELDS = ("generated_at", "packet", "provenance", "before_review", "receipt_binding")
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
    r"(?<![A-Za-z0-9])status[*_]*[ \t]*:[*_]*[ \t]*"
    r"(?P<value>[`*_]*(not applicable|pass|fail|gap|deferred|planned)\b(?:(?!(?<![A-Za-z0-9])status[*_]*[ \t]*:)[^\n])*)",
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
    # A fenced example or an HTML comment is not evidence: blank it before reading any status.
    text = _evidence_view(evidence_file.read_text(encoding="utf-8"))
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


_INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
# What may precede a block start on a line: block quote markers and list item markers.
_CONTAINER = re.compile(r"^(?:[ \t]{0,3}>[ \t]?|[ \t]{0,3}(?:[-+*]|\d{1,9}[.)])[ \t]+)*[ \t]{0,3}")
_FENCE_OPEN = re.compile(r"(`{3,}|~{3,})(.*)$")
_FENCE_CLOSE = re.compile(r"(`{3,}|~{3,})[ \t]*$")


def _blank(text: str) -> str:
    """Blank every visible character but keep line breaks, so line structure survives."""
    return re.sub(r"[^\r\n]", " ", text)


_STATUS_LABEL = re.compile(r"(?s).*?(?<![A-Za-z0-9])status[*_]*[ \t]*:", re.IGNORECASE)


def _blank_example_spans(line: str) -> str:
    """Blank inline code spans that hold a whole status declaration: an example, not a record.

    A value alone in code, as in ``Status: `pass```, is a supported declaration and is kept.
    """

    def blank_example(match: re.Match[str]) -> str:
        return _blank(match.group(0)) if _STATUS_LABEL.match(match.group(2)) else match.group(0)

    return _INLINE_CODE.sub(blank_example, line)


# Markup that changes what a page shows as text, so a status label next to it cannot be read from the raw line.
_MARKUP = re.compile(
    r"&(?:#\d+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);"  # character references
    r"|<(?![A-Za-z][A-Za-z0-9+.-]*:[^\s>]*>)/?[A-Za-z][^>]*>"  # inline HTML, but not an autolink
    r"|!\["  # image alt text
    r"|\]\("  # link destination and title
    r"|^[ \t]{0,3}\[[^\]]+\]:"  # link reference definition
    r"|\\[!-/:-@\[-`{-~]"  # backslash escape
)
_STATUS_LABEL_WORD = re.compile(r"(?<![A-Za-z0-9])status(?![A-Za-z0-9])", re.IGNORECASE)
_RAW_HTML = re.compile(r"<(?:pre|script|style|textarea)(?:[\s>]|$)", re.IGNORECASE)


def _indent(line: str) -> int:
    """Leading columns, counting a tab as four."""
    columns = 0
    for character in line:
        if character == " ":
            columns += 1
        elif character == "\t":
            columns += 4
        else:
            break
    return columns


_COMPLETE_COMMENT = re.compile(r"<!--.*?-->")


def _dangling_opener(text: str) -> bool:
    """Whether a raw HTML line still holds a ``<!--`` after its complete comments are removed.

    A page that passes the line through opens a comment there that runs to the end of the document,
    while a strict CommonMark reading shows the lines after it, so the two cannot be reconciled.
    """
    return "<!--" in _COMPLETE_COMMENT.sub("", text)


_HTML_TAG_LINE = re.compile(r"^ {0,3}</?[A-Za-z][A-Za-z0-9-]*(?:[\s/>]|$)")
_MARKER_TEXT = re.compile(r"`{3,}|~{3,}|<!--|-->")


def _html_block_hides_markdown(lines: list[str], index: int) -> bool:
    """Whether an HTML block starting here runs over a fence or comment marker before its blank line."""
    for later in lines[index:]:
        if not later.strip():
            return False
        if _MARKER_TEXT.search(later):
            return True
    return False


_STATUS_TEXT = re.compile(r"\b(?:not applicable|pass|fail|gap|deferred|planned)\b", re.IGNORECASE)
# A pipe-table delimiter row ("--- | ---", "|:--|--:|"). The table readers take only rows that start with a pipe.
_TABLE_DELIMITER = re.compile(r"^[ \t]*(?:>[ \t]*)*(?:[-+*][ \t]+)?\|?[ \t]*:?-{2,}:?[ \t]*(?:\|[ \t]*:?-{2,}:?[ \t]*)+\|?[ \t]*$")
_BLOCK_START = re.compile(r"^(?:[ \t]{0,3}(?:[-+*]|\d{1,9}[.)])[ \t]|[ \t]{0,3}[>#]|[ \t]{0,3}(?:`{3,}|~{3,})|[ \t]{0,3}<!--)")


def _evidence_view(text: str) -> str:
    """The evidence the reader may use. See ``_scan_evidence`` for what it hides and when it gives up."""
    return _scan_evidence(text)[0]


def _scan_evidence(text: str) -> tuple[str, list[str]]:
    """The part of a Markdown file that counts as a record, and why it may be misread.

    The view is what a rendered page shows as text: fenced code blocks and HTML comments are blanked,
    following CommonMark. One pass tracks the contexts together, so none can mis-open another: inside a
    fence a ``<!--`` is text, and inside a comment a fence marker is text.

    * A comment that starts a line (after quote or list markers) is an HTML block: every line up to
      and including the one holding ``-->`` is raw, and an unterminated one runs to the end.
    * A comment that starts mid-line is inline: it ends at ``-->``, which may be on a later line of the
      same paragraph. If none comes before the paragraph ends, it is literal text.
    * A ``<!--`` inside an inline code span is text. An unterminated fence runs to the end.

    Container rules and indented code are not modelled, so the second value lists constructs where this
    view could differ from a rendered page about a status: an unterminated fence or comment, a stray
    comment opener, a fence inside a quote or list item, a table whose rows do not start with a pipe, and
    indented text that mentions a status. The
    caller must not grant eligibility when it is not empty. Line structure is kept.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    notes: list[str] = []
    fence: tuple[str, int, bool] | None = None
    html_block = False
    inline_comment = False
    raw_html = False  # inside a raw HTML paragraph, where backticks are not code spans
    for index, line in enumerate(lines):
        body = line.rstrip("\r\n")
        newline = line[len(body) :]
        if fence is not None:
            # A top-level fence is closed only by a top-level line. One opened inside a quote or list
            # item is already flagged, so any container prefix is tolerated on its closing line.
            closing = _FENCE_CLOSE.match(body[len(_CONTAINER.match(body).group(0)) :] if fence[2] else body.lstrip(" ") if len(body) - len(body.lstrip(" ")) <= 3 else "")
            if closing and closing.group(1)[0] == fence[0] and len(closing.group(1)) >= fence[1]:
                fence = None
            out.append(_blank(body) + newline)
            continue
        if html_block:
            html_block = "-->" not in body
            if not html_block and _dangling_opener(body[body.find("-->") + 3 :]):
                notes.append("a comment opener left open on the line that closes a comment")
            out.append(_blank(body) + newline)
            continue
        prefix = ""
        if inline_comment:
            end = body.find("-->")
            if end < 0:
                out.append(_blank(body) + newline)
                continue
            prefix, body, inline_comment = _blank(body[: end + 3]), body[end + 3 :], False
        else:
            lead = len(_CONTAINER.match(body).group(0))
            if _indent(body) >= 4 and _STATUS_TEXT.search(body):
                notes.append("indented text that mentions a status (it may be a code block)")
            if _HTML_TAG_LINE.match(body) and _html_block_hides_markdown(lines, index):
                notes.append("a raw HTML block that contains a fence or comment marker, which a page leaves inert")
            if not body.strip():
                raw_html = False
            elif _HTML_TAG_LINE.match(body):
                raw_html = True
            if _RAW_HTML.search(body if raw_html else _INLINE_CODE.sub("", body)):
                notes.append("a raw HTML block (pre, script, style or textarea) whose content is not shown")
            opening = _FENCE_OPEN.match(body, lead)
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                if lead > 0:
                    notes.append("a fenced block inside a quote or list item")
                fence = (opening.group(1)[0], len(opening.group(1)), lead > 0)
                out.append(_blank(body) + newline)
                continue
            if body.startswith("<!--", lead):
                if lead > 0 and body[:lead].strip():
                    notes.append("an HTML comment inside a quote or list item")
                html_block = body.find("-->", lead + 2) < 0
                if not html_block and _dangling_opener(body[lead:]):
                    notes.append("a comment opener left open on the line that closes a comment")
                out.append(_blank(body) + newline)
                continue
        if "`" in _INLINE_CODE.sub("", body) and not _FENCE_OPEN.match(body, lead if not inline_comment else 0):
            notes.append("a code span that continues onto another line")
        visible, inline_comment, stray = _blank_inline_comments(body, lines, index)
        if stray:
            notes.append("an HTML comment that is not closed on the line where it opens")
        if _TABLE_DELIMITER.match(visible) and not (
            visible.lstrip().startswith("|") and index > 0 and lines[index - 1].lstrip().startswith("|")
        ):
            notes.append("a table that does not start each row with a pipe, or sits inside a quote or list item")
        outside_code = visible if raw_html else _INLINE_CODE.sub("", visible)
        # Markup before or inside a label and its value changes how it reads; markup after it does not.
        if any(_MARKUP.search(outside_code[: label.end() + 16]) for label in _STATUS_LABEL_WORD.finditer(outside_code)):
            notes.append("a status label next to markup the reader does not interpret (entities, inline tags, images, links, escapes)")
        if not raw_html:
            visible = _blank_example_spans(visible)
        elif any(_STATUS_LABEL.match(span.group(2)) for span in _INLINE_CODE.finditer(visible)):
            notes.append("a status example in backticks next to raw HTML, where a page may not show it as code")
        out.append(prefix + visible + newline)
    if fence is not None:
        notes.append("a fenced block that is never closed")
    if html_block or inline_comment:
        notes.append("an HTML comment that is never closed")
    return "".join(out), sorted(set(notes))


def _blank_inline_comments(body: str, lines: list[str], index: int) -> tuple[str, bool, bool]:
    """Blank inline HTML comments in one line.

    Returns the line, whether a comment is still open on the next line, and whether the line held a
    comment opener that is not closed on its own line (so it either spans lines or is literal text).
    """
    masked = _INLINE_CODE.sub(lambda match: "x" * len(match.group(0)), body)
    pieces: list[str] = []
    position = 0
    search_from = 0
    while True:
        start = masked.find("<!--", search_from)
        if start >= 0 and start > 0 and masked[start - 1] == "\\":
            search_from = start + 4  # an escaped `\<` is text, not a comment opener
            continue
        if start < 0:
            pieces.append(body[position:])
            return "".join(pieces), False, False
        end = body.find("-->", start + 2)
        if end >= 0:
            # A comment on one line is removed, not blanked: a page joins the text on either side.
            pieces.append(body[position:start])
            position = search_from = end + 3
            continue
        # No close on this line: it is a comment only if one comes before the paragraph ends. Another
        # block start (a list item, quote, heading, fence, or comment block) also ends the paragraph.
        for later in lines[index + 1 :]:
            if not later.strip() or _BLOCK_START.match(later):
                break
            if "-->" in later:
                # Where this paragraph ends depends on block rules not modelled here, so a comment
                # that spans lines is read as a comment but reported.
                pieces.extend((body[position:start], _blank(body[start:])))
                return "".join(pieces), True, True
        pieces.append(body[position:])
        return "".join(pieces), False, True


_SEPARATOR_CELL = re.compile(r"^:?-{2,}:?$")
_HEADING = re.compile(r"^[ \t]{0,3}(#{1,6})[ \t]+(.*)")


def _declared_claims(packet: Path) -> tuple[list[str], int]:
    """Claim ids a Standard packet declares under basis.md "Derived requirements or claims".

    Every section with that title is read, found with the structural validator's own heading reader,
    so indentation, extra spaces, closing hashes, case, and Setext headings are treated exactly as the
    validator treats them. Subsections stay inside a section; a top-level heading ends it.

    Also returns how many data rows in that section had no readable claim id. Such a row is a
    declaration the completeness check cannot see, so the caller must not treat it as absent.
    """
    basis = packet / "basis.md"
    if not basis.is_file():
        return [], 0
    sections = _sections(_evidence_view(basis.read_text(encoding="utf-8")), "derived requirements or claims")
    ids: list[str] = []
    unreadable = 0
    for section in sections:
        found, missed = _declared_in_section(section)
        ids.extend(declared for declared in found if declared not in ids)
        unreadable += missed
    return ids, unreadable


def _sections(text: str, title: str) -> list[str]:
    """Every H2 section with this normalized title, by the structural validator's own heading reader."""
    lines, starts = _markdown_h2_sections(text)
    found: list[str] = []
    for position, (start, heading) in enumerate(starts):
        if heading == title:
            end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
            found.append("".join(lines[start:end]))
    return found


def _declared_in_section(section: str) -> tuple[list[str], int]:
    in_table = False
    ids: list[str] = []
    unreadable = 0
    for line in section.splitlines():
        heading = _HEADING.match(line)
        if heading:
            if len(heading.group(1)) == 1:
                break  # a top-level heading is an ancestor of the section and ends it
            in_table = False
            continue
        if not line.lstrip().startswith("|"):
            in_table = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not in_table:  # the first row of each table is its header
            in_table = True
            continue
        if all(_SEPARATOR_CELL.match(cell) for cell in cells if cell):
            continue
        declared = claim_id(cells[0]) if cells else None
        if declared:
            if declared not in ids:
                ids.append(declared)
        elif any(cells):
            unreadable += 1
    return ids, unreadable


_STATUS_WORD = r"(?:not applicable|pass|fail|gap|deferred|planned)"
_STATUS_ONLY = re.compile(rf"{_STATUS_WORD}(?:\s*[;,]\s*{_STATUS_WORD})*", re.IGNORECASE)
_EXPLANATION = re.compile(r"\s*:\s")


def _cell_status(cell: str) -> str | None:
    """The status a table cell declares, or None if it does not declare one.

    Emphasis, code ticks, case, a parenthetical, and a trailing explanation after a dash, a colon or a
    sentence stop are ignored. After that the cell must be nothing but status words (a composite such as
    ``pass; gap`` reads as its weakest), so prose that merely mentions "pass" is not a status.
    """
    if _CHOICE_LIST.search(cell):
        return None
    head = _DECLARATION_END.split(cell.strip(), maxsplit=1)[0]
    head = _EXPLANATION.split(head, maxsplit=1)[0]
    cleaned = _normalize_table_label(_PARENTHETICAL.sub(" ", head))
    if not _STATUS_ONLY.fullmatch(cleaned):
        return None
    return effective_status([token.group(0).lower() for token in re.finditer(_STATUS_WORD, cleaned)])


def _claim_rows(text: str) -> list[tuple[str, str]]:
    """``(claim id, status)`` for each table row keyed by a claim id that declares a status.

    Fenced examples and HTML comments are blanked first: an illustration or a retired result is not evidence.
    """
    rows: list[tuple[str, str]] = []
    for line in _evidence_view(text).splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        row_id = claim_id(cells[0]) if len(cells) > 1 else None
        if row_id is None:
            continue
        # Every status cell counts, not the first: a table may hold an expected value beside the
        # actual verdict, and the row is only as strong as its weakest recognized status.
        found = [status for status in map(_cell_status, cells[1:]) if status]
        if found:
            rows.append((row_id, effective_status(found)))
    return rows


def _claim_support(packet: Path, mode: str) -> dict[str, Any]:
    """Per-row status from verification.md. Not a score: a row is evidence status, not truth."""
    if mode != STANDARD_MODE:
        return {"state": "not_applicable", "rows": []}
    verification = packet / "verification.md"
    rows: list[tuple[str, str]] = []
    advisory: list[str] = []
    if verification.is_file():
        rows = _claim_rows(verification.read_text(encoding="utf-8"))
        check_promotion(packet, advisory)
    seen = {row_id for row_id, _ in rows}
    declared, unreadable = _declared_claims(packet)
    return {
        "state": "recognized" if rows else "unrecognized",
        "rows": [{"id": row_id, "status": status} for row_id, status in rows],
        "weakest_status": effective_status([status for _, status in rows]) if rows else None,
        "declared_without_verification_row": [i for i in declared if i not in seen],
        "unreadable_declarations": unreadable,
        "propagation_advisories": advisory,
    }


def _evidence_notes(packet: Path, mode: str) -> list[str]:
    """Constructs in the evidence files that this reader cannot read faithfully, by file."""
    names = ("proof.md",) if mode == QUICK_MODE else ("verification.md", "basis.md") if mode == STANDARD_MODE else ()
    notes: list[str] = []
    for name in names:
        path = packet / name
        if path.is_file():
            notes.extend(f"{name} has {note}" for note in _scan_evidence(path.read_text(encoding="utf-8"))[1])
    return notes


def _release_eligibility(
    result: ValidationResult,
    mode: str,
    statuses: dict[str, int],
    support: dict[str, Any],
    notes: list[str] | None = None,
) -> dict[str, Any]:
    blocked: list[str] = []
    undetermined: list[str] = [f"{note}; the reader cannot tell what a rendered page shows" for note in notes or []]
    if not result.ok:
        blocked.append("record structure is invalid")
    if mode == UNSPECIFIED_MODE:
        undetermined.append("the packet mode could not be determined")
    elif not any(statuses.values()):
        undetermined.append("no evidence status declaration could be read, so the record cannot be assessed")
    for status in ("fail", "gap", "planned"):
        if statuses.get(status):
            blocked.append(f"{statuses[status]} evidence item(s) declared '{status}'")
    if support["state"] == "unrecognized":
        undetermined.append("no claim-to-evidence rows keyed by claim id were recognized in verification.md")
    if support.get("unreadable_declarations"):
        undetermined.append(
            f"{support['unreadable_declarations']} row(s) declared in basis.md have no readable claim id, "
            "so their verification cannot be checked"
        )
    if support["state"] == "recognized":
        for missing in support.get("declared_without_verification_row", []):
            blocked.append(f"claim {missing} is declared in basis.md but has no readable verification row")
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
    # Two readers see the verification table: the status-column counter and the claim-row
    # reader. They can disagree (a "Verdict" header, say), and a recorded failure must never be
    # lost to that, so each status takes the larger of the two counts.
    row_counts = dict.fromkeys(EVIDENCE_STATUSES, 0)
    for row in support["rows"]:
        row_counts[row["status"]] = row_counts.get(row["status"], 0) + 1
    statuses = {status: max(count, row_counts.get(status, 0)) for status, count in statuses.items()}
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
        "release_eligibility": _release_eligibility(result, mode, statuses, support, _evidence_notes(packet, mode)),
        "authorized_decision": {"state": NOT_ASSESSED},
        "apply_permission": {"state": NOT_ASSESSED},
        "note": ACCEPTANCE_NOTE,
    }


def _legacy_acceptance(reason: str) -> dict[str, Any]:
    return {
        "contract": None,
        "release_eligibility": {"state": "undetermined", "reasons": [reason]},
        "authorized_decision": {"state": NOT_ASSESSED},
        "apply_permission": {"state": NOT_ASSESSED},
    }


def read_acceptance(receipt: dict[str, Any]) -> dict[str, Any]:
    """The acceptance block of a receipt, as stored. It is read, not verified.

    Anything that is not a well-formed version 2 receipt reads as ``undetermined``, never as
    eligible: a missing or unsupported schema or version, another contract, an eligibility
    state outside the closed set, or a decision or apply permission that is not
    ``not_assessed`` (this validator cannot assess either). Use ``verify_receipt`` to check
    that a stored block still matches the packet.
    """
    if not isinstance(receipt, dict):
        return _legacy_acceptance("not a receipt")
    version = receipt.get("schema_version")
    if (
        receipt.get("schema") != RECEIPT_SCHEMA
        or type(version) is not int
        or version != RECEIPT_SCHEMA_VERSION
    ):
        return _legacy_acceptance("the receipt predates or lacks the acceptance contract")
    block = receipt.get("acceptance")
    if not isinstance(block, dict) or block.get("contract") != ACCEPTANCE_CONTRACT:
        return _legacy_acceptance("the receipt predates or lacks the acceptance contract")
    eligibility = block.get("release_eligibility")
    if (
        not isinstance(eligibility, dict)
        or eligibility.get("state") not in ELIGIBILITY_STATES
        or not isinstance(eligibility.get("reasons"), list)
    ):
        return _legacy_acceptance("the acceptance block has an unsupported eligibility state")
    for name in ("authorized_decision", "apply_permission"):
        proposition = block.get(name)
        if not isinstance(proposition, dict) or proposition.get("state") != NOT_ASSESSED:
            return _legacy_acceptance(f"the acceptance block claims {name}, which this validator never assesses")
    return block


def is_open_to_decision(receipt: dict[str, Any]) -> bool:
    return read_acceptance(receipt)["release_eligibility"].get("state") in ELIGIBLE_STATES


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
    version = receipt.get("schema_version")
    if type(version) is not int or version not in SUPPORTED_RECEIPT_VERSIONS:
        return {
            "state": "invalid",
            "reasons": [f"unsupported receipt schema version {version!r}; supported: 1 (file digests only), 2"],
            "checked": [],
        }
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
    # The bytes match. Everything else a version 2 receipt says about them, except where and when it
    # was issued, is derived from them: so rebuild the whole receipt with the strict flags it
    # records and compare every derived field, not only the digested file list. An edited verdict,
    # message list, status count, boundary text, or acceptance proposition therefore reads
    # invalid, as does a field the contract does not define.
    if receipt.get("schema_version") != RECEIPT_SCHEMA_VERSION:
        return {"state": "bound", "reasons": [], "checked": checked}
    block = receipt.get("acceptance")
    if not isinstance(block, dict):
        return {
            "state": "invalid",
            "reasons": ["a version 2 receipt must carry an acceptance block; it was removed or is not an object"],
            "checked": checked,
        }
    checked.append("derived-fields")
    strict = receipt.get("strict") if isinstance(receipt.get("strict"), dict) else {}
    provenance = receipt.get("provenance") if isinstance(receipt.get("provenance"), dict) else {}
    flags = {name: bool(strict.get(name)) for name in ("custody", "authority", "two_party")}
    fresh = validate_packet(
        packet,
        require_custody=flags["custody"],
        require_authority=flags["authority"],
        require_two_party=flags["two_party"],
        before_review=bool(receipt.get("before_review")),
    )
    rebuilt = build_receipt(
        packet,
        fresh,
        strict_custody=flags["custody"],
        strict_authority=flags["authority"],
        strict_two_party=flags["two_party"],
        validator_version=str(provenance.get("validator_version") or ""),
    )
    problems: list[str] = []
    for key in _DERIVED_FIELDS:
        if receipt.get(key) == rebuilt[key]:
            continue
        if key == "acceptance":
            names = [name for name in rebuilt[key] if block.get(name) != rebuilt[key][name]]
            names += sorted(name for name in block if name not in rebuilt[key])
            problems += [
                f"acceptance.{name} does not match what these bytes yield; the block was edited" for name in names
            ]
        else:
            problems.append(f"{key} does not match what these bytes yield; the receipt was edited")
    problems += [
        f"{key} is not a field of the receipt contract"
        for key in sorted(receipt)
        if key not in _DERIVED_FIELDS and key not in _CONTEXT_FIELDS
    ]
    if problems:
        return {"state": "invalid", "reasons": problems, "checked": checked}
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
