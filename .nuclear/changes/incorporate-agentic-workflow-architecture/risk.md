# Risk — Incorporate Agentic Workflow Architecture

**Purpose:** Sort this change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: `incorporate-agentic-workflow-architecture`
- PR / issue: branch `claude/loving-dijkstra-kd8q14`; draft PR to follow
- Owner: Maintainer
- Date: 2026-06-16
- Current lifecycle phase: Plan
- Current work phase: candidate
- Summary: Promote the Model Workspace Protocol stage contract from a hidden subcase of folder hygiene into a named planning artifact — the planner emits each delegable slice as a stage contract (selective-section inputs, outputs, context budget, determinism posture), backed by a new `stage-contract.md` template and a control-plane/execution-plane doctrine doc anchored on the existing rung ladder, plus the external-trace bridge and a discoverability surface that adds no new skill.

## Mission anchor

- Objective: leverage the agentic-workflow research where it adds value in the planning stage, and enforce the interpretable stage contract with this repo's existing out-of-band gates.
- Success criteria: a human can review, at the plan gate, exactly what context each fan-out slice loads; the pattern is discoverable; CI stays green; public wording stays inside the boundary.
- Non-goals / forbidden directions: no new skill; no validator code changes; no claim that folders replace durable runtimes; no compliance or certification claim.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the deep-research report and the Model Workspace Protocol paper (arXiv:2603.16021); originating session request.

## Questioning-attitude summary

- Decision question: where do the report's principles add value in this repo without growing its surface, and how are they enforced?
- Evidence that would change the decision: finding the pattern already fully wired into the planning artifacts (it is not — only into folder hygiene).
- Assumptions that changed the mode: editing an agent-authority artifact and publishing methodology claims both trigger Standard.
- Facts still needing validation: that every coupled CI edit is caught (handled by running the full gate locally).
- Stop or hold conditions: stop if a change would require a new skill, a 6th cluster, or unbounded public wording.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Planner agent | Agent prompt (authority artifact) | Changes what the Plan stage must produce; tool authority unchanged. | `agents/planner.md` |
| Standard plan template | Template | Adds stage-contract columns every future Standard packet can use. | `templates/standard/plan.md` |
| Stage-contract template | New template | The canonical reusable contract shape. | `templates/standard/stage-contract.md` |
| Workflow-architecture doctrine | New public-facing doc | Makes methodology claims; must stay inside the assurance boundary. | `docs/02-operating-system/agentic-workflow-architecture.md` |
| Skill prose | Skill bodies | Reconcile vocabulary and name the trace bridge; keep their contracts. | `skills/breaking-down-the-work/SKILL.md`, `skills/organizing-project-folders/SKILL.md`, `skills/recording-what-an-agent-did/SKILL.md` |
| Discoverability + coupled edits | Registry, catalogs, doctrine, tests | Keep CI green and make the path findable. | `nuclear-grade.yaml`, `WORKFLOWS.md`, `CORE.md`, `docs/02-operating-system/agentic-workflow-architecture.md`, `tests/test_public_docs.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | Shapes how agents plan delegated work repo-wide; wrong wording could mislead adopters. |
| Reversibility | High | Additive markdown plus a few registry/test lines; revert is clean. |
| Detectability | High | Tests, doctor, and the token gate catch structural regressions. |
| Exposure | Medium | The doctrine doc is public-facing and could be read as an over-claim if unbounded. |
| Uncertainty | Low | The pattern already exists in the repo; this promotes and reconciles it. |
| Dependency trust | Low | No new runtime dependencies; stdlib tooling only. |
| AI authority | Medium | Touches the planner prompt, an authority artifact; its tool grant is unchanged. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: the change touches an agent-authority artifact and makes public methodology claims.
- Why lighter mode is not enough: Quick mode would hide the boundary-wording, vocabulary-reconciliation, and coupled-CI risks.
- Why heavier mode is not yet required: reversible documentation, no production deployment, no data migration, no credentials, no irreversible side effects.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | The questioning summary above is sufficient for this change. | Maintainer |
| `basis.md` | yes | The change needs stated requirements (REQ-001..007) and protected outcomes. | Maintainer |
| `verification.md` | yes | The deterministic gates are the evidence. | Maintainer |
| `ship.md` | yes | A reversible methodology change still needs a decision, rollback, and monitoring. | Maintainer |
| `turnover.md` | no | No handoff of unfinished work. | Maintainer |
| `self-check.md` | no | No single irreversible critical action. | Maintainer |
| `supplier-trust.md` | no | No new dependency, model, or service. | Maintainer |
| Nuclear subset record | no | Not warranted for reversible documentation. | Maintainer |

## Immediate evidence obligations

- Minimum evidence before build: confirm the MWP source is already accepted, locate the planner→runner seam, and enumerate every coupled CI edit.
- Minimum evidence before merge/release: the full test suite, `ruff`, `ng doctor`, `ng tokens`, and `ng validate` on this packet all pass.
- Independent review needed? yes; a human confirms the boundary wording and the vocabulary reconciliation before merge.

## Required links

- Packet: `.nuclear/changes/incorporate-agentic-workflow-architecture/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade change record. The promoted pattern adapts the Model Workspace Protocol (Van Clief and McDermott, arXiv:2603.16021), kept in its control-surface box; the enforcement-rung and determinism framing are original to this repository. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
