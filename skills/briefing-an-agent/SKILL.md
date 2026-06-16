---
name: briefing-an-agent
description: Prepares focused context for an AI agent, reviewer, verifier, or releaser, with a clear role, goal anchor, authority, evidence to produce, forbidden actions, and stop conditions. Use when handing off or resuming work that matters. Do not use for a tiny self-contained task that needs no handoff.
---

# Briefing an Agent

## Overview

A context pack gives an agent or a reviewer the right focused information, and nothing extra. It states the role, the mode, the question to decide, the goal, the files affected, the evidence to produce, the approvals, the actions that are off limits, where the ideas came from, the most important next action, and the handoff state.

A good brief is how you supply competence and clarity so the agent can decide well rather than be micromanaged: name what good looks like, and state the decision rights — what it may decide at the edge and what it must escalate. Authority that outruns the clarity in the brief is the setup for a confident, wrong action.

## Decision contract

- **Claim checked:** the agent can answer what it may do, what must stay true, what evidence it owes, and when to stop -- its power over files, commands, network, credentials, approvals, and release is bounded no wider than the brief's clarity, with the goal anchor and forbidden actions stated.
- **Artifact observed:** the change-record path, its mode, the assigned role, and `context-packs.md` -> a context-pack with role, goal anchor, scoped files/commands, phase, authority bounds, stop conditions, next action, and a handoff prompt when responsibility transfers.
- **Decision affected:** block -- whether the briefed agent may start, and the authority bounds it may act within.
- **Failure class:** boundary-overreach (authority wider than the brief's clarity, or forbidden actions and allowed files unstated).
- **Next action:** bound the authority to the brief and state the forbidden actions; stop or escalate when credentials, production data, or release power appear.

## When to Use

- An AI agent will edit files, run commands, call tools, or prepare release evidence.
- A reviewer needs a one-screen summary of a Standard change record.
- A long research or build thread has to be boiled down into the context needed to act.
- Work is resumed, handed off, or transferred, and the next owner needs a clean briefing.

## When Not to Use

- The task is a small Quick change, and all the context is already in `risk.md` and `proof.md`.
- The agent has no power to act and only needs a file explained.

## Inputs

- The path to the change record and the chosen mode.
- The role: builder, reviewer, verifier, releaser, incident lead, or researcher.
- The files affected, the allowed commands, the forbidden actions, the approval gates, and the evidence required.
- `docs/02-operating-system/context-packs.md`.

## Process

1. Name the role, the question to decide, and the goal. Carry the goal anchor (the goal, the signs of success, and the non-goals, meaning what is out of scope) so it survives a context reset. See `staying-on-mission`.
2. Include only the record files, affected files, source rows, and evidence commands needed for the next decision.
3. State the last action that finished, what conditions changed, the most important next action, the likely mistake, and how to guard against it.
4. State the current phase: explore, candidate, audit, or accept.
5. State the agent's power over files, commands, the network, credentials, approvals, and the release.
6. State the claims that are off limits, the targets not to touch, when to stop, and whether a handoff is needed.
7. Link the context pack back to the record and the mode rules that apply.
8. Make the incoming owner confirm the handoff when responsibility transfers.

## Outputs

- A context-pack section or file.
- Clear limits on the agent's power.
- The next action and the evidence required.
- The last action that finished, the conditions that changed, and a handoff prompt that asks for confirmation back, when one is needed.

## Verification

- A reader can answer what they may do, what must stay true, what evidence is required, and when to stop.
- An agent that resumes or takes over can tell where to pick up and what changed.
- The context pack does not ask anyone to load the whole repo or all the standards without a reason.

## Escalation

- Stop if the requested actions go past the power set in the context pack.
- Escalate when credentials, network effects, production data, release power, or claims about outside trust appear.
- Move to `handing-off-work` when responsibility transfers with work still open or conditions changed.

## Common Rationalizations

- "More context is safer." Extra context hides the real decision and burns tokens.
- "The agent can work out its permissions." Tool power has to be stated.
- "Approval can happen later." Approval comes before the action that has side effects, not after.

## Red Flags

- No list of actions that are off limits.
- No list of allowed files or commands.
- No record of the last action that finished, for work that is resumed or handed off.
- The source lineage is pasted in whole instead of linked.

## Prompt

```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- role: <builder|reviewer|verifier|releaser|researcher>
- decision question: <one sentence>
- objective: <one paragraph>
- work phase: <explore|candidate|audit|accept>
- affected files: <list>
- last completed action:
- changed conditions:
- critical next action and likely error:
- allowed commands/tools: <list>
- forbidden actions: <list>
- do-not-touch targets: <list>
- approval gates: <list>
- required evidence: <commands/links/reviews>

Return a short context pack. Include the mode, the decision question, the goal, the work phase, a risk summary, a basis summary, the evidence required, the limits on what the agent may do, the claims it must not make, the open gaps, the last action completed, what has changed, the critical next action, and the next action. If responsibility is changing hands, add a step where the incoming owner confirms they understand.
```

## Source-lineage note

This skill is an original context-discipline pattern. It draws on public configuration-management, secure-development, AI-risk, and systems-engineering sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance.
