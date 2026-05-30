# Basis — Add Agent Tool Permissions

**Purpose:** State what must stay true for the example's permission limit to be safe, reliable, useful, and easy to review.

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
- **Decision this basis supports:** Whether the Standard-mode worked example can show one complete, honest claim-to-evidence chain for letting an AI agent write files.

## Mission / need

AI agents are given more and more power over tools: writing files, calling APIs, running shell commands, changing databases, and approving steps in a workflow. Nuclear-grade needs a small worked example. It should show how to turn one power-changing feature into a clear basis, controls, proof, and a release check, without pretending to solve every security problem.

The v0 mission is kept narrow on purpose: prove that an agent's file-write helper writes only inside an approved workspace, and makes denied writes visible.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| File writes stay inside the set workspace root. | Stops harmful or unallowed writes outside the approved area. | Tests for an allowed relative write and a denied `../`, absolute, or symlink escape. |
| Denied writes leave an audit event you can read. | Silent denials hide bypass attempts and weaken operations. | Test checks against `audit_events` for denied writes. |
| The example does not imply broad sandbox or security guarantees. | Keeps people from trusting it too much. | README, verification, and ship records clearly limit proof to C-001. |
| The other claims are labeled planned, gap, or deferred. | Stops a made-up table from looking complete. | Status labels in `trace.md`, `verification.md`, and `ship.md`. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A `../` path writes outside the workspace. | The agent could harm or leak files outside the allowed area. | Resolve the real path, then check it stays in the workspace; `../` test. |
| An absolute path writes outside the workspace. | The caller gets around the relative-path rule. | Resolve absolute paths and deny them when they fall outside the root; absolute-path test. |
| A symlink inside the workspace points writes outside it. | The workspace allowlist is dodged through a filesystem link. | Resolve the final path and deny it if it lands outside the root; symlink escape test. |
| A denied write vanishes with no record. | Operators cannot spot misuse, bad prompts, or bypass attempts. | Add a structured `write_denied` audit event; test checks. |
| The example is treated as a production sandbox. | Users may trust a teaching sample too much. | Source-lineage and ship notes state the teaching scope and the gaps. |

## Assumptions and constraints

| Assumption / constraint | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|
| The workspace root is the only approved place to write for C-001. | The worked-example mission and `risk.md`. | A need to write shared caches, temp folders, credentials, or production paths. | Maintainer |
| Standard-library path resolution is enough for this teaching example. | A minimal sample build with no outside dependency. | Moving to non-POSIX rules, a remote filesystem, containers, ACL-heavy setups, or production sandboxing. | Maintainer |
| Audit events can live in memory for v0 evidence. | The example scope; no production runtime. | A lasting service, multi-process workers, incident review, or outside operations. | Maintainer |
| No formal compliance or certification claim is made. | Repo boundary docs and the disclaimer. | Any public claim that this meets a regulator, a standard, a QA program, or certification. | Maintainer |

## Interfaces and trust boundaries

- **Internal interfaces affected:** the `WorkspaceGuard.write_text(requested_path, content)` sample API.
- **External services/APIs affected:** none for C-001.
- **Data classes affected:** example text file content only; no sensitive data in v0.
- **Human approval boundaries:** not built for C-001. High-impact writes would turn on C-003 in a later packet.
- **AI/model/tool authority boundaries:** the agent or tool caller may ask to write files; the guard keeps writes inside the workspace before it touches the filesystem.

## Dependency / model / supplier intended use

| Dependency/model/service | Intended use | Consequence if wrong/unavailable/compromised | Evidence or compensating control | Revalidation trigger |
|---|---|---|---|---|
| Python `pathlib` | Build and resolve the real path in the teaching code. | Wrong path handling could weaken C-001. | Tests that bad paths fail: `../`, absolute path, symlink escape. | Python or platform path rules change, production hardening, a Windows-only release. |
| `pytest` | Run the example's evidence tests. | The test evidence is missing or misleading. | Test command and output saved in `verification.md`. | The test framework or runtime changes. |

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| C-001 | The agent writes only under the set workspace root. | Protect the filesystem and limit the agent's power over tools. | Resolve the requested path, require it to stay under the workspace root, deny it otherwise, log the denial. | `pytest` tests: allowed write, denied `../`, denied absolute path, denied symlink. |
| C-004a | Denied C-001 writes produce visible audit events. | Denied actions are operational signals. | An in-memory structured audit event with the event, requested path, resolved path, root, and reason. | Test checks on `audit_events`. |
| C-002 | External API calls need approved tool IDs and scoped credentials. | Stop random network side effects and credential misuse. | A future tool list and credential binding. | Deferred or gap for v0. |
| C-003 | Human approval is required for high-impact actions. | Send consequence-changing power up to a person for review. | A future approval policy and approval record. | Deferred or gap for v0. |

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

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade worked-example basis inspired by public ideas on design basis, safety built into design, design description, hazard and failure analysis, AI risk, and supply-chain risk, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
