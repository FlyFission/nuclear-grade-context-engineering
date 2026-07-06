# Standard Verification

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

---

## Verification context

- Slug: skill-benchmark-and-amendments
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-07-06
- Verification scope: the benchmark's own methodology, both skill amendments, and the cross-branch reconciliation

## Evidence status legend

`pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 (adversarial review before applying) | local proof | independent verification | Separate subagent, given the diff and told to find problems, not validate | Critique finds and reports real, checkable issues or explicitly finds none | pass | `AMENDMENT_VALIDATION.md` (found redundant justification, non-house-style phrase); `MULTI_MODEL_CHECK.md` addendum (found missing deixis, bundled file-list ambiguity) | none |
| REQ-002 (artifact sync) | deterministic test | deterministic test | `python tools/ng.py gen-commands . --check` | Exits 0, no drift between skills and generated cards | pass | Verified after every amendment and after the `main` merge | none |
| REQ-003 (honest disconfirmation) | local proof | peer review | Read the master status table wording directly | `creating-change-records` is not labeled WINS without qualification | pass | `evals/skill-benchmark-pilot/README.md` current table | none |
| REQ-004 (cross-branch reconciliation) | local proof | independent verification | `git merge origin/main`, inspect and resolve conflicts, post PR comments | Merge completes cleanly; conflicts resolved with stated reasoning; PR #63 overlap is commented on, not silently ignored | pass (merge); gap (PR #63's own resolution is a maintainer decision, not closed) | Merge commit `eb3b016`; PR #63 comments | `briefing-an-agent` version choice between this branch and PR #63 |
| REQ-005 (disclosed statistics) | local proof | deterministic test | `python compute_stats.py`, Fisher-exact implementation checked against the known 3-vs-0-of-3 reference (p≈0.10) before trusting it on real data | Correct known-value match; result reported regardless of favorability | pass | `evals/skill-benchmark-pilot/scripts/compute_stats.py`, `data/statistical-analysis/statistical_summary.json`, stated in `STATISTICAL_ANALYSIS.md` | none |

## Verification type guide

(unchanged from template — see `checking-release-readiness`'s type guide for definitions.)

## Evidence independence

| Load-bearing claim | Who authored the evidence (actor / independent verifier / human) | Reproducible by an independent party? (command or artifact) | Independence rung (1-5) | Gap / residual risk if below the stakes |
|---|---|---|---|---|
| "28 of 28 tested skills show some measured effect on Sonnet" (round 1 + Gate 1 + closeouts + the separate reviewing-code-quality pilot) | Actor (this session) authored scenarios, criteria, ran trials, and graded | Yes — every raw prompt/response/script is checked into `evals/skill-benchmark-pilot/data/`; `scripts/run_pilot_all.py` reruns the 27-skill batch, `scripts/run_gate1.py` reruns the hard-case retest, and `scripts/run_pilot.py` separately reruns the 28th skill (`reviewing-code-quality`), which uses its own 3-task design rather than the shared scenario format | 2 (self-authored, but mechanically reproducible by a third party who reruns the scripts) | Not independently authored; disclosed prominently in `REPORT.md`'s executive summary and `README.md`'s self-audit, treated as a standing limitation, not resolved by this packet |
| "The briefing-an-agent amendment doesn't regress the skill's real niche" | Actor authored the fix; a separate subagent critiqued it; the actor ran and read the regression validation | Yes — `data/briefing-an-agent-amendment-validation/` has every raw response | 2 (adversarial critique adds a rung above pure self-check, but the critic is still the same overall effort) | Same non-independence limitation as above |
| "0 of 44 statistical tests survive correction" | Actor computed it | Yes — `compute_stats.py` is deterministic and checked in; anyone can rerun it against the same JSON data | 4 (deterministic computation over already-public raw data — a third party doesn't need to trust the actor's arithmetic, only run the script) | None material — this is math over disclosed data, not a judgment call |
| "PR #63 independently reached the same `briefing-an-agent` diagnosis" | Independent — a different effort (PR #63's author/agent), not this session | Yes — PR #63's diff and body are public on GitHub | 4 (genuinely independent authorship, verified by reading the actual PR diff rather than taking a claim at face value) | This is the one genuinely independent cross-check in the whole packet; noted as such rather than overclaimed as "third-party replication" of the full benchmark |

- Decider independent of the actor for the ship decision? no — this packet is authored by the same
  actor that did the work; the ship decision rests on a human PR reviewer at merge time, per this
  repo's own release-readiness discipline (`checking-release-readiness`).
- Evidence authored only by the actor is labeled a self-check and carried as residual risk in
  `ship.md`? yes.

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Unit/integration | `python -m pytest -q` | Repo root, Python 3.11 | 190 passed, 1 skipped (post-merge) | terminal output, this session |
| Lint | `python -m ruff check .` | Repo root | All checks passed | terminal output, this session |
| Structural doctor | `python tools/ng.py doctor .` | Repo root | OK: Nuclear-grade doctor | terminal output, this session |
| Command-card parity | `python tools/ng.py gen-commands . --check` | Repo root | OK: every command card matches its skill | terminal output, this session |
| Benchmark round 1 | `scripts/run_pilot_all.py`, `grade_pilot_all.py` | Headless `claude -p`, `--safe-mode` | 162/162 runs completed after a mid-run harness bug was found and fixed | `REPORT.md` section 3 |
| Benchmark Gate 1 | `scripts/run_gate1.py`, `grade_gate1.py` | Same | 140/140 runs completed | `GATE1_REPORT.md` |
| Amendment validation | `scripts/run_validation.py`, `grade_validation.py`; `ccr_amend_run_validation.py`, `ccr_amend_grade_validation.py` | Same, both Sonnet and Haiku as subject | See claim-to-evidence table | `AMENDMENT_VALIDATION.md`, `MULTI_MODEL_CHECK.md` |
| Statistical analysis | `scripts/compute_stats.py` | Local Python, no scipy (verified manual Fisher-exact implementation) | 0/44 significant after BH correction | `STATISTICAL_ANALYSIS.md` |
| Packet validation | `python tools/ng.py validate .nuclear/changes/skill-benchmark-and-amendments` | Repo root | see `ship.md` for the run recorded at ship time | this packet |

## Negative / failure-mode checks

What did this work actually try to break, and what happened?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| A skill amendment looks good on paper but regresses the skill's real use case | Regression validation on a *fresh*, not-the-diagnosis scenario, run after every amendment | `briefing-an-agent`: no regression (5/5 vs 0/5 on true niche). `creating-change-records`: no regression on Sonnet (3/3 held) | `AMENDMENT_VALIDATION.md`, `data/creating-change-records-amendment-validation/` |
| A grader's YES/NO count is actually a false positive (matching incidental words, not the intended signal) | Read the actual transcript text behind every surprising or divergent result, not just the grader's label | Found and discarded one flawed recheck (matching "pass"/"gap" as ordinary English in `creating-change-records`'s Gate 1 structural recheck); confirmed the Haiku multi-model divergence was real by reading both failing transcripts in full | `GATE2_AND_GATE3_FINDINGS.md`; `MULTI_MODEL_CHECK.md` |
| An amendment plan looks rigorous but manufactures false confidence | Adversarially critiqued the plan itself before executing any item | Critique found real problems in 3 of 5 items (wrong cost premise, redundant work, understated coverage gap) — plan was corrected before spending further | `PLAN_STATUS.md` |
| Two unreconciled edits to the same skill file land on `main` without anyone deciding which wins | Explicit `git merge` performed against current `main` rather than assuming a clean fast-forward | Found a real conflict (`dirty` mergeable state), resolved with stated reasoning | This packet's `trace.md`; merge commit `eb3b016` |
| A cost estimate for planned work turns out to be wrong once actually checked against real data | Adversarial critique cross-checked every cost estimate against this project's own already-observed per-run costs | Found item 2's estimate off ~3-4x and item 4's off ~1.5-3x; both corrected before spending | `PLAN_STATUS.md` |
| A rerun script that a report claims is reproducible actually isn't, on a truly independent check | GitHub Copilot code-review bot (`chatgpt-codex-connector`) reviewed the PR after this packet was written and tried the documented rerun path | Found 3 real issues: (1) `run_pilot_all.py`/`grade_pilot_all.py`/`run_gate1.py`/`grade_gate1.py`/`run_validation.py`/`grade_validation.py` looked for task/run files next to the script instead of under the checked-in `data/<pilot>/` directories, and several scripts hardcoded this session's absolute path instead of resolving repo-relative — both would break on a fresh checkout; (2) the top-level `README.md` headline said "27 of 28" while the benchmark `README.md` says "28 of 28, one Sonnet-only"; (3) `GATE2_AND_GATE3_FINDINGS.md` still said no amendment was proposed for `creating-change-records` after one had been attempted and validated. All three fixed; `compute_stats.py` rerun end-to-end afterward and reproduced the checked-in `statistical_summary.json` byte-for-byte | This session's fix commit `6dbd421`; `README.md`; `evals/skill-benchmark-pilot/GATE2_AND_GATE3_FINDINGS.md`; `evals/skill-benchmark-pilot/scripts/*.py` |
| The first reproducibility fix (above) was itself incomplete -- it missed sibling scripts with the identical bug | Codex re-reviewed the fix commit itself rather than trusting it was complete | Found 3 more: `run_pilot.py`/`grade_pilot.py` (the reviewing-code-quality pilot) still resolved `skill_body.txt`/`tasks/`/`answer_keys.json` under `scripts/`, and `skill_body.txt` turned out not to be checked in anywhere -- fixed by extracting the skill body live from `skills/reviewing-code-quality/SKILL.md`, matching every other rerun script's pattern, instead of reading a static file; `run_haiku.py`/`ccr_amend_run_validation.py` had their `TASKS`/`SKILLS_ROOT` paths fixed in the first pass but their `RUNS_DIR` (and `grade_haiku.py`/`ccr_amend_grade_validation.py`'s glob and output paths) were missed, still pointing at `scripts/runs` instead of `data/multi-model-check/runs` and `data/creating-change-records-amendment-validation/runs`; and `data/creating-change-records-structural-recheck/grade_ccr_structure.py`/`grade_corrected.py` still hardcoded this session's absolute path. All fixed and path-existence-checked programmatically (not just read by eye) before committing. Net lesson: an independent review pass on a fix is not redundant -- the same blind spot that produced the original bug can survive one self-corrected pass | This session's second fix commit; `evals/skill-benchmark-pilot/scripts/run_pilot.py`, `grade_pilot.py`, `run_haiku.py`, `grade_haiku.py`, `ccr_amend_run_validation.py`, `ccr_amend_grade_validation.py`; `evals/skill-benchmark-pilot/data/creating-change-records-structural-recheck/*.py` |
| The second reproducibility fix still had 2 more real gaps, plus this fix itself introduced a fresh bug caught before commit | Codex reviewed a third time; separately, path-existence-checking every fix programmatically (not trusting the edit by eye) before committing | Codex found: (1) `run_pilot.py`'s `run_one()` never checked `out_path.exists()` before invoking `claude`, unlike every sibling runner -- a partial rerun would silently overwrite all existing reviewing-code-quality transcripts instead of filling only the gap; (2) six archived `data/*/` copies of the runner/grader scripts (the ones that were actually executed to produce the checked-in evidence, as opposed to their `scripts/` siblings) still hardcoded this session's absolute path -- `data/statistical-analysis/compute_stats.py`, `data/creating-change-records-amendment-validation/run_validation.py`, `data/briefing-an-agent-amendment-validation/run_validation.py`, `data/proving-claims-structural-recheck/grade_structure.py`, `data/multi-model-check/run_haiku.py` and `grade_haiku.py`. While fixing the second issue, an off-by-one in the repo-root path computation (`BASE.parents[4]` instead of `[3]`, since `BASE` was already one level below the file) was caught by the same path-existence check *before* committing, not after -- the check that was supposed to prove the fix worked also caught the fix's own new bug. All paths re-verified against real files after correction; `compute_stats.py`'s archived copy rerun end-to-end and reproduced the checked-in `statistical_summary.json` byte-for-byte a second time | This session's third fix commit; `evals/skill-benchmark-pilot/scripts/run_pilot.py`; `evals/skill-benchmark-pilot/data/statistical-analysis/compute_stats.py`, `data/creating-change-records-amendment-validation/run_validation.py`, `data/briefing-an-agent-amendment-validation/run_validation.py`, `data/proving-claims-structural-recheck/grade_structure.py`, `data/multi-model-check/run_haiku.py`, `grade_haiku.py` |
| A fourth review pass found the rerun path could silently reintroduce a *previously discovered and fixed* harness bug, plus a stale-output trap in the report regenerator | Codex reviewed a fourth time, this time checking rerun scripts against the specific bug narratives `REPORT.md` itself documents, not just path resolution | Found: (1) `run_pilot_all.py` still passed `--tools ""` to the subject-model calls, the exact empty tool grant `REPORT.md` documents as having corrupted 23/162 round-1 runs before being fixed mid-run to `Read,Glob,Grep` -- a rerun or extension through this script would silently reintroduce a bug already found and fixed once; (2) `grade_gate1.py` writes a fresh `summary_gate1.json` on rerun, but `generate_gate1_report.py` only ever read the checked-in `summary_gate1_FINAL.json` snapshot, so a rerun-then-regenerate flow would produce updated raw grading rows but a stale headline comparison table. Fixed (1) by matching Gate 1's already-correct tool grant; fixed (2) by having the report generator prefer a fresh `summary_gate1.json` if present and fall back to the locked `_FINAL` snapshot otherwise -- verified both directions: with no fresh file, the regenerated `GATE1_REPORT.md` is byte-identical to the checked-in one; with a simulated fresh file in place, the fallback correctly steps aside and reads it instead | This session's fourth fix commit; `evals/skill-benchmark-pilot/scripts/run_pilot_all.py`, `generate_gate1_report.py` |
| A fifth review pass found a grading-correctness bug (not just a reproducibility one): grader-infrastructure failures could silently count as real misses, and this packet's own evidence-independence table understated the headline claim's true skill count | Codex reviewed a fifth time, checking grading logic and the packet's own claims for internal consistency, not just rerun mechanics | Found: (1) `grade_review()` in `grade_pilot_all.py`, `grade_gate1.py`, and `grade_pilot.py` catches grader-side failures (timeout, non-JSON output, `claude` CLI unavailable) and returns `meets_criteria: "ERROR"`, but the calling code hardcoded `error: False` on that row regardless -- summary/statistics code then counted it in the denominator as a non-YES, silently treating missing data as a real model miss on any future rerun that hits a transient grader failure; checked the currently checked-in graded data and confirmed zero existing rows are affected (`grep` found no `"meets_criteria": "ERROR"` in any checked-in `graded_results*.json`), so no existing headline number is wrong today, but a future rerun could have quietly corrupted one; (2) this packet's own `verification.md` evidence-independence row still said "27 of 27 tested skills" and cited only `run_pilot_all.py`, while the actual headline (fixed earlier in `README.md`) is 28 of 28 including the separately-run `reviewing-code-quality` pilot. Fixed (1) by having all three graders return `error: True` (with the raw grader error preserved as `grader_error`/`grader_quote`, not silently dropped) instead of folding it into the YES/PARTIAL/NO distribution -- verified with an isolated unit-style test per script that mocks a grader failure and confirms the resulting row is excluded rather than miscounted; fixed (2) by restating the claim as 28 of 28 and citing all three reproducer scripts (`run_pilot_all.py`, `run_gate1.py`, `run_pilot.py`) | This session's fifth fix commit; `evals/skill-benchmark-pilot/scripts/grade_pilot_all.py`, `grade_gate1.py`, `grade_pilot.py`; this file's evidence-independence table |
| The fifth fix's grader-failure handling was itself incomplete on the RCQ pilot's own path, on both sides (catching the failure and consuming its result) | Codex reviewed a sixth time, tracing the RCQ pilot's grader-failure path specifically since it has a different code shape (inline loop, not a shared `grade_one()`) than the two just-fixed graders | Found: (1) in `grade_pilot.py`, the `subprocess.run(...)` call itself sat *outside* the `try` block, so a `TimeoutExpired` or a missing `claude` binary would raise uncaught and crash the whole rerun before it could even reach the `ERROR`-handling code just added; (2) `compute_stats.py`'s RCQ aggregation block (in both the `scripts/` copy and the `data/statistical-analysis/` archived copy) never filtered `not r.get("error")` the way the round-1 and Gate-1 blocks immediately above it already do, so a rerun that produced even one `error: True` RCQ row would crash `compute_stats.py` with a `KeyError` on the missing `meets_criteria` key instead of excluding it and finishing the other 43 tests. Fixed (1) by moving `subprocess.run` inside the `try`, verified with a test that mocks `subprocess.run` to raise `TimeoutExpired` and confirms `grade_review()` now returns the `ERROR` dict instead of propagating the exception; fixed (2) by adding the same `and not r.get("error")` filter to both RCQ blocks, verified with an isolated test of the exact filter expression against a synthetic error row, and by rerunning both `compute_stats.py` copies end-to-end against the real (unmodified) data -- both still reproduce the checked-in `statistical_summary.json` byte-for-byte | This session's sixth fix commit; `evals/skill-benchmark-pilot/scripts/grade_pilot.py`, `compute_stats.py`; `evals/skill-benchmark-pilot/data/statistical-analysis/compute_stats.py` |
| The RCQ error-handling chain still had two more gaps: the producer side (subject-run timeout) didn't tag its own metadata, and a second consumer (the round-1 report generator, not just the stats script) didn't filter it | Codex reviewed a seventh time, tracing the full metadata chain from `run_pilot.py`'s own failure path through to every consumer of `graded_results.json`, not just the ones already touched | Found: (1) `run_pilot.py`'s `TimeoutExpired` branch wrote plain `task`/`condition`/`trial` keys instead of the underscored `_task`/`_condition`/`_trial` keys every consumer (`grade_pilot.py`, `generate_report.py`) actually reads -- a real subject-run timeout during a rerun would produce a row `grade_pilot.py` can't attribute to a task, and whose `None` task value would crash `sorted(set(...))` when mixed with the real task-name strings; (2) `generate_report.py`'s two RCQ blocks (the summary table and the per-trial detail loop) dereferenced `meets_criteria` without filtering `not r.get("error")`, unlike the round-1 block just above them in the same file, which filters once into a shared `rows` variable and reuses it for both its summary and detail sections. Fixed (1) by matching the underscored keys used everywhere else, verified with a test that mocks `subprocess.run` to raise `TimeoutExpired` and confirms the resulting record carries `_task`/`_condition`/`_trial`; fixed (2) by adding the same `and not r.get("error")` filter to both RCQ blocks, verified with an isolated test against a synthetic error row and by rerunning `generate_report.py` end-to-end against the real, unmodified data -- it reproduces the checked-in `REPORT.md` byte-for-byte | This session's seventh fix commit; `evals/skill-benchmark-pilot/scripts/run_pilot.py`, `generate_report.py` |

## AI-assisted work checks

- AI scope: this entire packet's underlying work (benchmark design and execution, both skill
  amendments, the statistical analysis, the cross-branch reconciliation, and this packet itself)
  was performed by an AI agent (Claude, this session) under a human's direct, turn-by-turn
  instructions.
- Model/tool used: `claude-sonnet-5` as the primary actor and benchmark subject model;
  `claude-haiku-4-5` as the grading model and secondary multi-model subject; headless `claude -p`
  CLI invocations as the evaluation mechanism; standard file/git/GitHub tools for the repo work.
- Permissions/actions allowed: normal repo write access on this session's branch
  (`claude/skills-program-bench-testing-h19nv5`); read/comment access to PR #63 (a different branch
  this session does not own — explicitly did not push to it or force-resolve its conflict).
- Independent checks performed: adversarial critique subagents for both skill amendments and for
  the self-audit remediation plan; reading raw transcripts directly rather than trusting grader
  output for every surprising result.
- Self-check / turnover records: no separate `self-check.md` — self-checks are recorded inline in
  `AMENDMENT_VALIDATION.md` and `MULTI_MODEL_CHECK.md` per amendment; no turnover, single session.
- Hallucination/slop screening: statistical claims verified against a known reference value before
  trusting the implementation on real data; every "the skill amendment works" claim was backed by a
  regression run, not asserted from the diff alone; the one amendment that didn't work
  (`creating-change-records` on Haiku) is reported as such rather than smoothed into a success.
- Human approval gates exercised: this packet and the underlying commits are all subject to human
  PR review before merge; no production system or credential was touched.

## Security / dependency / supply-chain checks

Not activated — no new dependency, model, or supplier was introduced by this change.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: this session's terminal output (pytest, ruff,
  doctor, gen-commands); `evals/skill-benchmark-pilot/` reports
- Implementation diff / PR: #62 (this branch), #63 (referenced, not merged into this branch)

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
