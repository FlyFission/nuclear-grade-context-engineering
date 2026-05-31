# ng-learn

## Purpose

Turn real experience into lasting fixes. Take a near miss, an incident, a bad handoff, a shallow analysis, a surprise in review, or user feedback, and turn it into a durable change to the workflow. We call these lessons from real operation (OPEX). This is a portable command prompt.

## Use when

- An agent went past its authority, or nearly did.
- A bad handoff, a made-up claim, an escaped defect, a weak review, a stale baseline, or user confusion showed up.
- An update to the method, a source, or an influence produced new prose but no lasting change to a control.
- A lesson should update a basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline.

## Do not use when

- You must contain the problem first, before any analysis.
- The request is to assign blame rather than improve the controls.
- No lasting control can reasonably change, and a note explaining why you are closing it is enough.

## Inputs

- The event, the affected packet/baseline/file, the evidence, the impact, the immediate fix, and the lasting change you are considering.

## Prompt text

```text
Create a Nuclear-grade OPEX record (lessons from real operation).

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

Produce a no-blame OPEX record. Each finding must either change a lasting control or be closed with a clear reason why not.
```

## Files created or modified

- `opex.md`
- The related basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline, if the lesson changes a control.

## Expected outputs

- The finding, the impact, the action or the reason for closing it, the verification, the owner, and the trigger.
- A re-check or new-baseline trigger if a version under control changed.
- A lasting control change when one is available.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- The lesson stays in the chat history only.
- The lesson records regret but changes no basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline.
- The record names a person or a model as the sole cause.
- A finding has no lasting fix and no reason given for closing it.

## Legal/assurance boundary note

Lessons-from-operation (OPEX) records support learning and keeping versions under control. They do not create formal corrective-action, quality-assurance, compliance, certification, safety, security, procurement, or regulatory records, unless you separately adopt them under an external program.
