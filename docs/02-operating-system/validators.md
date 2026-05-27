# Validators

**Purpose:** Define the first deterministic checks that keep Nuclear-grade usable, source-safe, and low-token without asking an LLM to re-audit everything on every change.

**Status:** A minimal validator is implemented at `../../tools/ng_validate.py`; richer checks described below remain a design spec. This is not a compliance audit or certification workflow.

---

## 1. Validator principle

Nuclear-grade validators should check structure, links, evidence status, and prohibited language. They should not pretend to decide whether a system is safe, secure, compliant, or ready for regulated use.

The useful split is:

```text
human judgment decides engineering adequacy
validator checks whether the packet exposes the evidence needed for that judgment
```

---

## 2. Activation threshold

Run validation when any of these are true:

- a `.nuclear/changes/<slug>/` packet is opened or updated;
- a PR claims a change is ready for review or release;
- a template, source-foundation doc, or worked example changes;
- an AI-assisted change produced docs, code, tests, or release evidence;
- the repo is preparing a public release or README/quickstart update.

**Minimum useful version:** a local script or checklist that fails on missing required files/sections, prohibited compliance claims, broken internal links, missing evidence status, and source-lineage notes that do not point to public URLs.

**Overhead trap:** building a heavyweight audit engine before the thin evidence spine has been proven in the worked example.

---

## 3. Validator rule set

| Check | What it verifies | Applies to | Failure condition |
|---|---|---|---|
| Public citation check | Direct citation/source-lineage links are public/open/linkable or explicitly marked TODO. | Source docs, templates, examples | Paywalled/proprietary lineage, missing URL, or unverified source presented as verified. |
| Prohibited compliance language | Public docs do not claim formal compliance/certification. | All public docs/templates | Phrases like “NQA-1 compliant,” “NRC compliant,” “ISO compliant,” or similar outside disclaimers/do-not-cite contexts. |
| Activated artifact check | Required packet files exist for the selected mode. | Change packets | Quick/Standard/Nuclear/Incident/Release mode selected but required files missing. |
| Required section check | Templates retain purpose, activation threshold, minimum useful version, overhead trap, required links, exit criteria, and source-lineage note. | Templates and examples | Required section absent or renamed beyond recognition. |
| Trace-link check | Important claims link to basis, implementation, verification, release, or explicit gap. | Standard+ packets | Claim has no evidence link and no declared gap. |
| Evidence status check | Evidence is labeled planned / run / passed / failed / blocked / not applicable. | `proof.md`, `verification.md`, `ship.md` | Evidence exists as prose but has no status or reproducible command/artifact link. |
| AI-assisted change control | AI scope, permissions, approvals, and independent checks are declared when AI materially contributes. | AI-assisted packets | AI/tool actions altered code/docs/tests/release evidence without scope and verification record. |
| Source-map reference check | Source-lineage notes reference `source-map.md` or approved public URLs. | Field guide/templates/examples | New source appears without source-map entry or public URL. |
| Token/context discipline | Agent context packs are focused on mode, packet, affected files, and relevant source excerpts. | Context packs | Prompt/context asks for whole repo or all standards without an activated reason. |
| CM record visibility | Activated CM records name controlled items, impact, baseline, variance, OPEX, and triggers. | CM records | Controlled state changes without owner, evidence link, or revalidation trigger. |

---

## 4. Mode-specific validation gates

### Quick mode

Required checks:

- `risk.md` exists;
- `proof.md` exists;
- risk declares reversibility, consequence, detectability, and escalation decision;
- proof contains at least one concrete verification step or explicit reason why manual inspection is enough.

Exit criteria:

- all Quick required files exist;
- proof status is not blank;
- no escalation trigger remains unresolved.

### Standard mode

Required checks:

- `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, and `ship.md` exist;
- important claims have evidence status or named gaps;
- dependency/model/API trust decisions are scoped by intended use;
- release record names baseline, rollback, monitoring, and unresolved risks.

Exit criteria:

- evidence needed to accept/reject the change is navigable from the packet;
- unresolved gaps are either closed, accepted by an explicit reviewer, or block ship.

### Nuclear / Incident / Research Board / Release modes

Required checks are stricter but still risk-scaled:

- triggered extensions are present only when activated;
- independent review is recorded when consequence demands it;
- OPEX or decision records link back to basis, tests, monitors, or thresholds;
- release readiness does not rely on vague “looks good” statements.

Exit criteria:

- the packet makes the decision reviewable without rereading the whole repo;
- future maintainers can see what changed, why, what proved it, and what remains uncertain.

### Activated CM records

Required checks remain lightweight in Public v0:

- controlled items have a reason for control;
- impact screens name update/no-op/defer/block disposition;
- baseline records name accepted state and revalidation triggers;
- variance/OPEX records link back to baseline or packet evidence.

Exit criteria:

- controlled state is navigable without rereading the whole repo;
- the validator does not claim to decide CM adequacy.

---

## 5. Prohibited-language validator seed list

Flag these when used as claims rather than boundaries/disclaimers:

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

Allowed contexts:

- `DISCLAIMER.md`;
- `do-not-cite-directly.md`;
- `compliance-boundaries.md`;
- examples that explicitly say “do not claim this.”

Prefer phrases like:

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

This validator design is an original software workflow inspired by public source families mapped in `source-map.md`: public nuclear/federal configuration and QA concepts, NRC public software assurance guidance, NIST SSDF and supply-chain risk guidance, CISA secure-by-design/SBOM materials, NASA software/systems engineering guidance, and open software assurance sources such as SLSA, OpenSSF, OWASP, SPDX, and CycloneDX.

It does not implement, certify, or claim compliance with those sources.
