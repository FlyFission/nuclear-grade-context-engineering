# Context Packs

**Purpose:** Define the focused context bundles that let humans and AI agents work from the right evidence without rereading the whole repo or every source document.

**Status:** Design spec. Context packs are operating aids, not compliance records.

---

## 1. Core idea

A context pack is a small, task-specific bundle:

```text
role + mode + packet state + affected files + required evidence + approval gates + HPI controls + relevant source lineage
```

It exists because Nuclear-grade is a control system for AI/LLM horsepower. Powerful agents should not receive unlimited context and ambiguous authority. They should receive a focused packet, clear constraints, and evidence obligations.

---

## 2. Activation threshold

Create or refresh a context pack when:

- an AI agent will modify code, docs, tests, prompts, dependencies, infrastructure, release records, or examples;
- a human reviewer needs a one-screen summary of a Standard+ packet;
- work changes mode, scope, risk, dependency trust, or release readiness;
- an incident/handoff needs to prevent repeated unsafe retries;
- a token-heavy research thread must be distilled into an operational decision record.

**Minimum useful version:** a short Markdown section or file with mode, objective, affected files, open risks, acceptance evidence, approval gates, and forbidden actions.

**Overhead trap:** pasting the entire source map, all brainstorming docs, every template, and every standard excerpt into every agent prompt.

---

## 3. Context pack schema

Use this structure before adding tooling:

```text
# Context Pack: <change slug>

Mode: Quick / Standard / Nuclear / Incident / Research Board / Release
Role: builder / reviewer / verifier / releaser / incident lead / researcher
Packet: .nuclear/changes/<slug>/
Objective: <one paragraph>
Affected files: <paths>
Current phase: Question / Specify / Plan / Execute / Verify / Review / Decide / Baseline / Operate / Learn
Last completed action: <resume point>
Changed conditions: <what changed since the prior agent/context>
Risk summary: <top risks and escalation triggers>
Basis summary: <what must remain true>
Critical next action: <action, likely error, control>
Required evidence: <commands, reviews, evals, links>
Approval gates: <who/what must approve before next step>
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
- whether network/source lookup is allowed;
- what approvals are required before side effects;
- what claims it must not make;
- what evidence it must produce before declaring completion;
- whether a self-check or turnover record is required before continuing.

For tool-bearing agents, include a denial rule:

> If the requested action exceeds the context pack’s authority, stop and record the needed approval or escalation path instead of improvising.

For handoffs, include a closed-loop rule:

> The incoming owner restates objective, authority, required evidence, and stop criteria before acting when consequence warrants turnover.

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
8. What critical action needs self-checking or turnover?

A context pack should be archived or refreshed when it becomes stale, when mode changes, or when the packet’s risk/evidence state changes.

---

## 8. Source-lineage note

This context-pack discipline is an original software operating pattern inspired by public configuration-management, software assurance, secure development, systems engineering, and lessons-learned sources mapped in `source-map.md` and `source-to-concept-crosswalk.md`.

It is not a formal compliance record and does not claim implementation of any external standard or framework.
