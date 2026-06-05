# Risk

## Change identity

- Slug: incorporate-planning-lessons
- PR / issue: #26
- Owner: maintainer
- Date: 2026-06-05
- Current lifecycle phase: Verify
- Summary: Fold a few generic, tool-agnostic planning lessons from an external review of 21 agent repos into existing controls, and record on the ledger what was deliberately declined. Four additive upgrades: a work-type lens (greenfield/brownfield/defect/refactor-migration) in `questioning-attitude`; a runtime blast-radius screen in `checking-what-a-change-affects`; delegable build-sequence slices in `plan.md` and `breaking-down-the-work`; and a named plan-phase vs build-phase authority boundary in the agent-authority model.

## Mission anchor

- Objective: Make planning sharper for brownfield changes and for delegated execution — the two thinnest spots in the current corpus — without adding always-on bulk.
- Success criteria: All gates green (pytest, ruff, `ng tokens`, `ng doctor`, `ng validate` on this packet); every edited skill keeps its 11-section contract and stays under the token budget; the work-type lens is orthogonal to Quick/Standard/Nuclear, not a competing mode; the decline decisions are recorded here.
- Non-goals / forbidden directions: Out of scope are all VS-Code-specific mechanics (custom agents, instructions files, prompt files, hooks JSON, plugins, cloud agent), a parallel specialist-subagent fan-out, a new scored eval harness, any new always-on skill, and any version bump. Forbidden is introducing the unbuilt `references/` skill-subfolder pattern.
- Drift check: re-anchor / escalate / stop when an edit stops serving brownfield or delegated-execution clarity.
- Traces to: the external 21-repo planning research and `.nuclear/charter.md` (rising standards, evidence over persuasion).

## Questioning-attitude summary

- Decision question: Of the research's ideas, which are generic gaps here versus already-present or tool-specific noise, and can the gaps be filled without bloat?
- Assumptions that changed the mode: The change edits a Core-7 always-on skill (`questioning-attitude`) and user-facing templates, so it is user-facing and lasting — a Standard change.
- Facts still needing validation: That the edits keep the token budget green (confirmed by `ng tokens`), keep the skill contract intact (confirmed by `test_skill_contracts.py`), and add no overclaiming language (confirmed by `test_public_docs.py`).
- Stop or hold conditions: Stop if any edit forces a skill rename, a new registered artifact, or a version-sync across files; none was needed.

## Affected configuration items

| Item | Type | Why it matters | Reference |
|---|---|---|---|
| questioning-attitude | Skill (Core 7) | Front-door work-type classification; ripples to every adopter | `skills/questioning-attitude/SKILL.md` |
| checking-what-a-change-affects | Skill | Adds runtime blast-radius screen | `skills/checking-what-a-change-affects/SKILL.md` |
| breaking-down-the-work | Skill | Points WBS leaves at delegable plan slices | `skills/breaking-down-the-work/SKILL.md` |
| standard plan template | Template | Build sequence gains slice columns | `templates/standard/plan.md` |
| cm change-impact template | Template | Adds a runtime/data blast-radius row | `templates/cm/change-impact.md` |
| golden-path questioning template | Template | Adds a work-type field | `templates/golden-path/questioning-attitude.md` |
| work-type lens doc | Docs (new) | Holds the four-type depth | `docs/02-operating-system/work-type-lens.md` |
| change-impact doc | Docs | Holds runtime blast-radius depth | `docs/02-operating-system/change-impact.md` |
| agent-authority model | Docs | Names plan-vs-build authority | `docs/04-adoption/agent-authority-model.md` |
| skill-evaluation prompts | Docs | Trigger prompts for the 3 edited skills | `docs/05-reference/skill-evaluation.md` |
| ng-question / ng-impact / ng-breakdown | Commands | Mirror the new lenses on the paste-ready surface | `commands/` |
| CHANGELOG.md | Docs | Records this change | `CHANGELOG.md` |
| rating-change-risk | Skill (Core 7) | Cross-links work type as orthogonal to mode | `skills/rating-change-risk/SKILL.md` |
| risk-tiers-and-modes doc | Docs | Points to the work-type lens from the mode side | `docs/02-operating-system/risk-tiers-and-modes.md` |
| docs index | Docs | Makes the work-type lens discoverable | `docs/README.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Edits a Core-7 always-on skill and public templates. |
| Reversibility | high | Markdown and template edits; revert the branch cleanly. No data migration. |
| Detectability | high | Contract, token, public-docs tests and the validator catch regressions. |
| Exposure | medium | Public repo; skill and template surface is agent-facing. |
| Uncertainty | low | Additive refinements within existing lifecycle beats. |
| Dependency trust | low | No new dependencies. |
| AI authority | low | No new agent write permissions; the authority note tightens, not loosens. |

## Selected mode

- **Mode:** Standard
- **Why this mode:** Edits a Core-7 always-on skill and user-facing templates that every adopter reads.
- **Why lighter mode is not enough:** Quick cannot record the adopt-vs-decline ledger or the claim-to-evidence mapping for a doctrine change.
- **Why heavier mode is not yet required:** Additive and non-breaking; no regulated use, safety basis, or new trust boundary.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| questioning-attitude.md | no | Captured inline in this risk record. | maintainer |
| basis.md | yes | Holds the adopt-vs-decline ledger. | maintainer |
| verification.md | yes | Per-claim evidence status plus a light efficacy note. | maintainer |
| ship.md | yes | Release decision and self-justification guard. | maintainer |
| turnover.md | no | Single-author packet. | maintainer |
| self-check.md | no | No high-consequence irreversible action. | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: Confirm each idea is a genuine gap, not already-present or tool-specific (recorded in `basis.md`).
- Minimum evidence before merge: pytest green; ruff clean; `ng tokens` and `ng doctor` OK; this packet validates; edited skills keep all 11 sections.
- Independent review needed? no for this PR; the adversarial review is recorded in `basis.md`.

## Required links

- Packet: `.nuclear/changes/incorporate-planning-lessons/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Mode is justified as Standard.
- The mission anchor names objective, success criteria, and non-goals.
- Claims map to evidence in `verification.md`.
- No hidden trigger for a stronger mode.

## Source-lineage note

Original Nuclear-grade packet influenced by public software-lifecycle and configuration-management practice mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
