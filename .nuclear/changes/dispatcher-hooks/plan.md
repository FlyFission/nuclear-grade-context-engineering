# Standard Plan

**Purpose:** Bound the dispatcher-hooks work, its review, and its rollback.

---

## Change context

- Slug: dispatcher-hooks
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: graded rigor (advisory, opt-in for the in-session tier); honest reporting (the advisory honesty note).

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | n/a | n/a | n/a |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Confirm the hook I/O contract + F2/F4 hardening | REQ-001..004 | none | doc fetch with citations | contract known |
| 2 | Write the two static, zero-network hook scripts | REQ-001, REQ-002, REQ-003 | step 1 | smoke-run emits valid JSON | scripts work |
| 3 | Write HOOKS.md (declare + enable + honesty) | REQ-004 | step 2 | enable snippet present | doc complete |
| 4 | Add `tests/test_hooks.py` (ban, no-echo, firewall, sync, budget) | REQ-002..005 | step 2 | `pytest` green | tests pass |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | confirm the hook I/O contract | contract known |
| candidate | write scripts + HOOKS.md + tests | smoke-run + tests green |
| audit | full suite + ruff + doctor + tokens + validate | all green |
| accept | open PR; maintainer reviews the code + runs a live session | human review |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Writing executable hooks | A network call or a prompt echo slips in | Exfiltration / injection-laundering | network-ban + no-echo tests; revert on failure | `verification.md` |
| Shipping the hooks | Auto-activation by accident | No-hooks default broken | Ship no `hooks/hooks.json`; absence is the control | `verification.md` |

## Agent briefing

- Role: builder (drafting under review).
- Authority source: the approved plan; this packet.
- Active procedure/template: Standard packet.
- Last completed action if resumed: scripts + HOOKS.md + tests written and verified locally.
- Handoff or turnover needed? no
- Pause when unsure condition: pause if a hook would need the network, echo input, auto-activate, or block tools.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `hooks/session_start.py` | new | REQ-001, REQ-003 | the SessionStart injection | FlyFission |
| `hooks/user_prompt_submit.py` | new | REQ-002, REQ-003 | the per-prompt reminder | FlyFission |
| `HOOKS.md` | new | REQ-004 | declares + enables the hooks | FlyFission |
| `tests/test_hooks.py` | new | REQ-002..005 | guards the properties | FlyFission |

## Non-goals

- No `hooks/hooks.json` (would auto-activate; we keep hooks opt-in).
- No PreToolUse blocking gate or enforcement dial (a separate, higher-risk tier).
- No live Claude Code session run from this container.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..005 each a clear trigger→response, reviewed | pass |
| Design approved | two static scripts + HOOKS.md + tests | pass |
| Tasks approved | Build steps carry requirement IDs | pass |
| Specification reviewed | Protected and unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to evidence | pass |
| Build complete | The scripts + doc + tests match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risk + rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Rollback approach

- Rollback method: delete `hooks/`, `HOOKS.md`, and the test (single revert); adopters remove the settings.json entry.
- State/data reversal notes: none.
- Feature flag / kill switch: the hooks are inert unless wired into settings.json.
- Owner: FlyFission
- Time to restore estimate: minutes.

## Proof commands

```bash
echo '{"source":"startup"}' | python hooks/session_start.py
python -m pytest -q tests/test_hooks.py
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/dispatcher-hooks
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the approved revised dispatcher design + F2/F4.

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on human performance improvement and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
