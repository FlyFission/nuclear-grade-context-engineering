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

## Headline finding: #7 was right, now with numbers (confirmed post-#12)

Skills load in two stages, and the two stages cost very differently:

| Cost | What loads | When | Tokens | Share |
|---|---|---|---|---|
| **Always-loaded** | frontmatter `description` (×23 skills) | every routing decision | **2,361** | **7.9%** |
| **On-invocation** | skill body | only when that one skill fires | 29,664 | 92.1% |

The always-loaded surface a routing agent pays on *every* turn is just **2,361 tokens —
about 103 per skill** — and is bounded by the contract test at 80–500 characters per
description. The 29,664 tokens of bodies are real, but an agent reads **one** body when a
skill fires, not all 23. So the "always-loaded cost is lean; bodies aren't the always-on
cost" conclusion from #7 holds up under measurement. The body cuts that #7 weighed remain
a *judgment* trade, not a measured win — which is why the original PR shipped measurement
only and deferred body edits. Targeted cuts have since been made to the heaviest bodies.

## Measured baseline (2026-05, 23 skills, post-#12 rename)

| Surface | Files | Tokens | Notes |
|---|---|---|---|
| Skill descriptions | 23 | 2,361 | always-loaded; avg 103, max 140 |
| Skill bodies | 23 | 29,664 | on-invocation; avg 1,290, max 2,403 |
| Command cards | 22 | 19,923 | avg 906, max 1,406 (`ng-folders.md`) |
| Templates | 23 | 18,404 | repetitive by design (form scaffolds) |
| Docs (top-level + `docs/` tree) | 87 | ~117,931 | onboarding / reference / worked examples |
| **All measured prose** | | **~194,600** | |

Heaviest skill bodies: `organizing-project-folders` (2,403), `breaking-down-the-work`
(2,089), `closing-stale-packets` (1,962), `staying-on-mission` (1,761),
`stress-testing-agent-changes` (1,742). Leanest: `checking-what-a-change-affects` (832),
`checking-source-claims` (872), `checking-legal-and-safety-wording` (879).

## Cost per decision signal

Joining body cost to the `ng eval` signal-coverage harness gives an evidence-based answer
to "is the prose worth its tokens," rather than an adjective:

| Worked example | Tokens / decision signal |
|---|---|
| U02 Agent workspace boundary | 169 |
| U04 Public assurance wording | 164 |
| U07 Payment webhook idempotency | 178 |

These are tight and consistent — each worked-example artifact spends ~170 tokens per
distinct decision element it surfaces. No outlier artifact is paying for signals it
doesn't deliver.

## Redundancy findings (counts, not estimates)

- **Assurance disclaimer.** "does not create ..." appears **58 times across 55 files**;
  the fuller "It does not ..." lineage sentence appears in a similar spread. This
  is genuine cross-file repetition. It is *sub-paragraph* and varies in wording, so it does
  not trip the paragraph-level redundancy index — it is tracked by the `phrase_frequency`
  count in `ng tokens` instead. **Post-#12 doctrine call: keep per-file self-containment.**
  Each skill is designed to be loaded and used independently; the disclaimer is part of
  each file's legal-boundary statement, and the wording varies by source lineage (DOE, NASA,
  DoD, NIST citations differ per skill). Collapsing to a linked source would require every
  skill to be read with a second file in context, which is a worse trade than the token cost.
- **No repeated prose blocks.** After excluding fenced code, **zero** paragraph-sized prose
  blocks recur across ≥3 files. The source-lineage notes are *not* copies — each cites
  different standards (DOE, NASA, GAO, MIL-STD, …), so the earlier "22× identical" estimate
  was wrong; measurement corrected it.
- **Shared command snippets are not waste.** The `ng validate ...` command recurs in ~17
  verification sections; that is a legitimate shared reference and is excluded from the
  redundancy scan by design.
- **`core-source-rationale.md`** (2,165 tokens of design justification) has been relocated
  from `docs/00-standards-foundation/` to `docs/05-reference/` — it is useful to repo
  designers, not to an agent executing a change, and the relocation removes it from the
  agent-runtime documentation path.

## Over-prescription observations (reported, not acted on)

These were flagged in the original audit (pre-#12); a targeted prose pass has since trimmed
the heaviest bodies (see post-#12 follow-up). Remaining guidance:

- Some `## When to Use` / `## When Not to Use` lists still prescribe *how to decide*
  applicability in some skills; future passes can tighten these toward landmine-only lists.
- A few `## Process` sections step through tasks the model handles well unaided, where a
  shorter "where the landmines are" framing would carry the same guidance for fewer tokens.

## Overlap clusters — decisions recorded (post-#12)

The audit flagged four clusters of skills on adjacent surfaces. PR #12's rename sweep has
now merged. **Decision: keep all four clusters as independent skills.** Each cluster serves
a distinct scope; consolidation would conflate surfaces that agents use separately, break
test contracts, and require routing changes. The mapping from pre-#12 to post-#12 names is:

1. **Trust-boundary trio** — `checking-source-claims` (source citation honesty),
   `checking-legal-and-safety-wording` (license and public assurance text),
   `vetting-outside-code-and-models` (dependency and model trust). These cover
   *what you cite*, *what you publish*, and *what you import* — three different objects.
2. **Agent-handoff trio** — `briefing-an-agent` (packing context before a hand-in),
   `handing-off-work` (turnover at the end), `double-checking-before-acting` (self-check
   before executing). These fire at three different moments in the agent lifecycle.
3. **Evidence / decision trio** — `proving-claims` (claim-to-evidence mapping),
   `checking-release-readiness` (release gate), `reviewing-code-quality` (code standards
   review). These work on different objects: a claim, a release, and a diff.
4. **Framing / risk overlap** — `questioning-attitude` (ongoing epistemic habit),
   `rating-change-risk` (one-time risk classification), `choosing-what-to-control` (scope
   selection for CM). These are different kinds of judgment at different points.

The pre-#12 audit names (`packing-agent-context`, `turning-over-agent-work`,
`self-checking-agent-actions`, `classifying-change-risk`, `identifying-controlled-items`,
`reviewing-ship-readiness`, `structuring-agentic-folders`, `decomposing-work-breakdown`,
`controlling-mission-drift`, `red-teaming-agent-changes`, `baselining-configuration`,
`screening-change-impact`, `checking-source-lineage`) are now superseded by the names above.

## The gate

`ng tokens` enforces per-file budgets from `nuclear-grade.yaml` (`token_budgets:`) and runs
in CI after `ng doctor`. Budgets are seeded above the current measured maxima with headroom,
so the gate blocks regression rather than the accepted corpus:

| Budget | Value | Measured max today |
|---|---|---|
| `description_max` | 200 | 140 |
| `skill_body_max` | 3000 | 2,403 |
| `command_max` | 1600 | 1,406 |
| `repeated_block_max_files` | 8 | 0 prose blocks |

A new skill that balloons past these, or a boilerplate paragraph copied into a 9th file,
fails CI — a gate that fires every time, not a style note that gets forgotten.

## Recommended next steps

PR #12's rename sweep has merged. The post-#12 follow-up has completed the following:

- Overlap clusters: decided — keep all four as independent skills (see section above).
- `core-source-rationale.md`: relocated to `docs/05-reference/`.
- Prose cuts: targeted trimming of the heaviest bodies (`organizing-project-folders`,
  `breaking-down-the-work`, `staying-on-mission`) to tighten over-prescriptive Process
  sections and reduce "how to decide" framing.
- Disclaimer: doctrine call made — keep per-file self-containment (see Redundancy findings).

Any further body trimming is optional. The data says that trade is optional, not urgent:
the always-loaded cost is already small, and per-signal cost is already tight. Measure
first, then cut only what the numbers justify (`python tools/ng.py tokens .`).

## Boundary

This audit measures token cost and prose repetition. It does not judge whether a skill is
correct, safe, secure, or compliant, and it does not create formal V&V, certification, or
regulatory adequacy.
