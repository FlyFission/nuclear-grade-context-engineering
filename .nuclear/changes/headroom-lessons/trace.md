# Trace: lessons from Headroom

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `summarize()` in `challenge-results/build.py` | E-001 | pass |
| REQ-002 | `uncommitted_inputs()`, `inputs_commit()` and `run_trial()` in `challenge-results/run.py` | E-002 | pass |
| REQ-003 | `identity_problems()` and `render()` in `challenge-results/build.py` | E-003 | pass |
| REQ-004 | `challenge-results/METHOD.md` (Pinning, How many runs, Changes to this method) | E-005 | pass |
| REQ-005 | `llms.txt`, `tests/test_public_docs.py` | E-004 | pass |
| REQ-006 | `ROADMAP.md` v0.2 | E-005 | pass |
| All | No regressions | E-006 | pass |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
