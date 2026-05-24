# U11 - External API Tool Permission

## Scenario Facts

- An AI agent will be allowed to call an external issue-tracker API.
- The agent needs read access and limited comment creation.
- Credentials and network calls are involved.

## Simple Prompt Trial

Prompt:

```text
Let the agent use the issue-tracker API to inspect issues and comment with status updates.
```

Expected simple output:

- Add API client or tool permission.
- Add docs for the tool.
- Maybe add a smoke test or mock.

Simple path strengths:

- Directly enables useful automation.
- Fast to prototype.

Simple path gaps:

- May over-broaden credentials.
- May not distinguish read, write, delete, assignment, and label authority.
- May not require dry-run or mock proof before live API use.
- May omit audit logging and stop conditions.
- May not baseline permission state.

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
- `proving-claims`
- `reviewing-ship-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent authority change
- Release readiness

Nuclear-grade output:

- Mode: Standard because network, credentials, and write authority are involved.
- Controlled items: API token scope, tool manifest, allowlist, audit log, prompt authority, dry-run behavior.
- Context pack: allowed read endpoints, allowed comment endpoint, forbidden delete/close/assign/label actions, no production credentials in tests.
- Proof claims: denied forbidden actions; dry-run records intended comment; live mode requires explicit approval; audit records tool call.
- Ship decision: block if token scope cannot be least-privilege or audit proof is missing.
- Baseline: accepted permission state and revalidation trigger when token, tool, prompt, or API surface changes.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 1 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 5 | 4 |

Nuclear-grade is strongly justified because credentials, network, and write authority create real blast radius.

## Decision

Use Standard mode with Agent authority and Controlled configuration workflows.

## Boundary Note

This trial does not prove API security, credential safety, or production suitability.
