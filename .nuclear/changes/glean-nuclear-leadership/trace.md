# Standard Trace Record

**Purpose:** Tie each requirement to the exact edit that satisfies it and the evidence that confirms it.

**Activation threshold:** Standard mode: claims span the charter, several docs, a skill, a command, and a template.

**Minimum useful version:** One row per requirement, from claim to design feature to evidence, with a status.

---

## Trace

| ID | Claim | Design feature (where) | Evidence type | Evidence | Status |
|---|---|---|---|---|---|
| REQ-001 | Honest error is protected; willful violation is accountable, never normalized | Charter Art. 19 refinement; `learning-from-experience` skill (Overview/Process/Red Flags/Prompt); regenerated `ng-learn` card prompt | local proof | `verification.md` (skill + command parity tests) | pass |
| REQ-002 | Control-stack layers must fail independently; same-model act-and-check is one barrier; layer count scales with consequence | "HPI control stack" section in `configuration-management.md`; cross-link in `authority-and-intent.md`; crosswalk row | manual review | `verification.md` (read + link check) | pass |
| REQ-003 | Deliberate temporary modifications are visible, have a named back-out, and expire | Temporary-modifications section in `variance-and-drift.md`; back-out column in `templates/cm/variance.md`; crosswalk row | manual review | `verification.md` (token audit + read) | pass |
| REQ-004 | Competence-to-act is defined: action class → demonstrated competence → revalidation trigger | Qualification section in `authority-and-intent.md` | manual review | `verification.md` (read + link check) | pass |
| REQ-005 | Durable memory is the persistent counterpart to context-window discipline, with a provenance/poisoning guard | `durable-memory.md`; back-link in `context-window-discipline.md`; boundary amendment in `leadership-and-high-reliability.md` | manual review | `verification.md` (boundary read + link check) | pass |

## Residual / deferred

| Item | Why deferred | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Leading-indicators metrics doc | Contradicts the repo's stated anti-dashboard boundary; duplicates an existing section | defer | FlyFission | A reviewer or OPEX shows precursor metrics are needed |
| Drill / game-day template | Most speculative; qualification + memory carry the learning substance | defer | FlyFission | Demonstrated use, or user request to add it |

## Required links

- `basis.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every requirement has a design feature, an evidence type, and a status.
- Deferred items carry a disposition, an owner, and a recheck trigger.

## Source-lineage note

Original Nuclear-grade trace record inspired by public software-assurance and configuration-management sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
