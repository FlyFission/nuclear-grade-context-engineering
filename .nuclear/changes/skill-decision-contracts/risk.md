# Risk -- skill decision contracts

**Purpose:** Sort this change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: skill-decision-contracts
- PR / issue: branch `claude/practical-faraday-dwcv5b` (PR to follow)
- Owner: FlyFission
- Date: 2026-06-16
- Current lifecycle phase: Verify
- Current work phase: audit
- Summary: Add a required five-field `## Decision contract` receipt to every skill (claim checked, artifact observed, decision affected with a block/warn/observe tier, failure class, next action), enforce it in `ng doctor` and the skill-contract tests, and add `ng decisions` as an operator receipt that promotes block/warn and keeps observe in telemetry.

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective: Make every skill name the decision it can change, so a reviewer scans one declaration instead of auditing prose -- Charter Art. 11, enforced structurally.
- Success criteria: every skill carries a well-formed decision contract; `ng doctor` and the tests enforce it; `ng decisions` renders all 27; the token budget stays green.
- Non-goals / forbidden directions: cutting or merging skills; rewriting skill bodies as a prose sweep; self-declaring a skill as deletable.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: reviewer feedback on decision artifacts, and `.nuclear/charter.md` Article 11.

## Questioning-attitude summary

- Decision question: should every skill be required to declare, in a scannable and machine-checkable block, the one decision it can change and its tier?
- Evidence that would change the decision: a block that becomes generic boilerplate which never changes a reader's judgment, or that blows the token budget.
- Assumptions that changed the mode: this edits the skill authoring contract and the validator -- controlled items every skill and CI depend on.
- Facts still needing validation: none open; tests, doctor, and tokens pass locally.
- Stop or hold conditions: stop if the budget gate fails, or if any skill cannot name a non-generic decision.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/*/SKILL.md` (27) | skill contract | each gains the required block | `skills/` |
| `nuclear_grade/cli.py` | validator and CLI | enforces the block, adds `ng decisions` | `nuclear_grade/cli.py` |
| `docs/05-reference/skill-authoring-contract.md` | contract doc | defines the block and the classes | `docs/05-reference/skill-authoring-contract.md` |
| `tests/test_skill_contracts.py` | test | guards the contract | `tests/test_skill_contracts.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | shapes every skill and the contract, but is docs and tooling, not runtime |
| Reversibility | high | text plus a lint; reverted by a single commit |
| Detectability | high | doctor, tests, and tokens fail loudly on regression |
| Exposure | medium | public docs and the skill surface |
| Uncertainty | low | the change is well understood and locally verified |
| Dependency trust | low | no new dependencies |
| AI authority | low | no agent runtime authority changes |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | yes | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | no | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: it changes a controlled item -- the skill authoring contract -- that every skill and the CI gate depend on.
- Why lighter mode is not enough: a Quick record would not trace the contract change across 27 skills, the validator, and the docs.
- Why heavier mode is not yet required: the change is reversible docs and tooling with no runtime or trust-boundary effect.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | summarized inline in this record | FlyFission |
| `basis.md` | yes | states the requirements the change must meet | FlyFission |
| `verification.md` | yes | records the test, doctor, and token evidence | FlyFission |
| `ship.md` | yes | records the release decision | FlyFission |
| `turnover.md` | no | no handoff | FlyFission |
| `self-check.md` | no | low-risk reversible change | FlyFission |
| `supplier-trust.md` | no | no new dependency | FlyFission |
| Nuclear subset record | no | the stakes do not warrant it | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the block format and the class taxonomy agreed in the authoring contract.
- Minimum evidence before merge/release: `pytest`, `ng doctor`, and `ng tokens` all green, and `ng decisions` renders 27 skills.
- Independent review needed? yes; why: it edits the public skill contract and the validator, so a human approves before merge.

## Required links

- Packet: `.nuclear/changes/skill-decision-contracts/`
- `questioning-attitude.md` if activated: not activated; summarized in `risk.md`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: `docs/05-reference/skill-authoring-contract.md`

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade change record, influenced by public graded-rigor and risk-classification ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
