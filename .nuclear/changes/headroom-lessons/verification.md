# Verification: lessons from Headroom

## Authorship disclosure

An AI agent (Claude Code) wrote this change and this record under the owner's instruction, and ran every check below in one session. A separate agent instance reviewed the first version of the diff; it was briefed with the files to check, not with conclusions. No human has reviewed it yet.

## Result

| Evidence ID | Claim | Method | Result status |
|---|---|---|---|
| E-001 | REQ-001 | `test_a_new_tool_version_is_a_new_row`. Fails when grouping drops the tool version (mutation 1) | pass |
| E-002 | REQ-002 | `test_each_run_records_which_pinned_inputs_were_uncommitted` covers: a temporary git repo, a commit to other files, skipped cache folders, an ignored `.env`, a renamed file with a space, and an edited validator. `test_runs_are_scored_by_the_repository_scorer` checks schema version 2 and the field shapes in real runs. The first test fails under mutations 3, 4 and 5 | pass |
| E-003 | REQ-003 | `test_runs_that_do_not_share_inputs_are_marked_not_comparable` and `test_the_agent_configuration_a_run_used_is_part_of_its_identity` cover each reason, unscored runs and a different HEAD with no flag, old schema-1 runs, the rendered note, and unchanged counts. Fails under mutations 1, 2, 6 and 7 | pass |
| E-004 | REQ-005 | `test_llms_txt_links_resolve_and_stay_clean` | pass |
| E-005 | REQ-004, REQ-006 | Read against the code and against `tests/test_public_docs.py`; the independent review's wording findings are dispositioned below | pass |
| E-006 | No regressions | `evidence/pre-pr-checks.txt`: full pytest, ruff, doctor, tokens, the worked-example validation, release identity and `git diff --check` | pass |

After `main` gained the scoreboard (#153), the branch was merged with it. Three conflicts (the `build.py` docstring, `METHOD.md` change entries and new tests) were resolved by keeping both sides. `run-all.py`, which now launches `run.py`, was added to the pinned inputs. The scoreboard already reads `tool_version` and `identity_problems`, and its tests pass with this change. Full suite after the merge: `1168 passed, 1 skipped` (`evidence/pre-pr-checks.txt`).

Mutation runs are in `evidence/mutation-check.txt`. Each guard was disabled on its own, the test file was run, and the files were restored before the next mutation.

### Independent review: findings and dispositions

| # | Finding (severity) | Disposition |
|---|---|---|
| 1 | The scorer also depends on `nuclear_grade/` (it loads `ng_validate.py` through `NG_REPO`), and that was not pinned (must-fix) | `nuclear_grade` added to `PINNED_INPUTS`; mutation 4 |
| 2 | Ignored files under `challenge/` (for example `.claude/settings.local.json`, `.env`) are copied into the agent's folder but were not reported (must-fix) | Status now uses `--ignored=matching`; only the folders the copy skips are left out; mutation 3 |
| 3 | Quoted and renamed paths were stored mangled (nit) | NUL-separated status, taking the new path of a rename |
| 4 | The commit was read after a run that can take 30 minutes (should-fix) | `HEAD`, the inputs commit and the status are all read before the copy |
| 5 | Comparing whole-repo HEAD would flag rows after any unrelated commit, and "unknown" counted as a commit (should-fix) | Rows compare `inputs_commit`; "unknown" is reported on its own |
| 6 | A scored run with no scorer digest was treated as matching (should-fix) | Flagged as "scored run(s) with no scorer digest"; mutation 6 |
| 7 | No test checked that runs write the new field (should-fix) | End-to-end test checks schema version 2 and the field shapes; ignored-file and rename cases added |
| 8 | The mutation check disabled all guards at once (nit) | Rerun with one guard at a time |
| 9 | `METHOD.md` had no dated entry, and How many runs omitted tool version (should-fix) | Both added |
| 10 | `build.py` docstring contradicted itself on grouping (nit) | Fixed |
| 11 | `llms.txt` said the CLI reference lists every subcommand; it lists 11 of 17 (should-fix) | Now "the main `ng` subcommands; `python tools/ng.py --help` lists all" |
| 12 | `llms.txt` AGENTS.md and skill-catalog wording was inexact (nit) | Fixed |
| 13 | ROADMAP said Headroom "hit and fixed" the problem, which the packet did not show; "loads on every turn (… a skill)" contradicts load-by-trigger (should-fix) | "guards against this"; skills dropped from that sentence |
| 14 | ROADMAP OPEX item named a source with no link (nit) | Pinned link to `headroom/learn/loops.py` added |
| 15 | The Quick risk record was wrong on two counts: (a) the not-comparable rule is new, not already in the method; (b) a rebuild cannot recover unrecorded inputs. It also needed a CM record or a reason (should-fix) | Mode raised to Standard to match earlier harness packets; (a) and (b) are corrected in [`risk.md`](risk.md); the CM reason is stated there |
| — | Badge stale | Regenerated with this packet |

### Review bots on the pull request (2026-11-20)

| Finding | Disposition |
|---|---|
| Codex and Copilot: a custom `--agents-file` can change the command and permission flags under one label while the pinned inputs stay clean | Fixed. Each run records `agent_config_sha256`, a digest of the agent entry it used; a row with more than one is not comparable; mutation 7 |
| Copilot: `build.py` should be a pinned input, since its outcome logic sets the published counts | Not adopted. `build.py` rebuilds every row from the kept run files in one pass, so all runs in a table are always aggregated by the same code; a per-run record of it would never differ within a table. A change to it is reviewed as a code change and logged in `METHOD.md` |

## Evidence custody and coupling

| Evidence ID | Claim ID | Decisive? | Artifact / raw result | Change actor | Generated by | Selected by | Transformed / summarized by | Executed / captured by | Retained by | Presented by | Verified / witnessed by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-002 | REQ-002 | yes | pytest output; `evidence/mutation-check.txt` | AI agent | pytest | AI agent | AI agent | AI agent | this record | AI agent | not yet witnessed; CI reruns the tests |
| E-003 | REQ-003 | yes | pytest output; `evidence/mutation-check.txt` | AI agent | pytest | AI agent | AI agent | AI agent | this record | AI agent | not yet witnessed; CI reruns the tests |

| Evidence ID | Actor | Context | Mechanism | Authority | Resource | Classification | Admissibility / residual-risk disposition |
|---|---|---|---|---|---|---|---|
| E-002 | partially separated; a second agent instance found the gaps, the authoring agent wrote the tests | coupled; same session | partially separated; CI reruns on a clean runner | coupled; no human has reviewed yet, and the maintainer controls merge | coupled; local runner | self-check | admitted for review only; residual coupling carried to [`ship.md`](ship.md) |
| E-003 | partially separated; a second agent instance found the gaps, the authoring agent wrote the tests | coupled; same session | partially separated; CI reruns on a clean runner | coupled; no human has reviewed yet, and the maintainer controls merge | coupled; local runner | self-check | admitted for review only; residual coupling carried to [`ship.md`](ship.md) |

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Record the actual outcomes and disclose that AI agents produced and checked the work.

## Source-lineage note

Custody terms follow [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). This self-check is not independent evidence.
