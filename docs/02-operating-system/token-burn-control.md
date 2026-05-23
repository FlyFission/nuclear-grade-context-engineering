# Token-Burn Control

**Purpose:** Keep Nuclear-grade usable for AI-assisted engineering by giving agents the smallest sufficient context to act safely and prove work.

**Thesis:** More rigor should reduce expensive iteration, not create prompt sludge. The packet is the context boundary.

---

## Context rule

Agents should read:

```text
role
current phase
selected mode
affected files/assets
packet summary
basis/protected outcomes
acceptance criteria
required proof
approval gates
source-map excerpt only if source lineage matters
```

Agents should not read:

```text
the entire repo
every source document
every brainstorming note
all standards foundation docs for a tiny change
old packets unrelated to current work
```

---

## Context budgets by mode

| Mode | Default context | Escalate only when |
|---|---|---|
| Quick | `risk.md`, `proof.md`, local diff, proof command. | A Standard trigger appears. |
| Standard | packet summary, `basis.md`, `plan.md`, affected files, `verification.md`, source-map excerpt if relevant. | Evidence/basis is disputed or high-consequence. |
| Nuclear | packet summary, activated Nuclear records, trace/evidence, relevant source-map/crosswalk excerpts. | SME/source review is needed. |
| Incident | incident record, logs/evidence excerpts, affected basis/tests/monitors. | Root cause or corrective action is uncertain. |
| Research Board | isolated research brief, source map, options matrix, decision record. | The decision becomes implementation work. |
| Release | `ship.md`, baseline, verification status, rollback, monitoring, handoff. | Release risk changes or evidence is stale. |

---

## Minimum useful context pack

A context pack for an agent should fit on one screen when possible:

```text
Change:
Mode:
Phase:
Do:
Do not:
Affected files:
Basis/protected outcomes:
Acceptance evidence:
Approval gate:
Known gaps:
Links:
```

If the context pack is long, the change is either too broad or needs a Research Board / Nuclear subset.

---

## Activation threshold

Use explicit context packs when:

- an AI agent will write files, run commands, call external APIs, or modify configuration;
- multiple agents/humans will hand off work;
- the packet has more than three active artifacts;
- evidence or approval gates are easy to miss;
- a long-running task must preserve state across sessions.

---

## Overhead trap

Do not ask an LLM to repeatedly reason over source documents to compensate for missing packet discipline. Summarize the source concept once in the packet, link the public URL, and use deterministic validators where possible.

---

## Required links

A context pack must link to:

- change packet path;
- selected mode and activation trigger;
- affected files/assets;
- proof commands/evidence destinations;
- approval gate or reviewer;
- source-map/crosswalk excerpts when source lineage is needed.

---

## Validator preference

Replace repeated LLM review with deterministic checks for:

- required activated artifacts;
- required sections;
- missing evidence status;
- broken relative links;
- prohibited compliance phrases;
- non-public citation patterns;
- unresolved TODOs in release packets;
- AI authority without independent proof.

---

## Source-lineage note

This document is an original operating discipline for AI-assisted software work. It is informed by public configuration-management, lifecycle, evidence, secure-development, and AI-risk sources in the source map, plus practical agent-workflow lessons captured in brainstorming. It does not use paywalled/proprietary standards as direct template lineage and makes no compliance claim.
