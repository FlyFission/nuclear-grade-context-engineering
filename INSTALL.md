# Install Nuclear-grade

Nuclear-grade is a repo-local workflow. Public v0 does not require a package registry, hosted service, or agent marketplace integration.

## Requirements

- Python 3.11 or newer (tested on 3.12).
- Git.
- `pytest` only if you want to run the test suite.

## Use in this repo

```bash
python tools/ng.py doctor .
python tools/ng.py list
python tools/ng.py status .
```

If your shell only has `python3`, use `python3` in the same commands.

## Add to another repo

Copy the repo or a vendored subset, then initialize the workspace:

```bash
python tools/ng.py init /path/to/your/repo --dry-run
python tools/ng.py init /path/to/your/repo
```

Create a packet:

```bash
python tools/ng.py new add-boundary --mode standard --repo /path/to/your/repo
python tools/ng.py validate /path/to/your/repo/.nuclear/changes/add-boundary
```

## Tool and agent harness notes

Public v0 ships portable command prompts in `commands/` and agent-operable skills in `skills/`. They are plain Markdown artifacts that can be pasted into or adapted for an AI coding agent. They are not packaged as a marketplace integration in Public v0.

## Optional editable install

For local console-script testing from this checkout:

```bash
python -m pip install -e .
nuclear-grade doctor .
```

The repo-local commands remain the canonical onboarding path for Public v0.

## Boundary note

MIT license permission does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, procurement adequacy, or a regulated quality program. Use qualified project-specific controls for those claims.

## Source-lineage note

This install guide describes how to use the Nuclear-grade workflow artifacts. Source influences are mapped in `docs/00-standards-foundation/source-map.md`.
