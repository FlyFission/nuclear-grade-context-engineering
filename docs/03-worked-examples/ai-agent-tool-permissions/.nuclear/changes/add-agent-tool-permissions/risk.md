# Risk — Add Agent Tool Permissions

**Purpose:** Classify the worked-example change and name the minimum evidence needed before release.

**Change slug:** `add-agent-tool-permissions`
**Owner:** Nuclear-grade example maintainer
**Date:** 2026-05-17
**Lifecycle phase:** Prove
**Status:** Worked example v0; educational reference implementation only.

---

## Change identity

- **Slug:** `add-agent-tool-permissions`
- **PR / issue:** example packet, no PR yet
- **Owner:** Nuclear-grade example maintainer
- **Date:** 2026-05-17
- **Current lifecycle phase:** Prove
- **Summary:** Add a controlled tool-permission layer for an AI agent workflow service. The first proved claim, C-001, limits file writes to an approved workspace path and denies traversal, absolute-path, and symlink escape attempts.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Workspace write guard | Reference code | Enforces the first authority boundary for file writes. | `../../reference/workspace_guard.py` |
| Workspace guard tests | Test evidence | Proves allowed writes and denied escape attempts for C-001. | `../../tests/test_workspace_guard.py` |
| Permission claims | Design/evidence record | Prevents broad “safe agent” claims by limiting proof to named claims. | `trace.md` |
| Audit events | Operational evidence concept | Denied actions must be visible, not silent. | `verification.md` |
| Release decision | Release record | Makes “ship the example v0” conditional on evidence and gaps. | `ship.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | A file-write permission boundary can affect integrity, confidentiality, and trust if reused in production. |
| Reversibility | Medium | Documentation/example changes are reversible; real file writes may not be. |
| Detectability | Medium | Denials are logged in the reference guard, but production monitoring is only specified as a future extension. |
| Exposure | Low for this repo; medium in a real agent service | This is local educational code, but the pattern targets externally useful AI systems. |
| Uncertainty | Medium | C-001 is tested; C-002 through C-004 remain planned/gap. |
| Dependency trust | Low | The reference implementation uses Python standard library only. |
| AI authority | Medium | The modeled agent receives file-write authority under a workspace boundary. |

## Selected mode

- **Mode:** Standard
- **Why this mode:** The change alters an AI agent authority boundary and needs more than happy-path proof.
- **Why lighter mode is not enough:** Quick mode would hide traversal, absolute-path, symlink, auditability, and release-readiness concerns.
- **Why heavier mode is not yet required:** This is an educational reference example with no production deployment, sensitive data, external customers, regulated records, financial records, or irreversible infrastructure changes.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | Authority boundary needs protected/unacceptable outcomes and trust boundaries. | Maintainer |
| `plan.md` | yes | The example needs a bounded implementation and proof sequence. | Maintainer |
| `trace.md` | yes | C-001 must visibly connect claim → basis → control → evidence → ship decision. | Maintainer |
| `verification.md` | yes | C-001 requires unit/integration-style tests and negative checks. | Maintainer |
| `ship.md` | yes | The example v0 needs residual risk, rollback, and monitoring posture. | Maintainer |
| Nuclear subset record | no | Not activated for an educational Standard-mode packet. | Maintainer |

## Immediate proof obligations

- **Minimum evidence before build:** Define C-001, protected outcomes, unacceptable outcomes, workspace trust boundary, and denial behavior.
- **Minimum evidence before merge/release:** Passing tests for allowed relative write, parent traversal denial, absolute path denial, symlink escape denial, and audit event presence.
- **Independent review needed?** Yes, lightweight adversarial review before launch docs claim the example is coherent.

## Required links

- Packet: `.nuclear/changes/add-agent-tool-permissions/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `../../../../00-standards-foundation/source-map.md`, `../../../../01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- Mode is justified.
- Activated artifacts are explicit.
- Important risks, assumptions, and proof obligations are not hidden in chat or commit messages.
- C-001 has a complete evidence chain with test output.

## Source-lineage note

Original Nuclear-grade worked-example packet inspired by public graded quality, configuration management, lifecycle, software assurance, secure development, AI risk, and supply-chain sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
