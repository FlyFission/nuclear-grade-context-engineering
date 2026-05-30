# Risk

## Change identity

- Slug: efficacy-eval-harness
- PR / issue: repo-review enhancements (Track A)
- Owner: maintainer
- Date: 2026-05-30
- Current lifecycle phase: Execute
- Summary: Add a reproducible efficacy harness (`python tools/ng.py eval`) that mechanically checks each worked-example artifact still surfaces the decision signals the methodology claims it teaches. Adds `nuclear_grade/efficacy.py`, three JSON eval cases under `evals/cases/`, an `eval` CLI subcommand, a bounded `efficacy-harness.md` doc, and tests.

## Mission anchor

State what this change is for, so a long session can be tested against it. See `staying-on-mission`.

- Objective: Convert one part of the existing qualitative efficacy comparison into a runnable, falsifiable check, without overclaiming that it proves engineering quality, safety, or compliance.
- Success criteria: `ng eval .` scores the three real trial-record artifacts, exits non-zero if a worked example drops a required signal, ships with a boundary doc that states what it does and does not measure, and is covered by tests including a teeth test that proves it can fail.
- Non-goals / forbidden directions: Out of scope is mechanizing the simple-prompt-versus-Nuclear-grade score table (unreliable via substring on author-written meta-sections), scoring a live model, adding any runtime dependency, and expanding to all 20 trials at shallow depth. Forbidden is wording that presents signal presence as proof of correctness, safety, or assurance.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: review finding that all efficacy evidence was author-judged with nothing runnable, and `.nuclear/charter.md` (evidence over persuasion, rising standards).

## Questioning-attitude summary

- Decision question: What can be measured mechanically and honestly about these artifacts without dressing author judgment up as measurement?
- Assumptions that changed the mode: A harness that emits an efficacy score is a public trust-bearing artifact; by the repo's own U04 logic, public assurance wording is a Standard trigger even when the code is small.
- Facts still needing validation: That the harness can genuinely fail (validated by a teeth test that strips a section and asserts the case fails), and that it stays zero-runtime-dependency (validated by a clean-venv wheel install).
- Stop or hold conditions: Stop if the only way to show a comparison "win" is to grep author-written gap prose, which would inflate the result; that path was rejected and the comparison stays qualitative.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/efficacy.py` | Code | The harness logic | `../../../nuclear_grade/efficacy.py` |
| `evals/cases/*.json` | Data | The three eval cases and their signals | `../../../evals/cases` |
| `nuclear_grade/cli.py` | Code | The `eval` subcommand | `../../../nuclear_grade/cli.py` |
| `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md` | Docs | The bounded public explanation | `../../../docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md` |
| `tests/test_efficacy.py` | Test | Behavior and teeth coverage | `../../../tests/test_efficacy.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Publishes an efficacy/reproducibility claim that a hostile reader could test. |
| Reversibility | high | Revert the branch; no migration. |
| Detectability | high | Tests and CI catch regressions; the harness reports its own coverage. |
| Exposure | medium | Public repo; a credibility-bearing artifact. |
| Uncertainty | low | Pure-stdlib presence checks over real files. |
| Dependency trust | low | No new runtime dependency. |
| AI authority | low | No new agent write permissions. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine/repetitive action where inattention is plausible | no | Bespoke signals authored per scenario |
| Known procedure where workflow adherence matters | yes | Packet path and the plan build sequence |
| Novel or uncertain work where assumptions may be wrong | yes | The overclaiming risk is controlled by a bounded doc and a teeth test |
| Interrupted, resumed, or handed-off work | no | Single session |
| High-consequence critical action | no | Read-only scoring tool |

## Selected mode

- **Mode:** Standard
- **Why this mode:** It publishes a trust-bearing efficacy claim; public assurance wording is a Standard trigger by the repo's own comparison findings.
- **Why lighter mode is not enough:** Quick cannot record the claim-to-evidence mapping or the boundary reasoning that keeps the claim honest.
- **Why heavier mode is not yet required:** No regulated use, safety basis, irreversible data, or external supplier; the change is reversible and well tested.

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

- Minimum evidence before build: Confirm the harness can fail, not only pass, before trusting a green run.
- Minimum evidence before merge/release: pytest green; ruff clean; doctor OK; this packet validates; clean-venv wheel install keeps the package dependency-free; `ng eval .` reports full coverage.
- Independent review needed? no for this PR; the boundary wording invites hostile review.

## Required links

- Packet: `.nuclear/changes/efficacy-eval-harness/`
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

Original Nuclear-grade packet influenced by public software verification and configuration-management concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
