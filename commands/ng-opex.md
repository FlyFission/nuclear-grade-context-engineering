# ng-opex

## Purpose

Convert operating experience, near misses, incidents, bad handoffs, review surprises, or user feedback into durable workflow updates. This is a portable command prompt.

## Use when

- An agent exceeded or nearly exceeded authority.
- A bad handoff, hallucinated claim, escaped defect, weak review, stale baseline, or user confusion appeared.
- A lesson should update a basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline.

## Do not use when

- Immediate containment must happen before learning analysis.
- The request is to assign blame rather than improve controls.
- No durable control can reasonably change and closure rationale is enough.

## Inputs

- Event, affected packet/baseline/artifact, evidence, impact, immediate correction, and candidate durable update.

## Prompt text

```text
Create a Nuclear-grade OPEX record.

Inputs:
- event or near miss:
- affected packet / baseline / artifact:
- evidence:
- impact:
- immediate correction:
- weak or missing control:
- candidate durable update:
- owner:
- due date or trigger:

Produce a no-blame OPEX record. Each finding must update a durable control or explicitly close with rationale.
```

## Files created or modified

- `opex.md`
- Related basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline if the lesson changes a control.

## Expected outputs

- Finding, impact, action or closure, verification, owner, and trigger.
- Revalidation or re-baseline trigger if controlled state changed.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Lesson stays in chat history only.
- Record names a person or model as sole cause.
- Finding has no durable update or closure rationale.

## Legal/assurance boundary note

OPEX records support learning and configuration discipline. They do not create formal corrective-action, quality-assurance, compliance, certification, safety, security, procurement, or regulatory records unless separately adopted under an external program.
