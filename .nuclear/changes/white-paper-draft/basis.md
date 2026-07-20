# White Paper Draft — Basis

**Purpose:** Define what the manuscript must establish, what it must not imply, and what evidence each contribution claim requires.

**Activation threshold:** Standard mode applies because the change contains lasting public claims about a bounded method, related work, implementation, preliminary evaluation, and executable validator behavior.

**Minimum useful version:** A bounded thesis, explicit contribution claims, evidence and source duties, one worked example, limitations, and a safe publication status.

**Overhead trap:** This is a claims basis, not a duplicate outline.

---

## Change context

- Slug: `white-paper-draft`
- Related risk record: `risk.md`
- Owner: Ben Huffer / FlyFission
- Date: 2026-07-19
- Decision this basis supports: Whether the method is ready for external editorial review in both practitioner-white-paper and academic-preprint forms.

## Mission / need

AI coding agents can change code, instructions, tools, dependencies, evidence, and release narratives. Existing context-engineering work often centers capability and task completion. The paper must explain and demonstrate a complementary specialization: engineering context for accountability at trust-bearing decisions.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Defensible contribution | Novelty must rest on synthesis, operational formulation, and implementation, not invented components. | Related-work matrix and contribution ledger. |
| Honest evidence posture | Preliminary qualitative evidence must not become an efficacy claim. | Methodology, results, and harness limitations quoted accurately. |
| Source integrity | Direct influences must be public, linkable, and described as influences. | Source map, official URLs, and citation review. |
| Assurance boundary | “Nuclear-grade” must not imply formal nuclear QA, compliance, certification, or safety. | Disclaimer, boundary section, and prohibited-claim scan. |
| Reader utility | A practitioner should understand when and how to use the method. | Clear model, packet example, adoption thresholds, and implementation links. |
| Academic portability | A preprint reviewer should receive conventional LaTeX source, structured citations, and a reproducible source archive rather than a branded report PDF. | Academic article structure, generated bibliography, clean source-package build, and arXiv checklist. |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| The paper claims the method is first, proven, validated, or defect-reducing. | insufficiency | Credibility loss and unsupported reliance. | Contribution ledger, claims guardrail, human review. |
| Source lineage is mistaken for compliance or endorsement. | insufficiency | Miscalibrated regulated or enterprise use. | Explicit influence wording and non-compliance boundary. |
| Author-scored trials are presented as controlled empirical evidence. | fault | False effectiveness claim. | Dedicated limitations and threats-to-validity section. |
| The manuscript becomes a comprehensive repository manual. | insufficiency | Thesis dilution and unreadable publication. | Center evidence custody and actor–evidence coupling; use one worked example. |
| PDF diverges from the source manuscript. | fault | Inconsistent public artifact. | Generate from the canonical draft and compare headings, links, and page content. |
| Practitioner and academic versions make materially different load-bearing claims. | fault | Reviewers receive inconsistent contribution or evidence boundaries. | Keep the thesis, claims, evidence limits, assessed baseline, and publication posture aligned; revalidate both after material edits. |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| The work has separate practitioner and academic-preprint expressions, neither of which is an empirical efficacy paper. | decision authority | User-approved practitioner concept, later academic-format request, and current evidence limits | Independent controlled evaluation becomes available | Ben Huffer |
| The sharpest contribution is explicit evidence custody plus multidimensional actor–evidence coupling within repository-native software acceptance. | assumption | Exhaustive novelty review, competing-systems audit, repository doctrine, and peer crosswalk | Primary prior art shows the same bounded bundle is already centered | Ben Huffer |
| Public, open sources are the direct lineage boundary. | fact | `DISCLAIMER.md` and source foundation | Author explicitly changes the publication policy | Ben Huffer |
| Pre-change baseline is `origin/main` at `7144831`; new implementation claims apply only to the candidate revision in this PR. | local proof | Git fetch and revision check | Candidate revision or base changes before merge | Ben Huffer |
| AI-assisted drafting does not count as independent verification. | decision authority | Evidence-custody and coupling doctrine | A verifier with sufficiently separated custody authors the decisive review | Ben Huffer |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The repository implements packets, CLI checks, tests, CI, skills, commands, and worked examples. | local proof | Public tree and testable repository | Supports feasibility/implementation claim. |
| The twelve-scenario comparison is author-judged and qualitative. | fact | Comparison methodology and results summary | Blocks empirical superiority claims. |
| Context engineering commonly addresses instructions, knowledge, tools, memory, state, and queries. | source claim | Public context-engineering survey cited in the repo | Grounds neighboring field, not a Nuclear-grade result. |
| Configuration management, graded rigor, independent V&V, traceability, and assurance cases are prior art. | source claim | DOE/NRC/NASA/NIST and assurance-case sources | Requires explicit credit and narrows novelty. |
| The bounded custody/coupling bundle is a differentiated synthesis and reference implementation. | assumption | Exhaustive novelty review and competing-systems audit | Must remain a bounded synthesis claim, not “first” or foundational invention. |

## Interfaces and trust boundaries

- Internal interfaces affected: Doctrine, source map, evaluation records, worked example, templates, validator/CLI/MCP behavior, tests, skills, generated command cards, starter kits, CI, and publication records.
- External services/APIs affected: Public source URLs only; no external writes.
- Data classes affected: Public repository text and public research sources.
- Human approval boundaries: Ben Huffer approves thesis, contribution language, authorship, venue, and publication.
- AI/model/tool authority boundaries: AI may research, draft, format, run local checks, commit, push the authorized branch, and open the requested PR; it may not merge, submit to a venue, release, mint a DOI, approve publication, or claim independent verification.

## Dependency / model / supplier intended use

Not activated. AI drafting tools are disclosed as process assistance, not relied upon as verification evidence.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE MANUSCRIPT SHALL argue that consequential context engineering should optimize accountability as well as task completion. | Publication thesis | Abstract, introduction, design requirements, conclusion | Editorial review against thesis. |
| REQ-002 | THE MANUSCRIPT SHALL distinguish established components from differentiated synthesis, bounded operational formulation, and implementation. | Novelty integrity | Contribution ledger and related-work section | Primary-source matrix and claim scan. |
| REQ-003 | THE MANUSCRIPT SHALL center evidence custody and a five-axis actor–evidence coupling profile without reducing the axes to a score or rung. | Sharpest bounded contribution | Dedicated conceptual section, custody path, and non-ordinal profile | Doctrine trace, exhaustive novelty review, and external prior-art stress test. |
| REQ-004 | THE MANUSCRIPT SHALL explain graded rigor, controlled agent operating envelopes, Verdict versus apply-clearance, and Git-native packets without implying formal assurance. | Method completeness | Method and implementation sections | Repo trace, boundary scan, human review. |
| REQ-005 | THE MANUSCRIPT SHALL demonstrate the method with the public agent-tool-permissions example and accurately bound what its tests prove. | Feasibility evidence | Worked-example section | Packet links and local test rerun. |
| REQ-006 | THE MANUSCRIPT SHALL report the twelve-scenario comparison and efficacy harness as preliminary design evidence with explicit limitations. | Evidence integrity | Evaluation and threats-to-validity sections | Method/results/harness trace. |
| REQ-007 | THE MANUSCRIPT SHALL cite public primary sources and include stable repository/version references. | Source integrity | Linked references and assessed-baseline note | Link/source review. |
| REQ-008 | BOTH MANUSCRIPT FORMS SHALL remain labeled as discussion drafts; the academic form SHALL include a self-contained LaTeX source package; neither form SHALL be represented as final or submitted to a venue by this change. | Decision authority and venue portability | Front matter, `docs/06-publications/arxiv/`, clean build, and `ship.md` split PR clearance from publication clearance | Human publication gate plus arXiv Preview at submission time. |
| REQ-009 | THE REPOSITORY SHALL operationalize the research through doctrine, templates, a worked example, opt-in strict validation, MCP/CLI wiring, tests, source maps, starter kits, and an external-enforcement roadmap. | Research-to-repository productization | Custody tables, five-axis profiles, structural consistency checks, compatibility mode, migrated examples, and explicit limits on PR-controlled enforcement | Full tests, Ruff, doctor, token/eval checks, strict packet validation, adversarial review, and CI YAML validation. |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | Abstract and introduction |
| Architecture — shape and major parts | yes | Method and implementation sections |
| Components and interfaces — boundaries above | yes | Authority, packets, and implementation sections |
| Data models — shapes, classes, ownership | yes | `CONTEXT.md` and `docs/02-operating-system/acceptance-graph-domain-model.md` describe a derived Git-native projection; no graph service is implemented |
| Error handling — failure paths and responses | yes | Evidence custody/coupling doctrine, strict-validator diagnostics, and limitations |
| Testing strategy — how each claim is checked | yes | Evaluation, threats to validity, and `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Current academic preprint: `../../../docs/06-publications/arxiv/paper.tex`
- Superseded practitioner draft retained for history: `../../../docs/06-publications/nuclear-grade-context-engineering-white-paper.md`
- Focused related-work matrix: `../../../docs/06-publications/research/related-work-matrix.md`
- Editorial and claims review: `../../../docs/06-publications/research/editorial-review-v0.1.md`
- Source map: `../../../docs/00-standards-foundation/source-map.md`
- Related-work crosswalk: `../../../docs/01-field-guide/context-engineering-literature-crosswalk.md`

## Exit criteria

- The author and reviewer can answer what the paper contributes and what it does not establish.
- Protected and unacceptable outcomes are explicit.
- Assumptions carry invalidation triggers.
- Requirements flow into `verification.md`.

## Source-lineage note

This basis uses the repository's claims-discipline workflow and public source foundation. It defines publication and implementation claims; it does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
