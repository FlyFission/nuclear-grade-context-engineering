# Quality / Verdict / Accountability — Verification

## Purpose

Record what was checked, how, and what the check did and did not establish.

## Evidence ledger

| ID | Claim | Check | Result | Status |
|---|---|---|---|---|
| V-1 | The triad is defined once with each collapse named | Read `docs/02-operating-system/quality-verdict-accountability.md`; four collapse rows present, each pointing at existing doctrine that refuses it | Present | pass |
| V-2 | The triad is reachable from headline docs | Terms appear in `CORE.md`, `MAXIMS.md`, `docs/glossary.md` (3 core rows + 1 idiom), `docs/README.md`, `validators.md` §1, `agents/judge.md` | Present | pass |
| V-3 | The archetype lens changes a decision | `archetype-lens.md` carries a mode-floor column for all five archetypes plus the re-grade-on-shift rule and the agent-briefing rule | Present | pass |
| V-4 | Cherny's framing preserved, repo extension not attributed to him | Source-lineage note states the drift/mode-floor/skill mapping is this repo's authored extension | Present | pass |
| V-5 | Token figures never appear without the pass-rate caveat | Scripted scan of every occurrence of `7.1%`, `8.5%`, `7–8%`, `34%` across `docs/`, `skills/`, `MAXIMS.md`, `CORE.md`, checking a ±2-line window for "pass rate" | 5 of 5 occurrences OK, 0 misses | pass |
| V-6 | Vendor affiliation **stated**, not merely pointed at, wherever the statistics are cited | Scan of all 9 citing files for a phrase that asserts the affiliation (`affiliated with`, `vendor-run`, `vendor whose product`, …) rather than the bare word "vendor" | 9 of 9 state it | pass |
| V-6a | The earlier weak form of V-6 | Original scan tested only whether the word "vendor" appeared anywhere in the file | **Produced a false all-clear** — see the note below | superseded |
| V-7 | The three sources are registered under existing citation discipline | New rows in `source-map.md` Tier 6 (Sonar survey), Tier 9 (arXiv:2605.20049), Tier 11 (Cherny), plus a standing vendor-affiliation note under Tier 6 and three `source-to-concept-crosswalk.md` rows | Present | pass |
| V-8 | No new skill added; skill-count invariant intact | `ls -d skills/*/` = 29 (the count `main` arrived at via #81); no skill folder added or removed by this change | 29 folders, unchanged by this PR | pass |
| V-9 | Full test suite **on the tree being accepted** | `python -m pytest -q`, re-run after the rebase and each review round | **317 collected, 0 failed.** Passed/skipped split is environment-dependent — see the note below | pass |
| V-10 | Lint | `python -m ruff check .` | All checks passed | pass |
| V-11 | Repo health and internal link resolution | `python tools/ng.py doctor .` | `OK: Nuclear-grade doctor` | pass |
| V-12 | Token budget not inflated by the new doctrine | `python tools/ng.py tokens .` | `OK: token budget` | pass |
| V-13 | Command-card parity after the skill edit | `python -m pytest -q tests/test_command_parity.py` after regeneration | pass | pass |
| V-14 | External source URLs resolve | Direct fetch attempted | **Blocked by this environment's egress policy** (gateway answered 403 to CONNECT for `sonarsource.com`, `arxiv.org`, `x.com`) | gap |
| V-15 | External figures are accurately stated | Cross-checked against search-result content from the primary pages plus independent secondary coverage (The Register, TFiR, a literature review of the arXiv paper, Hacker News discussion) | Figures corroborated across independent outlets | pass |
| V-16 | This packet satisfies Standard mode including custody disclosure | `python tools/ng.py validate .nuclear/changes/quality-verdict-accountability --strict-custody` | `OK` | pass |
| V-17 | The `mcp` upper bound repairs `mcp-smoke` | Clean venv: `pip install -e ".[mcp]"` then `pytest tests/test_mcp_server.py -q` | mcp resolved to 1.29.0; 13 passed | pass |
| V-18 | The `mcp` break is not caused by this change | `git diff --name-only origin/main..HEAD` before the pin showed markdown only; `main`'s head last passed CI 2026-07-25, before mcp 2.0.0 | Confirmed pre-existing | pass |

## Notes on the failed and partial checks

**V-13 required a correction mid-change.** The first suite run failed `test_cards_are_an_exact_projection_of_their_skills` for `ng-code-review.md`. The plan had assumed the generated command card projects only the skill's `## Prompt` block; it projects more than that, so the `## When to Use` addition put the card out of sync. Fixed by regenerating with `python tools/ng.py gen-commands .` (one-line diff to `commands/ng-code-review.md`). The `## Prompt` block itself was never edited, so the `GOLDEN` byte-for-byte snapshot in `tests/test_command_parity.py` needed no change and still passes.

**A third correction: an unrelated CI break, folded in on the owner's call.** `mcp-smoke` failed on this branch because the optional extra was unbounded and `mcp` 2.0.0 removed `mcp.server.fastmcp`. Reproduced and fixed in a clean environment (V-17) and confirmed pre-existing (V-18). The scope trade-off is argued in `risk.md`; the 2.x port is deliberately not attempted and is carried as a named risk in `ship.md`.

**V-14 is a real gap, not a formality.** This sandbox's network policy denies CONNECT to all three source hosts, so the URLs could not be fetched directly from here. The figures themselves are corroborated (V-15), but *link liveness* is unverified from this environment. A reviewer with unrestricted egress should confirm all four URLs before merge. This is recorded as `gap` rather than `pass` because "the search engine showed me the content" is not the same evidence as "the link resolves."

**Closed: the second maxim now carries the affiliation, not just the caveat.** `MAXIMS.md` originally stated the pass-rate caveat inline and left the vendor disclosure one click away in `token-burn-control.md`. That was recorded here as a partial, judged acceptable for a short quotable entry, and explicitly flagged so a reviewer could disagree. An automated review pass did disagree, on the correct ground: `source-map.md` asserts the affiliation is disclosed *at every citation point*, and the maxim was a citation point. The disclosure is now inline. Recorded rather than quietly amended — the invitation to disagree is only worth something if the disagreement changes the artifact.

**V-6 was a weak check that passed something it should have failed.** The original scan asked only whether the word "vendor" appeared in each citing file. `skills/reviewing-code-quality/SKILL.md` contained the string "boundary and vendor affiliation in `docs/…`" — a *pointer* to the disclosure, not the disclosure — and the scan counted that as a pass. A reviewer caught it, and made the sharper point that this skill is portable: installed or copied outside the repo, the pointer resolves to nothing and the reader gets the flattering number with no conflict-of-interest attached at all. The skill now states the affiliation itself. V-6 has been re-specified to test that each file *asserts* the affiliation rather than mentioning the word, and re-run: 9 of 9.

The lesson is the one this packet is about. A check that greps for a keyword measures vocabulary, not the claim; it produced a green result while the claim was false. That is the quality/verdict collapse in miniature, inside the packet that defines it.

**Source statuses were downgraded after review.** The Sonar and arXiv rows were registered `verified-public` while V-14 recorded that their URLs were never fetched. `source-map.md` defines `verified-public` as *the public page/link checked*, so the rows asserted something the packet simultaneously denied. Both now sit at `public-url-needed` with a status note stating the promotion condition. Corroborating the figures through secondary coverage supports the numbers; it does not discharge a link-checked status. Different claims.

**The recorded suite result is now stated as an invariant, because the raw counts are not one.** V-9 first recorded a pre-rebase count, which a reviewer correctly rejected. The correction recorded `316 passed, 1 skipped` — and a second review pass rejected *that*, reporting `315 passed, 2 skipped` from the same tree. Both numbers are real. The suite has exactly two `importorskip` gates:

| Gate | Location | Skips when |
|---|---|---|
| `mcp` | `tests/test_mcp_server.py:106` | the optional `mcp` extra is not installed |
| `yaml` | `tests/test_ng_cli.py:503` | PyYAML is not installed |

The authoring environment has PyYAML but not `mcp` → 316 passed, 1 skipped. An environment with neither → 315 passed, 2 skipped. Nothing about the tree differs; only what is installed around it.

So the passed/skipped split was never the right thing to record — it is a property of the runner, not of the candidate. What is stable is **317 collected and 0 failed**, and that is what V-9 now asserts. A reviewer reproducing this should compare those two figures, not the split.

## What this verification does not establish

- That the archetype→mode-floor mapping is correct. It is new doctrine with no field use behind it; nothing here tests whether it changes a real grading decision.
- That either statistical finding replicates. Both come from the same commercial vendor and neither has independent replication.
- That the triad is the right decomposition. The tests confirm the terms are defined and reachable, not that the definitions are the best ones. That judgment is the reviewer's.

## Evidence custody and coupling

The agent that selected and summarized the external evidence also wrote the doctrine that evidence supports, and authored this record. See `docs/02-operating-system/actor-evidence-independence.md`.

### Custody record

| Evidence ID | Claim ID | Decisive? | Artifact / raw result | Change actor | Generated by | Selected by | Transformed / summarized by | Executed / captured by | Retained by | Presented by | Verified / witnessed by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | REQ-007 | yes | `pytest -q`, `ruff`, `ng doctor`, `ng tokens` output (V-9 to V-13) | AI agent | repo test suite | test suite, all tests, no selection | not summarized beyond pass and fail | AI agent | git | AI agent | nobody yet; reproducible by any reviewer |
| E-002 | REQ-005 | yes | Scripted caveat and disclosure scans (V-5, V-6) | AI agent | AI agent | AI agent | AI agent | AI agent | packet | AI agent | nobody yet; scan logic stated so it is re-runnable |
| E-003 | REQ-005, REQ-006 | yes | External source figures (V-15) | AI agent | third-party publications | AI agent | AI agent | AI agent | packet | AI agent | nobody; not independently witnessed |
| E-004 | REQ-001, REQ-002, REQ-003, REQ-004 | yes | Readings of the new doctrine pages | AI agent | AI agent | AI agent | AI agent | AI agent | packet | AI agent | nobody; not independently witnessed |

### Coupling profile

Every row classifies as **self-check**. The deterministic checks feel independent because the tooling is standard and reproducible, but the change actor still ran them, chose which to run, and presented the results — and this repo's own rule is that a role label is not independence. Reproducibility is recorded in the disposition, not smuggled into the classification.

| Evidence ID | Actor | Context | Mechanism | Authority | Resource | Classification | Admissibility / residual-risk disposition |
|---|---|---|---|---|---|---|---|
| E-001 | coupled; the agent ran the suite and reported it | partially separated; the suite predates this change and the agent did not author it | partially separated; standard tooling the agent cannot silently alter | partially separated; a human owns merge | separated; no budget pressure shaped the outcome | self-check | admitted; reproducible verbatim by any reviewer, residual risk carried to `ship.md` |
| E-002 | coupled; the agent wrote and ran the scan | coupled; authored and executed in the same session | partially separated; a plain scan over the tree, stated in full | partially separated; a human owns merge | separated; no budget pressure shaped the outcome | self-check | admitted; the scan is stated so a reviewer can re-run it, residual risk carried to `ship.md` |
| E-003 | coupled; the agent chose and paraphrased the sources | coupled; selected and used in the same session | coupled; search-mediated because direct fetch was blocked | partially separated; a human owns merge | coupled; the agent chose how far to verify | self-check | admitted with residual risk; vendor affiliation and the V-14 link gap carried to `ship.md` |
| E-004 | coupled; the agent read pages it wrote | coupled; same session | coupled; unaided reading, no external check | partially separated; a human owns merge | coupled; the agent set its own depth | self-check | admitted only as a claim to re-derive; the reviewer must read the pages, carried to `ship.md` |

- **Evidence pattern used:** actor-selected primary artifacts and actor narrative throughout. No item reaches independent reproduction, because nobody but the change actor has yet run anything.
- **Verdict owner:** human reviewer via PR.
- **Apply-clearance owner:** human reviewer via PR; the authoring agent holds neither.
- **Minimum profile required by the consequence:** additive public documentation with externally sourced claims — deterministic checks reproducible, and every external figure independently re-derivable by a reviewer from its public source. Met for E-001/E-002; E-003 carries the V-14 gap.
- **Any unmet separation carried into `ship.md`:** yes — vendor affiliation of two sources, and unverified link liveness.

## Commands, evals, and reviews

```bash
python -m pytest -q                    # 317 collected, 0 failed (see note on the skip split)
python -m ruff check .                 # All checks passed
python tools/ng.py doctor .            # OK: Nuclear-grade doctor
python tools/ng.py tokens .            # OK: token budget
python tools/ng.py gen-commands .      # regenerated 27 cards; 1-line diff to ng-code-review.md
python tools/ng.py validate .nuclear/changes/quality-verdict-accountability --strict-custody
```

## Negative / failure-mode checks

- Token figures stated without the pass-rate caveat: scanned, 0 found.
- Statistics cited without vendor disclosure: scanned, 0 found.
- A skill folder silently added by this change: checked, 29 folders, matching `main` exactly.
- The `## Prompt` block of `reviewing-code-quality` altered: not altered; the `GOLDEN` snapshot still matches byte-for-byte.
- Any figure phrased as a promise about the reader's workload rather than the source's own benchmark: reviewed by reading; none found.

## AI-assisted work checks

- Scope: the agent drafted all doctrine and packet text, ran read-only verification commands, and used web search to verify public citations.
- Authority: no credentials held, no product code changed, no gate authored or edited.
- Approval: merge decision stays with a human via PR review.
- Custody and coupling: recorded above; coupled on the source-selection and doctrine-authorship axes.

## Security / dependency / supply-chain checks

**One dependency constraint changed.** This section originally read "not applicable"; that was written before the `mcp` pin was folded in and was left stale, making the packet internally contradictory against V-17, V-18, and `risk.md`. Corrected here.

| Item | What the check establishes | Status |
|---|---|---|
| `mcp` optional extra, `>=1.0` → `>=1.0,<2` | The bound **narrows** the accepted set; it admits no version the previous constraint did not already allow. Resolution verified in a clean venv: unbounded → 2.0.0 (import of `mcp.server.fastmcp` fails), bounded → 1.29.0 (import succeeds, 13 tests pass) | pass |
| Supply-chain posture of the pinned line | Not re-vetted. `mcp` was already an accepted optional dependency of this repo; this change constrains which of its versions are used, it does not introduce a new supplier, and no new trust decision was made | not applicable — no new supplier |
| Known advisories against `mcp` 1.x | **Not checked.** The pin holds the repo on a superseded major line, so an advisory against 1.x would make the bound a liability rather than a repair | **gap** — carried to `ship.md`; re-check when the 2.x port is scheduled |
| Base install | Unchanged. The base package still has zero runtime dependencies; `mcp` remains opt-in behind the extra | pass |
| Three new external URLs | Citations only. None is fetched at runtime, by the package or by CI | pass |

The one skip in V-9 is `tests/test_mcp_server.py::test_build_server_registers_expected_tools`, `importorskip`-gated on `mcp` not being installed in the base environment. It is not skipped in CI's `mcp-smoke` job, which installs the extra and exercises the server — that job is the evidence for the pin (V-17).

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Ship: `ship.md`
- Doctrine: `../../../docs/02-operating-system/quality-verdict-accountability.md`, `../../../docs/02-operating-system/archetype-lens.md`

## Exit criteria

- Every claim has a status.
- Failed and partial checks are described, not smoothed over.
- The limits of the verification are stated.

## Source-lineage note

Original Nuclear-grade packet inspired by public verification, evidence-status, and independent-review concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
