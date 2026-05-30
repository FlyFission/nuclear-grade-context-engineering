# U09 - Release Readiness Cut

## Scenario Facts

- A project is preparing a public v0.2 release.
- CI is green.
- Docs, examples, package metadata, and release notes changed.

## Simple Prompt Trial

Prompt:

```text
Prepare the release. CI is green, so cut v0.2.
```

Expected simple output:

- Update version.
- Create release notes.
- Tag release.

Simple path strengths:

- Fast release mechanics.
- Uses CI as a basic gate.

Simple path gaps:

- Treats green CI as the same thing as being ready.
- May skip rollback, monitoring, a package smoke test, a correct changelog, and the support handoff.
- Does not save the accepted release files as the known-good version.
- Does not surface leftover risks or docs and examples that were put off.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `recording-a-known-good-version`
- `rating-change-risk`
- `creating-change-records`
- `handing-off-work`
- `learning-from-experience`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent turnover
- Release readiness
- OPEX learning

Nuclear-grade output:

- Controlled items: the version, the changelog, the package metadata, the docs, the examples, the CI result, and the release notes.
- Impact screen: the README, the install docs, the examples, the package metadata, the workflows, and the support docs.
- Proof claims: the install command works; the examples pass the validator; the changelog matches the changes; CI passes; there are no banned assurance claims.
- Release decision: ship, defer, block, or ship with leftover risk.
- Turnover: the release owner and support owner get the accepted file state, the leftover risk, the monitoring, and the rollback notes.
- Baseline: the release tag and the accepted file state.
- Monitoring: watch issues and discussions, smoke-test the package install, and check the docs after release.
- OPEX (lessons from real operation): surprises after release feed back into docs, tests, templates, monitors, or a new known-good version.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 5 | 4 | 4 | 5 | 3 |

Nuclear-grade is better because release readiness is a decision record, not just a CI status.

## Decision

Use the Release readiness workflow for public releases.

## Boundary Note

This trial does not prove release suitability for all users or environments.
