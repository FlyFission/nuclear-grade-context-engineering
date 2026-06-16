# Configuration Management

**Purpose:** This file defines the Nuclear-grade backbone for keeping the approved version of everything under control (configuration management) in AI-assisted software work.

**Thesis:** AI agents change more than code. They change the setup around it: prompts, models, tool permissions, dependencies, evals, docs, release records, and assumptions about how things run. Nuclear-grade starts with a questioning attitude. Then it keeps each controlled item in line with its spec or design basis, its verification evidence, its release decision, its baseline, and its operating lessons.

This is a teaching model for how to work, not a regulated quality program or a compliance claim.

---

## Core loop

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

| Phase | CM question | Minimum useful output |
|---|---|---|
| Question | What assumptions, doubts, and stop conditions must be surfaced? | Decision question, assumptions, warning signs, evidence gaps. |
| Discover | What sources, repo facts, incidents, or prior packets matter? | Links to public sources, repo files, issues, and known gaps. |
| Specify | What behavior or state is required? | Requirements, claims, design-basis facts, acceptance criteria, controlled item expectations. |
| Plan | How will controlled state change? | Work sequence, affected items, rollback, proof commands. |
| Execute | Did the work stay inside authority? | Diffs, generated artifacts, agent actions, deviations. |
| Verify | Does evidence match the claims? | Tests, reviews, evals, scans, status labels, gaps. |
| Review | Can a skeptical reviewer accept the change? | Claim-to-evidence review and residual risk disposition. |
| Decide | Should the change proceed, ship, block, defer, or continue with residual risk? | Decision, conditions, owner, baseline trigger. |
| Baseline | What accepted state is now controlled? | Commit/release/artifact plus controlled item versions and evidence links. |
| Operate | What signals show drift or failure? | Monitoring, support signals, incident triggers, user feedback. |
| Learn | What changes next time? | Basis, tests, controls, thresholds, templates, or re-baseline action. |

---

## Controlled items

Treat an item as controlled when a future reviewer needs to know its approved state, or when drift could weaken trust.

Common controlled items:

- code, tests, docs, templates, skills, command prompts;
- system prompts, chosen models, evals, context packs, the list of tools an agent can use;
- dependencies, build services, outside APIs, data sources, the rules for credentials;
- release files, changelog entries, runbooks, dashboards, monitoring limits;
- source-map rows, public claims, and the wording for the license and the limits of what you claim.

Use `templates/cm/controlled-items.md` when the affected list does not fit cleanly in `risk.md` or `plan.md`.

---

## Baselines

A baseline is the version everyone agreed is correct: an accepted state at a decision point, after review and a decision. It is not just a Git commit. A useful baseline records:

- the commit, PR, release, or artifact it points to;
- which controlled items are included;
- links to the spec or design basis and to the verification;
- known gaps and the leftover risks you accepted;
- the triggers that force a re-check or a new baseline.

Use `templates/cm/baseline.md` when a change updates public docs, skills, prompts, tools, dependencies, release posture, or any other state people trust.

---

## Change impact

Every controlled change should ask what else might go out of date as a result:

- docs and examples;
- tests, evals, checkers, CI;
- skills and command prompts;
- the wording about where ideas came from and the wording that marks your limits;
- rollout, support, security, and release records.

Use `templates/cm/change-impact.md` when more than one group of files can be affected.

## HPI control stack

For agent work that matters, ask which controls are in place:

| Control family | Examples |
|---|---|
| deterministic | tests, validators, CI, evals, permission boundaries |
| procedural | lifecycle, packet templates, command prompts, context packs |
| review / oversight | peer review, independent verification, release review |
| learning | OPEX record, near-miss issue, updated baseline, updated test/template/skill |

These families are layers of defense, not a checklist: the point is that no single control is trusted alone (defense in depth). The layers only add up if they fail **independently**. Stacking controls that share one failure mode buys far less than it looks — the same model that performs an action and then "checks" it is one barrier wearing two hats, not two; code and the tests or evals a single agent generates from the same wrong spec fail together; several wrappers around one brittle classifier all miss the same input. Independent backup uses a different model, context, or method, so it does not inherit the same blind spot (see `authority-and-intent.md`). Add independent layers in proportion to consequence: a Tier 0 action earns more — and more independent — layers than a reversible one (`risk-tiers-and-modes.md`).

Do not blame a model or a person as the only cause of drift. Ask which control was missing, weak, stale, or skipped.

---

## Variance, drift, and OPEX

Variance is a known, recorded gap from the approved baseline. Drift is a gap that nobody controlled or noticed. OPEX is lessons from real operation that should change future work.

Record them when:

- the way the software runs contradicts the baseline;
- users misread public claims;
- an agent goes past, or nearly goes past, what it is allowed to do;
- dependencies, models, APIs, or source pages change;
- verification evidence goes stale.

An OPEX lesson is closed only when it updates a lasting control, or records why no lasting update is needed.

---

## Exit criteria

Configuration management is working when a reviewer can answer:

1. What configuration item changed?
2. What assumptions were questioned and what specification authorized the change?
3. What impact was screened?
4. What evidence verified it?
5. What decision was made?
6. What baseline now controls it?
7. What would require revalidation or re-baselining?

## Source-lineage note

This model for keeping the approved version of everything under control is an original software workflow. It draws on public sources about configuration management, software assurance, secure development, systems engineering, the HPI questioning attitude, and learning from operation, mapped in `../00-standards-foundation/source-map.md`. It does not claim compliance with those sources.
