# Trace: WS1 consequence engine

## Change context

- Slug: ws1-consequence-engine
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-10-30

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | highest matching rule sets the mode | `basis.md` | `plan.md` step 2 / `nuclear_grade/consequence.py#classify` | max-wins over matching rules | local proof | `verification.md` E-001 | ship | pass |
| REQ-002 | only new, open, path-naming, valid records cover | `basis.md` | `plan.md` step 3 / `nuclear_grade/consequence.py#_cover` | new-record-only coverage | local proof | `verification.md` E-002 | ship | pass |
| REQ-003 | human approval from a non-author, non-bot account | `basis.md` | `plan.md` step 3 / `nuclear_grade/consequence.py#_human_approvers` | approval filter | local proof | `verification.md` E-003 | ship | pass |
| REQ-004 | base policy, policy-self rule, fail closed | `basis.md` | `plan.md` step 2 / `nuclear_grade/consequence.py#load_policy` | policy from base | local proof | `verification.md` E-004 | ship | pass |
| REQ-005 | net-new, non-negated claims only | `basis.md` | `plan.md` step 4 / `nuclear_grade/consequence.py#_claims_in` | sentence and lead-in context | local proof | `verification.md` E-005 | ship with residual risk | pass |
| REQ-006 | globs match the gate's | `basis.md` | `plan.md` step 1 / `nuclear_grade/globmatch.py` | parity test | local proof | `verification.md` E-006 | ship | pass |

## Evidence chain

```text
Self-declared mode (risk)
  -> REQ-001..006 (basis)
  -> classify + _cover + approval filter (design)
  -> tests/test_consequence.py, tests/test_globmatch.py, backtest (verification)
  -> agent-generated evidence, re-run independently by CI; maintainer review (custody)
  -> ship with residual risk: heuristic claim detection; not yet wired into CI
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Claim detection is heuristic | paraphrased claims can evade it; ordinary wording can trip it | accept; human review stays the control, owner labels tune the policy | maintainer | next policy change |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to code and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
