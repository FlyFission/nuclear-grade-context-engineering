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
| AI-assisted change control | The AI's scope, permissions, approvals, custody roles, and five-axis actor–evidence coupling profile are stated when the AI did real work. | AI-assisted packets | AI or tool actions changed code, docs, tests, or release evidence with no scope or no custody/coupling disclosure when strict custody is enabled. |
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

**Built opt-in check: evidence-custody disclosure.** For a Standard packet,
`ng validate <packet> --strict-custody` requires the `## Evidence custody and coupling` section and
checks that it names all six custody roles (generated, selected, transformed, captured, retained,
presented), stable uppercase record IDs (for example `E-001` and `C-001`), an explicit yes/no
decisive status, raw artifact, change actor, verifier or witness, complete table-row width, all five
coupling axes (actor, context, mechanism, authority, resource), a basis for every axis, exactly one
classification, and an admissibility/residual-risk disposition. Unselected slash-delimited template
choices, escaped pipe characters, empty custody roles, and unknown decisive values fail. Custody and
profile IDs must match. A coupled actor axis cannot be labeled as independent/diverse verification;
any non-self-check
must declare a verifier or witness distinct from the change actor; and evidence generated, selected,
and presented by the change actor must be classified as a self-check. A decisive
self-check must point to its `ship.md` disposition. Without `--strict-custody`, legacy Standard packets
remain valid; if they include the section, an incomplete or internally inconsistent profile still fails.
This repository does not yet claim mandatory protected enforcement for strict custody. A PR-controlled
validator or packet mode can weaken an in-repository check. Mandatory policy therefore requires a
pinned validator and an expected packet mode supplied outside the candidate's writable tree.

This stays inside the validator principle: it checks that the packet **exposes** custody and coupling,
not that the declared profile is true or adequate. The check is opt-in during migration because a
structural check the authoring agent runs on its own packet is itself actor-controlled evidence. The
independent signal that carries a trust-bearing gate still comes from protected CI, independent
reproduction or diverse verification, and a reviewer with real authority — not from a line the
actor wrote and linted.

**Built opt-in check: evidence-conditioned decision authority.** For a Standard packet,
`ng validate <packet> --strict-authority` requires `decision-authority.md` and checks that prepare,
recommend, verify, validate, verdict, accept, apply, reopen, and close each appear exactly once; each
right names a non-null evidence-basis authority; the evidence-basis and allocation tables each occur
once inside their named sections; required episode, result, and reopening scalar fields occur once;
evidence-adjudicative rights cite Evidence IDs declared in
`verification.md`; coded source states use `observed`, `bounded_absence`, `unknown`, or `disputed`;
finite negative claims name a finite scope and time boundary; the policy record declares authority,
custodian, SHA-256 digest, and a calendar-valid, non-expired UTC validity under the validator host clock
(or a concrete non-expiry basis); authority values use the declared vocabulary; and the derived
structural result matches the apply allocation or a blocking override. Unknown, disputed, absent, or
decisive self-check evidence cannot produce `agent_apply_structurally_clearable`, and
`policy_result_indeterminate` never clears application. The check does not authenticate actors or the
declared policy, qualify evidence, prove authorization or independence, bind an approval
cryptographically to an action or effect, prevent replay, or establish effective human control. Those
require protected enforcement and additional implementation outside the writable packet.

For strict-authority records, equivalent Markdown H2 forms, including ATX headings with optional closing hashes or trailing HTML comments and Setext H2 headings, are normalized before required-section counting and extraction. HTML comments are removed, and backtick or tilde fenced examples with up to three leading spaces are ignored, before section, scalar, and table parsing. Raw HTML H2 tags are rejected. Scalar bullets recognize `-`, `+`, and `*` unordered-list markers with up to three leading spaces. This prevents visually conflicting declarations from evading uniqueness checks through the supported Markdown forms; it is not a general-purpose CommonMark parser.

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
- `--strict-custody`, when enabled, confirms that evidence IDs, custody roles, decisive status, matching five-axis profiles, classifications, and dispositions are structurally consistent;
- `--strict-authority`, when enabled, confirms that the activated decision-right record is structurally consistent with declared verification evidence and its apply result;
- trust decisions about a dependency, model, or API are scoped to how you will actually use it;
- the release record names the baseline, the rollback, the monitoring, and the open risks.

Exit criteria:

- the evidence needed to accept or reject the change can be reached from the packet;
- open gaps are closed, accepted by a named reviewer, or they block the ship.

### Nuclear / Incident / Research Board / Release modes

The required checks are stricter, but still scaled to the risk:

- the extra records show up only when they are turned on;
- the consequence-appropriate custody/coupling profile and review authority are recorded when the stakes call for stronger separation;
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
