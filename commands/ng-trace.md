# ng-trace

## Purpose

Capture execution evidence from an agent run — tool calls, decisions, inputs, outputs, token use, latency, and approval gates — and link it into the packet's `trace.md` and `verification.md` as structured, reviewable records. This is a portable command prompt.

## Use when

- An agent executed consequential tool calls and the packet needs verifiable execution evidence.
- A release decision depends on confirming the agent acted within its authority scope and plan.
- Token use, latency, or cost is a verification criterion.
- A post-incident or OPEX review requires reproducible execution records.

## Do not use when

- The execution was read-only with no consequential side effects.
- The packet mode is Quick and a single deterministic proof check is sufficient.
- A dedicated observability platform (OTel, Weave, Phoenix) already exports structured traces; cross-link that output instead.

## Inputs

- Agent execution log, chat transcript, or tool-call records.
- `basis.md` (intended execution scope and authority limits) and `plan.md` (planned sequence).
- Token use, latency, and cost data where relevant.
- Human approval gate records.

## Prompt text

```text
Trace the execution of this agent run and produce structured evidence.

Inputs:
- packet: .nuclear/changes/<slug>/
- execution source: <log / transcript / tool-call export>
- authority scope: <basis.md section or inline>
- token/latency data available: <yes/no>
- approval gates exercised: <list or none>

For each consequential step (tool call, file edit, command run, API call,
approval gate):
- Name the action and tool.
- Record inputs (abbreviated) and output or result.
- Assign evidence status: pass, gap, fail, or not applicable.
- At decision points: record choice, constraint applied, authority check.
- For approval gates: reviewer, date, decision.

Return:
- Trace rows for trace.md: step, action, inputs, outputs, evidence status.
- Decision-point records.
- Token use and latency summary (if available).
- Execution posture summary: steps within scope, steps uncertain, gaps.
- Links from each trace row to the claim in verification.md it supports.
```

## Files created or modified

- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/execution-trace.md` (optional; use when trace volume warrants a separate record)

## Expected outputs

- Structured trace rows: step, action, inputs, outputs, evidence status.
- Decision-point records with constraint and authority reference.
- Token use and latency summary where relevant.
- Execution posture summary linked to `ship.md`.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Recording only the final output and omitting intermediate steps.
- Treating raw chat history as a trace without structuring it.
- Missing decision-point authority checks.
- Asserting approval gates without a reviewer name or date.

## Legal/assurance boundary note

Execution trace evidence produced by this portable command prompt is scoped engineering record. It is not a formal audit trail, security certification, compliance record, or regulatory proof of agent behavior. Trace coverage is limited to the steps captured; unlogged actions are not evidenced.
