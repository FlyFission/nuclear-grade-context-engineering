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
   packet declares.

Claims are read from every table whose header has a claim (or requirement)
column and a status column, found by header rather than by position, with
Markdown emphasis, code spans, and links stripped from cells. A status cell is
read by its leading word, so ``**pass**``, ``pass (local)`` and ``pass -- 4
passed`` all read as ``pass``.

Enforcement is graded:

- ``required=True`` (``ng validate --two-party``): every ``pass`` claim must have
  a second party, a claim row whose status cannot be read fails, a claim the
  custody record cites must appear in a claim table, and a packet with no
  readable claim rows fails closed.
- ``required=False`` (default): legacy packets stay valid, but a packet that
  *opts in* by declaring a ``## Claim authorship`` table is held to it.

What this does not do: it compares declared identity strings after light
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
_CODE_FENCE = re.compile(r"^\s*(```|~~~)")
_ID_SPLIT = re.compile(r"\s*[,;/]\s*")
_ACTOR_SPLIT = re.compile(r"\s*(?:\+|,|;|/|&|\band\b)\s*")
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
}
_EMPTY_PARTY_PREFIXES = (
    "no separate",
    "no independent",
    "no second",
    "none ",
    "pending",
    "not yet",
    "to be ",
    "tbd ",
)


class ClaimParty(NamedTuple):
    """One declared author/verifier pairing that bears on a claim."""

    source: str
    author: str
    verifier: str
    change_actor: str = ""
    # Empty for the authorship table (no classification is declared there).
    classification: str = ""


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
    return norm in _EMPTY_PARTY or norm.startswith(_EMPTY_PARTY_PREFIXES)


def _identities(value: str) -> set[str]:
    """Split a multi-actor cell (``ben + agent:claude``) into normalized names."""
    whole = _norm(value)
    parts = {_norm(part) for part in _ACTOR_SPLIT.split(_clean_cell(value))}
    return ({whole} | parts) - {""}


def _named_verifiers(value: str) -> set[str]:
    """The individual, non-placeholder identities a verifier cell names."""
    if _is_empty_party(value):
        return set()
    parts = {_norm(part) for part in _ACTOR_SPLIT.split(_clean_cell(value))}
    return {part for part in parts if part and not _is_empty_party(part)}


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


def _tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Return ``(headers, rows)`` for every pipe table outside code fences."""
    tables: list[tuple[list[str], list[list[str]]]] = []
    block: list[str] = []
    in_fence = False

    def flush() -> None:
        if len(block) >= 2:
            split = [[c.strip() for c in line.strip().strip("|").split("|")] for line in block]
            body = [row for row in split[1:] if not all(set(c) <= set(":- ") for c in row)]
            tables.append((split[0], body))
        block.clear()

    for line in text.splitlines():
        if _CODE_FENCE.match(line):
            in_fence = not in_fence
            flush()
            continue
        if not in_fence and line.strip().startswith("|"):
            block.append(line)
        else:
            flush()
    flush()
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
    for headers, body in _tables(verification_text):
        columns = _claim_columns(headers)
        if columns is None:
            continue
        claim_col, status_col = columns
        for row in body:
            if max(claim_col, status_col) >= len(row):
                continue
            ids = _claim_ids(row[claim_col])
            raw_claim = _clean_cell(row[claim_col])
            if ids or raw_claim:
                rows.append(ClaimRow(ids, _status(row[status_col]), row[status_col], raw_claim))
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


def parse_authorship(verification_text: str) -> dict[str, tuple[str, str]]:
    """Return ``{claim_id: (evidence_author, verified_by)}`` from the authorship table.

    Only tables under a ``## Claim authorship`` heading are read.
    """
    section = _h2_section(verification_text, "claim authorship")
    out: dict[str, tuple[str, str]] = {}
    for _headers, body in _tables(section):
        for row in body:
            if len(row) < 3:
                continue
            for cid in _claim_ids(row[0]):
                out[cid] = (row[1], row[2])
    return out


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


def _is_second_party(party: ClaimParty, packet_actors: set[str]) -> bool:
    if _is_empty_party(party.verifier):
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
    if not any(name not in excluded for name in _named_verifiers(party.verifier)):
        return False
    if verifier in excluded:
        return False
    # A custody row's own classification is the stronger declaration: a row the
    # author classified as self-check is not a second party, whatever it names.
    return _norm(party.classification) != "self-check"


def _why_not(cid: str, parties: list[ClaimParty], packet_actors: set[str]) -> str:
    named = [p for p in parties if not _is_empty_party(p.verifier)]
    if not named:
        return (
            f"verification.md: claim {cid} is 'pass' but every declared verifier is "
            "empty or a placeholder; a load-bearing claim needs a named second party."
        )
    for party in named:
        excluded = _identities(party.change_actor)
        if not party.source.startswith("custody"):
            excluded |= _identities(party.author) | packet_actors
        names = _named_verifiers(party.verifier)
        if _norm(party.verifier) in excluded or (names and names <= excluded):
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

    authorship = parse_authorship(text)
    if not (required or authorship):
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
        if not parties and cid in authorship:
            author, verifier = authorship[cid]
            parties = [ClaimParty("claim authorship", author, verifier)]
        if not parties:
            messages.append(
                f"verification.md: claim {cid} is 'pass' but has no authorship or "
                "custody row; cannot confirm an independent verifier."
            )
            continue
        if any(_is_second_party(p, packet_actors) for p in parties):
            continue
        messages.append(_why_not(cid, parties, packet_actors))
