# Standard Verification

**Purpose:** Show the CI-scaffold generator claims have evidence that fits the change.

---

## Verification context

- Slug: ci-scaffold-generator
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Verification scope: the generator writes a valid, hardened workflow; this repo's CI is hardened; behavior is guarded. Excludes a live GitHub Actions run (no runner in this container).

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | `ng scaffold-ci` into a temp dir; assert the hardening lines by string match, then parse the file as YAML | a workflow file with the hardening present that runs the validator, and that parses as valid YAML | pass | `tests/test_ng_cli.py` | live Actions run deferred (no runner here), tracked in `ship.md`; YAML validity is now parsed deterministically (PyYAML, test-only dep — the shipped package stays zero-dep) |
| REQ-002 | local proof | deterministic test | guard test asserts permissions/trigger/no-secrets | `contents: read`; `pull_request`; no `pull_request_target`; no `secrets.` | pass | `tests/test_ng_cli.py` | none |
| REQ-003 | local proof | deterministic test + CI | `permissions: contents: read` in `ci.yml`; suite green | block present; CI passes | pass | `.github/workflows/ci.yml` | none |
| REQ-004 | local proof | deterministic test | write / dry-run / force / hardening tests | all pass | pass | `tests/test_ng_cli.py` | none |
| live run | unknown | independent verification | run the generated workflow on a real adopter PR | gate passes/fails correctly | deferred | maintainer run | tracked in `ship.md` |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Generate + string-assert + YAML parse | `ng scaffold-ci <tmp>`; assert `contents: read`, `pull_request`, no `secrets.`, validator step, branch-protection note; then `yaml.safe_load` the file | Python 3 + PyYAML, container | hardening lines present; parses as valid YAML | this packet |
| Full suite | `python -m pytest -q` | Python 3 | 122 passed | CI |
| Lint | `python -m ruff check .` | ruff 0.15.16 | clean | CI |
| Doctor | `python tools/ng.py doctor .` | repo | OK | CI |
| Token budget | `python tools/ng.py tokens .` | repo | OK | CI |
| Packet validate | `python tools/ng.py validate .nuclear/changes/ci-scaffold-generator` | repo | OK | CI |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Privileged fork trigger | test asserts no `pull_request_target` | pass | `tests/test_ng_cli.py` |
| Secret reference | test asserts no `secrets.` | pass | `tests/test_ng_cli.py` |
| Clobbering an existing workflow | refuses without `--force`; `--dry-run` is non-mutating | pass | `tests/test_ng_cli.py` |
| Closed packet blocks the gate forever | generated loop (and this repo's CI) skip dirs with a genuine `NUCLEAR-GRADE-CLOSED:` note | pass | `tests/test_ng_cli.py` |

## AI-assisted work checks

- AI scope: added a CLI subcommand + template, hardened `ci.yml`, added tests, drafted this packet under review.
- Model/tool used: Claude Code agent.
- Permissions/actions allowed: edit files; run tests; no in-session hooks shipped.
- Independent checks performed: full suite + lint + doctor + tokens + validate; YAML parse.
- Self-check / turnover records: not activated.
- Hallucination/slop screening: hardening traces to F5 and GitHub docs; no action SHAs were guessed.
- Human approval gates exercised: PR review + a maintainer live Actions run pending.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: GitHub Actions on the PR.
- Implementation diff / PR: this branch's PR.

## Exit criteria

- Each important claim has a status.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on software verification and validation and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
