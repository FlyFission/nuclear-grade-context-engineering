---
name: reconsidering-the-approach
description: Challenges a chosen strategy by generating genuinely different ways to achieve the same outcome. Use for rethink, ideation, design alternatives, or architectural reconsideration at any stage. Do not use for factual checks or approval panels.
---

# Reconsidering the Approach

## Overview

An optional, bounded innovation overlay across Question, Discover, Specify, Plan, Execute, Verify, Review, Decide, Baseline, Operate and Learn. It asks whether we chose the right approach, not just whether we executed it correctly. Reuse Nuclear-grade evidence, change records, and decision rights rather than importing a second governance system.

## Decision contract

- **Claim checked:** a materially different way to achieve the accepted objective was examined, or its absence was justified.
- **Artifact observed:** current mission, source, constraints, approved basis and evidence -> a rethink note, linked to the existing packet when one exists.
- **Decision affected:** warn -- recommend CONTINUE, REFINE, REOPEN or ESCALATE the approach; never approve a controlled revision or release.
- **Failure class:** premature-convergence (overlooking a better mechanism or presenting simulated agreement as proof).
- **Next action:** return to the appropriate lifecycle stage or escalate a proposed change to its authorized owner.

## When to Use

- User invokes `/ng-rethink`, asks for a Wise Council, or wants competing solutions.
- A consequential design is costly to reverse, has no examined alternative, or encounters contradictory requirements.
- Several iterations failed, a material constraint changed, or a better mechanism may exist.

## When Not to Use

- For simple assumption/fact checking; use `questioning-attitude` or `checking-facts`.
- For independent review of a trust-bearing verdict; use `running-a-review-panel`.
- For mission drift alone; use `staying-on-mission`.
- For authority to change a baseline or ship; use `deciding-who-decides`, `declaring-intent` and release controls.
- During an active incident before containment; use `responding-to-incidents`.

## Inputs

- Current stage, goal, accepted success criteria, non-goals and constraints.
- Repository files, approved design/ADR, evidence, prior attempts and uncertainty.
- Requested depth (quick, standard, deep or creative), decision owner and allowed resources.

## Process

1. **Ground.** Inspect the actual source, current work type, risk mode and accepted basis. Name the problem, hard requirements and decision owner. Read-only reconsideration does not authorize file edits or external calls; use `using-nuclear-grade` to classify any subsequent mutation.
2. **Choose depth proportionately.** Quick takes three opposing lenses; Standard takes five (First Principles, Product/User, Systems/Operations, Contrarian/Inversion, Craft/Execution); Deep takes up to seven with a disagreement map and meta-audit; Creative generates **at least eight distinct mechanisms before any critique**. Use `references/council-protocol.md` for optional detail.
3. **Generate alternatives.** Include a no-change baseline and at least one substantially different mechanism. Use two or three relevant mental models (first principles, TRIZ, inversion, working backwards, Gall's Law or second-order thinking). Every candidate targets the *same* accepted outcome; a violated hard constraint cannot be compensated by scoring.
4. **Challenge.** Seek first-pass positions before cross-examination where feasible. Anonymize peer critiques if helpful, preserve the strongest dissent and a falsification test. Label FACT, INFERENCE, ASSUMPTION and UNKNOWN. Five personas inside one model are not independent reviewers; substantive external review follows `running-a-review-panel`.
5. **Compare.** State reversibility, dependencies, risks, operator impacts and cheapest discriminating experiment. Use numerical weights only where justified and sensitivity-tested. No prototype execution, outside model calls or paid experiments without the relevant permissions.
6. **Recommend.** Return exactly one disposition: CONTINUE (resume), REFINE (bounded editable draft), REOPEN (propose revisiting an approved basis), or ESCALATE (consequential unknown or authority required). Specify the lifecycle re-entry stage, accountable owner, observable kill/reversal criterion, and one artifact-producing next action.
7. **Preserve controls.** Never silently alter accepted requirements, ADRs, evidence gates, permissions or release stance. Route REOPEN/ESCALATE through `checking-what-a-change-affects`, `creating-change-records` and `deciding-who-decides` as applicable. Existing `learning-from-experience` handles outcomes; no competing ledger. Quick may remain conversational, while consequential reconsiderations can record a linked `rethink.md` without adding a mandatory packet field.

## Outputs

- Current decision, constraints, baseline and materially different alternatives.
- Source status, strongest opposing argument and what observation would change the recommendation.
- CONTINUE / REFINE / REOPEN / ESCALATE with owner, re-entry stage and next artifact.
- Optional draft ADR and reconsideration record; neither is an automatically approved design.

## Verification

- Alternatives vary the actual mechanism, address the same goal and honor hard constraints.
- Material dissent survives synthesis and factual claims are sourced or explicitly unverified.
- The decision owner, reversal signal, re-entry stage and artifact are named.
- The output reports real models, tests, tool use and degraded reviewers honestly.
- No accepted basis, authority, evidence gate or release state changed through council consensus.

## Escalation

- Refer approved-basis, authority, trust, regulated, safety-critical or irreversible changes to the designated human owner.
- Reclassify if a proposed option introduces a new boundary or consequence.
- Prefer a determinative test or primary source over speculative debate.
- If context is missing, identify the gap; never claim comprehensive repository review.

## Common Rationalizations

- "All five experts agreed." Five prompted personas are one model, not five independent checks.
- "A famous visionary would do it." Thinker lenses are methodological analogies, not endorsements.
- "The scores prove it." Unsupported numbers create false certainty.
- "This lets us change the approved specification." Recommendations are not approvals.
- "We must start over." Re-enter at the narrowest justified stage.

## Red Flags

- Creative options are criticized before adequate divergence.
- The chair erases dissent or invents evidence.
- External models, costly tests, or controlled changes happen without authorization.
- A panel is called independent solely because its seats have different names.

## Prompt

```text
Run /ng-rethink at quick | standard (default) | deep | creative depth.

Inputs:
- current stage, accepted outcome, hard constraints and decision owner:
- code / documents / approved ADR / source evidence:
- alternatives considered, uncertainties, reversibility and budget:

Read the real basis. Compare the no-change case with materially different solutions, using opposing perspectives. In Creative mode, produce at least eight distinct mechanisms before critique. Preserve minority dissent, unknowns, and actual reviewer independence.

Return:
- decision under challenge and alternative approaches
- strongest objection, lowest-cost discriminating test and measurable reversal signal
- CONTINUE, REFINE, REOPEN or ESCALATE, owner and lifecycle re-entry stage
- one artifact-producing next action

Do not alter approved baselines or authorize releases. Route consequential decisions through existing Nuclear-grade change control. Make no formal V&V, compliance, certification, safety or security guarantee.
```

## Source-lineage note

Original adaptation of first-principles analysis, inversion, systems thinking, TRIZ and deliberate adversarial ideation within the repository's existing governance. Named thinkers represent documented reasoning methods, not imagined endorsements. No regulatory adequacy or formal assurance is claimed.
