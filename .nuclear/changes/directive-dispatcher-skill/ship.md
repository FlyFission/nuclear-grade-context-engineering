# Standard Ship

**Purpose:** State the release decision for the directive router skill.

---

## Release identity

- Change slug: directive-dispatcher-skill
- Version / release / baseline: `using-nuclear-grade` directive router (advisory)
- PR / commit / artifact: this branch's PR
- Owner: FlyFission
- Date: 2026-06-08
- Intended release window: with this PR merge

## Scope and exclusions

- Included: the directive rewrite of `skills/using-nuclear-grade/SKILL.md` + a guard test in `tests/test_skill_contracts.py`.
- Excluded: executable hooks, SessionStart/PreToolUse, edits to other skills, eval-prompt/corpus changes.
- Known non-goals: any enforcement behavior, and any claim that the wording provenly lifts behavior.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard justified |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass (lift deferred) | `verification.md` | A3 measures the lift |
| Dependency / supply-chain evidence | not applicable | this packet | no dependency; no executable code |
| AI-assisted work checks | pass | `verification.md` | design traces to the plan |
| Review / approval | planned | the PR | maintainer review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Behavioral lift unmeasured | The directive wording may not measurably raise classification rate | defer | FlyFission | The A3 classification-rate measurement |
| Over-triggering | A broader, directive router may fire on near-trivial work | accept | FlyFission | If adopters report noise, tighten the negative clause / split a lighter tier |

## Rollback / restore plan

- Rollback method: revert the SKILL.md + test edits (single revert).
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: revert restores the prior advisory router.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| A3 measurement result | A measurable classification lift at acceptable overhead | FlyFission | the A3 eval run | If no lift, revisit directiveness or move to the hooks tier |
| Over-triggering reports | The router does not nag on throwaway work | FlyFission | GitHub issues | Tighten the negative clause |

## Handoff

- Operator/customer/support notes: the router now asks for a spoken mode call first; it is advisory.
- Docs/runbook updated: the skill itself; no separate doc.
- Communication needed: note the directive router in release notes when cut.
- Turnover record if activated: not activated.
- Follow-up date: when the A3 measurement is run.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: the directive content is present, guarded, and within the contract/budget; the only unproven part (the behavioral lift) is the A3 measurement, which is a tuning input, not a blocker for shipping advisory guidance.
- Decision question answered by evidence? yes for "the router instructs the classification"; the lift is the named deferred residual.
- Conditions attached: maintainer runs the A3 measurement before going more forceful (hooks).
- Decision posture: conservative enough.
- Abort or rollback trigger: over-triggering complaints, or A3 showing the directive version is worse → revert.
- OPEX or post-release learning trigger: the A3 result updates whether to add hooks.

## Baseline trigger

- Baseline required? yes
- Baseline record: `using-nuclear-grade` becomes the controlled directive router.
- Revalidation trigger: the A3 result, or a change to skill-loading mechanics.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's PR.
- Monitoring/dashboard/log query: the A3 measurement; GitHub issues.
- Rollback/runbook: revert the SKILL.md + test edits.

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on release readiness, human performance improvement, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
