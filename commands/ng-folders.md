# ng-folders

## Purpose

Derive and audit a clean folder and file structure from a WBS or an existing tree, grouping by cohesion and disposition, naming for platform safety and sort order, and applying the Model Workspace Protocol when the structure is a sequential agent workflow. This is a portable command prompt.

## Use when

- Laying out a new repo, service, feature, or agent workspace tree.
- Deciding where a new file or module belongs.
- A directory has become a junk drawer and no longer maps to the work.
- Materializing a WBS into folders or reorganizing an existing tree.

## Do not use when

- A single file has an obvious home, or the tree is already clean and you are only renaming.
- The layout is fully dictated by an external framework's mandatory structure.
- The task is ownership, CI, or supply-chain enforcement (use the dedicated skills).

## Inputs

- The WBS and dictionary (`wbs.md`) when present; otherwise the scope to decompose.
- The current repo layout and any conventions doc.
- Disposition or retention intent per element (keep, transient, archive, generated).
- Platform or tooling constraints.

## Prompt text

```text
Derive and audit a folder/file structure.

Inputs:
- WBS or scope: <wbs.md path, or the deliverable to decompose>
- paradigm: <production-codebase | agent-workflow-workspace>
- existing tree to respect: <paths or none>
- naming convention: lowercase, hyphen or underscore (pick one), ISO-8601 dates,
  one dot for the extension, no spaces or special characters

Do this in order:
1. Branch on paradigm. Production codebase: deliverable roots plus a small
   approved set of common elements; the folder tree is the WBS projected to
   disk. Agent workflow workspace: numbered stage folders (01_, 02_), each with
   a context file stating Inputs, Process, Outputs; separate persistent
   reference material from per-run output; scripts do mechanical work; a human
   review gate at each stage boundary.
2. Establish source of truth: derive folders from WBS outline numbers, or
   reverse-engineer the implicit breakdown first.
3. For each proposed folder, answer the checklist: earned? cohesive (one reason
   to change)? low coupling out? maps to one WBS element or disposition rule?
   single home? named safely? shallow enough? documented?
4. Name and bound: enforce the naming convention; ban misc/stuff/tmp/new/old/
   backup/final and bare utils; cap depth near 8 levels and path near 255 chars.
5. Give each non-trivial folder a README/dictionary note and a disposition note.
6. Reconcile with the existing tree; propose the minimum new structure; flag
   conflicts rather than overwriting.

Return: the folder map (WBS outline number -> path, with a disposition column),
per-folder notes, and a naming/depth/single-source audit. Do not overwrite a
baselined tree; propose for review.
```

## Files created or modified

- `.nuclear/changes/<slug>/wbs.md` (the folder-map and audit section, when the template is used).
- No files unless separately authorized; otherwise the command proposes the structure for review.

## Expected outputs

- A folder map mapping each element to one folder or file, with a disposition column.
- Per-folder README or dictionary stubs and disposition notes.
- A naming, depth, and single-source-of-truth audit (pass or fail per rule).
- For workflow workspaces, the numbered stage layout with per-stage context contracts.
- Conflicts with existing conventions, flagged for an owner decision.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Proposing folders that map to no WBS element and no disposition rule (orphans).
- Junk-drawer names, spaces, capitals, or non-ISO dates.
- Runaway nesting, or one folder per WBS level nested mechanically.
- A concept given two homes, breaking single source of truth.
- Overwriting a baselined tree instead of flagging the conflict.

## Legal/assurance boundary note

A folder structure proposed with this portable command prompt is an engineering aid for organizing work and context. It is not ownership enforcement, CI policy, supply-chain assurance, certification, or regulatory confirmation; those belong to the dedicated trust, baseline, and ship-readiness workflows.
