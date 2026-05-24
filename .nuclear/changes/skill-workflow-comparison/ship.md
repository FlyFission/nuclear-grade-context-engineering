# Ship - Skill and Workflow Comparison

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Risk classification | pass | `risk.md` |
| Basis / claims | pass | `basis.md` |
| Coverage verification | pass | `verification.md` |
| Boundary review | pass | `verification.md` |
| Trial-record depth | pass | `verification.md` |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Evaluation is qualitative | Readers may treat it like a benchmark. | mitigate | maintainer | Any wording that implies measured performance. |
| Use cases are sandbox scenarios | Results may not generalize to every team. | accept | maintainer | When adding empirical case studies. |

## Rollback / restore plan

- Revert comparison README, `EXAMPLES.md` update, packet, and coverage tests.

## Monitoring and post-release checks

- Watch issues/discussions for confusion about whether this is a benchmark or assurance result.
- Add empirical examples only when supported by reproducible artifacts.

## Release decision

- Decision: ship with residual risk
- Decision maker: maintainer
- Rationale: Coverage tests and packet validation pass; residual risk is bounded by qualitative-evaluation language and rollback path.

## Baseline trigger

- Baseline required? yes
- Baseline record: this packet and the resulting commit.
- Revalidation trigger: any new skill, command, workflow, or public claim about evaluation results.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `source-map.md`

## Exit criteria

- Release decision is explicit.
- Evidence status and gaps are visible.
- Rollback/restore path exists.

## Source-lineage note

Original release decision record mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
