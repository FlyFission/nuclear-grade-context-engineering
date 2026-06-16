---
name: recording-what-an-agent-did
description: Captures an agent run's tool calls, decision points, inputs, outputs, token use, and approval steps as a clear, repeatable record linked into the packet trace and verification record. Use when how the agent got there matters for debugging, auditing, cost review, or defending a release decision. Do not use for a read-only run that changes nothing, or to produce a certified compliance audit trail.
---

# Recording What an Agent Did

## Overview

A "does it work" check proves what an agent produced, not how it got there. Sometimes how it got there matters: for debugging, for auditing, for reviewing cost, or for defending a release decision. This skill says what to record about the run, how much detail to capture, and how to link it into the packet's `trace.md` and `verification.md` as evidence someone else could reproduce.

## Decision contract

- **Claim checked:** every step that mattered -- tool call, edit, command, API call, approval -- has a recorded result and status, and each stayed inside the power `basis.md` granted.
- **Artifact observed:** the run log/transcript/trace export against `basis.md` and `plan.md` -> step-level trace rows, decision-point and approval records, and a token/delay summary in `trace.md`/`verification.md`, linked to `ship.md`.
- **Decision affected:** warn -- the step-level execution evidence the `ship.md` decision relies on.
- **Failure class:** unevidenced-run (a stayed-in-scope claim with no step-level evidence, or unexplained cost).
- **Next action:** record the gap for `ship.md`; a power breach or unexpected side effect escalates to pause/incident.

## When to Use

- An agent ran tool calls that matter (file writes, API calls, command runs) and the packet needs evidence you can check.
- A release decision turns on whether the agent followed the plan, the scope, and its power limits.
- Token use, delay (latency), or cost is one of the things you have to verify for this change.
- A reviewer or auditor needs to rebuild what the agent did without reading a raw chat log.
- A review after an incident, or an OPEX review (a lessons-from-operation review), needs repeatable evidence of how the agent behaved.

## When Not to Use

- The run was read-only exploring, with no real side effects and nothing riding on a release.
- The packet mode is Quick and the proof is one simple step that always gives the same answer.
- A full tracing platform already captures and exports this run data. Link to its output instead of copying it.

## Inputs

- The agent's run log, chat transcript, tool-call records, or trace export.
- `basis.md` (the scope the run was meant to stay in, the allowed actions, and the stop conditions).
- `plan.md` (the planned order of steps).
- Token use, delay, and cost data where they matter.
- Records of human approval steps.

## Process

1. Find the steps that matter and need trace evidence: any tool call, file edit, command run, API call, or approval step.
2. For each step that matters, record:
   - The tool or action name.
   - The inputs passed (just the content, not the full raw payload).
   - The output or result.
   - The evidence status: `pass`, `gap`, `fail`, or `not applicable`.
3. At decision points, record what the agent chose, what limits applied, and whether the choice was within its allowed power.
4. Capture token use (prompt and completion counts) and delay per step, where those are things you have to verify.
5. Record every human approval step: what was reviewed, by whom, and what was decided.
6. Record errors and fallbacks: what failed, what recovery was tried, and whether the fallback stayed in scope.
7. Link each trace row to the claim in `verification.md` that the evidence supports. When a tracing platform already holds the run, link to its export rather than copying it — an OpenAI trace, a LangSmith run, a Claude Code session log, a GitHub Actions run, a local command transcript, or an MCP/tool-call export — and record the link and its trace id in `trace.md`. The packet holds the link and the verified facts; the platform holds the raw spans.
8. Summarize how the run went: which steps stayed in scope, which went out of scope or are unclear, and which gaps need follow-up.

## Outputs

- Trace rows in `trace.md` or `verification.md`: step, action, inputs, outputs, evidence status.
- Decision-point records: the choice made, the limit applied, and the power check.
- A token-use and delay summary when it matters.
- Approval-step records with reviewer, date, and decision.
- A run summary linked to `ship.md`.

## Verification

- Every step that matters has a recorded result and an evidence status.
- Each trace row links to at least one claim in `verification.md`.
- Decision points show which limit or power boundary applied.
- The run summary is clear to a reviewer who was not there for the run.
- `python tools/ng.py validate .nuclear/changes/<slug>` passes.

## Escalation

- Stop if the records show tool calls or actions outside the allowed power in `basis.md`.
- Escalate when the evidence reveals an unexpected side effect on data, credentials, or production state.
- Escalate when a gap in the trace blocks a release decision you could otherwise make with acceptable leftover risk.

## Common Rationalizations

- "The output is correct, so the path does not matter." The path matters for debugging, auditing, cost, and staying inside the agent's power.
- "The chat log is the trace." Raw chat logs are not organized evidence. You cannot check or index them.
- "We can rebuild it later." Run evidence fades. Capture it while the run happens.
- "This is extra work." A trace row per step that matters is five fields. That is not a burden.

## Red Flags

- The packet says the agent stayed in scope, but there is no step-level evidence.
- Odd token cost or delay shows up but is never explained.
- Decision points are written as "agent chose X" with no limit or power reference.
- Human approval steps are claimed but not documented with reviewer and date.

## Prompt

```text
Trace this agent run and produce clear evidence.

Inputs:
- packet: .nuclear/changes/<slug>/
- execution source: <log / transcript / tool-call export>
- authority scope: <basis.md section or inline>
- token/latency data available: <yes/no>
- approval gates exercised: <list or none>

For each consequential step (tool call, file edit, command run, API call,
approval gate):
- Name the action and the tool.
- Record the inputs (shortened) and the output or result.
- Set an evidence status: pass, gap, fail, or not applicable.
- At decision points: record the choice made, the limit applied, and the authority check.
- For approval gates: the reviewer, the date, and the decision.

Return:
- trace rows for trace.md: step, action, inputs, outputs, evidence status.
- the decision-point records.
- a summary of token use and speed (if available).
- a run summary: steps within scope, steps uncertain, and gaps.
- a link from each trace row to the claim in verification.md it supports.
```

## Source-lineage note

This skill is an original run-evidence workflow for AI agents, influenced by W&B Weave trace-tree observability (span-per-call, auto-logging, audit lineage), the NVIDIA NeMo Agent Toolkit profiling model (token, latency, and cost captured per step), and OpenTelemetry distributed tracing concepts (structured spans, parent-child relationships, reproducible records), all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. It does not create formal audit assurance, security certification, compliance, or regulatory adequacy. A run trace is a focused engineering record, not a formal audit trail.
