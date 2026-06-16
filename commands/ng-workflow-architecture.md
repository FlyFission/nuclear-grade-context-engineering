# ng-workflow-architecture

## Purpose

Force an agentic or multi-stage AI workflow to be designed as a bounded, staged, inspectable
system *before* any code or repo edits. Produce a workflow architecture — classification, stage
contracts, authority map, and the deterministic checks around the probabilistic steps — so a
human can review the scoping before build authority opens. This is a portable command prompt.

## Use when

- Planning a multi-step AI/agent workflow, agent workspace, orchestration system, or a repo
  convention that several agents or sessions will follow.
- Work will be delegated or fanned out, and each slice needs its own scoped context.
- A workflow stage is release-bearing and needs a gate the producing agent cannot edit.

## Do not use when

- A single-file or single-step change a person will run and review in one sitting.
- A read-only exploration with no side effects and nothing riding on a release.
- The user wants a formal guarantee, certification, or compliance sign-off. This prompt does
  not provide regulatory approval.

## Inputs

- The goal of the workflow in one line, and the deliverable it produces.
- The stages or steps you already expect, and which are deterministic vs model-mediated.
- The tools, credentials, data, and external services each stage would touch.
- The mission anchor and any existing repo conventions or known-good layout.

## Prompt text

```text
Design this agentic workflow architecture the Nuclear-grade way.

Inputs:
- workflow goal / deliverable:
- expected stages or steps:
- deterministic vs model-mediated steps:
- tools / credentials / data per step:
- mission anchor + existing conventions:

Return, in order:
1. Workflow classification (deterministic / bounded-agentic / human-gated /
   durable-orchestrated / exploratory) and why.
2. Stage decomposition (numbered stages, the order, the owner of each).
3. A stage contract per stage: Inputs by exact file#section (Layer-3 references vs
   Layer-4 prior outputs) + context budget, Process, Outputs, next-stage handoff.
4. Authority map: allowed vs forbidden tools, credential scope, do-not-touch paths.
5. Deterministic checks (scripts/tests/transforms that need no model).
6. Probabilistic steps, each with its determinism posture (model id, prompt,
   replayable vs human-judgment).
7. Replay / resume plan: what re-runs safely, what is a one-way action.
8. Observability plan: which runs are traced, and where the trace export is linked.
9. Eval plan for the model-mediated steps that matter.
10. Release / merge gates, each tied to an enforcement rung (1-3 advisory / 4
    out-of-band CI / 5 human review).
11. What must stay under configuration control (prompts, model ids, tools, artifacts).

Flag any stage whose gate the producing agent could defeat by editing it.
```

## Files created or modified

- `templates/standard/stage-contract.md` — copied per stage into the packet or workspace.
- `.nuclear/changes/<slug>/plan.md` — the build-sequence slices as stage contracts.
- A workflow workspace tree (numbered stage folders) when the design is built on disk.

## Expected outputs

- A workflow classification with a reason.
- A stage contract per stage: scoped inputs, process, outputs, and a handoff.
- An authority map and the deterministic-vs-probabilistic split.
- Release/merge gates tied to enforcement rungs, with any self-editable gate flagged.
- The list of items that must stay under configuration control.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Designing the happy path only, with no stop, escalate, or replay condition.
- Stage contracts that load whole documents instead of exact sections.
- A release-bearing gate the producing agent can edit (advisory dressed up as enforcement).
- Marketing folders as a replacement for a durable runtime when state, retries, or scale are real.
- Model-mediated steps with no determinism posture and no eval.

## Legal/assurance boundary note

This prompt structures a workflow for review; it does not create formal verification and
validation, compliance, certification, or any guarantee that a system is safe, secure, or fit
for regulated use.
