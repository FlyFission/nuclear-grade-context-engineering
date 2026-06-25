# Actor-Evidence Independence — Plan

## Purpose

Bound the amendment so it lands coherently across the surfaces it touches.

## Build sequence

| # | Step | Reqs | Proof | Stop/done |
|---|---|---|---|---|
| 1 | Write the doctrine page (failure, rungs, gates, limits) | REQ-001 | Page exists and is internally consistent | Page reviewed |
| 2 | Add the self-authorship boundary as the dual in the authority model | REQ-001 | Section present with independence rungs | Section reviewed |
| 3 | Wire the seam into the loop docs and the skills | REQ-002 | Concept reachable at each gate | Grep confirms |
| 4 | Add template fields and the honest validator/threat-model posture | REQ-003 | Fields present; check kept as disclosure | Reviewed |
| 5 | Validate: tests, lint, doctor, tokens, packet validators | REQ-004 | All green | CI passes |

## Non-goals

- A runtime enforcement of independence (the tooling discloses; it does not enforce).
- A new skill, command, or template mode.
- Any formal-assurance claim.

## Rollback approach

- Rollback method: revert the branch; all changes are documentation and templates under normal git history.
- Owner: FlyFission.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Doctrine reviewed | The failure and defense are stated and internally consistent | pass |
| Wiring reviewed | The seam is named at each trust-bearing gate | pass |
| Independent human review | A reviewer agrees the doctrine closes the gap | gap |

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Verification: `verification.md`

## Exit criteria

- The work is bounded and the non-goals are explicit.
- Rollback is stated.
- The independent-review checkpoint is named and left open until a human signs off.

## Source-lineage note

Original Nuclear-grade packet inspired by public software-lifecycle and configuration-management ideas mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
