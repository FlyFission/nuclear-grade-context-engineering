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
a *judgment* trade, not a measured win — which is why the audit shipped measurement + a
gate first and treated body edits as a separate decision.

## Measured baseline (2026-05, 23 skills)

| Surface | Files | Tokens | Notes |
|---|---|---|---|
| Skill descriptions | 23 | 2,361 | always-loaded; avg 103, max 140 |
| Skill bodies | 23 | 30,222 | on-invocation; avg 1,314, max 2,641 |
| Command cards | 22 | 19,923 | avg 906, max 1,406 (`ng-folders.md`) |
| Templates | 23 | 18,969 | repetitive by design (form scaffolds) |
| Docs (top-level + `docs/` tree) | 87 | 123,121 | onboarding / reference / worked examples |
| **All measured prose** | | **194,596** | |

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

These are tight and consistent — each worked-example artifact spends ~170 tokens per
distinct decision element it surfaces. No outlier artifact is paying for signals it
doesn't deliver.

## Redundancy findings (counts, not estimates)

- **Assurance disclaimer.** "does not create ..." appears **59 times across 55 files**;
  the fuller "It does not ..." lineage sentence appears in a similar spread. This
  is genuine cross-file repetition. It is *sub-paragraph* and varies in wording, so it does
  not trip the paragraph-level redundancy index — it is tracked by the `phrase_frequency`
  count in `ng tokens` instead. It is defensible (each self-contained file keeps its own
  legal boundary) but is the largest single dedup opportunity if the team ever chooses to
  trade self-containment for compactness.
- **No repeated prose blocks.** After excluding fenced code, **zero** paragraph-sized prose
  blocks recur across ≥3 files. The source-lineage notes are *not* copies — each cites
  different standards (DOE, NASA, GAO, MIL-STD, …), so the earlier "22× identical" estimate
  was wrong; measurement corrected it.
- **Shared command snippets are not waste.** The `ng validate ...` command recurs in ~17
  verification sections; that is a legitimate shared reference and is excluded from the
  redundancy scan by design.
- **`core-source-rationale.md`** is 2,165 tokens of design justification (why the source
  foundation was chosen) — now measured as part of the `docs/` tree. Useful to repo
  designers, not to an agent executing a change — a relocation candidate, not a runtime cost
  the gate should police.

## Over-prescription observations (reported, not acted on)

These are flagged for an optional future prose pass; this follow-up does not edit any
skill body.

- Some `## When to Use` / `## When Not to Use` lists prescribe *how to decide* applicability,
  which the model is already good at, rather than only naming the landmines.
- A few `## Process` sections step through tasks the model handles well unaided, where a
  shorter "where the landmines are" framing would carry the same guidance for fewer tokens.

## Overlap clusters (decision recorded; NOT merged)

Four clusters of skills sit on adjacent surfaces. Consolidation would be a structural
change with routing/contract implications, so it is an explicit doctrine decision rather
than an automatic cleanup.

1. **Trust-boundary trio** — `checking-source-claims`, `checking-legal-and-safety-wording`,
   `vetting-outside-code-and-models`.
2. **Agent-handoff trio** — `briefing-an-agent`, `handing-off-work`,
   `double-checking-before-acting`.
3. **Evidence / decision trio** — `proving-claims`, `checking-release-readiness`,
   `reviewing-code-quality`.
4. **Framing / risk overlap** — `questioning-attitude`, `rating-change-risk`,
   `choosing-what-to-control`.

**Decision (2026-05-31): keep all four clusters as separate skills.** Rationale: each has
a distinct trigger and output surface; merging would blur routing and would require
contract/test updates. Revisit only if maintenance burden or repeated routing confusion
shows up in evidence.

## The gate

`ng tokens` enforces per-file budgets from `nuclear-grade.yaml` (`token_budgets:`) and runs
in CI after `ng doctor`. Budgets are seeded above the current measured maxima with headroom,
so the gate blocks regression rather than the accepted corpus:

| Budget | Value | Measured max today |
|---|---|---|
| `description_max` | 200 | 138 |
| `skill_body_max` | 3000 | 2,489 |
| `command_max` | 1600 | 1,295 |
| `repeated_block_max_files` | 8 | 0 prose blocks |

A new skill that balloons past these, or a boilerplate paragraph copied into a 9th file,
fails CI — a gate that fires every time, not a style note that gets forgotten.

## Recommended next step (post-#12)

Optional, evidence-triggered follow-ups:

- If token budgets ever block a needed addition, consider a scoped pass over the heaviest
  skill bodies (start with `organizing-project-folders`, `breaking-down-the-work`) and measure
  “tokens saved per decision signal lost.”
- If the team decides compactness outweighs per-file self-containment, consider collapsing
  the repeated “does not create …” boundary-note family to a single linked source and re-run
  `ng tokens` to quantify the win.

## Boundary

This audit measures token cost and prose repetition. It does not judge whether a skill is
correct, safe, secure, or compliant, and it does not create formal V&V, certification, or
regulatory adequacy.
