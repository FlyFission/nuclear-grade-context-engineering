# Baseline Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Record the controlled state everyone agreed is correct after review.

**Activation threshold:** Use when a Standard change ships, the release stance changes, or trust-bearing docs, prompts, models, dependencies, skills, commands, templates, validators, or source-lineage records are accepted.

**Minimum useful version:** the baseline name and identity, the controlled items included, the evidence links, the accepted gaps, and the triggers for a new baseline.

**Overhead trap:** A baseline is not a changelog. It records the accepted controlled state and what would make it out of date.

---

## Baseline identity

- Baseline name:
- Commit / PR / release / artifact:
- Owner:
- Date:
- Related packet:

## Included controlled items

| Item | Accepted state | Evidence link | Residual gap | Revalidation trigger |
|---|---|---|---|---|
| | | | | |

## Exclusions

| Item or claim excluded | Why excluded | Follow-up / trigger |
|---|---|---|
| | | |

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `controlled-items.md` if activated
- `change-impact.md` if activated

## Exit criteria

- The baseline can be rebuilt exactly from its identity.
- The items included and the items left out are stated plainly.
- Accepted gaps have owners or triggers.
- The triggers for a re-check or a new baseline are named.

## Source-lineage note

Original Nuclear-grade baseline template inspired by public sources on configuration management, software lifecycle, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
