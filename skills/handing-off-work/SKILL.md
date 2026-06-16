---
name: handing-off-work
description: Hands off unfinished work with a closed-loop briefing of state, changed conditions, remaining scope, authority limits, and open evidence. Use when AI-agent, reviewer, verifier, releaser, or resumed-thread work transfers to a new owner. Do not use when the same owner continues uninterrupted with full context.
---

# Handing Off Work

## Overview

A handoff transfers responsibility, not just context. The next person or agent has to know what changed, what is left, what they are allowed to do, and when to stop.

## Decision contract

- **Claim checked:** the receiving owner can resume without the chat history -- the last finished action, changed conditions, remaining scope, authority limits, open evidence, and stop conditions are all stated -- and the owner has restated scope, authority, proof owed, and when to stop before acting.
- **Artifact observed:** the change-record path, current phase, mode, the done/changed/assumed/open state, and the authority limits -> a `turnover.md` with the resume point, what changed, what remains, the next decision gate, and the incoming owner's confirmation.
- **Decision affected:** block -- whether the receiving owner may resume, or must hold and re-question first.
- **Failure class:** open-loop-handoff (state only implied, or the owner acts before confirming scope and stop conditions).
- **Next action:** make the incoming owner restate scope, authority, and stop conditions first; escalate when credentials, production data, or release authority are involved.

## When to Use

- Another agent, a reviewer, a verifier, a releaser, or a support owner will keep working.
- A long thread is being picked up again after the context changed.
- Work has open evidence, decisions not yet made, or limits on what the owner may do.
- Release work, incident work, or a lesson from real operation (OPEX) has to move to another owner.

## When Not to Use

- The work is done and the change record already holds the evidence and the decision.
- A tiny Quick change needs only a diff and a proof note.
- The request is just to summarize a file, with no transfer of responsibility.

## Inputs

- The change-record path, the current phase, and the chosen mode.
- The work that is done, the conditions that changed, the assumptions still in play, and the open gaps.
- Allowed files, commands, and tools; actions that are off limits; the evidence still owed; and when to stop.
- The next owner and their role: reviewer, verifier, or releaser.

## Process

1. Name the state you are handing off: the last action that finished, the artifacts that are done, and the evidence produced.
2. Name the conditions that changed, anything odd, the attempts that failed, and the assumptions not yet checked.
3. Flag the exact items under control, the targets not to touch, the hold points, and the approval gates.
4. Name the next decision, the next action, the most important action, the likely error, and how to guard against it.
5. Make the incoming owner restate the scope, what they may do, the proof needed, and when to stop, before they act.

## Outputs

- A `turnover.md` file, a turnover section in the context pack, or a release or support handoff note.
- The point to resume from, the conditions that changed, the work that remains, and the next decision gate.
- Confirmation back from the incoming owner when the stakes call for it.

## Verification

- A new agent can keep going without reading the full chat history.
- The handoff states what is done, what is left, what changed, and what must not be done.
- The limits on authority and the stop conditions are clear enough to obey.

## Escalation

- Stop if the next owner cannot restate the limits on what they may do.
- Escalate if credentials, production data, release authority, public claims, or unresolved evidence gaps are involved.

## Common Rationalizations

- "The next agent can figure it out." Handoffs fail when the state is only implied.
- "Everything important is in chat." Chat is not a controlled record.
- "Just continue from here." A resume point with no stated authority and no evidence is not a handoff.

## Red Flags

- No record of the last action that finished.
- No section for the conditions that changed.
- New build work is mixed into the handoff.
- The incoming owner is told to act before confirming the scope and the stop conditions.

## Prompt

```text
Create a Nuclear-grade turnover record.

Inputs:
- packet:
- current phase:
- outgoing owner / role:
- incoming owner / role:
- last completed action:
- completed artifacts:
- changed conditions:
- remaining work:
- allowed files/commands/tools:
- forbidden files/commands/tools:
- proof still needed:
- stop or hold conditions:

Produce a short turnover record. Include the critical next action, the likely error, the control, the evidence, and a prompt for the incoming owner to confirm they have it and understand it before they act.
```

## Source-lineage note

This skill is an original software-workflow translation of turnover, effective communication, place-keeping, flagging, task briefing, and review practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
