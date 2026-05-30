# U07 - Payment Webhook Idempotency

## Scenario Facts

- A SaaS app processes payment webhooks (callbacks the payment provider sends to the app).
- The same webhook can arrive twice, which can create duplicate credits or invoices.
- The change makes the handler idempotent (safe to run twice with the same result) and adds release notes.

## Simple Prompt Trial

Prompt:

```text
Make the payment webhook idempotent and add tests.
```

Expected simple output:

- Add idempotency key check.
- Add one duplicate-event test.
- Report tests pass.

Simple path strengths:

- Directly targets the obvious bug.
- Useful first implementation step.

Simple path gaps:

- May not treat side effects that move money as controlled items.
- May skip questions about events arriving at once, replays, partial failures, and rollback.
- May not name monitoring or the handoff to customer support.
- May not limit the agent's power over payment APIs or credentials.

## Nuclear-Grade Trial

Skills exercised:

- `questioning-attitude`
- `using-nuclear-grade`
- `choosing-what-to-control`
- `checking-what-a-change-affects`
- `rating-change-risk`
- `creating-change-records`
- `briefing-an-agent`
- `double-checking-before-acting`
- `vetting-outside-code-and-models`
- `proving-claims`
- `checking-release-readiness`

Workflows exercised:

- Questioning attitude
- Standard change
- Controlled configuration
- Agent authority change
- Critical action self-check
- Trust check
- Release readiness

Nuclear-grade output:

- Mode: Standard, and maybe stronger human review, because money-moving behavior is affected.
- Controlled items: the webhook handler, the store of already-seen events, the payment provider's event format, the ledger and credit side effects, and the monitoring alerts.
- Context pack: the agent may edit the handler and tests; may not use live credentials, call production APIs, or change billing data.
- Self-check: name the exact payment provider, the expected behavior for a duplicate event, and the stop condition before touching any payment path.
- Trust check: keep the provider's event-format claims apart from the local evidence on replays, invalid signatures, and partial failures.
- Proof claims: a duplicate event does not credit twice; a partial failure can retry safely; an invalid signature is denied; an event replay is logged.
- Release decision: release only with a rollback path, a monitoring query, a support note, and an owner for the leftover risk.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 5 | 4 |

Nuclear-grade is well worth it here because duplicate billing or credits are high-stakes, visible to users, and tricky in operation.

## Decision

Use Standard mode with a release-readiness check and clear limits on the agent's power.

## Boundary Note

This trial does not prove payment correctness, financial control adequacy, or compliance.
