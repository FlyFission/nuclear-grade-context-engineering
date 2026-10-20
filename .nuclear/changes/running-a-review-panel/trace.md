# Running a Review Panel — Trace

## Purpose

Link each claim the change makes to its basis, its implementation, and its evidence.

## Claim-to-implementation trace

| Claim ID | Implementation | Evidence |
|---|---|---|
| REQ-001 | `skills/running-a-review-panel/SKILL.md` — eight Process steps, each producing an entry in `## Outputs` | `verification.md` E-004; unmeasured, see V-14 |
| REQ-002 | Process step 3 (declare the axis, count distinct axes and families separately from seat count); `## Outputs` row 2; `## Verification` fold-down rule | `verification.md` E-004; enforcement limit at V-15 |
| REQ-003 | Process step 6 (panel health beside the result, "degraded panel" named); `## Escalation` bullet 2 | `verification.md` E-004 |
| REQ-004 | Process step 8 (verify here, then dispose; `verified` / `rejected` / `unresolved`); decision-contract failure class | `verification.md` E-004 |
| REQ-005 | Frontmatter description negative clause; `## When Not to Use` (six refusals); Process step 1 mode gate | `verification.md` E-004 |
| REQ-006 | No edit to `skills/reviewing-code-quality/`; `## When to Use` triggers on a verdict resting on one reviewer | `verification.md` V-16 (empty diff) |
| REQ-007 | `results-summary.md` row phrased as pending; `CHANGELOG.md` entry names the 28-versus-30 gap; `ship.md` named risk 1 | `verification.md` V-12, V-13 |
| REQ-008 | `nuclear-grade.yaml`, `SKILLS.md`, `CORE.md`, `COMMANDS.md`, `INSTALL.md`, `cli-reference.md`, `skill-authoring-contract.md`, `commands/ng-panel.md`, `tests/fixtures/command_prompts.json`, three test files | `verification.md` V-1, V-7, V-9, V-10 |
| REQ-009 | No `pyproject.toml` change, no new directory, no `source-map.md` change | `verification.md` V-11 |
| REQ-010 | `## Verification` boundary paragraph; `## Source-lineage note` in the skill | `verification.md` E-004 |

## Claim-to-source trace

| Claim as stated in the skill | Source | Status |
|---|---|---|
| Diversity as a defense against correlated failure in redundant review | NUREG/CR-6303 diversity taxonomy | already registered in `source-map.md`; concept lineage only, no new row added |
| Independence has distinct axes (technical, managerial, financial) rather than one scale | NASA SWE-141 | already registered in `source-map.md`; concept lineage only |
| Reliance on a tool should set how hard the tool is qualified | NASA SWE-136 | already registered in `source-map.md`; concept lineage only |
| Verification performed by someone other than the performer | DOE-HDBK-1028-2009 | already registered in `source-map.md`; concept lineage only |
| A model judging its own or a kin model's output shows self-preference and preference leakage | arXiv:2502.01534 | already registered in `source-map.md`; concept lineage only |
| The eight-step procedure, the seat-axis declaration, the panel-health record, and the verify-before-dispose rule | **this repository's authored extension** | not attributed to any external source |

## Doctrine-to-procedure trace

| Assertion already in the repo | Where it was made | Where the method now lives |
|---|---|---|
| High-consequence verdicts should use a panel plus a meta-judge | `evaluation-integrity.md` §4 | `running-a-review-panel` Process steps 1 to 8 |
| A panel sharing one biased brief is one view voiced three times | `evaluation-integrity.md` §4 | Process step 3 and the fold-down rule in `## Verification` |
| A check must name the diversity axis it varies | `independence-architecture.md` | Process step 3; `## Outputs` axis and family counts |
| The actor's own evidence is a coupled surface | `actor-evidence-independence.md` | `## When to Use` trigger 4; Process step 4 withholds the actor's conclusion |

## Gaps

| Gap | Why it is open | Disposition |
|---|---|---|
| No efficacy measurement for this skill; benchmarked set is 28, shipped set is 30 | The July 2026 pilot is a historical snapshot; bolting one late entry onto it would misrepresent the snapshot, and a fresh run needs its own design and pre-registration | Disclosed in the comparison table as pending, in the CHANGELOG, and as named risk 1 in `ship.md`. Not closed |
| The procedure has never been executed end to end | No panel has been convened with it; every behavioral claim is derived by reading | Named risk 2 in `ship.md`; the skill's own `## Verification` section makes the matching admission about its outputs |
| The axis declaration is unenforced | A seat can assert an axis it does not vary; the fold-down rule is executed by whoever runs the panel, possibly the same agent that composed the seats | Named risk 3 in `ship.md`; stated as a design limit, not fixed here |
| Hosted CI has not run on the merge commit | The merge was made locally; GitHub last ran on 2026-08-05 against a base that no longer exists | `verification.md` V-18 held at `planned`; owed before merge |
| This packet was written after the change | The branch was developed from a design discussion with no packet open | Recorded in `risk.md` under "Record-order deviation" and in `plan.md` task 14 |
| Cluster placement in `CORE.md` is a judgment call | The trigger shape matches Agent authority, but the skill is arguably its own concern; a sixth cluster is something `CORE.md` resists | Open for the reviewer; no evidence settles it |

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Plan: `plan.md`
- Verification: `verification.md`
- Ship: `ship.md`

## Exit criteria

- Every claim links to an implementation and an evidence row, or to a stated gap.
- The doctrine this change implements is traced to the step that implements it.
- The authored extension is distinguished from the external concept lineage.

## Source-lineage note

Original Nuclear-grade packet inspired by public configuration-management and traceability concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
