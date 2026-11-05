# Risk: record paths and artifact checks

## Selected mode

- **Mode:** Standard
- **Why this mode:** Public data, filesystem writes, executable agent cleanup, and release-facing wording cross trust boundaries. The user explicitly authorized fixing the reported issues, pushing a PR, and working toward a clean merge on 2026-11-05. Maintainer merge/release review remains separate.

## Mission anchor

Fix the verified artifact review findings while retaining useful research metadata and reproducible evidence. Work type: defect-fix; posture: Sweeper. Scope is the existing isolated checkout on a feature branch, not a new worktree. No new runtime dependencies, broad assurance claims, deletion of pre-existing branches, history rewrite, or release publication.

- Success criteria: verified defects fixed, regression tests and full validation pass, and a reviewable PR is prepared.
- Non-goals / forbidden directions: no history rewrite, deletion of pre-existing branches, release publication, or certification.

## Consequence and uncertainty

A malformed slug can write fixed template filenames outside the repo; a surviving agent child can defeat timeout cleanup. Copied third-party abstracts have an unverified reuse basis. A normal PR cannot erase external clones or GitHub cached PR references. Reversible code/data removal is delegated; irreversible history operations are excluded pending a coordinated maintainer plan.

## Controlled items

CLI/MCP scaffolding; challenge harness and tests; artifact review checks; research JSON; release inventory; history-cleanup guidance; this packet and evidence badge. Rollback: revert the PR, while retaining awareness that this reintroduces documented defects and copied abstract text.

## Evidence bar and stop conditions

Tests first for name traversal, absolute/Windows names, symlink escapes, inherited output pipes, transcript/diff/email coverage, and copied abstract fields. Run the complete suite, lint, doctor, tokens, release identity, packet validation, badge consistency, build and installed-wheel smoke. Hold merge for failing CI, material review findings, or an unresolved destructive action. Windows-native process-tree validation remains a named gap if no Windows executor is available.

## Required links

[risk.md](risk.md), [basis.md](basis.md), [plan.md](plan.md), [trace.md](trace.md), [verification.md](verification.md), [ship.md](ship.md).

## Exit criteria

The scoped regressions pass, remaining gaps are explicit, and maintainer review precedes merge.

## Source-lineage note

Original project remediation record using the public-source workflow mapped in [source-map.md](../../../docs/00-standards-foundation/source-map.md). No certification, legal opinion, or assurance claim.
