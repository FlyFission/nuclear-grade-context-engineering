# Independent Skill Benchmark Protocol

This protocol exists because static skill-contract scores are only eligibility checks. A skill proves value only when it changes a real decision or artifact compared with fair baselines under controlled conditions.

## Claim boundary

A benchmark result may claim only what it measured:

- **Structural readiness** means a skill has the sections, decision contract, prompt-bank coverage, and token shape needed for evaluation.
- **Internal pilot lift** means skill-informed prompts improved over a naive prompt-only baseline on author-designed scenarios.
- **Independent lift** requires independently authored scenarios, blinded grading, raw transcripts, fair baselines, and repeat trials.

Do not describe a skill as effective from the static score alone. A `100/100` structural score can still tie or lose to prompt-only.

## Required baselines

For each scenario, run the same model, tool access, fixture, and output budget across at least these variants:

1. **Naive prompt-only baseline** — the user prompt alone.
2. **Best-practice prompt baseline** — a concise direct instruction that an expert might write without the skill body.
3. **Equal-token generic checklist** — neutral safety/process text with roughly the same token count as the skill.
4. **Irrelevant skill control** — a randomly selected non-applicable skill to detect generic caution from extra context.
5. **Skill description only** — name/frontmatter/description, to isolate routing and trigger priming.
6. **Full skill** — the current `SKILL.md` body.
7. **Compressed skill ablation** — a short distilled version, to test whether the full skill's token cost is justified.

## Scenario mix per skill

Minimum independent run set per skill:

- 2 obvious positive triggers
- 2 hard rationalization traps
- 2 ambiguous or boundary cases
- 2 negative controls where the skill should not add process
- 1-2 cross-skill routing cases using known overlap pairs
- 1-2 fixture-backed tool/repo tasks when the skill implies artifact changes

Run at least 5 trials per scenario/variant for live LLM comparisons. Keep all raw outputs.

## Primary metrics

Report all of these, not only win/tie/loss:

- fatal decision miss rate
- required decision-element coverage
- forbidden/prohibited-claim rate
- false-positive or over-process rate
- artifact correctness for fixture tasks
- routing precision, recall, top-1 accuracy, and top-3 accuracy
- cost and latency per successful decision improvement
- effect size with confidence interval where sample size permits

## Grading rules

- Blind condition labels and randomize answer order.
- Use deterministic route/output scorers first when possible.
- Use at least two independent graders for subjective quality dimensions.
- Include calibration responses with known obvious pass/fail outcomes.
- Adjudicate all grader disagreements, thin-margin wins, all losses, and phrase-bar-only wins.
- Publish the invalid-run policy and rerun manifest before interpreting results.

## Routing benchmark

Content efficacy and routing efficacy are different. Test routing separately:

1. Present the model only with skill names/descriptions, not full bodies.
2. Ask it to select none/one/multiple skills for a prompt.
3. Include decoys and boundary cases.
4. Score false positives and false negatives, not only top-1 accuracy.
5. Generate a confusion matrix for overlap clusters.

## Known overlap clusters for first independent pass

Prioritize these clusters because static review and PR #62 pilot evidence show unclear boundaries or thin evidence:

1. `briefing-an-agent` vs `handing-off-work`
2. `proving-claims` vs `checking-release-readiness`
3. `proving-claims` vs `checking-source-claims`
4. `proving-claims` vs `checking-legal-and-safety-wording`
5. `creating-change-records` vs `proving-claims`
6. `using-nuclear-grade` vs `rating-change-risk`
7. `using-nuclear-grade` vs `questioning-attitude`
8. `choosing-what-to-control` vs `checking-what-a-change-affects` vs `recording-a-known-good-version`
9. `reporting-shared-defects` vs `tracking-deficiencies`
10. `deciding-who-decides` vs `declaring-intent` vs `double-checking-before-acting`

## Acceptance guidance

Use this as the first pass acceptance rule, then tighten after collecting data:

- **Promote / keep as control**: full skill beats all baselines on fatal misses or critical element coverage without unacceptable over-process, and cost per improvement is defensible.
- **Compress**: full skill beats prompt-only but not compressed skill, or adds high cost without proportional gain.
- **Narrow / rewrite**: skill helps only in self-authored traps, creates routing confusion, or overlaps a stronger neighboring skill.
- **Demote to reference**: skill repeatedly ties fair baselines and does not change decisions or artifacts.
- **Retire candidate**: skill increases fatal misses, prohibited claims, or false-positive process after retesting and amendment.

No skill should be removed on one benchmark run. Retire/demote decisions need a separate human-reviewed change record.
