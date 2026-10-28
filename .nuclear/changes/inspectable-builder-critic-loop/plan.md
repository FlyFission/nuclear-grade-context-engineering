# Plan: Inspectable builder-critic loop

## Change context

- Slug: `inspectable-builder-critic-loop`
- Related risk: `risk.md`
- Related basis: `basis.md`
- Owner: implementing agent; maintainer owns acceptance
- Date: 2026-08-06
- Current lifecycle phase: Execute

## Charter and anchor check

- Mission anchor confirmed before Plan: yes.
- Re-check before Verify: required.
- Charter articles: evidence over persuasion, no self-approval, controlled prompts/templates, bounded authority.
- Crossed non-goals: none.

## Build sequence

| # | Task / vertical slice | Reqs | Blocked by | Public seam | Outputs / artifact | Integrated proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | RED public contract for bounded non-authoritative cycle | REQ-001-004, REQ-006 | adversarial review | public docs/templates | failing test | targeted pytest | expected failure observed |
| 2 | Implement doctrine/template/briefing/source and pilot contract | REQ-001-004, REQ-006 | slice 1 | same public seam | docs/templates/skill | targeted test green | all required boundaries present |
| 3 | RED command propagation then update canonical prompt/golden/card | REQ-005 | slice 2 | command generator | prompt asset, fixture, card | parity tests | byte parity green |
| 4 | Fill packet and run integrated gates | all | slices 1-3 | repository checks | evidence records | full suite and tools | no unresolved P0/P1 |
| 5 | Independent review, commit, push, stacked PR | all | slice 4 | git/GitHub | draft PR | remote head and CI | maintainer review requested |

## Optional targeted improvement cycle for this implementation

- Task / intended outcome: add only mechanics that survive the adversarial transfer review.
- Build method and ownership: one sequential owner because doctrine, templates, prompt, and tests are coupled; independent reviewers inspect the final diff.
- Frozen inspectable bar: REQ-001 through REQ-006 and the failing public/parity tests.
- Bar custodian / change authority: FlyFission maintainer; implementing agent may propose but not weaken requirements.
- Critic inputs/artifact: exact base-to-head diff, packet, tests, and source links.
- Coupling profile: reviewer context separated; provider/model/orchestrator/resource coupling disclosed; not independent human validation.
- Iteration bound: at most two blocker-fix cycles; otherwise INCONCLUSIVE/BLOCKED.
- Integration observation: full repository checks and GitHub CI on exact head.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | research and adversarial review | no repo claim |
| candidate | TDD edits in isolated worktree | targeted tests |
| audit | full gates and independent review | no P0/P1 |
| accept | maintainer merge decision | separate from this agent |

## Affected files and assets

| File / asset | Change expected | Requirements | Owner |
|---|---|---|---|
| `WORKFLOWS.md` | optional Execute/Verify technique | REQ-001, REQ-003, REQ-004 | maintainer |
| briefing skill/prompt/generated command | bounded inputs and output contract | REQ-002, REQ-005 | maintainer |
| Standard plan/verification | bar/coupling/bounds/gap flow | REQ-001-004 | maintainer |
| pilot contract/source map | measured rollout and lineage | REQ-006 | maintainer |
| tests/fixtures | public and parity controls | all | maintainer |

## Non-goals

- No dedicated or promoted skill.
- No workflow catalog entry, lifecycle, mode, reviewer persona, or release gate.
- No live pilot execution or efficacy claim.
- No changes to PR #98 scope beyond using it as the stacked base.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | User authorized follow-up PR after adversarial review | pass |
| Transfer review | Three differentiated adversarial lenses completed | pass |
| RED observed | Public and command tests failed for missing behavior | pass |
| Focused GREEN | Targeted public and parity tests pass | pass |
| Full verification | pytest/Ruff/project gates/token budgets | planned |
| Independent diff review | spec and standards blockers resolved | planned |
| Release decision | maintainer only | planned |

## Rollback approach

- Rollback method: revert the follow-up branch/commit; no runtime state.
- Data reversal: none.
- Owner: FlyFission maintainer.

## Proof commands

```bash
python3 -m pytest -q
python3 -m ruff check .
python3 tools/ng.py doctor .
python3 tools/ng.py tokens .
python3 tools/ng.py eval .
python3 tools/ng.py gen-commands . --check
python3 tools/install-codex.py --check
python3 tools/ng.py validate .nuclear/changes/inspectable-builder-critic-loop

git diff --check
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- draft PR #98 as stacked base

## Exit criteria

- Every requirement traces to changed files and evidence.
- No duplicate workflow/skill/ledger or unsupported claim appears.
- Full local and remote gates are green before merge recommendation.

## Source-lineage note

This plan uses the public source boundary recorded in `docs/00-standards-foundation/source-map.md`. It creates no general efficacy, independence, compliance, formal verification, safety, security, certification, or release claim.
