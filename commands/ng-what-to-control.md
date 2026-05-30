# ng-what-to-control

## Purpose

Name the items a Nuclear-grade change must keep under control (CM) — the approved versions you protect and watch for drift. This is a portable command prompt.

## Use when

- A change touches prompts, models, dependencies, tools, docs, templates, skills, commands, validators, releases, runbooks, or public claims.
- Reviewers need to know which version is approved, and what drift would matter.

## Do not use when

- The work is a tiny Quick change that holds no state anyone needs to trust.

## Inputs

- The change goal, and the diff or the files it plans to touch.
- The path to the existing change record (the packet).
- `docs/02-operating-system/controlled-items.md`.

## Prompt text

List the items this change must keep under control (CM).

Inputs:
- change:
- packet:
- affected files/items:

Return a short table. For each item, give: the item, its type, its current state, its intended state, why it is controlled, a link to its evidence (or the gap), its owner, and what should trigger a re-check. Do not list unrelated repo files. Do not imply formal assurance or compliance.

## Files created or modified

- `.nuclear/changes/<slug>/controlled-items.md` when this is started.
- `risk.md`, `basis.md`, or `plan.md` if a short list is enough.

## Expected outputs

- The list of items under control.
- What should trigger a re-check.
- The items or claims you are leaving out on purpose, and any gaps.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating Git history as enough to keep the approved version under control.
- Listing the whole repo instead of the items this change controls.
- Leaving out prompts, docs, source-map rows, or agent permissions because they are not code.

## Legal/assurance boundary note

A controlled-items record backs up reviewable engineering decisions. It does not create formal QA records, certification, compliance, safety, security, procurement adequacy, or regulatory approval.
