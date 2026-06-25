# Standard Risk Template

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

**Activation threshold:** Use for behavior users can see, lasting design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational stance, or anything where the stakes, the uncertainty, or the review value are more than trivial.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts you turn on, and the evidence due right away.

**Overhead trap:** Do not score risk with fake precision. Use the screen to surface the stakes and the evidence you need.

---

## Change identity

- Slug: pmbok-pmi-ai-crosswalk
- PR / issue: this PR
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21
- Current lifecycle phase: Decide
- Current work phase: audit
- Summary: Add a named-background crosswalk doc bridging Nuclear-grade to the PMBOK Guide and the 2026 PMI AI standard, fold value/stakeholder/tailoring lenses into five existing skills (bodies only), and log PMI publications as excluded-direct sources. No compliance claim.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: Give PM-literate and enterprise adopters a vocabulary bridge into the framework without importing PM ceremony or making any compliance/conformance claim.
- Success criteria: One crosswalk doc; three concept gap-fills folded into existing skills; source-governance logs PMI as named background; all repo gates pass; command cards unchanged.
- Non-goals / forbidden directions: No new skills/clusters/templates; no PMBOK/PMI text reproduced; no structure derived from paywalled standards; no PMP/compliance/conformance positioning.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: originating user request ("deep research on PMBOK and how it would influence the repo"); charter boundary discipline.

## Questioning-attitude summary

- Decision question: Can PMBOK / the PMI AI standard enhance the repo as *named background* without breaching the repo's paywalled-source policy or adding token burn?
- Evidence that would change the decision: If PMI were a public/open source it could be direct lineage; it is not — it is already listed excluded-direct.
- Assumptions that changed the mode: Touches public docs + source governance + multiple skills → Standard, not Quick.
- Facts still needing validation: None blocking; PMBOK 8 per-item names intentionally not reproduced (described structurally only).
- Stop or hold conditions: Stop if any wording implies compliance/conformance/PMP, or if a skill `description:` would change.

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| pmbok-pmi-ai-crosswalk.md | public doc | New external-standards bridge; boundary-sensitive | `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md` |
| source-map / do-not-cite-directly / compliance-boundaries | governance docs | Keep PMI named as background only | `docs/00-standards-foundation/` |
| 5 SKILL.md files | skills (prompts) | Body fold-ins; must not change descriptions or command cards | `skills/` |
| risk-tiers-and-modes / enterprise-rollout / README | docs | Name tailoring; discoverability links | (repo paths) |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Public wording about a standards body; brand/boundary risk if it reads as a compliance claim |
| Reversibility | high | Docs and one-line skill edits; trivially revertible |
| Detectability | high | `ng doctor` + overclaim scan + review catch boundary slips |
| Exposure | medium | Public README link; enterprise adopters |
| Uncertainty | low | PMBOK/PMI public framing well understood; sourcing policy explicit |
| Dependency trust | low | No code or dependency change |
| AI authority | low | No change to agent authority |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path + boundary self-check |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: Public wording about an external standards body plus source-governance changes across several surfaces.
- Why lighter mode is not enough: Quick cannot carry the boundary-wording and multi-surface review this needs.
- Why heavier mode is not yet required: No code, dependency, data, credential, or agent-authority change; fully reversible.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline above | Ben Huffer |
| `basis.md` | yes | State what must stay true (boundary) | Ben Huffer |
| `verification.md` | yes | Record the gate results | Ben Huffer |
| `ship.md` | yes | Release decision | Ben Huffer |
| `turnover.md` | no | No handoff | — |
| `self-check.md` | no | Folded into verification | — |
| `supplier-trust.md` | no | No dependency/model change | — |
| Nuclear subset record | no | Not Tier 0/1 | — |

## Immediate evidence obligations

- Minimum evidence before build: Confirm PMI is already excluded-direct in source-map (it is).
- Minimum evidence before merge/release: `ng doctor` OK; overclaim scan clean; `gen-commands` leaves command cards unchanged; links resolve.
- Independent review needed? yes — human review of boundary wording before merge (PR review).

## Required links

- Packet: `.nuclear/changes/pmbok-pmi-ai-crosswalk/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `docs/00-standards-foundation/source-map.md`, `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
