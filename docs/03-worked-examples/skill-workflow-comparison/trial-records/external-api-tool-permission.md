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

- May give the credentials too much reach.
- May not tell read, write, delete, assign, and label powers apart.
- May not require a dry run or a mock proof before using the live API.
- May skip audit logging and stop conditions.
- May not save the permission state as the known-good version.

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
- `handing-off-work`
- `double-checking-before-acting`
- `vetting-outside-code-and-models`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent authority change
- Agent turnover
- Critical action self-check
- Trust check
- Release readiness

Nuclear-grade output:

- Mode: Standard, because the network, credentials, and write power are involved.
- Controlled items: the API token scope, the tool manifest, the allowlist, the audit log, the prompt power, and the dry-run behavior.
- Context pack: the allowed read endpoints, the allowed comment endpoint, the forbidden delete/close/assign/label actions, and no production credentials in tests.
- Self-check: name the exact token scope, the API endpoint, the expected allow-or-deny behavior, and the stop condition before any live call.
- Turnover: the reviewer or releaser gets the current permission state, the proof still owed, the approval gates, and the forbidden actions.
- Trust check: keep the API and provider claims apart from the local evidence on dry runs, audits, permissions, and approvals.
- Proof claims: forbidden actions are denied; a dry run records the intended comment; live mode needs explicit approval; the audit log records the tool call.
- Release decision: block if the token cannot be held to least privilege, or if the audit evidence is missing.
- Baseline: the accepted permission state, plus a re-check trigger for when the token, tool, prompt, or API surface changes.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 2 | 2 | 2 | 1 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 5 | 4 |

Nuclear-grade is well worth it here because credentials, network access, and write power can do real damage if they go wrong.

## Decision

Use Standard mode with the Agent authority and Controlled configuration workflows.

## Boundary Note

This trial does not prove API security, credential safety, or production suitability.
