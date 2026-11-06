# Trace: Fix five gaps a code review found in the challenge harness

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `run_trial()` in `challenge-results/run.py` | E-001 | pass |
| REQ-002 | `run_agent()` in `challenge-results/run.py` | E-002 | pass |
| REQ-003 | `run_trial()` in `challenge-results/run.py` | E-003 | pass |
| REQ-004 | `environment()` in `challenge-results/run.py` | E-001 | pass |
| REQ-005 | `wrote_invalid_record()` and `load_rulings()` in `challenge-results/build.py` | E-004 | pass |
| REQ-006 | `pypi-package-page/risk.md`, `command-menu-descriptions/plan.md` and `risk.md` | E-005 | pass |
| REQ-007 | `tests/test_command_contracts.py` | E-005 | pass |
| All | No regressions | E-006 | pass |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
