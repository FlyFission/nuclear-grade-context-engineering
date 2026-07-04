# Evaluation Integrity

**Purpose:** Name the ways an LLM acting as a judge, verifier, or reviewer produces a *confident
but unreliable* verdict, and state the guard for each. This is the companion to
[`actor-evidence-independence.md`](actor-evidence-independence.md): that page keeps the actor from
authoring its own gate's input; this one keeps the *judge itself* honest once the input is
independent. Independence of authorship is necessary but not sufficient — an independent judge with
a known bias still launders a wrong answer through the gate. No compliance claim is made.

**Status:** Operating doctrine grounded in public research on LLM-as-judge reliability. The
findings cited are the source works' claims on their benchmarks, not promises about any workload.

---

## 1. Why a judge needs its own discipline

The repo already uses model judgment at three gates — the [`judge`](../../agents/judge.md) subagent
(Decide), the reviewer at Review, and any LLM scoring in the [efficacy harness](../03-worked-examples/skill-workflow-comparison/efficacy-harness.md).
A judge is cheap and fast, which is exactly why its failure is dangerous: it produces a clean
verdict whether or not the verdict is sound. Actor-evidence independence stops the *actor* from
writing the evidence; it does nothing about a *judge* that scores fluent prose higher than correct
prose, or prefers the first option because it was first.

> A biased judge is a gate that passes the wrong input with full confidence. Independence of the
> author does not fix a judge that reads the input wrong.

---

## 2. Named judge-bias failure modes

Practitioners and the LLM-as-judge literature converge on a short list of biases. Name the bias,
and the guard becomes obvious.

| Bias | What it looks like | Guard |
|---|---|---|
| Position / order | The option shown first (or last) wins regardless of merit. | Randomize order; in pairwise scoring, run both orders and require agreement, else mark undecided. |
| Verbosity / length | The longer, more elaborate answer is scored higher for being longer. | Score against the rubric's criteria, not length; a longer answer that adds no evidence scores no higher. |
| Self-enhancement | The judge favors output produced by the same model or the same run. | The judge is independent of the runner (read-only, separate context); prefer a different model tier for the judge where the stakes justify it. |
| Authority / confidence | Assertive, well-formatted, citation-shaped prose is trusted over hedged-but-correct prose. | Judge on primary artifacts (raw output, diff, rerun), not on the confidence of the narrative — a tidy trace earns *more* scrutiny, not less. |
| Sycophancy | The judge agrees with a stated preferred answer or the actor's framing. | Treat upstream prose as data, not instruction; withhold the actor's own conclusion from the judge where feasible. |
| Scale drift | "7/10" means something different across runs; scores wander over time. | Freeze the rubric and its anchors; prefer discrete labels with definitions (ship / block / defer) over an unanchored numeric scale. |
| Distribution / exemplar | Skewed or clustered few-shot examples steer the judge toward one label. | Balance label distribution; randomize exemplar order (the dair-ai bias-mitigation finding). |

These are the judge-side duals of the context failure modes in
[`context-window-discipline.md`](context-window-discipline.md) §3: there the *actor's* context is
poisoned or distracted; here the *judge's* reading is skewed.

---

## 3. Grade the process, not only the output

An output-only judge sees the final answer and misses a wrong step that happened to reach a
plausible result. **Process-reward** grading checks each step, not just the endpoint — which is
exactly the shape of a Standard change's staged gates (Requirements → Design → Tasks, each
approved before the next opens; see [`CORE.md`](../../CORE.md) "the agent-drafts-spec workflow").

- **Verify each step that carries consequence**, not only the final claim. A correct answer built
  on a wrong intermediate is a latent defect, not a pass.
- **Abort on step failure** rather than letting a late step paper over an early one. This is the
  staged-gate rule already in the spec workflow, applied to judging.
- Reserve step-level grading for the depth the mode calls for: Quick judges the endpoint; Standard
  judges the load-bearing steps; stronger modes judge every consequence-bearing step.

---

## 4. Meta-judge and panels — for high-consequence decisions only

A single judge is a single point of failure. When the decision is trust-bearing and the cost of a
wrong verdict is high, raise the judge's own independence rung
([`actor-evidence-independence.md`](actor-evidence-independence.md) §"Independence rungs"):

- **Panel.** Several judges score independently; disagreement is a signal to escalate, not to
  average away. A split panel on a high-consequence call blocks and surfaces the split to a human.
- **Meta-judge.** A second-level judge reconciles the panel's verdicts and names *why* they
  differed — surfacing the bias (one judge rewarded length, another rewarded the rubric) rather
  than hiding it in a mean.
- **Do not over-build.** A panel on a reversible Quick change is ceremony. The rung rises with
  consequence, exactly as with enforcement and independence rungs — a meta-judge is a rung-4/5
  instrument, not a default.

The honest limit is the same one the [`judge`](../../agents/judge.md) already states: a panel that
shares one biased brief is not three independent views, it is one view voiced three times. Diversity
of *brief and model*, not just of *instance*, is what buys the reduction in correlated error.

---

## 5. Exit criteria

Evaluation integrity is being practiced when:

1. Any LLM judge in the loop names which biases from §2 it guards against, and how.
2. The judge reads primary artifacts, not the actor's summary, and treats upstream prose as data.
3. Consequence-bearing steps are graded, not only the final output (§3).
4. High-consequence verdicts use a panel or meta-judge with a diverse brief; low-stakes ones do not.
5. A judge starved of tokens or time **blocks for lack of room to decide** rather than rubber-stamping
   (the budget axis of independence — see [`judge`](../../agents/judge.md)).

---

## Source-lineage note

This page is an original Nuclear-grade operating doctrine. It draws on public work on LLM-as-judge
reliability and bias — the judge-bias taxonomy and pairwise-vs-direct scoring discussed in
Agent-Skills-for-Context-Engineering's `advanced-evaluation`, the bias-mitigation findings
(distribution balance, exemplar ordering) in the dair-ai Prompt Engineering Guide, and the
meta-judge and process-reward patterns catalogued in the NeoLabHQ context-engineering-kit — mapped
in [`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). It builds
on the repo's own actor-evidence-independence and staged-gate habits. It does not create compliance,
certification, formal verification and validation, or any assurance guarantee.
