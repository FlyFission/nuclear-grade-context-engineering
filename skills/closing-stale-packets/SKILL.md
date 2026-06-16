---
name: closing-stale-packets
description: Brings an abandoned or half-filled change packet to an honest terminal state by completing it, closing it with a recorded rationale, or deleting it. Use when ng status flags a scaffold or invalid packet, a long session left a draft behind, or work was abandoned mid-packet. Do not use for an actively in-progress packet, or to bypass validation on a packet you intend to ship.
---

# Closing Stale Packets

## Overview

A change packet that is started and then abandoned is a quiet integrity problem. It looks like work in progress, but no one owns it, its claims were never proven, and a reader cannot tell whether the change shipped, was dropped, or is still pending. `ng status` now surfaces these: a `scaffold` packet is an untouched draft still carrying the placeholder marker; an `invalid` packet fails validation for another reason. This skill turns that signal into a decision. Every stale packet must reach one honest terminal state: completed (filled and validating), closed (deliberately abandoned with a recorded reason), or deleted (never a real change). The forbidden state is the one most packets drift into: half-done and silent, where a green-looking directory hides an unproven claim. Closing a packet with a written rationale is a first-class successful outcome, not a failure to ship.

## Decision contract

- **Claim checked:** every stale packet reached one honest terminal state -- completed and validating, closed with a recorded reason and decider, or deleted as a genuinely empty scaffold -- none left half-done and silent.
- **Artifact observed:** `ng status .`/`validate` output and the packet against its originating issue/PR/anchor -> a `NUCLEAR-GRADE-CLOSED:` rationale line and an `ng status .` where every packet is `ok` or `closed`.
- **Decision affected:** block -- bring the stale packet to a terminal state so `ng status` reports ok/closed, not scaffold/invalid.
- **Failure class:** silent-stale-packet (a half-done packet hiding an unproven claim, or a faked pass by deleting the marker).
- **Next action:** complete, close-with-reason, or delete; escalate to the owner before deleting any packet whose change is not confirmed dead.

## When to Use

- `ng status` reports a `scaffold` or `invalid` packet and you are deciding what to do about it.
- A long or interrupted session left a packet directory behind that was never finished.
- A packet's underlying change was dropped, superseded, or merged elsewhere, but the packet still sits in `.nuclear/changes/`.
- A periodic cleanup or release-readiness sweep finds packets that do not map to live work.
- A packet was scaffolded to explore an idea that was then abandoned.

## When Not to Use

- A packet that is actively being worked right now; it is in progress, not stale.
- A packet you intend to ship: fill and validate it, do not close it to silence the validator.
- Incident containment that must happen before housekeeping.
- The user is asking for formal assurance, certification, or regulatory approval.

## Inputs

- The output of `python tools/ng.py status .` (packet names, modes, and health tags).
- The packet directory under `.nuclear/changes/<slug>` and its files.
- The originating issue, PR, or mission anchor, to tell whether the change is still live.
- The validator output (`python tools/ng.py validate .nuclear/changes/<slug>`) for an `invalid` packet.

## Process

1. List the candidates. Run `ng status .` and note every packet not tagged `ok`.
2. For each stale packet, establish ownership and intent: find the originating issue, PR, or anchor, and decide whether the change is still wanted.
3. Choose one terminal state, honestly:
   - Complete it: if the change is still wanted, fill the prompts that matter, remove the placeholder marker, and make `validate` pass.
   - Close it: if the change was deliberately abandoned, add a `NUCLEAR-GRADE-CLOSED:` line carrying the rationale (why it was dropped, what replaced it if anything, who decided) on that same line, and keep the packet as a recorded decision. `ng status` recognizes that marker line and reports the packet as `closed`, a terminal state.
   - Delete it: if it was never a real change (an empty scaffold from an aborted experiment with nothing to learn), remove the directory so it stops masquerading as work.
4. Prefer close over delete when there is any decision or rationale worth preserving; prefer delete only for genuinely empty scaffolds.
5. Record the closure where it will be seen: the `NUCLEAR-GRADE-CLOSED:` line in the packet (for close), plus an OPEX note when the abandonment is a near miss worth learning from.
6. Re-run `ng status .` and confirm every packet is now `ok` or `closed`, with none left in the half-done-and-silent `scaffold`/`invalid` state.

## Outputs

- Each stale packet moved to exactly one terminal state: completed (`ok`), closed, or deleted.
- A `NUCLEAR-GRADE-CLOSED:` rationale line recording why a packet was abandoned and who decided, for every closed packet.
- An updated `ng status .` in which every packet is `ok` or `closed`, with no `scaffold` or `invalid` packet left needing attention.
- An OPEX note when a recurring pattern of abandoned packets points to a process gap.

## Verification

- `ng status .` shows every remaining packet as `ok` or `closed`; none is left in the `scaffold`/`invalid` needs-attention state.
- Every closed packet's `NUCLEAR-GRADE-CLOSED:` line names why it was dropped and who decided, not just that it was dropped.
- A completed packet actually passes `python tools/ng.py validate`; the placeholder marker is gone because the packet is filled, not because the marker was deleted to fake a pass.
- Deleted packets were genuinely empty scaffolds, confirmed before removal.

## Escalation

- Escalate to the packet's owner before deleting any packet whose change you cannot confirm is dead, since deletion is the one irreversible option.
- Escalate when stale packets accumulate faster than they are closed; that is a process signal for `learning-from-experience`, not a cleanup task.
- Stop and ask when a packet's underlying change may have shipped without proof; closing the record does not close the risk.

## Common Rationalizations

- "I will finish it later." Later rarely comes; an unfilled packet is stale now, so decide now.
- "Deleting the marker makes it pass." That fakes the gate; either fill the packet or close it with a reason.
- "Leaving it open is harmless." A half-done packet hides an unproven claim and misleads the next reader.
- "Closing it means I failed." A recorded decision to drop a change is a successful outcome; silent abandonment is the failure.
- "It is just an empty scaffold, I will close it formally." If it is genuinely empty with nothing to learn, delete it; reserve closure for decisions worth keeping.

## Red Flags

- A packet directory whose files still contain the placeholder marker days after it was created.
- `ng status` shows `scaffold` or `invalid` packets that no one can explain.
- A packet was made to pass by deleting the marker rather than by filling the content.
- Abandoned packets are deleted to tidy the listing, erasing decisions that should have been recorded.
- The same kind of packet is repeatedly started and abandoned, with no OPEX note about why.

## Prompt

```text
Bring a stale Nuclear-grade change packet to an honest terminal state.

Inputs:
- ng status output (packet name, mode, health tag):
- packet path (.nuclear/changes/<slug>):
- originating issue / PR / anchor:
- is the underlying change still wanted? yes / no / unknown:

Do this:
- Establish ownership and intent before acting.
- Choose exactly one terminal state:
  - COMPLETE: change is still wanted; fill the prompts that matter, remove the
    placeholder marker because the packet is filled, and make validate pass.
  - CLOSE: change was deliberately abandoned; add a `NUCLEAR-GRADE-CLOSED:` marker
    line with the rationale (why dropped, what replaced it if anything, who decided)
    and keep the packet as a record. `ng status` then reports it as `closed`.
  - DELETE: it was never a real change (empty scaffold, nothing to learn); remove
    the directory so it stops looking like work.
- Prefer CLOSE over DELETE when any rationale is worth preserving.
- Do not fake a pass by deleting the marker on an unfilled packet.

Return the chosen state, the closure note (for CLOSE), and confirmation that
ng status no longer shows an unexplained scaffold or invalid packet.
Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

This skill is an original software workflow influenced by configuration-management closure discipline and the work-control and self-checking practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
