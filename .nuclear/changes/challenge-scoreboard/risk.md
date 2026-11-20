# Risk: a scoreboard page, a badge and a run-everything script for the challenge

## Change identity

- Slug: challenge-scoreboard
- Owner: FlyFission (maintainer); drafted by an AI agent
- Date: 2026-11-18
- Summary: `challenge-results/build.py` also writes a one-page scoreboard (`docs/scoreboard/index.html`) that sets each agent's task-only runs beside its house-rules runs, and a shields.io endpoint badge (`challenge-results/badge.json`). A new `challenge-results/run-all.py` runs every installed agent CLI on both tracks, then rebuilds. No outcome logic changes.

## Mission anchor

- **Objective:** make the challenge results easy to see and easy to produce, so one scored round can become a shareable page.
- **Success criterion:** with no runs, the page and badge say so plainly; with runs, the page shows each agent on both tracks from the same rows `RESULTS.md` uses; `run-all.py` skips missing CLIs and runs the rest on both tracks.
- **Non-goals:** no change to outcomes, good-outcome sets, the Wilson range, rulings, `run.py`, or the scorer; `METHOD.md` gains one dated method-history entry for the container round (corrected 2026-11-20, after review). No results are published by this change.

## Questioning-attitude summary

- The fact that would change the decision: if the page could state a result the rows do not support. It reads only the rows `summarize` builds, and its one headline number counts two existing outcomes.

## Affected configuration items

| Item | Change |
|---|---|
| `challenge-results/build.py` | gains `scoreboard_pairs`, `silent_widenings`, `render_scoreboard`, `render_badge`, and two output flags |
| `challenge-results/run-all.py` | new: runs every installed agent on both tracks, then `build.py` |
| `challenge-results/README.md` | documents both |
| `challenge-results/badge.json`, `docs/scoreboard/index.html` | generated, empty state |
| `tests/test_challenge_results.py` | five tests |

## Threshold screen

| Dimension | Rating | Why |
|---|---|---|
| Consequence | medium | the page is what people will share and quote |
| Reversibility | high | revert the commit; nothing reads these files yet |
| Detectability | high | tests cover pairing, counts, escaping and the empty state |
| Trust boundary | yes | results tooling is under the `validators` rule |
| Uncertainty | low | presentation only, over rows already tested |

## Selected mode

- **Mode:** Standard
- **Why this mode:** it edits results tooling (`validators`) and a trust-guarding test (`trust-tests`) under `.nuclear/consequence-policy.json`.

## Activated artifacts

- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Not activated: decision-authority record (no gate, CI or policy change).

## Immediate evidence obligations

- The five new tests fail on the previous commit and pass after.
- The full suite, ruff, doctor, token budgets, and `validate` on this record pass.

## Scope

- Paths covered by this record: `challenge-results/build.py`, `challenge-results/run-all.py`, `challenge-results/README.md`, `challenge-results/badge.json`, `docs/scoreboard/index.html`, `tests/test_challenge_results.py`.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship: [`ship.md`](ship.md)

## Exit criteria

- The mode is justified and every path this change touches is named above.
- Evidence obligations are met or carried into `ship.md` as gaps.

## Source-lineage note

Original Nuclear-grade record; graded-rigor lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
