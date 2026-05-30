---
name: staying-on-mission
description: Tests current work against a durable mission anchor and forces a re-anchor, escalate, or stop decision. Use when an agent keeps completing tasks but the work drifts from the objective, scope creeps, the same action is retried in a loop, or rigor erodes one concession at a time. Do not use for a tiny edit with an obvious objective, or during incident containment.
---

# Controlling Mission Drift

## Overview

Mission drift is when an agent keeps shipping work that no longer serves the original objective. It has two faces: intent drift (scope creep, goal substitution, local optimization that wins the task and loses the mission) and standards drift (rigor erodes one accepted concession at a time, the normalization of deviance). This skill keeps a durable mission anchor in front of the work and forces a decision when an action stops serving it: re-anchor, escalate, or stop. The anchor is the objective, the success criteria, and the explicit non-goals. Ownership of the anchor stays with a named person, in the spirit of nuclear-culture accountability: someone is responsible for whether this change still serves its mission. Small actions must still trace to that larger mission.

## When to Use

- A long session has produced many steps and the current action is hard to tie back to the original objective.
- Scope is growing: new files, new features, or new abstractions appear that no one asked for.
- The same action, file, or fix variant is being retried without progress (a loop).
- Token burn is high while observable progress is low.
- A reviewer or agent is reasoning from memory of the objective rather than a written anchor.
- A non-goal is about to be crossed, or a standard is about to be relaxed "just this once."
- Context was reset, compacted, or handed off and the objective must be re-established before work continues.

## When Not to Use

- A tiny Quick edit with an obvious objective and no risk of scope growth.
- Incident containment that must happen before reflection.
- The user is asking for formal assurance, certification, or regulatory approval.

## Inputs

- The mission anchor: `.nuclear/mission.md`, the `## Mission anchor` in `risk.md`, or the originating issue/PR.
- The repo charter (`.nuclear/charter.md`) when present: the durable principles the work must not violate.
- The current action and recent action history (what was attempted, how many times).
- Affected files, the diff so far, and the declared non-goals.

## Process

1. Restate the mission anchor from the written record, not from memory: objective, success criteria, and non-goals.
2. Test the current action against the anchor. Ask plainly: does this action move a success criterion, or does it serve a substituted local goal?
3. Zoom out one layer before deciding. Look at the objective and the architecture, not the line in front of you, so the decision is made at the right altitude.
4. Check the loop and attempt count. If the same objective has failed 3 times, or the same action or fix variant is being retried, stop attempting the next variant.
5. Check standards drift against the charter and any countable tripwires (for example, a file or function crossing a size limit, a skipped verification, a weaker-than-agreed evidence standard). A single normalized concession is a finding, not a rounding error.
6. Decide and record one of three outcomes:
   - Re-anchor: the action serves the mission; restate the anchor and continue.
   - Escalate: the action would cross a non-goal or relax a standard for a defensible reason; record a justification row (what is being crossed, why, why no simpler path exists) and get the owner's decision.
   - Stop: the action serves a substituted goal, or the justification does not hold; halt and return to the anchor.
7. Update the durable anchor so the decision survives the next context reset.

## Outputs

- A recorded re-anchor / escalate / stop decision with one line of rationale.
- An updated mission anchor (`.nuclear/mission.md` or the `## Mission anchor` section) that survives context loss.
- A justification row when a non-goal or standard was deliberately crossed.
- An OPEX note when the drift was a near miss worth learning from.

## Verification

- The decision names which success criterion the action serves, or names the substituted goal it was serving.
- The anchor in the written record matches the anchor the decision was tested against.
- Crossed non-goals have a justification row, not a silent edit.
- The attempt count and loop check were actually performed, not assumed.

## Escalation

- Escalate to the owner after 3 failed attempts at the same objective, on any security-sensitive or irreversible action, or on scope that cannot be verified against the anchor.
- Report the state plainly and immediately: what the objective is, what was attempted, what is blocked, and the recommendation. Bad news travels up intact; a softened report is itself a drift.
- Stop when the work would cross a non-goal without a defensible justification, or when no one owns the anchor.

## Common Rationalizations

- "While I am here, I will also fix this." Adjacent work is the most common scope drift; capture it as a separate change.
- "This is basically what they asked for." Basically is goal substitution; check the success criteria, not the vibe.
- "One more attempt will get it." After three failures the approach is suspect, not the next variant.
- "We can relax this standard just this once." Once is how deviance normalizes; record it as a justified exception or do not do it.
- "I remember the objective." Memory drifts across a long session; read the written anchor.
- "Restating the mission counts as checking it." Re-stating without honestly testing the current action against it is drift theater.

## Red Flags

- The current action cannot be traced to a success criterion in the anchor.
- Scope has grown but the anchor was never updated to justify it.
- The same file, action, or fix variant has been retried several times.
- A non-goal was crossed by an edit rather than by a recorded decision.
- A standard was relaxed without a justification row.
- Progress is measured in activity (tokens, edits) rather than in success criteria met.

## Source-lineage note

This skill is an original software workflow influenced by nuclear-industry mission ownership and rising-standards culture (Rickover and Navy nuclear practice as concept lineage, not an implemented program) and by the change-management, decision-making, and self-checking practices in DOE-HDBK-1028-2009 mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
