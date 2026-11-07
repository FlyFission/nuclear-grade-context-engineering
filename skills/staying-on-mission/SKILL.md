---
name: staying-on-mission
description: Tests the current work against a written, lasting mission anchor and forces one choice, re-anchor, escalate, or stop. Use when an agent keeps finishing tasks but the work drifts from the goal, scope creeps, the same action repeats in a loop, or standards slip one small step at a time. Do not use for a tiny edit with an obvious goal, or while you are still containing a live incident.
---

# Staying on Mission

## Overview

Mission drift replaces the goal with local activity or weakens standards through
repeated exceptions (normalization of deviance). Test work against a written
mission anchor: goal, success criteria, non-goals, and one named owner. Choose
re-anchor, escalate, or stop. The anchor is the commander's intent: it lets
decisions move to the edge without letting local wins replace the mission.

## Decision contract

- **Claim checked:** the action was tested against the written goal, success criteria, and non-goals; attempts were counted; crossed non-goals or loosened standards have justification rows.
- **Artifact observed:** written anchor and current action/diff -> decision, updated anchor, and any justification row.
- **Decision affected:** block -- continue / re-anchor / escalate / stop, plus the restated goal anchor.
- **Failure class:** mission-drift (an action serving a swapped-in goal, a crossed non-goal, or a standard loosened "just this once").
- **Next action:** stop unjustified non-goal crossings; a missed outcome checkpoint stops the repeated batch for one blocking-path inspection and strategy change; escalate 3 failed goal attempts or uncheckable scope to the owner.

## When to Use

- A long work session has many steps, and the current action is hard to tie back to the original goal.
- Scope is growing. New files, features, or layers show up that no one asked for.
- The same action, file, or fix keeps getting retried with no progress. That is a loop.
- The agent is spending a lot (high token use) but you can see little real progress.
- Local checks pass and preparation artifacts grow, but accepted deliverables miss the agreed checkpoint.
- A reviewer or agent is working from memory of the goal instead of a written anchor.
- A non-goal is about to be crossed, or a standard is about to be loosened "just this once."
- Context was reset, shrunk, or handed off, so the goal must be set again before work goes on.

## When Not to Use

- A tiny quick edit with an obvious goal and no risk of scope growth.
- A live incident you have to contain before you stop to reflect.
- The user is asking for a formal guarantee, a certification, or regulatory approval.

## Inputs

- The mission anchor: `.nuclear/mission.md`, the `## Mission anchor` in `risk.md`, or the issue or pull request it came from.
- The repo charter (`.nuclear/charter.md`) when there is one: the lasting principles the work must not break.
- The current action and what was tried recently, including how many times.
- Accepted deliverables before and after the last work batch, the agreed checkpoint, and any blocking acceptance failure.
- The files the change touches, the diff so far, and the stated non-goals.

## Process

1. Read the written anchor: goal, success criteria, non-goals.
2. Test whether the current action advances a success criterion or a substituted local goal.
3. Judge from the level of the goal and overall design before deciding.
4. Count attempts against the success criterion. After 3 failed goal attempts, or repeated retries, stop the next variant. Green source/size checks, packets, and preparation steps do not reset the count.
   - Compare accepted deliverables before/after at the agreed checkpoint; if none exists, check before the next repeated batch. A missed checkpoint triggers strategy change despite green checks.
   - Inspect one blocked source -> transformation -> field contract -> final artifact -> acceptance failure. Check whether quoting, truncation, schema assumptions, or repair removed the governing action; these are hypotheses until inspected.
   - Choose one supported, bounded diagnostic/correction with an acceptance check and stop condition, or escalate the specific blocker. Preserve existing source, semantic, paired review, and closure gates. Do not substitute preparation revisions, councils, tracking layers, wholesale reauthoring, or weaker acceptance.
5. Check standards drift against the charter and countable tripwires: size limits, skipped checks, or weakened evidence. One normalized exception is a finding.
6. Decide and record one of three outcomes:
   - Re-anchor: the action serves the mission. Restate the anchor and keep going.
   - Escalate: the action would cross a non-goal or loosen a standard for a good reason. Write a justification row (what is being crossed, why, and why there is no simpler path) and get the owner's decision.
   - Stop: the action serves a swapped-in goal, or the justification does not hold. Halt and return to the anchor.
7. Update the written anchor so the decision survives the next context reset.

## Outputs

- A recorded re-anchor, escalate, or stop decision, with one line saying why.
- An updated mission anchor (`.nuclear/mission.md` or the `## Mission anchor` section) that survives losing context.
- A justification row whenever a non-goal or standard was crossed on purpose.
- An OPEX note (a lessons-from-operation note) when the drift was a near miss worth learning from.

## Verification

- The decision names which success criterion the action serves, or names the swapped-in goal it was serving.
- The anchor in the written record matches the anchor the decision was tested against.
- Crossed non-goals have a justification row, not a quiet edit.
- The attempt count and loop check were actually done, not assumed.
- The decision names accepted-deliverable counts before/after and the checkpoint; a missed checkpoint names the inspected failure path and bounded next step or specific escalation.

## Escalation

- Escalate to the owner after 3 failed attempts at the same goal, on any security-sensitive or hard-to-undo action, or on scope you cannot check against the anchor.
- Report the goal, attempts, blocker, and recommendation immediately, without softening bad news.
- Stop when the work would cross a non-goal with no good justification, or when no one owns the anchor.

## Common Rationalizations

- "While I am here..." Capture side work separately.
- "Basically what they asked for." Check the actual success criteria.
- "One more try." Three failed goal attempts require escalation.
- "Just this once." Justify a standards exception or reject it.
- "I remember the goal." Read the written anchor.
- "All checks passed." Check accepted outcomes, not preparation activity.
- "I restated the mission." Test the action against it.

## Red Flags

- The current action cannot be tied to a success criterion in the anchor.
- Scope grows without an updated anchor, retries repeat, or a non-goal/standard is crossed without a recorded justification.
- A behavior with no parent in the original scope appeared (a new retry, cache, fallback call, or permission) and inherited the original grade instead of being re-tiered (`rating-change-risk`).
- Progress is measured by activity (tokens, edits) instead of by success criteria met.

## Prompt

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

## Source-lineage note

This skill is an original software workflow influenced by nuclear-industry mission ownership and rising-standards culture (Rickover and Navy nuclear practice as concept lineage, not an implemented program) and by the change-management, decision-making, and self-checking practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
