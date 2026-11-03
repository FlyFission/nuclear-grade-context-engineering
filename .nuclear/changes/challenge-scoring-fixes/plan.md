# Plan: Three challenge scoring fixes found in trial runs

## Build sequence

1. Give `rigging()` an optional set of original test files and flag autouse fixtures only in those. Pass the manifest's `original_test_files` from `check_tests_kept`.
2. Regenerate `challenge/judge/manifest.json` with `python challenge/score.py --write-manifest`.
3. Skip a release word joined to `post-` or `pre-` in `_release_commitment()`.
4. Add the new outcome to `challenge-results/build.py` and to the plain track's good outcomes.
5. Add tests to `tests/test_challenge.py` and `tests/test_challenge_results.py`.
6. Update `challenge-results/METHOD.md` and `CHANGELOG.md`.

Controlled items changed: the scorer and its manifest, the results builder, METHOD.md, and the tests above.

## Proof commands

```bash
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
git diff --check
python challenge/score.py <trial folder with the trial diff applied> --agent trial
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
