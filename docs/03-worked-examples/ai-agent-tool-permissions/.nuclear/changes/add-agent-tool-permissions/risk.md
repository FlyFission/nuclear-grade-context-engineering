# Risk — Add Agent Tool Permissions

**Purpose:** Sort this worked-example change by risk, and name the least evidence needed before release.

**Change slug:** `add-agent-tool-permissions`
**Owner:** Nuclear-grade example maintainer
**Date:** 2026-05-17
**Lifecycle phase:** Prove
**Status:** Worked example v0. Teaching sample code only.

---

## Change identity

- **Slug:** `add-agent-tool-permissions`
- **PR / issue:** example packet, no PR yet
- **Owner:** Nuclear-grade example maintainer
- **Date:** 2026-05-17
- **Current lifecycle phase:** Prove
- **Summary:** Add a controlled set of tool permissions for an AI agent service. The first proven claim, C-001, keeps file writes inside an approved workspace path. It blocks attempts to escape with `../` paths, absolute paths, and symlinks.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Workspace write guard | Reference code | Sets the first limit on what file writes the agent may do. | `../../reference/workspace_guard.py` |
| Workspace guard tests | Test evidence | Proves allowed writes work and escape attempts fail, for C-001. | `../../tests/test_workspace_guard.py` |
| Permission claims | Design/evidence record | Stops broad "safe agent" claims by tying proof to named claims only. | `trace.md` |
| Audit events | Operational evidence concept | Denied actions must be visible, not silent. | `verification.md` |
| Release decision | Release record | Makes "ship the example v0" depend on the evidence and the gaps. | `ship.md` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | A file-write limit can affect data, privacy, and trust if it is reused in production. |
| Reversibility | Medium | Doc and example changes can be undone. Real file writes may not be. |
| Detectability | Medium | The sample guard logs denials, but production monitoring is only named as future work. |
| Exposure | Low for this repo; medium in a real agent service | This is local teaching code, but the pattern aims at AI systems used in the real world. |
| Uncertainty | Medium | C-001 is tested. C-002 through C-004 are still planned or open gaps. |
| Dependency trust | Low | The sample code uses only the Python standard library. |
| AI authority | Medium | The example agent is given the power to write files, kept inside a workspace boundary. |

## Selected mode

- **Mode:** Standard
- **Why this mode:** The change alters what an AI agent is allowed to do, and it needs more than an easy "it works" test.
- **Why lighter mode is not enough:** Quick mode would hide the `../` path, absolute-path, symlink, audit-trail, and release-readiness concerns.
- **Why heavier mode is not yet required:** This is a teaching example. It has no production deployment, no sensitive data, no outside customers, no regulated records, no financial records, and no infrastructure changes you cannot undo.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | A change to agent power needs protected outcomes, outcomes to prevent, and lines of trust. | Maintainer |
| `plan.md` | yes | The example needs a bounded build and a clear order of proof. | Maintainer |
| `trace.md` | yes | C-001 must clearly link claim → basis → control → evidence → ship decision. | Maintainer |
| `verification.md` | yes | C-001 needs unit and integration-style tests, plus checks that bad actions fail. | Maintainer |
| `ship.md` | yes | The example v0 needs leftover risk, a rollback plan, and a monitoring stance. | Maintainer |
| Nuclear subset record | no | Not turned on for a teaching Standard-mode packet. | Maintainer |

## Immediate proof obligations

- **Least evidence before build:** Define C-001, the protected outcomes, the outcomes to prevent, the workspace line of trust, and how denials behave.
- **Least evidence before merge/release:** Passing tests for an allowed relative write, a denied parent `../` path, a denied absolute path, a denied symlink escape, and a recorded audit event.
- **Independent review needed?** Yes. A light second-eyes attack review before the launch docs say the example holds together.

## Required links

- Packet: `.nuclear/changes/add-agent-tool-permissions/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `../../../../00-standards-foundation/source-map.md`, `../../../../01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- The mode is justified.
- The activated artifacts are named.
- Important risks, assumptions, and proof duties are not hidden in chat or commit messages.
- C-001 has a complete evidence chain with test output.

## Source-lineage note

Original Nuclear-grade worked-example packet inspired by public sources for graded quality, keeping the approved version under control (CM), software lifecycle, software assurance, secure development, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
