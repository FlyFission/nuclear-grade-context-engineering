# Trace

**Purpose:** Tie each claim to its basis, its control feature, its evidence, and its status.

## Change context

- Slug: trust-propagation-two-party
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17

## Trace summary

Use status labels: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Effective trust is the minimum over counted claim statuses | `basis.md` | `plan.md` step 1 / `nuclear_grade/propagation.py` | `check_promotion` and `effective_status` | local proof | `verification.md` | ship | pass |
| REQ-002 | A pass claim self-verified by its evidence author is flagged | `basis.md` | `plan.md` step 2 / `nuclear_grade/two_party.py` | `check_two_party` | local proof | `verification.md` | ship | pass |
| REQ-003 | Wire both checks into `validate_packet` after normalization | `basis.md` | future follow-up packet | future `_check_*` calls | decision authority | `verification.md` | defer | planned |

## Evidence chain

```text
Risk / need
  -> Basis / requirement (REQ-001, REQ-002, REQ-003)
  -> Control / design feature (propagation and two_party modules)
  -> Verification evidence (unit tests, full suite, doctor, packet validation)
  -> Release decision / rollback / monitoring / baseline trigger (ship.md)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| REQ-003 integration not done | The gates are inert until wired in | defer | Ben Huffer | After the claim table is normalized |
| Claim-table schema varies across packets | Propagation cannot compute reliably yet | defer | Ben Huffer | When normalization work is scoped |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: `nuclear_grade/propagation.py`, `nuclear_grade/two_party.py`, `tests/test_propagation.py`, `tests/test_two_party.py`

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim to basis to evidence to release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on requirements tracing, verification, keeping the approved version under control (CM), software assurance, secure development, and release readiness, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
