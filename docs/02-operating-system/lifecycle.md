# Lifecycle

**Purpose:** Define the Nuclear-grade operating spine for AI-accelerated software changes.

**Core thesis:** Nuclear-grade is questioning attitude plus configuration management for AI-assisted software work: it channels LLM horsepower through assumption checks, specification, controlled items, traceability, verification, review, release decisions, baselines, and operating learning without token/process waste.

**Lifecycle spine:**

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

This is an operating model, not a compliance program. `Classify` remains inside `risk.md`: selected mode, escalation triggers, evidence obligation, and hold conditions.

---

## Phase map

| Phase | Decision being made | Minimum useful output | Exit criteria |
|---|---|---|---|
| Question | What assumptions, doubts, and stop conditions must be surfaced before work continues? | Decision question, assumptions, warning signs, evidence gaps. | Confidence is grounded in facts, not vibes. |
| Discover | What sources and repo facts matter? | Public sources, prior packets, constraints, known gaps. | Specification is grounded, not invented. |
| Specify | What state or behavior is required? | Requirements, claims, protected outcomes, assumptions, acceptance criteria. | Claims are testable or gap-labeled. |
| Plan | How will controlled configuration change? | Steps, affected items, rollback, proof commands. | Work can proceed without rediscovering scope. |
| Execute | Did implementation stay inside authority? | Diffs, commits, generated artifacts, AI-assist notes. | Deviations are recorded, not hidden drift. |
| Verify | What evidence supports the claims? | Tests/evals/reviews/results with status and gaps. | Evidence matches the claim. |
| Review | Can a skeptical reviewer accept this? | Claim-to-evidence review and residual risk disposition. | Accept/defer/block is reviewable. |
| Decide | Should the change proceed, ship, block, defer, or continue with residual risk? | Decision, conditions, owner, baseline trigger. | Release decision is explicit. |
| Baseline | What accepted state is now controlled? | Commit/release/artifact plus controlled item state and triggers. | Future drift can be detected. |
| Operate | What signals show drift or failure? | Monitors, support signals, incident triggers. | Operators know what to watch. |
| Learn | What updates next time? | OPEX note linked to basis/test/control/template/baseline update. | Lesson changes something or is closed. |

---

## Activation threshold

Use the full lifecycle for any Standard, Nuclear, Incident, Research Board, Release, or activated CM change. Quick changes may compress the lifecycle into `risk.md` + `proof.md`, but still answer the relevant phases in one or two lines.

Escalate beyond Quick when the change affects:

- user-visible behavior;
- data handling, auth, permissions, or network access;
- AI model/prompt/tool authority;
- external dependencies, APIs, packages, SaaS, build services, or data sources;
- release posture, rollback, monitoring, or operational handoff;
- durable architecture or hard-to-reverse configuration.

---

## Minimum useful version

For a small Standard change, the lifecycle is useful when the packet answers:

```text
What should we question? What facts did we discover? What are we specifying? What changed? What proves it? What decision was made? What baseline now controls it?
```

If the answer takes more than one screen before implementation starts, summarize it and link deeper evidence only where needed.

---

## Overhead trap

Do not turn the lifecycle into seven separate meetings or seven giant documents. The packet scales; the repo does not. If a phase adds no decision value for a low-consequence change, compress it rather than inventing ceremony.

---

## Required links

Every lifecycle record should link backward and forward:

- `questioning-attitude.md` links assumptions, uncertainty, stop conditions, and evidence gaps.
- `risk.md` links to selected mode and escalation triggers.
- `basis.md` or `spec.md` links to activated source-map concepts when relevant.
- `plan.md` links to specification, affected files, dependencies, and rollback.
- `verification.md` links to claims/acceptance criteria and results.
- `decision.md` or `ship.md` links evidence, unresolved risks, rollback, monitoring, handoff, and baseline trigger.
- `baseline.md` links to accepted controlled state after review and decision.
- `learn`/OPEX notes link to changed requirements, tests, monitors, or controls.

---

## Source-lineage note

Original software workflow inspired by public high-consequence engineering and software assurance sources, especially [DOE-HDBK-1028-2009](https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009) for questioning attitude, [DOE-STD-1073-2016](https://www.energy.gov/ehss/articles/doe-std-1073-2016), [DOE-STD-1189-2016](https://www.energy.gov/ehss/articles/doe-std-1189-2016), [DOE-STD-3024-2011](https://www.energy.gov/ehss/articles/doe-std-3024-2011), NRC software RG 1.168-1.173 source family listed in `../00-standards-foundation/source-map.md`, [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [NASA Software Engineering Handbook](https://swehb.nasa.gov/), and [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/nasa-systems-engineering-handbook/).

No compliance claim is made or implied.
