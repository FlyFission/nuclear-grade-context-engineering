# Ship: record paths and artifact checks

## Release decision

**Decision:** candidate for review; defer merge until full validation, GitHub CI and maintainer review. No version bump, tag, published release or history rewrite is authorized by this record. The user authorized fixes and a PR; the maintainer remains the merge verdict owner.

## Residual risks and gaps

Same-model-family actor-authored evidence remains self-check, as disclosed in [verification.md](verification.md). Earlier commits, old branch/PR tips, external clones and caches can retain previously disclosed personal information and removed third-party text. A PR cannot erase those copies. Native Windows cleanup and real Claude host-version compatibility were not verified in this executor. No exhaustive legal or security conclusion follows from this work. GitHub API network access may be needed for PR/review operations; do not bypass policy.

## Rollback and monitoring

Revert the PR if ordinary record scaffolding or harness execution regresses; this reintroduces known defects, so maintainer review is required. Watch CI, malformed artifact submissions, future raw transcripts, and review findings. Reopen provenance/history items when retained-data scope changes. Stop before destructive cleanup, release publication, or a claim beyond the executed evidence.

## Apply clearance and handoff

Hold. Root agent prepares branch and PR, resolves reversible checks and review defects. Maintainer confirms approvals, merge policy, history/cache cleanup and eventual release state. Work is not accepted merely because tests pass.

## Required links

[risk.md](risk.md), [basis.md](basis.md), [plan.md](plan.md), [trace.md](trace.md), [verification.md](verification.md), [ship.md](ship.md).

## Exit criteria

The scoped regressions pass, remaining gaps are explicit, and maintainer review precedes merge.

## Source-lineage note

Original project remediation record using the public-source workflow mapped in [source-map.md](../../../docs/00-standards-foundation/source-map.md). No certification, legal opinion, or assurance claim.
