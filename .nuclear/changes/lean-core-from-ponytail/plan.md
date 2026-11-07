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

These are the choices only the owner can make. Mark each `approved`, `revised: ...`, or `held`. Build authority for Phase 1 opens when D2 to D4 and D6 to D8 are marked. D1, D5, and D9 can wait.

| ID | Decision | Recommendation | Alternatives | Owner mark |
|---|---|---|---|---|
| D1 | A persona image to compress the value system, as "the lazy senior dev" does for Ponytail | hold until Phase 1 text exists; candidate: "the engineer whose name goes on the work package", because accountability staying with a person is the one idea no model release moves (`POSITIONING.md`) | no persona; "the shift supervisor"; "the QA inspector" | held |
| D2 | The rigor ladder, six rungs, stop at the first that holds: (1) administrative floor, the commit message is the record; (2) proof already exists, point at it; (3) one command proves it, run it; (4) Quick record; (5) a trap fired, Standard record; (6) irreversible or trust-bearing, a person decides | approve the rungs; wording is Phase 1 | five rungs (drop 2); seven (split 6 into panel and human) | pending |
| D3 | The floor, five items, never waived (REQ-005) | approve | four (fold the receipt into item 2); six (add "read before you write") | pending |
| D4 | The receipt, five lines in fixed order (REQ-006) | approve | three lines (Changed / Proof / Not checked) | pending |
| D5 | Marker words for deferred evidence (REQ-009) | recognize both `shortcut:` and `deferred:`; Ponytail users keep theirs | one word only; none | pending |
| D6 | Core body budget 1,200 tokens each, 8,500 total (REQ-003) | approve; current p95 is 3,212 and the five-bullet arm scored within 0.062 at about 170 tokens | 900 / 6,500 (tighter); 1,600 / 11,000 (safer) | pending |
| D7 | The card replaces the hook preamble, with a parity test (REQ-002) | approve; the hook phase is its own record with `decision-authority.md` and a human merge | leave the hook text as is and test only `AGENTS.md` parity | pending |
| D8 | Non-inferiority margin: mean −0.05, single skill −0.17, routing recall not lower (REQ-007) | approve; −0.17 is one scenario moving from YES to PARTIAL in a three-trial mean | −0.03 / −0.10 (stricter); mean only | pending |
| D9 | Whether the 24 non-Core skills follow the same budget in a later record | yes, after Phase 2 reports | Core only | held |

## Build sequence

Each phase is its own record and pull request. A phase that fails its gate stops; earlier phases stay.

| # | Task / vertical slice | Reqs | Blocked by | Public seam | Inputs (`file#section`) + budget | Outputs / artifact | Integrated proof | Stop/done |
|---|---|---|---|---|---|---|---|---|
| 0 | This record: analysis, specification, plan, baseline numbers | all | none | none | `analysis.md`; `evals/skill-control-ladder/REPORT.md#Secondary comparisons`; `ng tokens` output; 6k tokens | this packet | `ng validate` on this packet | owner marks the frontier |
| 1 | The card and its renders: write the card; render into `AGENTS.md`, `starter-kit/core/AGENTS.md`, `CORE.md` summary; add `card_max` and the parity test; update the completion standard to the receipt | REQ-001, 002, 005, 006, 010 | D2, D3, D4, D6, D8 | the card file | `CORE.md#The Core 7`; `hooks/session_start.py#PREAMBLE`; `AGENTS.md#Completion standard`; 4k tokens | `CORE-CARD.md` (name open); edited `AGENTS.md`; `tests/test_card_parity.py`; budget line in `tokens.py` | `pytest tests/test_card_parity.py tests/test_public_docs.py`; `ng tokens .` green; maintainer read of the card | card at or under 600 words; parity test green |
| 1h | Hook render: replace the `session_start.py` preamble and the `user_prompt_submit.py` line with the card's renders | REQ-002 | phase 1; D7 | the hook stdout | the two hook files; `tests/test_hooks.py`; 2k tokens | edited hooks; `decision-authority.md` in that record | `pytest tests/test_hooks.py`; `ng validate --strict-authority`; human merge | parity test covers the hooks |
| 2 | Lean Core 7 bodies: rewrite `using-nuclear-grade` and `rating-change-risk` first (mode owners), then the other five; regenerate cards; add `core_skill_body_max` | REQ-003, 004, 011 | phase 1; D6, D8 | the skill files and generated cards | each `SKILL.md`; the consolidation scenarios that needed that skill; `skill-authoring-contract.md#Writing rules`; 6k tokens per body | seven lean bodies; regenerated `commands/`; budget lines | `pytest tests/test_skill_contracts.py`; `ng doctor .`; `ng tokens .`; `ng gen-commands` parity; then the REQ-007 re-run by a maintainer or CI | ladder and routing gates pass, or the phase stops and reports |
| 3 | Review shape and markers: `reviewing-code-quality` and `checking-release-readiness` adopt the finding shape; `ng debt` harvester; marker test | REQ-008, 009 | phase 2; D5 | `ng debt` CLI; the two skills | the two `SKILL.md#Process` and `#Prompt`; Ponytail `commands/ponytail-review.toml` as the reference shape; 3k tokens | edited skills and cards; `nuclear_grade/debt.py`; `tests/test_debt.py` | targeted pytest; `ng doctor .`; routing cases for the two skills | tests green; routing recall for both skills unchanged |
| 4 | Deletion pass on doctrine: collapse the seven mode-rule restatements to the card plus links; make every `docs/02-operating-system/` page reachable or archive it; remove repeated blocks `ng tokens` flags | REQ-011, 010 | phase 1 | public docs | `ng tokens .#Repeated prose blocks`; link check; one page per sitting | edited or moved pages; reachability test | `pytest tests/test_public_docs.py`; link check; `ng tokens .` | every page reachable; mode rule in one place |
| 5 | Report: refresh `skills-token-audit.md` with before and after, including any score that fell | REQ-007, 010 | phases 2 to 4 | the audit page | the two eval reports; `ng tokens` before and after; 2k tokens | a dated refresh section | maintainer read | published with limits stated |

For any slice whose work is model-mediated, the determinism posture is: the lean text is drafted by a model and is not replayable; the parity, budget, contract, and routing checks are deterministic; the control-ladder re-run uses the harness's recorded model, grader, and rubric and is replayable from its data files.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `CORE-CARD.md` (name open) | new | REQ-001, 005, 006 | the one source | maintainer |
| `AGENTS.md`, `starter-kit/core/AGENTS.md` | render the card; receipt replaces the completion standard | REQ-002, 006 | always-loaded | maintainer |
| `hooks/session_start.py`, `hooks/user_prompt_submit.py` | render the card | REQ-002 | gate hooks, human merge | maintainer |
| seven `skills/*/SKILL.md` under Core 7 | rewrite to budget and register | REQ-003, 004, 008 | the operative surface | maintainer |
| `commands/*.md` | regenerated | REQ-008 | parity with skills | generated |
| `nuclear_grade/tokens.py`, `tests/test_skill_contracts.py`, new `tests/test_card_parity.py` | budgets and parity | REQ-002, 003 | the gate that stops regression | maintainer |
| `nuclear_grade/debt.py`, `nuclear_grade/cli.py` | `ng debt` | REQ-009 | greppable deferrals | maintainer |
| `CORE.md`, `QUICKSTART.md`, `docs/02-operating-system/*` | link, trim, or archive | REQ-011 | one source | maintainer |
| `docs/05-reference/skills-token-audit.md` | dated refresh | REQ-007 | honest before and after | maintainer |

## Non-goals

- No skill merges or deletions; the consolidation protocol stands.
- No change to the validator's checks, the two-party rule, or custody fields.
- No new always-on text beyond the card.
- No public comparison claim against Ponytail.
- No change to `.nuclear/charter.md`.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | the owner marks D2 to D4 and D6 to D8 | planned |
| Tests/evals defined | REQ-007 harness and margins recorded in this packet | pass |
| Build complete | per phase, in that phase's record | planned |
| Verification complete | per phase; REQ-007 re-run by a maintainer or CI | planned |
| Release decision ready | per phase `ship.md` | planned |

## Rollback approach

- Rollback method: revert the phase commit; the parity test and budgets make the reverted state checkable.
- State/data reversal notes: none; prose and tests only.
- Feature flag / kill switch: the hooks are opt-in; adopters who vendored old bodies are unaffected until they re-vendor.
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
