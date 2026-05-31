# Risk

## Change identity

- Slug: skill-contract-modernization
- PR / issue: (TBD on push)
- Owner: maintainer
- Date: 2026-05-28
- Current lifecycle phase: Execute
- Summary: Modernize the skill-authoring contract for higher triggering accuracy. Drop the mandatory `Use when` prefix and the 90-180 character cap; require descriptions that state what the skill does, when to trigger, and a negative clause, within 80-500 characters and YAML-safe. Rewrite all 18 skill descriptions. Allow optional `license`/`compatibility` frontmatter, add a name-format rule, document progressive disclosure, and sync the version to 0.3.0.

## Mission anchor

State what this change is for, so a long session can be tested against it. See `staying-on-mission`.

- Objective: Make skill descriptions trigger reliably, aligned with Anthropic skill-authoring guidance, without breaking existing skills or downstream authors.
- Success criteria: All 18 descriptions rewritten to what-plus-when-plus-negative form, 80-500 chars, colon-free; the contract test enforces the new rule; name-format and optional-license fields supported; progressive disclosure documented; version synced to 0.3.0; tests, ruff, doctor, and this packet all green.
- Non-goals / forbidden directions: Out of scope is the evidence-coverage validator rule, making the charter or anchor a hard gate, the cross-cutting hedge-word red-flag sweep, CM delta vocabulary, and adding description enforcement to the CLI doctor (which would false-fail stub fixtures). Forbidden is renaming any skill (a 32-char cap would force that).
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the deferred-backlog discussion and `.nuclear/charter.md` (rising standards, evidence over persuasion).

## Questioning-attitude summary

- Decision question: Is the old 90-180 char `Use when` rule actually wrong, and how do we fix it without breaking existing skills?
- Assumptions that changed the mode: Anthropic guidance says descriptions should be longer and richer (what + when + do-not). The change touches the contract enforced across all 18 skills, so it is a Standard change.
- Facts still needing validation: That the relaxation breaks no downstream authors (confirmed: it loosens our own test; it does not constrain external skills) and that all rewrites stay YAML-safe (confirmed: colon-free, plain scalars).
- Stop or hold conditions: Stop if a name-length cap or a CLI-doctor enforcement change would force skill renames or break stub fixtures; both were ruled out.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/*/SKILL.md` (18) | Skills | Description frontmatter rewritten | `../../../skills` |
| `tests/test_skill_contracts.py` | Test | The contract source of truth | `../../../tests/test_skill_contracts.py` |
| `docs/05-reference/skill-authoring-contract.md` | Docs | The published contract | `../../../docs/05-reference/skill-authoring-contract.md` |
| `SKILLS.md` | Docs | Contract summary | `../../../SKILLS.md` |
| `pyproject.toml`, `nuclear-grade.yaml`, `CITATION.cff` | Config | Version sync to 0.3.0 | `../../../pyproject.toml` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Changes a public authoring contract and all skill descriptions. |
| Reversibility | high | Revert the branch; descriptions and test revert cleanly. |
| Detectability | high | Contract test and doctor catch regressions. |
| Exposure | medium | Public repo; skill descriptions are agent-facing surface. |
| Uncertainty | low | Relaxation is well understood and non-breaking. |
| Dependency trust | low | No new dependencies. |
| AI authority | low | No new agent write permissions. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine/repetitive action where inattention is plausible | yes | 18 near-identical edits; a script applied them uniformly and verified length and colon-safety |
| Known procedure where workflow adherence matters | yes | packet path and the plan build sequence |
| Novel or uncertain work where assumptions may be wrong | no | the rule change is well understood |
| Interrupted, resumed, or handed-off work | no | n/a |
| High-consequence critical action | no | n/a |

## Selected mode

- **Mode:** Standard
- **Why this mode:** Changes a public authoring contract enforced across all skills, with a version bump.
- **Why lighter mode is not enough:** Quick cannot record the claim-to-evidence mapping for an interface change.
- **Why heavier mode is not yet required:** Non-breaking; no regulated use, safety basis, or controlled-supplier dedication.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline above. | maintainer |
| `basis.md` | yes | Claim-to-evidence mapping. | maintainer |
| `verification.md` | yes | Per-claim evidence status. | maintainer |
| `ship.md` | yes | Release decision for 0.3.0. | maintainer |
| `turnover.md` | no | Single-author packet. | maintainer |
| `self-check.md` | no | No high-consequence critical action. | maintainer |
| `supplier-trust.md` | no | No new external supplier. | maintainer |
| Nuclear subset record | no | Not warranted. | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: Confirm the relaxation loosens, not tightens, the contract (non-breaking for downstream).
- Minimum evidence before merge/release: pytest green; ruff clean; doctor OK; this packet validates; all 18 descriptions within band and colon-free.
- Independent review needed? no for this PR.

## Required links

- Packet: `.nuclear/changes/skill-contract-modernization/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Mode is justified as Standard.
- The mission anchor names objective, success criteria, and non-goals.
- Claims map to evidence in `verification.md`.
- No hidden trigger for a stronger mode.

## Source-lineage note

Original Nuclear-grade packet influenced by public skill-authoring practice and the human-performance and configuration-management concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
