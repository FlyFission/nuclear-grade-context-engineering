# Standard Ship

**Purpose:** State the release decision for the PROVE subagent pipeline.

---

## Release identity

- Change slug: prove-pipeline
- Version / release / baseline: five PROVE subagent definitions (opt-in, Standard+)
- PR / commit / artifact: this branch's PR
- Owner: FlyFission
- Date: 2026-06-08
- Intended release window: with this PR merge

## Scope and exclusions

- Included: `agents/planner.md`, `runner.md`, `observer.md`, `judge.md`, `educator.md`, `agents/README.md`, `tests/test_agents.py`.
- Excluded: executable hooks, in-session blocking, a live orchestration run.
- Known non-goals: real `permissionMode` confinement from the plugin; always-on fan-out.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard justified |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass (live deferred) | `verification.md` | live orchestration deferred |
| Dependency / supply-chain evidence | not applicable | this packet | no dependency; no executable code |
| AI-assisted work checks | pass | `verification.md` | schema traces to docs |
| Review / approval | planned | the PR | maintainer review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live multi-agent run here | End-to-end orchestration unproven | defer | FlyFission | Maintainer runs the pipeline on a Standard+ change |
| Tool boundaries are advisory (F6) | Not a real perimeter | accept | FlyFission | For confinement, move agents to `.claude/agents/` |
| Orchestrator sees all lanes (A7) | The "independent" judge is not independent of the orchestrator | accept | FlyFission | Back the verdict with rung-4 CI + human review |

## Rollback / restore plan

- Rollback method: delete `agents/` and the test (single revert).
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: the subagents are inert unless dispatched; deleting `agents/` removes them.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| First live pipeline run | Stages hand off + gate correctly | FlyFission | a Standard+ change | fix the defs; patch |
| Over-use on trivial work | The pipeline fires only at Standard+ | FlyFission | usage | tighten the descriptions |

## Handoff

- Operator/customer/support notes: dispatch the subagents for Standard+ changes; the baton pass is documented in `agents/README.md`.
- Docs/runbook updated: `agents/README.md`.
- Communication needed: note the pipeline in release notes when cut.
- Turnover record if activated: not activated.
- Follow-up date: when a maintainer runs the pipeline live.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: the defs are valid, encode the authority split, and carry the honesty caveat; the only unproven step (a live orchestration) is low-risk and reversible, and the confinement limit is documented, not hidden.
- Decision question answered by evidence? yes for the defs + authority encoding; the live run is the named residual.
- Conditions attached: maintainer reviews the authority model and runs one live orchestration before announcing.
- Decision posture: conservative enough.
- Abort or rollback trigger: an authority-split test failure, or live-orchestration breakage → revert.
- OPEX or post-release learning trigger: a live run that misbehaves updates the defs.

## Baseline trigger

- Baseline required? yes
- Baseline record: the five agent defs + the README become controlled items.
- Revalidation trigger: a subagent frontmatter schema change, or the plugin gaining permissionMode support.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's PR.
- Monitoring/dashboard/log query: live-run observation; GitHub issues.
- Rollback/runbook: delete `agents/` + the test.

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

Original Nuclear-grade record inspired by public ideas on configuration management, human performance improvement, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
