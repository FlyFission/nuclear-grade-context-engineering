"""Two-party integrity for load-bearing claims.

Ports the segregation-of-duties idea -- the party that produces a result cannot
also be the party that accepts it -- to the packet's independence principle: a
claim marked ``pass`` should name a verifier who is not the change actor.

The check reads two declarations, whichever the packet carries:

1. The evidence-custody record (``## Evidence custody and coupling``), which the
   validator already parses. A custody row counts as a second party when its
   ``Verified / witnessed by`` names someone who is not any of the row's change
   actors *and* its coupling profile is classified as something other than
   ``self-check``. When custody covers a claim, custody governs that claim: a
   lighter table cannot override a row the author classified as a self-check.
2. A lightweight ``## Claim authorship`` table, for claims the custody record
   does not cover::

       ## Claim authorship
       | Claim ID | Evidence author | Verified by |
       |----------|-----------------|-------------|
       | REQ-001  | agent:claude    | ben         |

   Its verifier must be neither the evidence author nor any change actor the
   packet declares. Columns are found by header (claim, author, verifier), in
   any order; a table whose headers do not name all three declares nothing.

Either way the party the verifier is compared against (the custody row's change
actor, or the authorship row's evidence author) must itself be named. A
placeholder there (``change actor``, ``TBD``, ``agent``) leaves nothing to compare
against, so the row is not a second party, whatever its verifier says.

The parser is asymmetric on purpose, so every parsing mistake fails closed:

- Claims are read generously, from the raw file. No markup (comment, fence,
  inline code, indentation) can hide a claim from the gate, and a claim row cut
  short before its status cell is kept with an unreadable status.
- Declarations (authorship and custody) are read strictly, from visible
  Markdown only: HTML comments, fenced code blocks, lines indented four or
  more spaces, and raw HTML blocks (``<pre>``, ``<details>``, ...) count for
  nothing. Hiding too much there only removes verifiers. Claims are read from every table (outer pipes optional) whose header
has a claim (or requirement) column and a status column, found by header rather
than by position, with Markdown emphasis, code spans, and links stripped from
cells. A status cell is
read by its leading word, so ``**pass**``, ``pass (local)`` and ``pass -- 4
passed`` all read as ``pass``.

Enforcement is graded:

- ``required=True`` (``ng validate --two-party``): every ``pass`` claim must have
  a second party, a claim row whose status cannot be read fails, a claim the
  custody record cites must appear in a claim table, and a packet with no
  readable claim rows fails closed.
- ``required=False`` (default): legacy packets stay valid, but a packet that
  *opts in* with a ``## Claim authorship`` heading is held to it, even if the
  table under it is empty or malformed.

Two authorship rows for one claim that name different parties fail closed.

Identity comparison splits multi-name cells on ``+``, ``,``, ``;``, ``&``, ``and``,
or a spaced `` / `` (an unspaced slash is part of one identifier, such as
``anthropic/claude-3.5-sonnet`` or ``N/A``, whose root is its last segment), treats
generic names (``assistant``, ``the agent``, ``me``) and negative phrases (``no
verifier``, ``not yet``) as no verifier, counts a multi-name cell as a second
party when at least one name in it is outside the excluded set, and matches
aliases by root (``Claude``, ``claude-opus-5.5``, and ``agent:claude`` are one
identity). That fails closed, so
verifiers should be recorded as full, stable identities. When the only second
party generated and verified its own evidence (legitimate for an independent
reproducer, indistinguishable in text from an actor's agent grading its own work),
the coupling-profile disposition must link ``ship.md``.

This is a *declared two-party integrity check*: it checks declared actor
separation. What it does not do: it compares declared identity strings after light
normalization. It cannot detect two names for one actor, two agent instances of
one model family sharing an orchestrator, a classification the author declared
falsely, or a verifier who rubber-stamped. Those couplings are what the
five-axis profile in ``docs/02-operating-system/actor-evidence-independence.md``
records, and the merge-level half of two-party integrity still belongs to
branch protection ("require review from someone other than the author") plus a
real CODEOWNERS file.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

# Same shape as ng_validate.RECORD_ID_PATTERN (a hyphen is required), so ids such
# as `C-004a` are seen and tokens such as `E2E` or `SHA256` are not.
_RECORD_ID = re.compile(r"^[A-Z][A-Z0-9]*-[0-9][A-Za-z0-9._-]*$")
_STATUSES = ("not applicable", "pass", "fail", "gap", "deferred", "planned")
_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_ID_SPLIT = re.compile(r"\s*[,;/]\s*")
# A slash separates names only when spaced (`ben / carol`); unspaced it is part of
# one identifier (`anthropic/claude-3.5-sonnet`, `N/A`).
_ACTOR_SPLIT = re.compile(r"\s*(?:\+|,|;|&|\band\b)\s*|\s+/\s+", re.IGNORECASE)
_PUNCT = " \t.,;:!?()[]{}\"'"
# Cells that declare the absence of a verifier, or name the actor indirectly,
# rather than naming a second party. Compared after normalization.
_EMPTY_PARTY = {
    "",
    "-",
    "--",
    "—",
    "–",
    "?",
    "none",
    "nobody",
    "no one",
    "n/a",
    "n.a",
    "na",
    "tbd",
    "todo",
    "unknown",
    "pending",
    "not applicable",
    "self",
    "author",
    "the author",
    "same",
    "same process",
    "same agent",
    "same actor",
    "same person",
    "change actor",
    "the change actor",
    # Generic agent and first-person aliases name no stable second party.
    "me",
    "myself",
    "i",
    "we",
    "us",
    "assistant",
    "the assistant",
    "ai",
    "the ai",
    "ai assistant",
    "agent",
    "the agent",
    "an agent",
    "model",
    "the model",
    "llm",
    "bot",
    "the bot",
}
# "no verifier", "no separate check", "not yet", "not reviewed", and the like.
_EMPTY_PARTY_PREFIXES = (
    "no ",
    "not ",
    "none ",
    "nobody ",
    "unverified",
    "pending",
    "to be ",
    "tbd ",
)
# Placeholders that contain a split character; kept whole before a cell is split.
_SLASH_PLACEHOLDER = re.compile(r"\bn\s*/\s*a\b", re.IGNORECASE)
_TABLE_DELIM = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_CELL_SPLIT = re.compile(r"(?<!\\)\|")


class ClaimParty(NamedTuple):
    """One declared author/verifier pairing that bears on a claim."""

    source: str
    author: str
    verifier: str
    change_actor: str = ""
    # Empty for the authorship table (no classification is declared there).
    classification: str = ""
    # The coupling profile's admissibility / residual-risk disposition (custody only).
    disposition: str = ""


class ClaimRow(NamedTuple):
    claim_ids: tuple[str, ...]
    status: str | None
    raw_status: str
    raw_claim: str = ""


def _clean_cell(cell: str) -> str:
    cell = _LINK.sub(r"\1", cell)
    return cell.replace("**", "").replace("__", "").replace("`", "").strip()


_EMPHASIS = "*_~"


def _norm(value: str) -> str:
    return " ".join(_clean_cell(value).casefold().split()).strip(_PUNCT + _EMPHASIS)


def _is_empty_party(value: str) -> bool:
    raw = _clean_cell(value).strip()
    if raw.startswith("<") and raw.endswith(">"):
        return True  # an unfilled `<reviewer>` placeholder
    norm = _norm(value)
    # `agent:TBD`, `human: self`: a role prefix does not turn a placeholder into
    # a name. The prefix is stripped only for this test; identities keep it.
    bare = re.sub(r"^[a-z]+:\s*", "", norm).strip(_PUNCT + _EMPHASIS)
    return any(v in _EMPTY_PARTY or v.startswith(_EMPTY_PARTY_PREFIXES) or (v.startswith("<") and v.endswith(">")) for v in (norm, bare))


def _split_names(value: str) -> set[str]:
    """Split a multi-name cell on ``+ , ; & and`` and a spaced `` / ``, keeping ``N/A`` whole."""
    cell = _SLASH_PLACEHOLDER.sub("n.a", _clean_cell(value))
    return {_norm(part) for part in _ACTOR_SPLIT.split(cell)} - {""}


def _identities(value: str) -> set[str]:
    """Split a multi-actor cell (``ben + agent:claude``) into normalized names."""
    return ({_norm(value)} | _split_names(value)) - {""}


_ALIAS_PREFIX = re.compile(r"^[a-z]+:\s*")
_CORE = re.compile(r"[a-z]+")


def _core(name: str) -> str:
    """The stable root of an identity: `agent:claude-opus-5.5` and `Claude` share `claude`.

    A vendor or router path keeps only its last segment, so
    `anthropic/claude-3.5-sonnet` and `openrouter/claude-opus` root at `claude`.
    """
    base = _ALIAS_PREFIX.sub("", name).strip().rsplit("/", 1)[-1]
    match = _CORE.match(base)
    return match.group(0) if match and len(match.group(0)) >= 3 else name


def _is_excluded(name: str, excluded: set[str]) -> bool:
    """True when ``name`` is an excluded identity or an alias sharing its root.

    Fails closed on purpose: two different people who share a first name are
    treated as one, so record verifiers as full, stable identities (a handle).
    """
    return name in excluded or _core(name) in {_core(e) for e in excluded}


def _named_verifiers(value: str) -> set[str]:
    """The individual, non-placeholder identities a verifier cell names."""
    if _is_empty_party(value):
        return set()
    # A one-character fragment is not a stable identity; it never counts.
    return {
        part
        for part in _split_names(value)
        if len(part) > 1 and not _is_empty_party(part)
    }


def _claim_ids(cell: str) -> tuple[str, ...]:
    """Return the record ids in a claim cell: `C-001`, `C-001 / C-004a`, `C-001: text`."""
    ids: list[str] = []
    for part in _ID_SPLIT.split(_clean_cell(cell)):
        token = part.split()[0].strip(_PUNCT + _EMPHASIS) if part.split() else ""
        if _RECORD_ID.fullmatch(token):
            ids.append(token)
    return tuple(ids)


def _status(cell: str) -> str | None:
    text = re.sub(rf"[{re.escape(_EMPHASIS)}]", "", _norm(cell))
    for status in _STATUSES:
        if text == status or re.match(rf"{re.escape(status)}\b", text):
            return status
    return None


def _visible(text: str) -> str:
    """The Markdown a reader sees: HTML comments and fenced code blocks removed.

    Declarations inside a comment or a fenced example are illustrations, not
    records, so they must not satisfy (or trip) the gate.

    One pass tracks both contexts, so a fence marker inside a comment, or a
    comment marker inside a fence, is just hidden text. Stripping one kind and
    then the other lets a marker of the first kind hide visible content.
    A ``<!--`` inside an inline code span is text, and a ``<!--`` that is not at
    the start of a line opens a comment only if a ``-->`` follows somewhere;
    otherwise it is literal, as Markdown renders it.
    Hidden characters become spaces; line structure is kept.
    """
    out: list[str] = []
    in_comment = False
    fence_character: str | None = None
    fence_length = 0
    offset = 0
    for line in text.splitlines(keepends=True):
        line_start = offset
        offset += len(line)
        body = line.rstrip("\r\n")
        ending = line[len(body):]
        if fence_character is not None:
            closing = rf"^ {{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*$"
            if re.fullmatch(closing, body):
                fence_character = None
            out.append(re.sub(r"\S", " ", body) + ending)
            continue
        if not in_comment:
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", body)
            if opening and not (opening.group(1).startswith("`") and "`" in opening.group(2)):
                fence_character = opening.group(1)[0]
                fence_length = len(opening.group(1))
                out.append(re.sub(r"\S", " ", body) + ending)
                continue
        kept: list[str] = []
        i = 0
        while i < len(body):
            if in_comment:
                end = body.find("-->", i)
                stop = len(body) if end == -1 else end + 3
                kept.append(re.sub(r"\S", " ", body[i:stop]))
                if end != -1:
                    in_comment = False
                i = stop
                continue
            if body[i] == "`":
                run = len(body[i:]) - len(body[i:].lstrip("`"))
                close = re.compile(rf"(?<!`)`{{{run}}}(?!`)").search(body, i + run)
                stop = close.end() if close else i + run
                kept.append(body[i:stop])  # a code span, or literal backticks
                i = stop
                continue
            if body.startswith("<!--", i):
                at_block_start = i <= 3 and not body[:i].strip()
                if at_block_start or text.find("-->", line_start + i + 4) != -1:
                    in_comment = True
                    kept.append("    ")
                    i += 4
                    continue
            kept.append(body[i])
            i += 1
        out.append("".join(kept) + ending)
    return "".join(out)


_INDENTED = re.compile(r"^(?: {4}|\t)")


def strip_indented_code(text: str) -> str:
    """Blank every line indented four or more spaces (or a tab).

    Markdown renders such lines as code, or as content nested under a list item.
    Either way they are not a top-level declaration, so they are dropped for
    declarations. This fails closed: a real table nested under a list stops
    counting as a verifier, and the claim it covered is then reported.
    """
    return "".join(
        re.sub(r"\S", " ", line) if _INDENTED.match(line) else line
        for line in text.splitlines(keepends=True)
    )


_HTML_RAW_OPEN = re.compile(r"^ {0,3}<(pre|script|style|textarea)(?:[\s>]|$)", re.IGNORECASE)
_HTML_BLOCK_OPEN = re.compile(r"^ {0,3}</?[A-Za-z][A-Za-z0-9-]*(?:[\s/>]|$)")


def strip_html_blocks(text: str) -> str:
    """Blank raw HTML blocks, following CommonMark's block rules.

    A ``<pre>``, ``<script>``, ``<style>`` or ``<textarea>`` block runs to its
    closing tag; any other block that starts with an HTML tag (``<details>``,
    ``<div>``, ...) runs to the next blank line. Nothing inside raw HTML is a
    declaration, so this fails closed.
    """
    out: list[str] = []
    raw_tag: str | None = None
    in_block = False
    for line in text.splitlines(keepends=True):
        if raw_tag is not None:
            out.append(re.sub(r"\S", " ", line))
            if f"</{raw_tag}" in line.casefold():
                raw_tag = None
            continue
        if in_block:
            if not line.strip():
                in_block = False
                out.append(line)
            else:
                out.append(re.sub(r"\S", " ", line))
            continue
        raw = _HTML_RAW_OPEN.match(line)
        if raw:
            tag = raw.group(1).casefold()
            out.append(re.sub(r"\S", " ", line))
            if f"</{tag}" not in line.casefold()[raw.end():]:
                raw_tag = tag
            continue
        if _HTML_BLOCK_OPEN.match(line):
            in_block = True
            out.append(re.sub(r"\S", " ", line))
            continue
        out.append(line)
    return "".join(out)


def declarations_text(text: str) -> str:
    """The text verifier declarations are read from: visible, and not code.

    Claims are read generously (an odd row fails rather than vanishing);
    declarations are read strictly (anything shown as code or raw HTML counts
    for nothing).
    """
    # Each filter reads the original text, and a character survives only if
    # every filter keeps it. Chaining them would let one filter's blanking
    # (a comment inside a <div>) end another's block early.
    masks = (_visible(text), strip_indented_code(text), strip_html_blocks(text))
    return "".join(
        ch if all(m[i] == ch for m in masks) else (ch if ch in "\r\n" else " ")
        for i, ch in enumerate(text)
    )


def _cells(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [c.strip() for c in _CELL_SPLIT.split(line)]


def _tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Return ``(headers, rows)`` for every table in already-visible text.

    A table is a header line followed by a delimiter row (outer pipes optional,
    as in GitHub Markdown), or a block of pipe-led lines.
    """
    tables: list[tuple[list[str], list[list[str]]]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        delimited = (
            "|" in line
            and i + 1 < len(lines)
            and "|" in lines[i + 1]
            and _TABLE_DELIM.match(lines[i + 1]) is not None
        )
        if not (delimited or line.strip().startswith("|")):
            i += 1
            continue
        block = [line]
        i += 1
        # GitHub Markdown: a table with a delimiter row runs to the next blank
        # line or block start, and a body line with no pipe is a one-cell row.
        # A pipe-led block without one ends at the first line with no pipe.
        while i < len(lines) and lines[i].strip():
            nxt = lines[i].lstrip()
            # Another block always ends the table, pipe or not: a heading, a
            # fence, a quote, or the header line of a new table.
            starts_table = i + 1 < len(lines) and "|" in lines[i + 1] and _TABLE_DELIM.match(lines[i + 1])
            if nxt.startswith(("#", "```", "~~~", ">")) or starts_table:
                break
            if "|" not in nxt and not delimited:
                break
            block.append(lines[i])
            i += 1
        if len(block) >= 2:
            split = [_cells(row) for row in block]
            body = [row for row in split[1:] if not all(set(c) <= set(":- ") for c in row)]
            tables.append((split[0], body))
    return tables


def _claim_columns(headers: list[str]) -> tuple[int, int] | None:
    """Return (claim column, status column) when this is a claim-status table."""
    labels = [_norm(h) for h in headers]
    claim = next((i for i, h in enumerate(labels) if "claim" in h or "requirement" in h), None)
    status = next((i for i, h in enumerate(labels) if "status" in h), None)
    if status is None:
        status = next((i for i, h in enumerate(labels) if h == "result"), None)
    if claim is None or status is None or claim == status:
        return None
    return claim, status


def parse_claim_rows(verification_text: str) -> list[ClaimRow]:
    """Return every claim row from tables that carry a claim and a status column."""
    rows: list[ClaimRow] = []
    # Claims come from the raw file: no markup can hide a claim from the gate.
    # A claim row inside a comment or an example is still checked (fails closed).
    for headers, body in _tables(verification_text):
        columns = _claim_columns(headers)
        if columns is None:
            continue
        claim_col, status_col = columns
        for row in body:
            # A row cut short is kept, whichever cell it lost: a missing status
            # reads as unreadable, and a `pass` with a missing claim cell reads
            # as a pass row with no readable id. Strict mode fails both.
            raw_claim = _clean_cell(row[claim_col]) if claim_col < len(row) else ""
            ids = _claim_ids(row[claim_col]) if claim_col < len(row) else ()
            raw_status = row[status_col] if status_col < len(row) else ""
            status = _status(raw_status) if raw_status else None
            if ids or raw_claim or status == "pass":
                rows.append(ClaimRow(ids, status, raw_status, raw_claim))
    return rows


def parse_claim_status(verification_text: str) -> dict[str, str]:
    """Return ``{claim_id: status}``; a ``pass`` on any row of a claim wins.

    When a base row and a qualified row share an id (``REQ-001`` and ``REQ-001
    (live install)``), the load-bearing ``pass`` is kept so a weaker later row
    cannot silently drop the independence check this module exists to enforce.
    """
    out: dict[str, str] = {}
    for row in parse_claim_rows(verification_text):
        if row.status is None:
            continue
        for cid in row.claim_ids:
            if cid not in out or row.status == "pass":
                out[cid] = row.status
    return out


def parse_authorship_rows(verification_text: str) -> dict[str, list[tuple[str, str]]]:
    """Return ``{claim_id: [(evidence_author, verified_by), ...]}``, every row kept.

    Only tables under a visible ``## Claim authorship`` heading are read.
    """
    section = _h2_section(declarations_text(verification_text), "claim authorship")
    out: dict[str, list[tuple[str, str]]] = {}
    for headers, body in _tables(section):
        columns = _authorship_columns(headers)
        if columns is None:
            continue  # unrecognized headers declare nothing (fails closed)
        claim_col, author_col, verifier_col = columns
        for row in body:
            if max(columns) >= len(row):
                continue
            for cid in _claim_ids(row[claim_col]):
                pair = (row[author_col], row[verifier_col])
                if pair not in out.setdefault(cid, []):
                    out[cid].append(pair)
    return out


def _authorship_columns(headers: list[str]) -> tuple[int, int, int] | None:
    """(claim, evidence author, verifier) columns, found by header, or None.

    Roles come from the header text, never from position, so reordering the
    columns cannot turn the evidence author into the verifier.
    """
    labels = [_norm(h) for h in headers]

    def find(*words: str) -> int | None:
        hits = [i for i, h in enumerate(labels) if any(w in h for w in words)]
        return hits[0] if len(hits) == 1 else None

    claim = find("claim", "requirement")
    verifier = find("verif", "witness", "checked by", "reviewed by")
    author = find("author", "generated", "produced")
    if None in (claim, author, verifier) or len({claim, author, verifier}) < 3:
        return None
    return claim, author, verifier


def parse_authorship(verification_text: str) -> dict[str, tuple[str, str]]:
    """Return ``{claim_id: (evidence_author, verified_by)}`` for unambiguous rows."""
    rows = parse_authorship_rows(verification_text)
    return {cid: pairs[0] for cid, pairs in rows.items() if len(pairs) == 1}


def has_authorship_section(verification_text: str) -> bool:
    """True when a visible ``## Claim authorship`` heading exists, rows or not."""
    return any(
        line.strip().startswith("## ")
        and line.strip()[3:].strip().casefold().startswith("claim authorship")
        for line in declarations_text(verification_text).splitlines()
    )


def _h2_section(text: str, title_prefix: str) -> str:
    lines: list[str] = []
    inside = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## ") and not stripped.startswith("### "):
            inside = stripped[3:].strip().casefold().startswith(title_prefix)
            continue
        if inside:
            lines.append(line)
    return "\n".join(lines)


def _reference(party: ClaimParty) -> str:
    """The identity a row's verifier is compared against."""
    return party.change_actor if party.source.startswith("custody") else party.author


def _unnamed(value: str) -> bool:
    """True when a cell, or any name in it, is empty or a placeholder.

    A verifier can only be shown distinct from a party that is named. `change
    actor`, `TBD`, or `ben + TBD` leave an actor unnamed, so they fail closed.
    """
    return _is_empty_party(value) or any(_is_empty_party(p) for p in _split_names(value))


def _is_second_party(party: ClaimParty, packet_actors: set[str]) -> bool:
    if _is_empty_party(party.verifier):
        return False
    if _unnamed(_reference(party)):
        return False
    verifier = _norm(party.verifier)
    if party.source.startswith("custody"):
        # An independent reproducer legitimately generates and witnesses their
        # own re-run; the reference is the change actor. The custody lint already
        # forces actor-controlled evidence paths to be classified self-check.
        excluded = _identities(party.change_actor)
    else:
        excluded = _identities(party.author) | packet_actors
    # Every identity a multi-verifier cell names is compared on its own; at least
    # one must be outside the excluded set.
    if not any(not _is_excluded(name, excluded) for name in _named_verifiers(party.verifier)):
        return False
    if verifier in excluded:
        return False
    # A custody row's own classification is the stronger declaration: a row the
    # author classified as self-check is not a second party, whatever it names.
    return _norm(party.classification) != "self-check"


def _self_generated(party: ClaimParty) -> bool:
    """A custody row whose verifier also generated the evidence."""
    if not party.source.startswith("custody") or _is_empty_party(party.author):
        return False
    generators = _identities(party.author)
    actors = _identities(party.change_actor)
    # Only verifiers outside the change actors are candidates; the row is
    # self-generated when every such candidate also generated the evidence.
    eligible = [n for n in _named_verifiers(party.verifier) if not _is_excluded(n, actors)]
    return bool(eligible) and all(_is_excluded(n, generators) for n in eligible)


def _why_not(cid: str, parties: list[ClaimParty], packet_actors: set[str]) -> str:
    named = [p for p in parties if not _is_empty_party(p.verifier)]
    if not named:
        return (
            f"verification.md: claim {cid} is 'pass' but every declared verifier is "
            "empty or a placeholder; a load-bearing claim needs a named second party."
        )
    for party in named:
        if _unnamed(_reference(party)):
            role = "change actor" if party.source.startswith("custody") else "evidence author"
            return (
                f"verification.md: claim {cid} names a verifier, but its {role} is empty "
                f"or a placeholder ('{_reference(party)}', {party.source}); name the "
                f"{role} so the verifier can be shown to be someone else."
            )
        excluded = _identities(party.change_actor)
        if not party.source.startswith("custody"):
            excluded |= _identities(party.author) | packet_actors
        names = _named_verifiers(party.verifier)
        if _norm(party.verifier) in excluded or (
            names and all(_is_excluded(n, excluded) for n in names)
        ):
            return (
                f"verification.md: claim {cid} verified by its own evidence author or "
                f"change actor ('{party.verifier}', {party.source}); an independent "
                "second party is required."
            )
    return (
        f"verification.md: claim {cid} is 'pass' on self-check evidence only; record "
        "an independent second party, or narrow the status and carry the coupling "
        "as residual risk in ship.md."
    )


def check_two_party(
    packet: str | Path,
    messages: list[str],
    *,
    custody_parties: dict[str, list[ClaimParty]] | None = None,
    required: bool = True,
) -> None:
    """Append a message when a ``pass`` claim lacks an independent second party.

    ``custody_parties`` is the ``{claim_id: [ClaimParty]}`` map the validator
    builds from the custody record. ``required`` selects strict enforcement;
    see the module docstring for the graded behavior.
    """
    vfile = Path(packet) / "verification.md"
    if not vfile.exists():
        return
    text = vfile.read_text(encoding="utf-8")

    authorship_rows = parse_authorship_rows(text)
    authorship = parse_authorship(text)
    if not (required or has_authorship_section(text)):
        return
    custody = custody_parties or {}
    all_rows = parse_claim_rows(text)
    rows = [row for row in all_rows if row.claim_ids]

    # A row that says `pass` but whose claim cell yields no readable id would
    # otherwise drop out of the gate silently; fail it instead.
    for row in all_rows:
        if not row.claim_ids and row.status == "pass":
            messages.append(
                f"verification.md: a claim row marked 'pass' has no readable Claim ID "
                f"('{row.raw_claim}'); write the id plainly (for example C-001) so "
                "two-party verification can check it."
            )

    if not rows:
        messages.append(
            "verification.md: no claim-to-evidence rows with Claim IDs and a status "
            "were found; two-party verification has nothing to check (add a "
            "claim-to-evidence table with a claim column and a status column, as in "
            "templates/standard/verification.md)."
        )
        return

    for row in rows:
        if row.status is None:
            messages.append(
                f"verification.md: claim {', '.join(row.claim_ids)} has a status "
                f"'{row.raw_status}' that does not start with pass, fail, gap, deferred, "
                "not applicable, or planned; two-party verification cannot read it."
            )

    statuses = parse_claim_status(text)
    seen = {cid for row in rows for cid in row.claim_ids}
    for cid in sorted(set(custody) - seen):
        messages.append(
            f"verification.md: the evidence-custody record cites claim {cid}, but no "
            "claim-to-evidence row for it was found."
        )

    packet_actors: set[str] = set()
    for parties in custody.values():
        for party in parties:
            packet_actors |= _identities(party.change_actor)

    for cid in sorted(c for c, st in statuses.items() if st == "pass"):
        # Custody governs a claim it covers; the authorship table fills gaps only.
        parties = list(custody.get(cid, []))
        if not parties and len(authorship_rows.get(cid, [])) > 1:
            messages.append(
                f"verification.md: claim {cid} has conflicting Claim authorship rows; "
                "keep one row per claim so the declared verifier is unambiguous."
            )
            continue
        if not parties and cid in authorship:
            author, verifier = authorship[cid]
            parties = [ClaimParty("claim authorship", author, verifier)]
        if not parties:
            messages.append(
                f"verification.md: claim {cid} is 'pass' but has no authorship or "
                "custody row; cannot confirm an independent verifier."
            )
            continue
        seconds = [p for p in parties if _is_second_party(p, packet_actors)]
        if any(not _self_generated(p) for p in seconds):
            continue
        if seconds:
            # R-9: the only second party generated and verified its own evidence.
            # That is a legitimate independent reproduction only if the reproducer
            # was separate from the change; text cannot prove it, so the packet
            # must say so where the release decision reads it.
            if any("ship.md" in p.disposition.casefold() for p in seconds):
                continue
            sources = ", ".join(p.source for p in seconds)
            messages.append(
                f"verification.md: claim {cid}'s only second party ({sources}) generated "
                "and verified its own evidence. That can be a legitimate independent "
                "reproduction, but it must be disclosed: link the coupling-profile "
                "disposition to ship.md, or name a verifier who did not generate the evidence."
            )
            continue
        messages.append(_why_not(cid, parties, packet_actors))
