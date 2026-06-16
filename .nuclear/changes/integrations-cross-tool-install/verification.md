# Standard Verification Record

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

**Activation threshold:** Use for Standard changes, and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/evals/reviews, the results, the evidence links, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim, be repeatable enough to review, and carry a status label.

---

## Verification context

- Slug: integrations-cross-tool-install
- Related basis: `basis.md`
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16
- Verification scope: the install/config CLI surface, the optional MCP server, and the version mirrors.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | `test_install_*` plus a dry-run | core installs 8, full 27, correct dirs | pass | `tests/test_ng_cli.py` | none |
| REQ-002 | local proof | deterministic test | run the suite without the extra | suite green; MCP test skipped | pass | CI `validate` job | none |
| REQ-003 | local proof | deterministic test | `test_install_unverified_tool_warns_to_verify_path` | unverified tool prints the note | pass | `tests/test_ng_cli.py` | none |
| REQ-004 | local proof | deterministic test | `test_all_version_mirrors_track_pyproject` | all mirrors equal `pyproject` | pass | `tests/test_packaging.py` | none |

## Verification type guide

| Type | Use when |
|---|---|
| self-check | the target of a critical action and the expected result matter |
| peer-check | another reviewer should stop a wrong action before it happens |
| concurrent verification | a high-stakes action must be watched as it happens |
| independent verification | the final state must be checked apart from the doer's claim |
| peer review | artifact quality, maintainability, usability, or boundary wording matters |
| deterministic test / eval | there is repeatable evidence of the behavior |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Unit/integration | `python -m pytest -q` | Python 3.11 and 3.12 | 165 passed, 1 skipped | CI `validate` job |
| Lint | `python -m ruff check .` | Python 3.12 | all checks passed | CI `validate` job |
| Repo health | `python tools/ng.py doctor .` | Python 3.12 | OK | CI `validate` job |
| MCP server | `pytest tests/test_mcp_server.py` with the extra | clean venv | list_tools returns 4 tools | CI `mcp-smoke` job |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| MCP extra absent | run the suite with no `mcp` installed | the server test skips, suite stays green | CI `validate` job |
| Unknown tool argument | `ng install emacs` / `ng mcp-config emacs` | argparse rejects with non-zero exit | `tests/test_ng_cli.py` |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: drafted the implementation, tests, docs, and this record on branch `claude/loving-ride-sgg6ww`.
- Model/tool used: Claude Code agent with file, shell, and web-search tools.
- Permissions/actions allowed: edit the repo, run tests, push the branch, open/update PR #42.
- Independent checks performed: deterministic tests plus a human PR review on #42.
- Self-check / turnover records: not applicable (single session, no handoff).
- Hallucination/slop screening: tool paths and the Codex manifest were re-verified against first-party docs after a sub-agent citation was found to be fabricated.
- Human approval gates exercised: plan approved before build; PR review before merge.

## Security / dependency / supply-chain checks

Use if activated.

- Dependency review: `mcp` is an optional extra only; the base install stays dependency-free.
- SBOM/provenance/build evidence: the wheel build is exercised by the `wheel-smoke` CI job.
- Vulnerability/security review: no network, secrets, or production surface; MCP tools act on local files only.
- Revalidation trigger: a new major of `mcp` or a FastMCP API change.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: PR #42 checks
- Implementation diff / PR: PR #42

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on software verification and validation, test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
