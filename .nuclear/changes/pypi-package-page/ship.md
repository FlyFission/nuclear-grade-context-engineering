# Ship: Make the package page ready for PyPI

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request, and merge authority stays with the maintainer. Nothing is published: no tag, no version bump, and PyPI publishing stays off until the maintainer sets it up.

Residual risk:

- E-001 to E-004 are self-checks by the AI agent that wrote the change. CI on a clean runner and a human look at the first real PyPI page are still to come.
- The PyPI page points at `main`, so its images and links show the current repo, which may be newer than the release.
- The build now needs `hatch-fancy-pypi-readme` from PyPI at build time.

## Rollback

Revert the commit. Nothing else holds state.

## Monitoring

Look at the PyPI page after the first upload and fix any link that does not work there.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
