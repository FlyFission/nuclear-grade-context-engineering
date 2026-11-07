# Releasing

**Purpose:** Cut a release so one version means one thing everywhere it is declared, and the evidence behind it can be checked later.

Pattern lineage: uber/ADR's release procedure (the tag must match the version, a published tag is never moved). See `../00-standards-foundation/source-map.md`, Tier 6.

## Before the tag

1. Write or update the ship-readiness record for the release (`checking-release-readiness`). The release stance changes only with that record.
2. Set the same version in `pyproject.toml`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `plugins/nuclear-grade-guard/.claude-plugin/plugin.json`, and `CITATION.cff`.
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

Pushing the tag runs `.github/workflows/release.yml`. It first refuses a tag whose commit is not already on the default branch, so a mistagged topic commit never builds. It then re-checks the release identity against the tag, runs the release gates, the MCP server tests against both supported SDK majors, and a CLI smoke test of the built wheel installed in a clean environment, builds the wheel and sdist, writes `ng validate --json` receipts for every change record, and creates the GitHub release with the distributions, receipts, and a `SHA256SUMS` file.

A pushed tag is never moved or reused. A correction ships as a new version.

## PyPI (off by default)

The `pypi` job runs only when the repository variable `PUBLISH_TO_PYPI` is `true`. Before turning it on:

1. Create a `pypi` environment in the repository settings (Settings, Environments, New environment), add required reviewers, and limit its deployment branches and tags to `v*` tags.
2. On PyPI, add a Trusted Publisher. Before the first upload the project does not exist yet, so use a pending publisher (Your account, Publishing, Add a new pending publisher) with project name `nuclear-grade`, owner `FlyFission`, repository `nuclear-grade-context-engineering`, workflow `release.yml`, and environment `pypi`.
3. Set the repository variable `PUBLISH_TO_PYPI` to `true` (Settings, Secrets and variables, Actions, Variables).

CI and the release build both run `twine check --strict`, so a package page that would not render on PyPI fails before any upload. PyPI shows `README.md` without the repo around it, so the build points its relative links and images at GitHub (`hatch-fancy-pypi-readme` in `pyproject.toml`); the file itself is unchanged.

Publishing uses OIDC, so there is no long-lived token to leak. The package is not on PyPI today.

## Boundary note

A consistent release identity and receipts show which bytes shipped and which checks ran. They do not show the release is adequate, safe, secure, or compliant.
