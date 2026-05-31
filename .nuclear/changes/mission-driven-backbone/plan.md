# Plan

## Change context

- Slug: mission-driven-backbone
- Mode: Standard
- Owner: maintainer

## Charter and anchor check

A re-evaluated gate, not a one-time note. Confirm before Plan and re-check before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes.
- Re-checked before Verify? yes; scope held to the anchor, deferred items stayed deferred.
- Charter articles in play: Rising standards, Formality, Evidence over persuasion, Graded rigor.

If a non-goal or charter article must be crossed, record the justification here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | not applicable | not applicable | proceed |

## Build sequence

1. Author the two skills (`staying-on-mission`, `reviewing-code-quality`).
2. Author the two command prompts.
3. Add charter primitive (`.nuclear/charter.md`) and `init` writes for charter and mission anchor.
4. Add the Mission anchor section to `templates/standard/risk.md` and the drift gate to `templates/standard/plan.md`.
5. Add advisory validator checks (`_check_mission_anchor`, `_check_unresolved_clarifications`).
6. Retrofit cross-references (questioning-attitude, briefing-an-agent, checking-release-readiness, using-nuclear-grade, context-packs, WORKFLOWS).
7. Register both skills and commands (SKILLS.md, COMMANDS.md, nuclear-grade.yaml, skill-evaluation.md, results-summary.md, contract test sets).
8. Add validator and init tests.
9. Fill this dogfood packet; validate.

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Validator change | False-trigger on existing packets | CI breaks | Only-when-present pattern; run all packets | verification.md |
| Registration | Forget a coupled file | Contract test fails | doctor + contract tests before commit | verification.md |

## Affected files and assets

| File / asset | Change expected | Why it matters | Owner |
|---|---|---|---|
| `skills/*`, `commands/*` | New skills and commands | Core deliverable | maintainer |
| `nuclear_grade/*` | Advisory checks and init writes | Teeth and primitives | maintainer |
| `templates/standard/*` | Anchor section and gate | Per-change backbone | maintainer |

## Non-goals

- Changing the skill description rule or any other contract field.
- Making the anchor or charter a hard required gate.
- The evidence-coverage validator rule.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Skills and commands authored | Pass the contract sections | pass |
| Validator change | Existing packets still validate | pass |
| Registration complete | Contract and public-doc tests pass | pass |
| Packet validates | This packet passes the validator | pass |

## Rollback approach

- Rollback method: revert the branch commits; each piece is additive.
- State/data reversal notes: none; no data migrations.
- Feature flag / kill switch: not applicable; advisory checks are non-blocking.
- Owner: maintainer.
- Time to restore estimate: minutes (single revert).

## Proof commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/mission-driven-backbone
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Build sequence executed; tests green; packet validates.

## Source-lineage note

Original Nuclear-grade plan influenced by lifecycle and configuration-management concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
