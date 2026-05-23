# CLI Reference

**Purpose:** Document the dependency-free `tools/ng.py` helper.

## Commands

```bash
python tools/ng.py init [repo] [--dry-run] [--yes]
python tools/ng.py new <slug> --mode quick|standard [--repo .] [--force]
python tools/ng.py validate <packet>
python tools/ng.py doctor [repo]
python tools/ng.py list
python tools/ng.py status [repo]
```

## Behavior

- `init` creates `.nuclear/README.md` and `.nuclear/changes/`.
- `new` copies Quick or Standard templates.
- `validate` delegates to `tools/ng_validate.py`.
- `doctor` checks repo health, contract structure, and required Quick/Standard/CM/golden-path templates.
- `list` shows available modes, skills, commands, packet files, CM files, and golden-path files.
- `status` lists active packets and detected modes.

## Boundary note

The CLI checks structure and evidence visibility. It does not decide engineering adequacy, safety, security, compliance, regulatory adequacy, or formal verification.

## Source-lineage note

This CLI reference documents local tooling for an original public-source-inspired workflow. It does not create formal assurance.
