---
name: turning-over-agent-work
description: Use when handing off AI-agent, reviewer, verifier, releaser, or resumed-thread work with unfinished scope, changed conditions, authority limits, or open evidence.
---

# Turning Over Agent Work

## Overview

Turnover transfers responsibility, not just context. The next human or agent must know what changed, what remains, what authority applies, and when to stop.

## When to Use

- A subagent, reviewer, verifier, releaser, or support owner will continue work.
- A long thread is being resumed after context changed.
- Work has open evidence, unfinished decisions, or authority limits.
- Release, incident, or OPEX work must move to another owner.

## When Not to Use

- The work is complete and the packet already records evidence and decision.
- A tiny Quick change needs only a diff and proof note.
- The request is only to summarize a file without transferring responsibility.

## Inputs

- Packet path, current lifecycle phase, and selected mode.
- Completed work, changed conditions, active assumptions, and open gaps.
- Allowed files/commands/tools, forbidden actions, evidence obligations, and stop conditions.
- Next owner, role, reviewer, verifier, or releaser.

## Process

1. Name the outgoing state: last completed action, completed artifacts, and evidence produced.
2. Name changed conditions, anomalies, failed attempts, and assumptions not yet validated.
3. Flag exact controlled targets, do-not-touch targets, hold points, and approval gates.
4. Name the next decision, next action, critical action, likely error, and control.
5. Require the incoming owner to restate scope, authority, proof, and stop criteria before acting.

## Outputs

- `turnover.md`, context-pack turnover section, or release/support handoff note.
- Resume point, changed conditions, remaining work, and next decision gate.
- Closed-loop acceptance by the incoming owner when consequence warrants it.

## Verification

- A new agent can continue without reading the full chat history.
- The handoff states what is done, what remains, what changed, and what must not be done.
- Authority and stop conditions are explicit enough to obey.

## Escalation

- Stop if the next owner cannot restate the authority boundary.
- Escalate if credentials, production data, release authority, public claims, or unresolved evidence gaps are involved.

## Common Rationalizations

- "The next agent can infer it." Handoffs fail when state is implied.
- "Everything important is in chat." Chat is not a controlled record.
- "Just continue from here." A resume point without authority and evidence is not turnover.

## Red Flags

- No last completed action.
- No changed-conditions section.
- New implementation work is mixed into the handoff.
- The incoming owner is asked to act before confirming scope and stop criteria.

## Source-lineage note

This skill is an original software-workflow translation of turnover, effective communication, place-keeping, flagging, task briefing, and review practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
