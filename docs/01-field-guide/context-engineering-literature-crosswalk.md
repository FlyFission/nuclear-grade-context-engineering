# The context-engineering conversation — where Nuclear-grade sits

**Status:** Named background and peer-project map, as of 2026. **Not** an endorsement, an
affiliation claim, or a compliance claim.

**Purpose:** The phrase "context engineering" is now used by two very different bodies of work: a
research literature that formalizes and surveys it, and a practitioner movement that ships templates
for coding agents. Adopters arriving from either one ask the same question — *how does Nuclear-grade
relate?* This doc answers it against two widely referenced, **public** repositories:

1. **[Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering)** —
   a curated survey (with an accompanying arXiv paper) that treats context engineering as optimizing
   *"the complete information payload provided to an LLM at inference time,"* decomposed into
   **instructions, knowledge, tools, memory, state, and queries**, and organizes the literature on
   memory systems, retrieval, context scaling, compaction/caching, agent runtimes, and observability.
2. **[coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro)** —
   an MIT-licensed template built around the **PRP (Product Requirements Prompt)** loop: write an
   `INITIAL.md`, run `/generate-prp` to research the codebase and produce a complete implementation
   blueprint, then `/execute-prp` to build it against **validation gates** with self-correcting
   iteration. Backbone files: `CLAUDE.md` (global rules), `INITIAL.md`, `examples/`, `PRPs/`.

**Boundary (read first).** Both repositories are public and openly licensed, so — unlike the
paywalled PMI works in [`pmbok-pmi-ai-crosswalk.md`](pmbok-pmi-ai-crosswalk.md) — their ideas *can*
be named and cited directly, and both are recorded in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md) (Tier 9). This
page still claims **no** endorsement by, affiliation with, or superiority over either project. The
mappings are conceptual and deliberately coarse so a future revision of either repo does not falsify
them. Nuclear-grade is an **original, software-native, agent-authority workflow**; these two projects
are **complementary neighbors**, not upstream standards it implements.

> Use wording like: *Nuclear-grade sits alongside the context-engineering literature and the PRP
> template movement; it borrows their vocabulary and shares their premise, and adds an
> evidence-and-configuration spine neither centers.* Do **not** say *implements*, *is based on*, or
> *is endorsed by* either project.

---

## 1. The three projects occupy different points on one map

All three accept the same premise — that an agent's failures are usually **context failures**, not
raw model limits, so the payload is the thing to engineer. They differ in what they optimize:

| Project | Kind | Optimizes for | Where it is strong | Where it is thin |
|---|---|---|---|---|
| Awesome-Context-Engineering | Academic survey + taxonomy | Completeness and a shared vocabulary | Naming *what* a context is made of; memory/retrieval/scaling literature | It is a map, not a method — no per-change discipline or evidence gates |
| context-engineering-intro | Practitioner template | Getting a coding agent to one-shot a feature | A crisp, low-ceremony build loop; examples the agent emulates; gates in the spec | No configuration control, no independence between builder and evidence, no graded rigor |
| **Nuclear-grade** | **Governed workflow** | **Staying in control of what ships** | **Evidence↔claim discipline, graded rigor, actor-evidence independence, baselines, CM** | **Heavier on-ramp; less "taxonomy-complete" than the survey** |

The survey gives us *vocabulary*. The template gives us *ergonomics*. Our spine — evidence,
independence, baselines — is the part **neither** carries. Everything below is additive.

---

## 2. Awesome-Context-Engineering taxonomy ↔ Nuclear-grade surfaces

The survey decomposes a context payload into components. Nuclear-grade already produces or governs
each; naming them by the survey's terms sharpens our own docs. Names are paraphrase, not quotation.

| Survey component | Nuclear-grade surface that carries it | Repo location |
|---|---|---|
| **Instructions** (system prompt, rules, role) | The agent brief, charter authority, and per-task role/authority lines in a context pack | [`../../AGENTS.md`](../../AGENTS.md), `briefing-an-agent`, [`../02-operating-system/context-packs.md`](../02-operating-system/context-packs.md) §5 |
| **Knowledge** (docs, retrieved facts, source lineage) | Just-in-time source-lineage excerpts and required evidence, retrieved by relevance | [`../02-operating-system/context-window-discipline.md`](../02-operating-system/context-window-discipline.md) §6, `context-packs.md` §3 |
| **Tools** (callable actions and their schemas) | The commands/tools an agent may run and its authority envelope | `context-packs.md` §5, [`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md) |
| **Memory** (episodic/working, cross-run store) | Durable memory: baselines, OPEX, the deficiency register, retrieved across runs | [`../02-operating-system/durable-memory.md`](../02-operating-system/durable-memory.md) |
| **State** (packet phase, resume point, changed conditions) | The context-pack fields for phase, last action, and changed conditions | `context-packs.md` §3 |
| **Query** (the immediate task) | The objective, critical next action, and mission anchor | `context-packs.md` §3, `staying-on-mission` |

**What this buys us.** The survey's component list is a good completeness check for a context pack:
if a pack cannot say what fills each of the six slots, a slot is probably being left to chance. This
lens is now named in `context-packs.md` §1.

**Where the survey goes deeper than we do.** Its **memory** section (episodic vs. working memory,
graph-backed memory, production systems such as MemGPT/Letta) is a richer literature than our
`durable-memory.md` currently cites — which is exactly why that doc and the planned retrievable
memory store over `.nuclear/` (see [`../../ROADMAP.md`](../../ROADMAP.md)) point at it as the place
to look when we build retrievable cross-run memory for real.

---

## 3. context-engineering-intro's PRP loop ↔ Nuclear-grade's beats

The PRP workflow is a tight two-command loop. Mapped onto our beats, it is a lightweight slice of the
same lifecycle — with our evidence and independence discipline layered on top.

| PRP element | What it does | Nearest Nuclear-grade surface |
|---|---|---|
| `CLAUDE.md` (global rules) | Standing behavior for the agent | [`../../AGENTS.md`](../../AGENTS.md) + charter |
| `INITIAL.md` (feature request) | Human states the desired change | Question + Specify beats; `questioning-attitude`, `templates/standard/basis.md` |
| `/generate-prp` (research → blueprint) | Agent reads the codebase and writes a complete implementation plan | Discover + Plan beats; `ng-context-pack`, `templates/standard/plan.md`, `context-packs.md` |
| The PRP document itself | The self-contained blueprint the agent executes from | A Standard packet's `basis.md` + `plan.md` + context pack |
| `examples/` (patterns to emulate) | Concrete code the agent copies | Worked examples ([`../03-worked-examples/`](../03-worked-examples/)) — *documentation of the method*, not yet an agent-facing "emulate these" folder (a named gap; see §4) |
| Validation gates in the PRP | Runnable tests the agent must pass, with self-correction | Verify beat; `templates/standard/verification.md`, `proving-claims` |
| `/execute-prp` (build against gates) | Agent implements and iterates until gates pass | Execute + Verify beats |

**What this buys us.** PRP is a clean name for a pattern we already support but never packaged as one
move: *research the codebase, produce a complete blueprint, then execute it against gates.* That
pattern is now a first-class entry in the [`../../WORKFLOWS.md`](../../WORKFLOWS.md) catalog
("Blueprint and execute").

**What we add that PRP does not.** Three things, all load-bearing in high-consequence work:

- **Evidence custody and actor–evidence coupling.** In the PRP loop the same agent can write the
  blueprint, code, tests, and "gates passed" narrative. Nuclear-grade records who generated,
  selected, transformed, captured, retained, presented, reviewed, and authorized decisive evidence,
  then evaluates actor, context, mechanism, authority, and resource coupling against consequence.
  Different authorship can reduce one axis but does not by itself establish independence
  ([`../02-operating-system/actor-evidence-independence.md`](../02-operating-system/actor-evidence-independence.md)).
- **Graded rigor.** PRP applies one ceremony to every feature. Nuclear-grade scales from an
  administrative floor to Nuclear+ by consequence
  ([`../02-operating-system/risk-tiers-and-modes.md`](../02-operating-system/risk-tiers-and-modes.md)).
- **Baselines and configuration management.** A passed PRP has no notion of a saved, agreed
  approved version to drift from; ours does
  ([`../02-operating-system/configuration-management.md`](../02-operating-system/configuration-management.md)).

---

## 4. What we can still learn (open gaps)

Naming the neighbors surfaces work worth doing. These are recorded, not yet all done:

1. **First-class emulation examples.** coleam00's `examples/` are *patterns the agent copies*; our
   `docs/03-worked-examples/` are *documentation of the method*. A distinct, agent-facing "emulate
   these" convention is a real gap — captured here and a candidate for the roadmap.
2. **Production memory patterns.** The survey's memory literature (episodic/working, MemGPT/Letta,
   graph memory) is the reference set to draw on when `durable-memory.md` and the MCP server graduate
   from discipline to a retrievable store.
3. **A simpler on-ramp.** The PRP loop's `INITIAL.md` → two commands is radically approachable. Our
   lightest real path is Quick mode; an even simpler "start here" for first-time users would lower
   adoption friction without touching the spine.

---

## 5. What not to claim

Do not state or imply that Nuclear-grade:

- is endorsed by, affiliated with, or a fork of Awesome-Context-Engineering or
  context-engineering-intro;
- implements, is based on, or conforms to the survey's taxonomy or the PRP method as a standard;
- is superior to either project — they optimize for different goals (a complete map; a fast build
  loop) than Nuclear-grade does (staying in control of what ships).

This page is an original synthesis. It names two public projects to help adopters orient in a crowded
space. See [`../../DISCLAIMER.md`](../../DISCLAIMER.md) and
[`source-to-concept-crosswalk.md`](source-to-concept-crosswalk.md) for the repo's actual
(public-sourced) lineage.

---

## Source-lineage note

This crosswalk draws on two public, openly licensed repositories recorded in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md) (Tier 9):
the Awesome-Context-Engineering survey and the context-engineering-intro PRP template. It reproduces
no proprietary text and derives no template structure from either; it maps concepts to surfaces this
repo already has. No compliance claim is made.
