# ng-impact

## Purpose

Check what else a change touches — its ripple effects — when that change is to an item kept under control (CM). This is a portable command prompt.

## Use when

- A controlled change may affect docs, tests, validators, skills, commands, templates, dependencies, the release, source lineage, or operations.
- A change record (the packet) deletes, renames, or alters evidence that other records link to.
- Lessons from real operation (OPEX), a near miss, or weak-control evidence suggest some linked records may now be stale.

## Do not use when

- A Quick change has one obvious proof step and touches nothing downstream.

## Inputs

- The list of items under control.
- The path to the change record (the packet).
- The diff, or the planned change.
- `docs/02-operating-system/change-impact.md`.

## Prompt text

Run a Nuclear-grade ripple-effect check.

Inputs:
- packet:
- controlled items:
- planned or actual diff:

For each family of files, decide one of: update, leave as is, defer, or block. Name the updates needed, the controls now stale, the evidence links, the owners, and what should trigger a re-check. Pay close attention to public claims, validator behavior, source-lineage notes, handoffs, trust checks, lessons from operation (OPEX), and the release.

## Files created or modified

- `.nuclear/changes/<slug>/change-impact.md` when this is started.
- The affected docs, tests, skills, commands, templates, or packet records.

## Expected outputs

- The ripple-effect screen.
- The updates needed, or the blockers.
- What should trigger a re-check.
- Weak or stale controls that need a lasting fix.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Deleting evidence while packet links still point at it.
- Updating the README lifecycle without updating the skills, commands, templates, or validator docs.
- Marking docs or validator claims as shipped before the behavior actually exists.

## Legal/assurance boundary note

A ripple-effect check makes the work easier to review. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
