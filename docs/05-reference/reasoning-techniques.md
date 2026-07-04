# Reasoning & Prompting Techniques (mapped to PROVE)

**Purpose:** The rest of this repo is about *governance* — what a change must prove and who decides.
This page is the missing *construction* layer: the established, public prompting and reasoning
techniques an agent uses to actually produce good output, each placed where it fits in the PROVE
path and each carrying its evidence caveat. It is a reference, not doctrine — reach for a technique
because it changes the outcome, not because it is listed here. No compliance claim is made.

**Framing:** These techniques improve *how an answer is produced*. They do **not** substitute for
independent evidence. A cleverly-prompted answer is still the actor's narration until an independent
party reproduces it (see [`../02-operating-system/actor-evidence-independence.md`](../02-operating-system/actor-evidence-independence.md)).

---

## The catalog

| Technique | What it is | Where it fits in PROVE | Evidence caveat |
|---|---|---|---|
| Zero-shot | Ask directly, no examples. | Plan / Run — the default first try. | Fine for reversible drafting; not a basis for a trust-bearing claim. |
| Few-shot / in-context | Show a few worked examples to steer format and behavior. | Plan / Run — when output shape matters. | Skewed or clustered examples bias the result — balance and randomize (see judge distribution bias in [`evaluation-integrity.md`](../02-operating-system/evaluation-integrity.md)). |
| Chain-of-thought (CoT) | Ask for explicit intermediate steps. | Run — makes reasoning inspectable. | The stated steps are a *claim about* the reasoning, not proof the answer is right; verify the endpoint. |
| Self-consistency | Sample several reasoning paths, take the consensus answer. | Run / Observe — raises confidence on reasoning-heavy tasks. | Consensus of one model is not independence; correlated errors survive the vote. |
| Generated-knowledge | Have the model surface relevant facts before answering. | Discover / Plan — priming the working set. | Generated "facts" are unverified until cited — treat as hypotheses, not evidence (context-poisoning guard). |
| **ReAct** (reason + act) | Interleave reasoning with tool actions and read the results back in. | **Run / Observe** — the native shape of grounding a claim against real sources. | Grounds claims in tool output the reviewer can rerun — but only if the tool call and its raw result are captured, not paraphrased. |
| **PAL** (program-aided) | Offload quantitative, temporal, or logical steps to *executed code* instead of prose reasoning. | **Verify** — a deterministic, rerunnable check. | The strongest fit for this repo: a run of code is reproducible evidence (independence rung 3+), where model arithmetic is narration. See below. |
| Reflexion / self-refine | The agent critiques its own output and revises. | Run — cheap error reduction within a draft. | A self-refine loop is a **self-check** (independence rung 1–2), *not* an independent gate. Label it as one; it does not clear a trust-bearing claim. |
| LLM-as-judge | A model scores or decides on output. | Review / Verdict. | Subject to judge bias — must follow [`evaluation-integrity.md`](../02-operating-system/evaluation-integrity.md). |

---

## The two techniques that carry the most weight here

**PAL / program-aided reasoning strengthens `proving-claims`.** When a claim rests on arithmetic, a
date calculation, a count, a unit conversion, or any deterministic logic, do not trust the model's
in-prose answer — have it emit code and run it. The run is reproducible: an independent party reruns
the same input and reads the same output, which is independence rung 3 by construction, where "the
model said the total is 4,812" is rung 1. This is the concrete mechanism behind the
[`proving-claims`](../../skills/proving-claims/SKILL.md) rule that a load-bearing claim needs
reproducible evidence, applied to the class of claims models are *most* likely to get confidently
wrong.

**ReAct is how a claim gets grounded during Run.** An agent that reasons, calls a tool, and reads
the result back produces a trail of primary artifacts (the query, the raw result) rather than a
summary of them — which is exactly what the Review gate is supposed to read
([`actor-evidence-independence.md`](../02-operating-system/actor-evidence-independence.md), "read the
artifact, distrust the coherence"). The value is realized only if the raw tool output is captured
into the packet, not compressed into the narrative.

---

## What this page is not

- It is **not** a claim that any technique makes output correct, safe, or trustworthy. Each raises
  the odds of a good answer; none replaces the independent check the stakes call for.
- It is **not** exhaustive or a leaderboard. Model-specific tricks age fast; the durable content is
  the *mapping to PROVE and the evidence caveat*, not the technique roster.
- It adds **no** framework or vendor dependency. These are prompt-construction patterns, usable with
  any tool.

## Source-lineage note

This reference draws on the public prompting-technique taxonomy in the dair-ai Prompt Engineering
Guide (zero/few-shot, CoT, self-consistency, generated-knowledge, ReAct, PAL) and the reflexion /
self-refine pattern catalogued in the NeoLabHQ context-engineering-kit, mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). The mapping
to PROVE and the evidence caveats are original to this repo. It does not create compliance,
certification, or any assurance guarantee.
