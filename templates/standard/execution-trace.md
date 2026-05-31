# Execution Trace Record

**Purpose:** Capture clear evidence from an agent run — tool calls, decisions, inputs, outputs, token use, latency, and approval gates — for verification and release review.

**Activation threshold:** Use when an agent ran tool calls that matter, and the packet needs step-by-step evidence to back the release decision.

**Minimum useful version:** the steps that matter, each with its action, inputs, outputs, and evidence status; the decision-point records; and the stance summary.

---

## Execution context

- Slug:
- Agent role:
- Authority scope (basis.md reference):
- Execution date:
- Owner:
- Trace source: `<log / transcript / tool-call export>`

## Trace rows

| Step | Action / tool | Inputs (abbreviated) | Output / result | Evidence status | Claim supported |
|---|---|---|---|---|---|
| 1 | | | | pass / gap / fail / N/A | `verification.md` REQ-XXX |

Evidence status legend: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Decision-point records

| Step | Decision made | Constraint applied | Authority check | Notes |
|---|---|---|---|---|
| | | | within scope / outside scope / uncertain | |

## Token use and latency summary

Use when token cost or latency is one of the things you check.

| Phase | Prompt tokens | Completion tokens | Latency (s) | Notes |
|---|---|---|---|---|
| Total | | | | |

## Approval gate records

| Gate | What was reviewed | Reviewer | Date | Decision |
|---|---|---|---|---|
| | | | | approved / blocked / deferred |

## Errors and fallbacks

| Step | Error encountered | Recovery attempted | Within scope? |
|---|---|---|---|
| | | | yes / no / uncertain |

## Execution posture summary

- Steps within scope:
- Steps outside scope or uncertain:
- Evidence gaps:
- Residual risk for release decision:

## Required links

- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every step that matters has an evidence status.
- The decision points point back to the limits on the agent's power.
- The approval gates have a reviewer, a date, and a decision.
- The stance summary makes sense to a reviewer who was not there for the run.

## Source-lineage note

Original Nuclear-grade template influenced by public ideas from W&B Weave trace-tree observability, the NVIDIA NeMo Agent Toolkit profiling model, and OpenTelemetry distributed tracing, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. An execution trace is a scoped engineering record. No formal audit assurance, security certification, compliance, or regulatory adequacy claim is made.
