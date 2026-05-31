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

- Decision: ship / do not ship / defer / ship with residual risk
- Decision maker:
- Rationale:
- Decision question answered by evidence? yes/no:
- Conditions attached:
- Decision posture: conservative enough / not conservative enough:
- Abort or rollback trigger:
- OPEX or post-release learning trigger:

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
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
