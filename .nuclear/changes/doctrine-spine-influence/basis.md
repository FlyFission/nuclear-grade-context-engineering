# Standard Basis Record

**Purpose:** State what must stay true while we turn the owner's influences into Nuclear-grade controls.

**Activation threshold:** Use because public docs, skills, commands, templates, and adoption surfaces need an explicit design basis.

**Minimum useful version:** Mission, protected outcomes, unacceptable outcomes, assumptions, constraints, influence mapping, and evidence needs.

**Overhead trap:** Do not convert influence into a doctrine essay. Capture only the controls needed for users, agents, and reviewers.

---

## Change context

- Slug: doctrine-spine-influence
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-05-30
- Decision this basis supports: Accept or block the doctrine-spine update for public workflow artifacts.

## Mission / need

Nuclear-grade needs a tighter control spine: question the decision first, make instructions hard to misuse, keep small work aligned to mission, ground claims in evidence, let agents build candidates quickly, and slow acceptance before claims, baselines, and releases.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| End users can still start quickly | Doctrine that slows every action would undermine adoption | Quickstart review and public-doc tests |
| Downstream agents receive operational instructions | Agent behavior is driven by skill descriptions, command cards, and templates | Skill/command contract tests and manual trigger review |
| Claims remain grounded | Public methodology must not confuse influence, source claim, local proof, or authority | Boundary scan and updated proving/source language |
| Acceptance gates remain deliberate | Fast candidate work must not become accepted configuration without evidence | Ship and baseline records |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| Quotes or named attributions appear in public artifacts | Creates source and attribution burden outside the chosen scope | Quote-exclusion scan |
| Inspirational wording replaces controls | Users and agents get prose without behavior change | Change-impact review across docs, skills, commands, templates |
| Every edit becomes slow | End users abandon the workflow as ceremony | Activation-threshold and Quickstart language preserve Quick mode |
| Subjective confidence is treated as proof | Release decisions become persuasion again | Claim-to-evidence and fact/source separation updates |
| Public language implies assurance | Legal/trust boundary weakens | Doctor and prohibited-claim scans |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Existing docs are the chosen surface | fact | User selected existing-docs approach | User requests a new doctrine page | FlyFission |
| No quotes or named attributions | fact | User direction and approved plan | User explicitly requests quoted material | FlyFission |
| Existing test contracts should remain enough | assumption | Current plan excludes validator changes | Tests cannot detect an unsafe required behavior | FlyFission |
| This is a public workflow-control update | fact | Risk screen | Scope expands to code, dependency, model, API, or release automation | FlyFission |

## Grounding status

Separate confidence from evidence before derived claims are accepted.

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| Existing docs are the chosen surface | fact | User selected existing-docs approach | Controls are added to existing artifacts, not a new page |
| No quotes or named attributions should be added | fact | User direction and approved plan | Boundary scan and packet wording must preserve this |
| Contract tests cover agent-facing structural regressions | local proof | `tests/test_skill_contracts.py` and `tests/test_command_contracts.py` | Passing tests support PR acceptance |
| Semantic quality of doctrine wording is partly review-based | assumption | `ship.md` residual risk | PR/Copilot review and future OPEX remain acceptance controls |
| PR review can block acceptance | decision authority | `ship.md` | Actionable review feedback must be addressed or explicitly dispositioned |

## Interfaces and trust boundaries

- Internal interfaces affected: skill contracts, command card contracts, Standard template fields, public docs, adoption docs, evaluation prompts.
- External services/APIs affected: none.
- Data classes affected: none.
- Human approval boundaries: PR review and requested Copilot review before merge.
- AI/model/tool authority boundaries: agent-facing instructions change; no new tool permissions are granted.

## Dependency / model / supplier intended use

Not activated. No dependency, model, API, SaaS, generated artifact, vendor claim, credential, or network authority changes.

## Doctrine influence mapping

| Control | Software translation | Artifact surface | Evidence planned |
|---|---|---|---|
| Decision-question discipline | Start by naming the decision and evidence that would change it | risk, lifecycle, questioning skill, classify command | Review and contract tests |
| Operational unambiguity | Instructions should be hard to misuse under pressure | skills, commands, templates | Skill/command contract tests |
| Mission-aligned small work | Local actions must serve objective and non-goals | charter, drift skill, risk/plan templates | Manual review |
| Grounded truth | Separate fact, assumption, unknown, source claim, local proof, and authority | basis, proving skill, verification templates | Boundary scan and tests |
| Two-speed control | Build candidates quickly; audit acceptance slowly | lifecycle, thresholds, Quickstart, ship template | Public-doc review |
| Cut-point self-checking | Measure exact target before critical or trust-bearing action | self-check skill/command, HPI overlays | Manual review |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| C-001 | Public docs express the control stack without quotes or new attributions | Owner direction | Existing-doc updates plus boundary scan | `verification.md` |
| C-002 | Downstream-agent surfaces are harder to misuse | Agent-facing need | Skill, command, template, and evaluation updates | Contract tests and manual review |
| C-003 | The workflow preserves fast exploration and slow acceptance | Adoption constraint | Quickstart, thresholds, lifecycle, ship/baseline edits | Public-doc review |
| C-004 | The review surprise becomes a durable control update | OPEX principle | `opex.md` and affected surfaces | Packet validation |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: user-approved plan in conversation
- Source lineage, if cited: existing notes map to `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Builder and reviewer can answer "what must remain true?"
- Protected and unacceptable outcomes are explicit.
- Important assumptions have invalidation triggers.
- Evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis record inspired by public design-basis, safety-in-design, design-description, hazard/failure-analysis, AI-risk, and supply-chain-risk concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
