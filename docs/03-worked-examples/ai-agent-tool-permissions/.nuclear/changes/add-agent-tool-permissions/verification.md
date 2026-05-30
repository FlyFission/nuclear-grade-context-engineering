# Verification — Add Agent Tool Permissions

**Purpose:** Show that the first important permission claim, C-001, has evidence that fits the worked-example scope.

**Slug:** `add-agent-tool-permissions`
**Related basis:** `basis.md`
**Owner:** Nuclear-grade example maintainer
**Date:** 2026-05-17
**Verification scope:** C-001 workspace-only file writes, and C-004a making denied writes visible in the audit log.

---

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| C-001 | Pytest allowed-write test | A relative path writes inside the workspace, and the content is there. | pass | `../../tests/test_workspace_guard.py::test_allowed_relative_write_stays_inside_workspace` | None for v0. |
| C-001 | Pytest parent-`../` failure test | `../outside.txt` raises `WorkspaceViolation`, makes no outside file, and records the denial. | pass | `../../tests/test_workspace_guard.py::test_parent_traversal_write_is_denied_and_logged` | Add fuzz and property tests before production reuse. |
| C-001 | Pytest absolute-path failure test | An absolute outside path raises `WorkspaceViolation`, makes no outside file, and records the denial. | pass | `../../tests/test_workspace_guard.py::test_absolute_path_write_is_denied` | Add Windows-specific path tests before a cross-platform claim. |
| C-001 | Pytest symlink-escape failure test | A workspace symlink to an outside folder cannot be used to write outside the root. | pass | `../../tests/test_workspace_guard.py::test_symlink_escape_is_denied` | Add TOCTOU hardening before a production sandbox claim. |
| C-004a | Test checks on the audit event | Denied writes add `write_denied` with reason `outside_workspace`. | pass | The same denied-write tests. | In-memory only; a lasting audit log is deferred. |
| C-002 | Not built in v0 | No claim made. | deferred | `trace.md` | A future tool-list packet. |
| C-003 | Not built in v0 | No claim made. | deferred | `trace.md` | A future approval-gate packet. |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| RED test run | `python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q` | WSL / Python 3.12 | Expected to fail to collect before the build: `ModuleNotFoundError: No module named 'reference'`. | Session output; shows the tests were written before the sample code. |
| GREEN test run | `python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q` | WSL / Python 3.12 | `4 passed in 3.08s` | `../../tests/test_workspace_guard.py` |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| A `../` path escapes the workspace | Tried to write to `../outside.txt`. | pass — denied, and no outside file was made. | Test file. |
| An absolute path gets around the rule | Tried to write to a temp path outside the workspace. | pass — denied, and no outside file was made. | Test file. |
| A symlink inside the workspace points outside the root | Made a workspace symlink to an outside folder, then tried to write through the link. | pass — denied, and no outside file was made. | Test file. |
| A denied write is silent | Checked the latest audit event after a denial. | pass — a `write_denied` event with reason `outside_workspace`. | Test file. |

## AI-assisted work checks

- **AI scope:** AI helped draft and edit the packet, the sample code, and the tests, under the maintainer's direction.
- **Model/tool used:** local AI-assisted coding tools.
- **Permissions/actions allowed:** made docs, example Python code, and pytest tests. No commits or pushes.
- **Independent checks performed:** the pytest red/green run, the validator pass, and the attack review.
- **Hallucination/slop screening:** claims are held to C-001 and C-004a; C-002 and C-003 are deferred.
- **Human approval gates exercised:** the user approved each listed step. No outside side effects beyond local files.

## Security / dependency / supply-chain checks

- **Dependency review:** the C-001 sample code uses the Python standard library. Tests use `pytest`, which is already in the environment.
- **SBOM/provenance/build evidence:** not applicable for teaching v0.
- **Vulnerability/security review:** the failure tests cover `../` paths, absolute paths, and symlink escape. TOCTOU, ACL, container escape, multi-user, and Windows path rules are gaps.
- **Revalidation trigger:** any production reuse, new platforms, a lasting service, broader agent power, or any public claim beyond the teaching example.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`
- CI run / eval report / test logs / review notes: the local pytest output above; `adversarial-review.md` after review.
- Implementation diff / PR: repository files under `docs/03-worked-examples/ai-agent-tool-permissions/`.

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, or `not applicable`.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade verification record inspired by public sources for software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
