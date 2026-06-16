# Validators

**Purpose:** This file defines the first deterministic checks that keep Nuclear-grade usable, safe about sources, and low on tokens, without asking an LLM to re-audit everything on every change.

**Status:** A basic checker is built at `../../tools/ng_validate.py`. The richer checks below are still a design spec. This is not a compliance audit or a certification workflow.

---

## 1. Validator principle

Nuclear-grade checkers should check structure, links, evidence status, and language that is not allowed. They should not pretend to decide whether a system is safe, secure, compliant, or ready for regulated use.

The useful split is:

```text
human judgment decides engineering adequacy
validator checks whether the packet exposes the evidence needed for that judgment
```

---

## 2. Activation threshold

Run the checker when any of these are true:

- a `.nuclear/changes/<slug>/` packet is opened or updated;
- a PR says a change is ready for review or release;
- a template, source-foundation doc, or worked example changes;
- an AI-assisted change produced docs, code, tests, or release evidence;
- the repo is getting ready for a public release or a README or quickstart update.

**Minimum useful version:** a local script or checklist that fails on missing required files or sections, on compliance claims that are not allowed, on broken internal links, on missing evidence status, and on source-lineage notes that do not point to public URLs.

**Overhead trap:** building a heavy audit engine before the thin evidence spine has proven itself in the worked example.

---

## 3. Validator rule set

| Check | What it verifies | Applies to | Failure condition |
|---|---|---|---|
| Public citation check | Direct citation and source-lineage links are public, open, and linkable, or clearly marked TODO. | Source docs, templates, examples | Paid or private lineage, a missing URL, or an unchecked source shown as checked. |
| Prohibited compliance language | Public docs do not claim formal compliance or certification. | All public docs/templates | Phrases like “NQA-1 compliant,” “NRC compliant,” “ISO compliant,” or similar outside disclaimers/do-not-cite contexts. |
| Activated artifact check | The required packet files exist for the chosen mode. | Change packets | Quick/Standard/Nuclear/Incident/Release mode selected but required files missing. |
| Required section check | Templates keep their purpose, activation threshold, minimum useful version, overhead trap, required links, exit criteria, and source-lineage note. | Templates and examples | A required section is gone or renamed past recognition. |
| Trace-link check | Important claims link to a basis, an implementation, a verification, a release, or a clearly marked gap. | Standard+ packets | A claim has no evidence link and no stated gap. |
| Evidence status check | Evidence is labeled planned / run / passed / failed / blocked / not applicable. | `proof.md`, `verification.md`, `ship.md` | Evidence is written as prose but has no status and no reproducible command or artifact link. |
| AI-assisted change control | The AI's scope, permissions, approvals, and independent checks are stated when the AI did real work. | AI-assisted packets | AI or tool actions changed code, docs, tests, or release evidence with no scope and no verification record. |
| Source-map reference check | Source-lineage notes point to `source-map.md` or approved public URLs. | Field guide/templates/examples | A new source shows up with no source-map entry and no public URL. |
| Token/context discipline | Agent context packs stay focused on the mode, the packet, the affected files, and the relevant source excerpts. | Context packs | The prompt or context asks for the whole repo or all standards with no reason to turn that on. |
| CM record visibility | Turned-on CM records name the controlled items, the impact, the baseline, the variance, the OPEX, and the triggers. | CM records | Controlled state changes with no owner, no evidence link, and no re-check trigger. |

**Possible future check (not built): stage-contract structure.** A stage contract (see
[`agentic-workflow-architecture.md`](agentic-workflow-architecture.md)) could be linted
structurally — does each stage name Inputs / Process / Outputs, an enforcement rung, and a
next-stage consumer for each output? That would stay inside the validator principle (structure,
not judgment). It is deliberately deferred: the roadmap keeps the deterministic checker the
default and stages any richer semantic check as an opt-in layer, so a structural stage-contract
check should arrive the same way — and never as a gate the authoring agent can edit (see
[`runtime-enforcement.md`](runtime-enforcement.md)).

---

## 4. Mode-specific validation gates

### Quick mode

Required checks:

- `risk.md` exists;
- `proof.md` exists;
- the risk states how easy it is to undo, how bad failure is, how easy it is to spot, and the escalation decision;
- the proof has at least one concrete verification step, or a clear reason why looking it over by hand is enough.

Exit criteria:

- all Quick required files exist;
- the proof status is not blank;
- no escalation trigger is left open.

### Standard mode

Required checks:

- `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, and `ship.md` exist;
- important claims have an evidence status or a named gap;
- trust decisions about a dependency, model, or API are scoped to how you will actually use it;
- the release record names the baseline, the rollback, the monitoring, and the open risks.

Exit criteria:

- the evidence needed to accept or reject the change can be reached from the packet;
- open gaps are closed, accepted by a named reviewer, or they block the ship.

### Nuclear / Incident / Research Board / Release modes

The required checks are stricter, but still scaled to the risk:

- the extra records show up only when they are turned on;
- an independent review is recorded when the stakes call for it;
- OPEX or decision records link back to the basis, tests, monitors, or limits;
- release readiness does not lean on vague “looks good” statements.

Exit criteria:

- the packet makes the decision reviewable without rereading the whole repo;
- future maintainers can see what changed, why, what proved it, and what is still uncertain.

### Activated CM records

The required checks stay light in Public v0:

- each controlled item has a reason for being under control;
- impact screens say whether each item is updated, left alone, deferred, or blocked;
- baseline records name the accepted state and the re-check triggers;
- variance and OPEX records link back to the baseline or to packet evidence.

Exit criteria:

- the controlled state can be reached without rereading the whole repo;
- the checker does not claim to decide whether the configuration management is adequate.

---

## 5. Prohibited-language validator seed list

Flag these when they are used as claims, not as limits or disclaimers:

```text
NQA-1 compliant
ASME compliant
EPRI compliant
IEEE compliant
IEC compliant
ISO compliant
ANSI/ANS compliant
NEI compliant
NRC compliant
DOE compliant
NASA compliant
NIST compliant
CISA compliant
certified quality assurance program
regulatory approval
commercial-grade dedication package
formal V&V
formal verification and validation
NQA-1 evidence
NQA-1 record
quality-assurance record
safety-basis evidence
procurement evidence
```

Allowed places:

- `DISCLAIMER.md`;
- `do-not-cite-directly.md`;
- `compliance-boundaries.md`;
- examples that plainly say “do not claim this.”

Prefer wording like:

> public-source-inspired, original software workflow, evidence-oriented, non-compliance-claiming.

---

## 6. Required links

Validator implementation should reference:

- `docs/00-standards-foundation/source-map.md`
- `docs/00-standards-foundation/compliance-boundaries.md`
- `docs/00-standards-foundation/do-not-cite-directly.md`
- `docs/00-standards-foundation/public-citation-strategy.md`
- `docs/01-field-guide/source-to-concept-crosswalk.md`
- `docs/02-operating-system/activation-thresholds.md`
- `docs/02-operating-system/change-control-packets.md`
- active packet files under `.nuclear/changes/<slug>/`

---

## 7. Source-lineage note

This checker design is an original software workflow. It draws on public source families mapped in `source-map.md`: public nuclear and federal configuration and quality-assurance ideas, NRC public software assurance guidance, NIST SSDF and supply-chain risk guidance, CISA secure-by-design and SBOM materials, NASA software and systems engineering guidance, and open software assurance sources such as SLSA, OpenSSF, OWASP, SPDX, and CycloneDX.

It does not implement, certify, or claim compliance with those sources.
