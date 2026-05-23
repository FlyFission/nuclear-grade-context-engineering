# Configuration Management

**Purpose:** Define the Nuclear-grade configuration-management spine for AI-assisted software work.

**Thesis:** AI agents change more than code. They change configuration: prompts, models, tool permissions, dependencies, evals, docs, release records, and operational assumptions. Nuclear-grade starts with questioning attitude, then keeps controlled items consistent with their specification/design basis, verification evidence, release decision, baseline, and operating lessons.

This is an educational operating model, not a regulated quality program or compliance claim.

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

Treat an item as controlled when a future reviewer needs to know its approved state or when drift could weaken trust.

Common controlled items:

- code, tests, docs, templates, skills, command prompts;
- system prompts, model selections, evals, context packs, tool registries;
- dependencies, build services, external APIs, data sources, credentials policy;
- release artifacts, changelog entries, runbooks, dashboards, monitoring thresholds;
- source-map rows, public claims, license and assurance boundary wording.

Use `templates/cm/controlled-items.md` when the affected list cannot fit cleanly in `risk.md` or `plan.md`.

---

## Baselines

A baseline is an accepted configuration state at a decision point after review and decision. It is not just a Git commit. A useful baseline records:

- commit, PR, release, or artifact identity;
- controlled items included;
- specification/design-basis and verification links;
- known gaps and accepted residual risks;
- revalidation and re-baseline triggers.

Use `templates/cm/baseline.md` when a change updates public docs, skills, prompts, tools, dependencies, release posture, or other trust-bearing state.

---

## Change impact

Every controlled change should ask what downstream state may become stale:

- docs and examples;
- tests, evals, validators, CI;
- skills and command prompts;
- source lineage and boundary language;
- rollout, support, security, and release records.

Use `templates/cm/change-impact.md` when more than one artifact family can be affected.

---

## Variance, drift, and OPEX

Variance is known deviation from the approved baseline. Drift is uncontrolled or unnoticed divergence. OPEX is operating experience that should change future work.

Record them when:

- runtime behavior contradicts the baseline;
- users misunderstand public claims;
- an agent exceeds or nearly exceeds authority;
- dependencies, models, APIs, or source pages change;
- verification evidence becomes stale.

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

This configuration-management model is an original software-native workflow inspired by public configuration-management, software assurance, secure-development, systems-engineering, HPI questioning-attitude, and operating-learning sources mapped in `../00-standards-foundation/source-map.md`. It does not claim compliance with those sources.
