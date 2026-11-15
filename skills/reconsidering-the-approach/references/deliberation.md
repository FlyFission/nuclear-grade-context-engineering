# Deliberation protocol: full Council, on explicit invocation only

## Separation of axes

**Mode** determines what the user needs: imagine, decide, challenge, design, build, audit. **Depth** determines effort: quick, standard, deep, creative. Creative is divergence-first regardless of mode. The caller chooses depth; do not silently escalate into Deep due solely to uncertainty.

**Functional lenses.** Five default seats:
1. First-Principles Architect (Feynman/Musk *methods*): eliminate requirements lacking physical, economic, or mathematical basis.
2. Product/Operator Visionary (Jobs/Ive *methods*): work backwards from end-user outcome; remove friction.
3. Systems/Reliability Pragmatist (Bezos/Rickover *methods*): invariants, dependencies, field operations, margins, failure modes.
4. Contrarian/Inversion Skeptic (Munger/Taleb *methods*): pre-mortem, second-order effects, incentives, tail risks, hidden alternatives.
5. Craft/Execution Engineer (Carmack/Torvalds *methods*): simple working core, interfaces, code review, realistic integration.

An optional sixth/seventh seat must cover a different failure mode (e.g. security, regulatory, evidence scientist, performance, accessibility, economics). Treat their positions as thought experiments, not real people consulted, endorsements, or substantiated quotations. Record the lens diversity axis and one opposing pair. If one model produces all opinions, label `SIMULATED_LENSES`; call them **not** independent reviews. For separately invoked authorized models, freeze and hash a shared neutral brief, isolate outputs until collected, log successful/failed/timed-out providers and actual model family where available. Use the existing `running-a-review-panel` for trust-bearing independent verdicts and custody.

## Depth contracts

| Depth | First pass | Challenge | Output |
|---|---|---|---|
| Quick | 3 opposing views, baseline and one different mechanism | strongest objection | disposition + smallest test |
| Standard | 5 distinct lenses, at least 3 mechanisms | three rounds + pre-mortem | alternative comparison, dissent, draft ADR when chosen |
| Deep | 5–7 unique failure axes | all Standard, explicit disagreement map and second synthesis meta-audit | sensitivity, conditional findings and decision owner |
| Creative | 5–7 lenses | **first** produce at least 8 structurally different ideas, **then** critique | clustered options, wildcard, 2–3 finalists and next experiment |

**Option quality:** distinct mechanism means different causal mechanism, algorithm, product interaction, organizational arrangement, physical constraint solution or system boundary—not renamed APIs or cosmetic features. Standard/Deep include minimalist/reversible, high-leverage, and structural-contrarian choices; include do-nothing/buy when relevant. If fewer than three are feasible, document each rejected mechanism and its violated hard constraint rather than fabricate options.

## Three mandatory Standard+ rounds

**Round 1: Independent initial positions (as far as the execution environment supports).** Each seat states thesis, recommended approach, strongest self-criticism, key proof, and one falsifying signal. Tag claims as OBSERVED (direct file/test), SOURCE (linked current authority), INFERRED (derived), ASSUMED (untested), UNKNOWN, or CONFLICTED. When only one model is available, record that its positions are *simulated* and must not be presented as blind, separate reviewers. Keep the first positions unchanged in an appendix or evidence packet when material.

**Round 2: Challenge across positions.** Mask identity/provider labels A/B/C where technically possible. Challenge a concrete assertion, not the seat's prestige. Each challenger records (a) strongest insight, (b) strongest flaw, (c) a **new falsifiable claim or concrete experiment**. Repeats are flagged as repeats, not invented novelty. Failed or missing reviewer outputs remain missing, not silent consensus.

**Round 3: Dispute and synthesis.** State which disagreements are factual (settled by retrieval/test), interpretive (settled by explicit priorities), and irreducible (owned risk). Map agreement, divergences, minority singleton, common blind spots, and what would reverse the recommendation. Steelman the strongest dissenter. Never count personas as independent votes or average incompatible approaches into a vague compromise. The synthesizer **only** integrates recorded positions; it may not invent a new argument as if another seat raised it.

**Standard+ pre-mortem:** assume failure after a realistic feedback horizon (default six months). Name at least 3 distinct mechanisms, root causes, earliest observable warnings, preventive controls, detecting tests, responsible owner and threshold to reopen. An unmeasurable threshold is marked `TO_DEFINE` with its owner, not fabricated.

**Deep meta-audit (separate pass):** inspect original positions against final verdict for suppressed dissent, misleading precision, violated gates, omitted stakeholder, unverified factual claims, correlation/shared source failures, missed alternative, and potential re-entry confusion. Record `PASS`, `REVISE` or `NO_DECISION`; if a critical issue survives, use `ESCALATE` with a specific missing piece of evidence.

## Reframing and stopping rules

Start from the accepted user outcome, not the council's preferred problem. If the reframing changes scope, present both and require owner agreement to revise objectives. Prefer 2–3 **selected** mental models: first principles, TRIZ contradiction resolution, working backwards, inversion, Gall's Law, systems dynamics, second-order effects, SCAMPER, Fermi estimation. State **how** each changed a candidate or test; name-only invocation is invalid.

Creative divergence rules: generate at least eight **different mechanisms before any criticisms or scores**, using two of SCAMPER, forced cross-domain analogy, constraint inversion, TRIZ or combining unrelated systems. Freeze the raw list. Cluster; retain one high-upside wildcard; advance a diverse set of finalists. Do not let the Contrarian dominate before divergence.

One revised design after initial critique is normally enough. Further rounds require new *empirical* evidence, not an incentive to argue forever. Stop deliberation when an authoritative source or deterministic test resolves the issue; if the economics of further evidence gathering are poor, state the bounded uncertainty and return to a reversible option.

## Mandatory recommendation record

- Outcome and baseline, hard requirements, permissions, cost/latency bounds and decision owner
- At least 3 competing mechanisms (or justified feasibility exception); creative eight-idea raw list first
- Lenses and actual independence/degradation
- Evidence source references; strongest dissent and falsifying observation
- Constraints gate, tradeoffs, pre-mortem and prospective kill/revisit criteria
- Analytical finding (`RECOMMENDED`, `CONDITIONAL`, `NO_DECISION`) and governed disposition (`CONTINUE`, `REFINE`, `REOPEN`, `ESCALATE`)
- Spec/plan artifact and named lifecycle stage for re-entry

Keep the conversational answer short; full initial positions can be saved in a linked optional `rethink.md` when the existing packet and authority permit.
