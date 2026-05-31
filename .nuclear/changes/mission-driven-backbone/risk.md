# Risk

## Change identity

- Slug: mission-driven-backbone
- PR / issue: (TBD on push)
- Owner: maintainer
- Date: 2026-05-27
- Current lifecycle phase: Execute
- Summary: Add a mission-driven backbone to the repo: a durable charter of process-integrity principles, a per-change mission anchor, two new skills (`staying-on-mission`, `reviewing-code-quality`), two paired command prompts, an advisory drift gate in the Standard templates, and minimal only-when-present validator checks.

## Mission anchor

State what this change is for, so a long session can be tested against it. See `staying-on-mission`.

- Objective: Give the repo a backbone that resists engineering drift, both intent drift (scope creep, goal substitution) and standards drift (normalization of deviance).
- Success criteria: The charter and mission anchor exist and are reachable; the two skills and two commands pass the contract checks; the validator advisory-checks a mission anchor only when present; the full test suite, ruff, doctor, and this packet's validation all pass.
- Non-goals / forbidden directions: Out of scope is rewriting the 90-180 char description rule or any other skill-contract change; out of scope is making the anchor or charter a hard required gate; out of scope is the evidence-coverage validator rule.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: workspace `.nuclear/charter.md` and the originating design discussion.

## Questioning-attitude summary

- Decision question: How do we make agents mission-driven and resistant to drift without adding heavyweight, mandatory process?
- Assumptions that changed the mode: The feature spans skills, commands, templates, validator, and docs, and adds advisory enforcement; that breadth justifies Standard.
- Facts still needing validation: That the advisory mission-anchor check does not false-trigger on existing packets (confirmed: only-when-present) and that the two new skills pass the live doctor contract.
- Stop or hold conditions: Stop if the advisory checks would break existing packets, or if the scope starts absorbing the deferred contract-evolution items.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `skills/staying-on-mission/SKILL.md` | Skill | New intent-drift skill | `../../../skills/staying-on-mission/SKILL.md` |
| `skills/reviewing-code-quality/SKILL.md` | Skill | New standards-drift skill | `../../../skills/reviewing-code-quality/SKILL.md` |
| `commands/ng-drift-check.md`, `commands/ng-code-review.md` | Commands | Portable prompts for the two skills | `../../../commands/ng-drift-check.md` |
| `nuclear_grade/ng_validate.py` | Code | Advisory mission-anchor and clarification-marker checks | `../../../nuclear_grade/ng_validate.py` |
| `nuclear_grade/cli.py` | Code | `init` writes charter and mission anchor | `../../../nuclear_grade/cli.py` |
| `templates/standard/risk.md`, `templates/standard/plan.md` | Templates | Mission anchor section and drift gate | `../../../templates/standard/risk.md` |
| `.nuclear/charter.md` | Charter | The durable backbone | `../../charter.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Adds public skills, commands, and an advisory validator rule. |
| Reversibility | high | Each piece is additive and revertible. |
| Detectability | high | Doctor, contract tests, and the validator catch regressions. |
| Exposure | medium | Public repo; new skills are visible surface. |
| Uncertainty | low | Only-when-present checks are well understood. |
| Dependency trust | low | No new runtime dependencies. |
| AI authority | low | No new agent write permissions. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine/repetitive action where inattention is plausible | no | n/a |
| Known procedure where workflow adherence matters | yes | packet path and the plan build sequence |
| Novel or uncertain work where assumptions may be wrong | yes | questioning attitude in this risk; advisory-only enforcement |
| Interrupted, resumed, or handed-off work | no | n/a |
| High-consequence critical action | no | n/a |

## Selected mode

- **Mode:** Standard
- **Why this mode:** A multi-surface feature (skills, commands, templates, validator, docs) with new public surface and an advisory rule.
- **Why lighter mode is not enough:** Quick cannot record the claim-to-evidence mapping across the surfaces.
- **Why heavier mode is not yet required:** No regulated use, no safety basis, no controlled-supplier dedication.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline above. | maintainer |
| `basis.md` | yes | Claim-to-evidence mapping. | maintainer |
| `verification.md` | yes | Per-claim evidence status. | maintainer |
| `ship.md` | yes | Release decision. | maintainer |
| `turnover.md` | no | Single-author packet. | maintainer |
| `self-check.md` | no | No high-consequence critical action. | maintainer |
| `supplier-trust.md` | no | No new external supplier. | maintainer |
| Nuclear subset record | no | Not warranted. | maintainer |

## Immediate evidence obligations

- Minimum evidence before build: Confirm the only-when-present pattern leaves existing packets green.
- Minimum evidence before merge/release: pytest green; ruff clean; doctor OK; this packet validates; both new skills and commands pass the live contract.
- Independent review needed? no for this PR.

## Required links

- Packet: `.nuclear/changes/mission-driven-backbone/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Charter: `../../charter.md`
- Source map: [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md)

## Exit criteria

- Mode is justified as Standard.
- The mission anchor names objective, success criteria, and non-goals.
- Claims map to evidence in `verification.md`.
- No hidden trigger for a stronger mode.

## Source-lineage note

Original Nuclear-grade packet influenced by nuclear-industry mission ownership and rising-standards culture and by the human-performance practices mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
