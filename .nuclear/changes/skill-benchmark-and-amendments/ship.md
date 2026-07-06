# Standard Ship

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

---

## Release identity

- Change slug: skill-benchmark-and-amendments
- Version / release / baseline: n/a (no versioned release; a repo PR merge)
- PR / commit / artifact: PR #62, branch `claude/skills-program-bench-testing-h19nv5`, HEAD at merge time
- Owner: FlyFission
- Date: 2026-07-06
- Intended release window: at reviewer's convenience; no time-sensitive dependency

## Scope and exclusions

- Included: the full with/without-skill benchmark (round 1 + Gate 1, all 28 skills), the
  `briefing-an-agent` amendment (validated, working), the `creating-change-records` amendment
  attempt (validated, partially working — see Residual risks below), the statistical analysis, the
  small multi-model check, and the merge reconciliation against `main`.
- Excluded: oracle-based verification, full 28-skill multi-model coverage, third-party independent
  replication — all explicitly deferred in `PLAN_STATUS.md`, not silently dropped.
- Known non-goals: this does not certify any skill as correct, safe, or production-ready; it does
  not consolidate, delete, or rewrite any skill beyond the two amendments named above.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified: two skill files that shape future agent behavior were amended |
| Basis / requirements / claims | pass | `basis.md` | REQ-001 through REQ-005 all traced to evidence |
| Questioning attitude | pass | folded into `risk.md` | No separate file; drift/re-anchor checks applied inline |
| Verification | pass, with named gaps | `verification.md` | Full test suite green; two negative/failure-mode checks (grader false-positive, cost estimate errors) found and fixed real problems before they shipped |
| Dependency / supply-chain evidence | not applicable | — | No new dependency introduced |
| AI-assisted work checks | pass | `verification.md` | Adversarial review performed on both amendments and on the remediation plan itself |
| Review / approval | pending | this PR | Independent human review has not yet occurred — see Release decision below |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| `briefing-an-agent` has an unreconciled conflict with PR #63's independent (unvalidated) version | If PR #63 merges after this PR without further reconciliation, the two diagnoses could get relitigated or one could silently lose | defer | FlyFission | Either PR merges, or the other's author responds to the flagged comments |
| `creating-change-records` does not reliably work on `claude-haiku-4-5` even after an amendment attempt | The skill's demonstrated value is Sonnet-specific for at least this scenario; downstream users on weaker models may not get the benefit | accept, named openly | FlyFission | A future amendment attempt, or evidence from real usage that this doesn't matter in practice |
| The benchmark's headline "27/28 skills show effect" claim does not survive formal multiple-comparisons-corrected significance testing | A reader who doesn't get to `STATISTICAL_ANALYSIS.md` could overtrust the headline | mitigate | FlyFission | Already mitigated: `README.md`'s status table and executive-summary-level framing point to the statistical caveat directly, not buried |
| No third-party has reviewed or re-run any part of this benchmark | Every scenario, criterion, grading pass, and amendment decision was made by the same overall effort | accept, stated as a standing limitation | FlyFission | An outside reviewer engages with the work |
| Oracle-based verification and full multi-model coverage remain unbuilt | The benchmark is weaker evidence than it would be with either | defer | FlyFission | Budget/scope explicitly allocated |
| This packet was authored retroactively, at Review phase | The repo's own process expects a packet scaffolded before or during build | accept, named here rather than hidden | FlyFission | Future work of comparable scale should scaffold a packet at Plan phase |

## Rollback / restore plan

- Rollback method: `git revert` the amendment commits; the benchmark evidence directory is additive
  and does not need rollback.
- Data migration reversal or restore notes: none — no data, no migration.
- Feature flag / kill switch: not applicable — static skill-instruction files, not a running service.
- Owner on call: FlyFission.
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| `test_command_parity.py` / `gen-commands --check` | Stays green after any future skill edit | FlyFission | CI / local pytest | Regenerate command cards, update golden fixture deliberately |
| Real-world usage reports of `briefing-an-agent` or `creating-change-records` behaving unexpectedly | None reported that contradict the validated findings | FlyFission | Issue tracker, PR comments | Re-open the amendment with a fresh diagnosis, following the same draft→critique→validate discipline |
| PR #63 activity | Any update, comment reply, or merge | FlyFission | GitHub PR #63 | Re-reconcile `briefing-an-agent` per whichever version is chosen |

## Handoff

- Operator/customer/support notes: none — this is a documentation/skill-content change, not an
  operational system.
- Docs/runbook updated: `evals/skill-benchmark-pilot/README.md` and its linked reports are the
  living record; no separate runbook needed.
- Communication needed: PR #62's description should be updated to reflect the full scope of work
  (see Required links); the two PR #63 comments already communicate the cross-branch overlap.
- Turnover record if activated: not activated — no handoff occurred.
- Follow-up date: none fixed; follow-up is trigger-based (see Monitoring table).

## Release decision

- Decision: **ship with residual risk**
- Decision maker: recommended by the actor (this session); **final decision should rest with an
  independent human reviewer via PR review**, consistent with this repo's own
  `actor-evidence-independence` discipline — the actor that did the work is not positioned to be the
  sole decider on trust-bearing content like a skill amendment.
- Rationale: the benchmark methodology and both amendments were adversarially reviewed and
  regression-validated; every negative/failure-mode check performed found and fixed a real problem
  before it shipped; the residual risks above are named, bounded, and owned rather than hidden. None
  of them block merge on their own — they're exactly the kind of "gap, not blocker" this repo's own
  `proving-claims` skill says should be recorded, not hidden.
- Decision question answered by evidence? yes — see `verification.md`'s claim-to-evidence table.
- Decider independent of the actor that produced the change? no, not yet — flagged above as the
  reason this is a recommendation, not a final verdict.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes —
  every claim links to raw, rerunnable data in `evals/skill-benchmark-pilot/data/` or a deterministic
  script.
- Conditions attached: PR #62's description should be updated to reflect the true current scope
  (see Required links) before a reviewer is asked to approve it; the PR #63 conflict should be
  actively communicated to whoever reviews, not left for them to discover.
- Decision posture: conservative enough — no skill was deleted or radically rewritten on this
  evidence alone; both amendments were narrow and validated; the one amendment that didn't fully
  work is reported as such.
- Abort or rollback trigger: a future report that either amendment measurably regressed real usage.
- OPEX or post-release learning trigger: if `creating-change-records`'s Haiku gap turns out to
  matter in practice, that's a concrete lesson for skill-authoring on this repo generally (skills may
  need model-capability-tiered instructions, not one-size-fits-all wording) — worth its own OPEX note
  if it recurs on another skill.

## Apply clearance

This change's "apply" is a GitHub PR merge, not a production deploy — there is no separate
operational window, external state, or deployment policy to check.

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | Independent human PR review has not yet occurred |
| Release / maintenance (freeze) window open | not applicable | No freeze window concept for this repo's PR process |
| External state unchanged since verification — verdict not stale | yes | Verified against current `origin/main` via the merge performed in this packet |
| Deployment policy satisfied | not applicable | No deployment; a docs/skill-content PR merge |
| Rollback / kill-switch confirmed ready at apply-time | yes | `git revert` path confirmed above |

- Clearance decision: **hold** — pending independent human PR approval (see Release decision above).
- Cleared by: not yet — awaiting a human reviewer independent of the actor.
- Apply window / valid until: no fixed expiry; re-verify against `main` again if significant time
  passes before merge, since this branch has already needed one non-trivial reconciliation against
  `main`'s independent progress.
- Re-clearance trigger: if `main` advances again with further changes to the same skill files before
  this merges, re-run the merge-conflict check in this packet's `trace.md` before treating clearance
  as still valid.

## Baseline trigger

- Baseline required? no — this repo's `recording-a-known-good-version` skill is for accepted
  versions of specific artifacts; the benchmark and amendments here don't introduce a new baselined
  artifact class, they extend the existing skill corpus already under git-based version control.
- Baseline record: n/a
- Revalidation trigger: if either amended skill is edited again, or if a future benchmark run
  contradicts a result in `evals/skill-benchmark-pilot/README.md`'s status table.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: PR #62 (update its description to reflect this packet before
  requesting review); PR #63 (referenced, unresolved conflict)
- Monitoring/dashboard/log query: n/a — see Monitoring table above
- Rollback/runbook: `git revert`, described above

## Exit criteria

- The release decision is stated plainly.
- The apply-clearance call is stated — cleared to apply / hold / lapsed — or marked `not applicable` when the change makes no real-world action.
- Clearance was checked against operational context (approvals, window, external state, deployment policy) at apply-time, not inherited stale from the verdict.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
