# Risk Tiers and Modes

**Purpose:** Give risk-tiered rigor a single taxonomy. The repo already grades work by **mode** — `quick`, `standard`, and the activated high-stakes mode named **Nuclear** (see [`modes.md`](modes.md)); this doc maps the familiar Tier 0–3 language onto those modes so there is one axis, not two. This honors Charter Art. 9 (graded rigor) and Art. 12 (operational unambiguity).

**Boundary:** Original software-workflow translation. It does not create formal assurance, compliance, certification, safety, or regulatory adequacy.

---

## One taxonomy: tiers map onto modes

The mistake is to apply critical-systems ceremony to a button-color change. The correct move is rigor scaled to consequence — and to express it through the modes the repo already validates, not a competing label.

| Tier (consequence) | Examples | Repo mode | Required rigor |
|---|---|---|---|
| Tier 0 — existential | auth, payments, encryption, production data deletion, infra-wide networking, agent production authority | Nuclear | design review, two-person/independent review, rollback plan, observability, dry run, post-change verification, baseline |
| Tier 1 — high | major backend release, schema migration, model rollout, permission changes | Standard | basis + plan, test/eval evidence, canary, alerting, owner sign-off, intent release brief |
| Tier 2 — normal | feature work, API extension, UI release | Standard or Quick | standard review, automated tests, feature flags where useful |
| Tier 3 — experimental | prototype, internal tool, throwaway exploration | Quick | lightweight review, time-boxed, no production authority |

How to use it: classify the work type with the work-type lens (`work-type-lens.md`) — orthogonal to the tier, it shapes which questions you ask, not how much rigor — then rate consequence and reversibility with `rating-change-risk`, pick the mode, and — for Tier 0/1 — add the intent release brief (`authority-and-intent.md`) and, at Tier 0, the critical-systems controls (`critical-systems.md`). Do not invent a separate "tier" record; the mode is the record.

## Design review at the higher tiers

A nuclear-style design review is a structured attack on assumptions, not a meeting to admire diagrams. For Tier 0/1, require: architecture and data-flow sketch, failure-mode analysis, threat model, dependency map, rollback plan, observability plan, named operational owner, security/privacy impact, and a migration/deprecation plan. For critical systems, include a competent reviewer from outside the team. The questioning-attitude and reviewing-code-quality skills carry this.

## Code review for risky changes

A nuclear-style code review of a risky PR asks more than "does this look clean?" (that complexity check is `reviewing-code-quality`). It asks about risk:

| Area | Question |
|---|---|
| Correctness | What invariant does this preserve? |
| Failure | What happens if this partially succeeds? |
| Observability | How will we detect bad behavior? |
| Recovery | Can we roll back safely? |
| Security | Did permissions, secrets, auth, or input validation change? |
| Data | Is there migration, backfill, deletion, or consistency risk? |
| Blast radius | How many users or systems can this affect? |
| Test evidence | What proves this works? |
| Operations | Does whoever supports it know how? |

For AI-authored changes the same review applies, plus: the human reviewer must understand the generated code before merging, treat it as a hypothesis rather than authority, and record why it was accepted for critical paths.

## Source-lineage note

Original Nuclear-grade operating doc influenced by SUBSAFE-style risk-tiering and conservative-design practice and the graded-rigor and design-review habits in public high-reliability software guidance, used as concept lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
