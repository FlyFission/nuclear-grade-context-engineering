---
name: running-a-review-panel
description: Convenes several reviewers on one frozen evidence packet, names the diversity axis each seat actually varies, preserves dissent, and verifies every finding against live source before it counts as actionable. Use when a trust-bearing or irreversible verdict currently rests on a single reviewer. Do not use for reversible low-stakes work where a second opinion is ceremony, and do not use it to overrule direct contradictory evidence by majority.
---

# Running a Review Panel

## Overview

The repo already says high-consequence verdicts should use a panel, and that "a panel that shares one biased brief is not three independent views, it is one view voiced three times" (`docs/02-operating-system/evaluation-integrity.md` §4). It has not said how to build one. This is that procedure. Its central move is making each seat declare the axis it varies -- model family, mechanism, brief, or human judgment -- because a panel's worth is not its headcount but the number of ways it can fail differently. Four reviewers sharing a model, prompt, and context are one reviewer billed four times. It also separates the panel's *result* from its *health*: a panel degraded to two correlated seats still returns a confident unanimous verdict. And nothing it says is actionable until checked against live source here -- a blocking finding is a reason to look, not an authorization to fix.

## Decision contract

- **Claim checked:** each seat names the diversity axis it varies, distinct-axis count is recorded separately from seat count, material dissent is preserved rather than averaged, and every actionable finding carries a host-verified state.
- **Artifact observed:** the frozen packet, the seat roster with declared axes, each seat's independent first-pass response, any challenge-round responses, and the degradation record -> `panel.md` plus Evidence IDs in `verification.md`.
- **Decision affected:** block -- does the panel's verified finding set support the underlying verdict, or does dissent or degradation escalate the call to a human?
- **Failure class:** false-independence (correlated seats counted as separate views, consensus treated as proof, dissent averaged away, a degraded panel reported as full, or an unverified finding acted on).
- **Next action:** record result and health together, verify each actionable finding against live source, and escalate a split or degraded panel rather than resolving it by vote.

## When to Use

- A trust-bearing or irreversible verdict -- ship, block, apply-clearance, a security or authorization call -- rests on one reviewer.
- The work is Nuclear / Tier 0, or a Standard change whose blast radius reached a critical system.
- A clean verdict came back on work where a wrong pass is expensive and you cannot name what would have caught the miss.
- Reviewer and actor share a model family, brief, or orchestrator, and you need a check that can fail differently (`docs/02-operating-system/actor-evidence-independence.md`).
- A consequential plan is about to be locked in and no one has stated the strongest opposing case.
- A prior OPEX record found a review missing a defect another method would have caught.

## When Not to Use

- The change is reversible and low-consequence. A panel on a Quick change is ceremony.
- You cannot name a second axis to vary. Two seats on one model, brief, and context are one seat; run the single review honestly.
- A deterministic check settles it. A type checker, a test, or reading the source beats four opinions for less.
- A required human approval already exists. This never talks past a gate.
- An incident is live and stabilization comes first (use `responding-to-incidents`).
- You want to overturn direct contradictory evidence. A majority is not a rebuttal.

## Inputs

- The verdict at stake, its consequence, whether it is reversible, and the mode or risk tier justifying the cost.
- The candidate at a pinned revision, the evidence to freeze -- diff, plan, source paths, prior verification records -- and the exclusions.
- The available seats and what each varies: model family, mechanism (test, type check, static analysis, direct observation), brief, or human judgment.
- Redaction rules for proprietary or secret material.
- The verification budget, and confirmation the work under review does not control it.

## Process

1. State the verdict at stake, the boundary, and the mode that earns the cost. Quick gets a self-check; Standard gets one independent method; a panel is for Nuclear / Tier 0 and trust-bearing calls. If you cannot name the consequence that earns the seats, stop. Do not let an audit widen silently.
2. Freeze the packet at a pinned revision. Redact it, record its contents and digest, give every first-pass seat exactly that. If it exceeds its bound, partition and say so -- never truncate load-bearing code silently.
3. Compose the seats. For each, write the axis it varies and the blind spot it covers. Count distinct axes and model families separately from seat count. Two seats on one family are one family with two voices.
4. Run the first pass independently. No seat sees another's conclusion. Withhold the actor's own conclusion where feasible -- a stated preferred answer is the sycophancy path in `evaluation-integrity.md` §2.
5. Run a challenge round when the stakes call for it. Anonymize the submissions; require each seat to attack the strongest claims rather than restate its own, and to name where its reasoning may be correlated with another's.
6. Record panel health beside the result: every seat dropped, timed out, invalid, or given a truncated packet. A panel that planned five axes and delivered two is a **degraded panel** and is reported as one. Health is a condition on the verdict, not a footnote.
7. Synthesize by evidence, not by vote. Deduplicate claims, attribute each to its axes, keep the strongest opposing case even when one seat held it, and give each material finding a falsification test.
8. Verify here, then dispose. Read the code path, run the test, or inspect the authoritative source for every finding you intend to act on; mark each `verified`, `rejected`, or `unresolved`, and never promote an unverified finding to a recommendation. Report the decision first, then verified blockers, non-blockers, dissent, panel health, and next checks. A split panel on a high-consequence call blocks and surfaces the split to a human.

## Outputs

- A `panel.md` record in the packet: the verdict at stake, the frozen packet's description and digest, the seat roster with each declared axis, and the exclusions.
- Distinct-axis and distinct-family counts, stated separately from seat count.
- A finding list, each with supporting axes, severity, falsification test, and a state of `verified`, `rejected`, or `unresolved`.
- Preserved dissent and the strongest opposing case, attributed and unaveraged.
- The degradation record: dropped, timed-out, truncated, and invalid seats.
- One disposition and any escalation trigger that fired, linked from `verification.md` as an Evidence ID.

## Verification

- Every seat names the axis it varies; a seat that cannot is folded into the seat it duplicates before counting.
- The record states distinct axes and model families separately from seat count, and every actionable finding has a host-session verification behind it.
- Dissent, dropped seats, timeouts, and invalid responses all appear; none was dropped for tidiness.
- A degraded panel is labeled degraded, and a split high-consequence panel escalated rather than resolved by majority.
- Passing proves the panel was built and reported honestly. It does not prove the findings correct, does not establish independence beyond the axes actually varied, and creates no assurance, safety, security, certification, or regulatory adequacy.

## Escalation

- Escalate to a human when the panel splits on a trust-bearing or irreversible call. The split is the signal; do not average it.
- Escalate when the panel degrades below the diversity that justified convening it. Report the degraded result and the missing axes; the owner decides whether it still supports the verdict.
- Stop when the packet could not be frozen, when partitioning would cut load-bearing evidence, or when the work under review controls the verification budget. A starved panel blocks for lack of room to decide.
- Reopen when the candidate moves after the packet was frozen. A panel result is bound to the revision it read.

## Common Rationalizations

- "All four agreed, so it is settled." Unanimous unsupported claims are still unsupported, and four copies of one blind spot agree readily.
- "We ran four reviewers, that is independence." That is a headcount. Independence is the axis you varied; if you cannot name it, there was one reviewer.
- "It came back clean." Clean is compatible with two seats dropped at preflight. Read panel health before the verdict.
- "The panel flagged it, so fix it." A blocking finding is a reason to look at the source, not an authorization to edit it.
- "The dissenter was outvoted." The minority view is what a panel is for. Losing it discards the only thing the extra seats bought.

## Red Flags

- A seat roster where no seat can state what it varies.
- A result reported by seat count with no family or axis count anywhere.
- Findings written as recommendations with no host-session verification behind them.
- Dropped or timed-out seats missing from a report that reads as full-strength.
- A panel convened on a reversible Quick change, or convened after the decision was already made.

## Prompt

```text
Convene a Nuclear-grade review panel on this verdict.

Inputs:
- verdict at stake, consequence, reversible? (yes/no):
- candidate at pinned revision, and the mode or tier that justifies a panel:
- evidence to freeze, and the exclusions:
- seats available and what each varies (model family / mechanism / brief / human):
- verification budget, and who controls it:

Do this:
- State the verdict and boundary; stop if the mode does not earn the seats.
- Freeze one packet; redact it, record its digest, partition rather than truncate.
- Per seat, name the axis it varies; count distinct axes and model families separately from seat count.
- Run the first pass independently, withholding the actor's own conclusion; where stakes call for it, add an anonymized challenge round attacking the strongest claims.
- Record every dropped, timed-out, truncated, or invalid seat as panel health beside the result.
- Synthesize by evidence, not by vote; keep the strongest opposing case; give each material finding a falsification test.
- Verify every actionable finding against live source or tests in this session; mark each verified, rejected, or unresolved.

Return the disposition first, then verified blockers, non-blockers, dissent, panel health, and next checks; distinct-axis and distinct-family counts stated separately from seat count; and any escalation trigger that fired.

Do not resolve a split high-consequence panel by majority, report unverified findings as recommendations, or edit reviewed code merely because the panel recommended it. Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

An original software-workflow procedure, not a claim to have invented panel review, multi-reviewer assurance, or ensemble evaluation. It is the operational cash-out of doctrine already here: the panel and meta-judge paragraph in `docs/02-operating-system/evaluation-integrity.md`, the named-diversity-axis rule in `docs/02-operating-system/independence-architecture.md`, and the coupling profile in `docs/02-operating-system/actor-evidence-independence.md`. Concept lineage: the diversity taxonomy in NUREG/CR-6303; independence axes in NASA SWE-141; tool qualification proportional to reliance in NASA SWE-136; independent verification in DOE-HDBK-1028-2009; and published findings on LLM-as-judge self-preference and preference leakage (arXiv:2502.01534) -- mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal verification and validation, independent V&V, compliance, certification, or any safety, security, or regulatory guarantee.
