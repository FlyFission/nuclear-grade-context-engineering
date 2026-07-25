# Ship — targeted agent reading

## Release decision

**Decision: defer to PR review.** The candidate is a reversible instruction simplification. Merge authority remains with the human reviewer; this packet does not authorize merge.

Residual risk: an agent may under-read. The wording mitigates this by preserving the applicable change record and directing task-triggered retrieval rather than forbidding either root document.

## Rollback

Revert the single commit to restore the blanket preload instruction. No data migration or operational restore is involved.

## Monitoring

During review and later agent runs, watch for missed workflow requirements attributable to selective reading. If observed, revert or name specific trigger conditions rather than restoring an unconditional full preload.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)
- Changed item: [`AGENTS.md`](../../../AGENTS.md)

## Exit criteria

Verification passes, the PR exposes the coupled evidence path, and a reviewer makes the final merge decision.

## Source-lineage note

This is a repository change decision, not a compliance, certification, safety, security, or regulatory-assurance claim. Sources are bounded in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
