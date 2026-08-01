# Plan — instruction conflict routing

## Build sequence

1. Add one conflict-routing bullet to `AGENTS.md` (REQ-001).
2. Inspect the focused diff and run the repository's full pre-PR checks.
3. Open a reviewable PR; do not merge or alter release posture.

Non-goals: defining a new precedence hierarchy, adding instruction inventories, changing permissions, or adding runtime enforcement.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/instruction-conflict-routing --strict-custody
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions --strict-custody
```

## Required links

- Risk: [`risk.md`](risk.md)
- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Only `AGENTS.md` and this packet change; every proof command passes before commit.

## Source-lineage note

The plan introduces no external standard or assurance claim; repository source boundaries remain those in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).