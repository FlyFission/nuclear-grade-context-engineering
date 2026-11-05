# Trace — bounded review evidence

| Claim | Changed control | Evidence | Status |
|---|---|---|---|
| REQ-001 | evaluation-integrity §5; panel budget input | E-001 | pass |
| REQ-002 | proving-claims actual-boundary section | E-001 | pass |
| REQ-003 | proving-claims hash/derivation section | E-001 | pass |
| REQ-004 | panel follow-up step; proving-claims parity section | E-001 | pass |

| REQ-005 | [review-run checker](../../../nuclear_grade/review_run.py), existing validate CLI and [templates](../../../templates/review-run/README.md) | E-003 | pass |

E-003 is the behavioral CLI regression and full repository check recorded in verification.

E-001 is the reproducible structural/docs verification in [verification](verification.md), not an
experiment demonstrating agent adherence or a reproduction of the motivating application runs.

## Required links

- [Risk](risk.md), [basis](basis.md), [plan](plan.md), [trace](trace.md), [verification](verification.md), [ship](ship.md).
- [Controlled items](controlled-items.md), [operating lesson](opex.md).

## Exit criteria

The scoped wording passes the recorded checks and remains pending human PR review.

## Source-lineage note

An original operational refinement of existing evidence custody and evaluation discipline; see the repository [source map](../../../docs/00-standards-foundation/source-map.md). No compliance, independence, efficacy, or formal assurance claim.
