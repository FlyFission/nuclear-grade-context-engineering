# Plan: lessons from Headroom

## Build sequence

1. `challenge-results/run.py`:
   - add `PINNED_INPUTS` (including `nuclear_grade`) and `COPY_SKIPS`;
   - add `uncommitted_inputs()`, which reads NUL-separated porcelain status and counts untracked and ignored files but not the folders the copy skips;
   - add `inputs_commit()`;
   - read both, and `HEAD`, before the copy is made;
   - set result schema version 2.
2. `challenge-results/build.py`:
   - group by tool version;
   - add `identity_problems()`;
   - show a "Tool version" column and a "not comparable" note.
3. Tests in `tests/test_challenge_results.py` for each guard, plus schema and shape checks in the end-to-end test. Then one mutation run per guard.
4. `challenge-results/METHOD.md`: the Pinning paragraph, How many runs, and a dated entry under Changes to this method.
5. `ROADMAP.md`: two v0.2 items. `llms.txt` and its test in `tests/test_public_docs.py`. `CHANGELOG.md` entries under Unreleased.
6. An independent read-only review of the diff, with findings dispositioned in `verification.md`.

Controlled items changed: the results harness, `METHOD.md`, `ROADMAP.md`, `CHANGELOG.md`, `llms.txt` (new), and two test files.

## Proof commands

```bash
python -m pytest tests/test_challenge_results.py tests/test_public_docs.py
python -m pytest
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions --strict-custody
python -m nuclear_grade.release
python tools/ng.py validate .nuclear/changes/headroom-lessons --strict-custody
python tools/ng.py badge . --out .nuclear/badge.json
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
