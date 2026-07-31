# Quality / Verdict / Accountability — Trace

## Purpose

Link each claim the change makes to its basis, its implementation, and its evidence.

## Claim-to-implementation trace

| Claim ID | Implementation | Evidence |
|---|---|---|
| REQ-001 | `docs/02-operating-system/quality-verdict-accountability.md` — three terms, four collapse rows | `verification.md` V-1 |
| REQ-002 | `CORE.md` (validator section), `MAXIMS.md` (new maxim), `docs/glossary.md` (3 rows + 1 idiom), `docs/README.md` (1 row), `validators.md` §1, `agents/judge.md` | `verification.md` V-2 |
| REQ-003 | `docs/02-operating-system/archetype-lens.md` — mode-floor column and the two load-bearing rules | `verification.md` V-3 |
| REQ-004 | `archetype-lens.md` source-lineage note; `source-map.md` Tier 11 row | `verification.md` V-4 |
| REQ-005 | Boundary text in `token-burn-control.md`, `quality-verdict-accountability.md`, `leadership-and-high-reliability.md`, `actor-evidence-independence.md`, `MAXIMS.md` | `verification.md` V-5, V-6 |
| REQ-006 | `source-map.md` Tiers 6, 9, 11 + vendor-affiliation note; `source-to-concept-crosswalk.md` 3 rows | `verification.md` V-7 |
| REQ-007 | No `skills/` folder added; edits confined outside `## Prompt` | `verification.md` V-8 |

## External claim-to-source trace

| Claim as stated in the repo | Source | Status |
|---|---|---|
| ~42% of committed code AI-generated or significantly assisted; ~65% projected by 2027 | Sonar 2026 State of Code Developer Survey (n > 1,100) — https://www.sonarsource.com/state-of-code-developer-survey-report.pdf | verified-public; vendor-run, self-reported |
| 96% do not fully trust AI code's functional correctness; ~48% always verify; 38% find review costlier | same survey | verified-public; vendor-run, self-reported |
| Cleaner code: pass rate unchanged (<1%), ~7.1% fewer input tokens, ~8.5% fewer output tokens, ~11% less reasoning effort, ~34% fewer already-edited-file revisits; 660 trials, 33 tasks, 6 repo pairs | Trivedi & Schmitt, arXiv:2605.20049 — https://arxiv.org/abs/2605.20049 | verified-public; authors affiliated with SonarSource |
| Prototyper / Builder / Sweeper / Grower / Maintainer, as patterns of work rather than job titles | Boris Cherny (Head of Claude Code, Anthropic), public post July 2026 — https://x.com/bcherny/status/2071379474277613732 | supporting-context; primary but low-stability |
| Archetype → characteristic drift → mode floor → skill mapping | **this repository's authored extension** | not attributed to any external source |

## Gaps

| Gap | Why it is open | Disposition |
|---|---|---|
| Both statistical sources are authored or run by the same commercial vendor, and both findings favor that vendor's product category | No independent replication exists at time of writing | Disclosed at every citation point and in a standing `source-map.md` note; recorded as a named risk in `ship.md`, not closed |
| The archetype source is a social-media post | No stable canonical publication exists | Cited as `supporting-context` only; a Threads mirror is recorded alongside it |
| The archetype→mode-floor mapping is unvalidated by field use | New doctrine, no adoption data | Stated as this repo's extension; first `program-self-assessment.md` cycle should check whether it changed any real grading decision |

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Verification: `verification.md`
- Ship: `ship.md`

## Exit criteria

- Every claim links to an implementation and an evidence row, or to a stated gap.

## Source-lineage note

Original Nuclear-grade packet inspired by public configuration-management and traceability concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
