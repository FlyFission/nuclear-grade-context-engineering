# U02 - Agent Workspace Boundary

## Scenario Facts

- An AI agent can write files during a coding task.
- The system must prevent writes outside an approved workspace root.
- The change includes a path guard, tests, and a public worked-example claim.

## Simple Prompt Trial

Prompt:

```text
Add a guard so the agent can only write inside the workspace. Include tests.
```

Expected simple output:

- A path check implementation.
- A happy-path test and perhaps a traversal test.
- A statement that tests pass.

Simple path strengths:

- Fast implementation.
- Likely catches the basic traversal case.

Simple path gaps:

- May compare strings instead of canonical paths.
- May omit symlink escape, absolute path escape, or denied-action audit visibility.
- May imply the guard is a complete sandbox.
- Does not name the agent's allowed and forbidden authority.
- Does not create a release decision or non-claims.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `rating-change-risk`
- `creating-change-records`
- `briefing-an-agent`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent authority change
- Release readiness

Nuclear-grade output:

- Decision question: can agent file-write authority be bounded to the approved workspace root?
- Controlled items: workspace guard, write authority, audit event behavior, worked-example claim.
- Mode: Standard because agent write authority changes a trust boundary.
- Proof claims: allowed in-root write; parent traversal denied; absolute external path denied; symlink escape denied; denial emits audit event.
- Context pack: agent may edit guard and tests only; may run targeted tests; may not broaden filesystem authority or claim production sandbox adequacy.
- Release decision: ship as scoped worked example with residual risk, not as production sandbox.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 4 | 4 |

Nuclear-grade is materially better because the risk is not just code correctness. The real issue is authority, evidence, and public non-claims.

## Decision

Use Nuclear-grade Standard mode. The overhead is justified by agent authority and public trust implications.

## Boundary Note

This trial does not prove the guard is safe, secure, complete, production-ready, or suitable for regulated use.
