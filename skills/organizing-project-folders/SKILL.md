---
name: organizing-project-folders
description: Designs a clean folder and file layout as real architecture, building it from a work breakdown or an existing tree, grouping by what changes together and what happens to it, with platform-safe sortable names and a short note per folder. Use when laying out a repo or agent workspace, deciding where a file belongs, or fixing a junk-drawer folder. Do not use for a single obvious file path or renaming inside an already-clean tree.
---

# Organizing Project Folders

## Overview

Folders are a real engineering decision, not an afterthought. Each folder is a choice about what to group. A good folder maps to one piece of the work breakdown or one disposition rule (what eventually happens to its contents: kept, temporary, archived, or generated). It holds things that change together. In other words, it has high cohesion (its contents share one reason to change) and low coupling (it does not depend tightly on other folders). Its name is safe on any platform, sorts cleanly, and is easy for tools to read.

This skill puts a folder-decision checklist in front of the agent, so folders get reasoned about instead of created by default. When the structure is a step-by-step agent workflow, it also applies the Model Workspace Protocol: numbered stage folders, a context file per stage, layered context, and review gates between stages. That workflow shape is a named path of its own — see `docs/02-operating-system/agentic-workflow-architecture.md` for when folders are enough (and when a durable runtime is not), and `templates/standard/stage-contract.md` for the full per-stage contract a release-bearing or delegated stage uses.

## Decision contract

- **Claim checked:** every folder maps to one work-breakdown piece or disposition rule with one home, its contents share one reason to change, and its name passes the naming/depth/path checks.
- **Artifact observed:** the work breakdown, its dictionary, and the current tree -> a folder map (outline number to path with disposition), per-folder README stubs, and a naming/depth/single-source check.
- **Decision affected:** warn -- accept vs rework the folder layout, or where a given file belongs.
- **Failure class:** junk-drawer-layout (a folder mapping to no piece or rule, or one idea with two homes).
- **Next action:** name the real idea or stop grouping; escalate to the owner on conflict with a saved known-good convention.

## When to Use

- Laying out a new repo, service, feature, or agent workspace tree.
- Deciding where a new file or module belongs.
- A folder has become a junk drawer and no longer maps to the work.
- Turning a work breakdown into real folders, or reorganizing an existing tree.
- Designing a step-by-step agent workflow as folders on disk instead of framework code.

## When Not to Use

- A single file with an obvious home, or a rename inside an already-clean, conventional tree.
- A live incident you have to contain first.
- A layout fully fixed by an outside framework's required structure. Follow that instead.
- Enforcing ownership, CI gates, or supply-chain trust. Those belong to `choosing-what-to-control`, `checking-release-readiness`, and `vetting-outside-code-and-models`.

## Inputs

- The work breakdown and its dictionary (`templates/standard/wbs.md` or a `wbs.md`) when there is one. Otherwise the scope, which you will break down in reverse.
- The current repo layout and any conventions doc.
- The mission anchor and any platform or tooling limits.
- For each piece, what eventually happens to it (keep, temporary, archive, generated).

## Process

1. Pick the pattern first. Decide whether you are structuring a production codebase (a product-first tree: deliverable roots plus a small approved set of common pieces, where the folder tree is the work breakdown laid onto disk) or an agent workflow workspace (the Model Workspace Protocol). Use the matching pattern.
2. Set the source of truth. If a work breakdown exists, build folders from its outline numbers and turn dictionary entries into per-folder notes. If not, work out the implied breakdown first, or hand off to `breaking-down-the-work`.
3. Run the folder-decision checklist for every proposed folder. Is it earned (does grouping cut the mental load, or would one file do)? Does its content share one reason to change? Are its ties to other folders loose? Does it map to exactly one work-breakdown piece or one disposition rule? Is it the single home for this idea? Is it named safely and kept shallow? Is it documented?
4. For the workflow pattern, apply the Model Workspace Protocol. Numbered stage folders set the order (`01_...`, `02_...`). Each stage has a context file with Inputs, Process, and Outputs. Keep lasting reference material separate from each run's working output. Scripts do the mechanical work. Every output is something you can open and edit, with a human review gate at each boundary.
5. Name for platform safety and clean sorting. Use lowercase letters and numbers, ISO-8601 dates (like 2026-05-30), one dot used only for the file extension, no spaces or special characters, and zero-padded sequence numbers. Pick one word separator (hyphen or underscore) and stick with it. The one accepted exception is the Model Workspace Protocol stage prefix `NN_` (a zero-padded number then an underscore, as in `01_research`), where the underscore marks the sequence boundary. Files that are normally capitalized by convention (`README.md`, `LICENSE`, and Model Workspace Protocol context files such as `CONTEXT.md` and `CLAUDE.md`) are an accepted exception to the lowercase rule. Ban junk-drawer names (`misc`, `stuff`, `tmp`, `new`, `old`, `backup`, `final`, bare `utils`).
6. Limit depth and path length. Prefer flatter trees. Cap nesting near eight levels and total path length near 255 characters. Do not blindly nest one folder per work-breakdown level.
7. Give each non-trivial folder a short README or dictionary note (purpose, what belongs, what does not, owner) and a note on what happens to its contents.
8. Compare with the existing tree before proposing changes. Respect current conventions, propose the least new structure you can, and flag conflicts as findings instead of overwriting a saved known-good layout.
9. Output the folder map (outline number to path, with a disposition column) and the result of the naming, depth, and single-source check.

## Outputs

- A folder map: each piece mapped to one folder or file, ordered by outline number, with a disposition column.
- Per-folder README or dictionary stubs and disposition notes.
- For workflow workspaces, the numbered stage layout with a context file per stage.
- A naming, depth, and single-source-of-truth check (pass or fail per rule).
- Conflicts with existing conventions, flagged for an owner decision.

## Verification

- Naming: every path is lowercase (apart from normally capitalized files like `README.md` and `CONTEXT.md`), uses the chosen word separator (with the Model Workspace Protocol `NN_` stage prefix excepted), uses ISO-8601 dates, has one dot, and has no spaces or special characters.
- Depth and path: no path goes past roughly eight levels or 255 characters.
- Mapping and one home: every folder maps to one work-breakdown piece or one disposition rule. No orphan folders. No idea has two homes.
- Cohesion and coupling: each folder's contents share one reason to change. References across folders are kept few and noted.
- Documentation: each non-trivial folder has a README or dictionary note and a disposition note.
- For workflows: each numbered stage has a context file with Inputs, Process, and Outputs, and a review gate.

## Escalation

- Escalate when the proposed tree conflicts with an established or saved known-good convention. The owner decides; do not override it quietly (see `recording-a-known-good-version`).
- Escalate when you cannot reach one source of truth without an architecture decision.
- Escalate to `breaking-down-the-work` when there is no breakdown to build from.
- For ownership, CI, or supply-chain enforcement, route to the dedicated skills instead of building it in here.

## Common Rationalizations

- "I'll make a utils or misc folder for now." "For now" junk drawers never get cleaned. Name the real idea or do not group at all.
- "Deeper nesting is more organized." Depth has a cost. Flatter is usually clearer and stays within path limits.
- "Spaces and capitals are fine on my machine." They break sorting, scripts, and other platforms.
- "This file fits in two places, so I'll copy it." Two homes destroys the single source of truth. Pick the main one and link to it.
- "The folder name explains itself." Without a note and a disposition, the next agent has to guess.
- "One folder per work-breakdown level keeps it tidy." Blind one-to-one nesting makes the tree too deep. Map levels on purpose.

## Red Flags

- `misc`, `utils`, `temp`, or `stuff` folders, or folders holding one unrelated file each.
- Spaces, special characters, or non-ISO dates in names, or capitals outside normally capitalized files (`README.md`, `CONTEXT.md`).
- Nesting past roughly eight levels, or one idea living in two trees.
- Tight coupling across folders, or a folder that maps to no work-breakdown piece and no disposition rule.
- A workflow stage with no context file or no review gate.
- Undocumented top-level folders.

## Prompt

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

## Source-lineage note

This skill is an original software workflow influenced by public folder-as-architecture and records-management practice: the Model Workspace Protocol (Van Clief and McDermott, "Interpretable Context Methodology", arXiv:2603.16021; numbered stage folders, layered context, stage contracts, review gates), NARA Bulletin 2015-04 and NIST file-naming guidance (platform-safe naming, ISO-8601 dates, depth and path limits, folder-to-disposition mapping), the DOE Work Breakdown Structure Handbook (common element structures), and Unix-pipeline and modular-decomposition principles encoded as original workflow, all mapped in `docs/00-standards-foundation/source-map.md`. It does not create compliance, formal assurance, certification, or regulatory adequacy.
