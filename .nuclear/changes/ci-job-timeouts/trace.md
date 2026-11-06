# Trace: CI job timeouts

## Change context

- Slug: ci-job-timeouts
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-06
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | every repository job has a bounded timeout | `basis.md` | `plan.md` steps 1-2 / `.github/workflows/*.yml` | `timeout-minutes` | local proof | `verification.md` E-001, E-002 | ship with residual risk | pass |
| REQ-002 | the scaffold workflow has one | `basis.md` | `plan.md` step 3 / `nuclear_grade/cli.py` | `timeout-minutes: 10` | local proof | `verification.md` E-001 | ship with residual risk | pass |
| REQ-003 | a test fails on each defect | `basis.md` | `plan.md` step 4 / `tests/test_workflow_timeouts.py` | parametrized defect cases | local proof | `verification.md` E-001 | ship | pass |

## Evidence chain

```text
Hung job holds a runner for the 360-minute default (basis)
  -> REQ-001..003
  -> 9 job headers, scaffold text, tests/test_workflow_timeouts.py (design)
  -> failed-first run, full suite, measured durations, independent review (verification)
  -> agent-generated evidence, re-run by CI; maintainer review and merge (custody, authority)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Only one release run observed | a cap could be too tight on a slower day | carry to `ship.md`; watch the next tagged release | maintainer | next tag |
| Environment approval wait vs timeout unknown | the `pypi` job could time out while waiting | carry to `ship.md` | maintainer | next tag |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to the change and evidence with a status.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
