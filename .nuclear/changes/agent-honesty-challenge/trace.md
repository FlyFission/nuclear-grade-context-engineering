# Trace: agent honesty challenge

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `challenge/score.py` `verdict` | E-001 | pass |
| REQ-002 | `check_judge`, `check_tests_kept` | E-001 | pass |
| REQ-003 | `find_record`, `check_no_self_approval`, `check_guard` | E-001 | pass |
| REQ-004 | `load_validator`, `builtin_validate`, `check_names_widening` | E-001, E-002 | pass |
| REQ-005 | `NO_NETWORK_PLUGIN`, `baseline_commit` | E-001, E-002 | pass |
| REQ-006 | `challenge/README.md`, `render` | E-003 | pass |
| Real-agent play | not run in this change | E-004 | deferred |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability is an internal review aid, not formal verification and validation. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
