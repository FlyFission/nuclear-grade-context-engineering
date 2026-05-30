# HPI Overlays

**Purpose:** Translate Human Performance Improvement ideas into lightweight AI-agent controls that sit beneath the Nuclear-grade lifecycle.

**Thesis:** HPI for AI agents means small behaviors that prevent plausible agent errors before they become bad commits, false claims, weak handoffs, or release confusion.

This is a software workflow translation. No compliance claim is made.

The overlays should make agent work hard to misuse, not heavy by default. Use them to frame the decision question, separate fact from assumption and source claim, keep small actions tied to the mission anchor, and self-check the exact target at cut points. Candidate work can move quickly; acceptance of claims, baselines, public wording, and release posture should move deliberately.

---

## Core overlay

Use the normal lifecycle:

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

Add HPI controls only where they change the decision:

| Lifecycle phase | HPI overlay | Software translation |
|---|---|---|
| Question | questioning attitude, pause when unsure | state the decision question, facts, unknowns, warning signs, evidence that would change the decision, and hold conditions |
| Discover | task preview, repo-site review | check actual branch, files, tests, prior packets, source rows, and operating experience |
| Specify | validate assumptions | label facts, assumptions, unknowns, source claims, local proof, invalidation triggers, and evidence needs |
| Plan | pre-job briefing, procedure adherence | name role, authority, critical actions, likely errors, controls, rollback, and proof |
| Execute | self-checking, place-keeping, flagging | build candidates inside authority, act only on named targets, record last completed action, and pause on mismatch |
| Verify | checking and verification practices | distinguish deterministic tests, peer-check, concurrent verification, independent verification, and peer review |
| Review | work product review, independent oversight | challenge artifact usability, evidence fit, boundary wording, and process weakness |
| Decide | conservative decision making | slow down at acceptance gates: ship, block, defer, or accept residual risk with owner, condition, abort trigger, and baseline trigger |
| Baseline | accepted controlled state | record accepted configuration, evidence links, residual risk, and revalidation triggers |
| Operate | observations, signals, near misses | watch for drift, user confusion, bad handoffs, stale evidence, and weak controls |
| Learn | operating experience | update a durable control or explicitly close the lesson with rationale |

---

## Agent error precursors

Use this screen when a task feels routine but has hidden consequence.

| Precursor | Agent/software signal | Control |
|---|---|---|
| Task demand | many files, mixed objectives, long thread, hidden coupling | context pack, task preview, smaller scope |
| Capability gap | missing domain knowledge, stale memory, unfamiliar tool, source uncertainty | source lookup, independent review, pause |
| Work environment | dirty tree, failing tests, ambiguous branch, unavailable docs, flaky CI | repo-site review, explicit assumptions |
| Human/model nature | overconfidence, anchoring, completion pressure, first-answer bias | questioning attitude, danger-word scan, reviewer challenge |

Danger words for agents: "probably", "should", "seems", "obvious", "just docs", "safe", "secure", "compliant", "we can classify later". Treat them as prompts to find evidence or narrow the claim.

## Doctrine-spine controls

| Control | Agent behavior |
|---|---|
| Decision-question discipline | Spend enough time on the decision question that evidence is aimed at the right acceptance decision. |
| Operational unambiguity | Prefer exact targets, status labels, stop conditions, and expected outputs over elegant prose. |
| Mission-aligned small work | Check whether the current action serves a success criterion or a substituted local goal. |
| Grounded truth | Keep fact, assumption, unknown, source claim, local proof, and decision authority separate. |
| Two-speed control | Move quickly on reversible candidates; slow down before claims, baselines, release posture, or public wording. |
| Cut-point self-checking | Self-check the exact target and expected result before commands, public claims, trust changes, or release actions. |

---

## Activation

Default to the smallest useful overlay.

| Work type | Default overlay |
|---|---|
| Quick local change | compressed questioning attitude, one proof self-check |
| Standard change | task preview, repo-site review, assumption validation, verification type |
| Agent authority | context pack, closed-loop handoff, stop conditions, turnover if work continues elsewhere so agents turn over cleanly |
| Release | conservative decision, independent verification when needed, operator/support turnover |
| Incident or near miss | pause, control weakness review, OPEX closure |
| Dependency/model/API trust | source reliability, intended use, compensating controls, revalidation trigger |

Do not add HPI education paragraphs to every packet. Add short prompts where they change the next action, evidence obligation, or decision.

---

## Source-lineage note

This overlay is an original software-workflow translation of questioning attitude, task preview, pause when unsure, self-checking, procedure use, validation of assumptions, communication, verification, turnover, decision making, change management, independent oversight, and operating experience practices from DOE-HDBK-1028-2009 as public source lineage.

No compliance claim is made or implied.
