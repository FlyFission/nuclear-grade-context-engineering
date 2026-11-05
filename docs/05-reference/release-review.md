# Release Review

**Purpose:** Record what a public release of this repository contains, where third-party material and data come from, and which risks are accepted. Modeled on the open-source release review in [uber/ADR](https://github.com/uber/ADR) (see the Tier 6 row in [`source-map.md`](../00-standards-foundation/source-map.md)).

**Reviewed:** inventory refreshed 2026-11-05. This is a bounded file review, not clearance to publish. Re-check it when a release adds data, assets, dependencies, or vendored text. See [artifact review](artifact-review.md) for the evidence boundary and remaining maintainer actions.

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
- **`evals/skill-control-ladder/`:** repo-authored scenarios, rubrics, control prompts, model runs, grading records, and analyses. These are experimental records, not independent assurance; raw model output can contain errors or session context.
- **Other `evals/` trees:** routing and output cases, compressed-skill and consolidation drafts, and analysis records. Treat new raw records as publication candidates requiring review, not automatically cleared fixtures.
- **`challenge-results/`:** scripts, agent manifests, adjudication records, and instructions for publishing challenge runs. The harness captures raw command, stdout/stderr, diff, model/tool version, and scorecard information. Submitted runs require the contributor's publication consent and privacy review before inclusion; see the [publication procedure](artifact-review.md).
- **`docs/06-publications/research/data/`:** search logs and bibliographic metadata used for related-work review. Copied arXiv/Crossref abstract and summary fields are omitted from these exports; identifiers, titles, authors, links, query provenance, and repo-authored annotations remain.
- **`docs/03-worked-examples/`:** example packets with small synthetic test fixtures.

## Third-party material

| Item | Source | Basis |
|---|---|---|
| `CODE_OF_CONDUCT.md` | Adapted from Contributor Covenant 2.1 | Attribution kept in the file |
| Bibliographic metadata in `docs/06-publications/research/data/` | arXiv, Crossref, and other named search sources in the records | Citation and query provenance retained. Copied abstract/summary fields removed because reuse terms had not been verified; source-specific rights are not relicensed by this repository |
| `docs/assets/*.svg`, `docs/assets/diagrams/`, `social-preview.png` | Made for this repo; SVG sources retained | SVG previews inspected use system fonts; no font files are vendored. This is not an independent originality review |
| `docs/assets/demo/demo.gif` | Terminal demonstration with `demo.tape` and `simulate_tool_call.py` beside it | Reproduction inputs retained. README identifies the calls as simulated; animation metadata inspection is not review of every rendered frame |
| Cited ideas | Public sources in [`source-map.md`](../00-standards-foundation/source-map.md) | Paraphrased concept lineage. Copyrighted sources are listed in [`do-not-cite-directly.md`](../00-standards-foundation/do-not-cite-directly.md) |

No vendored code, and no third-party license or NOTICE file, is tracked.

The root MIT license covers the project's original material. It does not grant rights in third-party material beyond the rights its owners provide. Contributor Covenant attribution remains in its file; confirm applicable upstream terms when updating adapted material. Public access to an API, standard, paper, or repository is not by itself permission to redistribute its text.

## Dependencies

- **Runtime:** none. `pyproject.toml` declares no `dependencies`, and the package uses only the Python 3.11+ standard library.
- **Optional:** the `mcp` extra (`mcp>=1.0,<3`) for the MCP server. If `tiktoken` is installed, it adds a token cross-check.
- **Development and CI:** `pytest`, `ruff`, and `build` (the `dev` extra). CI also installs `pyyaml`. GitHub Actions are pinned to commit SHAs, and Dependabot updates the pins.
- **Pilot scripts:** `evals/skill-benchmark-pilot/scripts/` call the `claude` CLI. They are not part of the package.

## Accepted risks and open items

- **Personal data in raw evidence (working-tree redaction 2026-10-12).** Six pilot files under `evals/skill-benchmark-pilot/data/` contained a maintainer's personal email address, copied by the model from its session context. With the owner's approval, each occurrence was replaced with `[redacted-email]`. No other byte changed, and no stored hash pinned those files. Earlier git history still holds the original text. A current-tree scan does not remove it from old commits, pull-request refs, forks, or GitHub caches. Coordinated history and hosting-cache cleanup remains a maintainer action; see the [artifact review procedure](artifact-review.md#historical-material). Never include the address in public remediation records.
- **Previously copied research abstracts.** Current abstract/summary fields have been removed rather than treating unverified reuse terms as publication clearance. Historical commits can still contain that text; retain citations and obtain a source-specific reuse basis before restoring any copied text.
- **Model output in the pilot data (accepted).** The raw responses are kept unedited as evidence, so they may contain wrong statements.

## What this review does not claim

It does not certify licenses, provide legal advice, or provide a security assessment. It does not claim the repo is free of all third-party content or private information. The inventory refresh and current-tree checks do not clear history, external copies, or future submissions. It does not create compliance, certification, or assurance of any kind.

## Source-lineage note

Original release-review page. The release-review idea comes from uber/ADR, mapped in [`source-map.md`](../00-standards-foundation/source-map.md). No compliance claim is made.
