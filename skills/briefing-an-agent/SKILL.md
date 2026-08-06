---
name: briefing-an-agent
description: Prepares focused context for an AI agent, reviewer, verifier, or releaser at the start of a task, with a clear role, goal anchor, authority, evidence to produce, forbidden actions, and stop conditions. Use when an agent or reviewer is about to begin work and needs bounded context before it starts. Do not use for a tiny self-contained task that needs no briefing, or for transferring already-open work to a new owner, which is handing-off-work.
---

# Briefing an Agent

## Overview

A context pack gives an agent or a reviewer the right focused information, and nothing extra. It states the role, the mode, the question to decide, the goal, the files affected, the evidence to produce, the approvals, the actions that are off limits, where the ideas came from, the most important next action, and the state of the work so far.

A good brief is how you supply competence and clarity so the agent can decide well rather than be micromanaged: name what good looks like, and state the decision rights — what it may decide at the edge and what it must escalate. Authority that outruns the clarity in the brief is the setup for a confident, wrong action.

## Decision contract

- **Claim checked:** the agent can answer what it may do, what must stay true, what evidence it owes, and when to stop -- its power over files, commands, network, credentials, approvals, and release is bounded no wider than the brief's clarity, with the goal anchor and forbidden actions stated.
- **Artifact observed:** the change-record path, its mode, the assigned role, and `context-packs.md` -> a context-pack with role, goal anchor, scoped files/commands, phase, authority bounds, stop conditions, and the next action.
- **Decision affected:** block -- whether the briefed agent may start, and the authority bounds it may act within.
- **Failure class:** boundary-overreach (authority wider than the brief's clarity, or forbidden actions and allowed files unstated).
- **Next action:** bound the authority to the brief and state the forbidden actions; stop or escalate when credentials, production data, or release power appear.

## When to Use

- An AI agent is about to edit files, run commands, call tools, or prepare release evidence, and needs its role, authority, and stop conditions stated before it starts.
- A reviewer needs a one-screen summary of a Standard change record before beginning the review.
- A long research or build thread has to be boiled down into the context needed to act.

## When Not to Use

- The task is a small Quick change, and all the context is already in `risk.md` and `proof.md`.
- The agent has no power to act and only needs a file explained.
- Responsibility for work that is already open is transferring to a new owner. That is a handoff, not a start-of-task briefing -- use `handing-off-work`, which also forces the incoming owner to restate scope, authority, and stop conditions before acting.

## Inputs

- The path to the change record and the chosen mode.
- The role: builder, reviewer, verifier, releaser, incident lead, or researcher.
- The files affected, the allowed commands, the forbidden actions, the approval gates, and the evidence required.
- `docs/02-operating-system/context-packs.md`.

## Process

1. Name the role, the question to decide, and the goal. Carry the goal anchor (the goal, the signs of success, and the non-goals, meaning what is out of scope) so it survives a context reset. Name who is affected by the work and anyone who must be consulted, so the brief carries the stakes, not just the task. See `staying-on-mission`.
2. Include only the record files, affected files, source rows, and evidence commands needed for the next decision.
3. State the last action that finished, what conditions changed, the most important next action, the likely mistake, and how to guard against it.
4. State the current phase: explore, candidate, audit, or accept, and name the **archetype** the brief puts the agent in. A briefing verb chooses a posture whether or not you say so -- "clean this up" is Sweeper, whose characteristic drift is deletion without a baseline; "make it work" is Builder, whose drift is volume outrunning review. Naming it puts the drift on the record before the agent starts. See `docs/02-operating-system/archetype-lens.md`.
5. State the agent's power over files, commands, the network, credentials, approvals, and the release.
6. State the claims that are off limits, the targets not to touch, and when to stop.
7. Link the context pack back to the record and the mode rules that apply.

## Outputs

- A context-pack section or file.
- Clear limits on the agent's power.
- The archetype the brief places the agent in, and the drift that posture is prone to.
- The next action and the evidence required.
- The last action that finished and the conditions that changed, when this brief follows earlier work in the same task.

## Verification

- A reader can answer what they may do, what must stay true, what evidence is required, and when to stop.
- An agent starting the work can tell what already happened and what changed, without reading the full chat history.
- The context pack does not ask anyone to load the whole repo or all the standards without a reason.

## Escalation

- Stop if the requested actions go past the power set in the context pack.
- Escalate when credentials, network effects, production data, release power, or claims about outside trust appear.
- Move to `handing-off-work` when responsibility is transferring to a new owner with work still open or conditions changed.

## Common Rationalizations

- "More context is safer." Extra context hides the real decision and burns tokens.
- "The agent can work out its permissions." Tool power has to be stated.
- "Approval can happen later." Approval comes before the action that has side effects, not after.

## Red Flags

- No list of actions that are off limits.
- No list of allowed files or commands.
- No record of the last action that finished, when this brief follows earlier work in the same task.
- The source lineage is pasted in whole instead of linked.

## Command prompt asset

The ready-to-paste command prompt is packaged at `assets/command-prompt.md`.
Load it only when the operator requests the command form; the runtime contract above remains primary.

## Source-lineage note

This skill is an original context-discipline pattern. It draws on public configuration-management, secure-development, AI-risk, and systems-engineering sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance.
