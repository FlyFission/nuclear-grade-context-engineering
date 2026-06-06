# Basis

## Protected outcomes

- The repo stays lean: no new always-on skill, no new registered template or command, no `references/` pattern (its tooling is unbuilt — see the `skill-contract-modernization` ship record).
- The work-type lens stays orthogonal to the Quick/Standard/Nuclear rigor modes.
- All boundary wording stays inside its limits (no compliance or assurance overclaim).

## Requirements

- REQ-001: `questioning-attitude` names the work type (greenfield/brownfield/defect/refactor-migration) and the questions it forces, with a doc holding the depth.
- REQ-002: `checking-what-a-change-affects` and the cm template screen runtime/data blast radius (schema/state, API consumers, backward-compat, rollback-of-state), not just repo artifacts.
- REQ-003: `plan.md` build-sequence steps can carry prereqs, per-slice proof, and a stop/done condition so a step is a delegable handoff contract (not a schedule); `breaking-down-the-work` points leaves at those slices.
- REQ-004: the agent-authority model names the read-only plan phase vs the write-enabled build phase.
- REQ-005: `skill-evaluation.md` keeps >=3 trigger / >=2 near-miss prompts per edited skill, exercising the new behavior.
- REQ-006: this packet records the decision and validates clean.

## Adopt-vs-decline ledger

The external review studied 21 repos to design a VS-Code planning agent. This repo was one of the 21, cited as the exemplar for evidence-first operation. Most of the research only validated what is already here; the table records the disposition of every idea.

| Research idea | Disposition | Where it lands, or why declined |
|---|---|---|
| Grill / clarifying questions before planning | Already present | `questioning-attitude` (Core 7) |
| Spec packet with explicit sections | Already present | `templates/standard/` and `golden-path/` |
| Evidence-first / verification gates | Already present | `proving-claims`, `verification.md` |
| Decision records | Already present | `golden-path/decision.md`, `ship.md` |
| Compound learning (durable lesson per session) | Already present | `learning-from-experience`, `cm/opex.md` |
| Human approval at trust boundaries | Already present | `deciding-who-decides`, staged `plan.md` gates |
| Domain glossary | Already present | `docs/glossary.md` |
| Work-type lens (green/brown/defect/refactor) | Adopt (REQ-001) | `questioning-attitude` + `docs/02-operating-system/work-type-lens.md` |
| Brownfield / migration impact depth | Adopt (REQ-002) | `checking-what-a-change-affects` + cm template + change-impact doc |
| Execution-ready task slices | Adopt (REQ-003) | `plan.md` build-sequence columns + `breaking-down-the-work` |
| Read-only planner vs write implementer | Adopt, minimal (REQ-004) | named in `agent-authority-model.md`; kernel already in `CORE.md` |
| VS-Code mechanics (agents, instructions, prompts, hooks, plugins, cloud agent) | Decline | tool-specific; this repo is tool-agnostic markdown |
| Parallel specialist-subagent fan-out | Decline | harness-specific; overlaps `stress-testing-agent-changes`, `reviewing-code-quality`, `deciding-who-decides` |
| Standalone scored planning-eval harness | Decline (defer) | biggest, most meta lift; replaced by a light baseline-vs-skill note in `verification.md` |

## Assumptions

| Assumption | Why it matters | Validation source | Status |
|---|---|---|---|
| Editing a Core-7 skill needs no starter-kit body sync | Bounds the blast radius | Kits reference skills by pointer (`starter-kit/core/` has no SKILL bodies) | pass |
| `references/` tooling is unbuilt | Justifies inlining instead | `skill-contract-modernization` ship record names it a deferred follow-up | pass |
| Adding columns/rows keeps templates valid | Avoids a validator break | Validator checks sections, not columns; synthetic fixtures untouched | pass |

## Acceptance scenarios

- Given the prompt "add a field to the user record" on a live service, the revised front door classifies it brownfield and surfaces migration and rollback-of-state questions a generic plan would skip.
- Given a multi-agent build, each WBS leaf becomes a `plan.md` slice with prereqs, per-slice proof, and a stop condition.

## Required links

- `risk.md`
- `plan.md`
- `verification.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Every research idea has a recorded disposition.
- Each adopted requirement maps to evidence in `verification.md`.
- Declined ideas name why.

## Source-lineage note

Original Nuclear-grade basis record. The external review is treated as influence, not authority; public software-lifecycle and configuration-management lineage is mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
