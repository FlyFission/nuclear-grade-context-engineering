---
name: staying-on-mission
description: Tests the current work against a written, lasting mission anchor and forces one choice, re-anchor, escalate, or stop. Use when an agent keeps finishing tasks but the work drifts from the goal, scope creeps, the same action repeats in a loop, or standards slip one small step at a time. Do not use for a tiny edit with an obvious goal, or while you are still containing a live incident.
---

# Staying on Mission

## Overview

Mission drift is when an agent keeps shipping work that no longer serves the original goal. It comes in two forms. The first is intent drift: scope creeps, the goal quietly gets swapped for a smaller one, or the agent wins the task but loses the mission. The second is standards drift: the work gets a little less careful each time you accept one more small exception. Letting a bad habit become normal this way is called the normalization of deviance.

This skill keeps a written mission anchor in front of the work. When an action stops serving that anchor, you make one of three choices: re-anchor, escalate, or stop. The anchor has three parts: the goal, the success criteria (how you know you are done), and the clear non-goals (what you are deliberately not doing). One named person owns the anchor. That person is responsible for whether this change still serves its mission. Every small action still has to trace back to that larger mission.

The anchor is also the clarity that lets authority move to the edge: it is the commander's intent that keeps a decentralized decision aligned with the goal. Push decisions to where the information is, but only against a clear, shared anchor — otherwise local wins quietly drift from the mission.

## Decision contract

- **Claim checked:** the current action was tested against the written anchor's goal, success criteria, and non-goals, the loop and attempt count were actually run, and any crossed non-goal or loosened standard has a justification row, not a quiet edit.
- **Artifact observed:** the written anchor (`.nuclear/mission.md`, `## Mission anchor` in `risk.md`, or `.nuclear/charter.md`) and the current action/diff -> a recorded continue/re-anchor/escalate/stop decision, updated anchor, and any justification row.
- **Decision affected:** block -- continue / re-anchor / escalate / stop, plus the restated goal anchor.
- **Failure class:** mission-drift (an action serving a swapped-in goal, a crossed non-goal, or a standard loosened "just this once").
- **Next action:** stop and return to the anchor when a non-goal would be crossed with no justification; 3 failed attempts or scope you cannot check escalates to the owner.

## When to Use

- A long work session has many steps, and the current action is hard to tie back to the original goal.
- Scope is growing. New files, features, or layers show up that no one asked for.
- The same action, file, or fix keeps getting retried with no progress. That is a loop.
- The agent is spending a lot (high token use) but you can see little real progress.
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
- The files the change touches, the diff so far, and the stated non-goals.

## Process

1. Restate the mission anchor from the written record, not from memory: the goal, the success criteria, and the non-goals.
2. Test the current action against the anchor. Ask plainly: does this action move a success criterion forward, or does it serve some smaller goal that got swapped in?
3. Step back one level before you decide. Look at the goal and the overall design, not just the line in front of you, so you decide from the right height.
4. Check for a loop and count the attempts. If the same goal has failed 3 times, or the same action or fix is being retried, stop trying the next version.
5. Check for standards drift against the charter and any countable warning lines. Examples: a file or function passing a size limit, a skipped check, or accepting weaker evidence than you agreed to. One normalized exception is a finding, not a rounding error.
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

## Escalation

- Escalate to the owner after 3 failed attempts at the same goal, on any security-sensitive or hard-to-undo action, or on scope you cannot check against the anchor.
- Report the state plainly and right away: what the goal is, what was tried, what is blocked, and your recommendation. Bad news has to travel up unchanged. A softened report is itself a kind of drift.
- Stop when the work would cross a non-goal with no good justification, or when no one owns the anchor.

## Common Rationalizations

- "While I am here, I will also fix this." Side work is the most common scope drift. Capture it as a separate change.
- "This is basically what they asked for." "Basically" means the goal got swapped. Check the success criteria, not the vibe.
- "One more try will do it." After three failures, the approach is the problem, not the next try.
- "We can loosen this standard just this once." "Once" is how a bad habit becomes normal. Record it as a justified exception or do not do it.
- "I remember the goal." Memory drifts over a long session. Read the written anchor.
- "Restating the mission counts as checking it." Restating without honestly testing the current action against it is just for show.

## Red Flags

- The current action cannot be tied to a success criterion in the anchor.
- Scope has grown, but the anchor was never updated to justify it.
- The same file, action, or fix has been retried several times.
- A non-goal was crossed by an edit instead of by a recorded decision.
- A standard was loosened without a justification row.
- Progress is measured by activity (tokens, edits) instead of by success criteria met.

## Prompt

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

## Source-lineage note

This skill is an original software workflow influenced by nuclear-industry mission ownership and rising-standards culture (Rickover and Navy nuclear practice as concept lineage, not an implemented program) and by the change-management, decision-making, and self-checking practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
