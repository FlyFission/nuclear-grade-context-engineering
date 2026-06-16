---
name: responding-to-incidents
description: Runs a live incident the stabilize-first way — name a commander, separate facts from hypotheses, prefer reversible actions, communicate on a cadence, and drive corrective actions to closure. Use when production is broken, data is at risk, or an agent action caused harm. Do not use for routine non-incident work, or as a substitute for the post-incident learning record.
---

# Responding to Incidents

## Overview

In a casualty you stabilize first and analyze second. An incident is run by one named commander, keeps known facts separate from guesses, prefers reversible moves while the picture is unclear, communicates on a fixed cadence, and does not close until corrective actions are tracked to done. The goal is to stop the harm and preserve the truth of what happened, not to find blame in the moment.

## Decision contract

- **Claim checked:** the incident has one named commander, a timeline that keeps confirmed facts separate from hypotheses, and corrective actions that each carry an owner and a definition of done -- none left as "we should."
- **Artifact observed:** the current symptom, what changed, who can authorize rollbacks/failovers/comms, and the reversible actions available -> an `incident.md` (timeline, facts-vs-hypotheses, decisions, comms), owned corrective actions with closure triggers, and a handoff to learning and deficiency records.
- **Decision affected:** block -- whether the incident is stabilized and its corrective actions are owned with closure triggers (it stays open until then).
- **Failure class:** premature-incident-close (closed with unowned actions, or a hypothesis recorded as fact).
- **Next action:** stop a proposed irreversible fix until the cause is confirmed or risk is accepted by a named owner; keep the incident open until actions are owned.

## When to Use

- Production is down or degraded, data is at risk, security is in question, or users are harmed.
- An agent took a harmful action, or a release is failing its abort criteria.
- Multiple people or agents need one source of truth and one decision-maker during a live event.

## When Not to Use

- The work is routine and reversible with no live harm (use the normal change path).
- The event is over and the task is the lesson, not the response (use `learning-from-experience`).
- A standing known problem needs logging, not a live response (use `tracking-deficiencies`).

## Inputs

- The current symptom, when it started, and what changed just before.
- Who is responding, and who can authorize rollbacks, failovers, or comms.
- The reversible actions available, and the risk of each.
- The channels and the cadence for status updates.

## Process

1. Declare the incident and name one commander; everyone else takes a defined role.
2. Stabilize: take the safest reversible action that stops or limits the harm.
3. Keep a running timeline, and label each line as a known fact or a hypothesis.
4. Prefer reversible actions while the cause is unconfirmed; record every decision and who made it.
5. Communicate status on a fixed cadence, even when the status is "no change yet."
6. Hand off cleanly across shifts with state, open actions, and authority limits.
7. Close the live phase only when stable; open corrective actions and route the lesson to learning and deficiency records.

## Outputs

- An `incident.md` record, or an incident section, with timeline, facts-vs-hypotheses, decisions, and comms.
- The corrective actions, each with an owner and a closure trigger.
- A handoff to the post-incident learning record and any new deficiency entries.

## Verification

- One commander is named and the roles are unambiguous.
- The timeline separates confirmed facts from hypotheses throughout.
- Every corrective action has an owner and a definition of done; none are left as "we should."

## Escalation

- Escalate immediately when data loss, security exposure, or user harm is possible.
- Stop a proposed irreversible fix until the cause is confirmed or the risk is explicitly accepted by a named owner.
- Pull in a second responder when the commander is also the one doing the hands-on work.

## Common Rationalizations

- "We know what it is." Acting on an unconfirmed cause is how a small incident becomes a large one.
- "Let's just push the fix." Irreversible fixes during uncertainty remove the way back.
- "We'll write it up later." Without a contemporaneous timeline the truth blurs within hours.
- "It's basically over." It is over when it is stable and the corrective actions are owned, not before.

## Red Flags

- No single commander, or several people directing conflicting actions.
- Hypotheses are recorded as facts in the timeline.
- Status goes quiet for long stretches during the event.
- The incident is closed with corrective actions that have no owner or no closure trigger.

## Prompt

```text
Run this incident the Nuclear-grade stabilize-first way.

Inputs:
- symptom and start time:
- what changed just before:
- responders and who can authorize rollback/failover/comms:
- reversible actions available:
- status channel and cadence:

Return:
- the named commander and the role for each responder
- the safest reversible stabilizing action to take first
- a running timeline with each line labeled fact or hypothesis
- decisions recorded with who made them, reversible-first while the cause is unconfirmed
- the fixed status cadence
- corrective actions, each with an owner and a closure trigger
- the handoff to the post-incident learning and deficiency records

Stabilize first, analyze second. Do not act on an unconfirmed cause with an irreversible fix. Do not imply this is a safety or compliance program.
```

## Source-lineage note

This skill is an original software-workflow translation of stabilize-first casualty-control response (concept lineage from naval damage-control and high-reliability incident practice), grounded in the procedure-use, place-keeping, three-way-communication, turnover, and operating-experience habits in DOE-HDBK-1028-2009, used as public idea lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
