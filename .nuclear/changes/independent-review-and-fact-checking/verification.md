# Independent Review and Fact Checking — Verification

## Verification context

- Slug: independent-review-and-fact-checking
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-11-03
- Verification scope: the five requirements in `basis.md`, on branch `claude/independent-review-fact-check`.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test + alternate method | Author's unit tests (V-2), plus the reviewer's own adversarial tests built separately (V-8) | Every branch of the rule exercised; worked example fails `--two-party` with the expected reason | pass | `../../../tests/test_two_party.py`; V-2, V-3, V-8 | Identity aliasing is out of scope by design (`basis.md` non-goals) |
| REQ-002 | local proof | alternate method | Validator output for every packet compared byte for byte against a `main` worktree, default and `--strict-custody` | 57 of 57 identical in both modes | pass | V-4 | none |
| REQ-003 | source claim | alternate method | Quotes compared across two independent copies of App B; the HDBK quote taken from the DOE PDF; re-fetched by the reviewer | Exact match | pass | V-5, V-8 | The HDBK was checked against one copy (DOE's own PDF) only |
| REQ-004 | local proof | deterministic test | Contract, parity, CLI, and public-doc tests; `doctor`; `tokens`; count grep; rendered diagram viewed | All green; every stated count is 31 | pass | V-1, V-6 | No efficacy measurement for the new skill |
| REQ-005 | local proof | check | Orchestrator spot-checked 4 load-bearing audit claims against source files | Each spot-check matches | pass | V-7 | The remaining audit rows are unchecked by a second party (`gap` below) |
| REQ-005a | local proof | check | Remaining audit rows | Second-party check | gap | `../../../evals/skill-catalog-audit/2026-11-03.md` | Owner to review before any merge packet is opened |

## Verification type guide

| Type | Use when |
|---|---|
| check | a second party follows the originator's path |
| alternate method | the result is reached a second, different way and compared |
| deterministic test | there is repeatable evidence of the behavior |

Full definitions: `../../../docs/02-operating-system/verification-methods-and-depth.md`.

## Commands, evals, and reviews

| ID | Method | Command / review | Environment | Result | Evidence link |
|---|---|---|---|---|---|
| V-1 | Full pre-PR gate | `python -m pytest -q`; `python -m ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions --strict-custody` | Linux container, Python 3.13 | all pass (pytest: 0 failures) | session output |
| V-2 | Unit tests for the rule | `python -m pytest -q tests/test_two_party.py` | same | pass; 41 tests, including the review regressions, covering custody self-check, independent custody row, placeholder verifier, fail-closed, default-mode opt-in, `C-004a` ids, section skipping, Quick-mode rejection, worked example both ways | `../../../tests/test_two_party.py` |
| V-3 | Repo sweep under the new flag | `ng_validate <packet> --two-party` over all 57 pre-existing packets | same | First run: 55 fail, 2 pass. Both passes had no claim-table rows and passed vacuously, so the fail-closed rule was added. After the review fixes (R-1 to R-4), 56 fail and 1 passes legitimately (`trust-propagation-two-party`, a declared authorship table). The worked example fails with "every declared verifier is empty" for `C-001` and `C-004a` | session output |
| V-4 | Default-mode regression | each packet validated by this branch and by a `git worktree` of `main`, output hashed | same | 57/57 identical (default); 57/57 identical (`--strict-custody`) | session output |
| V-5 | Quotation check | App B fetched from the eCFR versioner API and from Cornell LII; DOE-HDBK-1028-2009 Vol. 2 PDF fetched from energy.gov and text-extracted | network, 2026-11-03 | App B Criterion III, X, and XVIII text identical across both copies and matches every quote; HDBK "Independence exists when the verifier has freedom of thought from the performer." matches | session output |
| V-6 | Catalog surfaces | `ng gen-commands`; diagram rebuilt and rendered to PNG and viewed | same | 31 cards; `skill-map.svg` shows the new node with no overlap | session output |
| V-7 | Audit spot-check | `declaring-intent` vs `double-checking-before-acting` When to Use; `grep NUCLEAR-GRADE-CLOSED:`; v1c rows; CM record co-use | same | all 4 match the report | session output |
| V-8 | Independent review (agent) | see the section below | fresh-context agent | 2 blockers and 4 should-fix findings, all reproduced and fixed; 1 kept by design | below |

## Independent review (agent)

A second agent instance in a fresh context, briefed from `basis.md` without the author's conclusions or test results. Methods that differed from the author's:

- 30 adversarial packets of its own design;
- a default-mode comparison against a separate `main` worktree;
- fresh fetches of the eCFR XML and the DOE Vol. 2 PDF.

Its design judgments and skill review were re-reading, so they count as a check, not an independent review. Disposition: **two blocking findings**. The author reproduced every finding with the reviewer's probe script before changing code.

| # | Severity | Finding | Verified by author? | Disposition |
|---|---|---|---|---|
| R-1 | blocker | `--two-party` passed vacuously when claim rows used formatting the parser missed: `**pass**`, `pass (local)`, `pass — 4 passed`, or ids in backticks, bold, links, or `C-001:` | yes, cases 10–16 | fixed. Claim tables are located by header; cells are normalized; a status is read by its leading word; strict fails an unreadable status and a custody-cited claim missing from the claim table. Regression tests added. |
| R-2 | blocker | An authorship row could name the change actor as verifier, or override a custody row classified `self-check` | yes, cases 20–21 | fixed. Custody governs a claim it covers; an authorship verifier must differ from the author and every packet change actor. Tests added. |
| R-3 | should-fix | Any first-cell token such as `E2E`, `SHA256`, `E-001`, or `V-1` in any table was read as a claim | yes, cases 50–52 | fixed. Only tables with a claim column and a status column are read, and ids must match `RECORD_ID_PATTERN`. |
| R-4 | should-fix | Placeholder verifiers (`TBD.`, `(none)`, `?`, `<reviewer>`, `self`, `the author`, `same process`, the actor with a trailing period) and multi-actor cells (`ben + agent:claude`) slipped through | yes, cases 30–40 | fixed. Punctuation is normalized, the deny-list is wider, angle-bracket placeholders count as empty, and multi-actor cells are split. Tests added. |
| R-5 | should-fix | The doctrine said Appendix B keeps check and verify distinct; it does not ("verifying or checking ... such as"), and DOE-HDBK-1028 defines the pair differently | yes, against the eCFR text and HDBK p. 41 | fixed. The page now says the check/verify definitions are this repo's own, quotes both sources' actual wording, and calls the App B methods examples. The crosswalk, source-map, and skill lineage were reworded. |
| R-6 | nit | The third App B method is "a suitable testing program"; qualification testing applies only in lieu of the others. Peer-check is "before and during", in parallel. | yes | fixed in the doc, source map, and crosswalk |
| R-7 | should-fix | `checking-facts`: the contract required a second means in every mode but Quick skipped it; exact-string match against the same copy is not a second means; Standard was weaker than the doctrine | yes | fixed. Every mode requires the second means, and the mode sets who performs it. The match must be against a second, independently published copy. Standard requires someone other than the author. |
| R-8 | nit | The receipt showed `strict.custody: false` while `--two-party` forced the custody section | yes | fixed. `--two-party` no longer forces custody, so an authorship-only packet can pass strict (case 62) and the receipt is accurate. |
| R-9 | design question | A custody row whose generator and verifier are the same agent, with a human named as change actor, counts as a second party | yes, case 41 | kept by design. An independent reproducer legitimately generates and witnesses their own re-run. Recorded in the module docstring; the owner may decide otherwise. |
| R-10 | not raised | A falsely declared classification (case 42) cannot be detected from the record | n/a | documented limit |

After the fixes, the reviewer's probe script gives: 10–16, 20–21, 30–40 and 60 fail strict; 50, 51 and 62 pass; 52 and 61 fail for the right reason, the honest self-check. Default and `--strict-custody` output for all 57 pre-existing packets is still byte-identical to `main`. Under `--two-party`, 56 fail and 1 passes. The pass is `trust-propagation-two-party`, which declares a `## Claim authorship` table with `maintainer-at-merge` as verifier.

## Evidence custody and coupling

The author is one AI agent session (the "authoring session"). The reviewer was a second agent instance of the same model family, started by the authoring session with a brief written from `basis.md` that withheld the author's conclusions and test results. That gives a fresh context and different methods: its own adversarial tests and its own source fetches. It does not give freedom from the orchestrator, the model family, or the budget. So the reviewer's evidence is classified **self-check** here, and the human owner is the pending second party.

### Custody record

| Evidence ID | Claim ID | Decisive? | Artifact / raw result | Change actor | Generated by | Selected by | Transformed / summarized by | Executed / captured by | Retained by | Presented by | Verified / witnessed by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | REQ-001, REQ-002, REQ-004 | yes | pytest, ruff, doctor, tokens output; the default-mode sweep against `main` | authoring session | authoring session | authoring session | authoring session | authoring session in the container | session transcript; tests in git | authoring session | no separate verifier; reproducible commands only |
| E-002 | REQ-003 | yes | two fetched copies of App B and the DOE PDF text | authoring session | eCFR, Cornell LII, energy.gov | authoring session | authoring session | authoring session | session scratch only, not committed | authoring session | no separate verifier; re-fetch is reproducible |
| E-003 | REQ-001, REQ-003 | yes | reviewer agent's findings, adversarial tests, and source fetches | authoring session | review agent | review agent | review agent | review agent | review agent scratch | authoring session | review agent |
| E-004 | REQ-005 | yes | audit report plus 4 spot-checks | authoring session | audit agent | audit agent | audit agent and authoring session | audit agent | `evals/skill-catalog-audit/2026-11-03.md` | authoring session | authoring session |

### Coupling profile

| Evidence ID | Actor | Context | Mechanism | Authority | Resource | Classification | Admissibility / residual-risk disposition |
|---|---|---|---|---|---|---|---|
| E-001 | coupled; the author ran its own checks | coupled; one session | partially separated; deterministic tests and a byte comparison against `main` | coupled; the author chose what to run | coupled; same container | self-check | admitted for the PR; residual coupling carried in `ship.md` |
| E-002 | coupled; the author fetched and compared | coupled; one session | partially separated; two independent publishers of the same text | coupled; the author chose the sources | coupled; same container | self-check | admitted; re-checked in E-003; carried in `ship.md` |
| E-003 | partially separated; a separate agent instance, same model family | partially separated; fresh window briefed from `basis.md` without the author's conclusions | partially separated; its own tests and fetches, not the author's | coupled; the author wrote the brief and decides what to act on | coupled; same container and budget | self-check | admitted as an in-loop mitigation, not independent verification; human review pending in `ship.md` |
| E-004 | coupled; briefed by the author | partially separated; separate window | coupled; reading and grep | coupled; the author decides what to propose | coupled; same container and budget | self-check | admitted for a proposal only; no skill removed; carried in `ship.md` |

- **Two-party status:** `python tools/ng.py validate .nuclear/changes/independent-review-and-fact-checking --two-party` **fails by design** until the owner adds a custody row naming themselves as verifier of the claims they accept. This packet is meant to show the gate working.
- **Verdict owner:** FlyFission.
- **Minimum profile required by the consequence:** a human second party on the checker change (REQ-001, REQ-002) before merge.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Every requirement has a status.
- The coupling of every decisive evidence row is disclosed and classified.

## Source-lineage note

Original Nuclear-grade verification record inspired by public verification and independent-verification practice mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
