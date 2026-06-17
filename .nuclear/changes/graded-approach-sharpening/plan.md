# Standard Plan Record

**Purpose:** Sequence the edits so each lands in the surface that already owns the concept, with no competing taxonomy and no new machinery.

**Activation threshold:** Standard mode: several controlled docs, a skill, the generated command card, the maxims, and the source map change together.

**Minimum useful version:** the build sequence, the affected files, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a doctrine change. Capture only the decisions needed to build and review it.

---

## Change context

- Slug: graded-approach-sharpening
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-17
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: Art. 9 (graded rigor), Art. 15 (two-speed control), Art. 3 (rising standards / no normalization), Art. 4 (formality).

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| Recording IAEA/CNSC/ONR as references (earlier packet's "never IAEA" non-goal) | User explicitly relaxed the policy for public nuclear sources, with legal caution | Concept-only / `public-url-needed` is the lightest way to honor the report's cross-jurisdiction substance | FlyFission approved |

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Name the administrative floor + tripwires | REQ-001, REQ-002 | adversarial review done | `activation-thresholds.md`, `modes.md`, `change-control-packets.md`, `risk-tiers-and-modes.md` | floor section, trigger row, shortcut, same-axis notes | manual read; doctor | Floor reads as completing "smallest mode," not contradicting it |
| 2 | Add floor screen + change-vs-item + performance history to the skill | REQ-001, REQ-004, REQ-005 | step 1 | `skills/rating-change-risk/SKILL.md` (Process, When Not to Use, Common Rationalizations, description) | edited skill | skill contract tests | `## Prompt` untouched; description 80–500 chars, no colon-space |
| 3 | Regenerate the command card | REQ-001 | step 2 | `nuclear-grade.yaml#command_map` | `commands/ng-classify.md` | `gen-commands --check` | "every command card matches its skill" |
| 4 | Non-waiver maxim + completion-standard consistency | REQ-003 | step 1 | `MAXIMS.md`, `AGENTS.md`, `CORE.md` | maxim + clarifying lines | `test_public_docs` | Maxim present; completion standard still satisfied by the commit message |
| 5 | Reconcile the public surfaces | REQ-001 | step 1 | `README.md`, `WORKFLOWS.md`, `QUICKSTART.md`, `glossary.md`, `templates/README.md` | one floor line each | doctor; `test_public_docs` | Wording varied per surface (redundancy gate) |
| 6 | Consolidate lineage | REQ-006 | step 1 | `source-to-concept-crosswalk.md`, `source-map.md`, `modes.md` | crosswalk rows; Tier 1b refs; posture line | doctor links; boundary read | DOE-anchored; refs concept-only / `public-url-needed` |
| 7 | CHANGELOG + this packet + verify end to end | all | steps 1–6 | `CHANGELOG.md`, this packet | entry + packet | suite + tokens + doctor + validate green | All checks pass; residual risk in `ship.md` |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | adversarial review of the proposal | confirm each item is a true value-add |
| candidate | draft all doc/skill edits | local read + contract tests |
| audit | regenerate card; run suite, tokens, doctor, validate | all green |
| accept | PR review | reviewer confirms wording + boundary |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Editing the skill description | Breach 500 chars or add a colon-space | Skill contract test fails | Measure before/after | `verification.md` |
| Naming the floor | Create a downgrade loophole | A trust-bearing change skips review | Dominant tripwires + non-waiver maxim + extended rationalizations | `verification.md` |
| Adding foreign sources | Imply compliance | Legal/trust harm | Concept-only / `public-url-needed`; catch-all disclaimer | `verification.md` |

## Agent briefing

- Role: doctrine author for the graded-approach sharpening.
- Authority source: user-approved plan; charter Art. 9/15.
- Active procedure/template: Standard packet.
- Last completed action if resumed: all edits made; card regenerated; suite green.
- Handoff or turnover needed? no.
- Pause when unsure condition: any edit that would need a new skill/command, a validator change, or a compliance claim.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `skills/rating-change-risk/SKILL.md` + `commands/ng-classify.md` | floor screen, change-vs-item, performance history, description | REQ-001, REQ-004, REQ-005 | Agents load it to choose rigor | FlyFission |
| `docs/02-operating-system/{activation-thresholds,modes,change-control-packets,risk-tiers-and-modes}.md` | floor + modulator + change-vs-item | REQ-001, REQ-002, REQ-004, REQ-005 | Mode/tier/threshold doctrine | FlyFission |
| `MAXIMS.md`, `AGENTS.md`, `CORE.md` | non-waiver maxim + consistency | REQ-003 | Quotable principles + completion standard | FlyFission |
| `README.md`, `WORKFLOWS.md`, `QUICKSTART.md`, `glossary.md`, `templates/README.md` | one floor line each | REQ-001 | Reader-facing consistency | FlyFission |
| `source-map.md`, `source-to-concept-crosswalk.md` | DOE-anchored lineage; concept-only refs | REQ-006 | Lineage discipline | FlyFission |

## Non-goals

- No A/B/C/D taxonomy, no new mode token, template mode, `--mode` choice, or validator/CLI change.
- No new standalone doctrine page; no reproduced regulator text; no compliance/assurance/legal claim.

## Dependency / model / tool decisions

Not activated.

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one trigger→response statement with a `REQ-NNN` ID | pass |
| Design approved | The design outline in `basis.md` is complete enough | pass |
| Tasks approved | Every build step carries its requirement IDs | pass |
| Specification reviewed | Protected outcomes, outcomes to prevent, and assumptions stated | pass |
| Tests/evals defined | Each piece of evidence maps to a claim | pass |
| Build complete | The affected files match the plan | pass |
| Verification complete | The evidence is linked in `verification.md` | pass |
| Release decision ready | Leftover risks and rollback recorded | pass |
| Turnover complete if activated | n/a — same owner | n/a |

## Rollback approach

- Rollback method: revert the branch commit; every change is text in version control.
- State/data reversal notes: none; no data, schema, or production state is touched.
- Feature flag / kill switch: not applicable.
- Owner: FlyFission.
- Time to restore estimate: one revert.

## Proof commands

```bash
python tools/ng.py gen-commands --check
python tools/ng.py tokens .
python tools/ng.py doctor .
python -m pytest -q
python -m ruff check .
python tools/ng.py validate .nuclear/changes/graded-approach-sharpening
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the uploaded deep-research report; the user-approved plan

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade plan record inspired by public sources on software lifecycle, configuration management, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
