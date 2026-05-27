# ng-impact

## Purpose

Screen downstream impact from a controlled configuration change. This is a portable command prompt.

## Use when

- A controlled change may affect docs, tests, validators, skills, commands, templates, dependencies, release posture, source lineage, or operations.
- A packet deletes, renames, or changes evidence that other records link to.
- OPEX, near miss, or weak-control evidence suggests downstream records may be stale.

## Do not use when

- A Quick change has one obvious proof step and no downstream artifact impact.

## Inputs

- Controlled item list.
- Packet path.
- Diff or planned change.
- `docs/02-operating-system/change-impact.md`.

## Prompt text

Run a Nuclear-grade change-impact screen.

Inputs:
- packet:
- controlled items:
- planned or actual diff:

For each artifact family, decide update, no-op, defer, or block. Name required updates, stale controls, evidence links, owners, and revalidation triggers. Pay special attention to public claims, validator behavior, source-lineage notes, handoffs, trust checks, OPEX, and release posture.

## Files created or modified

- `.nuclear/changes/<slug>/change-impact.md` when activated.
- Affected docs, tests, skills, commands, templates, or packet records.

## Expected outputs

- Impact screen.
- Required updates or blockers.
- Revalidation triggers.
- Weak or stale controls that need durable updates.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Deleting evidence while packet links still point at it.
- Updating README lifecycle without updating skills, commands, templates, or validator docs.
- Marking docs or validator claims as shipped before behavior exists.

## Legal/assurance boundary note

Impact screening improves reviewability. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
