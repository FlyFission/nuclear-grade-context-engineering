# Agent Trace Evidence

**Purpose:** This file says what evidence to capture from an agent run, how fine-grained to make it, and how to link it into change records.

## Why this exists

When an agent runs, it makes things happen: file edits, API calls, command runs, token use. The final output alone does not explain those side effects. When the path the agent took matters for verification, release decisions, or review after an incident, a clear step-by-step trace closes that gap.

## What to capture

For each step in the agent's run that has real consequence:

| Evidence type | What to record |
|---|---|
| Tool call | Action name, tool, inputs (abbreviated), output, result |
| Decision point | Choice made, constraint applied, authority boundary check |
| Approval gate | Reviewer, date, decision (approved / blocked / deferred) |
| Token use | Prompt and completion token counts per step (where cost or efficiency is a criterion) |
| Latency | Wall time per step and total elapsed time (where performance is a criterion) |
| Error or fallback | Error description, recovery attempted, scope check |

"Real consequence" means the step could change a verification claim, a release decision, or a system further down the line. Read-only looking around, with no side effects, does not count.

## Granularity

Capture at the step level, not the prompt level. A step is one tool call, one decision point, or one approval gate. If the agent made ten file edits and five API calls, that is fifteen trace rows plus the approval gate records. It is not one "run summary."

## Linking to claims

Every trace row should point to the claim in `verification.md` it supports. For example:

| Step | Action | Evidence status | Claim supported |
|---|---|---|---|
| 3 | `write_file(auth.py)` | pass | REQ-002: only auth.py is modified |

## When to activate

Use trace evidence when any of these apply:

- The change record leans on the agent's run to back a verification claim.
- The release decision needs proof the agent stayed inside what it was allowed to do.
- Token cost or speed (latency) is something you must verify.
- A review after an incident, or an OPEX review, needs to rebuild what the agent did.

If a tool that watches your systems (OpenTelemetry, W&B Weave, Phoenix) is already capturing clean agent traces, link to that tool's export from the record instead of copying it.

## Relationship to trace.md and verification.md

`trace.md` records the build history: what was specified, what was built, and what changed. Agent trace evidence adds the run side: what the agent actually did, step by step, while building. Both feed `verification.md`.

## Minimum useful version

- Steps with real consequence, each with its action, inputs, outputs, and evidence status.
- Decision-point records with the limit applied and the authority reference.
- Approval gate records with reviewer, date, and decision.
- A short summary of how the run went, linked to `ship.md`.

Use `skills/recording-what-an-agent-did/SKILL.md` for the full process.
Use `commands/ng-trace.md` as a portable agent prompt.
Use `templates/standard/execution-trace.md` when trace volume warrants a separate record.

## Boundaries

A run trace is a focused engineering record, not a formal audit trail. It proves what was captured. It does not prove what was not captured. Actions that were never logged are not evidenced.

## Source-lineage note

Influenced by W&B Weave trace-tree observability (one record per call, audit history, the ability to reproduce a run), the NVIDIA NeMo Agent Toolkit profiling model (token, latency, and cost per step), and OpenTelemetry distributed tracing ideas (structured records with parent-child links). All are mapped as supporting context in `docs/00-standards-foundation/source-map.md`. Not a compliance or certification artifact.
