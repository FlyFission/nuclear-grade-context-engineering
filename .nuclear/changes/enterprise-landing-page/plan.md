# Plan — Enterprise Landing Page

**Purpose:** Bound the build, the review, and the rollback for the landing-page overhaul before scope grows.

---

## Change context

- **Slug:** `enterprise-landing-page`
- **Related risk record:** `risk.md`
- **Related basis record:** `basis.md`
- **Owner:** Maintainer
- **Date:** 2026-06-06
- **Current lifecycle phase:** Verify

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Add the role-sequence and configuration-management diagrams to `docs/diagrams.md` as canonical sections 6 and 7. | REQ-004 | None | Both diagrams validate as Mermaid. | Both sections present with text fallbacks. |
| 2 | Create the typographic SVG hero banner with descriptive alt text and no compliance imagery. | REQ-001 | None | Banner renders on GitHub; alt text present. | `docs/assets/landing-banner.svg` committed. |
| 3 | Rewrite `README.md`: hero, plain-language pitch, proof, embedded diagrams with fallbacks, qualified counts, governance links, and preserved invariants. | REQ-001, REQ-002, REQ-003, REQ-005, REQ-006 | Steps 1 and 2 | `tests/test_public_docs.py` passes. | Page reads top to bottom with no overclaim. |
| 4 | Author this Standard packet so the change models the method. | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006 | Steps 1 to 3 | `ng validate` reports OK. | All six records filled and valid. |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Draft wording, sketch diagrams, try layouts. | None; throwaway work. |
| candidate | Write the README, diagrams, banner, and packet. | Diagrams validate; page reads cleanly. |
| audit | Run the doc tests, validator, doctor, and token gate; re-read for overclaim. | All checks green; disclaimers intact. |
| accept | Commit, push, open the draft PR. | CI green on the branch. |

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `README.md` | Full rewrite in place. | REQ-001, REQ-002, REQ-003, REQ-005, REQ-006 | The public landing page and PyPI description. | Maintainer |
| `docs/diagrams.md` | Add canonical sections 6 and 7. | REQ-004 | Single source for the embedded diagrams. | Maintainer |
| `docs/assets/landing-banner.svg` | New file. | REQ-001 | The hero banner. | Maintainer |
| `.nuclear/changes/enterprise-landing-page/` | New Standard packet. | REQ-001 to REQ-006 | Makes the PR a worked example. | Maintainer |

## Non-goals

- No GitHub Pages site, HTML page, or build step.
- No changes to skills, commands, templates, the CLI, or the charter.
- No binary or generated image asset; the banner stays a hand-written, diffable SVG.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each REQ is one clear trigger to response statement, reviewed. | pass |
| Design approved | The design outline in `basis.md` is complete for this change. | pass |
| Tasks approved | Every build step carries the requirement IDs it delivers. | pass |
| Specification reviewed | Protected outcomes and outcomes to prevent are stated plainly. | pass |
| Tests/evals defined | Each claim maps to evidence in `verification.md`. | pass |
| Build complete | The affected files match the plan. | pass |
| Verification complete | Evidence is linked in `verification.md`. | pass |
| Release decision ready | Residual risks and rollback are recorded in `ship.md`. | pass |

## Rollback approach

- **Rollback method:** Revert the landing-page commit; the previous README and `docs/diagrams.md` return unchanged.
- **State/data reversal notes:** Not applicable; documentation-only change.
- **Feature flag / kill switch:** Not applicable; the PR is the gate.
- **Owner:** Maintainer.
- **Time to restore estimate:** Under ten minutes via `git revert`.

## Proof commands

```bash
python -m pytest tests/test_public_docs.py -v
python tools/ng.py validate .nuclear/changes/enterprise-landing-page
python tools/ng.py doctor .
python tools/ng.py tokens .
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Canonical diagrams: `docs/diagrams.md`

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback is thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade plan record inspired by public sources on software lifecycle, configuration management, release readiness, and software assurance mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
