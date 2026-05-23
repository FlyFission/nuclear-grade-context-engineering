# Tools

This directory contains lightweight local tooling for Nuclear-grade packets.

## `nuclear-grade.yaml`

`nuclear-grade.yaml` is a human-readable project manifest. The `ng doctor` command checks that this file exists. Keep it in sync with the `skills/`, `commands/`, and `templates/` directories to avoid silent drift.

## `ng.py`

Primary helper:

```bash
python tools/ng.py init [repo] [--dry-run] [--yes]
python tools/ng.py new <slug> --mode quick|standard [--repo .] [--force]
python tools/ng.py validate <packet>
python tools/ng.py doctor [repo]
python tools/ng.py list
python tools/ng.py status [repo]
```

`ng.py` is dependency-free and delegates packet validation to `ng_validate.py`.
`doctor` also checks the activated CM templates and the golden-path templates used by the Questioning Attitude workflow.

The importable console-script implementation lives in `nuclear_grade/`; `tools/ng.py` remains as the repo-local wrapper used throughout the docs.

## `ng_validate.py`

Checks Quick and Standard packets for:

- required packet files for the detected mode;
- required sections;
- evidence status labels;
- rollback, monitoring, and release-decision posture;
- source-lineage notes;
- broken local Markdown links;
- seed prohibited compliance-overclaim phrases.

Run:

```bash
python tools/ng_validate.py .nuclear/changes/<slug>/
```

Example:

```bash
python tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

The validator checks whether evidence is visible and structured. It does not decide safety, security, adequacy, or compliance.

## Boundary note

The tools check structure and evidence visibility. They do not create formal V&V, compliance, certification, safety, security, regulatory adequacy, or production suitability.
