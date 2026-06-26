# Standard Trace Record

**Purpose:** Tie each requirement to the exact edit that satisfies it and the evidence that confirms it.

**Activation threshold:** Standard mode: claims span several docs, a skill, the generated command card, the maxims, and the source map.

**Minimum useful version:** the claim IDs, the basis links, the control/design features, the evidence links, the ship stance, and the status labels.

**Overhead trap:** Do not build a giant trace table. Trace only the claims that matter.

---

## Change context

- Slug: graded-approach-sharpening
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-17

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Administrative floor: no packet, the commit message is the record | `basis.md` | `plan.md` step 1–2 / `activation-thresholds.md`, `modes.md`, `change-control-packets.md`, `risk-tiers-and-modes.md`, `rating-change-risk` | Floor section + trigger row + shortcut + same-axis notes + floor screen | local proof | `verification.md` (doctor + validate + read) | ship | pass |
| REQ-002 | Any tripwire lifts the change to at least Quick | `basis.md` | `plan.md` step 1–2 / floor edits + skill `## Common Rationalizations` | Tripwire list aligned to the router's Standard-plus traps | local proof | `verification.md` (skill contract tests + read) | ship | pass |
| REQ-003 | Grading scales how, not whether; the baseline is never waived | `basis.md` | `plan.md` step 4 / `MAXIMS.md`, `modes.md`, `CORE.md` | Non-waiver maxim + reinforcement | local proof | `verification.md` (`test_public_docs`) | ship | pass |
| REQ-004 | Grade the change independently of the standing item; take the higher | `basis.md` | `plan.md` step 2 / `rating-change-risk` `## Process`, `risk-tiers-and-modes.md` | Change-vs-item rule | local proof | `verification.md` (parity test + read) | ship | pass |
| REQ-005 | Performance history raises the mode above intrinsic risk | `basis.md` | `plan.md` step 2 / `activation-thresholds.md` dimension, skill clause | Performance-history modulator wired to `deficiency-register.md` | local proof | `verification.md` (read + link check) | ship | pass |
| REQ-006 | Lineage recorded once, DOE-anchored; cross-jurisdiction refs concept-only | `basis.md` | `plan.md` step 6 / `source-to-concept-crosswalk.md`, `source-map.md`, `modes.md` | Crosswalk rows + Tier 1b `public-url-needed` refs | local proof | `verification.md` (boundary read + doctor links) | ship | pass |

## Evidence chain

```text
Risk / need (graded approach implicit at the low end; logic stated only operationally)
  → Basis / requirement (REQ-001..006)
  → Control / design feature (floor + tripwires + non-waiver maxim + change-vs-item + performance history + DOE-anchored lineage)
  → Verification evidence (gen-commands --check, tokens, doctor, pytest, ruff, packet validate)
  → Release decision (ship after PR review) / rollback (one revert) / baseline (the merge commit)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Foreign-source URLs unverified | Marked `public-url-needed`, so not yet usable as direct lineage | accept | FlyFission | A current public URL is confirmed in-repo |
| Doctrine quality is partly review-based | Tests prove structure, not that the wording is the best translation | mitigate | FlyFission | PR review or future OPEX |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: the edited docs/skill above; `tests/` (contract + parity + public-docs tests)

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade trace record inspired by public sources on requirements tracing, verification, configuration management, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
