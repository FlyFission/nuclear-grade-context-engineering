# Plan: challenge results harness

## Build sequence

1. Add `to_json` and `--json` to `challenge/score.py`; regenerate `challenge/judge/manifest.json`.
2. Add `challenge-results/`: `run.py`, `build.py`, `disclosure.py`, `agents.json`, `tracks/plain/AGENTS.md`, `METHOD.md`, `README.md`, `adjudications.json`, `CORRECTIONS.md`.
3. Add issue forms for posting a result and questioning one.
4. Add tests in `tests/test_challenge.py` and `tests/test_challenge_results.py`.

Non-goals: running any real agent, publishing any named result, changing how the challenge is scored.

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

`python -m pytest -q`, `ruff check .`, `ng doctor`, and `ng tokens` pass.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
