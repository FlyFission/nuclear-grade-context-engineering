# Trace: typed acceptance contract and adversarial fixtures

## Change context

- Slug: acceptance-contract-v2
- Related basis record: [`basis.md`](basis.md)
- Related verification record: [`verification.md`](verification.md)
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-07

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Evidence ID / link | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | separate typed fields, no approval value | `basis.md` | `plan.md` | `build_acceptance` | local proof | `verification.md` E-001 | ship | pass |
| REQ-002 | eligibility rule | `basis.md` | `plan.md` | `_release_eligibility` | local proof | `verification.md` E-001, E-003 | ship with residual risk | pass |
| REQ-003 | bound, stale, invalid | `basis.md` | `plan.md` | `verify_receipt` | local proof | `verification.md` E-001, E-002 | ship | pass |
| REQ-004 | legacy never eligible | `basis.md` | `plan.md` | `read_acceptance` | local proof | `verification.md` E-001 | ship | pass |
| REQ-005 | consumers agree, exit codes unchanged | `basis.md` | `plan.md` | `handle_validate`, MCP tool | local proof | `verification.md` E-001 | ship | pass |
| REQ-006 | propagation advisory only | `basis.md` | `plan.md` | receipt reads it; `validate_packet` does not | local proof | `verification.md` E-001, E-003 | ship | pass |

## Evidence chain

```text
External roadmap review: a verdict must not read as approval, and "implemented" is not "effective"
  -> REQ-001..006 (basis)
  -> receipt.py, cli.py, mcp_server.py, consequence policy (design)
  -> 32 fixtures by property, 7 weakened-control reruns, a sweep of 82 earlier records (verification)
  -> agent-generated evidence, re-run by CI; maintainer review and merge (custody, authority)
  -> ship with the gaps named
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No owner-labelled ground truth for `blocked` and `undetermined` | 23 of 82 earlier records withhold eligibility; some may be format problems | carry to `ship.md` | maintainer | enforcement of `--require-eligible` |
| Approval replay and out-of-packet artifact swaps are not detected | two attacks the roadmap names | recorded as strict expected failures; carried to `ship.md` | maintainer | decision custody lands |
| Propagation has no dependency edges | alternatives, shared assumptions, conditional validity are not modeled | carried to `ship.md` | maintainer | typed dependency model |

## Required links

- [`basis.md`](basis.md), [`verification.md`](verification.md), [`ship.md`](ship.md)

## Exit criteria

- Every requirement traces to the code and evidence with a status.

## Source-lineage note

Original Nuclear-grade trace; lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
