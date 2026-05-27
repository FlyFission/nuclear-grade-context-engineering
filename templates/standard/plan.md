# Standard Plan Template

**Purpose:** Bound the work so implementation, review, verification, and rollback are planned before the change expands.

**Activation threshold:** Use for Standard changes where the implementation has multiple steps, affected configuration items, dependency/model/tool decisions, rollback concerns, or review sequencing needs.

**Minimum useful version:** Build sequence, affected files/assets, non-goals, review checkpoints, rollback approach, and proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions needed to build and review the change without losing intent.

---

## Change context

- Slug:
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner:
- Date:
- Current lifecycle phase: Plan / Execute / Verify / Review / Decide

## Build sequence

Number the minimum steps needed to complete the change.

1.
2.
3.

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| | | | | |

## Agent briefing

- Role:
- Authority source:
- Active procedure/template:
- Last completed action if resumed:
- Handoff or turnover needed? yes/no:
- Pause when unsure condition:

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| | | | |

## Non-goals

List what this change intentionally does not do.

-
-

## Dependency / model / tool decisions

Use only if activated.

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| | | | | |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Specification reviewed | Protected/unacceptable outcomes and assumptions are explicit. | planned / pass / gap |
| Tests/evals defined | Evidence maps to claims. | planned / pass / gap |
| Build complete | Affected files match plan. | planned / pass / gap |
| Verification complete | Evidence is linked in `verification.md`. | planned / pass / gap |
| Release decision ready | Residual risks and rollback are recorded. | planned / pass / gap |
| Turnover complete if activated | Next owner has state, authority, stop criteria, and remaining work. | planned / pass / gap |

## Rollback approach

- Rollback method:
- State/data reversal notes:
- Feature flag / kill switch:
- Owner:
- Time to restore estimate:

## Proof commands

```bash
# command(s) or manual checks needed before ship
```

## Required links

- `risk.md`
- `basis.md` or `spec.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc:

## Exit criteria

- Work is bounded enough to prevent scope creep.
- Review checkpoints are explicit.
- Rollback/restore thinking exists before release.
- Proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public lifecycle, configuration-management, software assurance, secure-development, release-readiness, and operating-learning sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
