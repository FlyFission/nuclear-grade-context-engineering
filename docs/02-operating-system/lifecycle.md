# The Lifecycle

**Purpose:** This file lays out the Nuclear-grade backbone for software changes made with AI help.

**Core thesis:** Nuclear-grade joins two habits. The first is a questioning attitude: challenge what you assume. The second is keeping the approved version of everything under control (configuration management). For AI-assisted work, that means you run the power of a large language model (LLM) through clear steps. Check your assumptions. Write down what you need. Name what must stay under control. Tie each claim to its proof. Verify. Review. Decide. Save the version everyone agreed is correct. Then learn from real use. You do all this without wasting tokens or piling on busywork.

**Lifecycle spine:**

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

That spine carries a handle: **PROVE** — Plan · Run · Observe · Verdict · Educate — or **PRO** (Plan · Run · Operate) zoomed out. See [`../diagrams.md`](../diagrams.md).

This is a way of working, not a compliance program. You sort the risk inside `risk.md`. That file holds the chosen mode, the triggers that force you to escalate, what the change must prove, and the conditions that make you hold.

Under the spine sit habits from Human Performance Improvement (HPI). Scale them to how much is at stake: preview the task, check the real repo and files, pause when unsure, check your own work, hand off cleanly, pick the right kind of verification, decide with care, and learn from real use (lessons from real operation, or OPEX). Use `hpi-overlays.md` for those small controls. Keep this lifecycle steady.

The lifecycle has two speeds. While you explore and build drafts, move fast and stay willing to throw work away. Slow down at acceptance. That is the moment a claim, a controlled item, the version everyone agreed is correct (a baseline), a public statement, a release call, or a change to what the agent may do becomes something people now trust. The early steps stop you from racing toward the wrong question. The later steps stop a quick draft from becoming the accepted version with no proof behind it.

---

## Phase map

| Phase | Decision being made | Minimum useful output | Exit criteria |
|---|---|---|---|
| Question | What decision must the evidence support? What assumptions, doubts, and stop conditions should you surface before work goes on? | Decision question, assumptions, warning signs, evidence gaps, and the evidence that would change the decision. | Confidence rests on facts, not a hunch. |
| Discover | What sources and repo facts matter? | Public sources, past records, limits, known gaps. | The spec rests on real facts, not guesses. |
| Specify | What state or behavior is required? | Requirements, claims, outcomes to protect, assumptions, acceptance criteria. | Claims can be tested or are marked as gaps. |
| Plan | How will the controlled setup change? | Steps, affected items, rollback, proof commands. | Work can go on without rediscovering scope. |
| Execute | Did the build stay inside its authority? Did it make a draft, not an accepted state? | Diffs, commits, generated files, self-checks, notes on what the AI did. | Any deviation is recorded, not hidden drift. |
| Verify | What hard evidence backs the claims? What is still a fact, an assumption, an unknown, a source claim, or local proof? | Tests, evals, reviews, and results, each with a status, a verification type, and gaps. | The evidence matches the claim. |
| Review | Can a doubting reviewer accept the work without relying on confidence or vague instructions? | A claim-to-evidence review, a work-product review, a check of boundary wording, and a call on leftover risk. | The accept, defer, or block call can be reviewed. |
| Decide | Should the draft become the accepted setup, ship, block, defer, or go on with leftover risk? | Decision, conditions, owner, baseline trigger. | The release decision is stated out loud. |
| Baseline | What accepted state is now under control after the slow, careful acceptance? | Commit, release, or artifact, plus the state of controlled items and the triggers. | Future drift can be spotted. |
| Operate | What signals show drift or failure? | Monitors, support signals, incident triggers. | Operators know what to watch. |
| Learn | What should change next time? | An OPEX note tied to a basis, test, control, template, or baseline update. | The lesson changes something or is closed out. |

---

## Activation threshold

Use the full lifecycle for any Standard, Nuclear, Incident, Research Board, Release, or activated control change. Quick changes may shrink the lifecycle down to `risk.md` plus `proof.md`. Even then, answer the steps that matter in a line or two.

Go past Quick when the change affects:

- behavior users can see;
- how data is handled, sign-in (auth), permissions, or network access;
- what an AI model, prompt, or tool is allowed to do;
- outside dependencies, APIs, packages, software you rent online (software-as-a-service, or SaaS), build services, or data sources;
- how you release, roll back, monitor, or hand off the work in real use;
- long-lived design or setup that is hard to undo.

---

## Minimum useful version

For a small Standard change, the lifecycle works when the record answers:

```text
What decision are we answering? What facts did we discover? What are we specifying? What changed as a candidate? What objective evidence supports the claim? What decision accepted, blocked, deferred, or bounded it? What baseline now controls it?
```

If the answer runs longer than one screen before you start building, sum it up. Link to deeper evidence only where you need it.

---

## Overhead trap

Do not turn the lifecycle into seven meetings or seven huge documents. The record grows with the stakes. The repo does not. If a step adds no decision value for a low-stakes change, shrink it instead of making up busywork.

---

## Required links

Every lifecycle record should link back and forward:

- `questioning-attitude.md` links assumptions, uncertainty, stop conditions, and evidence gaps.
- `risk.md` links to selected mode and escalation triggers.
- `basis.md` or `spec.md` links to activated source-map concepts when relevant.
- `plan.md` links to specification, affected files, dependencies, and rollback.
- `turnover.md` links current state, changed conditions, remaining work, authority, and incoming-owner confirmation when responsibility transfers.
- `self-check.md` links critical action, target, expected result, stop condition, actual result, and evidence.
- `verification.md` links to claims/acceptance criteria, verification type, and results.
- `decision.md` or `ship.md` links evidence, unresolved risks, rollback, monitoring, handoff, conservative decision posture, and baseline trigger.
- `baseline.md` links to accepted controlled state after review and decision.
- `learn`/OPEX notes link to changed requirements, tests, monitors, or controls.

---

## Source-lineage note

This is an original software workflow inspired by public sources on high-stakes engineering and software assurance. The main influences are [DOE-HDBK-1028-2009](https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009) for the questioning attitude, [DOE-STD-1073-2016](https://www.energy.gov/ehss/articles/doe-std-1073-2016), [DOE-STD-1189-2016](https://www.energy.gov/ehss/articles/doe-std-1189-2016), [DOE-STD-3024-2011](https://www.energy.gov/ehss/articles/doe-std-3024-2011), the NRC software guidance family RG 1.168-1.173 listed in `../00-standards-foundation/source-map.md`, [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), the [NASA Software Engineering Handbook](https://swehb.nasa.gov/), and the [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/nasa-systems-engineering-handbook/).

No compliance claim is made or implied.
