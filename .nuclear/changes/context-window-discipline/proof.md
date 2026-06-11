# Quick Proof

**Purpose:** Capture the smallest credible evidence record for this Quick change.

---

## Proof summary

- Change slug: context-window-discipline
- Proof owner: FlyFission
- Date/time: 2026-06-10
- Risk record: `risk.md`

## Claim proven

Claim: The context-window-discipline page and its supporting edits are additive only — they
keep the full test suite, ruff, `doctor`, the token budget, and this packet green; every
internal link in the touched docs resolves; every external source cited in the new Tier 9 of
`source-map.md` is public and was independently re-verified; and no unverifiable claim from
the triggering external report was carried into the repo.

## Method

- Command/check/eval/review: `python -m pytest`; `python -m ruff check .`;
  `python tools/ng.py doctor .`; `python tools/ng.py tokens .`;
  `python tools/ng.py validate .nuclear/changes/context-window-discipline`; a link-resolution
  script over all internal links in the five touched docs; web verification of each Tier 9
  source URL on 2026-06-10.
- Environment: Python 3.13, repo working tree on `claude/context-engineering-agents-492oi0`.
- Inputs/fixtures: the new page, the Tier 9 source-map section, the one-row `docs/README.md`
  edit, one grounding sentence each in `context-packs.md` and `token-burn-control.md`, seven
  glossary rows, and this packet.
- Expected result: full suite green; ruff clean; doctor OK; token budget OK; this packet
  validates; all internal link targets exist; every Tier 9 URL confirmed public.
- Self-check used? yes; target = the `docs/README.md` headings the public-docs test asserts
  (`## Use the repo`, `## Reference foundation`), confirmed present and unchanged, and the
  exclusion list from `risk.md` (no per-tool "context waste" percentages, no
  "Forward-Deployed Context Engineer" framing, no unverified efficiency numbers), confirmed
  absent from the tree.

## Result

- Status: pass
- Actual result: `python -m pytest` → 142 passed; `python -m ruff check .` → all checks
  passed; `doctor .` → OK; `tokens .` → OK: token budget; link-resolution script → 33
  internal links checked across the five touched docs, all resolve. Web verification
  confirmed each Tier 9 source: Anthropic context-engineering post; LangChain
  context-engineering docs; Neo4j practical guide; Breunig failure-mode post; Chroma
  context-rot report; arXiv 2307.03172 (Lost in the Middle; the arXiv abstract page itself
  records TACL acceptance); arXiv 2510.04618
  (ACE); microsoft/LLMLingua (arXiv 2310.05736 / 2310.06839 / 2403.12968); arXiv 2506.15655
  (cAST; venue EMNLP 2025 Findings verified against the ACL Anthology record,
  https://aclanthology.org/2025.findings-emnlp.430/); arXiv 2510.00446 (LongCodeZip; no
  independently verified venue, so none is claimed). Packet validation:
  recorded by the `python tools/ng.py validate .nuclear/changes/context-window-discipline`
  run after this file was added; the only prior finding was the then-missing `proof.md`.
- Evidence link or artifact path: `docs/02-operating-system/context-window-discipline.md`;
  `docs/00-standards-foundation/source-map.md` (Tier 9); `docs/README.md` (the "Budget and
  order an agent's context window" row); commands above.
- If failed/gap: none blocking. Two recorded limits: (1) external URLs can rot — Tier 9
  links were verified on 2026-06-10 only, an existing repo-wide concern; (2) the Anthropic,
  Chroma, and arXiv pages returned HTTP 403 to this environment's direct fetcher, so
  verification was via web-search confirmation of title, venue, and content rather than a
  byte-level fetch.

## Reviewer note

- Reviewer: FlyFission
- Review note: The page is grounding and a failure-mode index, not a new gate — context
  packs, token budgets, lessons-learned deltas, and turnover already exist; the page links
  out to them and explains why they work. The triggering external report's unverifiable
  numbers and marketing framing were excluded by name in `risk.md` and confirmed absent.
  Benchmark figures are attributed to their papers with an explicit "their benchmarks, not
  promises" hedge in both the page header and the Tier 9 intro.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: Extract verified context-engineering mechanics from external research report
- Relevant changed files: `docs/02-operating-system/context-window-discipline.md`,
  `docs/00-standards-foundation/source-map.md`, `docs/README.md`,
  `docs/02-operating-system/context-packs.md`,
  `docs/02-operating-system/token-burn-control.md`, `docs/glossary.md`
- CI run / test output: `python -m pytest` (142 passed), `python -m ruff check .` (clean),
  `python tools/ng.py doctor .` (OK), `python tools/ng.py tokens .` (OK)
- If AI-assisted: changes prepared by an AI agent under review; scope is one additive
  documentation page, one additive source-map tier, and five small additive edits, with no
  code or gate change; web access was used only to re-verify public citations.

## Exit criteria

- Evidence directly matches the claim in `risk.md`.
- Actual result is compared to the expected result named before proof.
- Result status is explicit.
- Any failure or gap has a next action or escalation.
- Reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade record inspired by public software test-documentation and verification
concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
