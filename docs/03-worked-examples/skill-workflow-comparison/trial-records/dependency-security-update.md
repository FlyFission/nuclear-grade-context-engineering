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

- "Latest" may be ambiguous or unverified.
- Runtime compatibility and advisory posture are collapsed into one "tests pass" statement.
- Lockfile, rollback, and revalidation triggers may be omitted.
- No decision distinction between ship, defer, and block.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `identifying-controlled-items`
- `screening-change-impact`
- `baselining-configuration`
- `classifying-change-risk`
- `creating-change-packets`
- `packing-agent-context`
- `checking-dependency-and-model-trust`
- `proving-claims`
- `reviewing-ship-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Trust check
- Release readiness

Nuclear-grade output:

- Mode: Standard because dependency trust and release posture may change.
- Controlled items: dependency declaration, lockfile, advisory review, smoke tests, release note.
- Trust check: package/version identity, source claims, advisory evidence, local smoke proof, rollback, and revalidation trigger stay separate.
- Claims separated:
  - D-001: runtime behavior still works.
  - D-002: selected version has acceptable advisory posture.
  - D-003: rollback path is known.
- Evidence statuses:
  - Runtime smoke: pass if tests run.
  - Advisory review: gap until checked.
  - Lockfile: deferred if project has no lockfile.
- Release decision: block or defer if advisory evidence is missing, even if tests pass.
- Baseline trigger: re-baseline dependency state after accepted update.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 4 | 4 | 5 | 4 |

Nuclear-grade is better because a missing advisory check becomes a visible blocker instead of disappearing behind green tests.

## Decision

Use Standard mode for dependency changes with security or release relevance. Use Quick only for dev-only tooling where rollback and proof are trivial.

## Boundary Note

This trial is not a supply-chain assurance result and does not prove dependency safety or security.
