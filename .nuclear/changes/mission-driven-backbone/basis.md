# Basis

## Change context

- Slug: mission-driven-backbone
- Scope: Two-tier mission-driven backbone plus two drift skills and their commands.
- Outcome to protect: The repo can detect and correct engineering drift without heavyweight mandatory process.

## Need and scope

AI agents drift across long sessions: they keep completing tasks while the work stops serving the objective, and rigor erodes one concession at a time. The repo controls configuration/baseline drift but nothing else. This change adds a durable charter (how we work) and a per-change mission anchor (what this change is for), plus skills and commands that force a re-anchor / escalate / stop decision and a standards-drift code review.

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| C-001 | A durable charter of named process-integrity principles exists at `.nuclear/charter.md` and `init` writes a starter charter. | File exists; `tests/test_ng_cli.py::test_init_creates_charter_and_mission_anchor`. |
| C-002 | A per-change mission anchor (objective + success + non-goals) is a section in the Standard risk template, and a workspace anchor is written by `init`. | Diff of `templates/standard/risk.md`; init test. |
| C-003 | `staying-on-mission` is a valid skill: 11-section contract, drift symptoms as triggers, the re-anchor/escalate/stop triad, a counted (3-attempt/loop) escalation trigger, and Rickover/Navy principles woven in. | `tests/test_skill_contracts.py`; live `doctor`. |
| C-004 | `reviewing-code-quality` is a valid skill capturing standards-drift review (delete-first, countable tripwires, abstraction-earns-keep, layering, single verdict). | `tests/test_skill_contracts.py`; live `doctor`. |
| C-005 | `ng-drift-check.md` and `ng-code-review.md` are valid command prompts (10-section contract). | `tests/test_command_contracts.py`; live `doctor`. |
| C-006 | The validator advisory-checks a mission anchor only when present (objective + success + non-goals) and flags unresolved clarification markers (the spec-kit style NEEDS-CLARIFICATION token), without breaking existing packets. | New `tests/test_ng_validate.py` cases; all existing packets still validate. |
| C-007 | A drift gate (charter and anchor check, re-checked before Verify, with a justification table) is present in the Standard plan template. | Diff of `templates/standard/plan.md`. |
| C-008 | Retrofits and registration land together: questioning-attitude, briefing-an-agent, checking-release-readiness, using-nuclear-grade, context-packs, WORKFLOWS, SKILLS.md, COMMANDS.md, nuclear-grade.yaml, skill-evaluation.md, results-summary.md. | Diffs; contract + public-doc tests. |

## Assumptions, constraints, and invalidation triggers

- Assumption: advisory only-when-present checks leave existing packets green. Invalidation trigger: any existing packet fails after the validator change.
- Constraint: no em dashes or en dashes.
- Constraint: both new skill descriptions obey the current 90-180 char "Use when" rule; the rule itself is not changed here.

## Acceptance scenarios

- A maintainer runs `nuclear-grade init` in a fresh workspace and finds `.nuclear/charter.md` and `.nuclear/mission.md`.
- An agent twenty steps into a task runs `ng-drift-check`, restates the anchor, and gets a re-anchor / escalate / stop decision.
- A reviewer runs `ng-code-review` on a 1500-line module and gets prioritized deletions and a single verdict.
- A packet with a Mission anchor missing its non-goals fails validation with a clear advisory message; a packet with no anchor validates unchanged.

## Required links

- Packet: `.nuclear/changes/mission-driven-backbone/`
- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Claims C-001 through C-008 are mapped to plan steps and have evidence rows.

## Source-lineage note

Original Nuclear-grade packet influenced by nuclear-industry safety and quality culture and the human-performance practices mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
