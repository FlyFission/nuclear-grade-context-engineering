# ng-trace

## Purpose

Capture what an agent actually did during a run — its tool calls, decisions, inputs, outputs, token use, speed, and approval gates — and link it into the change record's `trace.md` and `verification.md` as clear, reviewable records. This is a portable command prompt.

## Use when

- An agent ran consequential tool calls and the change record needs evidence you can verify.
- A release decision depends on confirming the agent acted within its authority and its plan.
- Token use, speed, or cost is one of the things you must verify.
- A post-incident or lessons-from-operation (OPEX) review needs run records you can reproduce.

## Do not use when

- The run was read-only and had no consequential side effects.
- The change record is Quick mode and a single, repeatable proof check is enough.
- A dedicated observability platform (OTel, Weave, Phoenix) already exports structured traces; link to that output instead.

## Inputs

- The agent's run log, chat transcript, or tool-call records.
- `basis.md` (the intended scope and authority limits) and `plan.md` (the planned sequence).
- Token use, speed, and cost data, where they matter.
- The human approval-gate records.

## Prompt text

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

## Files created or modified

- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/execution-trace.md` (optional; use when the trace is large enough to need its own record)

## Expected outputs

- Structured trace rows: step, action, inputs, outputs, evidence status.
- Decision-point records with the limit applied and the authority referenced.
- A summary of token use and speed where it matters.
- A run summary, linked to `ship.md`.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Recording only the final output and skipping the steps in between.
- Treating raw chat history as a trace without structuring it.
- Missing the authority checks at decision points.
- Claiming an approval gate without a reviewer name or a date.

## Legal/assurance boundary note

Run-trace evidence produced with this portable command prompt is a scoped engineering record. It is not a formal audit trail, security certification, compliance record, or regulatory proof of how the agent behaved. It covers only the steps you captured; unlogged actions are not evidenced.
