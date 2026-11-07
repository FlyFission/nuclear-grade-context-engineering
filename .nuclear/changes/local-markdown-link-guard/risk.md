# Risk — local Markdown link guard

## Selected mode

- **Mode:** Quick
- **Why:** A dependency-free CI assertion is low consequence, immediately detectable, and removable in one commit. It changes no runtime, authority, dependency, public claim, or release behavior.

## Decision

Scan every tracked Markdown document during the existing public-doc test and fail when a relative link resolves to no repository path. Ignore URL, email, and same-document anchor targets.

The main risk is rejecting unusual but valid Markdown syntax. Keep the parser deliberately narrow, use the current corpus as its fixture, and report both the source document and target when it fails.

## Required proof

- `python -m pytest tests/test_public_docs.py -q`
- `python -m ruff check tests/test_public_docs.py`
- `git diff --check`

## Required links

- Changed item: [`tests/test_public_docs.py`](../../../tests/test_public_docs.py)
- Proof: [`proof.md`](proof.md)

## Exit criteria

The current Markdown corpus passes, failure output identifies the broken reference, and no third-party checker or workflow is added.

## Source-lineage note

This repository-local maintenance control stays within the public source boundaries mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). It makes no compliance or efficacy claim.
