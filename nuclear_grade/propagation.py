"""Evidence-trust propagation for change packets (proposal, not yet wired in).

Ports Palantir Foundry's marking-propagation idea to the packet model: a derived
thing inherits the trust of its weakest source, so a packet (a baseline
candidate) cannot be promoted greener than its weakest claim. Where Foundry
propagates a security marking to derived datasets, this propagates evidence
*trust* up the claim graph and computes it, rather than trusting a summary label
an author typed.

This module is intentionally standalone and stdlib-only, matching the
``_check_*(..., messages)`` style of ``nuclear_grade.ng_validate`` so it can drop
into ``validate_packet`` later behind a maintainer decision on severity. It is
NOT imported by the validator yet; landing it as a gate is tracked as a planned
claim in the accompanying change packet.

Trust order (worst to best): ``fail`` < ``gap`` = ``planned`` < ``deferred`` <
``pass``. ``not applicable`` is neutral and excluded from the minimum. A packet
promotes only when every counted claim is ``pass``, or a non-pass claim is a
``deferred`` (or ``planned``) item recorded with a reason in a "Deferred items"
section. That recorded-reason rule is the seam where purpose-based access
(record *why* for an exception) enters.
"""

from __future__ import annotations

import re
from pathlib import Path

# Rank mirrors ng_validate.EVIDENCE_STATUSES; higher rank == more trusted.
# ``not applicable`` is neutral (None) and dropped from the minimum.
STATUS_RANK: dict[str, int | None] = {
    "fail": 0,
    "gap": 1,
    "planned": 1,
    "deferred": 2,
    "pass": 3,
    "not applicable": None,
}

PROMOTABLE_RANK = 3  # only an all-pass packet promotes

_CLAIM_ID = re.compile(r"^[A-Z]-?\d+$")


def parse_claim_statuses(verification_text: str) -> list[tuple[str, str]]:
    """Return ``(claim_id, status)`` pairs from the claim-to-evidence table.

    A row counts only when its first cell is a claim id (e.g. ``C-001`` or
    ``REQ-001``) and one later cell is a known status, so header and separator
    rows are skipped and column layout can vary a little.
    """
    results: list[tuple[str, str]] = []
    for line in verification_text.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not _CLAIM_ID.match(cells[0]):
            continue
        status = next(
            (c.lower() for c in cells[1:] if c.lower() in STATUS_RANK), None
        )
        if status is not None:
            results.append((cells[0], status))
    return results


def _deferred_section_ids(verification_text: str) -> set[str]:
    """Claim ids named under a heading mentioning 'deferred'."""
    in_deferred = False
    ids: set[str] = set()
    for line in verification_text.splitlines():
        if line.startswith("#"):
            in_deferred = "deferred" in line.lower()
            continue
        if in_deferred:
            ids.update(re.findall(r"[A-Z]-?\d+", line))
    return ids


def effective_status(statuses: list[str]) -> str:
    """The weakest counted status = the packet's inherited trust (the minimum)."""
    counted = [s for s in statuses if STATUS_RANK.get(s) is not None]
    if not counted:
        return "not applicable"
    return min(counted, key=lambda s: STATUS_RANK[s])  # type: ignore[index]


def check_promotion(packet: str | Path, messages: list[str]) -> None:
    """Append a message when a packet cannot promote greener than its weakest claim.

    Signature matches the existing ``_check_*`` helpers. A packet with no
    ``verification.md`` (for example a quick packet) has nothing to propagate.
    """
    vfile = Path(packet) / "verification.md"
    if not vfile.exists():
        return
    text = vfile.read_text(encoding="utf-8")

    claims = parse_claim_statuses(text)
    if not claims:
        return

    deferred_ok = _deferred_section_ids(text)
    inherited = effective_status([s for _, s in claims])
    for claim_id, status in claims:
        rank = STATUS_RANK[status]
        if rank is None:
            continue
        if status in ("deferred", "planned"):
            if claim_id not in deferred_ok:
                messages.append(
                    f"verification.md: claim {claim_id} is '{status}' but is not "
                    "recorded in a 'Deferred items' section; a parked claim needs "
                    "a recorded reason before the packet can promote."
                )
            continue
        if rank < PROMOTABLE_RANK:
            messages.append(
                f"verification.md: claim {claim_id} status '{status}' taints the "
                "packet; a baseline cannot be promoted greener than its weakest "
                f"claim (effective status = '{inherited}')."
            )
