---
name: reconsidering-the-approach
description: Generates rigorously challenged alternative solutions and implementation decisions for uncertain or consequential choices. Use when the operator invokes ng-rethink, wants a visionary council, or requests creative architectural alternatives. Do not use for routine fact checks, normal coding, independent approval panels, or releases.
---

# Reconsidering the Approach

## Overview

An **opt-in** invention and decision-analysis capability callable at any lifecycle stage. Challenge the selected mechanism, not merely implementation quality. The normal workflow **never automatically runs the council**; it may **offer once** on consequential uncertainty, without creating a gate. Existing Nuclear-grade execution, evidence and approval controls remain authoritative.

## Decision contract

- **Claim checked:** genuinely different mechanisms have been considered against the same accepted outcome, with assumptions, disconfirming evidence and decision owner identified.
- **Artifact observed:** the actual mission, frozen requirements/ADR, code, evidence and prior attempts -> optional linked `rethink.md`, candidate comparison, and draft ADR when warranted.
- **Decision affected:** warn -- recommend CONTINUE, REFINE, REOPEN or ESCALATE the *approach*, never approve a controlled revision, change of authority, or release.
- **Failure class:** premature-convergence (missing an effective alternative, theatrical consensus, unsupported confidence, or a council changing accepted scope).
- **Next action:** resume at a named lifecycle stage or submit the proposed decision/impact to the existing owner and control path.

## When to Use

- Explicit `/ng-rethink`, Wise Council, architect's debate, creative invention, alternative designs or pre-mortem of the *approach*.
- A costly or hard-to-reverse choice requires creative options and a defensible discriminating experiment.
- The operator elects to investigate a substantive uncertainty surfaced during ordinary Nuclear-grade work.
- A current design appears stuck or contradictory and a different mechanism could satisfy the same accepted requirements.

## When Not to Use

- For ordinary assumption or factual verification, use `questioning-attitude` or `checking-facts`.
- For independent proof of a trust-bearing verdict, use `running-a-review-panel`.
- For goal drift only, use `staying-on-mission`; for change-impact or owner authority use `checking-what-a-change-affects` and `deciding-who-decides`.
- For automatic blocking of a release or approval, use `checking-release-readiness`.
- For incident response or stopping agents, use `responding-to-incidents` or the separate SCRAM workflow.

## Inputs

- User-selected focus, task mode (`imagine`, `decide`, `challenge`, `design`, `build`, `audit`) and depth (`quick`, `standard`, `deep`, `creative`).
- Source paths, current stage and work type, accepted goal, non-goals, interfaces, hard constraints, approved basis and prior alternatives.
- Evidence and unknowns, decision owner, authorized tools/model access, cost/latency budget, prototype execution authority.

## Process

1. **Ground.** Inspect repo rules, files, evidence, approved basis and prior attempts. Distinguish accepted outcome from proposed reframing. Record hard constraints, reversibility, uncertainty and decision owner. Classify before any mutation or external effect.
2. **Cast and route.** Choose task mode independently from depth. Standard uses five seats (First Principles, Product/Operator, Systems/Reliability, Contrarian/Inversion, Craftsman/Executor); Quick three, Deep up to seven. Creative requires **at least eight structurally distinct options before any critique**. Historical thinkers are methodological lenses, not participants. Use `references/deliberation.md` and optional `references/lenses.md`.
3. **Invent mechanisms.** Select 2–3 models from `references/mental-models.md` and explain what each changes. Standard/Deep develop **at least three materially different mechanisms** (minimal, high-leverage, contrarian) plus no-change where feasible. Creative freezes eight raw ideas before clustering and retains a wildcard. Record assumptions, constraints, estimated costs, failure and falsifying test.
4. **Debate in three rounds.** First positions: thesis, strongest self-objection, evidence tags (FACT/SOURCE, INFERENCE, ASSUMPTION, UNKNOWN), test. Identity-masked peer challenge: strongest insight/flaw plus **new falsifiable correction**. Synthesis: contested assumptions, agreement, divergence, minority dissent and blind spots. Never invent votes; one model simulating seats is not independent. For independent consequential verdicts use `running-a-review-panel`.
5. **Pre-mortem and compare.** Standard+ uses a six-month or context-appropriate failure horizon, root causes, indicators, mitigations and measurable revisit triggers. Hard constraints are vetoes. Predeclare weights where defensible, analyze sensitivity, and keep missing metrics UNKNOWN. See `references/decision-and-prototypes.md`.
6. **Prototype tournament if justified.** Pre-freeze equal fixtures, correctness/security gates, budget and method. Compare **actual** repeated measurements; otherwise provide only a proposed test. `scripts/compare_prototypes.py` analyzes supplied data, never executes candidates or approves changes.
7. **Deep meta-audit.** Check for erased dissent, common-mode errors, omitted stakeholders, unsupported confidence and ignored vetoes. Unresolved critical issues produce `NO_DECISION` and an **ESCALATE** recommendation with the missing evidence.
8. **Handoff.** Draft ADR: selected/rejected options, invariants, interfaces, security/privacy, migration and rollback, dissent, proof and kill criteria. Ordered plan: exact inspected modules, schemas, tests, edge cases and checkpoints. Route through existing Specify/Plan/Execute controls. Build only when authorized; see `references/engineering-handoff.md`.
9. **Re-enter.** Recommend CONTINUE, REFINE, REOPEN or ESCALATE; name owner, lifecycle stage, evidence threshold and one next artifact. **Do not update accepted** ADRs, permissions, gates, baselines or releases by council consensus. Retain full positions in optional `rethink.md` when material; outcomes go through `learning-from-experience`.

## Outputs

- Verified question/basis and a competing-mechanism option map (Creative raw eight first).
- Deliberation record with model/provenance disclosure, strongest dissent, evidence states and critical unknowns.
- Constraint-gated comparison, pre-mortem, disconfirming experiment, uncertainty/sensitivity, and kill/revisit criteria.
- One advisory disposition, accountable owner, re-entry stage, optional draft ADR and exact implementation handoff.
- For authorized builds, report changed files, actual tests, rollback and gaps. No unsupported production-ready claims.

## Verification

- Independent positions, masked critique, dissent and hard-constraint vetoes survive synthesis; no unverified claim is elevated to FACT.
- Standard/Deep offer three *different* mechanisms or a specific feasibility exception; Creative contains eight options **before** any grading.
- Comparisons disclose weights/sensitivity and measured-vs-proposed results; missing data is not silently scored.
- A real model, tool, or test is only named as used if it actually ran. A single model with five lenses is not independent review.
- ADR/plan do not override accepted requirements or bypass controls; next decision, owner, re-entry stage, and reversal signal are explicit.
- Evaluate usefulness against a simpler approach using `references/evaluation.md`; formal completeness is not proof of decision quality.

## Escalation

- Escalate controlled-basis changes, security/agent authority, regulatory claims and irreversible effects to the human decision owner.
- Reclassify when an alternative adds scope, new tools/models or trust boundaries. An exploratory council grants no new execution power.
- If authoritative data/tests decide the issue, stop debate and use them. For live incidents, contain harm first.
- If input is insufficient, state `NO_DECISION` and the discriminating evidence rather than inventing certainty. No obligation to use a council when the offer is declined.

## Common Rationalizations

- "The five experts agree." One-model personas are not independent observers.
- "The council found a better approach so I'll rewrite the accepted spec." Recommendation is not approval.
- "An 8.9 score settles it." Missing evidence or hard constraints cannot be washed out by ranking.
- "We should always run Deep to be careful." Scope consequence, evidence value and budget govern depth.
- "The prototype won." Not until frozen, reproducible evidence exists and the owner accepts the decision.

## Red Flags

- Creative brainstorming is criticized before eight structurally different ideas exist.
- The synthesizer erases minority views, invents claims, or attributes fictional quotes to real people.
- An outside model call, cost, code mutation or release occurs without authority.
- A comparison omits failed candidates or reports fictional tests.
- The default workflow begins automatically invoking the council, or repeatedly pesters an operator who declined.

## Prompt

```text
Run /ng-rethink for this decision. Mode: imagine | decide | challenge | design | build | audit.
Depth: quick | standard (default) | deep | creative.

Ground in actual files, requirements, accepted basis and evidence. Cast complementary visionary,
systems, contrarian and engineering lenses using documented reasoning frameworks. Compare at
least three materially different mechanisms (Creative: eight raw ideas BEFORE critique).
Run three rounds: initial positions, identity-masked challenge, synthesis preserving dissent.
Use pre-mortem, hard-constraint gates, discriminating tests and measurable reversal criteria.
Deep: map disagreement and independently meta-audit the synthesis.
When justified, define fair competing-prototype benchmarks; claim measured results only if run.
Produce a draft ADR, exact file/interface/test plan for technical decisions; build only when
authorized by the user and the existing Nuclear-grade process.

Return the recommendation, strongest objection, decisive evidence or missing fact,
CONTINUE/REFINE/REOPEN/ESCALATE with owner and lifecycle re-entry stage, and one concrete
artifact-producing action. Do not change accepted baselines or release authority by consensus.
No formal verification, security, certification, nuclear compliance or safety claim.
```

## Source-lineage note

Original synthesis of first principles, TRIZ, inversion, systems dynamics, working backwards, adversarial design councils and engineering prototyping; informed by the user's earlier Wise Council v2.1 research package. Historical thinker references denote methods, never personal participation or endorsement. The Nuclear-grade framework provides evidence visibility, not formal nuclear compliance, certification or assurance.
