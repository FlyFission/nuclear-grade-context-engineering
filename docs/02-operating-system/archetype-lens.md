# Archetype Lens

**Purpose:** Name the *posture* the work is being done in, so the drift you should expect is named before it happens. The archetype is orthogonal to both the rigor mode and the work type: the mode grades how much rigor a change earns by consequence (`modes.md`); the work type sets which questions matter by kind (`work-type-lens.md`); the archetype says which failure this posture produces on its good days.

Use this from `questioning-attitude`, alongside the work-type lens, before picking a mode in `rating-change-risk`.

## The five archetypes

- **Prototyper** — comes up with brand new ideas; churns out many, most of which do not ship.
- **Builder** — quickly turns a prototype or idea into production-grade product or infrastructure.
- **Sweeper** — cleans up the interface, simplifies the code and the system, unships, optimizes performance.
- **Grower** — takes something already built and iterates it toward product-market fit.
- **Maintainer** — owns a mature system and keeps it secure, reliable, fast, and efficient as it scales.

**These are patterns of work, not job titles.** They cross the org chart — the same person moves between them within a week, and two people with identical titles can be in different archetypes on the same day. The mix also shifts by phase: heavy Prototyper and Builder before product-market fit, heavy Sweeper, Grower, and Maintainer after it.

## What each posture drifts toward

| Archetype | Characteristic drift | Mode floor | Fires |
|---|---|---|---|
| **Prototyper** | Exploration silently becomes a promise. | Administrative floor or Quick — **until** the work is exposed to a user, a dependency, or a trust boundary | `questioning-attitude`, `rating-change-risk`; the mission anchor must name **"shipping this prototype"** as an explicit non-goal, so the low floor rests on a stated boundary rather than an assumption |
| **Builder** | Volume outruns review; the promise is made before the evidence exists. | Standard | `declaring-intent`, `proving-claims`, `creating-change-records`, `checking-release-readiness`; `verifying-final-artifacts` when the deliverable is a produced artifact rather than source |
| **Sweeper** | Deletion without a baseline; "cleanup" that is quietly behavior change; unshipping something someone depended on. | Standard — unshipping crosses a trust boundary | `reviewing-code-quality` (its home archetype), `checking-what-a-change-affects`, `recording-a-known-good-version` |
| **Grower** | Iterating on a metric until the metric becomes the goal. | Standard | `staying-on-mission`, `rating-change-risk`, `evaluation-integrity.md` |
| **Maintainer** | Normalization of deviance — the standing exception becomes the norm. | Nuclear on trust-bearing surfaces | `tracking-deficiencies`, `recording-a-known-good-version`, `rebaseline.md`, `responding-to-incidents`, `learning-from-experience` |

## Two rules that make the lens load-bearing

**1. When the archetype changes mid-change, re-grade.** The prototype someone decides to ship has become Builder work, and the mode set when it was exploration no longer holds. This is the most common under-grading path there is: nothing about the diff changed, so nobody re-rates it — only the promise changed. A Prototyper's mode floor is low *because* the work is not a promise; the moment it is, the floor moves. This is the same idea as "go fast while you are exploring; slow down the moment the work becomes a promise," stated as a trigger you can actually catch.

**2. Agents run archetypes too, and they are briefed into them.** "Clean this up" briefs an agent into Sweeper posture — whose characteristic drift, deletion without a baseline, is exactly the failure an agent produces most fluently and most confidently. "Make it work" briefs Builder posture and its volume-outruns-review drift. Name the archetype in the context pack so the drift is on the record before the agent starts. See `../../skills/briefing-an-agent/SKILL.md` and `context-packs.md`.

## Why it changes the questions

The same diff — "delete the legacy export path" — is routine hygiene in Sweeper posture on a pre-launch prototype and a trust-boundary change in Maintainer posture on a system with external consumers. Naming the posture up front is what surfaces the baseline and blast-radius questions a generic quality review would skip. It is also the cheapest way to catch the case where the *work* did not change but the *promise* did.

## Exit criteria

The archetype is named, its characteristic drift has been checked against the actual change, the mode floor it implies has been applied or consciously overridden with a reason, and any mid-change archetype shift triggered a re-grade.

## Source-lineage note

The five archetypes are attributed to Boris Cherny (Head of Claude Code, Anthropic), paraphrased from a public July 2026 post and registered in `../00-standards-foundation/source-map.md`. The source is a primary but low-stability social-media post, cited as concept lineage only. The mapping from archetype to characteristic drift, mode floor, and skill set is this repository's authored extension — it is not part of the original observation and should not be attributed to it. This lens does not create formal assurance or compliance.
