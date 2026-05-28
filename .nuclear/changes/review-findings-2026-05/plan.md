# Plan

## Change context

- Slug: review-findings-2026-05
- Mode: Standard
- Owner: maintainer

## Build sequence

Three layers (tooling, content, hygiene) with regression tests added before each substantive code change so each fix has a verifiable definition of done.

1. **Packet skeleton.** `risk.md`, `basis.md`, `plan.md` exist from step one with `## Selected mode` declared (this file is step one).
2. **Pre-flight.** Confirm every existing repo packet declares a mode. (Completed: all seven packets already have a `## Selected mode` section.)
3. **Regression tests added first.** Paraphrase battery (F3), missing-mode (F4), `--mode cm` and `--mode golden-path` scaffolding (F5), long-label empty prompt (F7), packaging archive contents (F2 contract), `migrate` subcommand (F4). Confirmed failing before code changes.
4. **Validator updates.** `nuclear_grade/ng_validate.py` gets: tightened `EMPTY_PROMPT_PATTERN` (F7), explicit mode requirement (F4), and hybrid prohibited-claims detector (F3) that augments the fixed-phrase list with a verb-stem regex over compliance nouns. Negation gate broadens to `inspired by`, `influenced by`, `does not claim`, `not implementing`. Existing tests at `tests/test_ng_validate.py:122-151` are guardrails.
5. **CLI updates.** `nuclear_grade/cli.py` gets: `--mode cm` and `--mode golden-path` for `new` scaffolding all five files of each mode (F5); a `migrate` subcommand that inserts `## Selected mode` into a `risk.md` lacking one (F4 migration); and a wheel-aware resolver for `SKILLS`, `COMMANDS`, and the bundled-templates fallback (F2).
6. **Build backend switch.** `pyproject.toml` switches to `hatchling` with `[tool.hatch.build.targets.wheel.force-include]` mapping `templates`, `skills`, `commands` into `nuclear_grade/_bundled/` (F2, F12). Version bumps to `0.2.0` (F12). Adds `[tool.ruff]` configuration (F6).
7. **CI updates.** `.github/workflows/ci.yml` matrices on Python 3.11 and 3.12, adds a `ruff` step, and adds a `wheel-smoke` job that builds, installs, and exercises the wheel end to end (F6, F2 regression).
8. **Test pass.** Full pytest suite under 3.11 and 3.12 (or the available interpreter); `doctor` and `validate` on every existing packet.
9. **Content updates.** `README.md` (F1 framing, F8 tightened "validated"), `QUICKSTART.md` (F1 framing, F5 scaffold commands, F4 migration callout), `templates/quick/risk.md` (F4 pre-fill), `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` (F8 banner, centered cells), `docs/04-adoption/report-swot-gap-remediation.md` (F11 proposed banner).
10. **Hygiene.** `CHANGELOG.md` collapsed and stamped (F9), `CITATION.cff` (F10), `.github/CODEOWNERS` (F10).
11. **Packet closure.** Fill `trace.md`, `verification.md`, `ship.md`. Run `python tools/ng.py validate .nuclear/changes/review-findings-2026-05`.
12. **Push.** Commit and push to `claude/intelligent-knuth-QA4L5`. Open draft PR.

## Critical-action self-check

Not activated. No wrong-target risk: every file is edited within the repo tree and tests assert behavior at every layer.

## HPI work-mode controls

- **Task preview (before wheel rework):** Confirm `hatchling` `force-include` is the correct mechanism (it is, per Hatch docs). Confirm the resolver tries the repo path first so the in-repo dev workflow stays intact. Confirm CI catches a missing bundled file.
- **Self-check (before validator change):** The new regex must not break the three existing guardrail tests at `tests/test_ng_validate.py:122-151`. Run those tests after each edit to the validator module.
- **Turnover:** Not activated (single-author packet).

## Files to create

- `.nuclear/changes/review-findings-2026-05/risk.md` (this packet)
- `.nuclear/changes/review-findings-2026-05/basis.md`
- `.nuclear/changes/review-findings-2026-05/plan.md` (this file)
- `.nuclear/changes/review-findings-2026-05/trace.md`
- `.nuclear/changes/review-findings-2026-05/verification.md`
- `.nuclear/changes/review-findings-2026-05/ship.md`
- `CITATION.cff`
- `.github/CODEOWNERS`

## Files to modify

- `nuclear_grade/cli.py`, `nuclear_grade/ng_validate.py`
- `pyproject.toml`
- `.github/workflows/ci.yml`
- `tests/test_ng_validate.py`, `tests/test_ng_cli.py`, `tests/test_packaging.py`
- `README.md`, `QUICKSTART.md`
- `templates/quick/risk.md`
- `docs/03-worked-examples/skill-workflow-comparison/results-summary.md`
- `docs/04-adoption/report-swot-gap-remediation.md`
- `CHANGELOG.md`

## Required links

- Packet: `.nuclear/changes/review-findings-2026-05/`
- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Build sequence above is executed top to bottom.
- Test suite green.
- Packet passes its own validator.

## Source-lineage note

Original Nuclear-grade plan inspired by graded-rigor and configuration-management lifecycle concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
