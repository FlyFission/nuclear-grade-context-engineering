# Gate 2 (Overlap Sweep) and Gate 3 (Structural-Value Recheck) Findings

Follow-up to `AMENDMENT_VALIDATION.md`. Covers the three remaining open threads
from the `briefing-an-agent` work: closing out `proving-claims`, sweeping the
other candidate overlap pairs, and a lower-confidence check on
`creating-change-records`.

## `proving-claims`: closed — real value, on a dimension neither test round measured

`proving-claims` was one of two skills (with `briefing-an-agent`) that stayed a
flat tie even in Gate 1's hard-case retest. Manually reading the full transcripts
(not just the grader's YES/NO) showed both conditions already reach the correct
decision (self-check is not independent evidence) — the skill's own Outputs
section demands something neither round's criterion ever scored: a structured
claim-to-evidence table with named status labels (`pass`/`fail`/`gap`/`deferred`/
`not applicable`/`planned`).

Re-graded the **existing** 10 Gate 1 transcripts (no new generation cost) against
a criterion isolating exactly that: structured claim-to-evidence rows, a status
label from the skill's own enum, and an explicit fact-vs-source-claim split.

| Condition | Result |
|---|---|
| With skill | **5/5 YES** |
| Without skill | 0/5 YES (2/5 partial) |

Clean, unambiguous split. **This was a test-design gap, not a skill-content
gap.** No amendment needed — `proving-claims` demonstrably adds value; my first
two rounds just never asked the right question of it. Full grading data in
`data/proving-claims-structural-recheck/` (see raw JSON alongside this file).

## Overlap sweep (Gate 2): the other 4 candidate pairs — no further amendments

Read all remaining skills involved in the pairs flagged earlier in this
project's history: `recording-what-an-agent-did` + `handing-off-work`,
`proving-claims` + `checking-release-readiness`, `deciding-who-decides` +
`rating-change-risk`, `checking-what-a-change-affects` + `checking-release-readiness`.

None show the problem `briefing-an-agent` had — two skill files literally
claiming the same trigger words in their own "When to Use" sections. All four
pairs are legitimate pipeline compositions with genuinely distinct trigger
conditions:

- `proving-claims` produces claim-to-evidence status; `checking-release-readiness`
  *consumes* that status to make the separate ship/block/defer call, and adds
  rollback/monitoring/apply-clearance concerns `proving-claims` never touches.
  `proving-claims`'s own Decision Contract says its decision-affected is "warn --
  the release posture the `ship.md` decision weighs," not the ship decision
  itself.
- `checking-what-a-change-affects` screens what a change leaves stale;
  `checking-release-readiness` consumes that screen's output at the ship gate.
  Different artifacts (`change-impact.md` vs `ship.md`), different questions.
- `deciding-who-decides` (who has authority for *this specific action*) and
  `rating-change-risk` (how much rigor does *this change* need) share inputs
  (reversibility, consequence, evidence) but produce different outputs —
  authority placement vs. process-mode selection. No shared trigger wording.
- `recording-what-an-agent-did` (execution evidence: what actually happened,
  step by step) and `handing-off-work` (responsibility transfer: what's left,
  what's allowed) answer different questions and don't claim each other's
  territory.

**`briefing-an-agent` was a genuine one-off, not a systemic pattern.** No further
amendments proposed from this sweep.

## `creating-change-records`: probable same pattern as `proving-claims`, but not fully confirmed — a criterion flaw on my part, disclosed

`creating-change-records` is the one skill with a marginal/thin-margin result in
*both* rounds (round 1: near-ceiling `LOSES`; Gate 1: `0/5 YES` both conditions,
skill earning partial credit on all 5 trials vs. 1/5 for the baseline). Checked
whether, like `proving-claims`, this is a compound-criterion artifact rather than
a real gap — re-graded existing round-1 and Gate-1 transcripts against a
narrower structural criterion (does it name the required Standard-mode files /
use the status-label vocabulary, separate from full judgment quality).

| Round | With skill | Without skill |
|---|---|---|
| Round 1 | 3/3 YES | 0/3 YES |
| Gate 1 | 4/5 YES (+1 partial) | 3/5 YES |

Round 1 is a clean split, consistent with the `proving-claims` pattern. **The
Gate 1 recheck is not trustworthy and should be discarded** — inspecting the
grader's actual quotes for the `without_skill` "YES" trials showed it was
matching plain-English uses of "pass" and "gap" ("linter tests **pass**," "that
**gap** is exactly...") as if they were the skill's specific status-label
convention applied to a named claim, which they were not. My criterion wording
("uses at least 2 of these specific status-label words") was too loose — it
should have required the words be used *as a status tag attached to a specific
claim*, not merely present anywhere in prose. This is a flaw in the check I
wrote, not a real finding, and it is reported here rather than quietly
discarded.

**Net: `creating-change-records` probably follows the same pattern as
`proving-claims` (real value on a structural dimension the compound criterion
under-credits), but this is not confirmed with the same confidence.** No
amendment is proposed. If this skill's status matters enough to resolve fully,
the next step is re-running the Gate 1 structural recheck with a corrected,
tag-specific criterion — not yet done.
