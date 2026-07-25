# Basis

**Purpose:** State what must stay true for this change to be safe, reviewable, and useful.

## Change context

- Slug: trust-propagation-two-party
- Related risk record: `risk.md`
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17
- Decision this basis supports: Whether to adopt computed propagation and two-party gates and land them first as inert, tested modules.

## Mission / need

nuclear-grade enforces structural completeness of a packet, but two of its load-bearing principles, "a baseline is only as trusted as its weakest evidence" and the independence principle, are still norms a reviewer must uphold by hand. This change ports two Palantir Foundry trust mechanisms (marking propagation and purpose-based access) so those two principles can become computed properties.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Existing validator behavior is unchanged | The modules must not regress current packets | Full existing suite green; nothing imports the new modules |
| Trust never rises above the weakest claim | This is the core propagation guarantee | Unit tests over synthetic packets |
| A load-bearing claim needs an independent second party | This is the independence principle made structural | Unit tests over synthetic authorship tables |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A wired-in gate falsely blocks valid packets | fault | CI breaks for every packet | Keep modules inert this packet; land as advisory before blocking |
| Propagation silently miscomputes over a varied table | insufficiency | A tainted packet reads green | Normalize the claim table before wiring in; unit tests on the parser |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| The claim-to-evidence table can be normalized to one schema | assumption | Observed schema variance across current packets | A packet whose table cannot be normalized | Ben Huffer |
| Stdlib-only keeps runtime deps at zero | fact | Package ships zero runtime deps today | Any need for a third-party parser | Ben Huffer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Propagation computes the minimum over counted statuses | local proof | `tests/test_propagation.py` | Confirms the core guarantee |
| Packets do not record per-claim drafter versus verifier | fact | Git authorship on real packets is single-identity | Two-party gate needs a schema addition |

## Interfaces and trust boundaries

- Internal interfaces affected: `nuclear_grade` package gains two modules; no existing symbol changes.
- External services/APIs affected: none.
- Data classes affected: none; the modules read packet Markdown only.
- Human approval boundaries: maintainer review and merge remain the human gate.
- AI/model/tool authority boundaries: AI authored code and evidence under maintainer direction; no autonomous merge.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| Python standard library only | Parsing and set/min logic | none beyond normal runtime | Zero third-party imports | Any added dependency |

## Derived requirements or claims

- REQ-001: `THE SYSTEM SHALL` compute a packet's effective trust as the minimum over its counted claim statuses and report any claim below `pass` as tainting the packet.
- REQ-002: `WHEN` a claim is marked `pass` and its `Verified by` equals its `Evidence author`, `THE SYSTEM SHALL` report that the claim lacks an independent second party.
- REQ-003: `THE SYSTEM SHALL` wire both checks into `validate_packet` only after the claim-to-evidence table is normalized and a gate severity is chosen (planned; not in this packet).

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | Effective trust is the minimum over counted claim statuses | Weakest-evidence principle | `propagation.effective_status` / `check_promotion` | `tests/test_propagation.py` |
| REQ-002 | A pass claim self-verified by its evidence author is flagged | Independence principle | `two_party.check_two_party` | `tests/test_two_party.py` |
| REQ-003 | Wire the gates into `validate_packet` after normalization | Structural enforcement | future `_check_*` calls | planned; deferred to a follow-up packet |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | This basis and `risk.md` |
| Architecture — shape and major parts | yes | Two standalone modules mirroring `_check_*` style |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | yes | Claim table and proposed `Claim authorship` table |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: this PR description
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
