# ng-folders

## Purpose

Build and check a clean folder and file layout, starting from a work breakdown or an existing tree. Group files that change together, name them so they are safe across platforms and sort well, and use the staged-workspace layout when the work is a step-by-step agent workflow. This is a portable command prompt.

## Use when

- Laying out a new repo, service, feature, or agent workspace tree.
- Deciding where a new file or module belongs.
- A directory has become a junk drawer and no longer matches the work.
- Turning a work breakdown into folders, or reorganizing an existing tree.

## Do not use when

- A single file has an obvious home, or the tree is already clean and you are only renaming.
- The layout is fully set by an outside framework that requires a fixed structure.
- The task is about ownership, test-run (CI) rules, or supply-chain enforcement (use the dedicated skills).

## Inputs

- The work breakdown and dictionary (`wbs.md`) when there is one; otherwise the scope to break down.
- The current repo layout and any conventions doc.
- For each part, what happens to it over time: keep, transient, archive, or generated.
- Platform or tooling constraints.

## Prompt text

```text
Build and check a folder/file layout.

Inputs:
- WBS or scope: <wbs.md path, or the deliverable to break down>
- paradigm: <production-codebase | agent-workflow-workspace>
- existing tree to respect: <paths or none>
- naming convention: lowercase, hyphen or underscore (pick one), ISO-8601 dates,
  one dot for the extension, no spaces or special characters

Do this in order:
1. Choose the paradigm. Production codebase: one root per deliverable, plus a
   small approved set of shared parts; the folder tree is the work breakdown
   laid out on disk. Agent workflow workspace: numbered stage folders (01_,
   02_), each with a context file that states its Inputs, Process, and Outputs;
   keep lasting reference material separate from per-run output; let scripts do
   the mechanical work; put a human review gate at each stage boundary.
2. Set the source of truth: derive folders from the work breakdown's outline
   numbers, or, if there is none, reverse-engineer the implied breakdown first.
3. For each proposed folder, answer the checklist: has it earned a folder? Does
   it hold together (one reason to change)? Does little leak out of it? Does it
   map to one part of the breakdown or one over-time rule? Does it have a single
   home? Is it named safely? Is it shallow enough? Is it documented?
4. Name and bound it: enforce the naming convention; ban misc/stuff/tmp/new/old/
   backup/final and a bare utils; cap depth near 8 levels and the path near 255
   characters.
5. Give each non-trivial folder a README or dictionary note, plus a note on what
   happens to it over time.
6. Reconcile with the existing tree; propose the smallest new structure; flag
   conflicts instead of overwriting.

Return: the folder map (work-breakdown outline number -> path, with an over-time
column), the per-folder notes, and a check of the naming, the depth, and the
single source of truth. Do not overwrite a baselined tree; propose it for review.
```

## Files created or modified

- `.nuclear/changes/<slug>/wbs.md` (the folder-map and check section, when the template is used).
- No files unless that is separately authorized; otherwise the command proposes the structure for review.

## Expected outputs

- A folder map linking each part to one folder or file, with an over-time column.
- Per-folder README or dictionary stubs and over-time notes.
- A check of the naming, the depth, and the single source of truth (pass or fail per rule).
- For workflow workspaces, the numbered stage layout, each stage with its context contract.
- Any conflicts with existing conventions, flagged for an owner to decide.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Proposing folders that map to no part of the breakdown and no over-time rule (orphans).
- Junk-drawer names, spaces, capitals, or non-ISO dates.
- Runaway nesting, or one folder per breakdown level nested mechanically.
- A concept given two homes, which breaks the single source of truth.
- Overwriting a baselined tree instead of flagging the conflict.

## Legal/assurance boundary note

A folder layout proposed with this portable command prompt is an engineering aid for organizing work and context. It is not ownership enforcement, test-run (CI) policy, supply-chain assurance, certification, or regulatory confirmation; those belong to the dedicated trust, baseline, and ship-readiness workflows.
