# Basis: Prepare release 0.7.0

## Mission

When the maintainer pushes the `v0.7.0` tag, every place that declares the version says 0.7.0, the changelog has a dated section for it, and the release workflow's identity check passes.

## Requirements

- **REQ-001:** `pyproject.toml`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `plugins/nuclear-grade-guard/.claude-plugin/plugin.json`, `nuclear-grade.yaml`, and `CITATION.cff` shall all declare version 0.7.0.
- **REQ-002:** `CHANGELOG.md` shall move every `[Unreleased]` entry under `## [0.7.0] - 2026-11-03`, and `CITATION.cff` `date-released` shall carry the same date.
- **REQ-003:** `python -m nuclear_grade.release --tag v0.7.0` shall pass.
- **REQ-004:** The built wheel shall install in a clean environment and report version 0.7.0.
- **REQ-005:** Nothing shall be tagged or published by this change.

## Non-goals

No tag, no GitHub release, no PyPI upload, no change to what the package does.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)

## Exit criteria

Each requirement maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Follows [`releasing.md`](../../../docs/05-reference/releasing.md). See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
