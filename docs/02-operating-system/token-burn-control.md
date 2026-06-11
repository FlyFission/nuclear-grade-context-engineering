# Token-Burn Control

**Purpose:** This file keeps Nuclear-grade usable for AI-assisted engineering. It gives agents the smallest context they need to act safely and prove their work.

**Thesis:** More rigor should cut down on costly back-and-forth, not pile up prompt clutter. The packet is the line that bounds the context.

This is not just cost control: model recall measurably degrades as context grows, so the smallest honest context is also the most reliable one. The evidence and the failure-mode names are in [`context-window-discipline.md`](context-window-discipline.md).

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

If the context pack is long, the change is either too broad or needs a Research Board or Nuclear subset.

---

## Activation threshold

Use explicit context packs when:

- an AI agent will write files, run commands, call outside APIs, or change configuration;
- more than one agent or person will hand off work;
- the packet has more than three active records;
- evidence or approval gates are easy to miss;
- a long-running task has to keep its state across sessions.

---

## Overhead trap

Do not ask an LLM to reason over source documents again and again to make up for a sloppy packet. Sum up the source idea once in the packet, link the public URL, and use deterministic checks where you can.

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

- the records that should be turned on;
- required sections;
- missing evidence status;
- broken local links;
- compliance phrases that are not allowed;
- citations that point to non-public sources;
- leftover TODOs in release packets;
- AI authority with no independent proof behind it.

---

## Source-lineage note

This document is an original way of working for AI-assisted software work. It draws on public sources about keeping the approved version of everything under control, the lifecycle, evidence, secure development, and AI risk in the source map, plus practical agent-workflow lessons captured in brainstorming. It does not use paid or private standards as direct template lineage, and it makes no compliance claim.
