# Proof — local Markdown link guard

## Proof summary

- Change slug: `local-markdown-link-guard`
- Proof owner: Hermes scheduled maintenance run
- Date: 2026-08-02
- Risk record: [`risk.md`](risk.md)

## Claim proven

The generic local-link guard accepts the repository's current Markdown corpus and adds no lint, packet-validation, or whitespace failure.

## Method and result

- **pass** — `python -m pytest tests/test_public_docs.py -q`: 16 tests passed.
- **pass** — `python -m pytest -q`: full configured suite passed.
- **pass** — `python -m ruff check .`: all checks passed.
- **pass** — `python tools/ng.py doctor .` and `python tools/ng.py tokens .`.
- **pass** — both this packet and the flagship worked-example packet validated.
- **pass** — `git diff --check`.

The change actor ran and summarized deterministic local checks. PR CI can reproduce them; that same-actor coupling is accepted for this small, reversible test guard.

## Reviewer note

Quick mode remains valid. Review should focus on whether the intentionally narrow regex could reject a valid link shape used in this repository.

## Required links

- Changed item: [`tests/test_public_docs.py`](../../../tests/test_public_docs.py)
- Risk: [`risk.md`](risk.md)

## Exit criteria

The targeted and full checks pass, the result is reproducible in CI, and review can decide from this packet without unrelated context.

## Source-lineage note

This proof records deterministic repository checks within the public boundaries mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
