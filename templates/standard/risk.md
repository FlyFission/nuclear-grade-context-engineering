# Standard Risk Template

**Purpose:** Classify a meaningful change after questioning assumptions, justify Standard mode, and name any extra activated records.

**Activation threshold:** Use for user-visible behavior, durable design decisions, important dependency/model/API/prompt/tool changes, security/privacy/data handling, operational posture, or anything with non-trivial consequence, uncertainty, or review value.

**Minimum useful version:** Scope, affected configuration items, threshold dimensions, selected mode, activated artifacts, and immediate proof obligations.

**Overhead trap:** Do not score risk with fake precision. Use the screen to reveal consequences and evidence needs.

---

## Change identity

- Slug:
- PR / issue:
- Owner:
- Date:
- Current lifecycle phase: Question / Specify / Plan / Execute / Verify / Review / Decide / Baseline / Operate / Learn
- Summary:

## Questioning-attitude summary

- Decision question:
- Assumptions that changed the mode:
- Facts still needing validation:
- Stop or hold conditions:

## Affected configuration items

List affected code, docs, infra, dependencies, prompts, models, data, evals, releases, dashboards, or runbooks.

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
| Nuclear subset record | yes/no | | |

## Immediate proof obligations

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

- Mode is justified.
- Activated artifacts are explicit.
- Important risks, assumptions, and proof obligations are not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade template inspired by public graded quality, configuration management, lifecycle, software assurance, secure development, AI risk, and supply-chain sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
