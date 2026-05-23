# Basis — Add Agent Tool Permissions

**Purpose:** State what must remain true for the example permission boundary to be safe, reliable, useful, and reviewable.

**Change slug:** `add-agent-tool-permissions`
**Related risk record:** `risk.md`
**Owner:** Nuclear-grade example maintainer
**Date:** 2026-05-17

---

## Change context

- **Slug:** `add-agent-tool-permissions`
- **Related risk record:** `risk.md`
- **Owner:** Nuclear-grade example maintainer
- **Date:** 2026-05-17
- **Decision this basis supports:** Whether the Standard-mode worked example can demonstrate one complete, honest claim-to-evidence chain for AI agent file-write authority.

## Mission / need

AI agents increasingly receive tool authority: file writes, API calls, shell commands, database changes, and workflow approvals. Nuclear-grade needs a compact worked example that shows how to convert one authority-changing feature into explicit basis, controls, verification, and release readiness without pretending to solve every security problem.

The v0 mission is deliberately narrow: prove that an agent file-write helper writes only inside an approved workspace and makes denied writes visible.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| File writes remain inside the configured workspace root. | Prevents destructive or unauthorized writes outside approved scope. | Tests for allowed relative write and denied traversal/absolute/symlink escape. |
| Denied writes leave an inspectable audit event. | Silent denials hide bypass attempts and make operations weaker. | Test assertions against `audit_events` for denied writes. |
| The example does not imply broad sandbox/security guarantees. | Avoids teaching false confidence. | README, verification, and ship records explicitly scope proof to C-001. |
| Remaining claims are labeled as planned/gap/deferred. | Prevents fictional matrices from looking complete. | `trace.md`, `verification.md`, and `ship.md` status labels. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A `../` path writes outside the workspace. | Agent can corrupt or disclose files outside intended scope. | Canonical resolution plus workspace containment check; traversal test. |
| An absolute path writes outside the workspace. | Caller bypasses relative-path policy. | Absolute paths resolved and denied when outside root; absolute-path test. |
| A symlink inside the workspace redirects writes outside the workspace. | Workspace allowlist is bypassed through filesystem indirection. | Resolve final path and deny outside root; symlink escape test. |
| A denied write disappears without evidence. | Operators cannot detect misuse, prompts gone wrong, or attempted bypasses. | Append structured `write_denied` audit event; test assertions. |
| The example is treated as a production sandbox. | Users may overtrust a teaching artifact. | Source-lineage and ship notes state educational scope and gaps. |

## Assumptions and constraints

| Assumption / constraint | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|
| The workspace root is the only approved write target for C-001. | Worked-example mission and `risk.md`. | Need to write shared caches, temp dirs, credentials, or production paths. | Maintainer |
| Standard library path resolution is sufficient for this educational example. | Minimal reference implementation; no external dependency. | Porting to non-POSIX semantics, remote FS, containers, ACL-heavy environments, or production sandboxing. | Maintainer |
| Audit events can be in-memory for v0 evidence. | Example scope; no production runtime. | Persistent service, multi-process workers, incident review, or external operations. | Maintainer |
| No formal compliance/certification claim is made. | Repo boundary docs and disclaimer. | Any public claim that this satisfies a regulator, standard, QA program, or certification. | Maintainer |

## Interfaces and trust boundaries

- **Internal interfaces affected:** `WorkspaceGuard.write_text(requested_path, content)` reference API.
- **External services/APIs affected:** None for C-001.
- **Data classes affected:** Example text file content only; no sensitive data in v0.
- **Human approval boundaries:** Not implemented for C-001; high-impact writes would activate C-003 in a later packet.
- **AI/model/tool authority boundaries:** Agent/tool caller may request file writes; guard enforces workspace containment before filesystem mutation.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| Python `pathlib` | Canonical path composition/resolution in teaching implementation. | Incorrect path handling could weaken C-001. | Negative tests for traversal, absolute path, symlink escape. | Python/platform path semantics change, production hardening, Windows-specific release. |
| `pytest` | Execute example evidence tests. | Test evidence unavailable or misleading. | Test command and output captured in `verification.md`. | Test framework/runtime changes. |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| C-001 | Agent writes only under the configured workspace root. | Protect filesystem integrity and scope AI tool authority. | Resolve requested path, require it to remain under workspace root, deny otherwise, log denial. | `pytest` tests: allowed write, traversal denial, absolute denial, symlink denial. |
| C-004a | Denied C-001 writes emit visible audit events. | Denied actions are operational signals. | In-memory structured audit event with event, requested path, resolved path, root, and reason. | Test assertions on `audit_events`. |
| C-002 | External API calls require approved tool IDs and scoped credentials. | Prevent arbitrary network side effects and credential misuse. | Future tool registry and credential binding. | Deferred/gap for v0. |
| C-003 | Human approval is required for high-impact actions. | Escalate consequence-changing authority to human review. | Future approval policy and approval record. | Deferred/gap for v0. |

## Required links

- Risk record: `risk.md`
- Plan record: `plan.md`
- Trace record: `trace.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Reference implementation: `../../reference/workspace_guard.py`
- Tests: `../../tests/test_workspace_guard.py`
- Source lineage: `../../../../00-standards-foundation/source-map.md`, `../../../../01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- Builder and reviewer can answer “what must remain true?”
- Protected and unacceptable outcomes are explicit.
- Important assumptions have invalidation triggers.
- Evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade worked-example basis inspired by public design-basis, safety-in-design, design-description, hazard/failure-analysis, AI-risk, and supply-chain-risk concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
