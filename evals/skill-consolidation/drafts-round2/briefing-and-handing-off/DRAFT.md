---
name: briefing-and-handing-off
description: Gives an agent, reviewer, verifier, or releaser what it needs to act and nothing extra - a bounded brief before it starts (role, goal anchor, authority, evidence owed, forbidden actions, stop conditions), plus, when open work changes hands or a thread resumes, the state carried over and the new owner's confirmation before acting. Do not use when the same owner continues uninterrupted, or for a tiny self-contained task.
---

# Briefing and Handing Off

## Overview

Every time work starts in a fresh context or moves to a new owner, two things can go wrong: too little is said, so the agent fills gaps with confident guesses, or too much is said, so the real decision drowns. A brief states the role, the goal, what good looks like, what the agent may decide at the edge, what it must escalate, and when to stop. Authority that outruns the clarity of the brief is the setup for a confident, wrong action. A handoff transfers responsibility for open work, not just context, so it also carries the state: what finished, what changed, what remains. The new owner restates the brief before acting.

## Decision contract

- **Claim checked:** the receiving agent or owner can answer what it may do, what must stay true, what evidence it owes, and when to stop, with authority bounded no wider than the brief; for open work, the last finished action, changed conditions, and remaining scope are stated and the owner confirmed them before acting.
- **Artifact observed:** the change record, mode, and role -> a context pack, plus a `turnover.md` when open work changes hands.
- **Decision affected:** block -- whether the agent or new owner may start or resume, and within what authority.
- **Failure class:** boundary-overreach (authority wider than the brief) or open-loop-handoff (state implied, or acting before confirmation).
- **Next action:** bound the authority and state forbidden actions; require the restatement; escalate when credentials, production data, or release power appear.

## When to Use

- An agent is about to edit files, run commands, call tools, or prepare release evidence and needs its role, authority, and stop conditions first.
- A reviewer or verifier needs a one-screen summary of a change record before starting.
- Open work moves to another agent, reviewer, releaser, or support owner, or a long thread resumes after the context changed.

## When Not to Use

- The same owner continues uninterrupted with full context.
- A Quick change whose context is already in `risk.md` and `proof.md`, or an agent with no power to act that only needs a file explained.
- The work is done and the record already holds the evidence and the decision.

## Inputs

- The change record, mode, role (builder, reviewer, verifier, releaser, incident lead, researcher), and phase.
- Affected files, allowed commands and tools, forbidden actions, approval gates, evidence required, and the instruction files in force.
- The context-pack schema in `docs/02-operating-system/context-packs.md`, including its memory slot (baselines, OPEX, open deficiencies).
- For open work: last finished action, completed artifacts, changed conditions, failed attempts, unchecked assumptions, and the next owner.

## Process

**Every brief:**

1. Name the role, the question to decide, and the goal anchor (goal, signs of success, non-goals) so it survives a context reset. Name who is affected and who must be consulted.
2. Include only the record files, affected files, source rows, and commands needed for the next decision. Link; do not paste.
3. State the phase (explore, candidate, audit, accept) and the archetype the wording puts the agent in. "Clean this up" invites deletion without a baseline; "make it work" invites volume that outruns review (`docs/02-operating-system/archetype-lens.md`).
4. State the agent's power over files, commands, network, credentials, approvals, and the release; the claims it must not make; the targets not to touch; and when to stop.
5. Give a one-line risk summary (mode and tier), a basis summary, and the open gaps. Name the critical next action, the likely mistake, and the guard against it.

**When the brief follows earlier work in the same task:** add the last finished action and the conditions that changed. That is enough for a subagent the same owner is directing.

**When responsibility for open work moves to a new owner, or a thread resumes after its context changed:**

6. Carry the state in `turnover.md`: last finished action, completed artifacts, evidence produced, changed conditions, failed attempts, unchecked assumptions, controlled items, hold points, and the next decision gate.
7. Have the new owner restate scope, authority, proof owed, and stop conditions before acting. Keep new build work out of the handoff.

## Outputs

- A context-pack section or file: role, goal anchor, phase and archetype, risk and basis summary, open gaps, scoped files and commands, authority bounds, forbidden actions, evidence owed, stop conditions, next action.
- For a transfer, a `turnover.md` with the resume point, changes, remaining work, next gate, and the new owner's confirmation.

## Verification

- A reader can say what they may do, what must stay true, what evidence is owed, and when to stop, without the chat history.
- The brief does not ask anyone to load the whole repo or every standard without a reason.
- For a transfer, the new owner's restatement matches the brief.

## Escalation

- Stop if requested actions exceed the brief's authority, or the new owner cannot restate the limits.
- Escalate when credentials, network effects, production data, release power, public claims, or unresolved evidence gaps are involved.

## Common Rationalizations

- "More context is safer." Extra context hides the real decision and burns tokens.
- "The agent can work out its permissions." Tool power has to be stated.
- "The next agent can figure it out." Handoffs fail when state is only implied, and chat is not a controlled record.

## Red Flags

- No forbidden actions or no allowed files and commands.
- No last finished action or changed conditions when the work was already under way.
- The new owner is told to act before confirming scope and stop conditions.
- Source lineage pasted in whole instead of linked.

## Prompt

```text
Brief, or hand off, this work the Nuclear-grade way.

Inputs:
- packet, mode, phase, and role:
- decision question and goal anchor (goal, success signs, non-goals):
- affected files; allowed and forbidden commands, tools, and targets; approval gates:
- evidence required; instruction files in force and which wins on conflict:
- open work changing hands or resuming? (yes/no)
- if yes: last finished action, completed artifacts, changed conditions, remaining work, outgoing and incoming owner

Return a short context pack: role, decision question, goal anchor, phase and archetype with its likely drift, authority limits, forbidden claims and targets, evidence owed, stop conditions, critical next action and likely error.
If open work is changing hands, add the turnover state and a prompt for the new owner to restate scope, authority, proof owed, and stop conditions before acting.
```

## Source-lineage note

An original context-discipline and turnover pattern drawing on turnover, communication, place-keeping, flagging, and task-briefing practices in DOE-HDBK-1028-2009 and on public configuration-management, secure-development, AI-risk, and systems-engineering sources, mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE compliance or formal assurance.
