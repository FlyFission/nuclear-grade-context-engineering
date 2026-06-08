# Standard Plan

**Purpose:** Bound the PROVE-pipeline work, its review, and its rollback.

---

## Change context

- Slug: prove-pipeline
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: graded rigor (Standard+-only); honest reporting (the not-a-perimeter caveat).

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | n/a | n/a | n/a |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Confirm the subagent frontmatter schema + the F6 limit | REQ-001, REQ-002 | none | doc fetch with citations | schema known |
| 2 | Write the five agent defs with authority-encoding tools + baton contract | REQ-001, REQ-002, REQ-003 | step 1 | frontmatter valid; tools match the table | defs present |
| 3 | Write `agents/README.md` (baton pass + honesty caveat) | REQ-004 | step 2 | caveat present | README complete |
| 4 | Add `tests/test_agents.py` | REQ-001, REQ-002, REQ-004 | step 2-3 | `pytest` green | tests pass |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | confirm the subagent schema | schema known |
| candidate | write the defs + README + tests | frontmatter valid |
| audit | full suite + ruff + doctor + tokens + validate | all green |
| accept | open PR; maintainer reviews the authority model | human review |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Writing the agent tools | Tools contradict the stated authority | The split becomes a fiction | authority-split test; revert on failure | `verification.md` |
| Writing the README | Advertising a perimeter | Overclaim | "not a perimeter" + F6 caveat; caveat test | `verification.md` |

## Agent briefing

- Role: builder (drafting under review).
- Authority source: the approved plan; this packet.
- Active procedure/template: Standard packet.
- Last completed action if resumed: five defs + README + tests written and verified.
- Handoff or turnover needed? no
- Pause when unsure condition: pause if a def would claim confinement the packaging cannot deliver.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `agents/planner.md` … `educator.md` | new | REQ-001, REQ-002, REQ-003 | the five PROVE stages | FlyFission |
| `agents/README.md` | new | REQ-004 | baton pass + honesty | FlyFission |
| `tests/test_agents.py` | new | REQ-001, REQ-002, REQ-004 | guards the pipeline | FlyFission |

## Non-goals

- No executable hooks; no in-session blocking.
- No claim of real `permissionMode` confinement from the plugin (F6).
- No always-on fan-out (Standard+ only).

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..004 each a clear trigger→response, reviewed | pass |
| Design approved | five defs + README + tests | pass |
| Tasks approved | Build steps carry requirement IDs | pass |
| Specification reviewed | Protected and unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to evidence | pass |
| Build complete | The defs + README + tests match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risk + rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Rollback approach

- Rollback method: delete `agents/` and the test (single revert); no state.
- State/data reversal notes: none.
- Feature flag / kill switch: the subagents are inert unless dispatched; deleting `agents/` removes them.
- Owner: FlyFission
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q tests/test_agents.py
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/prove-pipeline
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the approved plan (Phase 4).

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on configuration management and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
