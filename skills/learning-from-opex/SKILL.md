---
name: learning-from-opex
description: Turns incidents, near misses, bad handoffs, review surprises, escaped defects, and operating signals into durable control updates. Use after something went wrong or nearly did and a future safeguard should change. Do not use during active incident containment, which comes first, or to assign blame.
---

# Learning From OPEX

## Overview

Operating experience is only useful when it changes future work. Treat agent mistakes, near misses, review surprises, shallow analysis, and support signals as control-system feedback.

## When to Use

- A bad handoff, wrong-file edit, hallucinated claim, tool-scope overrun, escaped defect, or review surprise occurred.
- Users or operators misunderstood a release, public claim, runbook, template, or baseline.
- A prior packet, skill, command, test, validator, monitor, or template failed to guide behavior.
- A doctrine, source, or influence update produced prose without a durable control change.

## When Not to Use

- The event has no repeatable lesson and no durable control can reasonably change.
- Immediate containment must happen before analysis.
- The request is to assign blame rather than improve controls.

## Inputs

- Event, near miss, review surprise, operating signal, or user feedback.
- Affected packet, baseline, artifact, skill, command, test, validator, monitor, or doc.
- Evidence, impact, immediate correction, and recurrence risk.

## Process

1. State what happened without blame language.
2. Identify the active error, weak or missing control, and affected baseline or artifact.
3. Choose a durable update: basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline.
4. Reject closure that only records regret or explanation when a durable control can change.
5. Verify the update or explicitly close the lesson with rationale.
6. Feed the lesson into future questioning, planning, verification, or turnover.

## Outputs

- OPEX record or issue entry.
- Durable control update or explicit non-update rationale.
- Revalidation or re-baseline trigger when controlled state changed.

## Verification

- Every finding has an action, owner, and evidence or closure rationale.
- Future agents can find the lesson before repeating the pattern.
- The lesson updates a controlled artifact or explains why no update is warranted.

## Escalation

- Escalate if the event affected users, data, security, credentials, releases, public claims, or repeated agent authority.
- Require independent review when the same weak control appears more than once.

## Common Rationalizations

- "The agent just made a mistake." Ask what prompt, context, validator, review, or authority boundary allowed it.
- "We fixed the bug." A fix without a lesson can repeat through another path.
- "No one was harmed." Near misses are cheaper signals than incidents.

## Red Flags

- OPEX record has no durable update or closure rationale.
- The lesson is trapped in chat history.
- The record names a person or model as the sole cause.
- Follow-up has no owner or trigger.

## Source-lineage note

This skill is an original software-workflow translation of operating experience, post-job review, reporting errors and near misses, change management, independent oversight, and no-blame learning practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
