# Context Packs

**Purpose:** This file defines the focused context bundles that let people and AI agents work from the right evidence, without rereading the whole repo or every source document.

**Status:** Design spec. Context packs are aids for getting work done, not compliance records.

---

## 1. Core idea

A context pack is a small bundle built for one task:

```text
role + mode + packet state + loaded instruction files + affected files + required evidence + approval gates + HPI controls + relevant source lineage
```

It exists because Nuclear-grade is a way to control the raw power of an AI or LLM. Powerful agents should not get endless context and vague authority. They should get a focused packet, clear limits, and a duty to prove their work.

The research grounding — why small, ordered context outperforms big context, and the named ways a context window fails — is in [`context-window-discipline.md`](context-window-discipline.md).

### What a context pack is made of

The public context-engineering literature decomposes a context payload into six components
(instructions, knowledge, tools, memory, state, and query — see the survey named in
[`../01-field-guide/context-engineering-literature-crosswalk.md`](../01-field-guide/context-engineering-literature-crosswalk.md)).
A context pack carries all six, so the list doubles as a completeness check: if a pack cannot say
what fills a slot, that slot is being left to chance.

| Component | Where it lives in the pack (§3 schema) |
|---|---|
| Instructions | Role, mission anchor, charter articles, forbidden actions |
| Knowledge | Basis summary, required evidence, source-lineage excerpts |
| Tools | The commands/tools and authority in §5 |
| Memory | Baselines, OPEX, and open deficiencies pulled in via [`durable-memory.md`](durable-memory.md) |
| State | Current phase, last completed action, changed conditions |
| Query | Objective and critical next action |

This is a lens on the schema below, not a new format. The pack stays one focused bundle.

---

## 2. Activation threshold

Create or refresh a context pack when:

- an AI agent will change code, docs, tests, prompts, dependencies, infrastructure, release records, or examples;
- a human reviewer needs a one-screen summary of a Standard or larger packet;
- the work changes mode, scope, risk, dependency trust, or release readiness;
- an incident or handoff needs to stop the same unsafe retry from happening again;
- a long, token-heavy research thread has to be boiled down into a single decision record.

**Minimum useful version:** a short Markdown section or file with the mode, the objective, the affected files, the open risks, the acceptance evidence, the approval gates, and the forbidden actions.

**Overhead trap:** pasting the whole source map, all the brainstorming docs, every template, and every standard excerpt into every agent prompt.

---

## 3. Context pack schema

Use this structure before adding tooling:

```text
# Context Pack: <change slug>

Mode: Quick / Standard / Nuclear / Incident / Research Board / Release
Role: builder / reviewer / verifier / releaser / incident lead / researcher
Packet: .nuclear/changes/<slug>/
Objective: <one paragraph>
Mission anchor: <objective, success criteria, non-goals; survives context resets>
Charter: <.nuclear/charter.md articles in play>
Affected files: <paths>
Current phase: Question / Specify / Plan / Execute / Verify / Review / Decide / Baseline / Operate / Learn
Last completed action: <resume point>
Changed conditions: <what changed since the prior agent/context>
Risk summary: <top risks and escalation triggers>
Basis summary: <what must remain true>
Critical next action: <action, likely error, control>
Required evidence: <commands, reviews, evals, links>
Approval gates: <who/what must approve before next step>
Loaded instruction files: <AGENTS.md / CLAUDE.md / .github/copilot-instructions.md / tool rules in force, with precedence or "none known">
Source-lineage excerpts: <only the relevant source-map/crosswalk links>
Forbidden actions: <scope and authority limits>
Do-not-touch targets: <files, commands, systems, claims>
Incoming confirmation: <owner restates objective, authority, proof, and stop criteria>
Open gaps: <what is unknown or blocked>
Next action: <single next move>
```

---

## 4. Context budgets by mode

| Mode | Default context | Do not include unless activated |
|---|---|---|
| Quick | `risk.md`, `proof.md`, local diff, proof command | Full source foundation, long design docs, unrelated templates |
| Standard | packet summary, `basis.md`, `verification.md`, `ship.md`, affected files, relevant source-map rows | All brainstorming docs, unrelated source families, Nuclear-mode extensions |
| Nuclear | full packet, activated extensions, source-map excerpts, trace/evidence status, independent review scope | Entire standards corpus or unrelated historical research |
| Incident | incident record, failing evidence, recent changes, rollback/mitigation state, OPEX targets | New feature design debates unless needed for correction |
| Research Board | research question, candidate sources, options matrix, decision criteria, distillation target | Operational packet noise not needed for decision |
| Release | release baseline, evidence status, unresolved risks, rollback, monitoring, handoff | Implementation chatter already superseded by evidence |

---

## 5. AI-agent authority boundaries

Every AI-facing context pack should state:

- what files the agent may read;
- what files the agent may edit;
- what commands it may run;
- which persistent instruction files or tool rules are in force, and which one wins on conflict;
- whether it may use the network or look things up online;
- what approvals it needs before it changes anything;
- what claims it must not make;
- what evidence it must produce before it says it is done;
- whether a self-check or a turnover record is required before it goes on.

For agents that hold tools, include a stop rule:

> If the requested action goes past the context pack's authority, stop. Record the approval you need, or the path to escalate, instead of making something up.

For handoffs, include a closed-loop rule:

> When the stakes call for a turnover, the incoming owner restates the objective, the authority, the required evidence, and the stop criteria before acting.

---

## 6. Required links

Each context pack should link to:

- its change packet under `.nuclear/changes/<slug>/`;
- mode rules in `docs/02-operating-system/modes.md`;
- activation rules in `docs/02-operating-system/activation-thresholds.md`;
- relevant template files;
- relevant `source-map.md` and `source-to-concept-crosswalk.md` rows only when source lineage affects the decision;
- validation results or explicit validator gaps when available.

---

## 7. Exit criteria

A context pack is ready when a competent human or AI agent can answer:

1. What am I allowed to do?
2. What must remain true?
3. What evidence proves the next decision?
4. What must not be claimed?
5. What should I read now, and what should I ignore?
6. What is the next action?
7. What changed since the prior owner or context?
8. Which standing agent instructions are in force, and do any conflict with this pack?
9. What critical action needs self-checking or turnover?

Archive or refresh a context pack when it goes stale, when the mode changes, or when the packet's risk or evidence state changes.

---

## 8. Source-lineage note

This context-pack practice is an original way of working. It draws on public sources about keeping the approved version of everything under control, software assurance, secure development, systems engineering, and lessons learned, mapped in `source-map.md` and `source-to-concept-crosswalk.md`.

It is not a formal compliance record and does not claim to implement any outside standard or framework.
