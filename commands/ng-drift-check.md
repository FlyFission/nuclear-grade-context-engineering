# ng-drift-check

## Purpose

Test the current work against its mission anchor and the repo charter, and force a re-anchor, escalate, or stop decision. This is a portable command prompt.

## Use when

- A long session has drifted and the current action is hard to tie to the original objective.
- Scope is growing, the same action is being retried, or a non-goal is about to be crossed.
- Context was reset, compacted, or handed off and the objective must be re-established.
- A standard is about to be relaxed "just this once."

## Do not use when

- A tiny Quick edit with an obvious objective and no risk of scope growth.
- Incident containment must happen before reflection.
- The user needs formal assurance, certification, legal advice, or regulatory approval.

## Inputs

- The mission anchor: `.nuclear/mission.md`, the `## Mission anchor` in `risk.md`, or the originating issue/PR.
- The repo charter (`.nuclear/charter.md`) when present.
- The current action and recent attempt history.
- Affected files, the diff so far, and the declared non-goals.

## Prompt text

```text
Run a Nuclear-grade mission-drift check on the current work.

Inputs:
- mission anchor (objective, success criteria, non-goals):
- charter principles in play:
- current action:
- recent attempts at this objective (how many, what variants):
- affected files / diff so far:

Do this:
- Restate the anchor from the written record, not from memory.
- Zoom out one layer; judge at the objective/architecture altitude.
- Test the current action against the success criteria and non-goals.
- Check the loop: if the same objective has failed 3 times, stop attempting the next variant.
- Check standards drift against the charter and any countable tripwires.

Return one decision:
- RE-ANCHOR: the action serves the mission; restate the anchor and continue.
- ESCALATE: a non-goal or standard must be crossed for a defensible reason; include a justification row (what is crossed, why, why no simpler path exists).
- STOP: the action serves a substituted goal, or the justification does not hold.

Also return the updated anchor text so the decision survives the next context reset.
Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- `.nuclear/mission.md` or the `## Mission anchor` section in `risk.md` (updated anchor).
- `ship.md` or an OPEX record when the drift was a near miss.

## Expected outputs

- A re-anchor / escalate / stop decision with one line of rationale.
- An updated, durable mission anchor.
- A justification row when a non-goal or standard was deliberately crossed.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Restating the mission without honestly testing the current action against it (drift theater).
- Attempting the next variant after three failures instead of escalating.
- Crossing a non-goal by editing rather than by a recorded decision.
- Measuring progress in activity rather than in success criteria met.

## Legal/assurance boundary note

This command supports mission alignment and evidence visibility. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
