# ng-baseline

## Purpose

Record accepted controlled configuration state after review, merge, release, or public-doc changes. This is a portable command prompt.

## Use when

- A Standard packet ships.
- Public docs, prompts, models, dependencies, tools, skills, commands, templates, validators, or release artifacts are accepted.
- Operation or review feedback requires a re-baseline.
- OPEX changed accepted state or revalidation triggers.

## Do not use when

- Evidence is not ready and the work is still under review.
- The change is a local Quick edit with no release or trust-bearing configuration state.

## Inputs

- Packet path.
- Controlled items and impact screen.
- PR/commit/release/artifact identity.
- Verification and ship records.

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

Return a baseline record with included state, excluded state, evidence links, residual gaps, and revalidation or re-baseline triggers. Do not imply formal assurance or compliance.

## Files created or modified

- `.nuclear/changes/<slug>/baseline.md` when activated.
- `ship.md` if a compact baseline section is enough.

## Expected outputs

- Baseline identity.
- Included/excluded controlled items.
- Revalidation and re-baseline triggers.
- OPEX links when learning changed the baseline.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating a commit SHA alone as the baseline record.
- Omitting exclusions and accepted gaps.
- Forgetting revalidation triggers for dependencies, prompts, models, tools, or public claims.

## Legal/assurance boundary note

Baseline records are workflow evidence. They are not formal V&V, compliance, certification, safety, security, procurement, or regulatory records unless separately adopted under a qualified external program.
