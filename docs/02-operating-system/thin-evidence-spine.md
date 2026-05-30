# Thin Evidence Spine

**Purpose:** This file defines the smallest useful set of records. It turns fast, AI-driven software work into engineering evidence a reviewer can check, without building a process binder.

**Thesis:** Nuclear-grade is a way to control the power of cutting-edge AI software work. The thin evidence spine runs that power through the design basis, controlled versions, a trace from claim to proof, verification, and release readiness. It keeps the context small enough for people and agents to actually use.

---

## 1. The spine

```text
Quick mode
  risk.md
  proof.md

Standard mode
  risk.md
  basis.md
  plan.md
  trace.md
  verification.md
  ship.md
```

The spine is incomplete on purpose, compared with a full quality system. It captures the fewest decisions and pieces of evidence a reviewer needs to answer:

1. What changed?
2. Why is this the right level of rigor?
3. What must stay true?
4. What evidence proves the important claims?
5. Is the change ready to ship, defer, or block?

The spine is not meant to slow every draft edit. It slows acceptance: the point where a draft becomes a claim, a controlled item, a baseline, a release decision, or a public statement.

---

## 2. Activation threshold

Use the thin spine when a change needs more than a commit message but does not call for the full Nuclear packet.

| Mode | Activate when | Minimum records |
|---|---|---|
| Quick | Local, easy to undo, low stakes, easy to verify, no new trust boundary. | `risk.md`, `proof.md` |
| Standard | Behavior users can see, an important dependency, a data, security, or permission change, a long-lived design decision, or model, prompt, or tool behavior that has real effect. | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md` |
| Nuclear subset | Failure is severe, silent, hard to undo, trusted by outsiders, close to regulated work, or the agent acts on its own in a big way. | Start with Standard, then add only the Nuclear records you turn on. |

If you cannot answer the evidence question in a few linked records, move up a mode instead of stretching the thin spine.

---

## 3. Minimum useful version

A minimum useful packet is one a doubting reviewer can move through quickly.

| Record | Minimum useful content | Review question |
|---|---|---|
| `risk.md` | Scope, affected items, how bad failure is, how easy to undo, how easy to spot, exposure, uncertainty, chosen mode, proof required. | Did we choose the right rigor? |
| `proof.md` | For Quick mode: command, check, or eval, plus the result, an evidence link, and a reviewer note. | Is the change we called low-risk actually proven? |
| `basis.md` | Mission, outcomes to protect, outcomes you cannot accept, assumptions, limits, dependency and AI trust decisions, evidence needs. | What must stay true? |
| `plan.md` | Build order, affected files and assets, non-goals, review checkpoints, rollback approach, proof commands. | How will we build this without losing scope or rollback thinking? |
| `trace.md` | Important claim, then basis, then control or design feature, then evidence, then ship posture. | Can reviewers move from claim to proof quickly? |
| `verification.md` | Claims, methods, verification type, commands, evals, or reviews, acceptance criteria, results, gaps. | Does the proof match the claims? |
| `ship.md` | Baseline, evidence status, leftover risks, rollback, monitoring, handoff, release decision. | Should this ship now? |

The verification type matters:

| Type | Use for |
|---|---|
| self-check | the target of a critical action and the result you expect |
| peer-check | another person or agent stops a likely wrong action before it happens |
| concurrent verification | someone watches a high-stakes action while it happens |
| independent verification | a separate person, agent, or deterministic tool checks the final state or evidence |
| peer review | the quality of the work, whether claims fit, how easy it is to maintain, and the boundary wording |
| deterministic test / eval | evidence of behavior you can reproduce |

---

## 4. Overhead trap

Do not turn the spine into a full packet in disguise.

Avoid:

- copying source-map text into every template;
- writing long stories where a link and a status field would do;
- filling Standard records for a change that is clearly Quick;
- claiming that test coverage proves unrelated safety, security, or reliability claims;
- letting AI-written documentation run ahead of independent evidence;
- letting the same agent's confident claim stand in for independent verification when the stakes demand separation;
- slowing exploration you can undo when only the acceptance gates need stronger evidence.

Use links, status labels, and clearly marked gaps instead.

---

## 5. Required links

Every packet should link to the relevant:

- change slug, PR, or issue;
- affected files, configs, prompts, models, dependencies, evals, docs, or release artifacts;
- the source or basis record when a claim depends on it;
- the verification command, CI run, eval report, review, screenshot or log, or a named evidence gap;
- the rollback or restore path and the monitoring signal when the change is release-facing;
- what the AI touched and the independent check, when the AI had real authority.

---

## 6. Exit criteria

A thin-spine packet is complete when:

1. the chosen mode is justified;
2. each turned-on record exists and answers a decision question;
3. every important claim has evidence, a clearly marked gap, or a deferral made on purpose;
4. the release status is clear: ship, do not ship, or ship with named leftover risk;
5. the packet is small enough to hand an agent as context without loading the whole repo.

---

## 7. Source-lineage note

This evidence spine is an original Git-based workflow. It draws on public sources about keeping the approved version of everything under control, designing for safety, software assurance, secure development, AI risk, the supply chain, and high-reliability software, mapped in:

- `../00-standards-foundation/source-map.md`
- `../../01-field-guide/source-to-concept-crosswalk.md`
- `change-control-packets.md`
- `activation-thresholds.md`

It is not a compliance framework and does not claim conformity with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.

---

## 8. Public v0 follow-ups

- Keep the v0 checker focused on the structure of Quick and Standard packets, evidence status, source-lineage notes, local links, and language that claims too much.
- Add richer checks for turned-on Nuclear, Incident, and Release records after the Quick and Standard path has proven useful.
- Prove the larger C-002 and C-003 chains in the `ai-agent-tool-permissions` worked example before adding heavier Nuclear-mode templates.
