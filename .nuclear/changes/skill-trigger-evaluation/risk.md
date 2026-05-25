# Skill Trigger Evaluation Risk

## Change identity

- Slug: skill-trigger-evaluation
- PR / issue: local public-readiness follow-up
- Owner: FlyFission
- Date: 2026-05-25
- Current lifecycle phase: Verify / Review / Decide
- Summary: Strengthen all public skill trigger descriptions and add a reusable skill-evaluation prompt bank.

## Questioning-attitude summary

- Decision question: Do the skills trigger from realistic user prompts without adding unnecessary skill-folder bloat?
- Assumptions that changed the mode: Skill descriptions are the primary trigger surface, and public skill behavior is a controlled item.
- Facts still needing validation: Contract tests and validator output must pass after the description and evaluation-doc changes.
- Stop or hold conditions: Hold release if descriptions exceed contract limits, omit any skill from eval coverage, or imply formal assurance.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/*/SKILL.md` | skill frontmatter | Primary trigger descriptions determine whether agents consult the right workflow | repo |
| `docs/05-reference/skill-evaluation.md` | reference doc | Provides should-trigger and near-miss prompts for future baseline-vs-skill checks | repo |
| `docs/05-reference/skill-authoring-contract.md` | contract doc | States the expected skill-evaluation discipline | repo |
| `tests/test_skill_contracts.py` | contract test | Prevents trigger and eval-prompt regression | repo |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Public skill behavior affects adoption and agent workflow selection |
| Reversibility | high | Text and tests can be reverted with normal git history |
| Detectability | medium | Bad triggers may only show during realistic use unless tested |
| Exposure | medium | Public repo consumers will see and copy the skills |
| Uncertainty | medium | Trigger quality is partly behavioral and needs continued evals |
| Dependency trust | low | No runtime dependency changes |
| AI authority | medium | Skills guide agents that may edit files or make release recommendations |

## Selected mode

- Mode: Standard
- Why this mode: The change touches all public skills, tests, and reference docs.
- Why lighter mode is not enough: A Quick record would not preserve the trigger-quality assumptions and eval obligation.
- Why heavier mode is not yet required: No production system, dependency, credential, safety, or regulatory control changes.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Summary captured in this risk record | FlyFission |
| `basis.md` | yes | Need explicit claims for trigger and eval behavior | FlyFission |
| `verification.md` | yes | Contract tests and validators must prove the change | FlyFission |
| `ship.md` | yes | Public release posture changes | FlyFission |
| Nuclear subset record | no | No formal safety or regulatory claim | FlyFission |

## Immediate proof obligations

- Minimum evidence before build: Skill-creator guidance reviewed and mapped to concrete repo gaps.
- Minimum evidence before merge/release: Pytest, doctor, packet validator, and skill-evaluation coverage pass.
- Independent review needed? no; this is a low-code documentation/test refinement with automated contract checks.

## Required links

- Packet: `.nuclear/changes/skill-trigger-evaluation/`
- Basis: `basis.md`
- Verification: `verification.md`
- Ship: `ship.md`
- Source-map/crosswalk references if source lineage is invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Mode is justified.
- Activated artifacts are explicit.
- Important risks, assumptions, and proof obligations are visible in packet files.

## Source-lineage note

Original Nuclear-grade packet inspired by public graded quality, configuration management, lifecycle, software assurance, secure development, AI risk, and supply-chain sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
