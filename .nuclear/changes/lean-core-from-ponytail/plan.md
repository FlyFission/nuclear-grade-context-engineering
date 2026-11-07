# Plan: lean core, learned from Ponytail

## Change context

- Slug: lean-core-from-ponytail
- Related risk record: [`risk.md`](risk.md)
- Related basis record: [`basis.md`](basis.md)
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Current lifecycle phase: Plan

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes/no: yes, in `risk.md`.
- Re-checked before Verify? yes/no/not yet: not yet; this record stops at Plan.
- Charter articles in play: 9 graded rigor; 12 operational unambiguity; 15 two-speed control; 8 evidence over persuasion.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none planned | not applicable | not applicable | not applicable |

## Decision frontier

These are the choices only the owner can make. Mark each `approved`, `revised: ...`, or `held`. Build authority for Phase 1 opens when D2, D3, D4, and D8 are marked.

| ID | Decision | Recommendation | Alternatives | Owner mark |
|---|---|---|---|---|
| D1 | A persona image to compress the value system | hold until the card exists; candidate: "the engineer whose name goes on the work package" | no persona | held |
| D2 | The card at 400 words, tier one plus the trap sentence plus the receipt, replacing `AGENTS.md`'s body and the hook preamble (REQ-001) | approve | 600 words; keep the Core 7 pointer list as well | pending |
| D3 | Two agent-facing states, ordinary and promise, and the seven trap surfaces; "user-visible behavior" and "only docs" leave the list (REQ-003) | approve | keep eight surfaces (add user-visible behavior); keep docs | pending |
| D4 | Delete the per-prompt reminder hook (REQ-002) | approve | keep it but fire only when a trap path is in the diff | pending |
| D5 | Marker words `shortcut:` and `deferred:` (REQ-009) | approve both | one word | pending |
| D6 | Four-section skills at 600 words; Core 7 first (REQ-004) | approve | keep When Not to Use as a fifth section; 800 words | pending |
| D7 | One-file Quick and three-file Standard; three threshold dimensions; custody only for decisive claims under `--strict-custody` (REQ-005) | approve | keep six files, shrink each | pending |
| D8 | Non-inferiority margin: mean −0.05, single skill −0.17, routing recall not lower (REQ-007) | approve | stricter −0.03 / −0.10 | pending |
| D9 | Lenses and HPI screen become reference, not steps (REQ-010) | approve | keep the archetype floor as one line in the rating skill | pending |
| D10 | The other 24 skills: same four-section rewrite in a later record, or demote the ones with `observe` tier to docs | rewrite the ones with `block` or `warn`; demote `observe` | rewrite all | held |

## Build sequence

Each phase is its own record and pull request. A phase that fails its gate stops; earlier phases stay.

| # | Task / vertical slice | Reqs | Blocked by | Public seam | Inputs (`file#section`) + budget | Outputs / artifact | Integrated proof | Stop/done |
|---|---|---|---|---|---|---|---|---|
| 0 | This record: analysis, specification, plan, baseline numbers | all | none | none | `analysis.md`; the ladder report; `ng tokens`; 6k tokens | this packet | `ng validate` on this packet | owner marks the frontier |
| 1 | The card: write it; replace `AGENTS.md` body and `starter-kit/core/AGENTS.md`; receipt replaces the completion standard; `CORE.md` links to it; `card_max` budget | REQ-001, 003, 006, 011 | D2, D3 | the card file | `AGENTS.md`; `CORE.md#The Core 7`; Ponytail `AGENTS.md` as register reference; 4k tokens | `CORE-CARD.md`; edited `AGENTS.md`; budget line | `ng tokens .`; `pytest tests/test_public_docs.py`; maintainer read | card at or under 400 words |
| 1h | Hooks: delete `user_prompt_submit.py` and its wiring; `session_start.py` prints the card; parity test | REQ-002 | phase 1; D4 | hook stdout | the two hook files; `tests/test_hooks.py`; `HOOKS.md`; 2k tokens | one hook; `tests/test_card_parity.py`; `decision-authority.md` in that record | `pytest tests/test_hooks.py tests/test_card_parity.py`; `ng validate --strict-authority`; human merge | one hook, parity green |
| 2 | Skills: amend the authoring contract and contract tests to four sections and 600 words; rewrite `using-nuclear-grade` and `rating-change-risk` to the two states, then the other five Core skills; regenerate cards | REQ-003, 004, 008 | phase 1; D6, D8 | skill files and cards | each `SKILL.md`; the consolidation scenarios that needed it; 6k tokens per body | seven four-section bodies; amended contract; regenerated `commands/` | `pytest tests/test_skill_contracts.py`; `ng doctor .`; `ng tokens .`; then the REQ-007 re-run by a maintainer or CI | gates pass or the phase stops and reports |
| 3 | Records: one-file Quick and three-file Standard templates; `ng new` emits them; validator accepts both shapes; three-dimension screen; custody only for decisive claims under `--strict-custody`; lenses and HPI screen become reference | REQ-005, 010 | phase 1; D7, D9 | `ng new`, `ng validate` | `templates/`; `nuclear_grade/ng_validate.py`; `tests/test_ng_validate.py`; 6k tokens | new templates; validator change; tests | `pytest tests/test_ng_validate.py tests/test_two_party.py`; validate every existing record still passes | both shapes validate; existing records untouched |
| 4 | Markers and review: `ng debt`; review shape in the two review skills; grep-callers rule | REQ-008, 009 | phase 2; D5 | `ng debt` | the two skills; Ponytail `ponytail-review.toml` as shape reference; 3k tokens | `nuclear_grade/debt.py`; tests; edited skills | targeted pytest; routing cases for the two skills | tests green; recall unchanged |
| 5 | Deletion pass and report: the seven mode-rule restatements collapse to the card; disclaimer repeats collapse to `DISCLAIMER.md` plus one line in root files; refresh the token audit with before and after, including any score that fell | REQ-011, 010 | phases 1 to 4 | public docs | `ng tokens .#Repeated prose blocks`; link check; 2k tokens per page | edited pages; dated audit section | `pytest tests/test_public_docs.py`; link check; `ng tokens .` | always-on tokens under 1,500; mode rule in one place |

For any slice whose work is model-mediated, the determinism posture is: the card and skill text are drafted by a model and are not replayable; the parity, budget, contract, validator, and routing checks are deterministic; the control-ladder re-run uses the harness's recorded model, grader, and rubric and is replayable from its data files.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `CORE-CARD.md` (name open) | new | REQ-001, 003, 006 | the only always-on text | maintainer |
| `AGENTS.md`, `CLAUDE.md`, `starter-kit/core/AGENTS.md` | body replaced by the card; receipt replaces the completion standard | REQ-001, 006 | always-loaded | maintainer |
| `hooks/user_prompt_submit.py` | deleted | REQ-002 | the per-prompt nag | maintainer, human merge |
| `hooks/session_start.py`, `HOOKS.md`, `plugins/nuclear-grade-guard/hooks/` | print the card once | REQ-002 | gate hooks | maintainer, human merge |
| `docs/05-reference/skill-authoring-contract.md`, `tests/test_skill_contracts.py` | four sections, 600 words | REQ-004 | the structure is the bloat | maintainer |
| seven `skills/*/SKILL.md` under Core 7 | rewritten | REQ-003, 004, 008 | the operative surface | maintainer |
| `commands/*.md` | regenerated | REQ-008 | parity with skills | generated |
| `templates/quick/`, `templates/standard/`, `nuclear_grade/cli.py` (`ng new`) | one-file Quick, three-file Standard | REQ-005 | records at the size a person reads | maintainer |
| `nuclear_grade/ng_validate.py`, `tests/test_ng_validate.py` | accept both shapes; custody only for decisive claims under `--strict-custody` | REQ-005, 011 | trust surface; Standard by policy | maintainer |
| `nuclear_grade/debt.py`, `nuclear_grade/cli.py` | `ng debt` | REQ-009 | greppable deferrals | maintainer |
| `nuclear_grade/tokens.py` | `card_max`; always-on budget | REQ-001, 011 | the gate against creep | maintainer |
| `docs/02-operating-system/work-type-lens.md`, `archetype-lens.md`, `hpi-overlays.md` | reference, no longer required by any skill or template | REQ-010 | gates become pages | maintainer |
| `CORE.md`, `QUICKSTART.md`, root docs | link to the card; disclaimer repeats collapse | REQ-011 | one source | maintainer |
| `docs/05-reference/skills-token-audit.md` | dated refresh | REQ-007 | honest before and after | maintainer |

## Non-goals

- No skill merges; the consolidation protocol stands. Demotion of `observe`-tier skills to docs is D10, a later record.
- No change to what the validator, two-party check, gate, policy, or badge decide, beyond accepting the smaller record shapes.
- No new always-on text beyond the card.
- No public comparison claim against Ponytail.
- No change to `.nuclear/charter.md`.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | the owner marks D2, D3, D4, and D8; D5 to D7 and D9 before their phases | planned |
| Tests/evals defined | REQ-007 harness and margins recorded in this packet | pass |
| Build complete | per phase, in that phase's record | planned |
| Verification complete | per phase; REQ-007 re-run by a maintainer or CI | planned |
| Release decision ready | per phase `ship.md` | planned |

## Rollback approach

- Rollback method: revert the phase commit; the parity test and budgets make the reverted state checkable.
- State/data reversal notes: none; prose and tests only.
- Feature flag / kill switch: the hooks are opt-in; the validator accepts the old record shapes, so existing records and adopters are unaffected until they re-vendor.
- Owner: maintainer
- Time to restore estimate: minutes.

## Proof commands

```bash
python tools/ng.py validate .nuclear/changes/lean-core-from-ponytail
python tools/ng.py tokens .
python -m pytest -q tests/test_skill_contracts.py tests/test_public_docs.py
python tools/ng_skill_catalog_route_score.py
python tools/ng_policy_backtest.py --policy .nuclear/consequence-policy.json --last 49
# control-ladder re-run: evals/skill-control-ladder/scripts/, same model, grader, and rubric as REPORT.md
```

## Required links

- [`risk.md`](risk.md), [`basis.md`](basis.md), [`analysis.md`](analysis.md), [`trace.md`](trace.md), [`verification.md`](verification.md), [`ship.md`](ship.md)
- [`evals/skill-control-ladder/README.md`](../../../evals/skill-control-ladder/README.md)
- [`evals/skill-consolidation/REPORT.md`](../../../evals/skill-consolidation/REPORT.md)

## Exit criteria

- The work stayed inside the non-goals.
- Proof commands are recorded with results in `verification.md`.

## Source-lineage note

Original Nuclear-grade plan. Ponytail (MIT) is cited as a design influence. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
