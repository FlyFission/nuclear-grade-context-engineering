# Work Breakdown and Folders

**Purpose:** Activate work-breakdown decomposition and folder structuring at the right points in the lifecycle so scope, ownership, and layout are reasoned, not improvised.

## Why this exists

The Specify and Plan phases assume scope is understood and the place work will live is obvious. For an epic, a new subsystem, or a fresh repo or agent-workspace layout, that assumption fails: scope grows without anyone noticing the gap, and directories accrete into junk drawers. Work-breakdown decomposition makes scope exhaustive and non-overlapping; folder structuring makes the tree an intentional projection of that scope rather than an accident.

## When to activate

Activate at Specify or Plan when any of these apply:

- An epic, feature, or new subsystem needs a defensible, complete scope basis before planning.
- A new repo, service, or agent-workspace tree is about to be laid out.
- Scope keeps growing and no one can say whether the plan is complete or overlapping.
- A directory has become a junk drawer and no longer maps to the work.

Quick changes skip this; one or two lines in `plan.md` are enough.

## How it fits in the lifecycle

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
                            ↑          ↑
              work-breakdown      folder structuring
              decomposition       (tree from outline numbers)
```

Work-breakdown decomposition runs at Specify/Plan and feeds `plan.md` (the work packages become the build sequence) and `trace.md` (each work package maps to a claim and its evidence). Folder structuring runs at materialization, before Execute, projecting the WBS outline numbers onto the directory tree.

## Minimum useful version

- A single Level 1 product, decomposed two to three levels to work packages.
- A dictionary entry per element (scope, deliverable, acceptance, owner).
- A folder map that traces every folder to a WBS element or a disposition rule, passing a naming and depth audit.

Use `skills/decomposing-work-breakdown/SKILL.md` and `skills/structuring-agentic-folders/SKILL.md` for the full process.
Use `commands/ng-wbs.md` and `commands/ng-folders.md` as portable agent prompts.
Use `templates/standard/wbs.md` when the WBS and folder map warrant a recorded artifact.

## Relationship to mission drift, baselines, and enforcement

The WBS bounds scope, so `controlling-mission-drift` has a concrete anchor to test growth against. Folder structuring respects, and does not silently overwrite, a baselined layout; conflicts route to `baselining-configuration`. Ownership, CI gates, and supply-chain trust are deliberately out of scope here: they belong to `identifying-controlled-items`, `reviewing-ship-readiness`, and `checking-dependency-and-model-trust`. This doc structures work and layout; it does not enforce them.

## Boundaries

This activation point is not:

- a schedule, Gantt, or authoritative cost estimate;
- a project-management certification;
- a mandated directory standard;
- a governance or compliance control.

The 8/80 sizing heuristic and the depth and path caps are heuristics, not rules.

## Source-lineage note

Influenced by public product-oriented decomposition and records-management sources (the DOE Work Breakdown Structure Handbook, MIL-STD-881F, the NASA WBS Handbook, GAO-20-195G, the Model Workspace Protocol at arXiv:2603.16021, NARA Bulletin 2015-04, and NIST file-naming guidance), mapped as supporting context in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
