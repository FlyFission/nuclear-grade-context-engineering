# Standard Plan

**Purpose:** Bound the dispatcher-skill edit, its review, and its rollback.

---

## Change context

- Slug: directive-dispatcher-skill
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: operational unambiguity (the classification is explicit); no-overclaim (advisory, not "enforce").

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | n/a | n/a | n/a |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Read the skill contract + token budget | REQ-004 | none | `test_skill_contracts.py` + `tokens.py` reviewed | rules known |
| 2 | Rewrite Overview + Process (classify-first + MUST trip-wire) in imperative voice | REQ-001, REQ-002 | step 1 | reads as directive; contract intact | sections updated |
| 3 | Strengthen Common Rationalizations + Red Flags with the classification traps | REQ-001 | step 2 | present in the skill | sections updated |
| 4 | Add the guard test | REQ-003 | steps 2-3 | `pytest` green | test passes |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | review contract / budget | rules known |
| candidate | edit the skill + add the test | reads directive |
| audit | full suite + ruff + doctor + tokens + validate | all green |
| accept | open PR; maintainer reviews wording + plans the A3 run | human review |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Editing an always-on skill | Over-budget body or broken contract → CI fails / bad load | Router degrades | `test_skill_contracts` + `test_tokens`; revert on failure | `verification.md` |
| Directive wording | Sounds like enforcement | Overclaim | Keep advisory voice; defer the lift to A3 | `verification.md` |

## Agent briefing

- Role: builder (drafting under review).
- Authority source: the approved plan; this packet.
- Active procedure/template: Standard packet.
- Last completed action if resumed: skill edited + guard test added + verified locally.
- Handoff or turnover needed? no
- Pause when unsure condition: pause if a step would add hooks, claim enforcement, or exceed budget.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `skills/using-nuclear-grade/SKILL.md` | edit | REQ-001, REQ-002, REQ-004 | the always-on router | FlyFission |
| `tests/test_skill_contracts.py` | edit | REQ-003 | guards the directive behavior | FlyFission |

## Non-goals

- No executable hooks, SessionStart, or PreToolUse behavior (a later, gated tier).
- No edits to other skills, and no change to the eval prompts (the A3 corpus is its own work).

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..004 each a clear trigger→response, reviewed | pass |
| Design approved | Five targeted edits + a guard test | pass |
| Tasks approved | Build steps carry requirement IDs | pass |
| Specification reviewed | Protected and unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to evidence | pass |
| Build complete | The skill + test match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risk + rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Rollback approach

- Rollback method: revert `skills/using-nuclear-grade/SKILL.md` and the test edit (single revert).
- State/data reversal notes: none.
- Feature flag / kill switch: revert restores the prior advisory router.
- Owner: FlyFission
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/directive-dispatcher-skill
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the approved dispatcher design.

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on human performance improvement and software lifecycle, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
