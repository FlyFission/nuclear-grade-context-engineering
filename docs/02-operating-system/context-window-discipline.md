# Context-Window Discipline

**Purpose:** This file explains *why* the smallest honest context wins, names the ways an
agent's context window fails, and maps each failure to the Nuclear-grade control that already
answers it. It is the mechanics behind `context-packs.md` and `token-burn-control.md`.

**Status:** Operating doctrine grounded in public research. The findings cited here are the
source papers' claims on their benchmarks, not promises about your workload. No compliance
claim is made.

---

## 1. Core idea

A context window is a finite, degradable resource — not a bucket you fill.

Public research keeps converging on the same three facts:

- **Attention is a budget.** As input grows, a transformer's ability to use any one fact in
  it shrinks. Anthropic's engineering guidance calls this the *attention budget* and frames
  good context engineering as "the smallest possible set of high-signal tokens" that gets the
  task done ([Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
- **Recall decays with length even on easy tasks.** Chroma's *context rot* report measured
  models degrading on simple retrieval as input token count grows
  ([Context Rot](https://research.trychroma.com/context-rot)).
- **Position matters.** Models use information at the start and end of a long context far
  better than information buried in the middle
  ([Lost in the Middle, Liu et al.](https://arxiv.org/abs/2307.03172)).

Nuclear-grade already acts on this: the context pack is a deliberately small briefing, and
the packet — not the chat transcript — is the source of truth. This page is the reasoning a
reviewer can point to when someone asks why an agent was *not* given the whole repo.

---

## 2. Context lifetimes

Mixing information with different lifetimes is the quiet cause of most context failures.
Orchestration frameworks separate at least three lifetimes (see
[LangChain's context-engineering docs](https://docs.langchain.com/oss/python/langchain/context-engineering)):
fixed run configuration, mutable per-run state, and persistent cross-run memory.
Nuclear-grade has a native home for each:

| Lifetime | What lives there | Nuclear-grade home |
|---|---|---|
| Fixed for the run | Role, authority limits, forbidden actions, stop rules | Context pack header; `.nuclear/charter.md`; agent authority model |
| Working state for one change | Intermediate results, open gaps, the resume point | The packet: `.nuclear/changes/<slug>/` |
| Long-lived across changes | Approved baselines, lessons learned, deficiencies | `baselines`, OPEX records, the deficiency register |
| One model call | Whatever this step actually needs | The per-phase context pack selection |

Two leakage rules follow:

- **Run-scoped facts do not get promoted silently.** A scratchpad conclusion becomes durable
  only by being written into the packet with evidence, or into a lesson with a citation —
  never by surviving in a transcript.
- **Durable artifacts are not edited from inside a run as a side effect.** Charter and
  baseline changes go through their own packet.

The "long-lived across changes" row is the durable memory layer. How a later agent retrieves
that memory and keeps it from poisoning future runs is its own doctrine:
[`durable-memory.md`](durable-memory.md).

---

## 3. Named failure modes

Practitioners have converged on a short vocabulary for how context windows fail
([Breunig, How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html);
[Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents);
the [ACE paper](https://arxiv.org/abs/2510.04618)). Name the failure, and the existing
control that answers it becomes obvious:

| Failure mode | What it looks like | Nuclear-grade control |
|---|---|---|
| Context poisoning | A hallucinated or wrong "fact" lands in context early and gets re-cited as if verified. | Evidence status labels; "confidence is not a source"; the Observe step writes only *verified, cited* facts back to the packet. |
| Context distraction | History grows so long the agent fixates on its own transcript instead of the task. | Mission anchor in the context pack; compaction into the packet; "single next action" framing. |
| Context confusion | Too many tools or irrelevant documents in scope; the agent picks the wrong one. | Minimal authority: the pack lists what the agent may read, edit, and run — and what to ignore. |
| Context clash | Two sources in context contradict each other and the agent oscillates or loops. | Precedence is explicit (charter > pack > transcript); conflicts halt work and surface as a question, not a guess. |
| Context rot | Slow quality decay as tokens accumulate across turns. | Context budgets by mode; the packet, not the transcript, is the unit of truth; refresh the pack on phase change. |
| Context collapse | Iterative re-summarizing of a long-lived document erodes its detail until the useful content is gone. | Durable records grow by **appended, discrete entries** (lessons, deficiencies, decisions), never by wholesale rewrites. |
| Brevity bias | Compression keeps the fluent prose and drops the load-bearing specifics (commands, limits, exact wording). | Proof commands, authority boundaries, and boundary wording are linked or quoted exactly — never paraphrased to save tokens. |

*Context collapse* and *brevity bias* are the two named by the Agentic Context Engineering
(ACE) paper, which found that contexts maintained by **incremental delta updates** — small,
itemized additions and corrections — outperform contexts maintained by repeated full
rewrites ([arXiv 2510.04618](https://arxiv.org/abs/2510.04618)). That is the same shape as
this repo's lessons-learned discipline: append the entry, cite the evidence, leave the rest
of the record alone.

---

## 4. Placement and ordering

Because position affects recall (section 1), the order of a context pack is part of its
correctness:

- **Stable content first.** Role, charter excerpts, and authority limits lead. This also
  makes prompt caching effective, since the static prefix does not churn.
- **Hard constraints at the edges.** Forbidden actions and stop rules belong near the start
  or the end — never buried in the middle of retrieved material.
- **The next action last.** The pack schema already ends with `Next action:`; keep it there.
  The last thing the model reads should be the one thing it must do.
- **Retrieved evidence in the middle, trimmed.** The middle is the lowest-attention zone, so
  it gets the material that is supporting, not governing.

---

## 5. Compress with care

A summary is a claim like any other: it asserts "nothing load-bearing was dropped." Treat it
that way.

- Compression of redundant natural-language prose is well supported — the LLMLingua family
  reports up to ~20x compression with small accuracy loss on its benchmarks
  ([microsoft/LLMLingua](https://github.com/microsoft/LLMLingua)).
- Code and exact logic are far more loss-sensitive. Code-aware methods compress along
  function and block boundaries and report much lower safe ratios (~5.6x for
  [LongCodeZip](https://arxiv.org/abs/2510.00446)) than prose methods.
- Some things are never compressed, only linked or quoted exactly: proof commands, evidence
  links, authority limits, legal and boundary wording, and anything a validator checks.

When you compact a long thread into a packet, record what the compaction dropped ("details of
the abandoned approach are in the PR thread, not carried forward") so the loss is a decision,
not an accident.

---

## 6. Retrieving code by structure

When an agent must pull code into context, retrieval units should match the units developers
reason in:

- **Chunk by syntax, not by lines.** Splitting on fixed token windows slices functions in
  half; AST-based chunking (one function or class per retrieval unit) measurably improves
  retrieval and downstream generation ([cAST](https://arxiv.org/abs/2506.15655)).
- **Prefer just-in-time retrieval over pre-loading.** Loading "everything that might matter"
  spends the attention budget before work starts; fetching on demand keeps the working set
  small ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
- **Combine search modes.** Lexical search catches exact identifiers and stack traces that
  embeddings miss; semantic search catches concepts that grep misses. Use both before
  trusting either.

This repo stays tool-agnostic: these are selection rules for whoever builds the pack, not a
required indexing stack.

---

## 7. Multi-agent state hygiene

When more than one agent works a change:

- **Reads fan out; writes funnel in.** Any agent may read the shared packet, but one
  designated owner writes updates back. Parallel writers are how packets get corrupted and
  how context clash is manufactured.
- **Hand off by turnover, not by transcript.** The incoming agent gets a fresh context pack
  and restates objective, authority, required evidence, and stop criteria — it does not
  inherit a poisoned or rotted history.
- **Close the loop each cycle.** After a tool acts, extract the verified fact with its
  citation and write it to the packet; discard the raw output. The packet stays small and
  clean while the transcript is allowed to be messy and disposable.

---

## 8. Exit criteria

You are practicing context-window discipline when:

1. Every agent briefing names what to read **and what to ignore**.
2. Facts enter durable records only with evidence attached (no poisoning path).
3. Long-lived records grow by appended deltas, not rewrites (no collapse path).
4. Proof commands and boundary wording are never paraphrased (no brevity-bias path).
5. Constraints sit at the edges of the prompt and the next action sits last.
6. A handoff replaces the transcript instead of forwarding it.

---

## Source-lineage note

This page is an original Nuclear-grade operating doctrine. It draws on public
context-engineering sources — Anthropic's engineering guidance, LangChain's
context-engineering documentation, Neo4j's practical guide, Breunig's failure-mode taxonomy,
Chroma's context-rot report, and the Lost-in-the-Middle, ACE, LLMLingua, cAST, and
LongCodeZip papers — mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md)
(Tier 9). Benchmark numbers quoted here are those papers' claims on their benchmarks. This
page creates no compliance, certification, or fitness claim.
