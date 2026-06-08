# Standard Plan

**Purpose:** Bound the CI-scaffold generator work, its review, and its rollback.

---

## Change context

- Slug: ci-scaffold-generator
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: graded rigor (the real gate matches the stakes); honest reporting (structural-only banner).

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | n/a | n/a | n/a |

## Build sequence

| # | Task | Requirements covered | Prereqs / blocked-by | Proof for this step | Stop / done condition |
|---|---|---|---|---|---|
| 1 | Add `scaffold-ci` subcommand + hardened workflow template to `cli.py` | REQ-001, REQ-002 | none | generator writes a file; YAML parses | subcommand works |
| 2 | Harden this repo's `ci.yml` (`permissions: contents: read`) | REQ-003 | none | CI still green | block present |
| 3 | Add generator tests (write, dry-run, force, hardening) | REQ-004 | step 1 | `pytest` green | tests pass |

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | confirm F5 hardening + CLI patterns | requirements known |
| candidate | write the subcommand + template + tests | generator runs; YAML parses |
| audit | full suite + ruff + doctor + tokens + validate | all green |
| accept | open PR; maintainer runs the generated workflow once | human review + a live Actions run |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Writing the workflow template | Wrong trigger or missing permissions → unsafe gate | Fork-PR token/secret exposure | Hardened template + guard test asserting the properties | `verification.md` |
| Editing this repo's `ci.yml` | A too-narrow token breaks a job | CI fails | `contents: read` suffices for read-only validate/build jobs; revert on failure | CI run |

## Agent briefing

- Role: builder (drafting under review).
- Authority source: the approved plan; this packet.
- Active procedure/template: Standard packet.
- Last completed action if resumed: subcommand + template + ci.yml hardening + tests written and verified.
- Handoff or turnover needed? no
- Pause when unsure condition: pause if a step would drop a hardening property or emit an unverified action SHA.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/cli.py` | edit | REQ-001, REQ-002 | the generator + template | FlyFission |
| `.github/workflows/ci.yml` | edit | REQ-003 | this repo's CI hardening | FlyFission |
| `tests/test_ng_cli.py` | edit | REQ-004 | guards the generator | FlyFission |

## Non-goals

- No in-session hooks (a later, gated tier).
- No guessed action SHAs (tag-pin + a SHA-pin recommendation instead).
- No live GitHub Actions run from this container.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| How the generated workflow gets the validator | `pip install nuclear-grade`, with a git-install fallback comment | vendoring the tool into adopter repos | simplest; adopters of nuclear-grade can install it | if PyPI publication lags, adopters use the git pin |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | REQ-001..004 each a clear trigger→response, reviewed | pass |
| Design approved | a CLI subcommand + a hardened template | pass |
| Tasks approved | Build steps carry requirement IDs | pass |
| Specification reviewed | Protected and unacceptable outcomes stated | pass |
| Tests/evals defined | Each claim maps to evidence | pass |
| Build complete | The subcommand + ci.yml + tests match the plan | pass |
| Verification complete | Evidence linked in `verification.md` | pass |
| Release decision ready | Leftover risk + rollback recorded | pass |
| Turnover complete if activated | Not activated | not applicable |

## Rollback approach

- Rollback method: revert the `cli.py`, `ci.yml`, and test edits (single revert); adopters delete the generated workflow file.
- State/data reversal notes: none.
- Feature flag / kill switch: removing the `scaffold-ci` subcommand disables the generator.
- Owner: FlyFission
- Time to restore estimate: minutes.

## Proof commands

```bash
python tools/ng.py scaffold-ci /tmp/scratch-repo
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/ci-scaffold-generator
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: the approved plan (Phase 3) + F5.

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on configuration management, release readiness, and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
