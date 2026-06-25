# Standard Plan Template

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

**Activation threshold:** Use for Standard changes where the build has several steps, affected controlled items, dependency/model/tool decisions, rollback concerns, or a review order to plan.

**Minimum useful version:** the build sequence, the affected files and assets, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions you need to build and review the change without losing the intent.

---

## Change context

- Slug: pmbok-pmi-ai-crosswalk
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: graded rigor (Art. 9), operational unambiguity (Art. 12), boundary/no-overclaim discipline.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| (none) | — | — | — |

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Write the crosswalk doc | REQ-001, REQ-002 | research | `source-to-concept-crosswalk.md` (format) | `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md` | links resolve; boundary note present | doc complete |
| 2 | Source-governance updates | REQ-001, REQ-002 | step 1 | `source-map.md`, `do-not-cite-directly.md`, `compliance-boundaries.md` | edited governance docs | PMI excluded-direct rows present | done |
| 3 | Fold value/stakeholder/tailoring into 5 skills (bodies only) | REQ-003 | — | the 5 `SKILL.md` bodies | edited skills | descriptions + command cards unchanged | done |
| 4 | Name tailoring + discoverability links | REQ-001 | steps 1-3 | `risk-tiers-and-modes.md`, `enterprise-rollout.md`, `README.md` | edited docs | links resolve | done |
| 5 | Run repo gates | all | steps 1-4 | `ng doctor`, `gen-commands`, overclaim scan | gate output | all pass | done |

For any slice whose work is model-mediated, record its determinism posture — all steps here are human-authored prose edits; no model-mediated build step.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | research PMBOK/PMI; map to repo | findings sufficient |
| candidate | draft doc + edits | self-review against boundary |
| audit | run gates; verify no overclaim, flat cards | all gates pass |
| accept | commit, PR, human review | reviewer accepts boundary wording |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Skill fold-ins | Touching `description:` or `## Prompt` | Token burn; card churn | Body-only edits; verify diff | `git diff` shows no description change; cards unchanged |
| Crosswalk wording | Implying compliance | False assurance | Boundary note; overclaim scan | scan clean |

## Agent briefing

- Role: builder (this session)
- Authority source: approved plan (ExitPlanMode)
- Active procedure/template: Standard packet
- Last completed action if resumed: n/a
- Handoff or turnover needed? no
- Pause when unsure condition: any wording that could read as a compliance/conformance claim.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md` | new | REQ-001, REQ-002 | the bridge | Ben Huffer |
| `docs/00-standards-foundation/{source-map,do-not-cite-directly,compliance-boundaries}.md` | edit | REQ-001, REQ-002 | governance | Ben Huffer |
| 5 `skills/*/SKILL.md` | one-line body fold-ins | REQ-003 | gap-fills without token burn | Ben Huffer |
| `docs/02-operating-system/risk-tiers-and-modes.md`, `docs/04-adoption/enterprise-rollout.md`, `README.md` | edit | REQ-001 | name tailoring + discoverability | Ben Huffer |

## Non-goals

- No new skills, clusters, or templates.
- No reproduction of PMI/PMBOK text or structure derivation.
- No PMP/compliance/conformance positioning.

## Dependency / model / tool decisions

Use only if activated. — None.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..003 each one trigger→response, reviewed | pass |
| Design approved | Design outline in `basis.md` complete | pass |
| Tasks approved | Each build step carries its requirement IDs | pass |
| Specification reviewed | Protected/unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to a gate in `verification.md` | pass |
| Build complete | Files match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Residual risk + rollback recorded | pass |
| Turnover complete if activated | n/a | not applicable |

## Rollback approach

- Rollback method: `git revert` the PR; docs/skill edits are isolated.
- State/data reversal notes: none — no data or schema.
- Feature flag / kill switch: n/a.
- Owner: Ben Huffer.
- Time to restore estimate: minutes.

## Proof commands

```bash
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/pmbok-pmi-ai-crosswalk
python tools/ng.py gen-commands && git status --short commands/   # expect: empty
git diff -U0 skills/ | rg -i 'description:'                        # expect: empty
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: this PR; `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
