# White Paper Draft — Risk

**Purpose:** Bound the publication and research-to-repository update, prevent unsupported efficacy/novelty/compliance claims, and keep PR clearance separate from merge or venue-publication clearance.

**Activation threshold:** Standard mode applies because this is lasting, claim-bearing public documentation grounded in external sources and intended for later publication.

**Minimum useful version:** A reviewable manuscript, explicit contribution ledger, cited public sources, one worked example, evidence limitations, and a publication hold until human review.

**Overhead trap:** The packet controls the paper's claims; it must not become a second manuscript.

---

## Change identity

- Slug: `white-paper-draft`
- PR / issue: local draft branch; no PR opened
- Owner: Ben Huffer / FlyFission
- Date: 2026-07-19
- Current lifecycle phase: Execute
- Current work phase: candidate
- Summary: Build the academic preprint and reproducible research record from pre-change baseline `7144831`, then propagate the narrowed custody/coupling contribution through repository doctrine, templates, validator/CLI/MCP/tests, CI, skills, examples, starter kits, and public boundaries.

## Mission anchor

- Objective: Produce a rigorous academic preprint and a coherent repository implementation centered on declared evidence custody and multidimensional actor–evidence coupling.
- Success criteria: The manuscript states a bounded thesis, distinguishes prior art from differentiated synthesis and implementation, shows the method and one worked example, reports current evidence honestly, cites public sources, and the repository operationalizes the contribution with backward-compatible strict checks while documenting the external controls still needed for mandatory enforcement.
- Non-goals / forbidden directions: No claim of being first, proven, validated, compliant, certified, safety-grade, regulator-ready, or defect-reducing; no derivation from paywalled standards; no merge, venue submission, release, or DOI action without a separate human decision.
- Drift check: Stop or narrow any section that becomes a repository tour, a generic AI-governance essay, or a compliance argument.
- Traces to: `.nuclear/charter.md`; user direction to proceed with the white paper.

## Questioning-attitude summary

- Decision question: Can the public baseline support a practitioner technical white paper describing a coherent method and feasibility evidence without overstating novelty or efficacy?
- Evidence that would change the decision: Closest primary-source prior art that already centers the same integrated contribution; unsupported or unverifiable source claims; inability to demonstrate the method with public artifacts.
- Assumptions that changed the mode: A draft can be reversed, but its claims are intended for external trust and therefore need source, evidence, and assurance-boundary review.
- Facts still needing validation: External prior-art completeness; publication venue requirements; independent reviewer feedback; final DOI/archive route.
- Stop or hold conditions: Any unsupported priority claim, compliance implication, invented result, broken citation, or attempt to publish before human approval.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Academic preprint | Public claim-bearing documentation | Current canonical publication candidate | `docs/06-publications/arxiv/paper.tex` |
| Superseded practitioner manuscript | Editorial history | Must remain clearly labeled superseded | `docs/06-publications/nuclear-grade-context-engineering-white-paper.md` |
| Source lineage | Public citations | Every external influence must be public, linkable, and bounded | `docs/00-standards-foundation/source-map.md` |
| Method and terminology | Controlled doctrine | Paper and repository must use the same custody/coupling model | `README.md`, `CORE.md`, `CONTEXT.md`, `docs/02-operating-system/` |
| Evaluation claims | Evidence | Current study is author-judged and qualitative | `docs/03-worked-examples/skill-workflow-comparison/` |
| Templates and worked example | Operational records | Custody and coupling must be usable rather than paper-only | `templates/`, `docs/03-worked-examples/ai-agent-tool-permissions/` |
| Validator, CLI, MCP, tests, and CI | Executable structural check | Strict mode must fail closed on malformed declarations while preserving legacy compatibility; in-repository CI is not represented as immutable enforcement | `nuclear_grade/`, `tests/`, `.github/workflows/ci.yml` |
| Skills, commands, and starter kits | Practitioner guidance | Generated and adoption surfaces must match current doctrine | `skills/`, `commands/`, `starter-kit/` |
| PDF/text derivatives | Publication artifacts | Must match the manuscript and remain draft-labeled | `dist/white-paper/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Overclaiming could weaken credibility; no operational system changes. |
| Reversibility | high | Local draft and branch can be deleted or reverted immediately. |
| Detectability | medium | Polished prose can conceal unsupported implications. |
| Exposure | medium | Draft is intended for external publication but is not published by this change. |
| Uncertainty | medium | Related-work completeness and independent review remain open. |
| Dependency trust | medium | Relies on public external sources and repository evidence. |
| AI authority | low | AI may draft, commit, push the authorized branch, and open the requested PR; it may not merge, submit to a venue, mint a DOI, or approve its own publication claims. |
| Controllability | high | Human review occurs before any public release. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | not applicable |
| Known procedure where following the steps matters | yes | contribution ledger, source check, claim scan, packet validation |
| New or uncertain work where the assumptions may be wrong | yes | primary-source research and independent review |
| Work that was interrupted, resumed, or handed off | yes | packet and manuscript status; delegated research treated as input, not authority |
| A high-stakes critical action | no | publication itself is excluded and requires a later human gate |

## Selected mode

- Mode: Standard
- Why this mode: The manuscript is a lasting public-claim artifact with multiple sources, evidence limits, and a future release decision.
- Why lighter mode is not enough: A Quick proof cannot capture the contribution ledger, source lineage, worked example, evaluation caveats, and publication boundary.
- Why heavier mode is not yet required: This change creates a local discussion draft only; no release, customer assurance, regulated use, or irreversible action occurs.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Decision screen is captured above. | Ben Huffer |
| `basis.md` | yes | Defines bounded claims and publication requirements. | Ben Huffer |
| `verification.md` | yes | Records source, structure, evidence, and claim checks. | Ben Huffer |
| `ship.md` | yes | Holds publication at draft/defer until human review. | Ben Huffer |
| `turnover.md` | no | Packet and git branch carry the current state. | — |
| `self-check.md` | no | Verification record carries the claim and source checks. | — |
| `supplier-trust.md` | no | No dependency/model adoption decision. | — |
| Nuclear subset record | no | No regulated or operational use. | — |

## Immediate evidence obligations

- Minimum evidence before build: Public baseline confirmed; canonical doctrine, evaluation, worked example, disclaimer, and source map inspected.
- Minimum evidence before merge/release: Manuscript structure check, link check, source-lineage review, assurance-claim scan, repository doctor, token budget, full tests, PDF visual inspection, and independent human editorial review.
- Independent review needed? yes; a human author must approve the contribution claims, sources, and release posture before publication.

## Required links

- Packet: `.nuclear/changes/white-paper-draft/`
- Basis: `basis.md`
- Verification: `verification.md`
- Ship: `ship.md`
- Source map: `../../../docs/00-standards-foundation/source-map.md`
- Crosswalk: `../../../docs/01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- The mode is justified.
- The activated artifacts are named.
- Important risks, assumptions, and evidence obligations are visible.
- The manuscript remains a discussion draft until human approval.

## Source-lineage note

Nuclear-grade change record using the repository's public graded-rigor, configuration-management, software-assurance, and claims-discipline sources. No compliance claim is made.
