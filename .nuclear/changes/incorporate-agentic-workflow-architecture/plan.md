# Plan — Incorporate Agentic Workflow Architecture

**Purpose:** Bound the build so the change tracks itself, breaks no CI, and stays inside the boundary.

---

## Change context

- Slug: `incorporate-agentic-workflow-architecture`
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Maintainer
- Date: 2026-06-16
- Current lifecycle phase: Plan

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: questioning attitude; rigor scales with consequence; no self-editable gates; honest claims.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| None | No non-goal or charter article is crossed | The change fits inside existing structure | Maintainer: proceed |

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Add the stage-contract template and the control/execution-plane doctrine doc; add glossary terms | REQ-002, REQ-003, REQ-004 | none | `templates/standard/wbs.md` (house style); `docs/04-adoption/agent-authority-model.md#rungs`; `docs/02-operating-system/context-window-discipline.md`; budget ~3k tokens read | `templates/standard/stage-contract.md`, `docs/02-operating-system/agentic-workflow-architecture.md`, glossary rows | files present; links resolve | done when both files exist and the doctrine names the boundary |
| 2 | Register the stage-contract template in the registry | REQ-002 | slice 1 file exists | `nuclear-grade.yaml#templates`; budget <1k | edited `nuclear-grade.yaml` | `ng doctor` passes | done when doctor is green |
| 3 | Wire the planner and the plan template to emit stage contracts | REQ-001 | slice 1 | `agents/planner.md#Do`; `templates/standard/plan.md#Build sequence`; budget ~2k | edited planner + plan template | `test_agents.py` green (tools unchanged) | done when slices carry inputs/outputs/budget |
| 4 | Reconcile vocabulary and name the trace bridge in the skills | REQ-004, REQ-005 | slice 1 | `skills/breaking-down-the-work#Process`; `skills/organizing-project-folders#Overview`; `skills/recording-what-an-agent-did#Process`; budget ~3k | three edited SKILL.md files | `test_skill_contracts.py` + `ng tokens` green | done when no conflicting definition remains |
| 5 | Add the discoverability surface and the coupled CI edits | REQ-006, REQ-007 | slices 1-4 | `WORKFLOWS.md#Workflow catalog`; `CORE.md#decision matrix`; `docs/02-operating-system/agentic-workflow-architecture.md` (§8); budget ~2k | catalog row + matrix trigger + the doctrine design-pass section | catalog/matrix rows present | done when the path is in the catalog, the matrix, and the doctrine |
| 6 | Add the preventive boundary test and the validators note; close this packet | REQ-007 | slices 1-5 | `tests/test_public_docs.py#BOUNDARY_PHRASES`; `docs/02-operating-system/validators.md#rule set`; budget ~2k | boundary test, validators note, filled packet | full local CI mirror + `ng validate` green | done when every gate passes |

For any slice whose work is model-mediated, record its **determinism posture**. This change was executed by an AI agent (model `claude-opus-4-8`, this session's instructions as the prompt). The edits themselves are deterministic artifacts under review; the drafting step is human-judgment-reviewed, not replayable. The gate of record is the human review plus the deterministic CI suite — not the model run.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | read repo, map the seam, enumerate coupled edits | none — read only |
| candidate | write files and edits on the branch | local tests pass |
| audit | run the full CI mirror; human reads the boundary wording | all gates green + human review |
| accept | merge the draft PR | human merge decision |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Add command card | Miss the hardcoded `EXPECTED_COMMANDS` edit | CI fails | Edit the test set in the same slice | `test_command_contracts.py` green |
| Write doctrine doc | Unbounded compliance wording | Over-claim | Boundary section + preventive test | boundary test green |
| Edit skill bodies | Break the 11-section or token contract | CI fails | Keep sections; run `ng tokens` | `test_skill_contracts.py` + tokens green |

## Agent briefing

- Role: builder (runner) executing an approved plan on the methodology repo.
- Authority source: approved plan in this packet; branch `claude/loving-dijkstra-kd8q14`.
- Active procedure/template: this `plan.md` and `templates/standard/stage-contract.md`.
- Last completed action if resumed: discoverability surface and coupled edits added.
- Handoff or turnover needed? no.
- Pause when unsure condition: stop if a change would need a new skill, a 6th cluster, or unbounded wording.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `agents/planner.md` | Slices become stage contracts | REQ-001 | Moves scoping in front of the gate | Maintainer |
| `templates/standard/plan.md` | Build-sequence gains contract columns | REQ-001 | Captures the contract for review | Maintainer |
| `templates/standard/stage-contract.md` | New template | REQ-002 | The reusable artifact | Maintainer |
| `docs/02-operating-system/agentic-workflow-architecture.md` | New doctrine | REQ-003 | The "why" and the boundary | Maintainer |
| `skills/*` (three) | Vocabulary + trace bridge | REQ-004, REQ-005 | One coherent pattern | Maintainer |
| `nuclear-grade.yaml`, `WORKFLOWS.md`, `CORE.md`, `docs/02-operating-system/agentic-workflow-architecture.md` (§8) | Register + discover | REQ-006 | Findable path | Maintainer |
| `tests/test_command_contracts.py`, `tests/test_public_docs.py`, `docs/02-operating-system/validators.md` | Coupled edits + preventive control | REQ-007 | Green CI + guarded boundary | Maintainer |

## Non-goals

- Adding a new `designing-agentic-workflows` skill or a sixth cluster.
- Adding validator code for stage contracts, a worked example, or an eval case in this change.
- Claiming folders replace durable runtimes, or any compliance/certification.

## Dependency / model / tool decisions

Not applicable — no new dependency, model, or tool is introduced.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one trigger→response statement with a `REQ-NNN` ID, human-reviewed. | pass |
| Design approved | The design outline in `basis.md` is complete enough and reviewed. | pass |
| Tasks approved | Every build step carries the requirement IDs it delivers. | pass |
| Specification reviewed | Protected outcomes, outcomes to prevent, and assumptions are stated. | pass |
| Tests/evals defined | Each piece of evidence maps to a claim. | pass |
| Build complete | The affected files match the plan. | pass |
| Verification complete | The evidence is linked in `verification.md`. | pass |
| Release decision ready | The leftover risks and the rollback are recorded. | pass |
| Turnover complete if activated | Not activated. | not applicable |

## Rollback approach

- Rollback method: revert the branch commits; all edits are additive markdown plus a few registry/test lines.
- State/data reversal notes: none — no state or data is changed.
- Feature flag / kill switch: not applicable for documentation.
- Owner: Maintainer.
- Time to restore estimate: under 10 minutes (git revert).

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/incorporate-agentic-workflow-architecture
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: this branch's draft PR

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade change record. The stage-contract columns adapt the Model Workspace Protocol (arXiv:2603.16021); the rung and determinism framing are original. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
