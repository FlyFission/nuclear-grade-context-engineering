# Risk — Enterprise Landing Page

**Purpose:** Sort the README landing-page overhaul by risk, justify Standard mode, and name the evidence due before it ships.

---

## Change identity

- **Slug:** `enterprise-landing-page`
- **PR / issue:** `claude/enterprise-landing-page-uSnWo` branch / landing-page PR
- **Owner:** Maintainer
- **Date:** 2026-06-06
- **Current lifecycle phase:** Verify
- **Summary:** Rewrite `README.md` into a best-in-class, plain-language landing page; add two canonical diagrams (a role sequence and a configuration-management loop) to `docs/diagrams.md`; add a typographic SVG hero banner; and ship this Standard packet so the change models the method it documents.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Public landing page | Documentation | First public trust surface and the PyPI long description. | `README.md` |
| Canonical diagrams | Documentation | Single source for diagrams embedded across docs; drift risk if duplicated. | `docs/diagrams.md` |
| Hero banner | Image asset | New typographic SVG shown at the top of the page. | `docs/assets/landing-banner.svg` |
| README invariant tests | Tests | Gate the lifecycle string, the HPI phrase, and negative-context boundary phrasing. | `tests/test_public_docs.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | A public landing page sets first impressions and can over- or under-sell the work. |
| Reversibility | High | Docs and one SVG revert cleanly; no data or runtime state changes. |
| Detectability | Medium | Overclaim and broken-fallback issues need explicit reading and tests, not just CI green. |
| Exposure | High | The README is the most-read public file and the packaged PyPI description. |
| Uncertainty | Medium | Mermaid and SVG render differently across GitHub and PyPI; fallbacks must hold. |
| Dependency trust | Low | No new runtime dependencies; badges use external shields.io images only. |
| AI authority | Low | Documentation-only change; no tool, permission, or model authority is altered. |

## Selected mode

- **Mode:** Standard
- **Why this mode:** The change touches the primary public trust surface and several controlled docs, and carries a real overclaim risk that needs a stated basis and verification.
- **Why lighter mode is not enough:** A Quick packet would not capture the no-overclaim, diagram-fallback, and counts-honesty claims that make this change safe to publish.
- **Why heavier mode is not yet required:** The change is documentation-only, reversible, and changes no code, permissions, data, or release behavior.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | States the protected outcomes and the claims the page must keep true. | Maintainer |
| `plan.md` | yes | Bounds the build sequence and the rollback. | Maintainer |
| `trace.md` | yes | Links each landing-page claim to its evidence. | Maintainer |
| `verification.md` | yes | Records the commands, tests, and reviews that back the claims. | Maintainer |
| `ship.md` | yes | Records the release decision and residual risks. | Maintainer |
| `questioning-attitude.md` | no | Adversarial review was captured during planning; no separate record needed. | Maintainer |
| `turnover.md` | no | Single-session change; no handoff. | Maintainer |
| Nuclear subset record | no | Stakes do not warrant a heavier mode. | Maintainer |

## Immediate evidence obligations

- README CI invariants are preserved: the eleven-beat lifecycle line, the `HPI for AI agents` phrase, and boundary phrases only in negative context.
- Both new diagrams validate as Mermaid and appear in `docs/diagrams.md` and `README.md`.
- Component counts match `nuclear-grade.yaml` and are qualified with the version.
- All relative links resolve; `ng doctor` and `ng tokens` stay green.

## Required links

- Packet: `.nuclear/changes/enterprise-landing-page/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source-map / crosswalk references: `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- The mode is justified.
- The activated artifacts are named.
- The overclaim, rendering, and link risks are visible and owned, not hidden in chat.

## Source-lineage note

Original Nuclear-grade risk record inspired by public graded-quality, configuration-management, lifecycle, verification, and source-lineage concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
