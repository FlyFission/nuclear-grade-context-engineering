# Quality / Verdict / Accountability — Plan

## Purpose

Sequence the work and name the review checkpoints.

## Review checkpoints

- Requirements approved: yes — the four ideas and their placement were confirmed with the owner before drafting (triad depth, archetype reach, and whether archetypes are normative).
- Design approved: yes — doctrine pages plus cross-wiring, no 29th skill, archetypes set mode floors.
- Tasks approved: yes — the sequence below.

## Sequence

| # | Task | Files | Status |
|---|---|---|---|
| 1 | Verify all four external claims against primary public sources, including authorship and affiliation | web verification | done |
| 2 | Write the triad doctrine page | `docs/02-operating-system/quality-verdict-accountability.md` | done |
| 3 | Write the archetype lens, modeled on `work-type-lens.md` | `docs/02-operating-system/archetype-lens.md` | done |
| 4 | Cross-wire the triad | `validators.md`, `agents/judge.md`, `CORE.md`, `docs/README.md` | done |
| 5 | Cross-wire the archetype lens | `work-type-lens.md`, `CORE.md`, `docs/README.md`, `reviewing-code-quality` | done |
| 6 | Place the prevalence evidence | `leadership-and-high-reliability.md`, `actor-evidence-independence.md` | done |
| 7 | Place the cleanliness evidence | `token-burn-control.md`, `context-window-discipline.md`, `reviewing-code-quality` | done |
| 8 | Register the three sources with boundary text and vendor disclosure | `source-map.md` (Tiers 6, 9, 11), `source-to-concept-crosswalk.md` | done |
| 9 | Add two maxims and seven glossary rows | `MAXIMS.md`, `docs/glossary.md` | done |
| 10 | Run the full verification suite and record results | `verification.md` | done |
| 11 | Record the verdict and the standing gaps | `ship.md` | done |
| 12 | Rebase onto `main` after it advanced 8 commits; correct every skill-count claim and wire in the new `verifying-final-artifacts` skill and `decision-authority.md` template | `CORE.md`, `archetype-lens.md`, `quality-verdict-accountability.md`, packet | done |
| 13 | Repair the unrelated `mcp-smoke` CI break by upper-bounding the optional extra (owner-approved; see `risk.md` scope note) | `pyproject.toml` | done |

## Deliberately not done

- **No new skill.** Cost would span `EXPECTED_SKILLS`, `SKILLS.md`, plugin catalogs, both eval manifests, a generated command card, the `GOLDEN` parity snapshot, and the skill counts in `CORE.md`/`README.md`/`INSTALL.md`. Decisive objection: `README.md` still claims "28 of 28 skills show a measured behavior change versus a plain prompt," and the repo now ships 29 skills after #81 added `verifying-final-artifacts`. Adding another unbenchmarked skill would widen a gap between the shipped count and the benchmarked count that the efficacy claim depends on. Precedent is explicit — `CORE.md` already refused a skill for workflow-architecture, "its home is the doctrine page, not a new `SKILL.md`."
- **No packet-template or context-pack schema change.** An archetype field in `templates/` was considered and dropped: the lens changes a mode decision at the front door, which is where it earns its keep. Adding a field to every packet would be process weight without a new decision.
- **No README.md headline section.** The triad lands in `CORE.md` and `MAXIMS.md`, which is where the repo states its principles.
- **No edit to the `## Prompt` block** of `reviewing-code-quality`, so `commands/ng-code-review.md` and its golden snapshot stay valid.

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Trace: `trace.md`
- Verification: `verification.md`

## Exit criteria

- Every task is done or explicitly deferred with a reason.
- The scope boundary is stated, not implied.

## Source-lineage note

Original Nuclear-grade packet inspired by public lifecycle and graded-rigor concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
