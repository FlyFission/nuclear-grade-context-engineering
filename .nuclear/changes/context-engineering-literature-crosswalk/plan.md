# Standard Plan Template

**Purpose:** Bound the work so the build, the review, the verification, and the rollback are planned before the change grows.

**Activation threshold:** Use for Standard changes where the build has several steps, affected controlled items, dependency/model/tool decisions, rollback concerns, or a review order to plan.

**Minimum useful version:** the build sequence, the affected files and assets, the non-goals, the review checkpoints, the rollback approach, and the proof commands.

**Overhead trap:** Do not write a project plan for a small change. Capture only the decisions you need to build and review the change without losing the intent.

---

## Change context

- Slug: context-engineering-literature-crosswalk
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: graded rigor, operational unambiguity, boundary/no-overclaim discipline, fair representation of others' work.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| (none) | — | — | — |

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Write the crosswalk doc | REQ-001, REQ-002 | research of both public repos | `pmbok-pmi-ai-crosswalk.md` (format) | `docs/01-field-guide/context-engineering-literature-crosswalk.md` | links resolve; boundary note present | doc complete |
| 2 | Add two Tier 9 rows | REQ-004 | step 1 | `source-map.md` Tier 9 | edited source-map | verified-public rows present | done |
| 3 | Name the payload-component lens | REQ-002, REQ-003 | step 1 | `context-packs.md` §1 | edited doc | no schema/format change; lens only | done |
| 4 | Add "Blueprint and execute" catalog entry + section | REQ-001, REQ-002 | step 1 | `WORKFLOWS.md` catalog | edited doc | links resolve | done |
| 5 | Point durable-memory + roadmap at the survey's memory literature | REQ-001 | step 1 | `durable-memory.md`, `ROADMAP.md` | edited docs | links resolve | done |
| 6 | Discoverability link | REQ-001 | steps 1-5 | `docs/README.md` | edited index | link resolves | done |
| 7 | Run repo gates | all | steps 1-6 | `ng doctor`, `ng validate`, `gen-commands`, overclaim scan | gate output | all pass | done |

For any slice whose work is model-mediated, record its determinism posture — all steps here are human-approved prose edits authored in one session; no model-mediated build step in the shipped artifact.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | research both repos; map to repo surfaces | findings sufficient |
| candidate | draft doc + edits | self-review against boundary |
| audit | run gates; verify no overclaim, flat cards, packet valid | all gates pass |
| accept | commit, PR, human review | reviewer accepts boundary wording |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Crosswalk wording | Implying endorsement/affiliation/superiority | Misrepresentation; false assurance | Boundary note + "what not to claim"; overclaim scan | scan clean |
| Doc edits | Touching a `SKILL.md` or command card | Token burn; card churn | Docs-only change; verify diff | `git status skills/ commands/` empty |

## Agent briefing

- Role: builder (this session)
- Authority source: approved plan (ExitPlanMode) and the user's "continue" direction
- Active procedure/template: Standard packet
- Last completed action if resumed: n/a
- Handoff or turnover needed? no
- Pause when unsure condition: any wording that could read as endorsement, affiliation, superiority, or a standard we conform to.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `docs/01-field-guide/context-engineering-literature-crosswalk.md` | new | REQ-001, REQ-002 | the bridge | Ben Huffer |
| `docs/00-standards-foundation/source-map.md` | edit | REQ-004 | source governance | Ben Huffer |
| `docs/02-operating-system/context-packs.md` | edit | REQ-002, REQ-003 | payload-component lens | Ben Huffer |
| `WORKFLOWS.md` | edit | REQ-001, REQ-002 | Blueprint-and-execute pattern | Ben Huffer |
| `docs/02-operating-system/durable-memory.md`, `ROADMAP.md` | edit | REQ-001 | production-memory pointer | Ben Huffer |
| `docs/README.md` | edit | REQ-001 | discoverability | Ben Huffer |

## Non-goals

- No new skills, clusters, templates, or commands.
- No endorsement, affiliation, or superiority claim; no claim we implement/conform to the taxonomy or PRP as a standard.
- No change to any skill `description:` or generated command card.

## Dependency / model / tool decisions

Use only if activated. — None.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..004 each one trigger→response, reviewed | pass |
| Design approved | Design outline in `basis.md` complete | pass |
| Tasks approved | Each build step carries its requirement IDs | pass |
| Specification reviewed | Protected/unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to a gate in `verification.md` | pass |
| Build complete | Files match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Residual risk + rollback recorded | pass |
| Turnover complete if activated | n/a | not applicable |

## Rollback approach

- Rollback method: `git revert` the PR; docs and packet edits are isolated.
- State/data reversal notes: none — no data or schema.
- Feature flag / kill switch: n/a.
- Owner: Ben Huffer.
- Time to restore estimate: minutes.

## Proof commands

```bash
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/context-engineering-literature-crosswalk
python tools/ng.py gen-commands && git status --short commands/   # expect: empty
git status --short skills/                                        # expect: empty
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: this PR; `docs/01-field-guide/context-engineering-literature-crosswalk.md`

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
