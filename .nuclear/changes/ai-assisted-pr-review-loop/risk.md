# AI-Assisted PR Review Loop: Risk

## Change identity

- Slug: ai-assisted-pr-review-loop
- PR / issue: user-authorized follow-up from an external AI-assisted PR workflow diagram
- Owner: FlyFission
- Date: 2026-07-24
- Current lifecycle phase: Review
- Current work phase: audit
- Summary: Tighten the existing role diagram and Standard templates around approved criteria, exact-candidate verdict identity, bounded correction rounds, and human merge/apply authority.

## Mission anchor

- Objective: Incorporate the diagram's useful simplicity and exact-artifact recheck into the existing Nuclear-grade workflow without creating a competing mode or model-branded process.
- Success criteria: The public role diagram stays readable; the plan records role/correction boundaries; the ship record proves the current candidate is the reviewed candidate; tests guard the contract.
- Non-goals / forbidden directions: No new workflow mode, model-vendor authority, validator enforcement claim, compliance claim, or claim that provider diversity alone establishes independence.
- Drift check: Stop if the change grows into a new skill, command, validator mode, or unrelated doctrine rewrite.
- Traces to: README `Who does what`, `WORKFLOWS.md`, `docs/diagrams.md`, and Standard packet templates.

## Questioning-attitude summary

- Decision question: Can the external diagram's useful control ideas be operationalized as a small refinement to existing surfaces rather than another framework layer?
- Evidence that would change the decision: Existing current-main controls already express the same requirements clearly and operationally, making the change redundant.
- Assumptions that changed the mode: Public workflow diagrams and Standard templates are controlled adoption surfaces; a stale-verdict omission can affect release decisions.
- Facts still needing validation: Mermaid readability, mirrored diagram consistency, template usability, full-suite compatibility, and reviewer assessment of scope.
- Stop or hold conditions: Hold if tests, lint, doctor, token budget, packet validation, or exact-candidate review fail.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `README.md` | public doctrine | Entry-point role diagram and explanation | `README.md#who-does-what` |
| `WORKFLOWS.md` | workflow doctrine | Compact AI-assisted PR interpretation | `WORKFLOWS.md` |
| `docs/diagrams.md` | canonical diagram source | Must mirror the README diagram | `docs/diagrams.md` |
| `templates/standard/plan.md` | operational template | Holds role and correction-round boundaries | `templates/standard/plan.md` |
| `templates/standard/ship.md` | release template | Holds reviewed/current candidate identity and stale-verdict disposition | `templates/standard/ship.md` |
| `tests/test_public_docs.py` | deterministic contract | Prevents the closure controls from drifting out | `tests/test_public_docs.py` |
| `CHANGELOG.md` | public change history | Names the operational change without overclaiming | `CHANGELOG.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes public workflow and release-template expectations |
| Reversibility | high | Documentation, templates, tests, and packet revert through git |
| Detectability | medium | Semantic drift can look plausible unless contract-tested and reviewed |
| Exposure | high | Public repo and copyable templates |
| Uncertainty | medium | The main uncertainty is whether the added detail preserves simplicity |
| Dependency trust | low | No dependency or runtime changes |
| AI authority | medium | AI agent authors the candidate; human owns the PR and merge decision |
| Controllability (human gate can catch/reverse in time?) | high | Isolated branch, PR review, and normal git rollback |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | focused diff and contract test |
| Known procedure where following the steps matters | yes | Standard packet and PR release gate |
| New or uncertain work where the assumptions may be wrong | yes | external-artifact critique plus independent review |
| Work that was interrupted, resumed, or handed off | no | packet preserves current state |
| A high-stakes critical action | no | push/PR authorized; merge remains human-owned |

## Selected mode

- Mode: Standard
- Why this mode: Public doctrine and Standard release templates change together and need traceable acceptance evidence.
- Why lighter mode is not enough: A Quick packet would not preserve the role, candidate-identity, correction-budget, and release-template chain.
- Why heavier mode is not yet required: No executable product behavior, production system, credential, dependency, or regulated-use claim changes.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | The summary above is sufficient for this bounded change | FlyFission |
| `basis.md` | yes | Requirements and non-goals need a stable basis | FlyFission |
| `verification.md` | yes | Public and template contracts need evidence | FlyFission |
| `ship.md` | yes | PR and exact-candidate decision need an explicit hold/ship state | FlyFission |
| `turnover.md` | no | One continuous workstream | FlyFission |
| `self-check.md` | no | No destructive or production action | FlyFission |
| `supplier-trust.md` | no | No supplier or dependency change | FlyFission |
| Nuclear subset record | no | This is a public software-method documentation change, not regulated nuclear work | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: Current-main README, workflow, diagrams, templates, and overlapping open PRs inspected; redundancy avoided.
- Minimum evidence before merge/release: Focused contract test, full pytest, Ruff, doctor, token budget, eval, generated-command parity, strict-custody packet validation, diff check, exact-candidate review, and GitHub checks.
- Candidate load-bearing / decisive claim IDs: REQ-001, REQ-002, REQ-003, REQ-004, REQ-005.
- Minimum actor/context/mechanism/authority/resource profile for those claims: Mechanical presence checks may be coupled if reproducible; semantic adequacy requires a reviewer outside the builder's opening analysis; human retains merge authority.
- Prohibited coupling paths: Builder may not grade semantic adequacy as independent, relax criteria inside remediation, or treat provider diversity as authority.
- Who owns evidence admissibility and residual-risk disposition: FlyFission.
- Independent reproduction, diverse verification, or direct witnessing needed? yes; an opening reviewer should inspect the frozen candidate and the human owner decides the PR.

## Required links

- Packet: `.nuclear/changes/ai-assisted-pr-review-loop/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: existing source-lineage notes only; no new source claim.

## Exit criteria

- Standard mode remains proportionate.
- The affected public and operational surfaces are explicit.
- Exact-candidate closure and correction-budget claims have reproducible evidence.
- No new compliance, formal V&V, or model-brand authority claim is introduced.

## Source-lineage note

This change is an original refinement of the existing Nuclear-grade workflow, prompted by an external diagram and grounded in the repository's existing public configuration-management, software-assurance, role-separation, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
