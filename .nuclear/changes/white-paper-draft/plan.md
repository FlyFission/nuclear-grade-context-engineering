# White Paper Draft — Plan

**Purpose:** Produce a bounded manuscript, propagate the research into executable repository surfaces, and open an authorized review PR without merging or submitting the paper to a venue.

**Activation threshold:** Standard mode applies because the work is multi-step, source-backed, claim-bearing, and intended for external review.

**Minimum useful version:** Source inspection, contribution ledger, manuscript, independent review inputs, verification, and draft artifacts.

**Overhead trap:** Do not add publication infrastructure that does not improve this draft.

---

## Change context

- Slug: `white-paper-draft`
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Ben Huffer / FlyFission
- Date: 2026-07-19
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: questioning attitude, evidence over persuasion, graded rigor, technical depth, honest reporting, controlled baseline.

No non-goal or charter boundary is authorized to be crossed.

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Confirm public baseline and canonical repo sources | REQ-002–REQ-007 | none | `README.md`; selected `docs/`; evaluation records | Baseline/source inventory | Git revision and file inspection | Sources and limits are known |
| 2 | Research closest primary-source prior art | REQ-002, REQ-003, REQ-007 | step 1 | source map and targeted public sources; concise matrix | `docs/06-publications/research/related-work-matrix.md` | URLs, dates, relevance, safe wording | Closest neighbors are represented or marked gap |
| 3 | Draft the practitioner manuscript | REQ-001–REQ-008 | steps 1–2 | basis requirements and canonical docs | `docs/06-publications/nuclear-grade-context-engineering-white-paper.md` | Requirement/headings/source self-check | Complete discussion draft, later marked superseded when the academic preprint becomes current |
| 4 | Run editorial/claim review | REQ-002–REQ-008 | step 3 | manuscript plus source matrix | `docs/06-publications/research/editorial-review-v0.1.md` | Actor review is labeled non-independent; publication gaps carried | Findings resolved or carried as gaps |
| 5 | Render historical practitioner artifacts | REQ-008 | step 4 | superseded practitioner manuscript | Historical PDF and text copies in `dist/white-paper/` | File inspection and superseded-label review | Historical artifacts remain clearly non-current |
| 6 | Verify and defer venue publication | REQ-001–REQ-008 | steps 1–5 | packet, manuscript, artifacts | `verification.md`, `ship.md` | tests, doctor, tokens, link/claim scans | Draft remains non-final and venue submission remains held |
| 7 | Restructure for academic preprint | REQ-001–REQ-008 | steps 1–6 | practitioner manuscript, source matrix, official arXiv guidance | `docs/06-publications/arxiv/paper.tex`, `references.bib` | Academic article structure, formal citations, bounded evidence language | Conventional preprint source exists without replacing the practitioner artifact |
| 8 | Compile and inspect the LaTeX preprint | REQ-008 | step 7 | LaTeX source and bibliography | 19-page v0.3 academic PDF candidate | Tectonic build, clean build, citation closure, metadata inspection, and all-page visual QA | No fatal, undefined, citation, or package errors; four non-blocking underfull-box warnings; no layout blockers |
| 9 | Package arXiv-compatible source | REQ-008 | step 8 | `paper.tex`, generated `paper.bbl`, `references.bib` | minimal `.tar.gz`, metadata, checklist | clean extraction and compilation with no hidden/local dependencies | Package is ready for human review and later arXiv Preview; no submission occurs |
| 10 | Productize research through repository surfaces | REQ-003, REQ-009 | steps 2, 7–9 | exhaustive review, current doctrine, templates, validator, skills, example | custody/coupling doctrine; Standard/Quick records; validator/CLI/MCP/tests; starter kits; external-enforcement roadmap; derived-graph design | adversarial tests, full suite, Ruff, doctor, token/eval checks, strict validation | Current surfaces match the bounded contribution without overstating PR-controlled enforcement or platform scope |
| 11 | Review, commit, push, and open PR | REQ-001–REQ-009 | steps 1–10 | staged tree, independent reviews, user authorization | verified branch and GitHub PR | independent blocker review, credential scan, strict packet validation, CI | PR opened; merge, release, DOI, and venue submission remain held |

Model-mediated work uses the current Hermes drafting session. The manuscript and tool outputs are reproducible only to the extent represented by committed source files and deterministic checks; prose judgment remains human-reviewed.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Read repository and primary sources; test thesis alternatives | No external publication or release claim |
| candidate | Write manuscript and local derivatives | Requirements and boundary wording present |
| audit | Independent review, source/link checks, tests, visual inspection | Gaps resolved or explicitly carried |
| accept | Human author decides whether to revise, circulate, or publish later | Separate release decision and publication workstream |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| State novelty | Confuse component prior art with integration novelty | Unsupported priority claim | Contribution ledger and falsification-oriented research | Related-work matrix and claim scan |
| Report evaluation | Turn author judgment into effectiveness proof | Misleading paper | Quote methodology limits and include threats to validity | Evaluation trace |
| Use nuclear sources | Imply compliance or regulated adequacy | Miscalibrated trust | Influence-only wording and disclaimer | Boundary scan and human review |
| Render PDF | Source and derivative drift | Conflicting artifacts | Generate from canonical source and compare headings/links | PDF/text checks |

## Agent briefing

- Role: Researcher, writer, repository implementer, and authorized PR operator—not merger, venue publisher, or independent decider.
- Authority source: User request plus this packet.
- Active procedure/template: Standard packet, source-claim check, legal/safety wording check, publication-readiness audit.
- Last completed action if resumed: Pre-change baseline confirmed at `7144831`; candidate branch contains the repository and publication updates under review.
- Handoff or turnover needed? no; packet is the current-state record.
- Pause when unsure condition: Unsupported novelty, efficacy, compliance, source, or publication claim.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `docs/06-publications/nuclear-grade-context-engineering-white-paper.md` | create, then supersede | REQ-001–REQ-008 | Practitioner draft retained as labeled editorial history | Ben Huffer |
| `docs/06-publications/arxiv/paper.tex` | create/update | REQ-001–REQ-009 | Current canonical publication candidate | Ben Huffer |
| `docs/06-publications/research/related-work-matrix.md` | create | REQ-002, REQ-003, REQ-007 | Closest-source overlap and contribution guardrail | Ben Huffer |
| `docs/06-publications/research/editorial-review-v0.1.md` | create | REQ-001–REQ-008 | Editorial findings and publication blockers | Ben Huffer |
| `.nuclear/changes/white-paper-draft/*` | create/fill | all | Decision and evidence record | Ben Huffer |
| `dist/white-paper/*.pdf` | create, untracked or ignored as appropriate | REQ-008 | Reviewable rendered draft | Ben Huffer |
| `dist/white-paper/*.txt` | create | REQ-008 | Discord-safe text attachment | Ben Huffer |
| `docs/06-publications/arxiv/paper.tex` | create | REQ-001–REQ-008 | Academic preprint manuscript and top-level arXiv source | Ben Huffer |
| `docs/06-publications/arxiv/references.bib` and `paper.bbl` | create | REQ-002, REQ-007, REQ-008 | Structured references and portable generated bibliography | Ben Huffer |
| `docs/06-publications/arxiv/README.md`, `ARXIV-CHECKLIST.md`, `arxiv-metadata.txt` | create | REQ-008 | Build, packaging, and copy-ready metadata instructions | Ben Huffer |
| `dist/white-paper/*arXiv*` | create | REQ-008 | Academic review PDF, text derivative, and minimal source archive | Ben Huffer |
| `CONTEXT.md`; `docs/02-operating-system/*`; root/public docs | create/update | REQ-003, REQ-009 | Canonical custody/coupling doctrine, bounded claims, lifecycle, glossary, source map, and derived domain model | Ben Huffer |
| `templates/`; worked example; `starter-kit/` | update | REQ-009 | Operational custody records, coupling profiles, migration guidance, and dogfooding | Ben Huffer |
| `nuclear_grade/`; `tests/`; `.github/workflows/ci.yml` | update | REQ-009 | Opt-in structural validation, CLI/MCP wiring, adversarial tests, normal compatibility checks, and explicit limits on protected enforcement | Ben Huffer |
| `skills/`; generated `commands/` | update/regenerate | REQ-009 | Practitioner workflow and command-card alignment | Ben Huffer |
| `agents/`; `hooks/session_start.py` | update | REQ-003, REQ-009 | Role boundaries, observer/judge custody language, and actor-controlled hook wording | Ben Huffer |
| `README.md`; `ROADMAP.md`; `CHANGELOG.md`; `CITATION.cff`; contribution/positioning records | update | REQ-002, REQ-003, REQ-006, REQ-009 | Public contribution, efficacy, migration, and release boundaries | Ben Huffer |

## Non-goals

- No merge, tag, GitHub release, DOI, website publication, or arXiv/venue submission. Commit, branch push, and PR creation are explicitly authorized.
- No claim that the method improves defects, safety, security, compliance, or production outcomes.
- No graph database, web platform, generalized ontology service, broad workflow engine, or claim that structural validation authenticates identities or establishes adequacy.
- No attempt to summarize every source or artifact in the repository.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Publication source format | Markdown practitioner manuscript plus a separately restructured LaTeX academic preprint | Word-first or PDF-only | The two genres require different structures; both remain versionable and reviewable | A load-bearing claim changes in either manuscript |
| PDF format | Vector/selectable text from canonical source | Rasterized pages | Reviewability, accessibility, search | Rendering tool cannot preserve links/text |
| Research boundary | Public primary sources | Paywalled/proprietary direct lineage | Existing repo policy | Author changes source policy |
| Academic compiler | Tectonic 0.16.9 for local verification; standard article-class source intended for arXiv TeX Live | Unverified PDF-only upload | Produces a reproducible local PDF and generated `paper.bbl` without shell escape or custom styles | arXiv TeX Live Preview differs or reports an unavailable package |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | User approved the white-paper concept; detailed claim requirements await manuscript review. | pass with later editorial review |
| Design approved | Outline follows the approved thesis and contribution seam. | pass for drafting |
| Tasks approved | Plan is bounded to draft/review/render; no publication. | pass for drafting |
| Specification reviewed | Protected outcomes, non-goals, assumptions, and evidence duties are explicit. | pass |
| Tests/evals defined | Each contribution/evidence claim maps to source or repository evidence. | pass |
| Build complete | Manuscript and derivatives exist. | pass |
| Verification complete | Checks and independent review findings are recorded. | pass with contribution-review gaps carried |
| Release decision ready | Draft circulation/publication decision belongs to the human author. | pass: defer public publication |
| Turnover complete if activated | Not activated. | not applicable |

## Rollback approach

- Rollback method: Before merge, close the PR and delete the branch; after merge, revert the commit through normal review.
- State/data reversal notes: The branch and PR are the only authorized external state changes; no release, DOI, or venue submission occurs.
- Feature flag / kill switch: Not applicable.
- Owner: Ben Huffer.
- Time to restore estimate: Immediate local revert before push; branch deletion or PR closure after push; venue publication remains excluded.

## Proof commands

```bash
python tools/ng.py validate .nuclear/changes/white-paper-draft --strict-custody
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
git diff --cached --check
$HOME/.local/bin/tectonic -X compile --keep-intermediates --keep-logs docs/06-publications/arxiv/paper.tex
```

Manual checks: link inventory, contribution/assurance-claim scan, source trace, PDF visual inspection, and human editorial review.

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Current academic preprint: `../../../docs/06-publications/arxiv/paper.tex`
- Superseded practitioner draft retained for history: `../../../docs/06-publications/nuclear-grade-context-engineering-white-paper.md`

## Exit criteria

- Work remains bounded to a discussion draft.
- Review checkpoints and human publication authority are explicit.
- Deterministic and judgment-based checks are separated.
- Rollback is explicit and the authorized PR is not confused with merge, release, or venue publication.

## Source-lineage note

Nuclear-grade plan using the repository's lifecycle, source-lineage, claims, verification, and release-readiness practices mapped in `../../../docs/00-standards-foundation/source-map.md`. No compliance claim is made.
