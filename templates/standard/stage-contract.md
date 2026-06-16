# Standard Stage-Contract Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Turn one stage of an agentic workflow into an explicit, inspectable interface — its inputs, process, outputs, the gate that accepts it, and what is deterministic versus model-mediated — so a human can review the scoping *before* build authority opens, and a fan-out agent gets only the context its slice needs.

**Activation threshold:** Use when a Standard change is built as a multi-stage agent workflow, or when a `plan.md` build-sequence slice will be handed to another agent or session to run. One contract per stage or per delegable slice.

**Minimum useful version:** the stage identity and mode, the selective-section Inputs, the Process with allowed/forbidden tools, the Outputs with trace links, and the enforcement rung that accepts the stage.

**Overhead trap:** Do not write a contract for a single-file edit a person will run and review in one sitting. The contract earns its keep when context must be scoped for delegation, or when a stage is release-bearing. This is the full form of the stage contract; the worked-example `CONTEXT.md` (Inputs / Process / Outputs) is the minimal form of the same pattern — see `docs/02-operating-system/agentic-workflow-architecture.md`.

---

## Stage identity

- Stage name:
- Order (`NN`, sets sequence):
- Owner:
- Mode: deterministic / bounded-agentic / human-gated / exploratory
- Parent change packet: `.nuclear/changes/<slug>/`

## Inputs (selective section routing)

Point to exact sections, not whole documents. Separate the lasting rules the stage must
follow (Layer 3, references) from the per-run artifacts it consumes (Layer 4, prior outputs).
See `docs/02-operating-system/context-window-discipline.md`.

| Input | Layer (3 reference / 4 prior output) | Exact location (`file#section`) | Why this stage needs it |
|---|---|---|---|
| | | | |

- Context budget for this stage (token ceiling, not a whole-repo load):
- External tools or data sources required:

## Process

- Deterministic steps (scripts, tests, transforms — no model needed):
- Model-mediated steps (judgment, synthesis, drafting):
- Human approval point (what is shown, and what is decided):
- Allowed tools (read / edit / run / network / credential scope):
- Forbidden tools and do-not-touch paths:

## Outputs

| Output | Where it is written | Format | Next-stage consumer or disposition |
|---|---|---|---|
| | | | |

- Evidence produced (links into `verification.md` or `trace.md`):
- Trace links (run log / external trace export — link, do not copy; see `recording-what-an-agent-did`):

## Determinism posture

A disclosure of what can be reproduced, not a guarantee that a model step is repeatable.

- Model id, prompt reference, and (where applicable) temperature/seed for any model-mediated step:
- Replayable steps (same inputs reproduce the output):
- Non-replayable steps (marked as human judgment or external dependency):

## Verification

- Commands:
- Expected results:
- Failure condition (what makes this stage fail):
- Replay condition (when this stage must be re-run):

## Enforcement rung

Which mechanism accepts this stage's output, and whether the agent that produced it could
defeat that mechanism by editing it. See `docs/04-adoption/agent-authority-model.md` and
`docs/02-operating-system/runtime-enforcement.md`.

- Rung (1-3 advisory / 4 out-of-band CI / 5 branch protection or human review):
- Why this rung is sufficient for this stage's consequence:

## Stop / Escalate

- Stop if:
- Escalate if (and to whom):
- Reviewer:

## Required links

- `risk.md`
- `plan.md`
- `trace.md`
- Prior-stage contract or output, if this stage consumes one:

## Exit criteria

- A reviewer can see exactly what context the stage loads and what it must not touch.
- Every output names a next-stage consumer or a disposition.
- Deterministic work is separated from model-mediated judgment.
- The enforcement rung matches the stage's consequence.

## Source-lineage note

Original Nuclear-grade template. The stage-as-contract shape draws on the Model Workspace
Protocol (Van Clief and McDermott, arXiv:2603.16021): numbered stages, layered context, and
per-stage Inputs/Process/Outputs. The enforcement-rung and determinism fields are original
Nuclear-grade controls. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No
compliance claim is made.
