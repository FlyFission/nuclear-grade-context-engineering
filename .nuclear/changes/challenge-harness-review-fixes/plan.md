# Plan: Fix five gaps a code review found in the challenge harness

## Build sequence

1. `challenge-results/run.py`: add a random part to run IDs and refuse to replace a result file; run the agent in its own process group and stop the group on timeout; diff against the root commit; add an `environment` block with the OS, Python version, and `NG_CONTAINER_IMAGE`.
2. `challenge-results/build.py`: require `tests_pass` for the invalid-record outcome; check every ruling field when loading `adjudications.json`.
3. Tests for each, written to fail on the old code first.
4. Wording fixes in `pypi-package-page/risk.md` and `command-menu-descriptions/plan.md` and `risk.md`; a direct card-to-skill description test.
5. Log the change in `challenge-results/METHOD.md`, the README, and `CHANGELOG.md`.

Controlled items changed: the results harness and two existing change records.

## Proof commands

```bash
python -m pytest -q tests/test_challenge_results.py tests/test_command_contracts.py
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
git diff --check
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
