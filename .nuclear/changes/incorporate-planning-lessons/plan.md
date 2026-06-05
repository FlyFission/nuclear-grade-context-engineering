# Plan

## Change context

- Slug: incorporate-planning-lessons
- Owner: maintainer
- Date: 2026-06-05
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: rising standards, evidence over persuasion, graded rigor.

## Build sequence

This packet dogfoods the new slice columns: each step is a delegable handoff contract with its prereqs, the proof that closes it, and a stop/done condition. It is a handoff contract, not a schedule.

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Work-type lens in skill + golden-path field + new doc | REQ-001 | none | `ng tokens` green; 11 sections kept | lens in Process+Outputs and doc exists |
| 2 | Runtime blast-radius in skill + cm template + impact doc | REQ-002 | none | template parses; doc renders | runtime row + skill step + doc subsection present |
| 3 | Slice columns in plan template + breaking-down pointers | REQ-003 | none | skills keep sections | slice columns + handoff pointers present |
| 4 | Name plan-vs-build authority in agent-authority model | REQ-004 | none | docs read cleanly | subsection present |
| 5 | Refresh skill-evaluation prompts for 3 edited skills | REQ-005 | steps 1-3 | `test_skill_contracts.py` green | each block keeps >=3 / >=2 |
| 6 | Record this packet | REQ-006 | steps 1-5 | `ng validate` green on packet | packet validates clean |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `skills/questioning-attitude/SKILL.md` | add work-type step + output | REQ-001 | Core-7 front door | maintainer |
| `skills/checking-what-a-change-affects/SKILL.md` | add runtime screen | REQ-002 | impact discipline | maintainer |
| `skills/breaking-down-the-work/SKILL.md` | add slice pointers | REQ-003 | delegation legibility | maintainer |
| `templates/standard/plan.md` | add slice columns | REQ-003 | handoff contract | maintainer |
| `templates/cm/change-impact.md` | add runtime row | REQ-002 | blast radius | maintainer |
| `docs/02-operating-system/work-type-lens.md` | new doc | REQ-001 | lens depth | maintainer |

## Non-goals

- No new always-on skill, registered template, or command.
- No version bump and no `references/` subfolders.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each REQ is a clear trigger-to-response statement, human-reviewed. | pass |
| Tasks approved | Every build step carries its requirement IDs and a stop condition. | pass |
| Build complete | Affected files match the plan. | pass |
| Verification complete | Evidence linked in `verification.md`. | pass |
| Release decision ready | Leftover risk and rollback recorded in `ship.md`. | pass |

## Rollback approach

- Rollback method: revert the branch; all edits are markdown/template.
- State/data reversal notes: none — no data or schema change.
- Feature flag / kill switch: not applicable — doctrine content.
- Owner: maintainer.
- Time to restore estimate: minutes (single revert).

## Proof commands

```bash
python -m pytest -q
ruff check .
python tools/ng.py tokens .
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/incorporate-planning-lessons
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The work is bounded; non-goals keep scope from creeping.
- Review checkpoints are named and passed.
- Rollback is thought through before release.

## Source-lineage note

Original Nuclear-grade plan record influenced by public software-lifecycle and release-readiness practice mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
