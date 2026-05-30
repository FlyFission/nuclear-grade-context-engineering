# ng-drift-check

## Purpose

Test the current work against its stated goal and the repo's charter, and force one call: re-anchor, escalate, or stop. The stated goal is the mission anchor — the goal written down so it survives. This is a portable command prompt.

## Use when

- A long session has drifted, and the current action is hard to tie back to the original goal.
- Scope is growing, the same action keeps getting retried, or a non-goal is about to be crossed.
- The context was reset, compacted, or handed off, and you must re-establish the goal.
- A standard is about to be relaxed "just this once."

## Do not use when

- It is a tiny Quick edit with an obvious goal and no risk of scope growth.
- You must contain an incident before you reflect on it.
- The user needs formal assurance, certification, or legal advice. This prompt does not give regulatory approval.

## Inputs

- The mission anchor: `.nuclear/mission.md`, the `## Mission anchor` in `risk.md`, or the originating issue/PR.
- The repo charter (`.nuclear/charter.md`) when there is one.
- The current action and the recent attempt history.
- The files affected, the diff so far, and the non-goals you declared.

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
- Restate the goal from the written record, not from memory.
- Zoom out one layer; judge at the level of the goal and the architecture, not the detail.
- Test the current action against the success criteria and the non-goals.
- Decide whether the action serves the mission, or a smaller local goal that has quietly replaced it.
- Check the loop: if the same goal has failed 3 times, stop trying the next variant.
- Check for slipping standards against the charter and any countable tripwires.

Return one decision:
- RE-ANCHOR: the action serves the mission; restate the goal and continue.
- ESCALATE: a non-goal or a standard must be crossed for a defensible reason; include a justification row (what is crossed, why, and why no simpler path exists).
- STOP: the action serves a smaller local goal, or the justification does not hold.

Also return the updated goal text, so the decision survives the next context reset.
Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- `.nuclear/mission.md`, or the `## Mission anchor` section in `risk.md` (the updated goal).
- `ship.md`, or a lessons-from-operation (OPEX) record, when the drift was a near miss.

## Expected outputs

- A re-anchor / escalate / stop decision, with one line of reasoning.
- An updated, lasting statement of the goal.
- A justification row when a non-goal or a standard was crossed on purpose.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Restating the goal without honestly testing the current action against it (drift theater).
- Trying the next variant after three failures instead of asking for help.
- Crossing a non-goal by editing, instead of by a recorded decision.
- Measuring progress by activity, not by success criteria met.
- Winning a local task while losing the mission.

## Legal/assurance boundary note

This command supports staying on mission and seeing the evidence. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
