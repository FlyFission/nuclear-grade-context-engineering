# Trace

## Trace summary

| Claim ID | Artifact | Status |
|---|---|---|
| C-001 | `nuclear_grade/efficacy.py`; `evals/cases/*.json`; live `ng eval .` | pass |
| C-002 | `tests/test_efficacy.py::test_harness_has_teeth_when_a_signal_is_dropped` | pass |
| C-003 | `nuclear_grade/efficacy.py` imports (json, dataclasses, pathlib); clean-venv wheel install | pass |
| C-004 | `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md` | pass |
| C-005 | `evals/cases/U02-...json`, `U04-...json`, `U07-...json` | pass |
| C-006 | `tests/test_efficacy.py::test_eval_command_is_graceful_without_cases`; wheel run from temp dir | pass |
| C-007 | `docs/03-worked-examples/skill-workflow-comparison/README.md`; `results-summary.md` links | pass |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every claim maps to a named artifact and a status.

## Source-lineage note

Original Nuclear-grade trace influenced by traceability concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
