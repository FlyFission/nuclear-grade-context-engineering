# Verification — Add Agent Tool Permissions

**Purpose:** Show that the first important permission claim, C-001, has evidence proportionate to the worked-example scope.

**Slug:** `add-agent-tool-permissions`
**Related basis:** `basis.md`
**Owner:** Nuclear-grade example maintainer
**Date:** 2026-05-17
**Verification scope:** C-001 workspace-only file writes and C-004a denied-write audit visibility.

---

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| C-001 | Pytest allowed-write test | Relative path writes inside workspace and content is present. | pass | `../../tests/test_workspace_guard.py::test_allowed_relative_write_stays_inside_workspace` | None for v0. |
| C-001 | Pytest parent-traversal negative test | `../outside.txt` raises `WorkspaceViolation`, does not create outside file, records denial. | pass | `../../tests/test_workspace_guard.py::test_parent_traversal_write_is_denied_and_logged` | Add fuzz/property tests before production reuse. |
| C-001 | Pytest absolute-path negative test | Absolute outside path raises `WorkspaceViolation`, does not create outside file, records denial. | pass | `../../tests/test_workspace_guard.py::test_absolute_path_write_is_denied` | Add Windows-specific path tests before cross-platform claim. |
| C-001 | Pytest symlink-escape negative test | Workspace symlink to outside directory cannot be used to write outside root. | pass | `../../tests/test_workspace_guard.py::test_symlink_escape_is_denied` | Add TOCTOU hardening before production sandbox claim. |
| C-004a | Test assertions on audit event | Denied writes append `write_denied` with reason `outside_workspace`. | pass | Same denied-write tests. | In-memory only; durable audit deferred. |
| C-002 | Not implemented in v0 | No claim made. | deferred | `trace.md` | Future tool registry packet. |
| C-003 | Not implemented in v0 | No claim made. | deferred | `trace.md` | Future approval-gate packet. |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| RED test run | `python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q` | WSL / Python 3.12 | Expected collection failure before implementation: `ModuleNotFoundError: No module named 'reference'`. | Session output; confirms tests were written before reference implementation. |
| GREEN test run | `python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q` | WSL / Python 3.12 | `4 passed in 3.08s` | `../../tests/test_workspace_guard.py` |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Parent traversal escapes workspace | Attempted write to `../outside.txt`. | pass — denied and outside file absent. | Test file. |
| Absolute path bypasses policy | Attempted write to temp outside path. | pass — denied and outside file absent. | Test file. |
| Symlink inside workspace points outside root | Created workspace symlink to outside directory, attempted write through link. | pass — denied and outside file absent. | Test file. |
| Silent denial | Checked latest audit event after denial. | pass — `write_denied` event with `outside_workspace` reason. | Test file. |

## AI-assisted work checks

- **AI scope:** AI-assisted drafting and editing produced the packet, reference implementation, and tests under maintainer direction.
- **Model/tool used:** Local AI-assisted coding tools.
- **Permissions/actions allowed:** Created docs, example reference Python code, and pytest tests. No commits or pushes.
- **Independent checks performed:** Pytest red/green run, validator pass, and adversarial review.
- **Hallucination/slop screening:** Claims are limited to C-001/C-004a; C-002/C-003 are deferred.
- **Human approval gates exercised:** User approved continuing with all listed steps; no external side effects beyond local files.

## Security / dependency / supply-chain checks

- **Dependency review:** C-001 reference implementation uses Python standard library. Tests use `pytest` already available in environment.
- **SBOM/provenance/build evidence:** Not applicable for educational v0.
- **Vulnerability/security review:** Negative tests cover traversal, absolute path, and symlink escape. TOCTOU, ACL, container escape, multi-user, and Windows semantics are gaps.
- **Revalidation trigger:** Any production reuse, platform expansion, persistent service, broader agent authority, or public claim beyond the educational example.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`
- CI run / eval report / test logs / review notes: local pytest output above; `adversarial-review.md` after review.
- Implementation diff / PR: repository files under `docs/03-worked-examples/ai-agent-tool-permissions/`.

## Exit criteria

- Each important claim has `pass`, `fail`, `gap`, `deferred`, or `not applicable` status.
- Evidence is linked rather than pasted in full.
- Gaps are explicit and reflected in `ship.md`.
- Reviewer can tell whether the evidence supports the release decision.

## Source-lineage note

Original Nuclear-grade verification record inspired by public software V&V, test-documentation, secure-development, software assurance, AI-risk, and application-security verification sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
