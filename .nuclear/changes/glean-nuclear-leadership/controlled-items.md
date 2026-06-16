# Controlled Items

**Purpose:** Name the approved-state items this change touches, so a reviewer can see what moved from which version to which.

**Activation threshold:** CM records are activated because the change amends the charter and durable public doctrine.

**Minimum useful version:** Each controlled item with its current state, target state, and why it is controlled.

---

## Controlled items

| Item | Type | Current state | Target state | Why controlled | Owner | Evidence | Change type |
|---|---|---|---|---|---|---|---|
| `.nuclear/charter.md` | charter | 1.2.0 | 1.3.0 with refined Art. 19 | Durable backbone all work holds to | FlyFission | `verification.md` | Charter amendment |
| `skills/learning-from-experience/SKILL.md` | skill | no-blame only | no-blame plus the willful-violation distinction | Downstream agents learn from it | FlyFission | `verification.md` | Skill body update |
| `commands/ng-learn.md` | command | no-blame OPEX prompt | prompt makes the just-culture distinction | Portable agent prompt | FlyFission | `verification.md` | Command prompt update |
| `docs/02-operating-system/configuration-management.md` | public doc | control stack as families | families that must fail independently | Core CM doctrine | FlyFission | `verification.md` | Doctrine addition |
| `docs/02-operating-system/authority-and-intent.md` | public doc | decision rights + intent | adds competence-to-act and control-stack cross-link | Authority/qualification doctrine | FlyFission | `verification.md` | Doctrine addition |
| `docs/02-operating-system/variance-and-drift.md` | public doc | discovered variance | adds deliberate temporary modifications | Variance/drift doctrine | FlyFission | `verification.md` | Doctrine addition |
| `templates/cm/variance.md` | template | no back-out field | adds a back-out/removal column | Packet interface users fill | FlyFission | `verification.md` | Template update |
| `docs/02-operating-system/durable-memory.md` | public doc | absent | new persistent-memory doctrine | Retrieval/provenance doctrine | FlyFission | `verification.md` | New doc |
| `docs/02-operating-system/context-window-discipline.md` | public doc | no memory pointer | back-links durable memory | Counterpart doctrine | FlyFission | `verification.md` | Cross-link |
| `docs/01-field-guide/leadership-and-high-reliability.md` | public doc | qualification/drills doctrine-only | qualification + memory in scope; line kept crisp | Boundary statement | FlyFission | `verification.md` | Boundary amendment |
| `docs/01-field-guide/source-to-concept-crosswalk.md` | public doc | no defense-in-depth / temp-mod rows | adds two concept rows | Source-to-concept bridge | FlyFission | `verification.md` | Crosswalk rows |
| `docs/README.md` | public doc | no durable-memory nav row | adds a nav row | Docs navigation | FlyFission | `verification.md` | Nav update |
| `CHANGELOG.md` | public doc | prior entries | adds this change | Version history | FlyFission | `verification.md` | Changelog entry |

## Required links

- `risk.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Every touched approved-state item is listed with current and target state.
- Each item names why it is controlled and where its evidence lives.

## Source-lineage note

Original Nuclear-grade controlled-items record inspired by public configuration-management sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
