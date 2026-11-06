# Ship: Prepare release 0.7.0

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request. Merging it and pushing the `v0.7.0` tag stay with the maintainer.

Residual risk:

- E-001 to E-004 are self-checks by the AI agent that wrote the change. CI on a clean runner and the release workflow run on the tag are still to come.
- The release workflow has never run, because the repository has no tags yet. The first `v*` tag is its first real test.
- The README's install lines point at PyPI, so they work only after the first upload.

## Rollback

Before the tag: revert the commit. After the tag: a pushed tag is never moved; a correction ships as 0.7.1.

## Monitoring

Watch the Release workflow on the tag. When it is green, check that the GitHub release has the wheel, the sdist, `SHA256SUMS`, and the receipts, and, if PyPI is on, that `pipx install nuclear-grade` works on a clean machine.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge and tag decisions.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
