# PMBOK and the PMI AI Standard — a rhyme, not a compliance matrix

**Status:** Named background, as of 2026. **Not** a conformance claim.

**Purpose:** Give project-management-literate and enterprise adopters a vocabulary bridge into
Nuclear-grade. It shows where this repo's *independently developed* practice happens to **rhyme
with** the public framing of two PMI publications:

1. the **PMBOK® Guide** (6th/7th/8th editions); and
2. the **PMI Standard for Artificial Intelligence in Portfolio, Program, and Project
   Management** (published 2026) — the first global standard for AI in project work.

**Boundary (read first).** Both publications are **paywalled PMI works**. Consistent with this
repo's standing policy, they are named as **background only**: no copyrighted text is reproduced,
no Nuclear-grade artifact is derived from their structure, and **nothing here claims compliance,
conformance, certification, PMP alignment, or endorsement.** The mappings below are conceptual and
deliberately coarse so a future edition (a PMBOK 9, a revised AI standard) does not falsify them.
PMI is already listed as *excluded as direct input* in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md) and
[`../00-standards-foundation/do-not-cite-directly.md`](../00-standards-foundation/do-not-cite-directly.md);
this page sits inside that boundary. See also
[`source-to-concept-crosswalk.md`](source-to-concept-crosswalk.md) for the repo's actual
(public-sourced) lineage.

> Use wording like: *an original, software-native, agent-authority workflow whose habits rhyme
> with public project-management framing.* Do **not** say *implements*, *complies with*, *conforms
> to*, or *is aligned with* a PMI standard.

---

## 1. Why this rhyme is worth naming

The 2026 PMI AI standard is, in public summary, built around **human-in-the-loop oversight at
every stage**, is **technology-agnostic**, and structures AI project work around governance, risk,
ethics, data quality, stakeholders, and value. That is the same problem Nuclear-grade attacks from
the engineering side: *let AI agents do serious work while a human stays in control of what ships.*
PMBOK 8 (2025) made an analogous move to Nuclear-grade's own shape — it pairs **principles**
(behavioral dispositions) with **reintroduced, non-prescriptive processes** and first-class
**tailoring**, which is structurally the same idea as this repo's **Core 7 dispositions +
control-point loop + risk-graded modes**.

Naming the rhyme lowers adoption friction for teams who already speak PMI, without importing PM
ceremony the framework does not need.

---

## 2. PMI AI Standard (2026) themes ↔ Nuclear-grade (lead table)

Themes below are from PMI's **public** descriptions of the standard (eight guiding principles;
five performance domains; a predictive/adaptive/hybrid lifecycle with human-in-the-loop). Names are
paraphrase, not quotation.

| PMI AI Standard public theme | Where Nuclear-grade already carries the same intent | Repo surface |
|---|---|---|
| Human-in-the-loop oversight at every stage | The agent-drafts / human-edits-and-approves loop; a self-check before any irreversible cut-point; trust-bearing specs need an independent approver | [`../../CORE.md`](../../CORE.md) (agent-drafts-spec loop), `double-checking-before-acting`, `agent-authority-model.md` (self-modification boundary) |
| Governance / accountability | Decision rights placed by reversibility and consequence; authority envelope in the charter; "who decides" before irreversible action | `deciding-who-decides`, `declaring-intent`, [`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md) |
| Risk | Risk-graded rigor (quick / standard / stronger); failure-mode naming before build | `rating-change-risk`, [`../02-operating-system/risk-tiers-and-modes.md`](../02-operating-system/risk-tiers-and-modes.md) |
| Data quality | Trust-check on external code, models, APIs, and generated artifacts before they are relied on | `vetting-outside-code-and-models`, `templates/standard/supplier-trust.md` |
| Ethics / responsible use | Public-claims discipline; keep wording inside its evidence; no overclaim | `checking-legal-and-safety-wording`, `checking-source-claims`, [`../../DISCLAIMER.md`](../../DISCLAIMER.md) |
| Stakeholders / stakeholder expectations | Name who is affected and who must be consulted when placing decision rights and briefing an agent | `deciding-who-decides`, `briefing-an-agent` |
| Strategic value / optimization | Frame the value and the cost of *not* acting at the question step and the release decision; context/token-burn discipline | `questioning-attitude`, `checking-release-readiness`, [`../02-operating-system/token-burn-control.md`](../02-operating-system/token-burn-control.md) |
| Recording / traceability of AI work | Structured run records of what an agent did (tool calls, inputs/outputs, approvals) | `recording-what-an-agent-did`, [`../02-operating-system/agent-trace-evidence.md`](../02-operating-system/agent-trace-evidence.md) |
| Predictive / adaptive / hybrid lifecycle; technology-agnostic | "Two speeds, one loop" (fast while exploring, slow when it becomes a promise); skills are tool-agnostic plain `.md` | [`../../WORKFLOWS.md`](../../WORKFLOWS.md), [`../../INTEGRATIONS.md`](../../INTEGRATIONS.md) |

**Enterprise note (EU AI Act / ISO 42001).** PMI's public materials position the AI standard as a
touchpoint for the EU AI Act and ISO/IEC 42001. Nuclear-grade is **not** a compliance instrument
for either; it can, however, produce the kind of *evidence trail* (decision rights, intent
declarations, run records, release decisions with named residual risk) that an organization's own
governance program may find useful as input. Treat that as a starting point for qualified review,
never as conformance. Adoption guidance lives in
[`../04-adoption/enterprise-rollout.md`](../04-adoption/enterprise-rollout.md).

---

## 3. PMBOK (6/7/8) ↔ Nuclear-grade

PMBOK 7's twelve principles and eight performance domains are well documented publicly and are used
here by their public names. PMBOK 8 (2025) is described **structurally only** (it consolidates to
six principles and seven performance domains and reintroduces ~40 non-prescriptive processes across
five focus areas) because the per-item names are not reproduced here.

| PMBOK 7 principle (public name) | Nuclear-grade rhyme |
|---|---|
| Stewardship | Own the change end to end; act as a careful steward of the codebase and the trust placed in it ([`leadership-and-high-reliability.md`](leadership-and-high-reliability.md), `staying-on-mission`) |
| Leadership | Push authority to where the evidence is, and declare intent before acting (`deciding-who-decides`, `declaring-intent`) |
| Team | Clean briefing and handoff between agents/people (`briefing-an-agent`, `handing-off-work`) |
| Stakeholders | Name who is affected / consulted (`deciding-who-decides`, `briefing-an-agent`) |
| Value | Value + cost-of-inaction at question and release (`questioning-attitude`, `checking-release-readiness`) |
| Systems thinking | Check what a change affects; ripple/re-check triggers (`checking-what-a-change-affects`) |
| Tailoring | Risk-graded modes — quick / standard / stronger (`rating-change-risk`, `risk-tiers-and-modes.md`) |
| Quality | Code-quality review; verification evidence over persuasion (`reviewing-code-quality`, `proving-claims`) |
| Complexity | Work breakdown (100% rule, no overlaps) before building (`breaking-down-the-work`) |
| Risk | Risk rating + failure-mode naming (`rating-change-risk`) |
| Adaptability & resiliency | Incident response; learning from experience into durable controls (`responding-to-incidents`, `learning-from-experience`) |
| Change | Configuration management: controlled items, baselines, change impact (`choosing-what-to-control`, `recording-a-known-good-version`) |

| PMBOK 7 performance domain | Nuclear-grade rhyme |
|---|---|
| Stakeholders | `deciding-who-decides`, `briefing-an-agent` |
| Team | `briefing-an-agent`, `handing-off-work` |
| Development approach & life cycle | "Two speeds, one loop"; modes ([`../../WORKFLOWS.md`](../../WORKFLOWS.md)) |
| Planning | `breaking-down-the-work`, `templates/standard/plan.md` |
| Project work | The Execute control point; stage contracts ([`../02-operating-system/agentic-workflow-architecture.md`](../02-operating-system/agentic-workflow-architecture.md)) |
| Delivery | `checking-release-readiness`, `templates/standard/ship.md` |
| Measurement | `ng` metrics / token audit; DORA-with-cautions note ([`../02-operating-system/token-burn-control.md`](../02-operating-system/token-burn-control.md)) |
| Uncertainty | `rating-change-risk`, standing `deficiency-register.md` |

**PMBOK 8's principle+process reconciliation** mirrors this repo's own structure: dispositions that
are always on (Core 7) plus concrete, non-prescriptive artifacts that fire by trigger (the
clusters and templates), with tailoring deciding how much rigor applies. Nuclear-grade arrived at
that shape independently from high-consequence engineering sources; the convergence is the point.

---

## 4. PMBOK artifacts (logs & registers) ↔ what Nuclear-grade already has

The repo does **not** need new artifacts to cover the common PMBOK logs and registers — it already
has equivalents. This table exists so a PMBOK-literate reader can find the door.

| PMBOK artifact | Nuclear-grade equivalent (already present) |
|---|---|
| Project charter | `.nuclear/charter.md` (authority envelope, mission anchor) |
| Risk register (per-change) | `templates/standard/risk.md` |
| Risk/issue register (standing) | [`../02-operating-system/deficiency-register.md`](../02-operating-system/deficiency-register.md), `tracking-deficiencies` |
| Lessons-learned register | `templates/cm/opex.md`, `learning-from-experience` |
| Change log / change control | [`../02-operating-system/change-control-packets.md`](../02-operating-system/change-control-packets.md), `.nuclear/changes/<slug>/` |
| Assumption log | The assumptions section of `questioning-attitude` / `risk.md` |
| Requirements & traceability | `templates/standard/basis.md`, `templates/standard/trace.md` |
| Configuration / baseline records | `templates/cm/controlled-items.md`, `templates/cm/baseline.md` |
| Stakeholder register | Covered lightly inside `deciding-who-decides` / `briefing-an-agent` — **intentionally not a standalone register** (agent-authority framework, not a PM stakeholder-management tool) |

---

## 5. What not to claim

Do not state or imply that Nuclear-grade:

- complies with, conforms to, or is certified against the PMBOK Guide or the PMI AI Standard;
- aligns with PMI standards, or qualifies anyone for the PMP or any PMI credential;
- is derived from, or reproduces, any PMI (or other paywalled) text;
- satisfies the EU AI Act, ISO/IEC 42001, or any regulatory regime.

This page is an original synthesis. It names PMI publications only as public background to help
adopters orient. See [`../../DISCLAIMER.md`](../../DISCLAIMER.md) and
[`../00-standards-foundation/compliance-boundaries.md`](../00-standards-foundation/compliance-boundaries.md).
