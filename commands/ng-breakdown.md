# ng-breakdown

## Purpose

Build a product-oriented work breakdown structure (WBS) for a deliverable that obeys the 100% rule, stays mutually exclusive, carries outline numbering, and defines every element in a dictionary, so scope is auditable before folders or work begin. This is a portable command prompt.

## Use when

- An epic, feature, or new subsystem needs decomposition before planning or layout.
- Scope keeps growing and no one can say whether the plan is complete or overlapping.
- A folder tree or repo layout needs a defensible scope basis.
- Multiple agents or people need one shared, non-overlapping map of the work.

## Do not use when

- The change is a single-file or Quick edit with an obvious target.
- The backlog item is already decomposed, owned, and dictionary-backed.
- The user needs a schedule, cost estimate, or project-management certification.

## Inputs

- The end deliverable or objective in one line.
- Mode (Quick or Standard) and the mission anchor or charter when present.
- Known deliverables, constraints, and declared non-goals or deferred scope.
- `templates/standard/wbs.md` when used.

## Prompt text

```text
Build a product-oriented work breakdown structure (WBS).

Inputs:
- end deliverable (one line): <the single product or outcome>
- mode: <quick|standard>
- known non-goals / deferred scope: <list or none>
- existing tree to respect: <paths or none>

Do this in order:
1. State the single top deliverable as WBS level 1. If you cannot name one
   product, stop and say so: it is a goal, not a deliverable.
2. Decompose product-first: break each parent into the nouns it is made of,
   not the verbs done to it. Keep verbs in a labeled activity layer only.
3. Enforce the 100% rule at every parent: children cover exactly the parent,
   no more and no less. Write any deferred scope as an explicit gap line.
4. Enforce mutual exclusivity and the one-home rule: every element under
   exactly one parent; no sibling overlap. Lift shared work into one common
   element rather than duplicating.
5. Stop decomposing at the work-package line: one ownable, estimable,
   verifiable unit (8/80 sense check, ~2-3 levels). Grade depth by mode.
6. Number with outline traceability (1, 1.2, 1.2.3).
7. Write the WBS dictionary: for each element give scope, in/out-of-scope,
   deliverable, interfaces, acceptance, rough size, owner, dependencies.

Return: the outline-numbered WBS table, the dictionary, named common elements,
the deferred-scope/gap line, and a 100%/MECE self-check result. Do not produce a
schedule, cost estimate, or compliance claim. Then hand off to ng-folders.
```

## Files created or modified

- `.nuclear/changes/<slug>/wbs.md` (the WBS table and dictionary, when `templates/standard/wbs.md` is used).
- No files unless separately authorized; otherwise the command proposes the WBS for review.

## Expected outputs

- An outline-numbered, product-oriented WBS table.
- A dictionary row per element with scope, deliverable, acceptance, owner, and dependencies.
- Named common elements and an explicit deferred-scope or gap line.
- A 100% rule and mutual-exclusivity self-check result.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Listing tasks (verbs) instead of decomposing products (nouns).
- Children that do not sum to the parent, with the gap left implied.
- The same work placed under two elements (overlap), or a "miscellaneous" bucket.
- Elements with no dictionary entry or no owner.
- Decomposing past the work-package line as if depth were rigor.

## Legal/assurance boundary note

A WBS built with this portable command prompt structures work and scope as engineering evidence. It is not a schedule, an authoritative cost estimate, a project-management certification, formal assurance, or regulatory confirmation.
