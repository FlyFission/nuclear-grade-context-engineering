# Standard Verification

**Purpose:** Show the PROVE-pipeline claims have evidence that fits the change.

---

## Verification context

- Slug: prove-pipeline
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Verification scope: the five subagent defs exist, are valid, encode the authority split, and carry the honesty caveat. Excludes a live multi-agent orchestration run.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | roster + frontmatter test | exactly the five agents; valid frontmatter | pass | `tests/test_agents.py` | live run deferred |
| REQ-002 | local proof | deterministic test | authority-split test over `tools` | judge read-only; observer no writes; runner build authority | pass | `tests/test_agents.py` | none |
| REQ-003 | local proof | peer review | read each def for the baton-pass contract | Context Pack + closed-loop confirm + data-fence + halt present | pass | `agents/*.md` | none |
| REQ-004 | local proof | deterministic test | README caveat test | "not a perimeter" + permissionMode + `.claude/agents/` | pass | `tests/test_agents.py` | none |
| live orchestration | unknown | independent verification | run the pipeline on a Standard+ change | stages hand off and gate correctly | deferred | maintainer run | tracked in `ship.md` |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Agent tests | `python -m pytest -q tests/test_agents.py` | Python 3 | pass | CI |
| Full suite | `python -m pytest -q` | Python 3 | all pass | CI |
| Lint | `python -m ruff check .` | ruff 0.15.16 | clean | CI |
| Doctor | `python tools/ng.py doctor .` | repo | OK | CI |
| Token budget | `python tools/ng.py tokens .` | repo | OK | CI |
| Packet validate | `python tools/ng.py validate .nuclear/changes/prove-pipeline` | repo | OK | CI |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| An agent's tools contradict its authority | authority-split test | pass | `tests/test_agents.py` |
| README overclaims a perimeter | caveat test asserts "not a perimeter" | pass | `tests/test_agents.py` |

## AI-assisted work checks

- AI scope: wrote five agent defs + README + tests + this packet under review.
- Model/tool used: Claude Code agent.
- Permissions/actions allowed: edit files; run tests; the defs ship no executable code.
- Independent checks performed: full suite + lint + doctor + tokens + validate.
- Self-check / turnover records: not activated.
- Hallucination/slop screening: frontmatter schema traces to cited official docs.
- Human approval gates exercised: PR review + a maintainer live-orchestration run pending.

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

Original Nuclear-grade record inspired by public sources on software verification and validation and human performance improvement, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
