# Standard Basis Record

**Purpose:** State what must stay true for the gleaned value-adds to help rather than bloat, and tie each requirement to the internal loop it closes and the public source it draws on.

**Activation threshold:** Standard mode: the change amends the charter and durable public doctrine.

**Minimum useful version:** Protected outcomes, requirements per workstream, and the assumptions that bound them.

---

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The repo's taste is preserved | Additions must sharpen existing material, not duplicate or inflate it | Each requirement names the existing loop it closes |
| Source discipline holds | The repo cites DOE/NRC/NIST/NASA public sources, never IAEA/WANO/INSAG or paywalled standards | Each requirement maps to an already-mapped source |
| No scope creep into an HR program | Learning/training stays change-scoped and agent-facing | Boundary statement in `leadership-and-high-reliability.md` stays crisp |
| Tests and budgets stay green | Doctrine edits must not break contracts or token budgets | Full suite, token audit, doctor, validation pass |

## Requirements

| ID | Requirement / claim | Closes which internal loop | Source lineage | Evidence planned |
|---|---|---|---|---|
| REQ-001 | Charter Art. 19 and `learning-from-experience` distinguish protected honest error from accountable willful violation | Reconciles no-blame learning with Art. 3 (never normalize a deviation) and Art. 4 | DOE-HDBK-1028 | `trace.md`, `verification.md` |
| REQ-002 | The HPI control stack states that layers must fail independently, with the agentic correlated-failure anti-pattern and graded layering | Generalizes the verification-only independence point in `authority-and-intent.md` | NIST SP 800-160, NRC RG 1.168, DOE-HDBK-1028 | `trace.md`, `verification.md` |
| REQ-003 | Variance discipline covers deliberate temporary modifications with operator visibility, a named back-out, and expiry | Extends discovered-variance handling to introduced exceptions | DOE-STD-1073 | `trace.md`, `verification.md` |
| REQ-004 | `authority-and-intent.md` defines competence-to-act (qualification) | Closes the undefined "train before delegating" referenced by Art. 17 | DOE-HDBK-1028, intent-based leadership | `trace.md`, `verification.md` |
| REQ-005 | A durable-memory doctrine exists as the persistent counterpart to context-window discipline, with a provenance/poisoning guard | Develops the "persistent cross-run memory" lifetime and answers the "stuck in chat history" red flag | Tier 9 context-engineering sources (LangChain, ACE) | `trace.md`, `verification.md` |

## Assumptions and constraints

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Every new concept maps to an already-mapped source | fact | `source-map.md` Tiers 1, 3, 9; Tier 8 | A reviewer finds a concept that needs a non-mapped source | FlyFission |
| Docs are not enumerated by packaging tests | fact | `tests/test_packaging.py` checks skills/commands/template modes only | A test starts enumerating operating-system docs | FlyFission |
| No new skill/command is added | fact | scope decision in `risk.md` | A reviewer asks for a drill or qualification skill/command | FlyFission |
| Token budgets have headroom for the additions | assumption | `nuclear-grade.yaml` budgets seeded above measured maxima | `ng tokens` reports a violation | FlyFission |

## Required links

- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`

## Exit criteria

- Protected outcomes and requirements are explicit and testable.
- Each requirement names the internal loop it closes and a mapped source.
- Assumptions carry an invalidation trigger and an owner.

## Source-lineage note

Original Nuclear-grade basis record inspired by public human-performance, configuration-management, systems-security-engineering, and context-engineering sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
