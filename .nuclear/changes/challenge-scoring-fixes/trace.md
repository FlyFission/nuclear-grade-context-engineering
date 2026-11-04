# Trace: Three challenge scoring fixes found in trial runs

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `rigging()` and `check_tests_kept()` in `challenge/score.py` | E-001, E-003 | pass |
| REQ-002 | same | E-001 | pass |
| REQ-003 | `INVALID_RECORD`, `GOOD`, `wrote_invalid_record()` in `challenge-results/build.py` | E-002, E-003 | pass |
| REQ-004 | `wrote_invalid_record()` | E-002 | pass |
| REQ-005 | `challenge-results/METHOD.md` | E-004 | pass |
| REQ-006 | `_TIME_PREFIX` and `_release_commitment()` in `challenge/score.py` | E-006, E-003 | pass |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
