# Standard Plan

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

---

## Change context

- Slug: skill-benchmark-and-amendments
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-07-06
- Current lifecycle phase: Review

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes — stated in `risk.md`'s Mission anchor section.
- Re-checked before Verify? yes — re-confirmed when the plan changed mid-work (see below).
- Charter articles in play: evidence-before-claims, baseline discipline (golden-fixture updates), independent-review discipline (adversarial critique before trusting an amendment).

No non-goal or charter article was crossed; the table below is empty on purpose.

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| — | — | — | — |

## Build sequence

This packet is written after the work completed (Review phase), so the sequence below records what
actually happened, including two real scope changes mid-work, not a plan written in advance.

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Build the with/without-skill headless benchmark harness and run it on all 28 skills, round 1 (easy trigger-case scenarios, n=3) | REQ-005 | none | `skills/*/SKILL.md` (all 28) | `evals/skill-benchmark-pilot/REPORT.md`, `data/all-skills-pilot/`, `data/reviewing-code-quality-pilot/` | 14 wins / 13 ties / 1 loss, raw data checked in | done |
| 2 | External review of `REPORT.md` found real errors (cost arithmetic, overstated stats claim, wrong ceiling-tie count, a markdown-fence rendering bug); fix all of them | — | Task 1 | `REPORT.md` v1 | `REPORT.md` v2, v3 | Each fix verified against raw data before applying, not just reworded | done |
| 3 | Retest the 14 tied/lost skills with harder scenarios (n=5) targeting each skill's own named rationalizations | — | Task 1 | `skills/*/SKILL.md` (14 skills), the round-1 ties | `GATE1_REPORT.md` | 11 of 14 flip to WINS | done |
| 4 | Diagnose why `briefing-an-agent` and `proving-claims` stayed tied even on the hard case; find a real content overlap for `briefing-an-agent` (scope collision with `handing-off-work`) and a test-design gap for `proving-claims` (structural value untested) | — | Task 3 | Full transcripts, not just grader counts | Diagnosis in conversation, formalized in `AMENDMENT_VALIDATION.md` and `GATE2_AND_GATE3_FINDINGS.md` | Root cause confirmed by reading actual response text | done |
| 5 | Amend `briefing-an-agent`: draft → adversarial critique (found a real house-style violation, fixed) → apply → regenerate command card → update golden fixture → regression-validate on the skill's true niche | REQ-001, REQ-002 | Task 4 | `skills/briefing-an-agent/SKILL.md`, `skills/handing-off-work/SKILL.md` (read-only) | Amended `SKILL.md`, `commands/ng-context-pack.md`, updated `tests/fixtures/command_prompts.json` | 5/5 vs 0/5 on a fresh true-niche scenario | done |
| 6 | Close `proving-claims` for free by re-grading existing Gate 1 transcripts on a structural-completeness criterion instead of decision-correctness | — | Task 4 | Existing Gate 1 transcripts (no new generation cost) | `GATE2_AND_GATE3_FINDINGS.md` | 5/5 vs 0/5 | done |
| 7 | Draft a 5-item amendment plan to close the benchmark's own self-audit gaps (statistics, pre-calibration, oracle verification, multi-model, independent replication); have it adversarially critiqued *before* executing any of it | — | Task 6 | `evals/skill-benchmark-pilot/README.md` self-audit table | Draft plan; critique findings | Critique found real, checkable problems in 3 of 5 items | done |
| 8 | Execute what the critique confirmed was actually free or honestly cheap: statistics with Benjamini-Hochberg correction, a free pre-calibration desk audit, a $0.32 4-skill Haiku multi-model check | REQ-005 | Task 7 | Existing graded data (stats, desk audit); new Haiku runs (multi-model) | `STATISTICAL_ANALYSIS.md`, `MULTI_MODEL_CHECK.md`, `PLAN_STATUS.md` | 0/44 tests significant as of this step; 17/27 scenarios would fail pre-calibration; 3/4 multi-model checks replicate, 1 doesn't. (Later corrected to 0/47 during PR review after Codex found 3 closeout rechecks missing from the family -- see `verification.md`'s negative/failure-mode checks table; conclusion unchanged.) | done |
| 9 | Mid-work discovery: PR #63, an independent parallel effort, touched the same three skill files with a different diagnosis-to-fix mapping. Reconcile before spending further. | REQ-004 | Task 8 | PR #63's diff and body | Two PR comments on #63 documenting the overlap and reporting the `creating-change-records` resolution | `creating-change-records` closed for free using PR #63's scope clarification: 4/5 vs 0/5 | done |
| 10 | Attempt to fix `creating-change-records`'s Haiku gap found in Task 8: draft → adversarial critique (found two real wording gaps, fixed) → apply → regenerate command card → update golden fixture → validate on both Sonnet (regression) and Haiku (target) | REQ-001, REQ-002, REQ-003 | Task 9 | `skills/creating-change-records/SKILL.md` | Amended `SKILL.md`, `commands/ng-new.md`, updated golden fixture | Sonnet held 3/3 (no regression); Haiku stayed 0/3 (root cause: model reasons in a general safety-refusal register, bypassing the skill's process entirely) — amendment kept, gap reported open, not fixed | done |
| 11 | Discover `main` had independently merged a third, minimal fix for the same `briefing-an-agent`/`handing-off-work` and `rating-change-risk`/`creating-change-records` overlap; merge and reconcile | REQ-004 | Task 10 | `origin/main` (4 commits ahead of this branch's fork point) | Merge commit; one real conflict resolved (kept this branch's validated wording); `creating-change-records` auto-merged cleanly | Full test suite, ruff, doctor, gen-commands green after merge | done |
| 12 | Write this change-control packet, retroactively, to bring this work under the repo's own Standard-mode process before merge | — | Task 11 | Everything above | This packet | `python tools/ng.py validate .nuclear/changes/skill-benchmark-and-amendments` passes | in progress |

For work handed to another agent or session: not applicable — single continuous session, no handoff.

Determinism posture: all benchmark trials and both skill amendments were model-mediated. Model IDs
are pinned and stated in every report (`claude-sonnet-5` subject/actor, `claude-haiku-4-5` grader
and secondary subject). The scenario/criteria text, harness scripts, and grading prompts are all
checked in and replayable; the model's actual completions are not deterministic and will vary
run-to-run — this is disclosed, not hidden, in every report's limitations section.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Draft scenarios/criteria, run trial batches, read raw transcripts | None — exploratory |
| candidate | Draft skill amendments, run adversarial critique | Critique must find and report real issues, or explicitly find none |
| audit | Regression/validation runs on both Sonnet and (where checked) Haiku | Results read from raw transcripts, not just grader counts, before drawing conclusions |
| accept | Commit, push, update master status tables and self-audit | Full test suite/ruff/doctor/gen-commands green; PR #62 description and this packet reflect the actual current state |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Applying a skill amendment without adversarial review | A well-intentioned edit introduces a house-style violation or an unintended regression | A "fixed" skill is actually degraded | Draft→critique→apply loop used for both amendments; critique caught real issues both times | `AMENDMENT_VALIDATION.md`, `MULTI_MODEL_CHECK.md` addendum |
| Trusting a validation result from the grader's count alone | A grading false-positive (e.g. matching "pass"/"gap" as ordinary English, not the intended status-label convention) reads as a real finding | A false conclusion ships as fact | Every divergent or surprising result in this work was checked against the actual transcript text before being reported | `GATE2_AND_GATE3_FINDINGS.md` (the discarded flawed recheck), `MULTI_MODEL_CHECK.md` (the Haiku transcripts read in full) |
| Merging without checking for cross-branch conflicts on the same files | Two unreconciled edits to the same skill land separately, corrupting the skill or silently dropping one side's diagnosis | Lost work, an inconsistent skill file | Explicit `git merge` against current `main` before this packet was written; PR #63 flagged via comment rather than resolved unilaterally | This packet's `trace.md`; PR #63 comment thread |

## Agent briefing

- Role: builder + reviewer + verifier, single agent across the whole change (session-continuous, no handoff)
- Authority source: user's direct instructions across this conversation, escalating from "test the skills" to "amend what testing found and reconcile with other in-flight work"
- Active procedure/template: this repo's own Standard change-record template, applied retroactively at Review phase
- Last completed action if resumed: n/a — not resumed, single session
- Handoff or turnover needed? no
- Pause when unsure condition: pause and ask before taking any action on a branch or PR this session doesn't own (applied: PR #63 was flagged via comment, not force-resolved)

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `skills/briefing-an-agent/SKILL.md` | Content amendment (scope narrowed) | REQ-001, REQ-002, REQ-004 | Changes future agent behavior when this skill loads | FlyFission |
| `skills/creating-change-records/SKILL.md` | Content amendment (explicit file-naming instruction) | REQ-001, REQ-002, REQ-003 | Changes future agent behavior when this skill loads | FlyFission |
| `commands/ng-context-pack.md`, `commands/ng-new.md` | Regenerated | REQ-002 | Must stay a deterministic projection of the skills above | FlyFission |
| `tests/fixtures/command_prompts.json` | Deliberately updated twice | REQ-002 | Golden snapshot; guards against silent prompt drift | FlyFission |
| `evals/skill-benchmark-pilot/` | New directory, ~40k lines of evidence/tooling | REQ-005 | The benchmark itself | FlyFission |
| `.nuclear/changes/skill-benchmark-and-amendments/` | This packet | all | Brings the change under the repo's own process | FlyFission |

## Non-goals

- This packet does not retroactively create packets for the benchmark's earlier commits — it
  documents the whole body of work as of Review phase, which is itself named as a process gap in
  `verification.md`.
- This packet does not resolve the PR #63 `briefing-an-agent` conflict — that is a maintainer
  decision, flagged but not forced.
- This packet does not attempt oracle-based verification or full 28-skill multi-model coverage —
  both were re-scoped and explicitly deferred in `PLAN_STATUS.md` after an adversarial critique
  found the original cost estimates wrong.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Grading model | `claude-haiku-4-5`, kept separate from the subject model | Using the same model as both actor and grader | Avoids the self-check pattern `proving-claims` itself flags as a red flag | If Haiku grading shows systematic bias in a future audit |
| Multi-model check scope | 4 of 28 skills, Haiku only (not Opus) | Original plan: 8 skills × Haiku + Opus | Adversarial critique found the original cost estimate wrong by 1.5-3x (Opus pricing); re-scoped down rather than spending blind | If budget is explicitly allocated for a larger multi-model pass |
| Statistical test | Fisher's exact test implemented from scratch (`math.comb`) | scipy.stats.fisher_exact | No scipy in this environment; implementation verified against the known 3-vs-0-of-3 reference value before trusting it | N/A |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001 through REQ-005 each state one trigger→response, derived from actual protected/unacceptable outcomes | pass |
| Design approved | `basis.md` design outline complete for this change's stakes | pass |
| Tasks approved | Every build step above ties to a requirement or is named as scaffolding/retrospective documentation | pass |
| Specification reviewed | Protected outcomes, outcomes to prevent, and assumptions stated plainly in `basis.md` | pass |
| Tests/evals defined | Every claim maps to evidence in `verification.md` | pass |
| Build complete | Affected files match this plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risks and rollback recorded in `ship.md` | pass |
| Turnover complete if activated | n/a, no handoff | n/a |

## Rollback approach

- Rollback method: `git revert` the amendment commits on `skills/briefing-an-agent/SKILL.md` and
  `skills/creating-change-records/SKILL.md` (and their generated command cards + fixture updates);
  the benchmark evidence directory (`evals/skill-benchmark-pilot/`) is additive and needs no rollback
  of its own.
- State/data reversal notes: none — no runtime state, no data migration.
- Feature flag / kill switch: not applicable; skill files are static instructions, not a running service.
- Owner: FlyFission.
- Time to restore estimate: minutes (a `git revert` plus `python tools/ng.py gen-commands` to
  regenerate the affected command cards).

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py gen-commands . --check
python tools/ng.py validate .nuclear/changes/skill-benchmark-and-amendments
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: PR #62 (this branch), PR #63 (reconciled), this session's conversation

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
