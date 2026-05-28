# Agent Trace Evidence

**Purpose:** Define what execution evidence to capture from an agent run, at what granularity, and how to link it into packet records.

## Why this exists

Agent execution produces side effects — file edits, API calls, command runs, token use — that functional output alone does not explain. When the execution path matters for verification, release decisions, or post-incident review, structured trace evidence closes that gap.

## What to capture

For each consequential step in the agent's execution:

| Evidence type | What to record |
|---|---|
| Tool call | Action name, tool, inputs (abbreviated), output, result |
| Decision point | Choice made, constraint applied, authority boundary check |
| Approval gate | Reviewer, date, decision (approved / blocked / deferred) |
| Token use | Prompt and completion token counts per step (where cost or efficiency is a criterion) |
| Latency | Wall time per step and total elapsed time (where performance is a criterion) |
| Error or fallback | Error description, recovery attempted, scope check |

"Consequential" means the step could affect verification claims, release posture, or downstream systems. Read-only exploration with no side effects is not consequential.

## Granularity

Capture at the step level, not the prompt level. A step is one tool call, one decision point, or one approval gate. If the agent produced ten file edits and five API calls, that is fifteen trace rows plus approval gate records — not one "execution summary."

## Linking to claims

Every trace row should reference the claim in `verification.md` it supports. Example:

| Step | Action | Evidence status | Claim supported |
|---|---|---|---|
| 3 | `write_file(auth.py)` | pass | REQ-002: only auth.py is modified |

## When to activate

Use trace evidence when any of these apply:

- The packet relies on agent execution to satisfy a verification claim.
- The release decision requires confirming the agent acted within its authority scope.
- Token cost or latency is a verification criterion.
- A post-incident or OPEX review needs to reconstruct what the agent did.

If a dedicated observability platform (OpenTelemetry, W&B Weave, Phoenix) is already capturing structured agent traces, cross-link the platform's export into the packet rather than duplicating it.

## Relationship to trace.md and verification.md

`trace.md` records the implementation lineage: what was specified, what was built, and what changed. Agent trace evidence adds the execution dimension: what the agent actually did, step by step, while building. Both feed `verification.md`.

## Minimum useful version

- Consequential steps with action, inputs, outputs, and evidence status.
- Decision-point records with constraint and authority reference.
- Approval gate records with reviewer, date, and decision.
- Execution posture summary linked to `ship.md`.

Use `skills/tracing-agent-execution/SKILL.md` for the full process.
Use `commands/ng-trace.md` as a portable agent prompt.
Use `templates/standard/execution-trace.md` when trace volume warrants a separate record.

## Boundaries

Execution trace evidence is scoped engineering record, not a formal audit trail. It proves what was captured; it does not prove what was not captured. Unlogged actions are not evidenced.

## Source-lineage note

Influenced by W&B Weave trace-tree observability (span-per-call, audit lineage, reproducibility), NVIDIA NeMo Agent Toolkit profiling model (token/latency/cost per step), and OpenTelemetry distributed tracing concepts (structured spans, parent-child relationships). All mapped as supporting context in `docs/00-standards-foundation/source-map.md`. Not a compliance or certification artifact.
