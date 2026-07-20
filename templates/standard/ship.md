# Standard Ship Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

**Activation threshold:** Use when a Standard change is merged or released, when the release stance changes, or when users, operations, dependencies, security, data, or AI power are affected.

**Minimum useful version:** the evidence status, the leftover risks, the rollback/restore plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and the operational controls are ready.

---

## Release identity

- Change slug:
- Version / release / baseline:
- PR / commit / artifact:
- Owner:
- Date:
- Intended release window:

## Scope and exclusions

- Included:
- Excluded:
- Known non-goals:

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | | `risk.md` | |
| Basis / requirements / claims | | `basis.md` | |
| Questioning attitude | | `questioning-attitude.md` if activated | |
| Verification | | `verification.md` | |
| Dependency / supply-chain evidence | | | |
| AI-assisted work checks | | | |
| Evidence custody / coupling profile | | `verification.md` | |
| Review / approval | | | |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| | | accept / mitigate / defer / block | | |

## Rollback / restore plan

- Rollback method:
- Data migration reversal or restore notes:
- Feature flag / kill switch:
- Owner on call:
- Time to restore estimate:

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| | | | | |

## Handoff

- Operator/customer/support notes:
- Docs/runbook updated:
- Communication needed:
- Turnover record if activated:
- Follow-up date:

## Release decision

This is the **verdict** on correctness and release-worthiness — *should this draft become the accepted version?* The verdict owner and any residual coupling to the actor must be visible. It is **not, by itself, authorization to apply right now**; that is the separate **Apply clearance** section below. A `ship` verdict says what the admitted evidence supports, not that the current moment is the right one to apply it.

- Decision: ship / do not ship / defer / ship with residual risk
- Decision maker:
- Rationale:
- Decision question answered by evidence? yes/no:
- Verdict owner's authority axis relative to the actor: coupled / partially separated / separated; why:
- Minimum coupling profile for this consequence met? yes / no; gap if no:
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes/no:
- Conditions attached:
- Decision posture: conservative enough / not conservative enough:
- Abort or rollback trigger:
- OPEX or post-release learning trigger:

## Apply clearance

The release decision above answers *what does the evidence support*. This section answers a **different question**: *may this exact candidate be applied to this target right now?* The two states line up most of the time, but once a change touches production they can diverge — approvals lapse, a freeze/maintenance window closes, external state drifts, or deployment policy changes after the verdict. A `ship` verdict is **not a standing authorization**: clearance is checked against operational reality at apply-time and can lapse. Clearance is an operator/policy call with explicit authority; its required separation from the change actor is consequence-specific (see `docs/02-operating-system/actor-evidence-independence.md`).

If the change makes no real-world action (for example a docs-only change that is its own apply), mark clearance `not applicable` and say why.

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | yes / no / not applicable | |
| Release / maintenance (freeze) window open | yes / no / not applicable | |
| External state unchanged since verification — verdict not stale | yes / no | |
| Deployment policy satisfied | yes / no / not applicable | |
| Rollback / kill-switch confirmed ready at apply-time | yes / no | |

- Clearance decision: cleared to apply / hold / lapsed / not applicable (no real-world action)
- Cleared by (operator or policy owner, independent of the actor where trust-bearing):
- Apply window / valid until:
- Re-clearance trigger: clearance lapses and must be re-confirmed if the apply does not happen within the window, or if approvals, external state, or policy change before apply — re-confirm clearance only, not the correctness verdict.

## Baseline trigger

- Baseline required? yes/no:
- Baseline record:
- Revalidation trigger:

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact:
- Monitoring/dashboard/log query:
- Rollback/runbook:

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
