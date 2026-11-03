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
| V-2 | Unit tests for the rule | `python -m pytest -q tests/test_two_party.py` | same | pass; 19 tests covering custody self-check, independent custody row, placeholder verifier, fail-closed, default-mode opt-in, `C-004a` ids, section skipping, Quick-mode rejection, worked example both ways | `../../../tests/test_two_party.py` |
| V-3 | Repo sweep under the new flag | `ng_validate <packet> --two-party` over all 57 pre-existing packets | same | First run: 55 fail, 2 pass. Both passes had no claim-table rows and passed vacuously, so the fail-closed rule was added; the re-run gives 57 of 57 fail. The worked example fails with "every declared verifier is empty" for `C-001` and `C-004a` | session output |
| V-4 | Default-mode regression | each packet validated by this branch and by a `git worktree` of `main`, output hashed | same | 57/57 identical (default); 57/57 identical (`--strict-custody`) | session output |
| V-5 | Quotation check | App B fetched from the eCFR versioner API and from Cornell LII; DOE-HDBK-1028-2009 Vol. 2 PDF fetched from energy.gov and text-extracted | network, 2026-11-03 | App B Criterion III, X, and XVIII text identical across both copies and matches every quote; HDBK "Independence exists when the verifier has freedom of thought from the performer." matches | session output |
| V-6 | Catalog surfaces | `ng gen-commands`; diagram rebuilt and rendered to PNG and viewed | same | 31 cards; `skill-map.svg` shows the new node with no overlap | session output |
| V-7 | Audit spot-check | `declaring-intent` vs `double-checking-before-acting` When to Use; `grep NUCLEAR-GRADE-CLOSED:`; v1c rows; CM record co-use | same | all 4 match the report | session output |
| V-8 | Independent review (agent) | see the section below | fresh-context agent | see below | below |

## Independent review (agent)

In progress when this record was first committed. Findings, and what was done about each, are added in a follow-up commit on this branch.

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
