---
name: structuring-the-work
description: Splits scope into a product-first work breakdown (100% rule, no overlaps, outline numbers, a dictionary entry per piece) and, when it lands on disk, lays it out as folders that group what changes together, with platform-safe sortable names and a note per folder. Use when an epic or subsystem needs a clean split, a repo or agent workspace needs a layout, or a folder has become a junk drawer. Do not use for a one-file edit or an obvious file path.
---

# Structuring the Work

## Overview

A work breakdown (WBS) splits one deliverable into pieces someone can own, with no gaps and no overlaps, plus a dictionary that defines each piece. "Product-first" means the pieces are things you build (nouns), not actions (verbs). It is the spine that estimates, ownership, delegation, and folders hang from. A folder layout is the same decision on disk: each folder maps to one piece of the breakdown or one disposition rule (kept, temporary, archived, generated) and holds things that change together. Do only the half you need: a breakdown with no folders, folders from an existing breakdown, or both.

## Decision contract

- **Claim checked:** children cover exactly their parent (100% rule) with no sibling overlap and a dictionary entry per outline number; every folder maps to one piece or disposition rule, has one reason to change, and passes the naming and depth checks.
- **Artifact observed:** the deliverable, mission anchor, `templates/standard/wbs.md`, and the current tree -> an outline-numbered breakdown with dictionary, and a folder map with per-folder notes.
- **Decision affected:** block for the breakdown (plan-ready or not); warn for the layout (accept or rework).
- **Failure class:** non-mece-breakdown (orphaned, invented, or overlapping scope) or junk-drawer-layout.
- **Next action:** name the gap or re-cut the boundary; escalate to the owner on overlap that will not resolve or on conflict with a recorded known-good layout.

## When to Use

- An epic, feature, or subsystem needs splitting before planning, estimating, or delegation, or scope keeps growing with no one able to say whether the plan is complete.
- A repo, service, or agent workspace needs a layout, a file needs a home, or a folder no longer maps to the work.
- A step-by-step agent workflow is being designed as folders on disk.

## When Not to Use

- A one-file edit, a file with an obvious home, or a rename inside a clean tree.
- A backlog item already broken down, owned, and defined; a layout fixed by a framework's required structure.
- A schedule, cost estimate, or certification; a breakdown feeds those but is not them.

## Inputs

- The one-line deliverable, the mission anchor, known non-goals and deferred scope, and the mode.
- The existing tree and conventions, and what eventually happens to each piece.

## Process

**Breakdown:**

1. Name one top deliverable. If you cannot name a product, stop: you have a goal, not a deliverable.
2. Split each parent into the nouns it is made of. Verbs live only in a labeled activity layer under a work package.
3. At every parent, children cover exactly its scope. Write deferred scope as an explicit gap line. Each piece has one parent; fix overlap by re-cutting or lifting shared work into one common piece, never by copying.
4. Stop at a leaf one person can own, estimate, and verify (the 8/80 sense check, about two or three levels). Number by outline (`1`, `1.2`, `1.2.3`).
5. Write a dictionary row per piece: scope, in and out, deliverable, interfaces, acceptance, rough size, owner, dependencies. For delegated work, point each leaf to its `plan.md` slice written as a stage contract (`templates/standard/stage-contract.md`).

**Layout:**

6. Pick the pattern: a product-first codebase tree (deliverable roots plus a small set of common pieces), or an agent-workflow workspace (numbered stage folders `01_`, `02_`, each with a context file of Inputs, Process, Outputs, lasting reference kept apart from run output, and a human review gate at each stage boundary). `docs/02-operating-system/agentic-workflow-architecture.md` says when folders are enough and when a durable runtime is needed.
7. For each proposed folder ask: has it earned a folder, does its content share one reason to change, are its ties to other folders loose, does it map to one piece or disposition rule, is it the single home, is it named safely and shallow, is it documented?
8. Name lowercase with one chosen separator, ISO-8601 dates, one dot for the extension, no spaces. Files capitalized by convention (`README.md`, `LICENSE`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and the like) and the `NN_` stage prefix are accepted exceptions. Ban `misc`, `stuff`, `tmp`, `new`, `old`, `backup`, `final`, and bare `utils`. Keep depth near eight levels and paths near 255 characters, and do not blindly nest one folder per breakdown level.
9. Compare with the existing tree, propose the least new structure, and flag conflicts instead of overwriting.

## Outputs

- An outline-numbered, product-first breakdown with a dictionary row per piece, named common pieces, and gap lines.
- A folder map (outline number to path, with a disposition column), per-folder README stubs, and a naming, depth, and single-home check.
- Conflicts with existing conventions, flagged for the owner.

## Verification

- For each parent, children cover it with nothing missing or invented; no piece sits under two parents; level 2 and 3 names are nouns.
- Every outline number has a dictionary entry; every leaf can be owned, estimated, and verified.
- Every folder maps to one piece or rule, one idea has one home, paths pass naming and depth rules, and each workflow stage has a context file and a human review gate at its boundary.

## Escalation

- Stop when no single deliverable can be named.
- Escalate when you cannot reach one source of truth without an architecture decision, when children cannot add up without overlap, when the breakdown reveals work no one can estimate, or when a proposed layout conflicts with a recorded known-good layout (`controlling-approved-versions`).

## Common Rationalizations

- "I'll just list the tasks." Tasks are verbs; a task list hides gaps and overlaps.
- "Close enough to 100%." That is where orphaned scope hides. Name the gap.
- "I'll make a utils folder for now." "For now" junk drawers never get cleaned.
- "This file fits in two places, so I'll copy it." Two homes destroys the single source of truth.

## Red Flags

- Children that plainly miss part of the parent with no stated gap, or the same work under two branches.
- Verbs as level 2 or 3 names; a piece with no dictionary entry or owner; a "misc" bucket.
- Spaces, non-ISO dates, or deep nesting in paths; a workflow stage with no context file or review gate.

## Prompt

```text
Structure this work the Nuclear-grade way.

Inputs:
- end deliverable (one line), mode, non-goals and deferred scope:
- need: breakdown / folder layout / both
- pattern if laying out: production-codebase / agent-workflow-workspace
- existing tree to respect:

Breakdown: state one top deliverable; split by product nouns; apply the 100% rule and one-home rule at every parent with explicit gap lines; stop at ownable work packages; number by outline; write a dictionary row per piece.
Layout: for an agent workflow, use numbered stage folders with a context file each and a human review gate at each boundary; map folders to outline numbers deliberately, not one per level; run the folder checklist; enforce naming, depth, and path rules; add a README and disposition to each non-trivial folder; propose the smallest change and flag conflicts.

Return the breakdown table and dictionary and/or the folder map with notes and checks. Do not produce a schedule, cost estimate, or compliance claim, and do not overwrite a recorded tree.
```

## Source-lineage note

An original workflow influenced by public product-oriented decomposition and folder-as-architecture practice: the DOE Work Breakdown Structure Handbook, MIL-STD-881F, the NASA WBS Handbook, GAO-20-195G, the Model Workspace Protocol (arXiv:2603.16021), and NARA Bulletin 2015-04 and NIST file-naming guidance, mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE, DoD, NASA, or GAO compliance, formal assurance, certification, cost-estimate validity, or regulatory adequacy.
