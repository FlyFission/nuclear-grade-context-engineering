# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim | Result status | Evidence link | Notes |
|---|---|---|---|
| C-001 charter + init write | pass | `../../charter.md`; `../../../nuclear_grade/cli.py` | `init` writes charter and mission; covered by `test_init_creates_charter_and_mission_anchor`. |
| C-002 mission anchor section | pass | `../../../templates/standard/risk.md` | Section present after Change identity; workspace template in `MISSION_TEMPLATE`. |
| C-003 staying-on-mission skill | pass | `../../../skills/staying-on-mission/SKILL.md` | 11 sections; description 143 chars; counted 3-attempt trigger and Rickover principles present. |
| C-004 reviewing-code-quality skill | pass | `../../../skills/reviewing-code-quality/SKILL.md` | 11 sections; description 155 chars; delete-first, tripwires, single verdict present. |
| C-005 two commands | pass | `../../../commands/ng-drift-check.md`; `../../../commands/ng-code-review.md` | 10 sections each; contain "portable command prompt"; no "slash command". |
| C-006 advisory validator checks | pass | `../../../nuclear_grade/ng_validate.py` | Mission-anchor check only-when-present; clarification-marker check; new tests pass; all existing packets still validate. |
| C-007 drift gate in plan template | pass | `../../../templates/standard/plan.md` | Charter-and-anchor check with justification table. |
| C-008 retrofits + registration | pass | `../../../SKILLS.md`; `../../../COMMANDS.md`; `../../../nuclear-grade.yaml`; `../../../docs/05-reference/skill-evaluation.md` | Contract and public-doc tests pass; doctor OK. |

## Reproduction commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/mission-driven-backbone
for p in .nuclear/changes/*; do python tools/ng.py validate "$p"; done
```

## Known gaps and deferrals

- The charter and mission anchor are advisory, not blocking gates. Recorded as `deferred`: hard enforcement is a future, breaking decision.
- The contract-evolution items (description-rule change, progressive disclosure, evidence-coverage check) are `deferred` to separate PRs.
- CI has not run at packet-authoring time; it is the public evidence for the matrix and wheel jobs.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Every claim has a recorded status.

## Source-lineage note

Original Nuclear-grade verification record influenced by graded-rigor evidence concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
