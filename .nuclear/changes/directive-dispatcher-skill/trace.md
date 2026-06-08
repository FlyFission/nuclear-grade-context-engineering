# Standard Trace

**Purpose:** Tie each claim to its basis, control, evidence, and ship stance.

---

## Change context

- Slug: directive-dispatcher-skill
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: FlyFission
- Date: 2026-06-08

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Router instructs classify-first (declaration of intent) before acting | `basis.md` | `plan.md` step 2 / `skills/using-nuclear-grade/SKILL.md` | "Classify first — out loud" step | local proof | `verification.md` | ship | pass |
| REQ-002 | MUST-promote trip-wire on the high-consequence traps | `basis.md` | `plan.md` step 2 / SKILL.md Process | imperative trap list | local proof | `verification.md` | ship | pass |
| REQ-003 | Directive behavior guarded against regression | `basis.md` | `plan.md` step 4 / `tests/test_skill_contracts.py` | guard test | local proof | `verification.md` | ship | pass |
| REQ-004 | Edit stays within skill contract + token budget | `basis.md` | `plan.md` step 1 / SKILL.md | required sections; budgets | local proof | `verification.md` | ship | pass |
| (efficacy) | The wording measurably lifts classification rate | `basis.md` | A3 measurement | n/a (advisory) | unknown | deferred | ship with residual risk | deferred |

## Evidence chain

```text
Need: force the risk classification the router currently leaves to chance
  -> Basis: REQ-001..004 (classify-first, trip-wire, guarded, within budget)
  -> Control: directive SKILL.md + guard test
  -> Verification: guard test, skill-contract test, token budget, pytest, ruff, doctor, validate
  -> Release: ship with residual risk (the behavioral-lift proof is the deferred A3 measurement)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Behavioral lift not measured | We assert the router *instructs* the classification, not that it *lifts* the rate | defer | FlyFission | The A3 classification-rate measurement (model-in-the-loop run) |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `skills/using-nuclear-grade/SKILL.md`, `tests/test_skill_contracts.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on requirements tracing and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
