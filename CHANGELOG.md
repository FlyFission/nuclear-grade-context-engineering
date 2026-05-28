# Changelog

All notable changes to Nuclear-grade are documented in this file.

This project uses changelog entries to record public-facing changes, not to imply semantic-versioned product maturity.

## [Unreleased]

### Added

- Mission-driven backbone. A durable repo charter (`.nuclear/charter.md`) of named process-integrity principles (ownership, facing facts, rising standards, formality, technical depth, integrity in reporting, questioning attitude, evidence over persuasion, graded rigor, baseline discipline; nuclear-culture and Rickover/Navy lineage), plus a per-change `## Mission anchor` (objective + success criteria + non-goals) in the Standard risk template. `nuclear-grade init` now writes a starter `.nuclear/charter.md` and `.nuclear/mission.md` (both advisory).
- `controlling-mission-drift` skill: detect and correct intent drift (scope creep, goal substitution) with a re-anchor / escalate / stop decision and a counted escalation trigger (stop after 3 failed attempts or a loop).
- `reviewing-code-quality` skill: standards-drift review (prefer deletion over rearrangement, countable complexity tripwires, abstractions must earn their keep, no feature logic in shared layers, single verdict).
- `ng-drift-check` and `ng-code-review` portable command prompts for the two skills.
- A re-evaluated drift gate (`## Charter and anchor check` with a justification table) in the Standard plan template.
- Advisory validator checks: a mission anchor is checked for objective, success criterion, and non-goals only when a `## Mission anchor` section is present; unresolved NEEDS-CLARIFICATION markers fail before ship. Both are non-breaking (only fire when present).
- Placeholder marker on every Quick, Standard, CM, and golden-path template; the validator now rejects any packet that still carries it, so an untouched scaffold no longer validates green.
- Doctor now requires `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` as public files.

### Removed

- Moved `docs/04-adoption/report-swot-gap-remediation.md` out of the public docs tree into the gitignored `.research/` scratch space; the only reference in `docs/04-adoption/README.md` is removed.

## [0.2.0] - 2026-05-27

### Breaking

- The validator now requires every packet's `risk.md` to declare its mode under a `## Selected mode` section (e.g. `- **Mode:** Quick` or `- **Mode:** Standard`). Packets without a declaration fail validation. Use `python tools/ng.py migrate <packet>` (or `nuclear-grade migrate <packet>` from an installed wheel) to insert a `## Selected mode` block with an inferred default based on the files present.

### Added

- `nuclear-grade new --mode cm` and `--mode golden-path` scaffold all five CM files and all five golden-path files respectively, so the QUICKSTART manual-`cp` blocks are no longer required.
- `nuclear-grade migrate <packet>` inserts a `## Selected mode` block into a packet whose `risk.md` does not yet declare one. Idempotent. Prints the inferred mode and a one-line override notice.
- Paraphrase-aware prohibited-claims detection: a tighter, entity-adjacent regex catches phrasings like "meets NQA-1 requirements", "fully ASME qualified", "conforms to IEEE 829", "satisfies 10 CFR 50 Appendix B", "implements quality assurance per NQA-1", "audited to NRC standards", and "regulator-approved". Negation gates (`inspired by`, `influenced by`, `does not claim`, "no formal", paragraph-level disclaimer markers) suppress legitimate boundary prose. Fenced code blocks are exempt.
- `_bundled/` snapshot of `templates/`, `skills/`, and `commands/` inside the wheel. The installed CLI no longer depends on its source-tree neighbors and now works end to end from a clean `pip install`.
- Hatchling build backend with `[tool.hatch.build.targets.wheel.force-include]` to bundle resources at wheel-build time without duplicating sources in the repo.
- CI matrix across Python 3.11 and 3.12.
- `ruff` lint step in CI (selects E, F, I, B, UP; ignores E501).
- `wheel-smoke` CI job that builds the wheel, installs it into a clean venv, and exercises `init`, `new --mode {quick,standard,cm,golden-path}`, `list`, and `validate` outside the source tree.
- `CITATION.cff` (CFF 1.2) at the repo root.
- `.github/CODEOWNERS` with a maintainer placeholder.

### Fixed

- README and QUICKSTART now frame the 60-second demo so the expected `FAILED` output reads as the validator catching unfilled prompts (intentional), not as breakage.
- The unfilled-template-prompt detector no longer caps the matched label at 80 characters; long verbose labels are now caught.
- `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` now leads with a methodology banner naming the qualitative, author-judged nature of the 1-5 scores and centres the numeric column markers.
- `docs/04-adoption/report-swot-gap-remediation.md` now explicitly marks the Files / Skills / Commands listed under Phases 1 through 4 as proposed deliverables, not existing refs.

### Changed

- README "What you get" CLI row lists all four `new` modes and the `migrate` subcommand.
- README "Public v0 status" replaces "validated worked example" with "tested worked example" (workspace-only file writes; pytest-checked) plus an "author-judged adoption comparison" line.
- `templates/quick/risk.md` ships with a pre-filled `## Selected mode` block (`- **Mode:** Quick`). The standard template already shipped with one.
- `pyproject.toml` bumps version to `0.2.0` and switches the build backend to `hatchling`.

## [0.1.0] - 2026-05-20

### Added

- Public-source-safe standards foundation and source-status labels.
- Quick and Standard packet templates.
- Git-native lifecycle, modes, activation thresholds, change packets, context packs, token-burn control, and validator guidance.
- Completed Standard-mode worked example for AI-agent workspace-only file writes.
- Dependency-free Python validator for Quick and Standard packet structure, evidence status, source-lineage notes, local packet links, and prohibited overclaiming phrases.
- Pytest coverage for the validator and worked-example path guard.
- Configuration-management public positioning and activated CM workflow records.
- Namespaced `nuclear_grade` package entry point for installed console scripts.
- Skill evaluation prompt bank for baseline-vs-skill trigger checks.
- HPI overlay operating doc for AI-agent task preview, self-checking, turnover, verification selection, conservative decisions, and OPEX learning.
- Skills and command prompts for agent turnover, critical-action self-checking, OPEX learning, and dependency/model/API trust checks.
- Golden-path templates for turnover and self-check records, plus an activated supplier-trust template.
- Agent near-miss issue template.
- Issue templates for bugs and docs/methodology/source-lineage concerns.
- Pull request template with Nuclear-grade verification and overclaiming checks.
- Contributor Covenant Code of Conduct.
- Private readiness cleanup: removed planning scaffolding and stripped internal content from the knowledge-graph usage note.

### Changed

- Reworked the README into a workflow-first landing page for AI builders.
- Clarified Public v0 boundaries, source-lineage rules, and non-compliance claims.
- Strengthened all skill trigger descriptions against skill-creator best practices.
- Strengthened context packs, verification, release decisions, templates, worked-example comparisons, and source lineage with HPI micro-controls.

### Not Included

- C-002 external API controls and C-003 human approval gate evidence chains.
- Rich deterministic validation for activated Nuclear, Incident, Research Board, and Release records.
- Production sandbox, compliance package, or regulated-use assurance workflow.
