# Standard Risk Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Sort a real change by risk after questioning the assumptions, justify Standard mode, and name any extra records you turn on.

**Activation threshold:** Use for behavior users can see, lasting design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational stance, or anything where the stakes, the uncertainty, or the review value are more than trivial.

**Minimum useful version:** the scope, the affected controlled items, the threshold ratings, the chosen mode, the artifacts you turn on, and the evidence due right away.

**Overhead trap:** Do not score risk with fake precision. Use the screen to surface the stakes and the evidence you need.

---

## Change identity

- Slug:
- PR / issue:
- Owner:
- Date:
- Current lifecycle phase: Question / Specify / Plan / Execute / Verify / Review / Decide / Baseline / Operate / Learn
- Current work phase: explore / candidate / audit / accept
- Summary:

## Mission anchor

State what this change is for, so a long session can be checked against it. See `staying-on-mission`.

- Objective:
- Success criteria:
- Non-goals / forbidden directions:
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: workspace `.nuclear/mission.md`, charter article, or originating PR/issue.

## Questioning-attitude summary

- Decision question:
- Evidence that would change the decision:
- Assumptions that changed the mode:
- Facts still needing validation:
- Stop or hold conditions:

## Affected configuration items

List the affected code, docs, infrastructure, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

| Item | Type | Why it matters | Link |
|---|---|---|---|
| | | | |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | | |
| Reversibility | | |
| Detectability | | |
| Exposure | | |
| Uncertainty | | |
| Dependency trust | | |
| AI authority | | |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | yes/no | self-check / proof |
| Known procedure where following the steps matters | yes/no | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | yes/no | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | yes/no | turnover / context pack |
| A high-stakes critical action | yes/no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard / Nuclear subset / Incident / Research Board / Release
- Why this mode:
- Why lighter mode is not enough:
- Why heavier mode is not yet required:

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | yes/no | | |
| `basis.md` | yes/no | | |
| `verification.md` | yes/no | | |
| `ship.md` | yes/no | | |
| `turnover.md` | yes/no | | |
| `self-check.md` | yes/no | | |
| `supplier-trust.md` | yes/no | | |
| Nuclear subset record | yes/no | | |

## Immediate evidence obligations

- Minimum evidence before build:
- Minimum evidence before merge/release:
- Independent review needed? yes/no; why:

## Required links

- Packet: `.nuclear/changes/<slug>/`
- `questioning-attitude.md` if activated
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked:

## Exit criteria

- The mode is justified.
- The artifacts you turned on are named.
- Important risks, assumptions, and evidence due are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
