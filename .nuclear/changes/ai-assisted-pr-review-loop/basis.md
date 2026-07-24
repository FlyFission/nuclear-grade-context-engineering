# AI-Assisted PR Review Loop: Basis

## Change context

- Slug: ai-assisted-pr-review-loop
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-07-24
- Decision this basis supports: Whether the proposed role diagram and template controls are coherent enough to open a public pull request.

## Mission / need

Make the existing Nuclear-grade AI-assisted change loop as easy to understand as the external diagram while preserving stronger controls: role-based authority, criteria validation, evidence custody, exact-candidate identity, bounded remediation, human merge/apply authority, and post-release learning.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The public workflow remains readable at a glance | Simplicity is the external artifact's strongest contribution | README and canonical Mermaid review |
| Roles, not vendors, carry authority | Model names do not establish independence or durable process | Role labels in both diagram copies and workflow prose |
| A verdict applies only to the exact reviewed candidate | Late edits, rebases, generated files, or conflict resolution can stale a verdict | `ship.md` identity fields and contract test |
| Review loops remain bounded without lowering criteria | Endless model loops create churn and criteria drift | `plan.md` correction budget and escalation fields |
| Human merge and apply authority remains explicit | Model review is advisory evidence, not release authorization | Diagram, workflow prose, and ship record |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind (fault / insufficiency) | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| A model brand is treated as an authority or independence guarantee | insufficiency | Brittle and misleading governance | Role-based labels and custody language |
| A prior verdict silently survives a material candidate change | fault | Unreviewed code or artifact may be merged | Candidate IDs, stale verdict state, re-review requirement |
| The builder authors criteria, evidence, and verdict without disclosed coupling | insufficiency | Persuasive self-check is mistaken for independent evidence | Human criteria approval, custody note, verifier role |
| A fixed one-round rule blocks useful correction or an unbounded loop consumes work | insufficiency | Either premature stop or review churn | Declared budget with human escalation |
| The change creates a duplicate workflow or new compliance claim | insufficiency | Method accretion and public overclaim | State this as a view of Standard mode; preserve boundary notes |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| Existing Standard mode is the correct host | fact | Current `WORKFLOWS.md` and templates | A required control cannot fit without a new artifact | FlyFission |
| Mermaid sequence diagrams render on GitHub | fact | Existing repository practice | GitHub render or parser failure | FlyFission |
| Candidate identity can be a commit SHA or artifact hash | fact | Existing git/artifact release practice | Target system lacks a stable identity mechanism | FlyFission |
| Two correction rounds are enough for this PR before escalation | assumption | Bounded scope and docs/template-only changes | P0/P1 remains after two rounds | FlyFission |
| Public wording can remain tool-agnostic | assumption | Role abstraction | A real workflow requires provider-specific behavior | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The current README already has a four-role sequence diagram | fact | `README.md#who-does-what` on base `77f1645` | Amend rather than add a second diagram |
| The current ship record lacks an explicit reviewed-versus-current candidate identity section | fact | Base `templates/standard/ship.md` | Add exact-candidate closure fields |
| The current plan lacks a correction-round budget | fact | Base `templates/standard/plan.md` | Add bounded remediation fields |
| The proposed wording preserves simplicity | assumption | Visual and human review pending | Hold merge if reviewers find the diagram overloaded |
| Ben authorized commit, push, and PR creation | decision authority | Direct user instruction in this session | PR may be opened; merge remains held |

## Interfaces and trust boundaries

- Internal interfaces affected: README and canonical diagram mirror; Standard plan and ship template contract; public-doc test.
- External services/APIs affected: GitHub rendering and pull-request hosting only.
- Data classes affected: Public Markdown and Mermaid source.
- Human approval boundaries: Ben/FlyFission owns PR acceptance and merge.
- AI/model/tool authority boundaries: Hermes may edit, test, commit, push, and open the requested PR; models do not authorize merge or establish independence by identity alone.

## Dependency / model / supplier intended use

Not activated. No dependency, model runtime, API, or supplier behavior changes.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | WHEN the public role diagram describes AI-assisted PR work THE DOCUMENTATION SHALL use durable roles rather than model brands and retain human criteria and merge/apply authority. | Role authority must survive provider changes | Five-role Mermaid sequence and text fallback | Public-doc contract plus visual/source review |
| REQ-002 | WHEN a verifier records a verdict THE RECORD SHALL bind it to an exact candidate identity and mark it stale after a material candidate change. | Verdicts do not cover moving targets | Candidate ID handoff in diagram and `ship.md` | Contract test, diff review, packet trace |
| REQ-003 | WHEN correction is authorized THE PLAN SHALL name a maximum round count and human escalation without lowering acceptance criteria. | Bounded remediation avoids churn and premature fixed stops | Review candidate and correction budget section | Contract test and template review |
| REQ-004 | BEFORE merge or apply THE SHIP RECORD SHALL compare the reviewed candidate identity with the current candidate and require renewed review when they differ. | Exact-candidate closure prevents stale release decisions | Reviewed candidate identity section | Contract test and template review |
| REQ-005 | WHEN the role diagram changes THE README AND canonical diagrams source SHALL remain semantically mirrored and all project checks SHALL pass. | Public diagrams are controlled items | Mirrored Mermaid and text fallback; test suite | Pytest, Ruff, doctor, tokens, eval, command parity, diff check |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview: what changes and why | yes | `WORKFLOWS.md` minimum assurance view |
| Architecture: shape and major parts | yes | README and `docs/diagrams.md` five-role sequence |
| Components and interfaces: boundaries above | yes | Interfaces and trust boundaries |
| Data models: shapes, classes, ownership | not applicable | Markdown fields only |
| Error handling: failure paths and responses | yes | Stale verdict and correction-budget escalation paths |
| Testing strategy: how each claim is checked | yes | `verification.md` and `tests/test_public_docs.py` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: direct user instruction and this packet
- Source lineage, if cited: existing repository source map; no new external source claim

## Exit criteria

- Builder and reviewer can identify the protected simplicity, exact-candidate closure, and human authority.
- Requirements are bounded to existing Standard-mode surfaces.
- Every requirement has a planned deterministic or review check.
- No model brand, external diagram expression, or compliance claim is imported.

## Source-lineage note

This basis is an original operationalization of the existing Nuclear-grade method. The external diagram supplied a design prompt, not copied wording or assurance evidence. Existing public sources mapped in `docs/00-standards-foundation/source-map.md` and non-compliance boundaries remain controlling.
