# Skill Consolidation: Pre-Registered Protocol

**Status:** registered before any routing or fit result was produced (2026-11-03). Results go in
`REPORT.md` beside this file, and any deviation from this protocol is stated there.

**Question:** Can the catalog shrink from 31 skills to 23 without losing anything the 31 could do,
and without any merged skill becoming the wrong tool for a job one of its parts used to do (a hammer
for a screw)?

## Candidate merges

From [`../skill-catalog-audit/2026-11-03.md`](../skill-catalog-audit/2026-11-03.md). Each merge is
decided on its own; a failing merge does not block the others.

| ID | Absorbed | Into | Audit confidence |
|---|---|---|---|
| M1 | `declaring-intent` | `double-checking-before-acting` | strong |
| M2 | `tracking-deficiencies`, `reporting-shared-defects` | `learning-from-experience` | strong |
| M3 | `checking-source-claims` | `checking-legal-and-safety-wording` | strong |
| M4 | `choosing-what-to-control` | `recording-a-known-good-version` | moderate-strong |
| M5 | `closing-stale-packets` | `creating-change-records` | moderate |
| M6 | `briefing-an-agent` | `handing-off-work` | contested |
| M7 | `breaking-down-the-work` | `organizing-project-folders` | lower |

## Evidence

1. **Scenario corpus.** 180 situations written by an agent that was not shown the skill names, the
   catalog, or the evals. They span 12 work types and 10 stage gates, include at least 35 mundane
   cases and at least 15 genuinely ambiguous ones, and avoid process vocabulary.
2. **Ground truth.** Two labelers work independently, each with the full 31 `SKILL.md` files, and
   name the skills (0 to 3) that should be loaded for each scenario. Every disagreement is resolved
   by an adjudicator who sees both labels and the skill files but not which merges are proposed.
   Agreement before adjudication is reported, along with the adjudicated truth.
3. **Blind routing.** Two router agents in fresh contexts see only skill names and frontmatter
   descriptions, which is what a host sees. One gets the current 31-skill catalog and the other the
   proposed 23-skill catalog. Each picks 0 to 3 skills per scenario. The existing 176 routing cases
   in `evals/skill-routing-cases.jsonl` are run as a secondary set.
4. **Fit.** For every scenario whose truth includes either side of a merge, a fit judge reads the
   merged draft and the scenario. It names the section that applies and answers two questions:
   would following the merged skill *miss* work the scenario needs, and would it *force* work the
   scenario does not need?
5. **Capability map.** Every distinct capability of each absorbed skill (its decision contract
   claim, each process step, each output, and each escalation trigger) is mapped to its location in
   the merged draft, or retired with a stated reason.

## Acceptance (all four must hold for a merge to ship)

- **A. Coverage.** 100% of the absorbed skill's capabilities are mapped or retired with a reason.
- **B. Routing parity.** Take the scenarios whose truth includes either side of the merge. The
  23-catalog router must pick the merged skill on at least as many as the 31-catalog router picked
  a correct side, minus 5 percentage points. Its false-positive rate for the merged skill on
  scenarios outside that set must not rise by more than 5 points over the two originals' combined
  rate.
- **C. Fit.** Zero scenarios where the merged skill would miss needed work. Forced unneeded work in
  at most 10% of the merge's scenarios, and in none of the target skill's original scenarios: the
  merge must not make the target's old jobs heavier.
- **D. Context.** The merged body is within `skill_body_max` (3900 tokens), the description within
  `description_max` (200), and the catalog's total body tokens fall.

A merge that fails may be revised once and re-tested. The first and second results are both
reported. A merge that still fails is not made.

## Known limits, stated in advance

- Every agent in this protocol (generator, labelers, adjudicator, routers, fit judge) is the same
  model family as the author and is briefed by the author's session. This is a structured check,
  not independent verification (`docs/02-operating-system/verification-methods-and-depth.md`).
  Errors are correlated across models (Kim et al., ICML 2025), so agreement among these agents
  is weak evidence on its own.
- Routing is measured on the frontmatter alone. Hosts may truncate descriptions under catalog
  budget pressure, and this protocol does not simulate that.
- A scenario corpus of 180 bounds per-merge rates coarsely. The pair-specific subsets are smaller,
  so a clean result on a subset of n bounds that merge's miss rate only near 3/n.

## Source-lineage note

Original evaluation protocol. Its design (independent double labeling with adjudication,
pre-registered thresholds, and measuring a checker before relying on it) follows
`docs/02-operating-system/verification-methods-and-depth.md` and its sources, mapped in
`docs/00-standards-foundation/source-map.md`. No compliance claim is made.
