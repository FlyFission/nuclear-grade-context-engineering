# Ship — instruction conflict routing

## Release decision

**Decision: defer to PR review.** The candidate is a reversible agent-instruction change. Merge authority remains with the human reviewer; this packet does not authorize merge.

Residual risk: an agent may over-read ordinary tension as a conflict and stop unnecessarily. The wording limits the stop to an affected action after documented precedence fails to resolve the conflict.

## Rollback

Revert the single commit to remove the bullet and this packet. No data migration or operational restore is involved.

## Monitoring

Watch later agent runs for false stops or silent conflict resolution. If false stops recur, narrow the trigger; if silent resolution recurs, add a small fixture before considering runtime enforcement.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)
- Changed item: [`AGENTS.md`](../../../AGENTS.md)

## Exit criteria

Verification passes, the PR exposes the coupled evidence path, and a reviewer makes the final merge decision.

## Source-lineage note

This is a repository change decision, not a compliance, certification, safety, security, or regulatory-assurance claim; source boundaries remain those in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).