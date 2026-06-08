# Standard Verification

**Purpose:** Show the dispatcher-hooks claims have evidence that fits the change.

---

## Verification context

- Slug: dispatcher-hooks
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Verification scope: the hooks emit valid, static, zero-network output; they are opt-in; the preamble stays in sync and within budget. Excludes a live Claude Code session (no runtime in this container).

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | run `session_start.py`; inspect output | valid JSON; `additionalContext` has classify-first + honesty | pass | `tests/test_hooks.py` | live session deferred |
| REQ-002 | local proof | deterministic test | feed a seeded prompt; assert it is not echoed | seeded prompt absent from output | pass | `tests/test_hooks.py` | none |
| REQ-003 | local proof | deterministic test | scan hook sources for banned imports | no `socket`/`urllib`/`requests`/`http`/`subprocess`/... | pass | `tests/test_hooks.py` | none |
| REQ-004 | local proof | inspection | confirm no `hooks/hooks.json`; HOOKS.md enable step | hooks inert until wired in settings.json | pass | `HOOKS.md` | none |
| REQ-005 | local proof | deterministic test | cluster-sync vs CORE.md; preamble length | clusters present in both; preamble < budget | pass | `tests/test_hooks.py` | none |
| live injection | unknown | independent verification | enable hooks; start a Claude Code session | preamble + reminder appear in context | deferred | maintainer run | tracked in `ship.md` |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Hook smoke-run | `echo '{...}' | python hooks/session_start.py` | Python 3, container | valid JSON; 1898-char preamble | this packet |
| No-echo smoke | `echo '{"user_prompt":"SECRET"}' | python hooks/user_prompt_submit.py` | Python 3 | SECRET absent | this packet |
| Full suite | `python -m pytest -q` | Python 3 | 123 passed | CI |
| Lint | `python -m ruff check .` | ruff 0.15.16 | clean | CI |
| Doctor | `python tools/ng.py doctor .` | repo | OK | CI |
| Token budget | `python tools/ng.py tokens .` | repo | OK | CI |
| Packet validate | `python tools/ng.py validate .nuclear/changes/dispatcher-hooks` | repo | OK | CI |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Hook reaches the network / shells out | banned-import scan over hook sources | pass | `tests/test_hooks.py` |
| Hook echoes the user's prompt | seeded-prompt no-echo test | pass | `tests/test_hooks.py` |
| Injection markers in the preamble | injection-firewall test | pass | `tests/test_hooks.py` |
| Preamble drifts from CORE.md | cluster-sync test | pass | `tests/test_hooks.py` |

## AI-assisted work checks

- AI scope: wrote two hook scripts + HOOKS.md + tests + this packet under review.
- Model/tool used: Claude Code agent.
- Permissions/actions allowed: edit files; run tests; the shipped hooks make no network calls.
- Independent checks performed: full suite + lint + doctor + tokens + validate; hook smoke-runs.
- Self-check / turnover records: not activated.
- Hallucination/slop screening: hook I/O traces to cited official docs; the preamble mirrors CORE.md.
- Human approval gates exercised: PR review + a maintainer live-session run pending.

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
