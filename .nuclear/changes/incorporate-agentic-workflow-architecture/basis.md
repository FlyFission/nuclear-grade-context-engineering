# Basis — Incorporate Agentic Workflow Architecture

**Purpose:** State what must stay true for this change to add value without growing the repo's surface or its claims.

---

## Change context

- Slug: `incorporate-agentic-workflow-architecture`
- Related risk record: `risk.md`
- Owner: Maintainer
- Date: 2026-06-16
- Decision this basis supports: how to leverage the agentic-workflow research in the planning stage and enforce the stage contract with existing gates.

## Mission / need

The planner emits delegable slices and the runner is told to give each fan-out agent "only its slice," but the plan never specifies what that scoped context is — the runner invents it at execution time, after the human gate. This change closes that seam by making each slice an explicit, reviewable stage contract, and documents the control-plane/execution-plane synthesis the research points to.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| A human can review per-slice context scoping before build authority opens | It moves a trust-bearing decision in front of the gate, where this repo's doctrine wants it | `agents/planner.md` and `templates/standard/plan.md` now require the inputs (REQ-001) |
| The repo's surface does not grow without earning it | "Reject fat doctrine by measurement"; the skill set is deliberately closed | No new skill; token gate still passes (REQ-006) |
| Public wording stays inside the assurance boundary | The repo's credibility depends on not over-claiming | Boundary test guards the doctrine doc (REQ-003, REQ-007) |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Two conflicting definitions of "stage contract" in the repo | Readers lose trust; the pattern reads as incoherent | Reconcile minimal (CONTEXT.md) and full (template) forms once (REQ-004) |
| The doctrine reads as "folders replace frameworks" or as a compliance claim | Easy to attack; misleads adopters | Explicit boundary section + boundary test (REQ-003, REQ-007) |
| A coupled CI edit is missed and the branch breaks | Wastes review; erodes the "self-tracking" claim | Enumerate and run every gate locally (REQ-007) |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| The MWP is already an accepted source | fact | `docs/00-standards-foundation/source-map.md` lists arXiv:2603.16021 | The source entry is removed or downgraded | Maintainer |
| The validator has no per-template schema, so new plan columns won't break it | fact | `nuclear_grade/ng_validate.py` checks structure, not build-sequence columns | A future validator inspects column content | Maintainer |
| Command and skill sets are hardcoded in tests | fact | `tests/test_command_contracts.py`, `tests/test_skill_contracts.py` | The tests stop pinning the sets | Maintainer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Adding a skill costs 5+ coupled edits | local proof | hardcoded `EXPECTED_SKILLS` + `skill-evaluation.md` + comparison-study coverage | Justifies promote-in-place over a new skill |
| Templates/docs have no per-file token ceiling | local proof | `nuclear_grade/tokens.py` `check_budgets` gates only skills/commands/repeats | New template and doc are budget-safe |

## Interfaces and trust boundaries

- Internal interfaces affected: the planner→runner Context Pack handoff; the plan-template build-sequence table.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: the plan gate (unchanged in placement, sharper in content).
- AI/model/tool authority boundaries: planner stays read-only over product code (Write only to the packet); tool grant unchanged.

## Dependency / model / supplier intended use

Not applicable — this change introduces no new dependency, model, or service.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN the planner produces a delegable slice THE planner SHALL express it as a stage contract naming Inputs by exact `file#section`, Outputs, a context budget, and a determinism posture for model-mediated steps. | Mission / need | `agents/planner.md`, `templates/standard/plan.md` build-sequence columns | Manual review of both files |
| REQ-002 | THE repository SHALL provide a registered, discoverable `stage-contract.md` template carrying Inputs/Process/Outputs, an enforcement rung, and a determinism posture. | Protected outcome | `templates/standard/stage-contract.md`, registered in `nuclear-grade.yaml` | `ng doctor`; file present |
| REQ-003 | THE doctrine SHALL map the control/execution-plane split onto PROVE and the rung ladder, and SHALL state determinism posture as a disclosure, not a guarantee. | Protected outcome | `docs/02-operating-system/agentic-workflow-architecture.md` | Boundary test; manual review |
| REQ-004 | THE repository SHALL define the stage-contract vocabulary once and reconcile the minimal and full forms so no two definitions conflict. | Unacceptable outcome | `docs/glossary.md`, `organizing-project-folders`, doctrine doc | Manual review |
| REQ-005 | THE `recording-what-an-agent-did` skill SHALL name the external-trace link targets and state that the packet links to the export rather than copying it. | Mission / need | `skills/recording-what-an-agent-did/SKILL.md` Process step 7 | `ng tokens`; manual review |
| REQ-006 | THE workflow-architecture path SHALL be discoverable without a new skill — via the workflow catalog, the decision matrix, and the doctrine's design-pass section. | Protected outcome | `WORKFLOWS.md`, `CORE.md`, `docs/02-operating-system/agentic-workflow-architecture.md` (§8) | Catalog/matrix rows present; manual review |
| REQ-007 | WHEN this change is built THE change SHALL keep CI green and SHALL add a preventive control guarding the doctrine doc's boundary wording. | Unacceptable outcome | coupled test/registry edits; `tests/test_public_docs.py` boundary test | Full local CI mirror |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md`, this file |
| Architecture — shape and major parts | yes | `docs/02-operating-system/agentic-workflow-architecture.md` |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | No data models change |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the deep-research report; this branch's draft PR
- Source lineage: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade change record. The stage-contract shape adapts the Model Workspace Protocol (Van Clief and McDermott, arXiv:2603.16021); the enforcement-rung and determinism framing are original. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
