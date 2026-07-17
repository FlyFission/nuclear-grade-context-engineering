# Risk

**Purpose:** Sort this change by risk, justify Standard mode, and name the records turned on.

## Change identity

- Slug: trust-propagation-two-party
- PR / issue: this PR (branch `trust-propagation-two-party`)
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17
- Current lifecycle phase: Verify
- Current work phase: candidate
- Summary: Add two standalone, stdlib-only validator modules, `nuclear_grade/propagation.py` (evidence-trust propagation) and `nuclear_grade/two_party.py` (two-party integrity), with unit tests. The modules are NOT wired into `validate_packet`; wiring is a separate, planned decision. The change ports two Palantir Foundry trust mechanisms (marking propagation, purpose-based access) into the packet model.

## Mission anchor

- Objective: Give nuclear-grade computed trust gates so "a baseline is only as trusted as its weakest evidence" and "the drafter is not the sole author of a load-bearing claim" become machine-checked properties rather than norms reviewers uphold.
- Success criteria: Both modules exist with passing unit tests, lint clean, and a change packet that records the design, the two findings, and the integration path; existing validator behavior is unchanged because nothing is wired in yet.
- Non-goals / forbidden directions: Do not change `validate_packet` behavior in this packet; do not weaken any existing check; do not assert any external-standard conformance.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: originating design work in the Palantir-ontology teaching workspace and this PR.

## Questioning-attitude summary

- Decision question: Should nuclear-grade adopt computed propagation and two-party gates, and is landing them as inert modules plus a documented plan the right first step?
- Evidence that would change the decision: If the claim-to-evidence table schema cannot be normalized, propagation cannot compute reliably and the gate should stay advisory.
- Assumptions that changed the mode: The modules touch the validator package (a controlled item) and shape future merge gates, so Standard applies even though nothing is wired in yet.
- Facts still needing validation: Maintainer decision on gate severity (advisory versus blocking) and on the `Claim authorship` schema addition.
- Stop or hold conditions: Hold wiring into `validate_packet` until table normalization lands and severity is chosen.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `nuclear_grade/propagation.py` | code (new) | New trust-computation module | `../../../nuclear_grade/propagation.py` |
| `nuclear_grade/two_party.py` | code (new) | New independence-check module | `../../../nuclear_grade/two_party.py` |
| `tests/test_propagation.py` | test (new) | Proves propagation behavior | `../../../tests/test_propagation.py` |
| `tests/test_two_party.py` | test (new) | Proves two-party behavior | `../../../tests/test_two_party.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Shapes future merge gates for every packet, but inert today. |
| Reversibility | high | New files, not wired in; revert is a file deletion. |
| Detectability | high | Behavior is unit-tested and observable via the modules directly. |
| Exposure | low | No user data, no runtime dependency, no network. |
| Uncertainty | medium | Table-schema variance and gate severity are open. |
| Dependency trust | high | Stdlib only; zero new dependencies. |
| AI authority | medium | AI drafted the code and evidence; maintainer is the independent decider. |
| Controllability (human gate can catch/reverse in time?) | high | Merge review plus CI catch regressions before landing. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check |
| Known procedure where following the steps matters | yes | packet path |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude and review |
| Work that was interrupted, resumed, or handed off | yes | this packet is the turnover for pickup elsewhere |
| A high-stakes critical action | no | independent maintainer review at merge |

## Selected mode

- **Mode:** Standard
- Why this mode: The change adds to the validator package and defines future merge-gate behavior, which is a lasting design decision.
- Why lighter mode is not enough: A Quick packet would not capture the basis, trace, and verification a reviewer needs to judge the gate design.
- Why heavier mode is not yet required: Nothing is wired into `validate_packet`, there is no runtime or data exposure, and the change is fully reversible.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record | Ben Huffer |
| `basis.md` | yes | States what must stay true | Ben Huffer |
| `verification.md` | yes | Carries the evidence | Ben Huffer |
| `ship.md` | yes | Records the release stance | Ben Huffer |
| `turnover.md` | no | Handoff captured in the ship.md handoff section | Ben Huffer |
| `self-check.md` | no | Self-check folded into verification.md | Ben Huffer |
| `supplier-trust.md` | no | No new dependencies | Ben Huffer |
| Nuclear subset record | no | Not a nuclear-subset change | Ben Huffer |

## Immediate evidence obligations

- Minimum evidence before build: A claim table mapping each module to a unit-tested behavior.
- Minimum evidence before merge/release: Unit tests green, ruff clean, existing suite unaffected, doctor and packet validation green.
- Independent review needed? yes; why: AI authored the code and evidence, so a maintainer must independently confirm before merge.

## Required links

- Packet: `.nuclear/changes/trust-propagation-two-party/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified.
- The activated artifacts are named.
- Risks, assumptions, and evidence due are recorded here, not hidden in chat.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
