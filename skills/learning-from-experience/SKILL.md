---
name: learning-from-experience
description: Turns incidents, near misses, bad handoffs, review surprises, escaped bugs, and signals from real use into lasting fixes to your safeguards. Use after something went wrong or nearly did and a future safeguard should change. Do not use during a live incident, which comes first, or to blame someone.
---

# Learning From Experience

## Overview

Lessons from real operation (OPEX) only help if they change future work. So treat agent mistakes, near misses, review surprises, sloppy analysis, and support tickets as feedback. Each one shows you where a control was weak. A control is anything that steers behavior, like a test, a checker, a rule, or a permission limit. Use the lesson to make that control stronger.

## Decision contract

- **Claim checked:** the event is stated as actual-versus-standard with a root cause and weak control named, and closes with an owned, verified control fix or a deliberate waiver saying why no fix was needed.
- **Artifact observed:** the event, near miss, or operating signal and the control it touched -> an OPEX record with the finding, action, owner, and evidence or close-out reason.
- **Decision affected:** block -- whether a durable control (test, template, prompt, monitor, checker, or baseline) is updated, or the lesson is explicitly waived with a reason.
- **Failure class:** unlearned-lesson (a fix with no control change, or a record closed with regret instead of a fix).
- **Next action:** assign an owner and a recheck trigger; a repeated weak control escalates to a second independent reviewer.

## When to Use

- A bad handoff, a wrong-file edit, a made-up claim, an agent going past its allowed tools, a bug that escaped to users, or a surprise in review happened.
- Users or operators misread a release, a public claim, a runbook, a template, or an approved version.
- A past change record, skill, command, test, checker, monitor, or template failed to steer behavior the way it should have.
- A change to the rules or sources produced new text but no lasting change to a control.

## When Not to Use

- The event has no lesson that would repeat, and no control could reasonably change.
- You must contain a live incident first; analyze it after.
- The request is to blame someone rather than improve a control.

## Inputs

- The event, near miss, review surprise, operating signal, or user feedback.
- The change record, approved version, file, skill, command, test, checker, monitor, or doc it affected.
- The evidence, the impact, the quick fix you already made, and the chance it happens again.

## Process

1. State the actual condition in plain words, no blame, and name the standard or expected condition it fell short of.
2. Name where it is red — the gap between actual and standard — then find the root cause, not the symptom, and the weak or missing control and which approved version or file it touched.
3. Pick a lasting fix: update a basis, a test, a checker, a template, a skill, a command, a doc, a monitor, a threshold, or an approved version.
4. Do not close the lesson with just regret or an explanation when a real control could change instead.
5. Give the correction an owner, then verify the improvement — or close the lesson on purpose and say why no fix was needed.
6. Feed the lesson into future questioning, planning, verification, and handoffs.

This actual-vs-standard, root-cause, owner, verify structure keeps a retro from drifting into a vague "what went well / what could improve." A standing deficiency that will outlive this lesson belongs in the deficiency register (`tracking-deficiencies`).

## Outputs

- An OPEX record (a lessons-from-operation record) or an issue entry.
- A lasting control fix, or a clear reason why no fix is warranted.
- A trigger to re-verify or re-record the approved version when a controlled item changed.

## Verification

- Every finding has an action, an owner, and either evidence or a reason it was closed.
- Future agents can find the lesson before they repeat the pattern.
- The lesson updates a controlled item, or explains why no update is needed.

## Escalation

- Escalate if the event touched users, data, security, credentials, releases, public claims, or repeated agent power.
- Require a second, independent reviewer when the same weak control shows up more than once.

## Common Rationalizations

- "The agent just made a mistake." Ask what prompt, context, checker, review, or power limit let it happen.
- "We fixed the bug." A fix with no lesson can come back through another path.
- "No one was harmed." A near miss is a cheaper warning than a real incident.

## Red Flags

- The OPEX record has no lasting fix and no reason it was closed.
- The lesson is stuck in chat history.
- The record blames one person or one model as the sole cause.
- The follow-up has no owner and no trigger.

## Source-lineage note

This skill is an original software-workflow translation of operating experience, post-job review, reporting errors and near misses, change management, independent oversight, and no-blame learning practices from DOE-HDBK-1028-2009 as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
