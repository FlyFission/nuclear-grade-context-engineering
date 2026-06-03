# Standard Basis Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

**Activation threshold:** Use for Standard changes where the requirements, architecture, interfaces, dependencies, AI power, protected outcomes, or outcomes to prevent need a clear basis.

**Minimum useful version:** the mission, the protected outcomes, the outcomes to prevent, the assumptions, the constraints, the trust decisions about intended use, and the evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to the real needs and capture only the basis this change needs.

---

## Change context

- Slug:
- Related risk record: `risk.md`
- Owner:
- Date:
- Decision this basis supports:

## Mission / need

What capability or problem does this change address?

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| | | |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| | | |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| | | | | |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| | | | |

## Interfaces and trust boundaries

- Internal interfaces affected:
- External services/APIs affected:
- Data classes affected:
- Human approval boundaries:
- AI/model/tool authority boundaries:

## Dependency / model / supplier intended use

Use this section only when activated.

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| | | | | |

## Derived requirements or claims

Include only the important claims that need evidence.

Write each requirement as one controlled, testable statement — a clear trigger
and a clear response — so a builder and a reviewer read it the same way and a
test can check it. This serves the "operational unambiguity" charter article.
Prefer these shapes:

- `THE SYSTEM SHALL <response>` — an always-true rule.
- `WHEN <trigger> THE SYSTEM SHALL <response>` — an event.
- `WHILE <state> THE SYSTEM SHALL <response>` — a continuous state.
- `WHERE <feature is present> THE SYSTEM SHALL <response>` — an optional feature.
- `IF <unwanted condition> THEN THE SYSTEM SHALL <response>` — a failure path.

Worked example — REQ-001: `WHEN a draft packet fails the structural validator THE
SYSTEM SHALL block the merge and name the first failing section.` One trigger, one
response, testable. Keep the `REQ-NNN` IDs; `trace.md` and `plan.md` reference them.

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | | | | |

## Design outline

A short completeness check, not a design essay. Tick what this change actually
needs; link the real design notes instead of restating them (see the overhead
trap above).

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes / no / n/a | |
| Architecture — shape and major parts | yes / no / n/a | |
| Components and interfaces — boundaries above | yes / no / n/a | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes / no / n/a | |
| Error handling — failure paths and responses | yes / no / n/a | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes / no / n/a | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc:
- Source lineage, if cited:

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
