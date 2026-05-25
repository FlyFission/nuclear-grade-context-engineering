# Skill Trigger Evaluation Basis

## Change context

- Slug: skill-trigger-evaluation
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-05-25
- Decision this basis supports: Update skill descriptions and add an evaluation prompt bank for future trigger testing.

## Mission / need

The repo needs skills that are concise enough to use, specific enough to trigger, and testable enough to improve without guesswork.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Trigger descriptions remain concise and concrete | The description is the first agent selection surface | Skill contract test |
| Every public skill has eval prompts | Future changes need realistic should-trigger and near-miss coverage | Evaluation prompt coverage test |
| Skill folders stay lean | Extra files inside each skill would dilute the public skill surface | Manual review of changed files |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A skill description becomes vague or too broad | Agents may miss the skill or over-trigger it | Minimum and maximum description-length tests |
| Evaluation prompts omit a skill | Future changes could be made by taste alone | Coverage test keyed to expected skill folders |
| Public docs imply formal assurance | Users may misunderstand the repo boundary | Existing public-doc tests and validator language checks |

## Assumptions and constraints

| Assumption / constraint | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|
| Description text is the primary trigger surface | Local Codex skill-creator and Anthropic skill-creator guidance | Tooling changes skill triggering semantics | FlyFission |
| Prompt bank belongs in reference docs, not each skill folder | Skill-creator guidance discourages extraneous files inside skills | Repeated evals show a skill needs bundled resources | FlyFission |
| Three positive and two negative prompts per skill are a useful minimum | Anthropic skill-creator recommends realistic trigger evals | More formal benchmark tooling is adopted | FlyFission |

## Interfaces and trust boundaries

- Internal interfaces affected: skill frontmatter, docs reference index, skill contract tests.
- External services/APIs affected: not applicable.
- Data classes affected: public docs and test artifacts only.
- Human approval boundaries: maintainer review remains required before release.
- AI/model/tool authority boundaries: skills guide AI workflow selection but grant no credentials or production authority.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| Local Codex skill-creator | Skill authoring guidance | Trigger descriptions may underperform | Contract tests and prompt bank | Local guidance updates |
| Anthropic skill-creator | External best-practice comparison | Eval process may lag ecosystem practice | Public source review and conservative adaptation | Upstream skill-creator changes |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | All skills have concrete trigger descriptions within repo limits | Skill authoring guidance | Frontmatter update and length tests | Pytest |
| REQ-002 | Every skill has at least three should-trigger and two should-not-trigger prompts | Evaluation discipline | `docs/05-reference/skill-evaluation.md` and coverage test | Pytest |
| REQ-003 | No bundled resources are added without demonstrated repeated need | Progressive-disclosure principle | Reference doc outside skill folders | Git diff review |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: public-readiness follow-up
- Source lineage, if cited: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Builder and reviewer can answer what must remain true.
- Protected and unacceptable outcomes are explicit.
- Important assumptions have invalidation triggers.
- Evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade basis inspired by public design-basis, safety-in-design, design-description, hazard/failure-analysis, AI-risk, and supply-chain-risk concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
