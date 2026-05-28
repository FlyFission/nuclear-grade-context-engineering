# Standard Basis Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** State what must remain true for the change to be safe, reliable, secure, useful, and reviewable.

**Activation threshold:** Use for Standard changes where requirements, architecture, interfaces, dependencies, AI authority, protected outcomes, or unacceptable outcomes need an explicit basis.

**Minimum useful version:** Mission, protected outcomes, unacceptable outcomes, assumptions, constraints, intended-use trust decisions, and evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to authoritative needs and capture only the basis needed for this change.

---

## Change context

- Slug:
- Related risk record: `risk.md`
- Owner:
- Date:
- Decision this basis supports:

## Mission / need

What capability or problem is this change addressing?

## Protected outcomes

What must the system preserve?

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

Only include important claims that need evidence.

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | | | | |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc:
- Source lineage, if cited:

## Exit criteria

- Builder and reviewer can answer “what must remain true?”
- Protected and unacceptable outcomes are explicit.
- Important assumptions have invalidation triggers.
- Evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public design-basis, safety-in-design, design-description, hazard/failure-analysis, AI-risk, and supply-chain-risk concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
