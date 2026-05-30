# ng-baseline

## Purpose

Record the version everyone agreed is correct — the baseline — after a review, merge, release, or change to public docs. This is a portable command prompt.

## Use when

- A Standard change record (the packet) ships.
- Public docs, prompts, models, dependencies, tools, skills, commands, templates, validators, or release files are accepted.
- Feedback from operation or review means you must save a new baseline.
- Lessons from real operation (OPEX) changed the accepted version or the re-check triggers.

## Do not use when

- The evidence is not ready and the work is still under review.
- The change is a local Quick edit with no release and no state anyone needs to trust.

## Inputs

- The path to the change record (the packet).
- The list of items under control and the ripple-effect screen.
- The PR, commit, release, or file that identifies this version.
- The verification and ship records.

## Prompt text

Create or update the Nuclear-grade baseline record for this change.

Inputs:
- packet:
- baseline identity:
- included controlled items:
- excluded items/claims:
- verification evidence:
- OPEX / near-miss links:
- accepted gaps:

Return a baseline record. Include the version that is saved, the items it covers, the items it leaves out, links to the evidence, the gaps you have accepted, and what should trigger a re-check or a new baseline. Do not imply formal assurance or compliance.

## Files created or modified

- `.nuclear/changes/<slug>/baseline.md` when this is started.
- `ship.md` if a short baseline section is enough.

## Expected outputs

- The version that is saved.
- The items under control that are included, and those left out.
- What should trigger a re-check or a new baseline.
- Links to lessons from operation (OPEX) when learning changed the baseline.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating a commit SHA alone as the baseline record.
- Leaving out the items you excluded and the gaps you accepted.
- Forgetting the re-check triggers for dependencies, prompts, models, tools, or public claims.

## Legal/assurance boundary note

Baseline records are workflow evidence. They are not formal V&V, compliance, certification, safety, security, procurement, or regulatory records, unless you separately adopt them under a qualified external program.
