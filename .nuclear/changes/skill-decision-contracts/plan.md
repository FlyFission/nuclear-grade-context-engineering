# Plan -- skill decision contracts

**Purpose:** Bound the build and review for the decision-contract change.

---

## Change context

- Slug: skill-decision-contracts
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-16
- Current lifecycle phase: Verify

## Charter and anchor check

A gate you check more than once, not a one-time note. Confirm it before Plan, and check it again before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: Art. 11 decision-question discipline, Art. 12 operational unambiguity, Art. 3 rising standards.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | no non-goal is crossed | n/a | FlyFission |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Define the block and classes in the authoring contract | REQ-001 | none | contract doc updated | the contract states the block and the classes |
| 2 | Add the block to all 27 skills | REQ-001 | step 1 | `ng decisions` lists 27 | every skill has a valid block |
| 3 | Enforce in the validator and tests, and add `ng decisions` | REQ-001, REQ-002, REQ-003 | step 2 | `pytest`, `ng doctor` | the gates are green |

## Two-speed work plan

Keep fast trial work apart from the slower gates where work is accepted.

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | draft the block format and the exemplars | the format is agreed |
| candidate | add blocks, wire the validator, build the rollup | local edits only |
| audit | run pytest, doctor, tokens, and decisions | all green |
| accept | human review and merge | reviewer approval |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Editing 27 skills | a generic or malformed block | weak signal or CI failure | exemplars, lint, and review | `ng decisions`, `pytest` |

## Agent briefing

- Role: implementing agent on branch `claude/practical-faraday-dwcv5b`.
- Authority source: the approved plan.
- Active procedure/template: the Standard packet.
- Last completed action if resumed: the validator and the rollup are wired.
- Handoff or turnover needed? no
- Pause when unsure condition: any skill that cannot name a non-generic decision.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `skills/*/SKILL.md` | add the block | REQ-001 | the core change | FlyFission |
| `nuclear_grade/cli.py` | enforce and add `ng decisions` | REQ-001, REQ-002 | the gate and the rollup | FlyFission |
| `tests/test_skill_contracts.py` | new assertions | REQ-001 | guards the contract | FlyFission |

## Non-goals

List what this change does not do, on purpose.

- Cutting, merging, or rewriting skills.
- Self-declaring a skill as deletable.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one clear trigger->response statement with a `REQ-NNN` ID, reviewed by a human. | pass |
| Design approved | The design outline in `basis.md` is complete enough for this change and reviewed. | pass |
| Tasks approved | Every build step carries the requirement IDs it delivers, and the sequence is reviewed. | pass |
| Specification reviewed | The protected outcomes, the outcomes to prevent, and the assumptions are stated plainly. | pass |
| Tests/evals defined | Each piece of evidence maps to a claim. | pass |
| Build complete | The affected files match the plan. | pass |
| Verification complete | The evidence is linked in `verification.md`. | pass |
| Release decision ready | The leftover risks and the rollback are recorded. | pass |
| Turnover complete if activated | The next owner has the state, the authority, the stop rules, and the work left to do. | not applicable |

## Rollback approach

- Rollback method: revert the branch commit; the change is text plus a lint.
- State/data reversal notes: none; no state or data is touched.
- Feature flag / kill switch: not applicable.
- Owner: FlyFission
- Time to restore estimate: minutes.

## Proof commands

```bash
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py decisions .
```

## Required links

- `risk.md`
- `basis.md` or `spec.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: reviewer feedback on decision artifacts

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade change record, influenced by public software-lifecycle and configuration-management ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
