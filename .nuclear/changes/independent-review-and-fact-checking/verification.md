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
| REQ-005 | local proof | check | Orchestrator spot-checked 4 load-bearing audit claims against source files | Each spot-check matches | pass | V-7 | Covers only that the audit exists, cites evidence, and changes nothing. Four clean spot-checks bound the audit's error rate only below about 53% (95%), so its accuracy is carried as REQ-005a |
| REQ-005a | local proof | check | Remaining audit rows, which drive the merge decisions | Each merge re-tested by its own scenario evaluation before any skill is removed | gap | `../../../evals/skill-catalog-audit/2026-11-03.md` | Owner to review before any merge packet is opened |

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
| R-9 | design question | A custody row whose generator and verifier are the same agent, with a human named as change actor, counts as a second party | yes, case 41 | resolved after the external reviews below: still allowed, because an independent reproducer legitimately generates and witnesses their own re-run, but no longer silent. When that is the only second party, the coupling-profile disposition must link `ship.md`, or the check fails. |
| R-10 | not raised | A falsely declared classification (case 42) cannot be detected from the record | n/a | documented limit |

After the fixes, the reviewer's probe script gives: 10–16, 20–21, 30–40 and 60 fail strict; 50, 51 and 62 pass; 52 and 61 fail for the right reason, the honest self-check. Default and `--strict-custody` output for all 57 pre-existing packets is still byte-identical to `main`. Under `--two-party`, 56 fail and 1 passes. The pass is `trust-propagation-two-party`, which declares a `## Claim authorship` table with `maintainer-at-merge` as verifier.

## External review (Codex, on the PR)

A second automated reviewer from a different vendor's model reviewed head `63d84c9` and raised two P2 findings. The author reproduced both before fixing them.

| # | Finding | Reproduced? | Disposition |
|---|---|---|---|
| CX-1 | A multi-verifier cell (`agent:claude + ben`) was compared as one identity, so it counted as a second party against the actors `ben + agent:claude` | yes | fixed: every name in a verifier cell is compared on its own, and at least one non-placeholder name must fall outside the excluded set; test added |
| CX-2 | A single-emphasis claim ID (`*C-001*`, `_C-001_`) was not read, so a `pass` row silently left the gate | yes | fixed: single emphasis is stripped from IDs and statuses; a `pass` row whose claim cell yields no readable ID now fails strict mode instead of being skipped; tests added |

These are the same class of bypass as R-1 and R-4: strict parsing that let ordinary Markdown move a claim out of the gate. A reviewer on a different model family found two the same-family reviewer missed, which is the diversity argument in `docs/02-operating-system/independence-architecture.md` working as written.

A second round (Codex on `1e956bc` and `3adf16c`; Copilot on `1e956bc`) raised more of the same class. The author reproduced each one first, and each passed before its fix.

| # | Finding | Reproduced? | Disposition |
|---|---|---|---|
| CX-3 | `no verifier` and similar negative phrases counted as a named verifier | yes | fixed: cells starting `no `, `not `, `unverified`, and the like name no party; tests added |
| CX-4 | `ben + N/A` split into `n` and `a`, which counted as second parties | yes | fixed: `N/A` is kept whole before splitting, and one-character fragments never count; tests added |
| CX-5 | Authorship rows inside an HTML comment or a fenced example counted | yes | fixed at the root: the parser reads only visible Markdown (comments and fences removed), as the custody parser already did; tests added |
| CX-6 | A claim table without outer pipes was skipped | yes | fixed: GitHub-style tables with a delimiter row are read with or without outer pipes; test added |
| CX-7 | Conflicting duplicate authorship rows: the last row won | yes | fixed: rows naming different parties for one claim fail closed; identical duplicates pass; test added |
| CX-8 | A `## Claim authorship` heading with no readable rows did not opt a packet in | yes | fixed: the heading alone opts in; test added |
| CX-9 | A custody verifier cell naming the generator plus a separate witness (`alice + carol`) needed the R-9 disclosure | yes | fixed: R-9 applies only when every eligible verifier also generated the evidence; test added |
| CX-10 | MCP `two_party` forwarding untested; MCP docstring said "distinct from its evidence author" for custody rows; `trace.md` cited a missing symbol | yes | fixed: MCP test added; docstring now states the custody and authorship rules separately; trace symbol corrected |
| CX-12 | A custody section inside an HTML comment or a fence still exported second parties (Codex on `931448b`) | yes | fixed: `_check_evidence_custody` removes comments and fences before locating the section, as CX-5 does for authorship; test added |
| CX-13 | A four-backtick outer fence was closed by an inner triple-backtick line, exposing example authorship rows (Codex on `c164d8b`) | yes | fixed: the two-party parser now uses the validator's CommonMark fence rule (same character, at least the opening length); a test keeps both implementations in agreement |
| CX-14 | `ben AND agent:claude` was not split, so `agent:claude` passed as verifier (Codex on `c164d8b`) | yes | fixed: the name split is case-insensitive; test added |
| CX-15 | An authorship example indented four spaces still supplied verifiers (Codex on `a6867fa`) | yes | fixed by a general rule rather than another special case: declarations are read strictly, so any line indented four or more spaces is code and counts for nothing, in both the authorship and the custody parser; tests added for both |
| CX-16 | A claim row cut short before its status cell was skipped (Codex on `a6867fa`) | yes | fixed by the matching rule: claims are read generously, so the row is kept with an unreadable status and strict mode fails it; test added |
| CX-17 | A fence opener inside an HTML comment hid the visible claim table after it, because fences were stripped before comments (Codex on `a50edba`) | yes | fixed at the root: one pass tracks comments and fences together, so a marker of either kind inside the other is just hidden text; the custody parser now uses the same function; tests cover both nestings and inline comments |
| CX-18 | A literal `<!--` inside inline code opened a comment and hid a visible claim table (Codex on `9b920ee`) | yes | fixed by closing the class: claims are now read from the raw file, so no markup can hide a claim; declarations stay visible-only. No existing verification file has a claim row inside a comment or fence (40 checked), so nothing else changes; tests cover inline code, comments, fences, and plain text |
| CX-19 | Follow-on from CX-18, found by the author: a literal `<!--` in inline code, or one with no closing `-->`, hid the rest of a file on the declaration side, so this packet's own custody section disappeared | yes | fixed: code spans are skipped and a mid-line `<!--` opens a comment only if a `-->` follows, as Markdown renders it; tests added, including one that this packet passes `--strict-custody`; see the near-miss note below |
| CX-20 | With the status column first, a `| pass |` row cut short before its claim cell was dropped (Codex on `9b920ee`) | yes | fixed: a short row is kept whichever cell it lost, so it reads as a pass row with no readable id and strict mode fails it; test added. Copilot's overview also asked for a CLI `--two-party --json` regression, now added |
| CX-21 | Authorship columns were read by position, so `Claim ID \| Verified by \| Evidence author` made the author the verifier (Codex on `4e951a1`) | yes | fixed: author and verifier columns are found by header in any order; a table whose headers do not name all three roles declares nothing; tests added |
| CX-22 | A role prefix hid a placeholder: `ben + agent:TBD` passed (Codex on `8e23443`) | yes | fixed: the placeholder test also checks the name with any `role:` prefix removed; real prefixed names (`human:carol`) still count; tests added both ways |
| CX-23 | In a table without outer pipes, a pipe-free body line ended the table, hiding it and every later `pass` row (Codex on `ff6f7f2`) | yes | fixed: a delimited table runs to the next blank line or block start, as GitHub Markdown renders it, so the line becomes a one-cell row with an unreadable status; test added |
| CX-24 | A heading containing a pipe (`## Claims \| local`) was absorbed into the table above it, hiding the claim table after it (Codex on `b37030d`) | yes | fixed: a heading, fence, quote, or new table header always ends a table, pipe or not, as GitHub Markdown does; tests added |
| CX-25 | Authorship rows inside `<pre>` still supplied verifiers (Codex on `684fd21`) | yes | fixed for raw HTML as a class: CommonMark HTML blocks are hidden from declarations (`<pre>`, `<script>`, `<style>`, `<textarea>` to the closing tag; any other tag-led block to the next blank line); tests cover four tags and text after a closed block |
| CX-11 | `ben + reviewer` passes against actor `ben` | yes | kept by design: a cell counts when at least one name in it is outside the excluded set, the same rule CX-9 asks for |

Default-mode and `--strict-custody` output stays identical to `main` across all 56 packets (112 runs).

CX-3 to CX-16 are one failure class: a lenient Markdown parser letting text drop out of, or slip into, the gate. After CX-15 the parser follows one stated rule instead of a growing list of cases, and after CX-18 the rule is complete on the claim side. Claims are read from the raw file, so no markup can hide one, and an odd row fails rather than vanishing. Declarations are read strictly, so anything a reader would see as a comment, a fence, or indented code is ignored. Every parsing mistake on either side now fails closed.

## External reviews forwarded by the owner (Grok, ChatGPT)

Each claim was checked against the code before acting.

| # | Source | Point | Checked? | Disposition |
|---|---|---|---|---|
| GX-1 | both | R-9: same agent as generator and verifier can pass as a second party | yes | fixed: allowed only with a `ship.md` disclosure (R-9 above); tests added |
| GX-2 | Grok | Aliases (`Claude`, `claude-opus-5.5`, `assistant`, `me`) fail open | yes, reproduced | fixed: generic names count as no verifier; aliases match by identity root; fails closed and is documented; tests added |
| GX-3 | Grok | Docs should recommend `--two-party` for Standard packets with a pass claim | n/a | done in CLI help, `validators.md`, `cli-reference.md` |
| GX-4 | ChatGPT | Name it a *declared two-party integrity check*; separate actor, evidence, and method independence | n/a | done in CLI help, the module, `validators.md`, and the doctrine page |
| GX-5 | ChatGPT | State the 3/n assumptions; make depth and independence two axes; give alternate-method records a contract | n/a | done in `verification-methods-and-depth.md` |
| GX-6 | ChatGPT | `checking-facts` needs an adversarial efficacy set scored on false acceptance | n/a | deferred: recorded in `ship.md` as a follow-up; no efficacy claim is made |
| GX-7 | ChatGPT | 124-A and 124-B (multi-verifier, single emphasis) | yes | already fixed as CX-1 and CX-2 |
| GX-8 | Gemini | `ben + N/A` split into `n` and `a`; tables without outer pipes; authorship in HTML comments; conflicting duplicate rows; CLI/MCP contract wording | yes | already fixed as CX-4, CX-6, CX-5, CX-7, and CX-10 (the review read an earlier head) |
| GX-9 | Gemini | A vendor or router path (`anthropic/claude-3.5-sonnet`, `openrouter/claude-opus`) split on `/`, so the vendor counted as a second party | yes, reproduced in three forms | fixed: only a spaced ` / ` separates names; an unspaced slash is part of one identifier whose root is its last segment; `agent: x` with a space is also an alias prefix; tests added, including distinct verifiers that must still pass |
| GX-10 | Gemini | Do not require `--two-party` repo-wide yet; scope it to new or modified packets | n/a | agrees with the open owner decision in `ship.md` |
| GX-11 | Gemini | R-9: same-agent generator and verifier should count only as an isolated independent reproduction | n/a | matches the rule as built: a `self-check` classification never counts, an agent named as change actor is excluded, and the remaining case needs the `ship.md` disclosure |

## Near miss during build (OPEX)

While adding the source-map row for the adjudication study, the author wrote author names from memory
("Mathes, Klassen, and Pieper (or as listed)") before reading the record. The check on the next step
found that PubMed's page carried no author meta tags. The author list was then taken from NCBI's
E-utilities record (E, Saldanha, Canner, Schmid, Le, Li) and corrected before commit. This is exactly
the failure `checking-facts` names ("I know this"), and it was caught only because the second lookup was
done. Lesson carried into the skill: a citation's metadata is a fact, and it gets the same primary-source
read as its content.

A second near miss came late in review. The pre-commit check for this packet was run as
`ng validate ... | tail -1 && git add ... && git commit`. Because the pipe's exit status is `tail`'s,
the failing validation ("missing required section: Evidence custody and coupling") printed but did not
stop the commit, and the commit was pushed. The failure was real: the CX-18 row added to this file
contains a literal `<!--` in inline code, and the parser hid everything after it. The author read the
printed line, stopped, fixed the parser so it follows Markdown's rules (a `<!--` in a code span, or one
with no closing `-->`, is text), and added `test_this_change_record_passes_strict_custody` so this
packet must validate under its own rules. Lessons: never pipe a gate through a filter that drops its
exit status; and the parser's first real-world false fail came from its own change record.
Also restored here: this section's heading, which an earlier edit (`3adf16c`) dropped by accident.

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
