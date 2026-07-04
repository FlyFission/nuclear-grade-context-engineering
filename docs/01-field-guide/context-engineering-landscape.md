# The Context-Engineering Landscape (and where Nuclear-grade sits)

**Purpose:** Situate this repo inside the wider public field of "context engineering," credit the
practitioner collections it learns from, and state plainly which parts of that field Nuclear-grade
adopts, which it only points to as landscape, and which it deliberately declines. This keeps the
repo honest about its scope: it is not the whole field, and it does not pretend the rest does not
exist. No compliance claim is made.

---

## 1. The field's own framing

The public field has converged on a definition of context engineering as the deliberate assembly of
everything a model sees at inference — instructions, knowledge, tools, memory, state, and query —
optimized toward a task. Some surveys write it as an optimization: choose the context that maximizes
`Reward(LLM(context), target)`. The recurring thesis across the field is that **context failures,
not reasoning failures, are the new bottleneck** in agent systems.

Nuclear-grade agrees with the premise and specializes one layer of it. Most of the field optimizes
context for *capability* — better retrieval, longer windows, richer memory. This repo optimizes
context for *accountability*: which facts are load-bearing, who authored the evidence, what would
change the decision, and what must stay under control. The mechanics of a small, well-ordered window
are already ours ([`../02-operating-system/context-window-discipline.md`](../02-operating-system/context-window-discipline.md));
this page maps the neighboring territory we lean on rather than rebuild.

---

## 2. Adjacent territory — landscape, not adopted

These are real, useful bodies of technique. This repo stays **tool-agnostic**: it names them so an
adopter can go find them, and it does *not* take on any of them as a dependency.

| Area | The field's toolkit (landscape only) | How Nuclear-grade relates |
|---|---|---|
| Retrieval (RAG) | A taxonomy from naive retrieval through adaptive, corrective, and graph-based RAG. | We give retrieval *selection rules* (JIT retrieval, chunk by structure) in context-window-discipline; we do not ship or require a RAG stack. |
| Memory systems | Working / episodic / long-term / temporal-knowledge-graph layers; frameworks like Mem0, Zep, Letta. | Our [`durable-memory.md`](../02-operating-system/durable-memory.md) is the *discipline* (provenance, append-only, retrieve-by-relevance); the store can be any of these. |
| Agent interoperability | Emerging protocols — MCP, A2A, AG-UI — for exchanging context between agents and tools. | The repo already ships an MCP server; these protocols are the portable surface our tool-agnostic `.nuclear/` shape rides on, named as landscape here. |
| Construction techniques | Prompting/reasoning patterns (CoT, ReAct, PAL, reflexion). | Adopted as a *reference* mapped to PROVE — see [`../05-reference/reasoning-techniques.md`](../05-reference/reasoning-techniques.md). |
| Evaluation | LLM-as-judge, process-reward, observability (OpenTelemetry, tracing). | Adopted where it hardens our gates — see [`../02-operating-system/evaluation-integrity.md`](../02-operating-system/evaluation-integrity.md). |

The practitioner collections this repo reviewed for the map above — and now credits in the source
map — are dair-ai's Prompt Engineering Guide, Meirtz's Awesome-Context-Engineering survey,
muratcankoylan's Agent-Skills-for-Context-Engineering, NeoLabHQ's context-engineering-kit, and
jasontang-ai's Context-Engineering curriculum. See
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md) (Tier 11).

---

## 3. What this repo deliberately does not adopt

Declining is a decision, so it is recorded here rather than left silent.

- **Speculative "field physics" framing** — neural-field theory, attractor dynamics, quantum
  semantics, and similar metaphors that model context as a continuous resonating medium. They are
  intellectually interesting and appear in parts of the public curriculum material, but they are
  **not evidence-grounded operating guidance**, and importing them would put unfalsifiable language
  next to a repo whose entire posture is *claims stay inside their evidence*. That trade is a net
  loss for a method that asks agents to prove things. We decline it on purpose.
- **Framework-specific lock-in** — adopting a particular memory store, RAG library, or agent
  framework as *the* way. The field moves too fast and the repo's value is the portable discipline,
  not a stack. Named tools stay in the landscape column above, never in the required path.
- **Capability benchmarks as proof of the method** — success-rate tables from other projects are
  cited as illustrative external evidence, never restated as claims about Nuclear-grade (see the
  comparison study's standing honesty caveat).

---

## 4. Exit criteria

- An adopter can tell, for any context-engineering technique they hear about, whether this repo
  *owns* it, *points to* it, or *declines* it — and why.
- No named external framework has become a required dependency of the workflow.
- The declined material (§3) stays declined: new docs do not quietly import field-physics metaphors
  or restate other projects' benchmarks as our own.

## Source-lineage note

This page is an original Nuclear-grade field-orientation note. It draws on public context-engineering
collections and surveys — dair-ai's Prompt Engineering Guide, Meirtz's Awesome-Context-Engineering,
muratcankoylan's Agent-Skills-for-Context-Engineering, NeoLabHQ's context-engineering-kit, and
jasontang-ai's Context-Engineering — recorded in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). Those are
secondary/aggregator sources: this repo derives no template from them and claims no lineage to any
standard they cite. It does not create compliance, certification, or any assurance guarantee.
