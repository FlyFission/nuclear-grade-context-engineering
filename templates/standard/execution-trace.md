# Execution Trace Record

**Purpose:** Capture structured execution evidence from an agent run — tool calls, decisions, inputs, outputs, token use, latency, and approval gates — for verification and release review.

**Activation threshold:** Use when an agent executed consequential tool calls and the packet needs step-level evidence to support the release decision.

**Minimum useful version:** Consequential steps with action, inputs, outputs, and evidence status; decision-point records; posture summary.

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

Use when token cost or latency is a verification criterion.

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

- Every consequential step has an evidence status.
- Decision points reference the authority boundary.
- Approval gates have reviewer, date, and decision.
- Execution posture summary is legible to a reviewer who was not present for the run.

## Source-lineage note

Original Nuclear-grade template influenced by W&B Weave trace-tree observability, NVIDIA NeMo Agent Toolkit profiling model, and OpenTelemetry distributed tracing concepts, all mapped as supporting context in `docs/00-standards-foundation/source-map.md`. Execution trace evidence is scoped engineering record. No formal audit assurance, security certification, compliance, or regulatory adequacy claim is made.
