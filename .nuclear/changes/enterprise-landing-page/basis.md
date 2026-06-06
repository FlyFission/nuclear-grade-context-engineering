# Basis — Enterprise Landing Page

**Purpose:** State what must stay true for the new landing page to be clear, honest, and safe to publish.

---

## Change context

- **Slug:** `enterprise-landing-page`
- **Related risk record:** `risk.md`
- **Owner:** Maintainer
- **Date:** 2026-06-06
- **Decision this basis supports:** Whether to replace the README with the new landing page and embed the new diagrams.

## Mission / need

The current README is honest and substantive but dense, and a first-time visitor cannot tell in ten seconds what the project is or why it matters. The need is a landing page a newcomer can follow that still keeps the brand, the proof, and every boundary the project depends on.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| A newcomer understands what this is and can run a proof within the first screen. | First impression decides whether anyone adopts the work. | Self-check read of the rendered page; the proof commands run near the top. |
| The page never overclaims. | Over-trust is the project's primary reputational hazard. | Boundary and disclaimer language present, uncollapsed, and in negative context. |
| Diagrams degrade to readable text where Mermaid does not render. | The README is also the PyPI long description, where Mermaid is broken. | An adjacent text fallback under every embedded diagram. |
| Counts and links stay honest as the corpus grows. | A stale hardcoded count silently becomes an overclaim. | Counts qualified with the version and pointed at the live source. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A hedge is upgraded into a hard claim. | The page promises assurance the project does not provide. | Keep the study, v0, and disclaimer wording near-verbatim; review the diff. |
| The README breaks a CI doc invariant. | Public docs tests fail and the page loses a guaranteed property. | Preserve the lifecycle line, the HPI phrase, and negative-context boundary phrasing. |
| A diagram carries meaning only in Mermaid. | PyPI and screen-reader users lose the content. | Text fallback under each diagram. |
| A second diagram copy drifts from canon. | Two sources disagree over time. | New diagrams are canonical in `docs/diagrams.md` and embedded, not forked. |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| GitHub renders committed relative SVG and Mermaid in the README. | Fact | GitHub markdown rendering behavior. | The banner or diagrams fail to render on the branch. | Maintainer |
| PyPI strips Mermaid and may strip SVG from the long description. | Assumption | Known PyPI long-description sanitizing. | PyPI renders the page with no fallback text. | Maintainer |
| Component counts are 27 skills and 26 command prompts at v0.5.0. | Fact | `nuclear-grade.yaml`. | The catalog in `nuclear-grade.yaml` changes. | Maintainer |
| No new runtime dependency is introduced. | Fact | The change is markdown plus one SVG. | A build step or package dependency is added. | Maintainer |

## Interfaces and trust boundaries

- **Internal interfaces affected:** Markdown links from `README.md` to other repo docs; embedded Mermaid mirrored from `docs/diagrams.md`.
- **External services/APIs affected:** shields.io badge images only (decorative, not load-bearing).
- **Data classes affected:** None; documentation-only change.
- **Human approval boundaries:** Maintainer review and CI must pass before merge.
- **AI/model/tool authority boundaries:** Unchanged; no agent authority is added or removed.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE README SHALL state what the project is, the one idea, and a runnable proof within the first screen. | A newcomer must orient in seconds. | Hero, "What this is", "The one idea", and "See it work in 30 seconds" sit at the top. | Self-check read of the rendered page. |
| REQ-002 | WHERE a diagram is embedded THE README SHALL provide an adjacent text fallback. | The README is the PyPI long description, where Mermaid is broken. | An "In words" line or table under every Mermaid block. | Self-check that each block has a fallback. |
| REQ-003 | THE README SHALL keep the boundary and disclaimer language present, uncollapsed, and in negative context. | Over-trust is the main hazard. | "What this is NOT", license/limits, and disclaimer links stay expanded. | `tests/test_public_docs.py` plus diff review. |
| REQ-004 | THE new diagrams SHALL live canonically in `docs/diagrams.md` and be embedded, not duplicated as a separate source. | Two sources drift. | Sections 6 and 7 of `docs/diagrams.md` are the source; the README mirrors them. | Both diagrams present in both files; Mermaid validates. |
| REQ-005 | WHERE a component count appears THE README SHALL qualify it with the version and point to the live source. | A stale count becomes an overclaim. | Counts marked "as of v0.5.0" with links to `nuclear-grade.yaml`, `SKILLS.md`, `COMMANDS.md`. | Counts match `nuclear-grade.yaml`. |
| REQ-006 | THE README SHALL keep every relative link resolvable and preserve the CI doc invariants. | Broken links and lost invariants erode trust. | Verified link targets; lifecycle line and HPI phrase kept verbatim. | `tests/test_public_docs.py` plus link check. |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `Mission / need` above |
| Architecture — shape and major parts | yes | `plan.md` build sequence |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | Documentation-only change |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Canonical diagrams: `docs/diagrams.md`
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?" for the page.
- The protected outcomes and the outcomes to prevent are stated plainly.
- Each important assumption has a trigger that would prove it wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis record inspired by public ideas on design basis, configuration management, software assurance, and source-lineage discipline mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
