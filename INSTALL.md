# Install Nuclear-grade

Nuclear-grade runs inside your repo. Public v0 does not need a package registry, a hosted service, or an agent marketplace plug-in.

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

From this checkout, set up the target repo:

```bash
python tools/ng.py init /path/to/your/repo --dry-run
python tools/ng.py init /path/to/your/repo
python tools/ng.py doctor /path/to/your/repo
```

Make a packet:

```bash
python tools/ng.py new add-boundary --mode standard --repo /path/to/your/repo
python tools/ng.py validate /path/to/your/repo/.nuclear/changes/add-boundary
```

`validate` is **supposed to fail** on the untouched packet. Each template ships with a `NUCLEAR-GRADE-PLACEHOLDER` marker line, and the checker refuses any packet that still has it. That is the gate doing its job. Fill in the fields, set at least one real status (`pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`), delete the marker line in every file, and validate again:

```bash
python tools/ng.py validate /path/to/your/repo/.nuclear/changes/add-boundary
# OK: /path/to/your/repo/.nuclear/changes/add-boundary
```

`new` uses templates in `/path/to/your/repo/templates/` when they exist. If they do not, it copies the bundled templates from this Nuclear-grade checkout, so a target repo only needs `.nuclear/` to get started.

## Tool and agent harness notes

Public v0 ships paste-ready command prompts in `commands/` and agent-ready skills in `skills/`. They are plain Markdown files you can paste into, or adapt for, an AI coding agent. Public v0 does not package them as a marketplace plug-in.

## Optional editable install

To test the console script locally from this checkout:

```bash
python -m pip install -e .
nuclear-grade doctor .
```

The repo-local `python tools/ng.py ...` commands are still the main way to get started in Public v0. The console script is a convenience for local checkout work. It is not a packaged marketplace or a standalone release.

## Boundary note

MIT license permission does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, procurement adequacy, or a regulated quality program. For those claims, use qualified controls built for your own project.

## Source-lineage note

This install guide shows how to use the Nuclear-grade workflow files. The sources that shaped it are mapped in `docs/00-standards-foundation/source-map.md`.
