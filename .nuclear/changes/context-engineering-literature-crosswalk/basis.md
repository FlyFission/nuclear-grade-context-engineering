# Standard Basis Template

**Purpose:** State what must stay true for the change to be safe, reliable, secure, useful, and easy to review.

**Activation threshold:** Use for Standard changes where the requirements, architecture, interfaces, dependencies, AI power, protected outcomes, or outcomes to prevent need a clear basis.

**Minimum useful version:** the mission, the protected outcomes, the outcomes to prevent, the assumptions, the constraints, the trust decisions about intended use, and the evidence needs.

**Overhead trap:** Do not invent requirements by writing a long design essay. Link to the real needs and capture only the basis this change needs.

---

## Change context

- Slug: context-engineering-literature-crosswalk
- Related risk record: `risk.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03
- Decision this basis supports: Whether to add a crosswalk to two public context-engineering repos, and in what form, plus the small concept fold-ins it recommends.

## Mission / need

Adopters evaluating Nuclear-grade increasingly arrive from the broader "context engineering"
conversation — the academic survey/taxonomy on one side, the PRP coding-agent template on the other.
They need a bridge that shows where Nuclear-grade sits, what it borrows, and what is genuinely distinct
about it. This change supplies that bridge and folds in the highest-signal, lowest-surface adoptions
(a payload-component lens, a named blueprint-and-execute pattern, a production-memory pointer), while
preserving the repo's boundary discipline and flat always-on token cost.

## Protected outcomes

What must the system keep safe?

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The repo never implies endorsement by, affiliation with, or superiority over either external project | Brand/boundary integrity; fair representation of others' work | Overclaim scan clean; explicit boundary notes; `ng doctor` OK |
| The repo never implies it implements or conforms to the survey's taxonomy or the PRP method as a standard | Core "no compliance claim" posture | Boundary note + "what not to claim" section in the crosswalk |
| Always-on token cost stays flat | Context-window discipline | Skill `description:` unchanged; command cards unchanged |

## Unacceptable outcomes

What must not happen?

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A reader concludes Nuclear-grade is endorsed by or a fork of either project | Misrepresentation; reputational risk | Boundary note at top + "what not to claim" section; overclaim scan |
| Skill descriptions or command cards grow | Token burn across every fan-out | Docs-only change; no skill/command edits; verify with `gen-commands` diff |
| New unmaintained surface (extra docs/templates) | Drift, stale maintenance | One doc + targeted edits to existing docs; zero new templates/skills/commands |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Both repos are public and citable | fact | Public GitHub + arXiv; coleam00 MIT-licensed | A repo goes private/relicenses restrictively | Ben Huffer |
| Survey decomposes context into instructions/knowledge/tools/memory/state/query | source claim | Awesome-Context-Engineering README | Survey revises its taxonomy | Ben Huffer |
| PRP loop = generate-prp (blueprint) then execute-prp (against gates) | source claim | context-engineering-intro README | Template revises its workflow | Ben Huffer |
| Mappings kept conceptual/coarse | constraint | Avoid falsification on repo revision | — | Ben Huffer |

## Grounding status

Keep confidence apart from evidence before any derived claim is accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Survey treats context as a payload with six named components | source claim (public README + arXiv) | Awesome-Context-Engineering | Frames §2 taxonomy table + `context-packs.md` lens |
| PRP is a research→blueprint→execute-against-gates loop | source claim (public README) | context-engineering-intro | Frames §3 table + "Blueprint and execute" workflow |
| Each survey component and PRP element maps to an existing repo surface | local proof | The crosswalk maps to actual repo files | Justifies "complementary neighbors, additive" framing |
| Our spine (independence, graded rigor, baselines) is absent in both | local proof | Neither repo's docs carry these | Justifies the "what we add" section |

## Interfaces and trust boundaries

- Internal interfaces affected: cross-links among field-guide, standards-foundation, operating-system docs, WORKFLOWS, ROADMAP, docs/README.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: PR review of boundary wording before merge.
- AI/model/tool authority boundaries: unchanged.

## Dependency / model / supplier intended use

Use this section only when activated. — Not activated; no dependency, model, or service change.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHERE the repo references either external project THE SYSTEM SHALL frame it as a public peer/named background and state no endorsement, affiliation, or superiority claim. | Protected outcome 1 | Boundary note + "what not to claim" section in crosswalk | Overclaim scan; review |
| REQ-002 | THE SYSTEM SHALL NOT claim to implement or conform to the survey's taxonomy or the PRP method as a standard. | Protected outcome 2 | "Not a compliance claim" status line; conceptual mappings only | Doc inspection; review |
| REQ-003 | THE SYSTEM SHALL leave every skill `description:` and the generated command cards unchanged. | Token discipline | Docs-only change; no `skills/` or `commands/` edits | `git diff` on descriptions; `gen-commands` diff |
| REQ-004 | WHEN external repos are cited THE SYSTEM SHALL record them in `source-map.md` as verified-public with role and boundary notes. | Source governance | Two Tier 9 rows | `source-map.md` inspection |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | `risk.md`, this file |
| Architecture — shape and major parts | n/a | docs only |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes` |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: originating user request; `docs/01-field-guide/context-engineering-literature-crosswalk.md`
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
