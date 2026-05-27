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

- Equates green CI with readiness.
- May omit rollback, monitoring, package smoke test, changelog accuracy, and support handoff.
- Does not baseline accepted release artifacts.
- Does not expose residual risks or deferred docs/examples.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `identifying-controlled-items`
- `screening-change-impact`
- `baselining-configuration`
- `classifying-change-risk`
- `creating-change-packets`
- `turning-over-agent-work`
- `learning-from-opex`
- `proving-claims`
- `reviewing-ship-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent turnover
- Release readiness
- OPEX learning

Nuclear-grade output:

- Controlled items: version, changelog, package metadata, docs, examples, CI result, release notes.
- Impact screen: README, install docs, examples, package metadata, workflows, support docs.
- Proof claims: install command works; examples validate; changelog matches changes; CI passes; no forbidden assurance claims.
- Release decision: ship, defer, block, or ship with residual risk.
- Turnover: releaser/support owner gets accepted artifact state, residual risk, monitoring, and rollback notes.
- Baseline: release tag and accepted artifact state.
- Monitoring: issue/discussion watch, package install smoke, post-release docs check.
- OPEX: post-release surprises feed docs, tests, templates, monitors, or baseline changes.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 5 | 4 | 4 | 5 | 3 |

Nuclear-grade is better because release readiness is a decision record, not a CI status.

## Decision

Use Release readiness workflow for public releases.

## Boundary Note

This trial does not prove release suitability for all users or environments.
