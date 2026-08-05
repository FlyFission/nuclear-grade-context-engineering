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
