# Basis: Make the package page ready for PyPI

## Mission

When the maintainer turns on PyPI publishing, the first upload shows a complete, working project page.

## Requirements

- **REQ-001:** The package metadata shall include an author, keywords, classifiers, and Homepage, Documentation, Source, Issues, and Changelog links.
- **REQ-002:** The long description shall be README.md with every relative link and image source pointed at the GitHub repository, and `README.md` shall be unchanged.
- **REQ-003:** CI and the release build shall run `twine check --strict` on the built package.
- **REQ-004:** `docs/05-reference/releasing.md` shall list the exact PyPI setup steps, including the pending publisher for a project that does not exist yet.
- **REQ-005:** The wheel's file list shall be unchanged, and nothing shall be published or tagged.

## Non-goals

No upload, no version bump, no tag, no change to install instructions (they change after the first upload).

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)

## Exit criteria

Each requirement maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
