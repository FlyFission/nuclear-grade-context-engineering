# Controlled items — bounded review evidence

| Item | Current state | Intended state | Owner | Evidence | Revalidation trigger |
|---|---|---|---|---|---|
| [Evaluation integrity](../../../docs/02-operating-system/evaluation-integrity.md) | general judge/budget doctrine | bounded usable/attempt/reserve and follow-up rules | change author | E-001 | budget or retry policy changes |
| [Panel skill](../../../skills/running-a-review-panel/SKILL.md) | source-verified dissent already present | explicit budget route and changed/missing-state follow-up | change author | E-001 | review protocol changes |
| [Proving claims skill](../../../skills/proving-claims/SKILL.md) | evidence custody and scope | stable hashes, actual ingress, honest derivation and parity guidance | change author | E-001 | proof boundary changes |

| [Generated panel card](../../../commands/ng-panel.md), [proof card](../../../commands/ng-prove.md) | generated from skill inputs | regenerated matching input routes | change author | E-001 | source skill changes |

| [Evidence badge](../../badge.json) | stale derived count after packet addition | regenerated 75 records / 42 open items | change author | E-002 | packet inventory changes |

| [Validator integration](../../../nuclear_grade/ng_validate.py), [CLI](../../../nuclear_grade/cli.py), [run checker](../../../nuclear_grade/review_run.py) | no pre-call run admission | opt-in versioned declared-budget gate | change author | E-003 | schema/CLI/admission changes |
| [Run templates](../../../templates/review-run/README.md), [behavior tests](../../../tests/test_review_run.py), [prompt fixture](../../../tests/fixtures/command_prompts.json) | no executable run protocol | actionable setup and accepted/rejected CLI regressions | change author | E-003 | protocol changes |

Base: origin/main 7f7e9bd. Installed source remains pinned to 3609ff2; these candidate edits are
isolated in a worktree and do not establish a new accepted baseline.

## Required links

- [Risk](risk.md), [basis](basis.md), [plan](plan.md), [trace](trace.md), [verification](verification.md), [ship](ship.md).
- [Controlled items](controlled-items.md), [operating lesson](opex.md).

## Exit criteria

The scoped wording passes the recorded checks and remains pending human PR review.

## Source-lineage note

An original operational refinement of existing evidence custody and evaluation discipline; see the repository [source map](../../../docs/00-standards-foundation/source-map.md). No compliance, independence, efficacy, or formal assurance claim.
