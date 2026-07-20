# White Paper Draft — Verification

**Purpose:** Record whether the manuscript's contribution, method, example, evaluation, source, boundary, and artifact claims have evidence appropriate for a discussion draft.

**Activation threshold:** Standard mode applies because the manuscript is claim-bearing and intended for external review.

**Minimum useful version:** Requirement statuses, source and repo evidence, deterministic checks, independent-review status, and gaps.

**Overhead trap:** Passing repository tests does not verify the manuscript's intellectual contribution; judgment checks remain separate.

---

## Verification context

- Slug: `white-paper-draft`
- Related basis: `basis.md`
- Owner: Ben Huffer / FlyFission
- Date: 2026-07-19
- Verification scope: Practitioner manuscript, academic LaTeX preprint, packet, source links, repository claims, evaluation language, and rendered/package artifacts.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | decision authority + source claim | peer review | Read abstract, introduction, design requirements, and conclusion as one argument | Accountability thesis is consistent and capability is not treated as the only goal | pass for discussion draft | manuscript + `../../../docs/06-publications/research/editorial-review-v0.1.md` | Human final editorial approval remains open |
| REQ-002 | source claim + assumption | independent review | Compare contribution ledger against primary-source matrix and exhaustive novelty review | No “first” claim; established components credited; uncertain seams bounded | pass for bounded synthesis claim | `../../../docs/06-publications/research/exhaustive-novelty-review-2026-07-19.md` + manuscript | Human publication approval and patent/FTO review remain open |
| REQ-003 | bounded operational formulation | independent review | Trace to repo doctrine, competing-systems audit, and close prior art | Custody/coupling formulation is precise and not presented as foundational invention | pass for discussion draft | `../../../docs/02-operating-system/actor-evidence-independence.md` + `../../../docs/06-publications/research/competing-systems-audit-2026-07-19.md` | Empirical efficacy and external human review remain open |
| REQ-004 | local proof + source claim | peer review + deterministic scan | Trace method sections to canonical repo docs; scan prohibited claims | Method matches repo and makes no formal-assurance claim | pass | manuscript + source docs | Final human wording review remains open |
| REQ-005 | local proof | deterministic test + peer review | Re-run workspace-boundary tests and inspect claimed/deferred evidence | Paper says exactly what C-001 proves and what remains deferred | pass | worked example; targeted pytest passed | Does not establish broader method efficacy |
| REQ-006 | local proof | peer review | Compare evaluation section to methodology/results/harness | Author-judged, no panel/timing/defect/A-B result, signal-presence limit all explicit | pass | evaluation docs | Independent evaluation deferred to Version 2 |
| REQ-007 | source claim + local proof | peer review + link check | Confirm URLs, titles, dates/versions, and assessed commit | Direct citations are public and stable enough for a draft | pass | references + git evidence + focused assurance matrix | Generic NRC/NASA links were replaced by exact official PDFs/requirement pages; final release-time link check remains required |
| REQ-008 | decision authority | artifact inspection + clean build | Inspect Markdown and LaTeX source, both PDFs, text derivatives, source archive, metadata, and ship record | Every artifact says discussion draft; LaTeX source is self-contained; no venue submission or representation as final occurs | pass | artifacts + `../../../docs/06-publications/arxiv/` + `ship.md` | Human category, license, merge, and publication decisions deferred |
| REQ-009 | local proof + decision authority | adversarial test + independent review | Inspect doctrine/templates/code/tests/CI/example/starter-kit/roadmap propagation and probe strict validation with malformed inputs | Current repository surfaces expose custody/coupling consistently; malformed rows, IDs, enum choices, and missing roles fail; PR-controlled checks are not mislabeled as immutable enforcement | pass after blocker correction | staged diff + validator tests + independent review record | Structural declarations do not authenticate identity or establish adequacy; mandatory external enforcement and broader packet migration remain staged |

## Verification type guide

- Deterministic checks verify repository structure, links, tests, formatting, and artifact properties.
- Peer review verifies coherence, source use, reader value, and boundary wording.
- Independent review is required for the contribution claim because the drafting actor cannot independently approve its own novelty framing.

## Evidence custody and coupling

Actor identifiers below are declarations, not authenticated identities. Structural validation checks
the record and its internal consistency; it does not establish truth, adequacy, or independence.

| Evidence ID | Claim ID | Decisive? | Artifact / raw result | Change actor | Generated by | Selected by | Transformed / summarized by | Executed / captured by | Retained by | Presented by | Verified / witnessed by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | REQ-004, REQ-005, REQ-008, REQ-009 | yes | Local pytest, Ruff, doctor, token, eval, strict-custody, Tectonic, citation-closure, and visual-QA outputs summarized below | Hermes Agent drafting process | Local deterministic tools invoked by Hermes Agent | Hermes Agent | Hermes Agent; command output summarized | Hermes Agent tool session | Hermes session records and committed source artifacts | Hermes Agent | Hermes Agent self-check; independent review is separately disclosed |

| Evidence ID | Actor | Context | Mechanism | Authority | Resource | Classification | Admissibility / residual-risk disposition |
|---|---|---|---|---|---|---|---|
| E-001 | coupled — the drafting process invoked and selected its own checks | partially separated — deterministic tools constrain some interpretation but inherit actor-selected scope | partially separated — pytest, Ruff, repository validators, and Tectonic are distinct mechanisms but exercise actor-authored artifacts | coupled — Ben authorizes the PR, but the drafting process controls this evidence summary | coupled — the drafting session controls local runtime and evidence presentation | self-check | Admitted for reproducible structural/build claims only; see `ship.md#residual-risks-and-gaps`. It does not establish novelty, efficacy, authenticated identity, or publication approval. |

- Human apply authority: Ben Huffer explicitly authorized committing, pushing, and opening a PR on 2026-07-19.
- Public-paper publication, venue submission, and merge remain separate decisions.

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Packet validation | `python tools/ng.py validate .nuclear/changes/white-paper-draft --strict-custody` | local worktree | pass | `OK: .nuclear/changes/white-paper-draft` |
| Full tests | `python -m pytest -q` | local worktree | pass | 212 tests completed with no failures on the rebased tree |
| Ruff | `python -m ruff check .` | local worktree | pass | `All checks passed!` |
| Repository doctor | `python tools/ng.py doctor .` | local worktree | pass | `OK: Nuclear-grade doctor` |
| Token budget | `python tools/ng.py tokens .` | local worktree | pass | `OK: token budget` |
| Diff whitespace | `git diff --cached --check` | local worktree | pass | No output |
| Credential-pattern scan | Added-line scan for common token/private-key/assigned-secret patterns | staged diff | pass | No candidate credentials found; no secret values printed |
| Worked-example proof | `python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q` | local worktree | pass | Four tests passed |
| Source/link review | Manuscript URLs plus focused agent and assurance matrices | local/public web | pass | Exact NRC PDFs and NASA requirement pages replaced unstable generic links; assurance review checked all 26 official URLs in its scope |
| Boundary review | assurance/source claim scan | local worktree | pass | Hits were negative/disclaimer uses or ordinary uses of “first,” not priority claims |
| PDF content review | `pypdf` extraction and annotations | local artifact | pass | 24 pages; selectable text extracted; 32 URI annotations covering 29 unique links; draft label and closest-source additions present |
| PDF visual review | rasterized samples of cover, TOC, body, tables, evaluation, and references | local artifact | pass | Post-review related-work and final-reference pages were re-inspected; no clipping, broken tables, orphaned headings, or delivery-blocking layout defects observed |
| Academic LaTeX build | clean Tectonic compile from current source | local, Tectonic | pass | 19-page v0.3 candidate; 47 citations and 47 bibliography entries; no missing or uncited entries; four non-blocking underfull-box warnings |
| Clean source-package build | Extract minimal source archive and run Tectonic with `-C` cached-only mode | `/tmp/ng-arxiv-clean` | pass | Archive containing only `paper.tex`, `paper.bbl`, and `references.bib` compiled without source-network or local-path dependencies |
| Academic PDF content review | `pdfinfo` plus citation/bibliography closure check | local artifact | pass | 19 US-Letter pages; correct v0.3 title/author metadata; no JavaScript/encryption; 47/47 citation closure |
| Academic PDF visual review | 19-page rasterized contact sheet | local artifact | pass | No blank pages, clipping, overlap, broken tables/figures, malformed title, or publication-blocking layout defect observed |
| arXiv metadata check | abstract extraction and package checklist | local artifact + official arXiv guidance accessed 2026-07-19 | pass for source candidate | Metadata lists 19 pages, two figures, and five tables; arXiv Preview remains a human submission-time gate |
| Independent staged reviews | Three delegated review rounds plus `codex review --base origin/main` | staged tree | pass after corrections | Reviewers exposed malformed-input false passes, stale baseline/ordinal and packet-scope claims, boolean decisive aliases, and PR-controlled-enforcement overclaim; each blocker was corrected, retested, and independently closure-reviewed |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Unsupported priority claim | Search for “first”, “novel”, “proven”, “validated”, “reduces defects” and inspect context | pass | No priority claim; “first” hits were grammatical or source-title uses; “proven/validated/reduces defects” appear only in explicit non-claims |
| Compliance/assurance implication | Search assurance terms and inspect negative/disclaimer context | pass | Assurance terms occur in boundary or negative sentences |
| Evaluation overclaim | Compare every reported result to methodology limits | pass | Author judgment, missing panel/timing/defect/A-B measures, and harness limits are explicit |
| Source drift/broken links | Extract and check cited URLs | pass | Generic failing government links replaced with exact official documents; repeat immediately before publication |
| PDF/source divergence | Compare headings, page text, links, and draft label | pass | Canonical source copied to text derivative; PDF regenerated from source and inspected |

## AI-assisted work checks

- AI scope: Repository inspection, primary-source research coordination, drafting, editing, local checks, and PDF rendering.
- Model/tool used: Hermes Agent session and delegated research agents; local Git, Python, and rendering tools.
- Permissions/actions allowed: Read public/local files; create files only in the dedicated worktree and review-artifact paths; run local tests/checks; use read-only web access.
- Independent checks performed: Planned delegated research, deterministic repository checks, and visual artifact inspection; human review remains required.
- Self-check / turnover records: This packet; no separate turnover record.
- Hallucination/slop screening: Planned source trace, citation/link check, unsupported-claim scan, and independent editorial review.
- Human approval gates exercised: User approved drafting; publication approval not exercised.

## Security / dependency / supply-chain checks

Not activated. Rendering tools will be locally inspected; no new runtime dependency is added to the repository.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- Current academic preprint: `../../../docs/06-publications/arxiv/paper.tex`
- Superseded practitioner draft retained for history: `../../../docs/06-publications/nuclear-grade-context-engineering-white-paper.md`
- Academic build instructions: `../../../docs/06-publications/arxiv/README.md`
- Academic package checklist: `../../../docs/06-publications/arxiv/ARXIV-CHECKLIST.md`
- Worked example: `../../../docs/03-worked-examples/ai-agent-tool-permissions/README.md`
- Evaluation methodology: `../../../docs/03-worked-examples/skill-workflow-comparison/methodology.md`

## Exit criteria

- Every requirement has a status.
- Deterministic proof is kept separate from editorial and novelty judgment.
- Evidence is linked and gaps are carried into `ship.md`.
- Publication remains blocked until a human approves the claims and final artifact.

## Source-lineage note

Nuclear-grade verification record using public software verification, claims-evidence, source-lineage, and release-readiness concepts mapped in `../../../docs/00-standards-foundation/source-map.md`. It does not establish formal verification and validation, compliance, certification, safety, security, or regulatory adequacy.
