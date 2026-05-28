# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim | Result status | Evidence link | Notes |
|---|---|---|---|
| C-001 README + QUICKSTART demo framing | pass | `../../../README.md`, `../../../QUICKSTART.md` | "Try it in 60 seconds" now names the expected `FAILED`; QUICKSTART has the `> **Note on the demo**` callout. |
| C-002 wheel install end-to-end | pass | `../../../.github/workflows/ci.yml` `wheel-smoke` job; `../../../tests/test_packaging.py` | Locally built `nuclear_grade-0.2.0-py3-none-any.whl`; installed into a clean venv; `nuclear-grade init / new --mode {quick,standard,cm,golden-path} / list / validate` all run outside the source tree. |
| C-003 paraphrase battery | pass | `../../../tests/test_ng_validate.py` `test_paraphrased_compliance_claims_all_fail`, `test_boundary_paraphrases_all_pass` | Seven paraphrases fail; five boundary phrases pass. Existing guardrail tests at `tests/test_ng_validate.py:122-151` still pass. |
| C-004 mode declaration required + migrate | pass | `../../../nuclear_grade/ng_validate.py` `_declared_mode`; `../../../nuclear_grade/cli.py` `handle_migrate`; `../../../tests/test_ng_cli.py` `test_migrate_*` | Three migrate tests pass; missing-mode test passes; all seven existing repo packets and the worked-example packet still validate (each declares mode). |
| C-005 cm + golden-path scaffolds | pass | `../../../tests/test_ng_cli.py` `test_new_cm_packet_scaffolds_all_cm_files`, `test_new_golden_path_packet_scaffolds_all_files` | Both scaffold all five files. |
| C-006 CI matrix + ruff | pass | `../../../.github/workflows/ci.yml` | Matrix is `["3.11", "3.12"]`. `ruff check .` step added before tests pass. `pyproject.toml` `[tool.ruff.lint]` selects E, F, I, B, UP. CI run on push will confirm green. |
| C-007 long-label empty-prompt | pass | `../../../tests/test_ng_validate.py` `test_long_label_empty_prompt_is_detected` | 200-char label registers as unfilled. |
| C-008 "validated" tightened | pass | `../../../README.md` line 19 and line 151; `../../../docs/03-worked-examples/skill-workflow-comparison/results-summary.md` banner | README now says "one tested worked example and one author-judged comparison study." Banner adds methodology disclaimer above the score table. |
| C-009 CHANGELOG stamped | pass | `../../../CHANGELOG.md` | Single Unreleased section, then a stamped `[0.2.0] - 2026-05-27` section with Breaking / Added / Fixed / Changed. |
| C-010 CITATION + CODEOWNERS | pass | `../../../CITATION.cff`; `../../../.github/CODEOWNERS` | Both files exist; both carry MAINTAINER placeholders to be filled by the human maintainer. |
| C-011 SWOT proposed framing | pass | `../../../docs/04-adoption/report-swot-gap-remediation.md` | Italic banner above Phase 1 declares Phase 1 through Phase 4 lists as proposed deliverables, not refs to existing files. |
| C-012 hatchling + force-include + 0.2.0 | pass | `../../../pyproject.toml`; locally built wheel | Wheel contains `nuclear_grade/_bundled/templates/{quick,standard,cm,golden-path}/*`, `nuclear_grade/_bundled/skills/*/SKILL.md`, and `nuclear_grade/_bundled/commands/*.md`. |

## Reproduction commands

```bash
python -m pytest -q
python tools/ng.py doctor .
for packet in .nuclear/changes/*; do python tools/ng.py validate "$packet"; done
find docs/03-worked-examples -path '*/.nuclear/changes/*' -type d -prune -print \
  | while read p; do python tools/ng.py validate "$p"; done

python -m build --wheel --outdir /tmp/wheel-test
python -m venv /tmp/smoke-venv
/tmp/smoke-venv/bin/pip install /tmp/wheel-test/nuclear_grade-0.2.0-py3-none-any.whl
cd /tmp && mkdir smoke-work && cd smoke-work
/tmp/smoke-venv/bin/nuclear-grade init .
/tmp/smoke-venv/bin/nuclear-grade new my-quick --mode quick
/tmp/smoke-venv/bin/nuclear-grade new my-cm --mode cm
/tmp/smoke-venv/bin/nuclear-grade new my-gp --mode golden-path
/tmp/smoke-venv/bin/nuclear-grade list
```

## Known gaps and deferrals

- CI itself has not run yet at the time of packet authorship. It will run on push and is the primary public evidence for C-006 and C-002.
- The `CITATION.cff` and `.github/CODEOWNERS` carry `MAINTAINER:` placeholders. The maintainer must replace these before tagging a release. Recorded as a `gap` not blocking 0.2.0 merge.
- The `nuclear-grade migrate` command does not rewrite multi-mode legacy packets that mix Quick and Standard files. Recorded as `deferred`; behavior is "infer Standard if any Standard-only file is present."

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Every claim has a recorded status of `pass`, `gap`, `deferred`, or `not applicable`.
- Reproduction commands above are runnable.

## Source-lineage note

Original Nuclear-grade verification record inspired by graded-rigor evidence and lifecycle concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
