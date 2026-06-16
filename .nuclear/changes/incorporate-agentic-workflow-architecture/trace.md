# Trace — Incorporate Agentic Workflow Architecture

**Purpose:** Tie each requirement to its edit and its evidence so the change reads end to end.

---

## Change context

- Slug: `incorporate-agentic-workflow-architecture`
- Related basis record: `basis.md`
- Related verification record: `verification.md`
- Owner: Maintainer
- Date: 2026-06-16

## Trace summary

| ID | Claim | Basis link | Task / code ref | Control / design feature | Support type | Verification evidence | Ship posture | Status |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | Planner emits each slice as a stage contract | `basis.md` | `plan.md` step 3 / `agents/planner.md`, `templates/standard/plan.md` | Selective-section inputs + context budget in the build-sequence | local proof | `verification.md` | ship | pass |
| REQ-002 | Registered, discoverable stage-contract template | `basis.md` | `plan.md` steps 1-2 / `templates/standard/stage-contract.md`, `nuclear-grade.yaml` | Template + registry entry | local proof | `verification.md` | ship | pass |
| REQ-003 | Doctrine maps control/execution plane to PROVE + rungs, inside boundary | `basis.md` | `plan.md` step 1 / `docs/02-operating-system/agentic-workflow-architecture.md` | Boundary section + diagram | local proof | `verification.md` | ship | pass |
| REQ-004 | Vocabulary reconciled, no conflicting definitions | `basis.md` | `plan.md` steps 1,4 / `docs/glossary.md`, `skills/organizing-project-folders/SKILL.md` | Minimal vs full form named once | local proof | `verification.md` | ship | pass |
| REQ-005 | External-trace bridge named | `basis.md` | `plan.md` step 4 / `skills/recording-what-an-agent-did/SKILL.md` | Link targets named in Process step 7 | local proof | `verification.md` | ship | pass |
| REQ-006 | Discoverable without a new skill | `basis.md` | `plan.md` step 5 / `WORKFLOWS.md`, `CORE.md`, `docs/02-operating-system/agentic-workflow-architecture.md` | Catalog row + matrix trigger + doctrine design pass | local proof | `verification.md` | ship | pass |
| REQ-007 | CI stays green; boundary wording is guarded | `basis.md` | `plan.md` steps 5-6 / `tests/test_command_contracts.py`, `tests/test_public_docs.py` | Coupled edits + preventive test | local proof | `verification.md` | ship | pass |

## Evidence chain

```text
Risk / need (runner invents per-slice scoping after the gate)
  → Basis / requirement (REQ-001: planner emits a stage contract)
  → Control / design feature (selective-section inputs + enforcement rung)
  → Verification evidence (pytest, doctor, tokens, ng validate all pass)
  → Release decision (ship; revert is a clean git revert)
```

## Open trace gaps

| Gap | Why it matters | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No structural validator check for stage contracts yet | The contract shape is not machine-enforced | defer | Maintainer | When the opt-in semantic/validator layer lands (v0.2) |
| No worked example or eval case for the new path | Less hands-on illustration | defer | Maintainer | If adopters ask for a runnable example |

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `verification.md`
- `ship.md`
- Implementation / docs / tests / evals: the files listed in the trace summary

## Exit criteria

- Each important claim has a status label.
- Each important claim names its support type.
- Every shipped claim has evidence or an accepted leftover risk.
- Deferred or gap claims are not used as release evidence.
- A reviewer can move quickly from claim → basis → evidence → release decision.

## Source-lineage note

Original Nuclear-grade change record. The stage-contract pattern adapts the Model Workspace Protocol (arXiv:2603.16021); the rung and determinism framing are original. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
