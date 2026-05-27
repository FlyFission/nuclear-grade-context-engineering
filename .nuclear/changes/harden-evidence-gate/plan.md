# Plan

## Build sequence

1. Add `PLACEHOLDER_MARKER` to `nuclear_grade/ng_validate.py` and have `validate_packet` append a clear, file-named message whenever the marker is found in any `*.md` of the packet.
2. Inject the marker as a single HTML comment near the top of every template under `templates/quick`, `templates/standard`, `templates/cm`, `templates/golden-path`.
3. Confirm with `grep -r` for the marker constant that it is absent from the four `.nuclear/changes/` packets, the flagship example packet, and all test fixtures.
4. Add the pytest case in `tests/test_ng_validate.py` that injects the marker into a minimal Quick packet's `proof.md` and asserts the named failure.
5. Add the CLI regression in `tests/test_ng_cli.py` that copies the real `templates/` tree into a tmp repo, runs `python tools/ng.py new <slug> --mode quick --repo <tmp>`, and asserts validate fails because of the marker.
6. Add `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` to `REQUIRED_PUBLIC_FILES` in `nuclear_grade/cli.py`.
7. Move `docs/04-adoption/report-swot-gap-remediation.md` to `.research/report-swot-gap-remediation.md` and delete the bullet at `docs/04-adoption/README.md:8`.
8. Update `README.md`, `INSTALL.md`, and `QUICKSTART.md` so the new-then-validate sequence states that validate is expected to fail on the untouched packet, shows filling one real status and deleting the marker, then a green validate.
9. Add a CI step in `.github/workflows/ci.yml` that validates `.nuclear/changes/harden-evidence-gate`.
10. Add a CHANGELOG `[Unreleased]` entry.

## Affected files and assets

| File / asset | Change expected |
|---|---|
| `nuclear_grade/ng_validate.py` | New constant and check in `validate_packet`. |
| `nuclear_grade/cli.py` | Four new entries in `REQUIRED_PUBLIC_FILES`. |
| `templates/quick/*.md`, `templates/standard/*.md`, `templates/cm/*.md`, `templates/golden-path/*.md` | One marker line each. |
| `tests/test_ng_validate.py` | One new test. |
| `tests/test_ng_cli.py` | One new test plus `shutil` import. |
| `docs/04-adoption/README.md` | Remove SWOT bullet. |
| `docs/04-adoption/report-swot-gap-remediation.md` | Removed from version control; moved to gitignored `.research/`. |
| `README.md`, `INSTALL.md`, `QUICKSTART.md` | Update new-then-validate explanation. |
| `.github/workflows/ci.yml` | Validate `harden-evidence-gate`. |
| `CHANGELOG.md` | `[Unreleased]` entry. |

## Non-goals

- Renaming `docs/00-standards-foundation/flyfission-ops-knowledge-graph-usage.md`; flagged for maintainer decision in `risk.md`.
- Reworking unrelated docs or skills.
- Changing the public signatures of `validate_packet` or `detect_packet_mode`.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Marker injected | Marker present only in templates. | pass |
| Validator check | Marker triggers a per-file message. | pass |
| Tests | New tests pass and existing tests stay green. | pass |
| Doctor | `python tools/ng.py doctor .` green. | pass |
| Packets | All five existing packets validate, new packet validates. | pass |

## Rollback approach

- Rollback method: revert the merge commit; the change is a single coherent commit on `claude/zen-ptolemy-ZIQhj`.
- State/data reversal: no data; the SWOT file remains in maintainer working trees under `.research/` regardless.
- Time to restore estimate: under one minute via `git revert`.

## Proof commands

```bash
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/public-v0-launch
python tools/ng.py validate .nuclear/changes/peer-ready-release
python tools/ng.py validate .nuclear/changes/cm-public-readiness
python tools/ng.py validate .nuclear/changes/questioning-attitude-golden-path
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
python tools/ng.py validate .nuclear/changes/harden-evidence-gate
python -m py_compile nuclear_grade/cli.py nuclear_grade/ng_validate.py tools/ng.py tools/ng_validate.py
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Build sequence steps are complete.
- Proof commands all pass and are recorded in `verification.md`.

## Source-lineage note

Original Nuclear-grade build-plan record grounded in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
