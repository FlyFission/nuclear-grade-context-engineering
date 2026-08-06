# Basis: Inspectable builder-critic loop

## Change context

- Slug: `inspectable-builder-critic-loop`
- Related risk record: `risk.md`
- Owner: FlyFission maintainer
- Date: 2026-08-06
- Decision supported: whether a narrow, measured improvement-loop technique belongs in a follow-up PR.

## Mission / need

Nuclear-grade already separates actors from evidence, plans vertical slices, and distinguishes verification, review, and release. It lacks one compact operational rule for repeatedly improving an inspectable artifact against a frozen bar while targeting the largest consequential gap. The change should deepen existing seams rather than add a competing workflow.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Existing lifecycle and release authority remain controlling | A critic must not become an alternate acceptance path | public contract test and diff review |
| Evidence custody and five-axis coupling remain visible | Fresh context alone can launder dependence | template/brief wording and adversarial review |
| Coupled work retains coherent ownership | Broad fan-out can create integration defects | plan/workflow contract |
| Adverse findings and unresolved gaps survive | Bounded iteration must not manufacture a clean pass | verification/ship flow |
| Efficacy claims stay bounded to observed evidence | Practitioner examples do not generalize automatically | pilot contract and source-map boundary |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| New mode, lifecycle, promoted skill, or release authority appears | fault | control duplication and route drift | REQ-001 and public contract test |
| Builder weakens the bar or controls critic evidence/retention | fault | self-certifying loop | REQ-002 and five-axis custody wording |
| Fresh critic is called independent without basis | insufficiency | misleading evidence weight | REQ-003 and verification wording |
| Bound expires but result is reported as pass | fault | false acceptance | REQ-004 terminal states |
| Critic score rises while external artifact quality does not | insufficiency | reward-hacking style false progress | REQ-006 pilot measures/kill criteria |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Type | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Existing Standard templates are the stable public seam | fact | repository inspection | template ownership changes | maintainer |
| Practitioner evidence is useful for mechanics, not efficacy | source claim | Shumer article/repository | stronger replicated evidence | maintainer |
| A dedicated skill would currently duplicate promoted skills | inference | catalog and workflow inspection | pilot demonstrates distinct routing value | maintainer |
| PR #98 lifecycle/catalog changes are the prerequisite base | fact | draft PR #98 | base retargeted or rejected | maintainer |

## Interfaces and trust boundaries

- Internal interfaces affected: public workflow doctrine, briefing skill/prompt, Standard plan/verification, source map, public/parity tests.
- External services/APIs affected: none.
- Data classes affected: public Markdown and test fixtures only.
- Human approval boundaries: maintainer retains acceptance, merge, release, and later skill-promotion authority.
- AI/model/tool authority boundaries: critic reports findings/evidence status only; no release verdict.
- Stable public seam for behavior tests: `tests/test_public_docs.py` and `tests/test_command_parity.py`.
- Deep-module boundary: one optional targeted improvement technique behind existing Execute/Verify and briefing/template interfaces.
- Prototype boundary: measured pilot contract only; no live efficacy claim or dedicated skill in this PR.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN targeted iteration is used THE WORKFLOW SHALL keep it inside Execute and Verify and SHALL preserve Review, Decide, Baseline, and release authority. | lifecycle doctrine | `WORKFLOWS.md` boundary | public contract test |
| REQ-002 | WHEN a cycle starts THE PLAN SHALL freeze the inspectable bar, custodian, candidate scope, critic inputs, retention, and stop rule outside unilateral builder control. | adversarial custody review | Standard plan and briefing fields | public/parity tests |
| REQ-003 | WHEN work is decomposed THE PLAN SHALL fan out only independently judgeable slices, keep coupled work under one sequential owner, and disclose five-axis critic coupling. | source warning plus existing coupling doctrine | workflow/plan/verification wording | public contract and review |
| REQ-004 | WHEN a round completes THE VERIFICATION RECORD SHALL target the largest consequential unresolved gap, inspect the fresh artifact, preserve adverse findings, and stop non-pass at declared bounds. | improvement-loop mechanics plus claims discipline | verification rule and ship carryover | public contract test |
| REQ-005 | WHEN an operator uses `ng-context-pack` THE GENERATED COMMAND SHALL carry the optional bounded-cycle fields without projection drift. | command ownership contract | prompt asset, golden fixture, regenerated card | command parity tests |
| REQ-006 | BEFORE a dedicated skill is proposed THE REPO SHALL require a paired, externally adjudicated pilot and a fresh hidden confirmation set; critic scores SHALL NOT count as outcome evidence. | evaluation integrity | pilot contract and source boundary | public contract/review |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview | yes | `WORKFLOWS.md` |
| Architecture | yes | optional subroutine inside Execute/Verify |
| Components/interfaces | yes | existing briefing, plan, verification, ship seams |
| Data models | n/a | Markdown records only |
| Error handling | yes | NOT VERIFIED / INCONCLUSIVE / BLOCKED |
| Testing strategy | yes | `verification.md` |

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Verification: `verification.md`
- Ship: `ship.md`
- Source lineage: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Builder and reviewer can distinguish improvement evidence from acceptance authority.
- The optional path has one source of truth for each field and no duplicate ledger.
- Evaluation and promotion claims are fail-closed.

## Source-lineage note

This basis selectively adapts public practitioner mechanics under Nuclear-grade's existing evidence and authority controls. It makes no general efficacy or assurance claim.
