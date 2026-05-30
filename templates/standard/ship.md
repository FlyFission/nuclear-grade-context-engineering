# Standard Ship Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Make the release decision explicit: ship, block, defer, or ship with named residual risk.

**Activation threshold:** Use when a Standard change is merged/released, when release posture changes, or when users/operations/dependencies/security/data/AI authority are affected.

**Minimum useful version:** Evidence status, residual risks, rollback/restore, monitoring, handoff, release decision, and baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and operational controls are ready.

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

- Release decision is explicit.
- Slow-audit acceptance is complete before baseline or public claims are accepted.
- Baseline trigger is explicit when controlled state changes.
- Evidence status and gaps are visible.
- Residual uncertainty is bounded, owned, or blocks/defer the decision.
- Rollback/restore path exists or the lack is consciously accepted.
- Monitoring/handoff covers the claims most likely to fail in operation.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade template inspired by public configuration-management, release-readiness, secure-development, software-assurance, supply-chain, lifecycle, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
