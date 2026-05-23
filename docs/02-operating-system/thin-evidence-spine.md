# Thin Evidence Spine

**Purpose:** Define the smallest useful set of records that turns AI-accelerated software work into reviewable engineering evidence without creating a process binder.

**Thesis:** Nuclear-grade is a control system for frontier AI software engineering. The thin evidence spine channels horsepower through design basis, configuration discipline, traceability, verification, and release readiness while keeping context small enough for humans and agents to use.

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

The spine is intentionally incomplete compared with a full quality system. It captures the minimum decisions and evidence needed for a reviewer to answer:

1. What changed?
2. Why is this the right rigor level?
3. What must remain true?
4. What evidence proves the important claims?
5. Is the change ready to ship, defer, or block?

---

## 2. Activation threshold

Use the thin spine when a change needs more than a commit message but does not justify the full Nuclear packet.

| Mode | Activate when | Minimum records |
|---|---|---|
| Quick | Local, reversible, low-consequence, easy to verify, no new trust boundary. | `risk.md`, `proof.md` |
| Standard | User-visible behavior, important dependency, data/security/permission change, durable design decision, model/prompt/tool behavior with material effect. | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md` |
| Nuclear subset | Failure is severe, silent, hard to reverse, externally trusted, regulated-adjacent, or agent/autonomy authority is high. | Start with Standard, then add only activated Nuclear records. |

Escalate instead of stretching the thin spine if the evidence question cannot be answered in a few linked records.

---

## 3. Minimum useful version

A minimum useful packet is one a skeptical reviewer can navigate quickly.

| Record | Minimum useful content | Review question |
|---|---|---|
| `risk.md` | Scope, affected items, consequence, reversibility, detectability, exposure, uncertainty, selected mode, proof required. | Did we choose the right rigor? |
| `proof.md` | For Quick mode: command/check/eval, result, evidence link, reviewer note. | Is the claimed low-risk change actually proven? |
| `basis.md` | Mission, protected outcomes, unacceptable outcomes, assumptions, constraints, dependency/AI trust decisions, evidence needs. | What must remain true? |
| `plan.md` | Build sequence, affected files/assets, non-goals, review checkpoints, rollback approach, proof commands. | How will we build this without losing scope or rollback thinking? |
| `trace.md` | Important claim → basis → control/design feature → evidence → ship posture. | Can reviewers navigate from claim to proof quickly? |
| `verification.md` | Claims, methods, commands/evals/reviews, acceptance criteria, results, gaps. | Does the proof match the claims? |
| `ship.md` | Baseline, evidence status, residual risks, rollback, monitoring, handoff, release decision. | Should this ship now? |

---

## 4. Overhead trap

Do not turn the spine into a hidden full packet.

Avoid:

- copying source-map text into every template;
- writing long narratives where a link and status field would work;
- filling Standard records for a clearly Quick change;
- claiming test coverage proves unrelated safety/security/reliability claims;
- letting AI-generated documentation outrun independent evidence.

Use links, status labels, and explicit gaps instead.

---

## 5. Required links

Every packet should link to the relevant:

- change slug / PR / issue;
- affected files, configs, prompts, models, dependencies, evals, docs, or release artifacts;
- source/basis record when a claim depends on it;
- verification command, CI run, eval report, review, screenshot/log, or named evidence gap;
- rollback/restore path and monitoring signal when release-facing;
- AI-assisted scope and independent check when AI had material authority.

---

## 6. Exit criteria

A thin-spine packet is complete when:

1. the selected mode is justified;
2. each activated artifact exists and answers a decision question;
3. every important claim has evidence, an explicit gap, or a deliberate deferral;
4. release status is clear: ship, do not ship, or ship with named residual risk;
5. the packet is small enough to be used as agent context without loading the whole repo.

---

## 7. Source-lineage note

This evidence spine is an original Git-native workflow inspired by public configuration management, safety-in-design, software assurance, secure development, AI risk, supply-chain, and high-reliability software sources mapped in:

- `../00-standards-foundation/source-map.md`
- `../../01-field-guide/source-to-concept-crosswalk.md`
- `change-control-packets.md`
- `activation-thresholds.md`

It is not a compliance framework and does not claim conformity with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.

---

## 8. Public v0 follow-ups

- Keep the v0 validator focused on Quick and Standard packet structure, evidence status, source-lineage notes, local links, and prohibited overclaiming language.
- Add richer validator checks for activated Nuclear/Incident/Release artifacts after the Quick/Standard path has proven useful.
- Prove the expanded C-002/C-003 chains in the `ai-agent-tool-permissions` worked example before adding heavier Nuclear-mode templates.
