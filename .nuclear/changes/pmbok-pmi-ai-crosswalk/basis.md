# Standard Basis Template

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

**Activation threshold:** Use for Standard changes where the requirements, architecture, interfaces, dependencies, AI power, protected outcomes, or outcomes to prevent need a clear basis.

**Minimum useful version:** the mission, the protected outcomes, the outcomes to prevent, the assumptions, the constraints, the trust decisions about intended use, and the evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to the real needs and capture only the basis this change needs.

---

## Change context

- Slug: pmbok-pmi-ai-crosswalk
- Related risk record: `risk.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21
- Decision this basis supports: Whether to add PMBOK / PMI-AI-standard material to the repo, and in what form.

## Mission / need

Project-management-literate and enterprise teams evaluating Nuclear-grade need a bridge from PMI vocabulary (PMBOK, the 2026 PMI AI standard) to the framework. The need is orientation and adoption, not conformance. This change supplies that bridge while preserving the repo's standing policy that PMI material is paywalled and excluded as direct lineage.

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The repo never implies PMI/PMBOK compliance, conformance, certification, or PMP qualification | Core brand/boundary integrity; legal cleanliness | Overclaim scan clean; explicit boundary notes; `ng doctor` OK |
| No paywalled PMI text is reproduced or used to derive structure | Honors do-not-cite-directly policy | Doc describes PMBOK 8 structurally only; PMI listed excluded-direct |
| Always-on token cost stays flat | Context-window discipline | Skill `description:` unchanged; command cards unchanged |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A reader concludes Nuclear-grade is PMI-aligned/certified | False assurance; reputational + legal risk | Boundary note at top + "what not to claim" section; overclaim scan |
| Skill descriptions or command cards grow | Token burn across every fan-out | Edit bodies only; verify with `gen-commands` diff |
| New unmaintained surface (extra docs/templates) | Drift, stale maintenance | Adversarial trim to one doc, zero new templates |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| PMBOK & PMI AI standard are paywalled PMI works | fact | PMI publishes them for sale | PMI releases an open edition | Ben Huffer |
| PMI already excluded-direct in this repo | fact | `source-map.md` Tier 7 | Policy change | Ben Huffer |
| PMBOK 7 principle/domain names are public | fact | Widely published summaries | — | Ben Huffer |
| PMBOK 8 per-item names withheld here | constraint | Avoid reproducing paywalled detail | — | Ben Huffer |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| PMI AI standard centers human-in-the-loop, tech-agnostic, 8 principles / 5 domains | source claim (PMI public materials) | PMI press release, June 2026 | Frames lead crosswalk table |
| PMBOK 8 pairs 6 principles / 7 domains / 40 processes in 5 focus areas | source claim (public summaries) | Public 2025/2026 write-ups | Described structurally only |
| Repo Core 7 + loop + modes rhyme with the above | local proof | The crosswalk maps to actual repo surfaces | Justifies "rhyme, not compliance" framing |

## Interfaces and trust boundaries

- Internal interfaces affected: cross-links among field-guide, standards-foundation, operating-system, adoption docs, README.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: PR review of boundary wording before merge.
- AI/model/tool authority boundaries: unchanged.

## Dependency / model / supplier intended use

Use this section only when activated. — Not activated; no dependency, model, or service change.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHERE the repo references PMI/PMBOK THE SYSTEM SHALL frame it as named background and state no compliance/conformance claim. | Protected outcome 1 | Boundary note + "what not to claim" section in crosswalk; compliance-boundaries entry | Overclaim scan; review |
| REQ-002 | THE SYSTEM SHALL NOT reproduce PMI text or derive artifact structure from PMI works. | do-not-cite policy | PMBOK 8 described structurally only; PMI excluded-direct | Doc inspection; source-map row |
| REQ-003 | WHEN skills are edited THE SYSTEM SHALL leave every skill `description:` and the generated command cards unchanged. | Token discipline | Body-only edits, avoid `## Prompt` | `git diff` on descriptions; `gen-commands` diff |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md`, this file |
| Architecture — shape and major parts | n/a | docs + skill fold-ins only |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: originating user request; `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`, `docs/00-standards-foundation/do-not-cite-directly.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
