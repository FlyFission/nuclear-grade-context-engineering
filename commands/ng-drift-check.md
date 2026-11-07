---
description: "Tests the current work against a written, lasting mission anchor and forces one choice, re-anchor, escalate, or stop."
disable-model-invocation: true
---

# ng-drift-check

Portable command prompt generated from `skills/staying-on-mission/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- A long work session has many steps, and the current action is hard to tie back to the original goal.
- Scope is growing. New files, features, or layers show up that no one asked for.
- The same action, file, or fix keeps getting retried with no progress. That is a loop.
- The agent is spending a lot (high token use) but you can see little real progress.
- Local checks pass and preparation artifacts grow, but accepted deliverables miss the agreed checkpoint.
- A reviewer or agent is working from memory of the goal instead of a written anchor.
- A non-goal is about to be crossed, or a standard is about to be loosened "just this once."
- Context was reset, shrunk, or handed off, so the goal must be set again before work goes on.

## Do not use when

- A tiny quick edit with an obvious goal and no risk of scope growth.
- A live incident you have to contain before you stop to reflect.
- The user is asking for a formal guarantee, a certification, or regulatory approval.

## Inputs

- The mission anchor: `.nuclear/mission.md`, the `## Mission anchor` in `risk.md`, or the issue or pull request it came from.
- The repo charter (`.nuclear/charter.md`) when there is one: the lasting principles the work must not break.
- The current action and what was tried recently, including how many times.
- Accepted deliverables before and after the last work batch, the agreed checkpoint, and any blocking acceptance failure.
- The files the change touches, the diff so far, and the stated non-goals.

## Prompt text

```text
Run a Nuclear-grade mission-drift check on the current work.

Inputs:
- mission anchor (objective, success criteria, non-goals):
- charter principles in play:
- current action:
- recent attempts at this objective (how many, what variants):
- accepted deliverables before/after, agreed checkpoint, blocking acceptance failure:
- affected files / diff so far:

Do this:
- Restate the goal from the written record, not from memory.
- Zoom out one layer; judge at the level of the goal and the architecture, not the detail.
- Test the current action against the success criteria and the non-goals.
- Decide whether the action serves the mission, or a smaller local goal that has quietly replaced it.
- Check the loop against accepted outcomes: 3 failed goal attempts stop the next variant; green local checks do not reset the count.
- If the outcome checkpoint is missed, inspect one blocked source -> transformation -> field contract -> final artifact -> acceptance path before another work batch.
- Choose one bounded diagnostic/correction with an acceptance check and stop condition, or escalate the specific blocker. Preserve all quality gates; do not add preparation loops or reauthor accepted records.
- Check for slipping standards against the charter and any countable tripwires.

Return one decision:
- RE-ANCHOR: the action serves the mission; restate the goal and continue.
- ESCALATE: a non-goal or a standard must be crossed for a defensible reason; include a justification row (what is crossed, why, and why no simpler path exists).
- STOP: the action serves a smaller local goal, or the justification does not hold.

Also return the updated goal text, so the decision survives the next context reset.
Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Verification

- The decision names which success criterion the action serves, or names the swapped-in goal it was serving.
- The anchor in the written record matches the anchor the decision was tested against.
- Crossed non-goals have a justification row, not a quiet edit.
- The attempt count and loop check were actually done, not assumed.
- The decision names accepted-deliverable counts before/after and the checkpoint; a missed checkpoint names the inspected failure path and bounded next step or specific escalation.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/staying-on-mission/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
