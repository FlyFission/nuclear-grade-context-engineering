# Decision Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Record the decision to ship, block, defer, or continue with named leftover risk.

**Activation threshold:** Use when the evidence has been reviewed and the change needs a plain decision before baseline, release, or operation.

**Minimum useful version:** the decision, the evidence status, the open gaps, the owner, the conditions, and the baseline trigger.

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

- The decision is stated plainly.
- Gaps are not used as evidence.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A baseline or re-check action is named when the controlled state changes.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on review, decision-making, release readiness, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
