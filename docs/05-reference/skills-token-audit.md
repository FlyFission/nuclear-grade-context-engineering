# Skills Token Audit

Measured token cost of the repo's own prose surfaces, and the budget gate that keeps
that cost from silently regressing. Every number here is reproducible:

```bash
python tools/ng.py tokens .
```

The counter (`nuclear_grade/tokens.py`) is deterministic and dependency-free, so CI and
every developer machine produce the same figures. `tiktoken` (`o200k_base`) is supported
as an optional accuracy cross-check but is never required by the gate.

> **Why this exists.** This project preaches *measure, don't assume* and *enforce with
> code, not prompts*, yet until now it had no measurement or gate on the token cost of its
> own skills. PR #7 dropped a "progressive disclosure" token refactor on the judgment that
> the always-loaded cost is the skill descriptions (already lean), not the bodies. That
> call was made by estimate. This audit settles it with data — and the data confirms it.

## Headline finding: #7 was right, now with numbers

Skills load in two stages, and the two stages cost very differently:

| Cost | What loads | When | Tokens | Share |
|---|---|---|---|---|
| **Always-loaded** | frontmatter `description` (×23 skills) | every routing decision | **2,361** | **7.2%** |
| **On-invocation** | skill body | only when that one skill fires | 30,222 | 92.8% |

The always-loaded surface a routing agent pays on *every* turn is just **2,361 tokens —
about 103 per skill** — and is bounded by the contract test at 80–500 characters per
description. The 30,222 tokens of bodies are real, but an agent reads **one** body when a
skill fires, not all 23. So the "always-loaded cost is lean; bodies aren't the always-on
cost" conclusion from #7 holds up under measurement. The body cuts that #7 weighed remain
a *judgment* trade, not a measured win — which is why this PR ships measurement only and
defers any body edits.

## Refresh — 2026-05-31 (leadership and high-reliability pass, 27 skills)

The leadership and high-reliability pass added four skills (`deciding-who-decides`,
`declaring-intent`, `responding-to-incidents`, `tracking-deficiencies`) and four command
cards. Current reproducible aggregates (`python tools/ng.py tokens .`):

| Surface | Count | Tokens | Notes |
|---|---|---|---|
| Skill descriptions | 27 | 2,812 | always-loaded; avg ~104, still bounded 80–500 chars |
| Skill bodies | 27 | 35,366 | on-invocation; one body loads when a skill fires; heaviest 2,641 (`organizing-project-folders`) |
| Command cards | 26 | 23,392 | largest 1,406 (`ng-folders.md`), within the 1,600 budget |
| All measured prose | | ~219,600 | onboarding / reference / worked examples / doctrine |

The headline conclusion is unchanged: the always-loaded surface is the lean descriptions
(~104 tokens each), not the bodies, and the budget gate stays green. The historical baseline
below is the original 2026-05 23-skill snapshot, kept for provenance.

## Refresh -- 2026-06-16 (decision-contract pass, 27 skills)

Every skill now carries a five-field `## Decision contract` receipt -- claim checked,
artifact observed, decision affected (with a `block`/`warn`/`observe` tier), failure
class, and next action -- enforced by `ng doctor` and `tests/test_skill_contracts.py`.
The receipt lives in the body, not the always-loaded `description`, so it costs tokens
only when a skill fires:

| Surface | Count | Tokens | Change | Notes |
|---|---|---|---|---|
| Skill descriptions | 27 | 2,814 | +2 | always-loaded; unchanged by design -- the receipt is body-only |
| Skill bodies | 27 | 44,024 | +8,658 | on-invocation; one body loads when a skill fires; heaviest 2,875 (`organizing-project-folders`) |

The always-loaded surface a routing agent pays on every turn is unchanged (2,812 ->
2,814), which confirms the receipt sits in the on-invocation tier where it was placed on
purpose. The budget gate stays green: the heaviest body, `organizing-project-folders`,
is 2,875 against the 3,000 `skill_body_max`, leaving ~125 headroom -- and it is also the
heaviest `warn` body, i.e. the standing relocation candidate the existence-decision
measurement (cost-per-decision-signal, below) is meant to catch. The receipts average
~320 tokens; tightening the wordier ones is an evidence-triggered follow-up, not a budget
need.

## Measured baseline (2026-05 original snapshot, 23 skills)

| Surface | Files | Tokens | Notes |
|---|---|---|---|
| Skill descriptions | 23 | 2,361 | always-loaded; avg 103, max 140 |
| Skill bodies | 23 | 30,222 | on-invocation; avg 1,314, max 2,641 |
| Command cards | 22 | 19,923 | avg 906, max 1,406 (`ng-folders.md`) |
| Templates | 23 | 18,969 | repetitive by design (form scaffolds) |
| Docs (top-level + `docs/` tree) | 87 | 123,142 | onboarding / reference / worked examples |
| **All measured prose** | | **194,603** | |

("All measured prose" includes this audit page itself, so the grand total drifts by a few
hundred tokens as this doc is edited; the skill, command, and template figures above are
stable. Re-run `python tools/ng.py tokens .` for the live number.)

Heaviest skill bodies: `organizing-project-folders` (2,641), `breaking-down-the-work`
(2,217), `closing-stale-packets` (1,962), `staying-on-mission` (1,953),
`stress-testing-agent-changes` (1,742). Leanest: `checking-what-a-change-affects` (832),
`checking-source-claims` (872), `checking-legal-and-safety-wording` (879).

## Cost per decision signal

Joining body cost to the `ng eval` signal-coverage harness gives an evidence-based answer
to "is the prose worth its tokens," rather than an adjective:

| Worked example | Tokens / decision signal |
|---|---|
| U02 Agent workspace boundary | 182 |
| U04 Public assurance wording | 170 |
| U07 Payment webhook idempotency | 192 |

These are tight and consistent — each worked-example artifact spends ~180 tokens per
distinct decision element it surfaces. No outlier artifact is paying for signals it
doesn't deliver.

## Redundancy findings (counts, not estimates)

- **Assurance disclaimer.** "does not create ..." appears **79 times across 69 files** (after the leadership and high-reliability pass; 58 across 55 files on main before it);
  the fuller "It does not ..." lineage sentence appears in a similar spread. This
  is genuine cross-file repetition. It is *sub-paragraph* and varies in wording, so it does
  not trip the paragraph-level redundancy index — it is tracked by the `phrase_frequency`
  count in `ng tokens` instead. It is defensible (each self-contained file keeps its own
  legal boundary) but is the largest single dedup opportunity if the team ever chooses to
  trade self-containment for compactness.
- **One small repeated block.** After excluding fenced code, exactly one ~46-token block
  recurs across ≥3 files — the `**Boundary:**` line shared by four new operating-system docs
  (4 files, well under the 8-file gate threshold), introduced by the leadership pass. It is
  defensible for the same reason as the disclaimer: each self-contained doc keeps its own
  boundary note. The source-lineage notes are *not* copies — each cites different standards
  (DOE, NASA, GAO, MIL-STD, …), so the earlier "22× identical" estimate was wrong; measurement
  corrected it.
- **Shared command snippets are not waste.** The `ng validate ...` command recurs in ~17
  verification sections; that is a legitimate shared reference and is excluded from the
  redundancy scan by design.
- **`core-source-rationale.md`** is 2,165 tokens of design justification (why the source
  foundation was chosen) — now measured as part of the `docs/` tree. Useful to repo
  designers, not to an agent executing a change — a relocation candidate, not a runtime cost
  the gate should police.

## Over-prescription observations (reported, not acted on)

These are flagged for a future prose pass; the audit does not edit any skill body.

- Some `## When to Use` / `## When Not to Use` lists prescribe *how to decide* applicability,
  which the model is already good at, rather than only naming the landmines.
- A few `## Process` sections step through tasks the model handles well unaided, where a
  shorter "where the landmines are" framing would carry the same guidance for fewer tokens.

## Overlap clusters — decision: keep all four as separate skills

Four clusters of skills sit on adjacent surfaces and were reviewed for a deliberate
keep-or-merge call (names below reflect the post-#12 plain-language slugs):

1. **Trust-boundary trio** — `checking-source-claims`, `checking-legal-and-safety-wording`,
   `vetting-outside-code-and-models`.
2. **Agent-handoff trio** — `briefing-an-agent`, `handing-off-work`,
   `double-checking-before-acting`.
3. **Evidence / decision trio** — `proving-claims`, `checking-release-readiness`,
   `reviewing-code-quality`.
4. **Framing / risk overlap** — `questioning-attitude`, `rating-change-risk`,
   `choosing-what-to-control`.

**Decision (issue #14): keep all four clusters as separate, independently routed skills.**
Each member covers a distinct object at a distinct moment in the loop — the trust-boundary
trio separates *source claims* from *legal/safety wording* from *outside code and models*;
the handoff trio separates *briefing an agent* from *handing off work* from *double-checking
before acting*. Merging any cluster would collapse distinct routing triggers and break the
per-skill test contracts, trading reliable activation for a token saving the budget gate
already shows is unnecessary. Revisit only if two members begin firing on identical triggers
in practice.

## The gate

`ng tokens` enforces per-file budgets from `nuclear-grade.yaml` (`token_budgets:`) and runs
in CI after `ng doctor`. Budgets are seeded above the current measured maxima with headroom,
so the gate blocks regression rather than the accepted corpus:

| Budget | Value | Measured max today |
|---|---|---|
| `description_max` | 200 | 140 |
| `skill_body_max` | 3000 | 2,875 |
| `command_max` | 1600 | 1,406 |
| `repeated_block_max_files` | 8 | 0 prose blocks over threshold |

A new skill that balloons past these, or a boilerplate paragraph copied into a 9th file,
fails CI — a gate that fires every time, not a style note that gets forgotten.

## Decisions on the optional follow-ups (issue #14)

With PR #12's rename sweep landed, the remaining audit follow-ups were reviewed and
dispositioned:

- **Assurance disclaimer — keep per-file self-containment.** The cross-file repetition is a
  deliberate trade: each self-contained file carries its own legal boundary, and the wording
  varies by source lineage, so collapsing it to one linked source would force every reader
  (human or agent) to hold a second file just for the boundary. Not collapsed.
- **Heaviest skill bodies — cuts deferred as optional, evidence-triggered.** The
  always-loaded cost is already small and per-signal cost is already tight, so trims are a
  quality nicety, not a budget need. Trim a body only when a specific section is shown to
  mislead or bloat — not as a sweep. The budget gate prevents regression in the meantime.
- **`core-source-rationale.md` relocation — kept as an open option, deferred.** It remains a
  relocation candidate (design justification, not agent-runtime context), but the move is
  optional and the destination is undecided, so it is left in place rather than moved
  speculatively before a release.

Measure first, then cut only what the numbers justify.

## Boundary

This audit measures token cost and prose repetition. It does not judge whether a skill is
correct, safe, secure, or compliant, and it does not create formal V&V, certification, or
regulatory adequacy.
