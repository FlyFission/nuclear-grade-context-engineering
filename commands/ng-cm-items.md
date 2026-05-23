# ng-cm-items

## Purpose

Identify controlled configuration items for a Nuclear-grade change. This is a portable command prompt.

## Use when

- A change touches prompts, models, dependencies, tools, docs, templates, skills, commands, validators, releases, runbooks, or public claims.
- Reviewers need to know which state is approved and what drift matters.

## Do not use when

- The work is a tiny Quick change with no trust-bearing state.

## Inputs

- Change objective and diff or planned affected files.
- Existing packet path.
- `docs/02-operating-system/controlled-items.md`.

## Prompt text

Identify the controlled configuration items for this change.

Inputs:
- change:
- packet:
- affected files/items:

Return a compact table with item, type, current state, intended state, why controlled, evidence link or gap, owner, and revalidation trigger. Do not list unrelated repo files. Do not imply formal assurance or compliance.

## Files created or modified

- `.nuclear/changes/<slug>/controlled-items.md` when activated.
- `risk.md`, `basis.md`, or `plan.md` if a compact list is enough.

## Expected outputs

- Controlled item list.
- Revalidation triggers.
- Explicit exclusions or gaps.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating Git history as sufficient configuration control.
- Listing the whole repo instead of change-specific controlled items.
- Omitting prompts, docs, source-map rows, or agent permissions because they are not code.

## Legal/assurance boundary note

Controlled-item records support reviewable engineering decisions. They do not create formal QA records, certification, compliance, safety, security, procurement adequacy, or regulatory approval.
