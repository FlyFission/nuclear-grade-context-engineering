# Plan: agent honesty challenge

## Build sequence

1. Add the toy repo: `challenge/app/` (config, runner, tests), `AGENTS.md`, `CLAUDE.md`, `TASK.md`, and a validated example record.
2. Add `challenge/score.py` and `challenge/judge/` (manifest built by `score.py --write-manifest`).
3. Add `challenge/README.md` with rules, run steps, verdicts, and what the score does not mean.
4. Add `tests/test_challenge.py`; add `challenge` to the residue scan in `tests/test_public_docs.py`; link the challenge from `docs/README.md`.
5. Add `/challenge` to the sdist include in `pyproject.toml`, since the sdist ships `tests/`.
6. Regenerate `.nuclear/badge.json`.

Non-goals: changes to `README.md`, `CHANGELOG.md`, `nuclear_grade/cli.py`, `.github/`, or `hooks/` (proposed text goes to the owner); a hosted leaderboard.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
python tools/ng.py validate .nuclear/changes/agent-honesty-challenge --strict-custody
```

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, and one manual end-to-end run is recorded.

## Source-lineage note

See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
