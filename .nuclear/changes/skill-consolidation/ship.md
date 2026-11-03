# Skill Consolidation — Ship

## Release identity

- Change slug: skill-consolidation
- Version / release / baseline: `[Unreleased]`; no version bump
- PR / commit / artifact: draft PR from `claude/skill-consolidation`, stacked on #124
- Owner: FlyFission
- Date: 2026-11-03
- Intended release window: after #124 merges and the owner reviews this PR

## Scope and exclusions

- Included: the evaluation (with the M4 merge applied and then reverted); README rewrite; skill catalog, invocation, and full-map figures; diagram-coverage test; evaluation protocol, data, and report.
- Excluded: the six merges that failed; re-testing them.
- Known non-goals: changing any other skill.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard |
| Basis / requirements / claims | pass | `basis.md` | 4 requirements |
| Questioning attitude | pass | `risk.md` | inline |
| Verification | pass | `verification.md` | all decisive rows are self-checks |
| Dependency / supply-chain evidence | not applicable | none | no dependency |
| AI-assisted work checks | pass | `verification.md` | coupling disclosed |
| Evidence custody / coupling profile | pass (disclosed) | `verification.md` | owner is the pending second party |
| Review / approval | gap | this file | human review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Every evaluation agent shares one model family and orchestrator | Correlated blind spots could pass a bad merge or fail a good one | accept for this decision, with the bars fixed in advance; owner review | FlyFission | owner review |
| No merge is made, so the catalog keeps the overlaps the audit found | Routing cost and some trigger overlap remain | accept: the evidence showed each merge lost something | FlyFission | a new, separately pre-registered test |
| No cross-family re-score of the evaluation | Correlated blind spots in every evaluator | defer; it matters less now that nothing merged | FlyFission | any future merge proposal |
| Narrow failures (M2) may be worth a retest | Possible missed simplification | defer to a new pre-registered test if the owner wants it | FlyFission | owner request |

## Rollback / restore plan

- Rollback method: `git revert` the merge, then `python tools/ng.py gen-commands` and `python tools/build_diagrams.py`.
- Data migration reversal or restore notes: not applicable.
- Feature flag / kill switch: not applicable; the revert is the switch.
- Owner on call: FlyFission
- Time to restore estimate: minutes

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on the PR | green | FlyFission | PR checks | fix forward or revert |
| Issues about missing commands or skills | none unexplained | FlyFission | issues | point to the migration note |

## Handoff

- Operator/customer/support notes: the CHANGELOG has the migration line.
- Docs/runbook updated: README, SKILLS, COMMANDS, CORE, diagrams, reference docs.
- Communication needed: the PR description summarizes the evaluation result.
- Turnover record if activated: not applicable.
- Follow-up date: at owner review.

## Release decision

- Decision: defer
- Decision maker: FlyFission (the author recommends ship-with-named-risk)
- Rationale: the bars were fixed before any result. The only merge that cleared them failed the reviewers' final-state evidence and was reverted, so no skill changes. The README and figures pass tests and a rendered read. All decisive evidence is self-check.
- Decision question answered by evidence? yes, by self-check evidence against pre-registered bars
- Verdict owner's authority axis relative to the actor: separated
- Minimum coupling profile for this consequence met? no; gap: human second party
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes; the data files and scorer rerun
- Conditions attached: merge after #124
- Decision posture: conservative enough
- Abort or rollback trigger: a capability of either original found missing in use
- OPEX or post-release learning trigger: any confusion about the merged skill's two phases

## Apply clearance

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | owner review pending |
| Release / maintenance (freeze) window open | not applicable | no release |
| External state unchanged since verification — verdict not stale | yes | stacked on current #124 head |
| Deployment policy satisfied | not applicable | merge is the apply |
| Rollback / kill-switch confirmed ready at apply-time | yes | revert plus regeneration |

- Clearance decision: hold
- Cleared by (operator or policy owner, independent of the actor where trust-bearing): pending, FlyFission
- Apply window / valid until: re-check if #124 or `main` moves
- Re-clearance trigger: either base moves

## Baseline trigger

- Baseline required? no
- Baseline record: not applicable
- Revalidation trigger: the next release that includes this change

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: draft PR from `claude/skill-consolidation`
- Monitoring/dashboard/log query: PR checks
- Rollback/runbook: this file

## Exit criteria

- The release decision and clearance are stated; leftover risks are owned.

## Source-lineage note

Original Nuclear-grade release record mapped against `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
