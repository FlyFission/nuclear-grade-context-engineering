# Ship

## Release decision

- **Decision:** ship as a new minor feature on a new branch and PR, once CI is green.
- **Rationale:** The backbone is additive and advisory; it adds two skills, two commands, a charter, a mission anchor, and only-when-present validator checks. Nothing is a breaking change.
- **Pre-merge gates:**
  - `python -m pytest -q` green
  - `ruff check .` clean
  - `python tools/ng.py doctor .` OK
  - `python tools/ng.py validate` OK on every packet including this one
  - CI green (matrix and wheel-smoke from the base branch carry over)

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Verification | pass | `verification.md` |
| Trace | pass | `trace.md` |
| Skills and commands | pass | live doctor + contract tests |
| Validator advisory checks | pass | new validator tests |
| Packet self-validation | pass | `python tools/ng.py validate .nuclear/changes/mission-driven-backbone` |

## Rollback / restore plan

- Each piece is additive; revert the branch commits to restore prior state. No data migration.
- If the advisory mission-anchor check is noisy in practice, narrow `MISSION_ANCHOR_CONCEPTS` or gate it more tightly; this does not require reverting the skills.

## Monitoring and post-release checks

- Watch for false positives from the mission-anchor advisory check and the unresolved-clarification-marker check on real packets; widen the keyword families or the disclaimer markers if legitimate prose is flagged.
- Watch how `ng-drift-check` and `ng-code-review` get used; write an OPEX note (a lesson from real operation) if either skill keeps firing at the wrong time.
- Revisit whether the charter should become a hard gate once the advisory version has proven out.

## Maintainer follow-ups

- Replace `<date>` placeholders in the init `CHARTER_TEMPLATE` output if a dated starter is preferred.
- Consider the deferred contract-evolution PR (description rule, progressive disclosure, evidence coverage).

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`

## Exit criteria

- Decision recorded; rollback named; monitoring named.

## Source-lineage note

Original Nuclear-grade ship record influenced by release-readiness concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
