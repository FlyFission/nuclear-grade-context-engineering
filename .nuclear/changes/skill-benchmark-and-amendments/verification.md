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
| "27 of 27 tested skills show some measured effect on Sonnet" (round 1 + Gate 1 + closeouts) | Actor (this session) authored scenarios, criteria, ran trials, and graded | Yes — every raw prompt/response/script is checked into `evals/skill-benchmark-pilot/data/`; `scripts/run_pilot_all.py` reruns it | 2 (self-authored, but mechanically reproducible by a third party who reruns the scripts) | Not independently authored; disclosed prominently in `REPORT.md`'s executive summary and `README.md`'s self-audit, treated as a standing limitation, not resolved by this packet |
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
