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
| **Always-loaded** | frontmatter `description` (×23 skills) | every routing decision | **2,337** | **7.7%** |
| **On-invocation** | skill body | only when that one skill fires | 27,902 | 92.3% |

The always-loaded surface a routing agent pays on *every* turn is just **2,337 tokens —
about 102 per skill** — and is bounded by the contract test at 80–500 characters per
description. The 27,902 tokens of bodies are real, but an agent reads **one** body when a
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
| Skill bodies | 27 | 35,366 | on-invocation; one body loads when a skill fires |
| Command cards | 26 | 23,392 | largest 1,406 (`ng-folders.md`), within the 1,600 budget |
| All measured prose | | 218,612 | onboarding / reference / worked examples / doctrine |

The headline conclusion is unchanged: the always-loaded surface is the lean descriptions
(~104 tokens each), not the bodies, and the budget gate stays green. The historical baseline
below is the original 2026-05 23-skill snapshot, kept for provenance.

## Measured baseline (2026-05 original snapshot, 23 skills)

| Surface | Files | Tokens | Notes |
|---|---|---|---|
| Skill descriptions | 23 | 2,337 | always-loaded; avg 102, max 138 |
| Skill bodies | 23 | 27,902 | on-invocation; avg 1,213, max 2,489 |
| Command cards | 22 | 18,079 | avg 822, max 1,295 (`ng-folders.md`) |
| Templates | 23 | 18,404 | repetitive by design (form scaffolds) |
| Docs (top-level + `docs/` tree) | 87 | 117,931 | onboarding / reference / worked examples |
| **All measured prose** | | **184,653** | |

Heaviest skill bodies: `structuring-agentic-folders` (2,489), `decomposing-work-breakdown`
(2,108), `closing-stale-packets` (1,960), `controlling-mission-drift` (1,890),
`red-teaming-agent-changes` (1,617). Leanest: `baselining-configuration` (738),
`screening-change-impact` (754), `checking-source-lineage` (803).

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

- **Assurance disclaimer.** "does not create ..." appears **78 times across 69 files** (2026-05-31 refresh; 57 across 54 at the original baseline);
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

These are flagged for a future, post-#12 prose pass; this PR does not edit any skill body.

- Some `## When to Use` / `## When Not to Use` lists prescribe *how to decide* applicability,
  which the model is already good at, rather than only naming the landmines.
- A few `## Process` sections step through tasks the model handles well unaided, where a
  shorter "where the landmines are" framing would carry the same guidance for fewer tokens.

## Overlap clusters flagged for a human decision (NOT merged)

The user asked to flag conceptual overlap rather than merge it. Four clusters of skills sit
on adjacent surfaces and are worth a deliberate keep-or-merge decision **after** the #12
rename sweep lands (merging now would collide with it):

1. **Trust-boundary trio** — `checking-source-lineage`, `checking-license-and-assurance-boundaries`,
   `checking-dependency-and-model-trust`.
2. **Agent-handoff trio** — `packing-agent-context`, `turning-over-agent-work`,
   `self-checking-agent-actions`.
3. **Evidence / decision trio** — `proving-claims`, `reviewing-ship-readiness`,
   `reviewing-code-quality`.
4. **Framing / risk overlap** — `questioning-attitude`, `classifying-change-risk`,
   `identifying-controlled-items`.

Flagged only. Each is independently routed today; consolidation is a structural change with
test-contract and routing implications, to be decided separately.

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

Once PR #12's rename sweep merges, a follow-up *may* trim the heaviest bodies and collapse
the disclaimer to a single linked source — **if** the team decides self-containment is worth
trading for compactness. The data says that trade is optional, not urgent: the always-loaded
cost is already small, and per-signal cost is already tight. Measure first, then cut only
what the numbers justify.

## Boundary

This audit measures token cost and prose repetition. It does not judge whether a skill is
correct, safe, secure, or compliant, and it does not create formal V&V, certification, or
regulatory adequacy.
