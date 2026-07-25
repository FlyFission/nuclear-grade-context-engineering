"""Two-party integrity for load-bearing claims (proposal, not yet wired in).

Ports Palantir Foundry's purpose-based access split, where the party that
requests access cannot also be the party that approves it, to the packet's
independence principle: a load-bearing claim cannot be marked verified by the
same identity that authored its evidence.

Honest prerequisite: packets today do not record who drafted versus who verified
each claim (evidence is authored by one identity on an agent branch), so this
check reasons over a small proposed schema addition to ``verification.md``, a
"Claim authorship" table::

    ## Claim authorship
    | Claim ID | Evidence author | Verified by |
    |----------|-----------------|-------------|
    | REQ-001  | agent:claude    | ben         |

Without that table the check is advisory: it flags that independence cannot be
confirmed but blocks nothing. The stronger, merge-level half of two-party
integrity lives in GitHub branch protection ("require review from someone other
than the author") plus a real CODEOWNERS, not in this module.

Like ``propagation``, this is standalone and stdlib-only and is NOT imported by
the validator yet.
"""

from __future__ import annotations

import re
from pathlib import Path

_CLAIM_ID = re.compile(r"^[A-Z]-?\d+$")


def parse_claim_status(verification_text: str) -> dict[str, str]:
    """Return ``{claim_id: status}`` from the claim-to-evidence table."""
    out: dict[str, str] = {}
    known = {"pass", "fail", "gap", "deferred", "not applicable", "planned"}
    for line in verification_text.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not _CLAIM_ID.match(cells[0]):
            continue
        status = next((c.lower() for c in cells[1:] if c.lower() in known), None)
        if status is not None:
            out[cells[0]] = status
    return out


def parse_authorship(verification_text: str) -> dict[str, tuple[str, str]]:
    """Return ``{claim_id: (evidence_author, verified_by)}`` from the authorship table.

    Only rows under a '## Claim authorship' heading are read, so this never
    collides with the main claim-to-evidence table.
    """
    out: dict[str, tuple[str, str]] = {}
    in_section = False
    for line in verification_text.splitlines():
        if line.startswith("#"):
            in_section = "claim authorship" in line.lower()
            continue
        if not in_section or "|" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not _CLAIM_ID.match(cells[0]):
            continue
        out[cells[0]] = (cells[1].lower(), cells[2].lower())
    return out


def check_two_party(packet: str | Path, messages: list[str]) -> None:
    """Append a message when a ``pass`` claim lacks an independent second party.

    Signature matches the existing ``_check_*`` helpers.
    """
    vfile = Path(packet) / "verification.md"
    if not vfile.exists():
        return
    text = vfile.read_text(encoding="utf-8")

    statuses = parse_claim_status(text)
    verified = {cid for cid, st in statuses.items() if st == "pass"}
    if not verified:
        return

    authorship = parse_authorship(text)
    if not authorship:
        messages.append(
            "verification.md: claims are marked 'pass' but no 'Claim authorship' "
            "table records who drafted versus verified each; two-party integrity "
            "cannot be confirmed (add the authorship table, or enforce at merge "
            "via branch protection)."
        )
        return

    for cid in sorted(verified):
        if cid not in authorship:
            messages.append(
                f"verification.md: claim {cid} is 'pass' but has no authorship "
                "row; cannot confirm an independent verifier."
            )
            continue
        author, verifier = authorship[cid]
        if not verifier:
            messages.append(
                f"verification.md: claim {cid} is 'pass' but 'Verified by' is "
                "empty; a load-bearing claim needs a named second party."
            )
        elif verifier == author:
            messages.append(
                f"verification.md: claim {cid} verified by its own evidence "
                f"author ('{verifier}'); an independent second party is required."
            )
