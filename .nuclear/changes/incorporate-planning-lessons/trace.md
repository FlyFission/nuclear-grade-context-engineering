# Trace

## What was done

| Step | Requirement | Action taken | Files touched |
|---|---|---|---|
| 1 | REQ-001 | Added a work-type classification clause to Process step 4 and an Outputs bullet; added a golden-path `Work type` field; created the lens doc | `skills/questioning-attitude/SKILL.md`, `templates/golden-path/questioning-attitude.md`, `docs/02-operating-system/work-type-lens.md` |
| 2 | REQ-002 | Added a runtime blast-radius clause to Process step 1 and a When-to-Use bullet; added a runtime/data row to the cm template; added a runtime subsection to the impact doc | `skills/checking-what-a-change-affects/SKILL.md`, `templates/cm/change-impact.md`, `docs/02-operating-system/change-impact.md` |
| 3 | REQ-003 | Added prereqs/proof/stop columns and a handoff-contract note to the build sequence; added a slice pointer to the WBS skill Process and Outputs | `templates/standard/plan.md`, `skills/breaking-down-the-work/SKILL.md` |
| 4 | REQ-004 | Added a "Plan-phase vs build-phase authority" subsection before Exit criteria | `docs/04-adoption/agent-authority-model.md` |
| 5 | REQ-005 | Added one trigger prompt to each of the three edited skill blocks | `docs/05-reference/skill-evaluation.md` |
| 6 | REQ-006 | Wrote this packet | `.nuclear/changes/incorporate-planning-lessons/` |
| 7 | REQ-001/002/003 | Mirrored the lenses on the command surface; added a CHANGELOG entry | `commands/ng-question.md`, `commands/ng-impact.md`, `commands/ng-breakdown.md`, `CHANGELOG.md` |
| 8 | REQ-001 | Adversarial-review follow-up: cross-linked the work-type lens from the mode side to guard work-type/mode confusion | `docs/02-operating-system/risk-tiers-and-modes.md`, `skills/rating-change-risk/SKILL.md`, `docs/README.md` |
| 9 | — | Addressed PR #26 Copilot review: filled the PR number, corrected the stale CHANGELOG follow-up, and used the concrete mode name (Quick/Standard/Nuclear) | `risk.md`, `ship.md`, `docs/02-operating-system/work-type-lens.md`, `skills/questioning-attitude/SKILL.md` |
| 10 | REQ-001 | Addressed PR #26 Codex review: made the work-type lens additive (types can overlap; ask the union of questions) so one label cannot excuse another's questions | `skills/questioning-attitude/SKILL.md`, `docs/02-operating-system/work-type-lens.md`, `templates/golden-path/questioning-attitude.md`, `commands/ng-question.md` |
| 11 | REQ-001 | Codex follow-up: gave the golden-path template a Work-type questions section and exit criterion so a packet captures the union of forced questions, not just the labels | `templates/golden-path/questioning-attitude.md` |

## Decisions during execution

- Inlined depth into skill bodies plus docs rather than `references/` subfolders, because the `references/` tooling is unbuilt and the additions fit the token budget.
- Extended `plan.md` columns instead of creating an `execution-slices.md` template, to avoid overlap with `briefing-an-agent` and `handing-off-work` and to avoid new validator/manifest surface.
- Kept the runtime impact to one gated row plus doc depth, to respect the change-impact template's overhead trap.

## Required links

- `plan.md`
- `verification.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Every executed step maps to a requirement and the files it touched.
- Execution decisions that shaped the result are recorded.

## Source-lineage note

Original Nuclear-grade trace record influenced by configuration-management and agent-trace practice mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
