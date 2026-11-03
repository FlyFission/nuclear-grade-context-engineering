# Work Breakdown and Folders

**Purpose:** This file turns on the work breakdown and folder layout at the right points in the lifecycle, so scope, ownership, and layout are thought through, not improvised.

## Why this exists

The Specify and Plan phases assume the scope is understood and the place the work will live is obvious. For an epic, a new subsystem, or a fresh repo or agent-workspace layout, that assumption breaks. Scope grows and no one notices the gap. Folders pile up into junk drawers. The work breakdown (WBS) makes the scope complete and free of overlap. The folder layout makes the tree a deliberate picture of that scope, not an accident.

## When to activate

Turn this on at Specify or Plan when any of these apply:

- An epic, feature, or new subsystem needs a solid, complete picture of its scope before you plan.
- A new repo, service, or agent-workspace tree is about to be laid out.
- Scope keeps growing and no one can say whether the plan is complete or overlapping.
- A folder has become a junk drawer and no longer maps to the work.

Quick changes skip this. One or two lines in `plan.md` are enough.

## How it fits in the lifecycle

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
                            ↑          ↑
              work-breakdown      folder structuring
              decomposition       (tree from outline numbers)
```

The work breakdown runs at Specify and Plan. It feeds `plan.md` (the work packages become the build order) and `trace.md` (each work package maps to a claim and its evidence). The folder layout runs when you build the tree, before Execute. It maps the work-breakdown outline numbers onto the folders.

## Minimum useful version

- A single top-level product (Level 1), broken down two to three levels into work packages.
- A dictionary entry for each element (scope, deliverable, acceptance, owner).
- A folder map that traces every folder to a work-breakdown element or a disposition rule, and that passes a naming and depth check.

Use `skills/breaking-down-the-work/SKILL.md` and `skills/organizing-project-folders/SKILL.md` for the full process.
Use `commands/ng-breakdown.md` and `commands/ng-folders.md` as portable agent prompts.
Use `templates/standard/wbs.md` when the work breakdown and folder map are worth a recorded file.

## Relationship to mission drift, baselines, and enforcement

The work breakdown bounds the scope, so `staying-on-mission` has a concrete anchor to test growth against. The folder layout respects, and does not quietly overwrite, a layout that has been baselined. Conflicts go to `recording-a-known-good-version`. Ownership, CI gates, and supply-chain trust are left out here on purpose. They belong to `choosing-what-to-control`, `checking-release-readiness`, and `vetting-outside-code-and-models`. This doc shapes the work and the layout. It does not enforce them.

## Boundaries

This activation point is not:

- a schedule, a Gantt chart, or an official cost estimate;
- a project-management certification;
- a required directory standard;
- a governance or compliance control.

The 8/80 sizing rule of thumb and the depth and path caps are rules of thumb, not hard rules.

## Source-lineage note

Influenced by public sources on product-oriented breakdown and records management (the DOE Work Breakdown Structure Handbook, MIL-STD-881F, the NASA WBS Handbook, GAO-20-195G, the Model Workspace Protocol at arXiv:2603.16021, NARA Bulletin 2015-04, and NIST file-naming guidance), mapped as supporting context in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
