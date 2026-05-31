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

- May compare text strings instead of resolving the real path.
- May skip symlink escape, absolute-path escape, or making denied actions visible in the audit log.
- May imply the guard is a complete sandbox.
- Does not name what the agent is allowed and not allowed to do.
- Does not produce a release decision or a list of things it does not claim.

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

- Decision question: can the agent's power to write files be held to the approved workspace root?
- Controlled items: the workspace guard, the write power, how audit events behave, and the worked-example claim.
- Mode: Standard, because changing the agent's write power changes a line of trust.
- Proof claims: an in-root write is allowed; a parent `../` path is denied; an absolute outside path is denied; a symlink escape is denied; a denial produces an audit event.
- Context pack: the agent may edit the guard and tests only; may run targeted tests; may not widen filesystem power or claim the production sandbox is good enough.
- Release decision: ship as a scoped worked example with leftover risk, not as a production sandbox.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 2 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 4 | 4 |

Nuclear-grade is clearly better here, because the risk is not just whether the code is correct. The real issue is the agent's power, the evidence, and being clear about what the public claim does not cover.

## Decision

Use Nuclear-grade Standard mode. The extra work is worth it because of the agent's power and what it means for public trust.

## Boundary Note

This trial does not prove the guard is safe, secure, complete, production-ready, or suitable for regulated use.
