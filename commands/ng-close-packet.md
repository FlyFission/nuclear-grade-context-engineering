# ng-close-packet

## Purpose

Bring an abandoned or half-filled change packet to an honest terminal state: complete it, close it with a recorded rationale, or delete it. This is a portable command prompt that pairs with `ng status` health tags.

## Use when

- `ng status` reports a `scaffold` or `invalid` packet and you must decide what to do about it.
- A long or interrupted session left a packet directory behind that was never finished.
- A packet's underlying change was dropped, superseded, or merged elsewhere but still sits in `.nuclear/changes/`.
- A cleanup or release-readiness sweep finds packets that no longer map to live work.

## Do not use when

- A packet is actively being worked right now; it is in progress, not stale.
- You intend to ship the packet: fill and validate it instead of closing it to silence the validator.
- Incident containment must happen before housekeeping.
- The user needs formal assurance, certification, legal advice, or regulatory approval.

## Inputs

- The output of `python tools/ng.py status .`.
- The packet directory under `.nuclear/changes/<slug>` and its files.
- The originating issue, PR, or mission anchor, to tell whether the change is still live.
- The validator output for an `invalid` packet.

## Prompt text

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
  - CLOSE: change was deliberately abandoned; write a closure note (why dropped,
    what replaced it if anything, who decided) and keep the packet as a record.
  - DELETE: it was never a real change (empty scaffold, nothing to learn); remove
    the directory so it stops looking like work.
- Prefer CLOSE over DELETE when any rationale is worth preserving.
- Do not fake a pass by deleting the marker on an unfilled packet.

Return the chosen state, the closure note (for CLOSE), and confirmation that
ng status no longer shows an unexplained scaffold or invalid packet.
Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- `.nuclear/changes/<slug>/` (filled to completion, given a closure note, or deleted).
- An OPEX record when repeated abandonment points to a process gap.

## Expected outputs

- The packet moved to exactly one terminal state: completed, closed, or deleted.
- A closure note for every closed packet, naming why it was dropped and who decided.
- An `ng status .` listing with no unexplained `scaffold` or `invalid` packet.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Deleting the placeholder marker to fake a validation pass instead of filling the packet.
- Leaving a packet half-done and silent because "I will finish it later."
- Deleting a packet whose change may have shipped without proof, erasing the risk record.
- Tidying the listing by deleting packets that recorded real decisions worth keeping.
- Treating a recorded closure as a failure rather than a successful terminal state.

## Legal/assurance boundary note

This command supports packet lifecycle hygiene and evidence visibility. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
