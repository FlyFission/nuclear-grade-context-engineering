# U07 - Payment Webhook Idempotency

## Scenario Facts

- A SaaS app processes payment webhooks.
- Duplicate webhook delivery can create duplicate credits or invoices.
- The change adds idempotency handling and release notes.

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

- May not identify money-moving side effects as controlled items.
- May omit concurrency, replay, partial failure, and rollback questions.
- May not name monitoring or customer-support handoff.
- May not bind agent authority around payment APIs or credentials.

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

- Mode: Standard, possibly stronger human review, because money-moving behavior is affected.
- Controlled items: webhook handler, event idempotency store, payment-provider event schema, ledger/credit side effects, monitoring alerts.
- Context pack: agent may edit handler/tests; may not use live credentials, call production APIs, or alter billing data.
- Self-check: exact payment-provider target, expected duplicate-event behavior, and stop condition are named before touching payment paths.
- Trust check: provider event-schema claims are separated from local replay, invalid-signature, and partial-failure evidence.
- Proof claims: duplicate event does not double-credit; partial failure can retry safely; invalid signature is denied; event replay is logged.
- Release decision: release only with rollback path, monitoring query, support note, and residual risk owner.

## Scoring Rationale

| Path | Decision clarity | Hidden risk discovery | Evidence quality | Ship/defer usefulness | Overhead |
|---|---:|---:|---:|---:|---:|
| Simple prompt | 3 | 2 | 3 | 2 | 1 |
| Nuclear-grade | 5 | 5 | 5 | 5 | 4 |

Nuclear-grade is strongly justified because duplicate billing or credits are high-consequence, user-visible, and operationally sensitive.

## Decision

Use Standard mode with release readiness and agent authority boundaries.

## Boundary Note

This trial does not prove payment correctness, financial control adequacy, or compliance.
