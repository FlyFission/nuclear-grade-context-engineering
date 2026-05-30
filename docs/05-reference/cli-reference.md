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
- `new` copies Quick or Standard templates from the target repo when present, otherwise from this Nuclear-grade checkout.
- `validate` delegates to `tools/ng_validate.py`.
- `doctor` checks a Nuclear-grade distribution repo for public files, contracts, and templates. In an initialized target repo, it checks `.nuclear/README.md` and `.nuclear/changes/`.
- `list` shows available modes, skills, commands, packet files, CM files, golden-path files, and optional templates, including turnover, self-check, and supplier-trust records.
- `status` lists active packets, their detected modes, and a health tag: `ok` (validates), `scaffold` (an untouched draft still carrying the placeholder marker), or `invalid` (fails validation for another reason). It prints a closing reminder when any packet needs attention, so abandoned half-filled drafts are visible rather than silent.

## Boundary note

The CLI checks structure and evidence visibility. It does not decide engineering adequacy, safety, security, compliance, regulatory adequacy, or formal verification.

## Source-lineage note

This CLI reference documents local tooling for an original public-source-inspired workflow. It does not create formal assurance.
