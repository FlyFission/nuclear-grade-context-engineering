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
| V-6 | Vendor affiliation disclosed wherever the statistics are cited | Scan of the six citing files for a vendor disclosure | 6 of 6 disclosed | pass |
| V-7 | The three sources are registered under existing citation discipline | New rows in `source-map.md` Tier 6 (Sonar survey), Tier 9 (arXiv:2605.20049), Tier 11 (Cherny), plus a standing vendor-affiliation note under Tier 6 and three `source-to-concept-crosswalk.md` rows | Present | pass |
| V-8 | No new skill added; skill-count invariant intact | `ls -d skills/*/` = 29 (the count `main` arrived at via #81); no skill folder added or removed by this change | 29 folders, unchanged by this PR | pass |
| V-9 | Full test suite | `python -m pytest -q` | 238 passed, 1 skipped | pass |
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

**Partial: the second maxim carries the caveat but not the affiliation.** `MAXIMS.md` states the pass-rate caveat inline and points to `token-burn-control.md`, which carries the vendor disclosure. Judged acceptable for a deliberately short quotable entry with a one-click pointer; noted so a reviewer can disagree.

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
python -m pytest -q                    # 238 passed, 1 skipped
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

Not applicable — no dependency, model, API, permission, or build change. Three external URLs were added as citations only; none is fetched at runtime.

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
