# Baseline Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Record the accepted controlled configuration state after review.

**Activation threshold:** Use when a Standard change ships, release posture changes, or trust-bearing docs, prompts, models, dependencies, skills, commands, templates, validators, or source-lineage records are accepted.

**Minimum useful version:** Baseline identity, included controlled items, evidence links, accepted gaps, and re-baseline triggers.

**Overhead trap:** A baseline is not a changelog. It records accepted controlled state and what would make it stale.

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

- Baseline identity is reproducible.
- Included and excluded items are explicit.
- Accepted gaps have owners or triggers.
- Future revalidation/re-baseline triggers are named.

## Source-lineage note

Original Nuclear-grade baseline template inspired by public configuration-management, lifecycle, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
