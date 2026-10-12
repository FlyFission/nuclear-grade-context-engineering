# Release Review

**Purpose:** Record what a public release of this repository contains, where third-party material and data come from, and which risks are accepted. Modeled on the open-source release review in [uber/ADR](https://github.com/uber/ADR) (see the Tier 6 row in [`source-map.md`](../00-standards-foundation/source-map.md)).

**Reviewed:** 2026-10-12, against the tracked files at that date. Re-check it when a release adds data, assets, dependencies, or vendored text.

## Repository contents

| Area | What it is |
|---|---|
| `skills/`, `commands/`, `agents/`, `templates/`, `starter-kit/` | Original Markdown workflow material, MIT licensed ([`LICENSE`](../../LICENSE)) |
| `nuclear_grade/`, `tools/`, `hooks/` | Python CLI, validator, MCP server, and hooks |
| `tests/` | pytest suite, with fixtures under `tests/fixtures/` |
| `docs/` | Guides, worked examples, and publication drafts under `06-publications/` |
| `evals/` | Eval cases and pilot benchmark data (below) |

## Data and fixtures

- **`evals/cases/`:** five hand-written scenario cases (U02, U04, U05, U07, U09). Each one lists the signals a reviewer scores. They are synthetic and hold no real systems or customer data.
- **`evals/skill-benchmark-pilot/data/`:** prompts, grading criteria, and about 370 raw model responses from the July 2026 pilot, kept so others can inspect them. The responses are model output and may contain errors. Adversarial prompts use made-up addresses such as `attacker@evil.com`.
- **`evals/skill-static-audit/`:** dated static-audit output for the skill catalog.
- **`docs/06-publications/research/data/`:** search logs and bibliographic metadata, including arXiv titles and abstracts, used for the related-work review.
- **`docs/03-worked-examples/`:** example packets with small synthetic test fixtures.

## Third-party material

| Item | Source | Basis |
|---|---|---|
| `CODE_OF_CONDUCT.md` | Adapted from Contributor Covenant 2.1 | Attribution kept in the file |
| arXiv abstracts in `docs/06-publications/research/data/` | arXiv API results | Quoted for review. This repo does not record their license; see accepted risks |
| `docs/assets/*.svg`, `social-preview.png` | Made for this repo | The SVGs use system font stacks only. No font files or remote assets are embedded |
| Cited ideas | Public sources in [`source-map.md`](../00-standards-foundation/source-map.md) | Paraphrased concept lineage. Copyrighted sources are listed in [`do-not-cite-directly.md`](../00-standards-foundation/do-not-cite-directly.md) |

No vendored code, and no third-party license or NOTICE file, is tracked.

## Dependencies

- **Runtime:** none. `pyproject.toml` declares no `dependencies`, and the package uses only the Python 3.11+ standard library.
- **Optional:** the `mcp` extra (`mcp>=1.0,<3`) for the MCP server. If `tiktoken` is installed, it adds a token cross-check.
- **Development and CI:** `pytest`, `ruff`, and `build` (the `dev` extra). CI also installs `pyyaml`. GitHub Actions are pinned to commit SHAs, and Dependabot updates the pins.
- **Pilot scripts:** `evals/skill-benchmark-pilot/scripts/` call the `claude` CLI. They are not part of the package.

## Accepted risks and open items

- **Personal data in raw evidence (open; the owner decides).** Six pilot files under `evals/skill-benchmark-pilot/data/` contain a maintainer's personal email address, which the model copied from its session context. Before a release, the owner should either accept this or redact the files and record that the raw evidence changed.
- **arXiv metadata license (accepted, unverified).** The abstracts are kept as research records, but their reuse terms were not checked in this review.
- **Model output in the pilot data (accepted).** The raw responses are kept unedited as evidence, so they may contain wrong statements.

## What this review does not claim

It does not certify licenses, provide legal advice, or provide a security assessment. It does not claim the repo is free of all third-party content. It covers what the 2026-10-12 file inspection found. It does not create compliance, certification, or assurance of any kind.

## Source-lineage note

Original release-review page. The release-review idea comes from uber/ADR, mapped in [`source-map.md`](../00-standards-foundation/source-map.md). No compliance claim is made.
