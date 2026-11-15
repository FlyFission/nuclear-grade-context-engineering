---
description: "Generates rigorously challenged alternative solutions and implementation decisions for uncertain or consequential choices."
disable-model-invocation: true
---

# ng-rethink

Portable command prompt generated from `skills/reconsidering-the-approach/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- Explicit `/ng-rethink`, Wise Council, architect's debate, creative invention, alternative designs or pre-mortem of the *approach*.
- A costly or hard-to-reverse choice requires creative options and a defensible discriminating experiment.
- The operator elects to investigate a substantive uncertainty surfaced during ordinary Nuclear-grade work.
- A current design appears stuck or contradictory and a different mechanism could satisfy the same accepted requirements.

## Do not use when

- For ordinary assumption or factual verification, use `questioning-attitude` or `checking-facts`.
- For independent proof of a trust-bearing verdict, use `running-a-review-panel`.
- For goal drift only, use `staying-on-mission`; for change-impact or owner authority use `checking-what-a-change-affects` and `deciding-who-decides`.
- For automatic blocking of a release or approval, use `checking-release-readiness`.
- For incident response or stopping agents, use `responding-to-incidents` or the separate SCRAM workflow.

## Inputs

- User-selected focus, task mode (`imagine`, `decide`, `challenge`, `design`, `build`, `audit`) and depth (`quick`, `standard`, `deep`, `creative`).
- Source paths, current stage and work type, accepted goal, non-goals, interfaces, hard constraints, approved basis and prior alternatives.
- Evidence and unknowns, decision owner, authorized tools/model access, cost/latency budget, prototype execution authority.

## Prompt text

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

## Verification

- Independent positions, masked critique, dissent and hard-constraint vetoes survive synthesis; no unverified claim is elevated to FACT.
- Standard/Deep offer three *different* mechanisms or a specific feasibility exception; Creative contains eight options **before** any grading.
- Comparisons disclose weights/sensitivity and measured-vs-proposed results; missing data is not silently scored.
- A real model, tool, or test is only named as used if it actually ran. A single model with five lenses is not independent review.
- ADR/plan do not override accepted requirements or bypass controls; next decision, owner, re-entry stage, and reversal signal are explicit.
- Evaluate usefulness against a simpler approach using `references/evaluation.md`; formal completeness is not proof of decision quality.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/reconsidering-the-approach/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
