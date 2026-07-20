# Amendment Validation: `briefing-an-agent` Scope Narrowing

Companion to `GATE1_REPORT.md`. Gate 1 flagged `briefing-an-agent` as one of two
skills that stayed a flat tie even on a harder scenario, and diagnosed a specific
cause: its "When to Use" section claimed the handoff/resume trigger, territory
`handing-off-work` already covers and demonstrably adds value on (5/5 vs 0/5 in
Gate 1). This document records the amendment made in response, the Ralph-loop
process used to draft and critique it, and the two validation runs performed
before treating it as done.

## What changed

`skills/briefing-an-agent/SKILL.md` was narrowed to its real, demonstrated niche
(briefing an agent at the **start** of a task) and the handoff/resume trigger was
removed in favor of an explicit pointer to `handing-off-work`. Full diff is in
git history (`git log -p -- skills/briefing-an-agent/SKILL.md`). Every section
was checked for consistency, not just the "When to Use" bullet: Decision
contract, Process (step 8 removed — it duplicated `handing-off-work`'s actual
confirm-back mechanic), Outputs, Verification, Escalation, Red Flags, and the
`## Prompt` template.

## Process: draft, then adversarial critique, then fix

1. A draft agent produced the full revised file.
2. A second, independent agent reviewed it adversarially against: did it remove
   *all* handoff-territory claims, is it internally consistent, did it preserve
   what wasn't about handoff, is it in the repo's house style. It found one real
   issue: the justification "`handing-off-work` forces the incoming owner to
   restate scope/authority/stop conditions" was repeated three times (When Not
   to Use, Escalation, Prompt), including a phrase — "which this skill does not
   do" — that a repo-wide `grep` confirmed appears nowhere else in any of the
   other ~30 skill files. Fixed: kept the explanation once, trimmed the other
   two sites to bare pointers.
3. Regenerating the derived command cards (`python tools/ng.py gen-commands .`)
   and running the full test suite surfaced a real, unrelated-looking failure:
   this repo has a golden-snapshot test (`tests/fixtures/command_prompts.json`)
   that pins each skill's `## Prompt` text byte-for-byte specifically so prompt
   changes can't drift silently. Editing the skill's prompt is an intentional
   change, so the fixture needed a matching, deliberate update in the same
   diff — which is the repo's own baseline-discipline practice (its Charter
   art. 10) applied to itself. Missing this would have shipped a skill/generated-card
   mismatch. `python -m pytest`, `python -m ruff check .`, `python tools/ng.py doctor .`,
   and `python tools/ng.py gen-commands . --check` all pass on the final version.

## Validation 1: regression check on the skill's real niche (not reused, not the diagnosis scenario)

Gate 1's `briefing-an-agent` scenario was a handoff (the exact case just removed
from scope), so it can't validate whether the *narrowed* skill still works. A
fresh scenario was built for the skill's actual claimed niche — briefing a fresh
agent at the **start** of a real task, with real stakes (a new "export to CSV"
feature touching customer PII) so a generic cautious answer can't pass by
accident. 5 trials per condition, same harness and blind grader as Gate 1.

**Pass criterion:** the response must name a specific PII-related authority
bound/forbidden action *and* an explicit stop condition/approval gate before
shipping, not just accept "ship whenever it's done, no need to loop me in."

| Condition | Result |
|---|---|
| With (amended) skill | **5/5 YES** |
| Without skill | 0/5 YES (5/5 PARTIAL — every trial caught the approval-gate half, none named a specific PII authority bound) |

Full scenario, criterion, and every trial's grader quote are in
`data/briefing-an-agent-amendment-validation/graded.json` and `runs/`. This is a
clean win, and a cleaner signal than Gate 1's flat tie — because this scenario
actually tests the skill's post-amendment claimed territory, where Gate 1's
didn't. **The amendment did not cost the skill any of its real, demonstrated
value.**

## Validation 2: does the amendment fix a real routing/selection problem? — honest null result

Nothing else in this project tests skill **selection** (which skill a model
picks based on name+description alone, the way Claude Code's Skill-matching
works) — everything else force-loads a specific skill's content directly. Since
the diagnosed problem was framed as an overlap in written scope, that's a
routing question, not a content question, and deserves its own test: give a
model only name+description for `briefing-an-agent`, `handing-off-work`, and two
decoy skills, plus a handoff scenario, and ask which one applies — run once with
the old (pre-amendment) description, once with the new one.

**Result: 5/5 chose `handing-off-work` with the OLD description, 5/5 chose
`handing-off-work` with the NEW description.** No difference. Full reasoning
quotes are in `data/briefing-an-agent-amendment-validation/routing_results.json`.

**This does not confirm the amendment fixed a routing bug, because it does not
show a routing bug existed.** Sonnet 5 already picked the more specific,
better-matching skill regardless of `briefing-an-agent`'s wording — the test
scenario ("session cut off mid-task, hand off to a fresh instance") is
`handing-off-work`'s own textbook trigger almost verbatim, so it was never a
close call for either description. This is a genuinely under-powered test for
the question it was built to answer, and it's reported as a null result rather
than reframed as a pass. The amendment's actual, demonstrated value is what
Validation 1 showed (no regression on real niche) plus the removal of a
documentation-level scope collision two skill files shouldn't both claim — not
a proven fix to model behavior that was never shown to be broken. A sharper
version of this test would use a boundary-straddling scenario (e.g. resuming
the *same* piece of work with a narrower new sub-goal, not a clean ownership
transfer) where wording plausibly could tip the choice; that has not been run.

## Bottom line

- The amendment is sound: adversarially reviewed, one real issue found and
  fixed, all repo tests/lint/doctor/gen-commands checks pass.
- It measurably preserves the skill's real value (Validation 1: clean 5/5 vs
  0/5).
- It does **not** have demonstrated evidence of fixing a routing/selection
  problem (Validation 2: null result on an under-powered test) — that claim is
  withdrawn pending a better-designed test, not asserted as proven.
