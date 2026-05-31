# U03 - Dependency Security Update

## Scenario Facts

- A project uses `requests==2.31.0`.
- A maintainer wants to bump the dependency.
- The project has light tests but no full supply-chain process.

## Simple Prompt Trial

Prompt:

```text
Bump requests to the latest version and run tests.
```

Expected simple output:

- Version changed.
- Tests run or import smoke test passes.
- Brief note that dependency was updated.

Simple path strengths:

- Fast.
- Likely catches direct import breakage.

Simple path gaps:

- "Latest" may be unclear or unchecked.
- It folds "does it still work?" and "is the version free of known security advisories?" into one "tests pass" line.
- The lockfile, the rollback plan, and re-check triggers may be left out.
- It does not tell ship, defer, and block apart.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `recording-a-known-good-version`
- `rating-change-risk`
- `creating-change-records`
- `briefing-an-agent`
- `vetting-outside-code-and-models`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Trust check
- Release readiness

Nuclear-grade output:

- Mode: Standard, because trust in the dependency and the release stance may change.
- Controlled items: the dependency declaration, the lockfile, the advisory review, the smoke tests, and the release note.
- Trust check: keep these apart — the package and version identity, the source claims, the security-advisory evidence, the local smoke-test proof, the rollback plan, and the re-check trigger.
- Claims kept apart:
  - D-001: the runtime behavior still works.
  - D-002: the chosen version has no known security advisories of concern.
  - D-003: the rollback path is known.
- Evidence statuses:
  - Runtime smoke test: pass if the tests run.
  - Advisory review: gap until it is checked.
  - Lockfile: deferred if the project has no lockfile.
- Release decision: block or defer if the advisory evidence is missing, even if the tests pass.
- Baseline trigger: save a new known-good dependency state after the update is accepted.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 4 | 4 | 5 | 4 |

Nuclear-grade is better because a missing advisory check turns into a visible blocker instead of disappearing behind green tests.

## Decision

Use Standard mode for dependency changes that touch security or a release. Use Quick only for dev-only tooling where rollback and proof are trivial.

## Boundary Note

This trial is not a supply-chain assurance result and does not prove dependency safety or security.
