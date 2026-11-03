# Plan: Make the package page ready for PyPI

## Build sequence

1. Add the metadata fields and `[project.urls]` to `pyproject.toml`.
2. Replace `readme` with `dynamic = ["readme"]`, add `hatch-fancy-pypi-readme` to the build requirements, and configure two substitutions (image sources to raw files, links to the repo).
3. Add `twine check --strict` after the build in `.github/workflows/ci.yml` and `.github/workflows/release.yml`.
4. Update `docs/05-reference/releasing.md` and `CHANGELOG.md`.

Controlled items changed: `pyproject.toml` build requirements, the CI and release workflows, and the release doc.

## Proof commands

```bash
python -m build --outdir <scratch>
python -m twine check --strict <scratch>/*
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
git diff --check
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
