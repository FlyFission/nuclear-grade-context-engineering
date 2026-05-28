# Trace

## Trace summary

| Claim ID | Finding | Evidence artifact | Status |
|---|---|---|---|
| C-001 | F1 README + QUICKSTART framing | `README.md` 60-second-demo paragraph; `QUICKSTART.md` Note callout | pass |
| C-002 | F2 wheel install path | `.github/workflows/ci.yml` `wheel-smoke` job; `tests/test_packaging.py`; `nuclear_grade/cli.py` `_resolve_resource_root` and `template_root_for` | pass |
| C-003 | F3 paraphrase detection | `nuclear_grade/ng_validate.py` `PARAPHRASE_PATTERNS`, `_check_prohibited_claims`, `_has_paragraph_disclaimer`; `tests/test_ng_validate.py` `test_paraphrased_compliance_claims_all_fail`, `test_boundary_paraphrases_all_pass` | pass |
| C-004 | F4 mode declaration required | `nuclear_grade/ng_validate.py` `MODE_DECLARATION_PATTERN`, `_declared_mode`; `nuclear_grade/cli.py` `handle_migrate`; `tests/test_ng_validate.py` `test_packet_without_mode_declaration_fails`; `tests/test_ng_cli.py` `test_migrate_*` | pass |
| C-005 | F5 CM + golden-path scaffolds | `nuclear_grade/cli.py` `MODE_FILES`, expanded `--mode` choices; `tests/test_ng_cli.py` `test_new_cm_packet_scaffolds_all_cm_files`, `test_new_golden_path_packet_scaffolds_all_files` | pass |
| C-006 | F6 CI matrix + ruff | `.github/workflows/ci.yml` matrix `["3.11", "3.12"]`, `python -m ruff check .` step; `pyproject.toml` `[tool.ruff]` | pass |
| C-007 | F7 long-label empty-prompt | `nuclear_grade/ng_validate.py` `EMPTY_PROMPT_PATTERN` (cap removed); `tests/test_ng_validate.py` `test_long_label_empty_prompt_is_detected` | pass |
| C-008 | F8 "validated" tightened | `README.md` line referencing tested worked example + author-judged comparison; `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` methodology banner | pass |
| C-009 | F9 CHANGELOG | `CHANGELOG.md` single Unreleased + stamped `[0.2.0] - 2026-05-27` | pass |
| C-010 | F10 CITATION + CODEOWNERS | `CITATION.cff`; `.github/CODEOWNERS` | pass |
| C-011 | F11 SWOT proposed framing | `docs/04-adoption/report-swot-gap-remediation.md` proposed-deliverables banner | pass |
| C-012 | F12 hatchling + force-include + version | `pyproject.toml` `build-system`, `[tool.hatch.build.targets.wheel.force-include]`, `version = "0.2.0"`; local wheel build at `/tmp/wheel-test/nuclear_grade-0.2.0-py3-none-any.whl` confirmed to contain `nuclear_grade/_bundled/{templates,skills,commands}/*` | pass |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every claim above has a named artifact and a recorded status.

## Source-lineage note

Original Nuclear-grade trace inspired by configuration-management and lifecycle-traceability concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
