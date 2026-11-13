# Risk — outcome stagnation

## Selected mode

- **Mode:** Standard
- **Why:** this changes agent prompt behavior. Decision owner: repository reviewer.

## Mission anchor

Make a missed accepted-deliverable checkpoint trigger inspection of the blocking
artifact and a bounded strategy change even when local checks pass. Non-goals:
new hooks, MCP, tracking infrastructure, weakened gates, bulk reauthoring,
throughput guarantees, merge, release, or changes to downstream Ledger evidence.

Existing doctrine already rejects activity metrics and stops after three failed
goal attempts. The ambiguity is whether locally successful preparation counts as
progress; the entry router also did not explicitly route this case. This change
clarifies doctrine and activation, not automatic runtime enforcement. Risk:
agents may still ignore it. Recheck against live delivery evidence after adoption.

See [basis](basis.md), [plan](plan.md), [verification](verification.md), and [ship](ship.md).

## Required links

[Risk](risk.md) · [basis](basis.md) · [verification](verification.md) · [ship](ship.md)

## Exit criteria

REQ-001 and REQ-002 have reviewable evidence; unchanged acceptance gates and live efficacy gaps remain explicit.

## Source-lineage note

This clarifies existing mission-drift doctrine; no new external source or formal assurance claim. Existing lineage: [source-map.md](../../../docs/00-standards-foundation/source-map.md).
