---
name: tracing-agent-execution
description: Captures an agent run's tool calls, decision points, inputs, outputs, token use, and approval gates as structured, reproducible execution evidence linked into the packet trace and verification record. Use when the execution path matters for debugging, auditing, cost review, or defending a release decision. Do not use for a read-only run with no side effects, or to produce a certified compliance audit trail.
---

# Tracing Agent Execution

## Overview

Functional verification proves what an agent produces, not how it got there. When an agent's execution path matters — for debugging, auditing, cost review, or defending a release decision — this skill specifies what execution evidence to capture, at what granularity, and how to link it into the packet's `trace.md` and `verification.md` as reproducible evidence.

## When to Use

- An agent executed consequential tool calls (file writes, API calls, command runs) and the packet needs verifiable execution evidence.
- A release decision depends on whether the agent followed the specified plan, scope, and authority limits.
- Token use, latency, or cost is a verification criterion for the change.
- A reviewer or auditor needs to reconstruct what the agent did without reading a raw chat log.
- A post-incident or OPEX review requires reproducible evidence of execution behavior.

## When Not to Use

- The execution was read-only exploration with no consequential side effects and no release dependency.
- The packet mode is Quick and the proof is a simple, single-step deterministic check.
- A full distributed tracing platform already captures and exports structured agent telemetry; cross-link its output instead of duplicating it.

## Inputs

- Agent execution log, chat transcript, tool-call records, or trace export.
- `basis.md` (intended execution scope, allowed actions, stop conditions).
- `plan.md` (planned sequence of operations).
- Token use, latency, and cost data where relevant.
- Human approval gate records.

## Process

1. Identify the consequential steps in the execution that require trace evidence: any tool call, file edit, command run, API call, or approval gate.
2. For each consequential step, record:
   - Tool or action name.
   - Inputs passed (abbreviated to content, not raw payload).
   - Output or result received.
   - Evidence status: `pass`, `gap`, `fail`, or `not applicable`.
3. At decision points, record what the agent chose, what constraints were applied, and whether the decision was within authority.
4. Capture token use (prompt and completion counts) and latency per step where those are verification criteria.
5. Record every human approval gate: what was reviewed, by whom, and what decision was recorded.
6. Record errors and fallbacks: what failed, what recovery was attempted, and whether the fallback was within scope.
7. Link each trace row to the claim in `verification.md` that the evidence supports.
8. Summarize the execution posture: steps within scope, steps outside scope or uncertain, gaps requiring follow-up.

## Outputs

- Trace rows in `trace.md` or `verification.md`: step, action, inputs, outputs, evidence status.
- Decision-point records: choice made, constraint applied, authority check.
- Token use and latency summary when relevant.
- Approval gate records with reviewer, date, and decision.
- Execution posture summary linked to `ship.md`.

## Verification

- Every consequential step has a recorded outcome and evidence status.
- Each trace row is linked to at least one claim in `verification.md`.
- Decision points show what constraint or authority boundary applied.
- The execution posture summary is legible to a reviewer who was not present for the run.
- `python tools/ng.py validate <packet>` passes.

## Escalation

- Stop if execution records show tool calls or actions outside the authority scope in `basis.md`.
- Escalate when execution evidence reveals an unexpected side effect affecting data, credentials, or production state.
- Escalate when the trace gap prevents a release decision from being made with acceptable residual risk.

## Common Rationalizations

- "The output is correct, so the path does not matter." The path matters for debugging, auditing, cost, and authority compliance.
- "The chat log is the trace." Raw chat logs are not structured evidence; they cannot be validated or indexed.
- "We can reconstruct it later." Execution evidence degrades; capture at run time.
- "This is overhead." A trace row per consequential step is five fields; it is not a burden.

## Red Flags

- The packet claims agent execution was within scope but no step-level evidence exists.
- Token cost or latency anomalies are present but unexplained.
- Decision points are recorded as "agent chose X" without any constraint or authority reference.
- Human approval gates are asserted but not documented with reviewer and date.

## Source-lineage note

This skill is an original execution-evidence workflow for AI agents, influenced by W&B Weave trace-tree observability (span-per-call, auto-logging, audit lineage), the NVIDIA NeMo Agent Toolkit profiling model (token/latency/cost captured per step), and OpenTelemetry distributed tracing concepts (structured spans, parent-child relationships, reproducible records), all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. It does not create formal audit assurance, security certification, compliance, or regulatory adequacy. Execution trace evidence is scoped engineering record, not a formal audit trail.
