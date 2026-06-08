# Install Nuclear-grade

Nuclear-grade runs inside your repo and is Markdown-first. For Claude Code it also installs as a plugin in two commands (see below). No package registry or hosted service is required either way.

> The `ng` CLI scaffolds and checks packets, but Nuclear-grade is markdown-first. Many adopters only need [`CORE.md`](CORE.md) (the seven habits + the decision matrix) plus one [`starter-kit/`](starter-kit/) directory copied into their repo. The steps below set up the optional CLI.

## Install as a Claude Code plugin (two commands)

For Claude Code users, this repository is its own plugin marketplace. Add it, then install:

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade@nuclear-grade
```

The plugin exposes the existing skills (`skills/`) and command prompts (`commands/`). It configures **no hooks**, so nothing runs automatically when you install it or start a session. Because the marketplace source is the repository root, the install also copies the repo's `ng` Python CLI — but that runs only when you invoke it (for example `ng validate`), never on its own.

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

Public v0 ships paste-ready command prompts in `commands/` and agent-ready skills in `skills/`. They are plain Markdown files you can paste into, or adapt for, an AI coding agent. For Claude Code they also install as a plugin (see the one-line install above); the plugin packages these same Markdown files, with no executable hooks in this tier.

## Optional editable install

To test the console script locally from this checkout:

```bash
python -m pip install -e .
nuclear-grade doctor .
```

The repo-local `python tools/ng.py ...` commands remain a primary way to work in Public v0, alongside the Claude Code plugin (above) for agent users. The console script is a convenience for local checkout work, not a standalone release.

## Boundary note

MIT license permission does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, procurement adequacy, or a regulated quality program. For those claims, use qualified controls built for your own project.

## Source-lineage note

This install guide shows how to use the Nuclear-grade workflow files. The sources that shaped it are mapped in `docs/00-standards-foundation/source-map.md`.
