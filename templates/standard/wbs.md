# Standard WBS and Folder-Map Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Split one deliverable into a work breakdown (WBS) — organized by product, covering 100% of the work, with no overlaps — then build the folder structure from it, so the scope and layout can be checked before you build.

**Activation threshold:** Use for Standard changes whose deliverable has several parts, or whose file and folder layout is not decided yet and needs a scope you can defend.

**Minimum useful version:** a numbered WBS table, one dictionary row per element, and a folder map with a naming and depth check.

**Overhead trap:** Do not build a WBS for a single-file change. Stop splitting at the work-package line, and do not blindly nest one folder per WBS level.

---

## Change context

- Slug:
- Related risk record: `risk.md`
- Related plan record: `plan.md`
- Owner:
- Date:

## Mission and Level 1 product

- Mission anchor confirmed (objective, success criteria, non-goals)? yes/no:
- Level 1 product or outcome (the single top node):
- Mode: quick / standard

## WBS table (outline-numbered, product-oriented)

| Outline no. | Element (noun) | Parent | Type (product / common / work-package) |
|---|---|---|---|
| 1 | | - | product |
| 1.1 | | 1 | product |
| 1.1.1 | | 1.1 | work-package |

## WBS dictionary (one row per element, no blanks)

| Outline no. | Scope | In / out of scope | Deliverable | Interfaces | Acceptance | Size | Owner | Dependencies |
|---|---|---|---|---|---|---|---|---|
| 1.1.1 | | | | | | | | |

## 100% rule and mutual-exclusivity check

| Parent | Children cover 100%? | No sibling overlap? | Notes / explicit gaps |
|---|---|---|---|
| 1 | yes/no | yes/no | |

## Common elements (named once, not copied)

-

## Folder map (derived from WBS outline numbers)

Each element maps to exactly one folder or file. Names: lowercase, one word-separator (a hyphen or an underscore), dates in YYYY-MM-DD form (the ISO-8601 standard), one dot for the extension, and a limited depth. The Model Workspace Protocol stage prefix `NN_` (a number, then an underscore) is the one allowed naming exception. Every folder traces back to a WBS outline number or a disposition rule.

| WBS outline no. | Path | File or folder | Disposition (keep / transient / archive / generated) | Note |
|---|---|---|---|---|
| 1.1 | | | | |

## Folder decision checklist (run before creating any folder)

- [ ] Earned (grouping reduces load) [ ] Cohesive (one reason to change) [ ] Low coupling out
- [ ] Maps to one WBS no. or disposition rule [ ] Single home for the concept
- [ ] Named safely (lowercase, hyphen/underscore, ISO-8601, one dot, sortable)
- [ ] Depth within ~8 levels and path within 255 chars [ ] Documented (README + disposition note)

## Model Workspace Protocol layer (only for sequential agent-workflow workspaces)

| Stage folder | Context contract present (Inputs / Process / Outputs)? | Reference vs working separated? | Review gate? |
|---|---|---|---|
| 01_ | | | |

## Naming and depth audit

| Rule | Pass / fail | Evidence (grep or count) |
|---|---|---|
| Names lowercase with one word-separator (the MWP `NN_` stage prefix is the exception) | | |
| Dates only in YYYY-MM-DD form (ISO-8601) | | |
| Max depth within ~8 levels | | |
| Max path within 255 characters | | |
| Single source of truth (no dual homes) | | |
| No orphan folders (each maps to a WBS no. or disposition rule) | | |

## Conflicts with existing conventions

| Existing path / convention | Proposed change | Why | Owner decision |
|---|---|---|---|
| | | | |

## Required links

- `risk.md`
- `plan.md`
- `trace.md`

## Exit criteria

- The WBS covers 100% of the work with no overlaps, and every element has a dictionary entry.
- The folder map traces every folder to a WBS element or a disposition rule, and passes the naming and depth check.
- Conflicts with existing conventions are flagged for an owner to decide, not quietly overwritten.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on splitting work by product and on records management: the DOE Work Breakdown Structure Handbook, MIL-STD-881F, the NASA WBS Handbook, GAO-20-195G, the Model Workspace Protocol (arXiv:2603.16021), NARA Bulletin 2015-04, and NIST file-naming guidance, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
