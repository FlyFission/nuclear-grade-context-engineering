# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim | Result status | Evidence link | Notes |
|---|---|---|---|
| C-001 scores real artifacts | pass | `../../../nuclear_grade/efficacy.py` | `ng eval .` reports 15/15 signals across U02, U04, U07; each case isolates the `## Nuclear-Grade Trial` section. |
| C-002 harness has teeth | pass | `../../../tests/test_efficacy.py` | The teeth test strips the scored section in a temp copy and asserts the case becomes `incomplete` with 0 present signals and a non-ok result. |
| C-003 zero runtime deps | pass | `../../../nuclear_grade/efficacy.py` | Imports only json, dataclasses, pathlib; a clean-venv wheel install then `nuclear-grade eval` ran without extra packages. |
| C-004 bounded doc | pass | `../../../docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md` | States what it measures, what it does not measure, and a non-assurance boundary note. |
| C-005 reviewable JSON cases | pass | `../../../evals/cases` | Three cases; signals authored from each scenario's stated risks with multiple accepted phrasings. |
| C-006 graceful outside repo | pass | `../../../tests/test_efficacy.py` | Run from a temp dir, the installed CLI prints "No eval cases found" and exits 0. |
| C-007 comparison preserved | pass | `../../../docs/03-worked-examples/skill-workflow-comparison/README.md` | Harness linked from README and results-summary; the qualitative scope and boundary note are unchanged. |

## Reproduction commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py eval .
python tools/ng.py validate .nuclear/changes/efficacy-eval-harness
```

## Known gaps and deferrals

- The harness covers three of twelve trials by design (`deferred`): three scenario-grounded cases are more honest than twelve shallow ones; more cases can be added as JSON later.
- The simple-versus-Nuclear-grade comparison stays qualitative (`not applicable` to mechanize): scoring author-written gap prose by substring would inflate the result and is deliberately excluded.
- CI has not run at packet-authoring time; it is the public evidence for the matrix and wheel-smoke jobs.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Every claim has a recorded status.

## Source-lineage note

Original Nuclear-grade verification record influenced by graded-rigor evidence concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
