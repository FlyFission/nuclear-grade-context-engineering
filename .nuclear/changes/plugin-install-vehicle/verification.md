# Standard Verification

**Purpose:** Show the plugin-packaging claims have evidence that fits the change.

---

## Verification context

- Slug: plugin-install-vehicle
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Verification scope: manifest validity, version-sync, no-executable-code structure, honest docs. Excludes the live `/plugin install` (no Claude Code CLI in this container).

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | source claim / local proof | deterministic test + peer review | manifests parse; fields match the official schema; packaging test | manifests valid and match docs | pass | `tests/test_plugin_packaging.py`; official docs | live install deferred |
| REQ-001 (live install) | unknown | independent verification | `/plugin marketplace add` + `/plugin install` on a Claude Code surface | plugin installs; skills/commands appear | deferred | maintainer run | tracked in `ship.md` |
| REQ-002 | local proof | deterministic test | `test_plugin_version_tracks_pyproject` | versions equal | pass | `tests/test_plugin_packaging.py` | none |
| REQ-003 | local proof | deterministic test | `test_components_live_at_plugin_root_not_inside_claude_plugin` + `test_no_auto_activated_hooks_config` | components at root; no `hooks/hooks.json` (no auto-activation) | pass | `tests/test_plugin_packaging.py` | none |
| REQ-004 | local proof | deterministic test + peer review | `test_public_docs`; `doctor`; wording review | boundary phrasing intact; leads with the plugin | pass | `tests/test_public_docs.py`; `INSTALL.md` | none |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Manifest parse | `python -c "import json; json.load(open('.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json'))"` | Python 3, CI container | manifests parse | this packet |
| Full suite | `python -m pytest -q` | Python 3 | 122 passed | CI |
| Lint | `python -m ruff check .` | ruff 0.15.16 | clean | CI |
| Doctor | `python tools/ng.py doctor .` | repo | OK | CI |
| Token budget | `python tools/ng.py tokens .` | repo | OK | CI |
| Packet validate | `python tools/ng.py validate .nuclear/changes/plugin-install-vehicle` | repo | OK | CI |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Components misplaced inside `.claude-plugin/` | test asserts only manifests live there | pass | `tests/test_plugin_packaging.py` |
| Version drift, plugin vs package | version-sync test | pass | `tests/test_plugin_packaging.py` |

## AI-assisted work checks

- AI scope: drafted manifests, test, docs, and this packet under review.
- Model/tool used: Claude Code agent.
- Permissions/actions allowed: edit files in this repo; run tests; no executable hooks shipped.
- Independent checks performed: schema confirmed against cited official docs; full suite + lint + doctor + tokens + validate.
- Self-check / turnover records: not activated.
- Hallucination/slop screening: schema verified against cited official docs, not from memory.
- Human approval gates exercised: PR review + maintainer live-install pending.

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

Original Nuclear-grade record inspired by public sources on software verification and validation, test documentation, and AI risk, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
