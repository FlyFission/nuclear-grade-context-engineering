# Plan: Prepare release 0.7.0

## Build sequence

1. Set version 0.7.0 in `pyproject.toml`, both plugin manifests, the guard plugin manifest, `nuclear-grade.yaml`, and `CITATION.cff`.
2. Add `## [0.7.0] - 2026-11-03` under `## [Unreleased]` in `CHANGELOG.md`, so every unreleased entry now sits in the 0.7.0 section, and set `CITATION.cff` `date-released` to the same date.
3. Update the version assertion in `tests/test_packaging.py`.
4. Write this record, regenerate `.nuclear/badge.json`, and run the gates.

Controlled items changed: the release identity (every version declaration) and the changelog.

## Proof commands

```bash
python -m nuclear_grade.release --tag v0.7.0
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m build --outdir <scratch>
python -m twine check --strict <scratch>/*
python -m venv <scratch>/v && <scratch>/v/bin/pip install <scratch>/*.whl && <scratch>/v/bin/python -c "import importlib.metadata as m; print(m.version('nuclear-grade'))"
git diff --check
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md) and [`releasing.md`](../../../docs/05-reference/releasing.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
