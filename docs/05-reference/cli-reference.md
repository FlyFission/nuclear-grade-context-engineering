# CLI Reference

**Purpose:** Document the `tools/ng.py` helper, which needs no extra dependencies.

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
- `new` copies Quick or Standard templates from the target repo when they are there. If not, it copies them from this Nuclear-grade checkout.
- `validate` hands off to `tools/ng_validate.py`.
- `doctor` checks a Nuclear-grade distribution repo for public files, contracts, and templates. In a target repo that has been set up, it checks `.nuclear/README.md` and `.nuclear/changes/`.
- `list` shows what is available: modes, skills, commands, packet files, CM files (records for keeping the approved version under control), golden-path files, and optional templates. That includes turnover, self-check, and supplier-trust records.
- `status` lists active packets and the modes it detects.

## Boundary note

The command-line tool checks structure and whether evidence is visible. It does not decide engineering adequacy, safety, security, compliance, regulatory adequacy, or formal verification.

## Source-lineage note

This reference documents the local tooling for an original workflow built from public sources. It does not create formal assurance.
