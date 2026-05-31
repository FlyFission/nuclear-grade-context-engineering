# ng-incident

## Purpose

Run a live incident the stabilize-first way — name a commander, separate facts from hypotheses, prefer reversible actions, communicate on a cadence, and drive corrective actions to closure. This is a portable command prompt.

## Use when

- Production is down or degraded, data is at risk, security is in question, or users are harmed.
- An agent took a harmful action, or a release is failing its abort criteria.
- Several people or agents need one source of truth and one decision-maker during a live event.

## Do not use when

- The work is routine and reversible with no live harm.
- The event is over and the task is the lesson, not the response.
- A standing known problem needs logging, not a live response.

## Inputs

- The current symptom, when it started, and what changed just before.
- Who is responding, and who can authorize rollbacks, failovers, or comms.
- The reversible actions available and the risk of each.
- The channels and the cadence for status updates.

## Prompt text

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

## Files created or modified

- `.nuclear/changes/<slug>/incident.md` from `templates/standard/incident.md`.
- New entries in the deficiency register and a handoff to `opex.md`.

## Expected outputs

- One commander, clear roles, and a fact-vs-hypothesis timeline.
- Reversible-first decisions recorded with their owners.
- Corrective actions with owners and closure triggers.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- No single commander, or several people directing conflicting actions.
- Hypotheses written into the timeline as facts.
- Status going quiet for long stretches during the event.
- Closing with corrective actions that have no owner or no closure trigger.

## Legal/assurance boundary note

Running an incident this way helps you stabilize and preserve the truth of what happened. It does not create formal verification and validation, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
