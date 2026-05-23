# Verification

## Evidence status

| Check | Command | Status |
|---|---|---|
| Tests | `/tmp/ng-venv/bin/python -m pytest -q` | pass |
| Compile | `python3 -m py_compile tools/ng.py tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py` | pass |
| Doctor | `python3 tools/ng.py doctor .` | pass |
| Flagship packet | `python3 tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions` | pass |
| Productization packet | `python3 tools/ng.py validate .nuclear/changes/peer-ready-release` | pass |
| Launch packet | `python3 tools/ng.py validate .nuclear/changes/public-v0-launch` | pass |
| Diff check | `git diff --check` | pass |
| Boundary scans | Manual `rg` scans from plan | pass |

## Required links

- `risk.md`
- `trace.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Required verification commands pass or have a recorded blocker.
- Manual scans have no unsafe hits.

## Source-lineage note

This verification record is part of the original Nuclear-grade packet workflow and references `docs/00-standards-foundation/source-map.md`.
