# Standard Basis Record

**Purpose:** State what must stay true for the graded-approach sharpening to help rather than bloat, and tie each requirement to the loop it closes and the public source it draws on.

**Activation threshold:** Standard mode: the change edits public doctrine, an agent-loaded skill, and the maxims.

**Minimum useful version:** the protected outcomes, the per-item requirements, and the assumptions that bound them.

**Overhead trap:** Do not invent requirements by writing a long design essay. Capture only the basis this change needs.

---

## Change context

- Slug: graded-approach-sharpening
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-17
- Decision this basis supports: which graded-approach ideas to adopt, and how, so each is a true value-add that sharpens an existing surface.

## Mission / need

The repo already runs a graded approach but leaves its low end implicit ("trivial → nothing" is never named or guarded) and states some of its logic only operationally. The need is to name the floor, close the loophole that naming it could open, and make the consequence-to-rigor link explicit — without a parallel taxonomy.

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The repo's taste is preserved | Additions must sharpen existing surfaces, not duplicate or inflate them | Each requirement names the existing loop it closes; the adversarial review killed a redundant new page |
| No new oversight loophole | A named floor must not become a sanctioned way to skip rigor | Dominant tripwires + "when in doubt it is Quick" + the non-waiver maxim |
| Source discipline holds | Lineage stays legally clean | Load-bearing lineage on already-mapped DOE/NASA; cross-jurisdiction refs marked concept-only / `public-url-needed`, no compliance claim |
| One axis, not two | The repo rejects a competing taxonomy | The floor sits on the existing mode/tier axis; no A/B/C/D letters |
| Tests and budgets stay green | Doctrine edits must not break contracts | Suite, token audit, doctor, validation pass; `ng-classify` regenerated |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| The floor downgrades a trust-bearing change | A consequential change ships with no review | Tripwires dominate; "when in doubt it is Quick"; extended rationalization traps in the skill |
| An implied-compliance claim with a regulator | Legal / trust harm | Concept-only lineage; `public-url-needed`; the catch-all disclaimer covers IAEA/CNSC/ONR |
| A competing taxonomy fragments the model | Two axes, reader confusion | Floor expressed only in existing mode/tier vocabulary |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Every concept maps to an already-mapped source | fact | `source-map.md` Tiers 1, 4; DOE-HDBK-1028, NASA Lessons Learned | A reviewer finds a concept needing a non-mapped source as direct lineage | FlyFission |
| The floor never waives the always-on Core habits | fact | `CORE.md`, charter Art. 9; the non-waiver maxim | A record uses the floor to skip the questioning attitude | FlyFission |
| `change-control-packets.md` already permits "no packet when a commit message suffices" | fact | `docs/02-operating-system/change-control-packets.md` | That line is removed or narrowed | FlyFission |
| Foreign-source URLs are unverified from this environment | fact | WebFetch blocked in sandbox | A current public URL is confirmed in-repo → promote to verified-public | FlyFission |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The graded approach is already DOE-sourced in the repo | local proof | `source-map.md` line for the DOE QA page; `modes.md` source-lineage note | No new primary source needed; foreign refs stay concept-only |
| "No artifact at all" contradicts the completion standard | local proof | `AGENTS.md` completion standard; charter Art. 4 | Floor reframed to "no packet; commit message is the record" |
| Several report ideas are already covered | local proof | adversarial redundancy review | New page killed; items reframed to sharpen, not duplicate |

## Interfaces and trust boundaries

- Internal interfaces affected: the skill→command generation (`gen-commands`) projection for `ng-classify`.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: unchanged; the floor explicitly defers to Quick+ at any tripwire.
- AI/model/tool authority boundaries: unchanged.

## Dependency / model / supplier intended use

Use this section only when activated. Not activated — no dependency, model, or supplier trust change.

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a change is purely administrative, instantly reversible, and crosses no trust boundary THE SYSTEM SHALL treat it as the administrative floor — no packet, the commit message is the record | 10 CFR 830.3 graded approach; `change-control-packets.md` commit-message line | Floor section + trigger row + shortcut in `activation-thresholds.md`; notes in `modes.md`, `change-control-packets.md`, `risk-tiers-and-modes.md`; floor screen in the skill | `verification.md` (read + doctor + validate) |
| REQ-002 | IF any tripwire is present (auth, data, dependency, model/prompt, agent authority, CI/`.github/`, release, baseline, public/claim-bearing wording, or non-reversibility) THEN THE SYSTEM SHALL lift the change to at least Quick | The router's existing Standard-plus traps in `using-nuclear-grade` | Tripwire list aligned across the floor edits; extended Common Rationalizations in the skill | `verification.md` (read; skill contract tests) |
| REQ-003 | THE SYSTEM SHALL hold that grading scales how, not whether — the always-on baseline is never waived | `CORE.md` Core 7; charter Art. 9 | Non-waiver maxim in `MAXIMS.md`; reinforced in `modes.md` and `CORE.md` | `verification.md` (`test_public_docs`) |
| REQ-004 | THE SYSTEM SHALL grade the change independently of the standing item and take the higher | DOE/NRC change-significance practice (USQ/50.59) already referenced | Line in the skill `## Process` and `risk-tiers-and-modes.md` | `verification.md` (read; parity test) |
| REQ-005 | WHERE the affected component carries a live deficiency, a recent incident, or recurring escaped defects THE SYSTEM SHALL raise the mode above intrinsic risk | DOE-HDBK-1028 operating experience; NASA Lessons Learned | Performance-history dimension in `activation-thresholds.md`; clause in the skill; wired to `deficiency-register.md` | `verification.md` (read + link check) |
| REQ-006 | THE SYSTEM SHALL record the graded-approach lineage once, anchored on DOE, with cross-jurisdiction refs concept-only | source discipline; `do-not-cite-directly.md` | Crosswalk rows (§1, §2) anchored on DOE 10 CFR 830; Tier 1b `public-url-needed` refs in `source-map.md` | `verification.md` (boundary read; doctor links) |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md` summary, this basis |
| Architecture — shape and major parts | n/a | doctrine-only change |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the uploaded deep-research report; the user-approved plan
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis record inspired by public ideas on design basis, the graded approach, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
