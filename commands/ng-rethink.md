---
description: "Challenges a chosen strategy by generating genuinely different ways to achieve the same outcome."
disable-model-invocation: true
---

# ng-rethink

Portable command prompt generated from `skills/reconsidering-the-approach/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- User invokes `/ng-rethink`, asks for a Wise Council, or wants competing solutions.
- A consequential design is costly to reverse, has no examined alternative, or encounters contradictory requirements.
- Several iterations failed, a material constraint changed, or a better mechanism may exist.

## Do not use when

- For simple assumption/fact checking; use `questioning-attitude` or `checking-facts`.
- For independent review of a trust-bearing verdict; use `running-a-review-panel`.
- For mission drift alone; use `staying-on-mission`.
- For authority to change a baseline or ship; use `deciding-who-decides`, `declaring-intent` and release controls.
- During an active incident before containment; use `responding-to-incidents`.

## Inputs

- Current stage, goal, accepted success criteria, non-goals and constraints.
- Repository files, approved design/ADR, evidence, prior attempts and uncertainty.
- Requested depth (quick, standard, deep or creative), decision owner and allowed resources.

## Prompt text

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

## Verification

- Alternatives vary the actual mechanism, address the same goal and honor hard constraints.
- Material dissent survives synthesis and factual claims are sourced or explicitly unverified.
- The decision owner, reversal signal, re-entry stage and artifact are named.
- The output reports real models, tests, tool use and degraded reviewers honestly.
- No accepted basis, authority, evidence gate or release state changed through council consensus.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/reconsidering-the-approach/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
