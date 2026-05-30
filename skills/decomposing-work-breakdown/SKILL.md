---
name: decomposing-work-breakdown
description: Decomposes scope into a product-oriented work breakdown structure that obeys the 100% rule and stays mutually exclusive, with outline numbering and a dictionary entry per element. Use when an epic, feature, or new subsystem needs clean deliverable decomposition or a single source of truth before folders or work begin. Do not use for a one-file edit or an already-decomposed backlog item.
---

# Decomposing Work Breakdown

## Overview

A work breakdown structure (WBS) is a product-oriented, exhaustive, non-overlapping decomposition of one deliverable into ownable work packages, plus a dictionary that defines every element. It is the spine that estimates, folders, ownership, and traceability hang from. Two failure modes destroy it: under-coverage (orphaned scope no one owns) and over-coverage (invented or gold-plated scope), with a third drift where verbs masquerade as the backbone and hide missing products. This skill holds the 100% rule and mutual exclusivity, and forces a dictionary entry per element, so the breakdown is auditable before any folder or line of code exists.

## When to Use

- An epic, feature, or new subsystem needs breaking down before planning or layout.
- A folder tree or repo structure is about to be designed and needs a defensible scope basis.
- Scope keeps growing and no one can say whether the plan is complete or overlapping.
- Multiple agents or people need one shared, non-overlapping map of the work.
- A `.nuclear/changes/<slug>/` packet needs its internal structure decided on principle.

## When Not to Use

- A single-file or Quick edit with an obvious target and no sub-deliverables.
- A backlog item that is already decomposed, owned, and dictionary-backed.
- Incident containment that must happen before reflection.
- The user wants a schedule, Gantt, cost estimate, or project-management certification (a WBS feeds those but is not them).

## Inputs

- The end deliverable or objective, stated in one line.
- The mission anchor (`.nuclear/mission.md` or the `## Mission anchor` in `risk.md`) and charter when present.
- Known deliverables, constraints, and declared non-goals or deferred scope.
- The existing repo tree and naming conventions, when the WBS will be materialized.
- `templates/standard/wbs.md` when used.

## Process

1. Name the single top deliverable as WBS level 1. If you cannot name one product, stop: you have a goal, not a deliverable, and decomposition will not be exhaustive.
2. Decompose product-first. Break each parent into the nouns it is made of (components, subsystems, documents, data), not the verbs done to it. Verbs live only in a clearly labeled activity layer below a work package.
3. Enforce the 100% rule at every parent. The children must cover exactly the parent scope, no more and no less. Write any deferred scope as an explicit gap line rather than leaving it implied.
4. Enforce mutual exclusivity and the one-home rule. Every element belongs to exactly one parent, and no two siblings claim the same work. Resolve overlap by re-cutting the boundary or lifting shared work into a single common element, never by duplicating.
5. Level to actionability. Decompose until a leaf is a single ownable, estimable, verifiable work package (the 8/80 sense check, roughly two to three levels), then stop. Decomposition past the work-package line is overhead, not rigor. Grade depth by mode.
6. Number with outline traceability (`1`, `1.2`, `1.2.3`). The number is the durable identity the folder map, the dictionary, and cross-references all key on.
7. Write the WBS dictionary. For each element record scope, in-scope and out-of-scope, deliverable, interfaces, acceptance criteria, rough size, owner, and dependencies. An element with no dictionary entry is unestimable and unownable.
8. Apply same-taxonomy-everywhere. The WBS is the one taxonomy reused for ownership, folder grouping, CI grouping, and risk labels, so the project keeps a single source of truth.
9. Self-verify (see Verification) and emit the WBS table plus dictionary, then hand off to `structuring-agentic-folders` to derive the folder structure.

## Outputs

- A WBS as an outline-numbered table, product-oriented.
- A dictionary row per element: scope, in/out-of-scope, deliverable, interfaces, acceptance, size, owner, dependencies.
- Named common elements held once, not copied across siblings.
- An explicit deferred-scope or gap line wherever the 100% rule was bounded.
- A handoff note to folder structuring.

## Verification

- 100% rule: for each parent, the children's scope statements cover it with nothing missing and nothing invented; any gap is written, not implied.
- Mutual exclusivity and one-home: no element appears under two parents; no sibling scopes overlap.
- Product orientation: level 2 and 3 names are nouns; verbs appear only under a labeled activity layer.
- Dictionary completeness: every outline number has a non-empty dictionary entry.
- Leveling: every leaf is an ownable, estimable, verifiable work package; none decomposed below actionable value.
- Reviewer litmus test: for any element a reviewer can answer what product it is, who owns it, what interfaces it serves, and what would prove it acceptable.

## Escalation

- Stop when no single top deliverable can be named: the objective is a goal, not a product.
- Escalate to the owner when children cannot sum to the parent without overlap, or when decomposition reveals unestimable or unknown work.
- Escalate when the user needs an authoritative cost or schedule artifact, which is outside this skill.
- Escalate before forcing a boundary that conflicts with a baselined structure; see `baselining-configuration`.

## Common Rationalizations

- "I'll just list the tasks." Tasks are verbs; a WBS is product nouns. A task list hides gaps and overlaps.
- "Close enough to 100%." Close enough is exactly where orphaned scope hides; name the gap.
- "Two siblings can both own this." Overlap is double-counted work and ambiguous ownership, not convenience.
- "The dictionary is obvious from the names." A name is not scope; an undefined element is unownable.
- "Deeper is more rigorous." Decomposition past the work package is tracking overhead.
- "The breakdown grew, so the mission grew." Scope growth past the anchor is drift; see `controlling-mission-drift`.

## Red Flags

- Children that plainly do not cover the parent, with no stated gap.
- The same work reachable through two branches of the tree.
- Verbs ("update", "refactor") used as level 2 or 3 element names.
- An element with no dictionary entry or no owner.
- A "miscellaneous" or "other" bucket absorbing unrelated scope.
- Outline numbers with gaps or duplicates; a leaf no one can estimate.

## Source-lineage note

This skill is an original software workflow influenced by public product-oriented decomposition practice: the DOE Work Breakdown Structure Handbook (product-oriented WBS, the 100% rule, common element structures, the WBS dictionary), MIL-STD-881F, the NASA WBS Handbook, and GAO-20-195G, with mutual-exclusivity and work-package framing encoded as original workflow, all mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE, DoD, NASA, or GAO compliance, formal assurance, certification, cost-estimate validity, or regulatory adequacy.
