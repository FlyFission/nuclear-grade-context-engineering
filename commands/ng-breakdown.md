# ng-breakdown

## Purpose

Build a work breakdown for a deliverable — a tree that splits the thing you are building into its parts. The tree must add up to the whole and nothing more (the 100% rule), have no overlap between parts, use outline numbering, and define every part in a short dictionary. Do this so the scope can be checked before any folders or work begin. This is a portable command prompt.

## Use when

- An epic, feature, or new subsystem needs to be broken down before you plan or lay out folders.
- Scope keeps growing and no one can say whether the plan is complete or overlapping.
- A folder tree or repo layout needs a scope you can defend.
- Several agents or people need one shared map of the work, with no overlaps.

## Do not use when

- The change is a single-file or Quick edit with an obvious target.
- The backlog item is already broken down, owned, and backed by a dictionary.
- The user needs a schedule, a cost estimate, or a project-management certification.

## Inputs

- The end deliverable or goal in one line.
- The mode (Quick or Standard) and the stated goal (mission anchor) or charter, when there is one.
- The known deliverables, the constraints, and any non-goals or deferred scope you declared.
- `templates/standard/wbs.md` when used.

## Prompt text

```text
Build a product-oriented work breakdown (a work breakdown structure, or WBS).

Inputs:
- end deliverable (one line): <the single product or outcome>
- mode: <quick|standard>
- known non-goals / deferred scope: <list or none>
- existing tree to respect: <paths or none>

Do this in order:
1. State the single top deliverable as level 1. If you cannot name one
   product, stop and say so: it is a goal, not a deliverable.
2. Break down by product first: split each parent into the parts (nouns) it is
   made of, not the actions (verbs) done to it. Keep verbs in a labeled
   activity layer only.
3. Apply the 100% rule at every parent: the children must cover exactly the
   parent, no more and no less. Write any deferred scope as an explicit gap line.
4. Keep parts separate, with one home each: every part sits under exactly one
   parent, and no two siblings overlap. Lift shared work into one common part
   rather than duplicating it.
5. Stop splitting at the work-package line: one part that someone can own,
   estimate, and verify. A good test is that it takes between about 8 and 80
   hours of work (the 8/80 rule), which is usually about 2 to 3 levels deep.
   Grade the depth by mode.
6. Number with outline traceability (1, 1.2, 1.2.3).
7. Write the dictionary: for each part give its scope, what is in and out of
   scope, the deliverable, the interfaces, how it is accepted, a rough size,
   the owner, and its dependencies.

Return: the outline-numbered breakdown table, the dictionary, the named common
parts, the deferred-scope/gap line, and a self-check that it adds up to 100% with
no overlap. Do not produce a schedule, a cost estimate, or a compliance claim.
Then hand off to ng-folders.
```

## Files created or modified

- `.nuclear/changes/<slug>/wbs.md` (the breakdown table and dictionary, when `templates/standard/wbs.md` is used).
- No files unless that is separately authorized; otherwise the command proposes the breakdown for review.

## Expected outputs

- An outline-numbered, product-first breakdown table.
- A dictionary row per part, with its scope, deliverable, how it is accepted, owner, and dependencies.
- Named common parts and an explicit deferred-scope or gap line.
- A self-check that the parts add up to the whole (the 100% rule) and do not overlap.
- For delegated execution, a per-leaf note of prerequisites, the proof that closes it, and a stop/done condition, so `plan.md` can carry it as a slice (a handoff contract, not a schedule).

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Listing actions (verbs) instead of breaking down products (nouns).
- Children that do not add up to the parent, with the gap left implied.
- The same work placed under two parts (an overlap), or a "miscellaneous" bucket.
- Parts with no dictionary entry or no owner.
- Splitting past the work-package line as if more depth meant more rigor.

## Legal/assurance boundary note

A work breakdown built with this portable command prompt structures the work and scope as engineering evidence. It is not a schedule, an authoritative cost estimate, a project-management certification, formal assurance, or regulatory confirmation.
