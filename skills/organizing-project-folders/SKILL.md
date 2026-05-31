---
name: organizing-project-folders
description: Designs a clean folder and file layout as real architecture, building it from a work breakdown or an existing tree, grouping by what changes together and what happens to it, with platform-safe sortable names and a short note per folder. Use when laying out a repo or agent workspace, deciding where a file belongs, or fixing a junk-drawer folder. Do not use for a single obvious file path or renaming inside an already-clean tree.
---

# Organizing Project Folders

## Overview

Folders are a real engineering decision, not an afterthought. Each folder is a choice about what to group. A good folder maps to one piece of the work breakdown or one disposition rule (what eventually happens to its contents: kept, temporary, archived, or generated). It holds things that change together. In other words, it has high cohesion (its contents share one reason to change) and low coupling (it does not depend tightly on other folders). Its name is safe on any platform, sorts cleanly, and is easy for tools to read.

This skill puts a folder-decision checklist in front of the agent, so folders get reasoned about instead of created by default. When the structure is a step-by-step agent workflow, it also applies the Model Workspace Protocol: numbered stage folders, a context file per stage, layered context, and review gates between stages.

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

1. Pick the pattern first. Decide whether you are structuring a production codebase (a product-first tree: deliverable roots plus a small approved set of common pieces) or an agent workflow workspace (the Model Workspace Protocol). Use the matching pattern.
2. Set the source of truth. If a work breakdown exists, build folders from its outline numbers. If not, work out the implied breakdown first, or hand off to `breaking-down-the-work`.
3. Run the folder-decision checklist for every proposed folder: Is it earned? Does its content share one reason to change? Are its ties to other folders loose? Does it map to exactly one work-breakdown piece or one disposition rule? Is it the single home for this idea? Is it named safely?
4. For the workflow pattern, apply the Model Workspace Protocol: numbered stage folders, a context file per stage with Inputs, Process, and Outputs, lasting reference material separate from each run's working output, and a human review gate at each stage boundary.
5. Name for platform safety and clean sorting. Use lowercase letters and numbers, ISO-8601 dates, one dot only for the file extension, no spaces or special characters, and zero-padded sequence numbers. The one accepted exception is the Model Workspace Protocol stage prefix `NN_`. Normally capitalized files (`README.md`, `LICENSE`, `CONTEXT.md`, `CLAUDE.md`) are exempt from the lowercase rule. Ban junk-drawer names (`misc`, `stuff`, `tmp`, `new`, `old`, `backup`, `final`, bare `utils`).
6. Limit depth and path length. Prefer flatter trees. Cap nesting near eight levels and total path length near 255 characters.
7. Give each non-trivial folder a short README or dictionary note (purpose, what belongs, what does not, owner) and a disposition note (keep, temporary, archive, generated).
8. Compare with the existing tree before proposing changes. Respect current conventions, propose the least new structure you can, and flag conflicts instead of overwriting.
9. Output the folder map and the result of the naming, depth, and single-source check.

## Outputs

- A folder map: each piece mapped to one folder or file, ordered by outline number, with a disposition column.
- Per-folder README or dictionary stubs and disposition notes.
- For workflow workspaces, the numbered stage layout with a context file per stage.
- A naming, depth, and single-source-of-truth check (pass or fail per rule).
- Conflicts with existing conventions, flagged for an owner decision.

## Verification

- **Naming**: every path is lowercase (apart from normally capitalized files), uses the chosen word separator (MWP `NN_` prefix excepted), uses ISO-8601 dates, has one dot, and has no spaces or special characters.
- **Depth and path**: no path goes past roughly eight levels or 255 characters.
- **Mapping**: every folder maps to one work-breakdown piece or one disposition rule. No orphan folders. No idea has two homes.
- **Cohesion**: each folder's contents share one reason to change. Cross-folder references are few and noted.
- **Documentation**: each non-trivial folder has a README or dictionary note and a disposition note.
- **Workflows**: each numbered stage has a context file with Inputs, Process, and Outputs, and a review gate.

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

## Source-lineage note

This skill is an original software workflow influenced by public folder-as-architecture and records-management practice: the Model Workspace Protocol (Van Clief and McDermott, "Interpretable Context Methodology", arXiv:2603.16021; numbered stage folders, layered context, stage contracts, review gates), NARA Bulletin 2015-04 and NIST file-naming guidance (platform-safe naming, ISO-8601 dates, depth and path limits, folder-to-disposition mapping), the DOE Work Breakdown Structure Handbook (common element structures), and Unix-pipeline and modular-decomposition principles encoded as original workflow, all mapped in `docs/00-standards-foundation/source-map.md`. It does not create compliance, formal assurance, certification, or regulatory adequacy.
