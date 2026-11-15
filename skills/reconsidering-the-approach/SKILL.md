---
name: reconsidering-the-approach
description: Generates rigorously challenged alternative solutions and implementation decisions for uncertain or consequential choices. Use when the operator invokes ng-rethink, wants a visionary council, or requests creative architectural alternatives. Do not use for routine fact checks, normal coding, independent approval panels, or releases.
---

# Reconsidering the Approach

## Overview

An **opt-in** deep invention and decision-analysis capability across Question, Discover, Specify, Plan, Execute, Verify, Review, Decide, Baseline, Operate and Learn. It asks whether the chosen *mechanism* is right, not merely whether the current solution passes review. The normal Nuclear-grade path must **never automatically run a council**. When a consequential decision lacks sufficient input, the router may **offer once** to run `/ng-rethink`; a declined offer is not a defect or gate. All execution, evidence, release, incident and change authority stays with the existing Nuclear-grade system.

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

1. **Ground the actual decision.** Read applicable repo rules, files, live evidence and change packet. Separate what the user asked from a proposed reframing; never silently replace the objective. Name baseline, hard constraints, stakeholders, reversibility, uncertainty, and decision owner. Read-only council work is allowed within existing authority; classification still precedes any mutation or external effect.
2. **Choose mode and depth independently.** Default Standard, five functional lenses. Quick (three lenses) only for low-stakes reversible choices; Deep (up to seven) for major contested decisions; Creative (five to seven) requires **at least eight structurally distinct options before critique**. Do not force Deep into a trivial decision. Read `references/deliberation.md` when selected, and `references/lenses.md` for domain-specific/custom casting. Historical thinkers are **documented methodological lenses**, not impersonations; cast custom names on request. The five default seats are First Principles, Product/Operator, Systems/Reliability, Contrarian/Inversion, and Craftsman/Executor.
3. **Diverge and establish alternatives.** Select 2–3 relevant models using `references/mental-models.md` when needed (e.g. TRIZ, first principles, working backwards, Gall's Law, inversion, system feedback). Explain how each changed the candidate set. Standard and Deep propose **at least three materially different mechanisms** (minimal/reversible, ambitious/leverage, contrarian/structural) plus no-change when feasible. Creative produces eight ideas first and then clusters them, retaining one wildcard. Every option states assumptions, interfaces, hard constraints, time/cost *estimates labeled as such*, worst failure, and cheapest disconfirming test.
4. **Deliberate in three rounds.** Round 1 records each seat's initial thesis, objection to its own thesis, claims marked FACT/SOURCE, INFERENCE, ASSUMPTION or UNKNOWN and a falsifiable test. Round 2 uses anonymized or identity-masked challenges: strongest insight, strongest flaw, and **one new testable correction**. Round 3 cross-examines disputed assumptions and maps consensus, real divergences, singletons and blind spots; the chair may synthesize but **cannot invent votes or positions**. One model simulating seats remains one model. For a genuinely independent consequential review route to `running-a-review-panel`, not an imaginary multi-agent result.
5. **Stress-test and compare.** Standard+ conducts a six-month pre-mortem (or realistic feedback horizon): root cause, early indicator, mitigation, test, and observable kill/revisit trigger. Hard constraints are gates, not weighted preferences. For weighted tradeoffs, state preselected criteria, data basis, scoring directions and sensitivity; unknown or missing results remain unknown. Read `references/decision-and-prototypes.md` for detailed controls. No unjustified numerical confidence, majority-vote truth, or unsupported costs.
6. **Prototype competition, conditionally.** For valuable resolvable uncertainty, propose two or more isolated competing implementations against **pre-frozen, equivalent fixtures, acceptance gates and budgets**. When permitted, evaluate *actually measured* results including repeatability and variability; if not, output only a test plan. Do not claim benchmark execution from a prompt. The optional stdlib `scripts/compare_prototypes.py` ranks **provided evidence data**, never runs code or grants approval.
7. **Deep meta-audit.** In Deep mode separately inspect the synthesis for lost dissent, common-mode reasoning, missing stakeholder, invented facts, overlooked vetoes, baseline drift, and false precision. Unresolved critical uncertainty yields `NO_DECISION` for the analytic finding and an **ESCALATE** disposition to the accountable owner, not a manufactured winner. Preserve distinct model-family count and degraded reviews when applicable.
8. **Deliver a build-ready handoff without bypassing authority.** When the recommendation is actionable, create a **draft ADR** covering decision, rejected alternatives, evidence, invariants, interfaces, security/privacy, migration/rollback, minority dissent, and reversal criteria. Provide a sequenced implementation plan with exact modules, schemas/contracts, tests, integration checkpoints and evidence needed for a verdict. Route into existing Specify/Plan/Execute controls; implement code only after the user's implementation instruction and existing authority checks. See `references/engineering-handoff.md`.
9. **Disposition and return.** Choose CONTINUE, REFINE, REOPEN or ESCALATE. Name owner, exact re-entry stage, success/kill signal with observation window, single artifact-producing next step, and unresolved evidence. Do not update accepted ADRs, permissions, test gates, baseline or ship stance based on council opinion. Prefer a short decision first; full positions, evidence, and disagreement map can live in an optional existing-packet `rethink.md`. Existing `learning-from-experience` owns outcomes.

## Outputs

- Verified question/basis and a competing-mechanism option map (Creative raw eight first).
- Deliberation record with model/provenance disclosure, strongest dissent, evidence states and critical unknowns.
- Constraint-gated comparison, pre-mortem, disconfirming experiment, uncertainty/sensitivity, and kill/revisit criteria.
- One advisory disposition, accountable owner, re-entry stage, optional draft ADR and exact implementation handoff.
- If authorized to build, changed files, executed tests, verified scope, rollback and open gaps. Never call generated code production-ready without proof.

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
