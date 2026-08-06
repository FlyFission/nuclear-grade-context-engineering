# Inspectable Builder-Critic Pilot Contract

**Purpose:** Test whether a bounded builder-critic cycle improves inspectable artifacts enough to justify a dedicated beta skill. This is an evaluation contract, not evidence that the method works.

## Boundary

The targeted improvement cycle is an optional technique inside Execute and Verify. It does not replace Question, Specify, Review, Decide, Baseline, Operate, or Learn. A critic reports findings and evidence status. It has no acceptance, merge, release, or apply-clearance authority.

A fresh context changes only the context axis. It is not independent verification unless the actor, context, mechanism, authority, and resource bases support that claim. Critic scores are process telemetry, not outcome evidence.

## Paired design

Compare two arms against the same frozen task, requirements, candidate boundary, tools, model family, budget, and external adjudication criteria:

- **B0 paired baseline:** the current Standard workflow with a sequential owner, existing verification, and no targeted builder-critic cycle.
- **B1 targeted cycle:** the same workflow plus a frozen inspectable bar, bounded largest-gap iterations, fresh artifact criticism, and final integration observation.

Use at least four tasks in each of three classes before considering a beta skill:

1. **visual artifact:** a rendered page, figure, PDF, or interface compared with a reference and functional requirements;
2. **deterministic code:** behavior checked through tests, benchmarks, failure cases, and the integrated public seam;
3. **source-backed technical document:** factual and inferential claims checked against a frozen source pack and claim inventory.

Run both arms in randomized order. Use multiple fixed run seeds or equivalent repeated trials where the provider permits it. Record model, prompt, tool, environment, token, latency, and artifact digests. The builder and critic do not receive hidden adjudication items.

## Evidence custody

Before either arm starts, freeze:

- task and protected constraints;
- candidate boundary and starting revision;
- inspectable bar and acceptance threshold;
- public development cases and hidden adjudication cases;
- evaluator instructions and decision rules;
- run budget, stop conditions, and adverse-result retention location.

Retain prompts, raw findings, produced artifacts, commands, results, rejected findings, and bar variances. The builder may propose a variance but cannot edit the hidden evaluator, bar, threshold, critic budget, retention policy, or terminal-state rule.

An evaluator outside the builder path inspects the actual artifact, not the builder narrative. For visual and generated outputs, adjudication regenerates or opens the consumer-facing artifact. For code, it runs the public seam and hidden failure cases. For documents, it checks claims directly against the frozen source pack.

## Measures

Primary measures are external outcomes:

- load-bearing acceptance criteria passed;
- serious defects remaining after the candidate is complete;
- serious defects corrected without introducing a new serious defect;
- hidden-case performance by task class;
- whole-artifact regressions and cross-slice integration failures.

Secondary measures are cost and operating burden:

- rounds, tokens, elapsed time, and tool calls;
- human adjudication and review time;
- findings that changed the artifact and survived external adjudication;
- repeated findings, critic reversals, and unresolved gaps at the stop bound.

Report each class separately. Do not average away a regression in one class. Do not treat critic confidence, critic score, reviewer agreement, or a higher self-score as a quality result.

## Promotion gate

A dedicated skill may enter **beta**, not Core or promoted status, only when all of these are true:

1. B1 improves externally adjudicated outcomes over the paired baseline in every task class, with no serious hidden-case or integration regression.
2. Corrected serious defects outnumber new serious defects attributable to the loop.
3. Cost and latency remain inside the predeclared bound, or the human owner accepts a documented tradeoff.
4. No run changes the bar without authority, suppresses an adverse finding, launders fresh context as independence, or lets a critic make the release decision.
5. The result repeats on a **fresh hidden confirmation set** frozen after the development pilot closes.
6. The routing value of a dedicated skill is demonstrated against extending the existing briefing, proving, artifact-verification, and review skills.

The pilot can support a provisional beta decision. Any general efficacy claim requires a separately preregistered, adequately powered study and qualified external review.

## Kill conditions

Stop or reject the pilot path when any of these occurs:

- critic scores rise while external adjudication is flat or worse;
- the builder controls or weakens the bar, evaluator, retention, or stopping rule;
- adverse findings or failed artifacts are omitted;
- coupled work is fanned out and integration defects rise;
- the loop repeatedly attacks an easy aesthetic gap while a higher-consequence claim remains unresolved;
- the critic is starved of the budget needed for a relied-upon check;
- a bounded run ends and is reported as pass despite unmet criteria;
- B1 exceeds the agreed cost bound without a material outcome gain;
- the same failure repeats without a changed strategy.

At a bound, preserve the remaining gaps and terminate as NOT VERIFIED, INCONCLUSIVE, or BLOCKED. Carry release-relevant gaps into `ship.md`.

## Minimum artifacts

A pilot package contains:

- frozen taskset and source/reference pack;
- B0/B1 run matrix and randomized order;
- prompts, tool/model/environment records, and artifact digests;
- raw public and hidden adjudication results;
- five-axis coupling profiles;
- class-level outcome and cost report;
- accepted, rejected, and unresolved findings;
- confirmation-set decision and promotion disposition.

## Source-lineage note

This contract is an authored Nuclear-grade adaptation informed by Matt Shumer's public Gauntlet Loop article and Claude-of-Duty repository, plus the repository's existing evidence-custody and evaluation-integrity doctrine. Source-specific results are not generalized. This document creates no efficacy, independence, compliance, formal verification, safety, security, certification, or release claim.
