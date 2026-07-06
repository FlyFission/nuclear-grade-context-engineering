# Standard Basis

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

---

## Change context

- Slug: skill-benchmark-and-amendments
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-07-06
- Decision this basis supports: whether the benchmark evidence justifies the two skill amendments
  made, and whether both are safe to ship as-is.

## Mission / need

The repo's skills had never been tested for whether loading them actually changes model behavior —
only an author-judged qualitative comparison existed (`docs/03-worked-examples/skill-workflow-comparison/`),
which explicitly disclaims being a benchmark. This change builds that missing objective evidence,
then acts on what it found: two skills had real, diagnosed problems (a scope overlap, a weak-model
robustness gap), and both got a proposed fix, adversarially reviewed and validated before shipping.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Skills that already worked keep working after any amendment | An amendment that fixes one thing but regresses another is a net loss | Regression test on the skill's real niche, run after the amendment, not assumed |
| Every claim in the benchmark states its own confidence level | A false-confidence benchmark is worse than no benchmark — readers act on it | Statistical significance computed and disclosed even when the result is unflattering (`STATISTICAL_ANALYSIS.md`) |
| Amendments are adversarially reviewed before being trusted | A single author's judgment (human or AI) missing a real issue is exactly the failure mode this repo's own skills (`reviewing-code-quality`, `stress-testing-agent-changes`) exist to catch | A separate critique pass per amendment, with real findings recorded, not rubber-stamped |
| Cross-PR/cross-branch conflicts on the same files are surfaced, not silently resolved | Two unreconciled edits to the same skill file landing separately would corrupt the skill without anyone deciding it | PR comments on #63 documenting the overlap; explicit merge-conflict resolution against `main`'s independently-merged fix, recorded in this packet |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A skill amendment silently regresses the skill's already-working behavior | fault | The skill gets worse while the record says it was "fixed" | Regression validation run and recorded for both amendments (`AMENDMENT_VALIDATION.md`, `MULTI_MODEL_CHECK.md` addendum) before either was kept |
| The benchmark's statistical claims overstate certainty | insufficiency | Readers treat "27 WINS" as proven when it isn't; downstream decisions (keep/cut a skill) get made on false confidence | Full Fisher-exact + Benjamini-Hochberg correction computed and disclosed as the headline finding of `STATISTICAL_ANALYSIS.md`, not buried |
| A skill amendment is kept despite validation showing it doesn't work | insufficiency | The record claims a fix that isn't real | `creating-change-records`'s amendment is disclosed as attempted-and-insufficient in the master status table and `MULTI_MODEL_CHECK.md`, not marked WINS |
| This branch silently overwrites main's or PR #63's independent fix to the same skill files | fault | Two people's/agents' diagnostic work gets lost without anyone deciding which should win | Explicit merge performed against current `main`; conflict resolved with stated reasoning (kept this branch's validated version); PR #63 conflict flagged via PR comment, left for a maintainer decision |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| `claude-sonnet-5` is the only subject model tested for 24 of 28 skills | assumption | Cost/scope decision, disclosed throughout | A future multi-model run showing widespread divergence like `creating-change-records`'s | FlyFission |
| Scenario/criteria authorship is not independent of skill authorship | fact | Same effort built both, disclosed in `REPORT.md` executive summary | Independent third-party review of any scenario | FlyFission |
| No scipy in this environment | fact | Confirmed by import error before writing `compute_stats.py` | N/A — implementation verified against known reference values instead | FlyFission |
| PR #63's changes to `briefing-an-agent` are not adopted in this branch | assumption | This branch's version has live regression validation; PR #63's does not yet | If PR #63's link-based composition approach gets its own validation showing it's better | Whoever merges #62/#63 |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| "0 of 44 statistical tests survive Benjamini-Hochberg correction" | local proof | `evals/skill-benchmark-pilot/data/statistical-analysis/statistical_summary.json`, computed by `compute_stats.py`, Fisher-exact implementation verified against the known 3-vs-0-of-3 reference value (p≈0.10) before trusting it on real data | Every "WINS" label in the benchmark is downgraded from "proven" to "directional, pilot-level" |
| "17 of 27 round-1 scenarios had baseline success ≥50%" | local proof | Same statistical_summary.json, a free desk-audit query, no new trials | Confirms the pre-calibration gap was real and larger than the 5-skill "thin margin" cohort alone suggested |
| "`creating-change-records`'s amendment did not fix the Haiku gap" | local proof | `data/creating-change-records-amendment-validation/runs/`, read in full, not just the grader's count | The amendment ships anyway (harmless, small improvement) but the gap is reported open |
| "main independently merged a fix for the same overlap" | fact | `git diff 5b3167d origin/main -- skills/briefing-an-agent/SKILL.md` etc., inspected directly | Treated as a third independent convergence on the same diagnosis, strengthening confidence the problem was real |

## Interfaces and trust boundaries

- Internal interfaces affected: `tools/ng.py gen-commands` (projects skill Prompt sections into
  command cards); `tests/test_command_parity.py` (golden-snapshot fixture).
- External services/APIs affected: none in the shipped product; the benchmark itself calls the
  `claude` CLI headless (`claude -p`) against the Anthropic API as its evaluation mechanism, not a
  shipped dependency.
- Data classes affected: none — no user data, no production data.
- Human approval boundaries: this entire packet is gated on human PR review before merge; the
  benchmark's own runs used `--safe-mode` and restricted tool access so no run could touch real
  files or state.
- AI/model/tool authority boundaries: the two amended skills are instructions loaded into future AI
  agent sessions — this is the actual behavior surface being changed, which is why this is Standard
  and not Quick.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| `claude-sonnet-5` (subject model, primary) | Runs the with-skill/without-skill scenario trials | A model update changing baseline behavior could shift results without anyone noticing | Model ID pinned and stated in every report; scripts checked in so a future run can re-baseline | Anthropic ships a new Sonnet version |
| `claude-haiku-4-5` (grading model + secondary subject model) | Blind grading throughout; subject model for the multi-model check | Same as above, plus grader drift could change what counts as YES/PARTIAL/NO | Grader kept separate from subject model to avoid self-check bias; grader prompts and schemas checked in | Anthropic ships a new Haiku version |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN a skill amendment is proposed based on benchmark evidence THE SYSTEM SHALL have it adversarially critiqued by a separate agent before it is applied. | Protected outcome: amendments are adversarially reviewed before being trusted | Draft→critique→apply loop used for both `briefing-an-agent` and `creating-change-records` | `AMENDMENT_VALIDATION.md`, `MULTI_MODEL_CHECK.md` addendum |
| REQ-002 | WHEN a skill's `## Prompt` section changes THE SYSTEM SHALL regenerate the corresponding command card and update `tests/fixtures/command_prompts.json` in the same change. | Protected outcome: derived artifacts stay in sync; caught by `test_command_parity.py` | `tools/ng.py gen-commands`; golden fixture updated deliberately per the repo's own baseline-discipline practice | `verification.md` commands table |
| REQ-003 | IF a post-amendment validation result contradicts the amendment's justification THEN THE SYSTEM SHALL report the skill's status as open/unresolved, not fixed. | Unacceptable outcome: a skill amendment is kept despite validation showing it doesn't work | `creating-change-records` disposition in the master status table and `MULTI_MODEL_CHECK.md` | `evals/skill-benchmark-pilot/README.md` status table |
| REQ-004 | WHEN this branch's changes conflict with content already merged to `main` or proposed in a parallel open PR touching the same files THE SYSTEM SHALL reconcile explicitly (merge + documented resolution, or a flagged PR comment) before merge. | Protected outcome: cross-PR/cross-branch conflicts are surfaced, not silently resolved | Merge performed against current `main`; PR #63 conflict flagged via two PR comments | This packet's `trace.md`; PR #63 comment thread |
| REQ-005 | THE SYSTEM SHALL disclose statistical significance findings even when they are unflattering to the benchmark's own headline claims. | Protected outcome: every claim states its own confidence level | Benjamini-Hochberg correction computed across all 44 tests; result (0 survive) stated as the headline of `STATISTICAL_ANALYSIS.md`, not softened | `STATISTICAL_ANALYSIS.md` |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `evals/skill-benchmark-pilot/README.md`, this file |
| Architecture — shape and major parts | yes | `evals/skill-benchmark-pilot/README.md` ("Start here" table); harness described in `REPORT.md` section 1 |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` above |
| Data models — shapes, classes, ownership | n/a | No data model; evaluation artifacts are JSON/Markdown checked into git |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` above; harness bugs found mid-run are disclosed with before/after impact in `REPORT.md` section 3 |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: this session's conversation; PR #62, #63
- Source lineage, if cited: n/a — original evaluation methodology, informed by public benchmark-practice
  literature cited in `evals/skill-benchmark-pilot/README.md`'s self-audit (HELM, the Agentic
  Benchmark Checklist, BetterBench, SkillsBench) as comparison points, not as adopted templates.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
