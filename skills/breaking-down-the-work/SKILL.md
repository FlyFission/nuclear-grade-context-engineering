---
name: breaking-down-the-work
description: Splits scope into a product-first work breakdown that follows the 100% rule, keeps pieces from overlapping, uses outline numbers, and gives every piece a dictionary entry. Use when an epic, feature, or new subsystem needs a clean split into deliverables, or one source of truth before folders or work begin. Do not use for a one-file edit or a backlog item already broken down.
---

# Breaking Down the Work

## Overview

A work breakdown (WBS) splits one deliverable into smaller pieces someone can own, with no gaps and no overlaps, plus a dictionary that defines every piece. "Product-first" means the pieces are the things you build (nouns), not the actions you take (verbs). The work breakdown is the spine that estimates, folders, ownership, and traceability hang from.

Three things can wreck it. Under-coverage: some scope is orphaned and no one owns it. Over-coverage: invented or gold-plated scope that no one asked for. And a third drift where verbs pose as the backbone and hide products that are actually missing. This skill holds two rules: the 100% rule (the pieces add up to exactly the whole, no more and no less) and no overlaps. It also forces a dictionary entry for every piece. That way the breakdown can be reviewed before any folder or line of code exists.

## When to Use

- An epic, feature, or new subsystem needs breaking down before planning or layout.
- A folder tree or repo structure is about to be designed and needs a scope basis you can defend.
- Scope keeps growing and no one can say whether the plan is complete or has overlaps.
- Several agents or people need one shared map of the work with no overlaps.
- A `.nuclear/changes/<slug>/` packet needs its inside structure decided on principle.

## When Not to Use

- A single-file or quick edit with an obvious target and no smaller deliverables under it.
- A backlog item that is already broken down, owned, and backed by a dictionary.
- A live incident you have to contain before you stop to reflect.
- The user wants a schedule, a Gantt chart, a cost estimate, or a project-management certification. A work breakdown feeds those, but it is not them.

## Inputs

- The end deliverable or goal, stated in one line.
- The mission anchor (`.nuclear/mission.md` or the `## Mission anchor` in `risk.md`) and the charter, when there is one.
- Known deliverables, constraints, and any stated non-goals or scope put off for later.
- The existing repo tree and naming conventions, when the work breakdown will be turned into real folders.
- `templates/standard/wbs.md` when you use it.

## Process

1. Name the single top deliverable as level 1. If you cannot name one product, stop. You have a goal, not a deliverable, and the breakdown will leave gaps.
2. Break it down product-first. Split each parent into the nouns it is made of (components, subsystems, documents, data), not the verbs done to it. Verbs live only in a clearly labeled activity layer below a work package.
3. Apply the 100% rule at every parent. The children must cover exactly the parent's scope, no more and no less. Write any put-off scope as a clear gap line instead of leaving it unsaid.
4. Apply no overlaps and the one-home rule. Every piece belongs to exactly one parent, and no two siblings claim the same work. Fix overlap by re-cutting the boundary or by pulling shared work up into one common piece. Never fix it by copying.
5. Break down only until each leaf is doable. Stop when a leaf is one piece of work someone can own, estimate, and verify (the 8/80 sense check, roughly two to three levels). Going deeper than the work-package line is overhead, not rigor. Match the depth to the mode.
6. Number with outline traceability (`1`, `1.2`, `1.2.3`). The number is the lasting ID that the folder map, the dictionary, and cross-references all key on.
7. Write the dictionary. For each piece, record the scope, what is in and out of scope, the deliverable, the interfaces, the acceptance criteria, a rough size, the owner, and the dependencies. A piece with no dictionary entry cannot be estimated or owned.
8. Use the same taxonomy everywhere. The work breakdown is the one taxonomy you reuse for ownership, folder grouping, CI grouping, and risk labels. That keeps one source of truth.
9. Self-check (see Verification), then output the work-breakdown table plus the dictionary. Hand off to `organizing-project-folders` to turn it into a folder structure. When the work will be built by another agent or session, also hand each leaf to `plan.md` as a delegable build-sequence slice written as a stage contract — its prerequisites, its Inputs by exact `file#section` with a context budget, its Outputs, the proof that closes it, and a stop or done condition. The full form is `templates/standard/stage-contract.md`; the doctrine is `docs/02-operating-system/agentic-workflow-architecture.md`.

## Outputs

- A work breakdown as an outline-numbered table, product-first.
- A dictionary row per piece: scope, in and out of scope, deliverable, interfaces, acceptance, size, owner, dependencies.
- Named common pieces held once, not copied across siblings.
- A clear put-off-scope or gap line wherever the 100% rule was bounded.
- A handoff note to folder structuring.
- For delegated execution, a pointer from each leaf work-package to its `plan.md` build-sequence slice, written as a stage contract (prerequisites, Inputs by `file#section` + context budget, Outputs, per-slice proof, stop/done condition). See `briefing-an-agent`, `handing-off-work`, and `templates/standard/stage-contract.md`.

## Verification

- 100% rule: for each parent, the children's scope statements cover it with nothing missing and nothing invented. Any gap is written, not left unsaid.
- No overlaps and one home: no piece appears under two parents; no two siblings overlap.
- Product-first: level 2 and 3 names are nouns. Verbs appear only under a labeled activity layer.
- Dictionary complete: every outline number has a filled-in dictionary entry.
- Leveling: every leaf is a piece someone can own, estimate, and verify. None is broken down below the point where that adds value.
- Reviewer test: for any piece, a reviewer can answer what product it is, who owns it, what interfaces it serves, and what would prove it done.

## Escalation

- Stop when you cannot name one top deliverable. The goal is a goal, not a product.
- Escalate to the owner when the children cannot add up to the parent without overlap, or when the breakdown reveals work you cannot estimate or do not understand.
- Escalate when the user needs an official cost or schedule document, which is outside this skill.
- Escalate before forcing a boundary that conflicts with a saved known-good structure. See `recording-a-known-good-version`.

## Common Rationalizations

- "I'll just list the tasks." Tasks are verbs; a work breakdown is product nouns. A task list hides gaps and overlaps.
- "Close enough to 100%." Close enough is exactly where orphaned scope hides. Name the gap.
- "Two siblings can both own this." Overlap means double-counted work and unclear ownership, not convenience.
- "The dictionary is obvious from the names." A name is not scope. A piece with no definition cannot be owned.
- "Deeper is more rigorous." Breaking down past the work package is just tracking overhead.
- "The breakdown grew, so the mission grew." Scope growth past the anchor is drift. See `staying-on-mission`.

## Red Flags

- Children that plainly do not cover the parent, with no stated gap.
- The same work reachable through two branches of the tree.
- Verbs ("update", "refactor") used as level 2 or 3 piece names.
- A piece with no dictionary entry or no owner.
- A "miscellaneous" or "other" bucket soaking up unrelated scope.
- Outline numbers with gaps or duplicates, or a leaf no one can estimate.

## Source-lineage note

This skill is an original software workflow influenced by public product-oriented decomposition practice: the DOE Work Breakdown Structure Handbook (product-oriented WBS, the 100% rule, common element structures, the WBS dictionary), MIL-STD-881F, the NASA WBS Handbook, and GAO-20-195G, with mutual-exclusivity and work-package framing encoded as original workflow, all mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE, DoD, NASA, or GAO compliance, formal assurance, certification, cost-estimate validity, or regulatory adequacy.
