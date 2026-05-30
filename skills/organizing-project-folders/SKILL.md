---
name: organizing-project-folders
description: Designs a clean folder and file structure as agentic architecture, deriving it from a work breakdown structure or an existing tree, grouping by cohesion and disposition with platform-safe sortable names and a dictionary note per folder. Use when laying out a repo or agent workspace, deciding where a file belongs, or fixing a junk-drawer directory. Do not use for a single obvious file path or renaming inside an already-clean tree.
---

# Structuring Agentic Folders

## Overview

Folders are a first-class engineering decision, not an afterthought. Each one is a grouping commitment that should map to a work-breakdown element or a disposition rule, hold things that change together (high cohesion, low coupling), and carry a name that is platform-safe, sortable, and machine-friendly. This skill puts a folder-decision checklist in front of the agent so directories are reasoned about rather than defaulted, and it applies the Model Workspace Protocol (numbered stage folders, per-stage context contracts, layered context, review gates) when the structure is a sequential agent workflow.

## When to Use

- Laying out a new repo, service, feature, or agent workspace tree.
- Deciding where a new file or module belongs.
- A directory has become a junk drawer and no longer maps to the work.
- Materializing a WBS into folders, or reorganizing an existing tree.
- Designing a sequential agent workflow as filesystem structure rather than framework code.

## When Not to Use

- A single file with an obvious home, or a rename inside an already-clean, conventional tree.
- Incident containment.
- A layout fully dictated by an external framework's mandatory structure (follow that instead).
- Enforcement of ownership, CI gates, or supply-chain trust, which belong to `choosing-what-to-control`, `checking-release-readiness`, and `vetting-outside-code-and-models`.

## Inputs

- The WBS and dictionary (`templates/standard/wbs.md` or a `wbs.md`) when present; otherwise the scope to be reverse-decomposed.
- The current repo layout and any conventions doc.
- The mission anchor and platform or tooling constraints.
- Disposition or retention intent per element (keep, transient, archive, generated).

## Process

1. Branch on paradigm. Decide whether you are structuring a production codebase (product-oriented tree: deliverable roots plus a small approved set of common elements, where the folder tree is the WBS projected to disk) or an agent workflow workspace (Model Workspace Protocol). Apply the matching pattern.
2. Establish the source of truth. If a WBS exists, derive folders from its outline numbers and turn dictionary entries into per-folder notes. If not, reverse-engineer the implicit breakdown first, or escalate to `breaking-down-the-work`.
3. Run the folder-decision checklist for every proposed directory. Is it earned (does grouping reduce load, or is one file enough)? Is it cohesive (one reason to change)? Is coupling out of it low? Does it map to exactly one WBS element or one disposition rule? Is it the single home for this concept? Is it named safely and shallow enough? Is it documented?
4. For the workflow paradigm, apply the Model Workspace Protocol. Numbered stage folders encode order (`01_...`, `02_...`); each stage carries a context file with Inputs, Process, and Outputs; persistent reference material and per-run working output are separated; scripts do the mechanical work; every output is an inspectable edit surface with a human review gate at each boundary.
5. Name for platform safety and sort. Lowercase, alphanumeric, ISO-8601 dates, one dot used only for the extension, no spaces or special characters, and zero-padded sequence numbers. Pick one word-separator (hyphen or underscore) and hold it; the one accepted exception is the Model Workspace Protocol stage prefix `NN_` (a zero-padded number then an underscore, as in `01_research`), where the underscore marks the sequence boundary. Conventionally capitalized marker files (`README.md`, `LICENSE`, and Model Workspace Protocol context files such as `CONTEXT.md` and `CLAUDE.md`) are an accepted exception to the lowercase rule. Ban junk-drawer names (`misc`, `stuff`, `tmp`, `new`, `old`, `backup`, `final`, bare `utils`).
6. Bound depth and path. Prefer flatter trees, cap nesting near eight levels and total path near 255 characters, and do not nest one folder per WBS level mechanically.
7. Give each non-trivial folder a short README or dictionary note (purpose, what belongs, what does not, owner) and a disposition note.
8. Reconcile with the existing tree before proposing changes. Respect current conventions, propose the minimum new structure, and flag conflicts as findings rather than overwriting a baselined layout.
9. Emit the folder map (outline number to path, with a disposition column) and the naming, depth, and single-source audit result.

## Outputs

- A folder map: each element mapped to one folder or file, ordered by outline number, with a disposition column.
- Per-folder README or dictionary stubs and disposition notes.
- For workflow workspaces, the numbered stage layout with per-stage context contracts.
- A naming, depth, and single-source-of-truth audit (pass or fail per rule).
- Conflicts with existing conventions, flagged for an owner decision.

## Verification

- Naming: every path is lowercase (apart from conventional marker files such as `README.md` and `CONTEXT.md`), uses the chosen word-separator (with the MWP `NN_` stage prefix excepted), ISO-8601 dates, one dot, and no spaces or special characters.
- Depth and path: no path exceeds roughly eight levels or 255 characters.
- Mapping and one-home: every folder maps to one WBS element or one disposition rule; no orphan folders; no concept has two homes.
- Cohesion and coupling: each folder's contents share a reason to change; cross-folder references are minimized and noted.
- Documentation: each non-trivial folder has a README or dictionary note and a disposition note.
- For workflows: each numbered stage has a context contract with Inputs, Process, and Outputs, and a review gate.

## Escalation

- Escalate when the proposed tree conflicts with an established or baselined convention; the owner decides, not a silent override (see `recording-a-known-good-version`).
- Escalate when single source of truth cannot be reached without an architectural decision.
- Escalate to `breaking-down-the-work` when there is no breakdown to project from.
- For ownership, CI, or supply-chain enforcement, route to the dedicated skills rather than encoding it here.

## Common Rationalizations

- "I'll make a utils or misc folder for now." For now junk drawers never get cleaned; name the real concept or do not group.
- "Deeper nesting is more organized." Depth is a cost; flatter is usually clearer and within path limits.
- "Spaces and capitals are fine on my machine." They break sort, scripts, and other platforms.
- "This file fits in two places, so I'll copy it." Two homes destroys single source of truth; pick canonical and link.
- "The folder name explains itself." Without a note and disposition the next agent guesses.
- "One folder per WBS level keeps it tidy." Mechanical one-to-one nesting over-deepens the tree; map levels deliberately.

## Red Flags

- `misc`, `utils`, `temp`, or `stuff` directories, or folders holding one unrelated file each.
- Spaces, special characters, or non-ISO dates in names, or capitals outside conventional marker files (`README.md`, `CONTEXT.md`).
- Nesting beyond roughly eight levels, or a concept living in two trees.
- High cross-folder coupling, or a folder that maps to no WBS element and no disposition rule.
- A workflow stage with no context contract or no review gate.
- Undocumented top-level directories.

## Source-lineage note

This skill is an original software workflow influenced by public folder-as-architecture and records-management practice: the Model Workspace Protocol (Van Clief and McDermott, "Interpretable Context Methodology", arXiv:2603.16021; numbered stage folders, layered context, stage contracts, review gates), NARA Bulletin 2015-04 and NIST file-naming guidance (platform-safe naming, ISO-8601 dates, depth and path limits, folder-to-disposition mapping), the DOE Work Breakdown Structure Handbook (common element structures), and Unix-pipeline and modular-decomposition principles encoded as original workflow, all mapped in `docs/00-standards-foundation/source-map.md`. It does not create compliance, formal assurance, certification, or regulatory adequacy.
