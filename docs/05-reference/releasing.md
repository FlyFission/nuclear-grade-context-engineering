# Releasing

**Purpose:** Cut a release so one version means one thing everywhere it is declared, and the evidence behind it can be checked later.

Pattern lineage: uber/ADR's release procedure (the tag must match the version, a published tag is never moved). See `../00-standards-foundation/source-map.md`, Tier 6.

## Before the tag

1. Write or update the ship-readiness record for the release (`checking-release-readiness`). The release stance changes only with that record.
2. Set the same version in `pyproject.toml`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, and `CITATION.cff`.
3. Move the `[Unreleased]` entries in `CHANGELOG.md` under `## [X.Y.Z] - YYYY-MM-DD`, and set `CITATION.cff` `date-released` to the same date.
4. Run the gates in `../../GOVERNANCE.md`, plus:

   ```bash
   python -m nuclear_grade.release            # versions, citation, and changelog agree
   python -m nuclear_grade.release --tag vX.Y.Z
   ```

   CI runs the first form on every PR, so drift fails before release day.
5. Merge to `main` through the PR gate.

## Tag and publish

```bash
git tag -a vX.Y.Z -m "vX.Y.Z" <merge-commit>
git push origin vX.Y.Z
```

Attach the wheel, the sdist, and `ng validate --json` receipts for the shipped change records to the GitHub release, along with a `SHA256SUMS` file covering them.

A pushed tag is never moved or reused. A correction ships as a new version.

## Not yet automated

A tag-triggered workflow (identity check, gates, build, receipts, GitHub release, and an opt-in PyPI Trusted Publishing job behind a protected environment) is drafted but not merged. It creates public release artifacts, so it needs the maintainer's explicit approval. The package is not on PyPI today.

## Boundary note

A consistent release identity and receipts show which bytes shipped and which checks ran. They do not show the release is adequate, safe, secure, or compliant.
