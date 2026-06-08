# Standard Plan

**Purpose:** Bound the plugin-packaging work, its review, and its rollback.

---

## Change context

- Slug: plugin-install-vehicle
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: operational unambiguity (a clear install contract); no-overclaim (honest wording).

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | n/a | n/a | n/a |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Confirm the current official plugin/marketplace schema | REQ-001 | none | claude-code-guide doc fetch with citations | schema fields confirmed |
| 2 | Write `plugin.json` + `marketplace.json` (no hooks) | REQ-001, REQ-003 | step 1 | manifests parse + match schema | manifests present |
| 3 | Add `test_plugin_packaging.py` (validity, version-sync, structure) | REQ-002, REQ-003 | step 2 | `pytest` green | test passes |
| 4 | Update INSTALL.md + README install | REQ-004 | step 2 | `test_public_docs` + `doctor` green | docs lead with the plugin |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | confirm the official schema | schema confirmed |
| candidate | write manifests + test | manifests parse |
| audit | run full suite + doctor + tokens + validate | all green |
| accept | open PR; maintainer live-install + review | human review + live `/plugin install` |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Writing the manifest | Wrong schema field → broken install | Adopters cannot install | Verify against official docs; parse + structure test; defer live install to maintainer | `verification.md` |

## Agent briefing

- Role: builder (drafting under review).
- Authority source: the approved plan; this packet.
- Active procedure/template: Standard packet.
- Last completed action if resumed: manifests + test written and verified locally.
- Handoff or turnover needed? no
- Pause when unsure condition: pause if a step would add executable hooks or a public enforcement claim.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `.claude-plugin/plugin.json` | new | REQ-001, REQ-002 | the plugin manifest | FlyFission |
| `.claude-plugin/marketplace.json` | new | REQ-001 | repo-as-marketplace | FlyFission |
| `tests/test_plugin_packaging.py` | new | REQ-002, REQ-003 | guards validity + drift | FlyFission |
| `INSTALL.md` | edit | REQ-004 | leads with the plugin | FlyFission |
| `README.md` | edit | REQ-004 | one-line install in Quick start | FlyFission |

## Non-goals

- No executable hooks, SessionStart, or PreToolUse behavior (a later tier).
- No change to the `ng` CLI, skill bodies, or command bodies.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..004 each a clear trigger→response, reviewed | pass |
| Design approved | Two manifests + auto-discovery; basis complete | pass |
| Tasks approved | Build steps carry requirement IDs | pass |
| Specification reviewed | Protected and unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to evidence | pass |
| Build complete | The affected files match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risk + rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Rollback approach

- Rollback method: delete `.claude-plugin/` and revert the INSTALL.md / README edits.
- State/data reversal notes: none (no state).
- Feature flag / kill switch: removing the marketplace/plugin manifest disables the install path.
- Owner: FlyFission
- Time to restore estimate: minutes (single revert).

## Proof commands

```bash
python -c "import json; json.load(open('.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json'))"
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/plugin-install-vehicle
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the approved plugin-packaging plan.

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on software lifecycle, configuration management, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
