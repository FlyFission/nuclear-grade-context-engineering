# Decision Record

**Purpose:** Record the decision to ship, block, defer, or continue with named residual risk.

**Activation threshold:** Use when evidence has been reviewed and the change needs an explicit decision before baseline, release, or operation.

**Minimum useful version:** Decision, evidence status, unresolved gaps, owner, conditions, and baseline trigger.

---

## Change context

- Slug:
- Owner:
- Date:
- Current golden-path phase: Decide
- Related verification:
- Related independent review:

## Evidence status

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Questioning attitude | | `questioning-attitude.md` | |
| Specification | | `spec.md` / `basis.md` | |
| Verification | | `verification.md` | |
| Review | | `independent-review.md` / review notes | |

## Decision

- Decision: ship / block / defer / continue with residual risk
- Decision maker:
- Rationale:
- Conditions attached:
- Decision posture: conservative enough / not conservative enough:
- Abort or rollback trigger:

## Residual risks and gaps

| Risk / gap | Disposition | Owner | Recheck trigger |
|---|---|---|---|
| | accept / mitigate / defer / block | | |

## Baseline trigger

- Baseline required? yes/no:
- Baseline record:
- Revalidation trigger:

## Required links

- `risk.md`
- `verification.md`
- `ship.md` or release record:
- `baseline.md` if activated:

## Exit criteria

- Decision is explicit.
- Gaps are not used as evidence.
- Residual uncertainty is bounded, owned, or blocks/defer the decision.
- Baseline or revalidation action is named when controlled state changes.

## Source-lineage note

Original Nuclear-grade template inspired by public review, decision, release-readiness, and configuration-management concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
