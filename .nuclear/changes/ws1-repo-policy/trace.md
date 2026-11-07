# Trace: WS1 repository consequence policy

## Change context

- Slug: ws1-repo-policy
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-03

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | trust surfaces need Standard or the top mode | `basis.md` | `plan.md` step 1 / `.nuclear/consequence-policy.json` | path and content rules | local proof | `verification.md` E-001 | ship | pass |
| REQ-002 | ordinary work stays at the floor | `basis.md` | `plan.md` step 3 | `default: none` | local proof | `verification.md` E-001 | ship | pass |
| REQ-003 | wording modes per owner decision 2 | `basis.md` | `plan.md` step 3 | claim rules | local proof | `verification.md` E-001 | ship with residual risk | pass |
| REQ-004 | CI and gate rules are not overridable | `basis.md` | `plan.md` step 3 | `overridable: false` | local proof | `verification.md` E-001 | ship | pass |
| REQ-005 | Dependabot pin bumps use the lane | `basis.md` | `plan.md` step 1 | `dependency_lane` | local proof | `verification.md` E-002 | ship | pass |

## Evidence chain

```text
Six owner decisions (master plan WS1)
  -> REQ-001..005 (basis)
  -> .nuclear/consequence-policy.json (design)
  -> tests/test_repo_policy.py, path-match check, 49-commit backtest (verification)
  -> agent-generated evidence, re-run by CI; maintainer review and merge (custody, authority)
  -> ship as policy only; CI does not read it until the advisory job lands
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No owner-labelled ground truth | the 13 shortfalls may be over-classification | carry to `ship.md`; label before enforcing | maintainer | enforcement change |
| `gate-cli` matches identifiers, not every gate-relevant line | an edit to `handle_required_mode` that names none of them stays at the floor | carry to `ship.md`; move the handler into `consequence.py` | maintainer | next engine change |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to the policy and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
