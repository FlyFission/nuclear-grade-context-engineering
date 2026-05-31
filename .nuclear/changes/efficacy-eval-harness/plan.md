# Plan

## Change context

- Slug: efficacy-eval-harness
- Mode: Standard
- Owner: maintainer

## Charter and anchor check

A re-evaluated gate, not a one-time note. Confirm before Plan and re-check before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes.
- Re-checked before Verify? yes; scope held to a presence-check harness; the comparison-mechanization temptation stayed a non-goal.
- Charter articles in play: Evidence over persuasion, Rising standards, Questioning attitude, Formality.

If a non-goal or charter article must be crossed, record the justification here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | not applicable | not applicable | proceed |

## Build sequence

1. Add `nuclear_grade/efficacy.py`: stdlib loader and scorer over real artifacts.
2. Author three JSON eval cases (U02, U04, U07) with signals grounded in each scenario's stated risks.
3. Wire an `eval` subcommand into `nuclear_grade/cli.py`.
4. Write `efficacy-harness.md` with explicit what-it-measures and what-it-does-not boundaries; link it from the comparison README and results-summary, and add `eval` to the CLI reference.
5. Add `tests/test_efficacy.py` including a teeth test that proves the harness can fail.
6. Run the gate (ruff, pytest, doctor, validate) and a clean-venv wheel build; fill this packet.

## Non-goals

- Mechanizing the simple-versus-Nuclear-grade score table.
- Scoring a live model or claiming an A/B result.
- Adding any runtime dependency.
- Expanding to all 20 trials at shallow depth.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Harness scores real artifacts | `ng eval .` returns coverage | pass |
| Harness has teeth | A stripped section fails the case | pass |
| Zero runtime deps | Clean-venv wheel install works | pass |
| Boundary doc | States non-assurance limits | pass |
| Packet validates | This packet passes the validator | pass |

## Rollback approach

- Rollback method: revert the branch; the module, cases, subcommand, doc, and tests revert cleanly.
- State/data reversal notes: none.
- Feature flag / kill switch: not applicable; the command is read-only.
- Owner: maintainer.
- Time to restore estimate: minutes.

## Proof commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py eval .
python tools/ng.py validate .nuclear/changes/efficacy-eval-harness
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

Original Nuclear-grade plan influenced by configuration-management concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
