# Changelog

This file lists every notable change to Nuclear-grade.

These entries record public-facing changes. They do not claim the project is a mature product with strict semantic versions.

## [Unreleased]

## [0.3.0] - 2026-05-28

### Changed

- Changed the rules for how a skill describes itself, so agents pick the right skill more often. We dropped the required `Use when` prefix and the old 90-to-180-character limit. Each description now says what the skill does, when to use it, and a clear "Do not use for ..." line. It must be 80 to 500 characters and must not contain a colon followed by a space, so strict file readers treat it as one piece of text. We rewrote all 18 skill descriptions this way. A skill `name` must be lowercase with words joined by hyphens. There is no length limit, since some names run longer than 32 characters. `license` and `compatibility` are now optional header fields. We also wrote down the "load detail only when needed" rule: a skill may add optional `references/`, `scripts/`, and `assets/` folders next to `SKILL.md`, so an agent pulls in detail only when it needs it.
- Matched the version in `nuclear-grade.yaml` to the one in `pyproject.toml` and raised both to 0.3.0.

### Added

- A mission backbone. A lasting repo charter (`.nuclear/charter.md`) lists the named principles for keeping the work honest: ownership, facing facts, raising standards, formality, technical depth, honest reporting, a questioning attitude, evidence over persuasion, rigor that matches the stakes, and discipline about the version everyone agreed is correct (the baseline). It credits its nuclear-culture and Rickover/Navy roots. Each change also gets a `## Mission anchor` in the Standard risk template: the goal, the success test, and what is out of scope. `nuclear-grade init` now writes a starter `.nuclear/charter.md` and `.nuclear/mission.md`. Both are advice, not rules.
- A `staying-on-mission` skill. It spots and fixes drift away from the goal, such as scope creep or swapping in a different goal, with a re-anchor, escalate, or stop decision. It has a counted trigger to escalate: stop after 3 failed tries or a loop.
- A `reviewing-code-quality` skill. It reviews for slipping standards: prefer deleting code over moving it, count the warning signs of needless complexity, make every abstraction earn its place, keep feature logic out of shared layers, and give one clear verdict.
- `ng-drift-check` and `ng-code-review` paste-ready command prompts for those two skills.
- A drift check in the Standard plan template (`## Charter and anchor check`, with a reasons table).
- Advisory checker rules. A mission anchor is checked for goal, success test, and out-of-scope items, but only when a `## Mission anchor` section is present. Open NEEDS-CLARIFICATION markers fail before ship. Both fire only when present, so they break nothing.
- A placeholder marker on every Quick, Standard, CM (keeping the approved version under control), and golden-path template. The checker now rejects any record that still has it, so an untouched template no longer passes.
- The doctor command now requires `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` as public files.

### Removed

- Moved `docs/04-adoption/report-swot-gap-remediation.md` out of the public docs and into the git-ignored `.research/` scratch space. The one link to it in `docs/04-adoption/README.md` is gone now.

## [0.2.0] - 2026-05-27

### Breaking

- The checker now requires every record's `risk.md` to state its mode under a `## Selected mode` section (for example `- **Mode:** Quick` or `- **Mode:** Standard`). Records without this fail the check. Run `python tools/ng.py migrate <packet>` (or `nuclear-grade migrate <packet>` from an installed copy) to add a `## Selected mode` block with a sensible default based on which files are present.

### Added

- `nuclear-grade new --mode cm` and `--mode golden-path` now build all five CM files and all five golden-path files for you, so the manual copy steps in QUICKSTART are no longer needed.
- `nuclear-grade migrate <packet>` adds a `## Selected mode` block to a record whose `risk.md` does not have one yet. It is safe to run more than once. It prints the chosen mode and a one-line note on how to override it.
- Better detection of overclaiming, even when reworded. A tighter pattern catches phrasings like "meets NQA-1 requirements", "fully ASME qualified", "conforms to IEEE 829", "satisfies 10 CFR 50 Appendix B", "implements quality assurance per NQA-1", "audited to NRC standards", and "regulator-approved". It leaves honest boundary wording alone when it sits near words like "inspired by", "influenced by", "does not claim", "no formal", or a paragraph-level disclaimer. It skips fenced code blocks.
- A `_bundled/` snapshot of `templates/`, `skills/`, and `commands/` inside the installed package. The installed tool no longer needs its source-tree neighbors and now works fully from a clean `pip install`.
- A Hatchling build setup with `[tool.hatch.build.targets.wheel.force-include]`, so the resources are bundled at build time without copying them twice in the repo.
- CI now runs on Python 3.11 and 3.12.
- A `ruff` lint step in CI (it selects E, F, I, B, UP; ignores E501).
- A `wheel-smoke` CI job that builds the package, installs it into a clean environment, and runs `init`, `new --mode {quick,standard,cm,golden-path}`, `list`, and `validate` outside the source tree.
- `CITATION.cff` (CFF 1.2) at the repo root.
- `.github/CODEOWNERS` with a maintainer placeholder.

### Fixed

- The README and QUICKSTART now frame the 60-second demo so the expected `FAILED` output reads as the checker catching unfilled prompts on purpose, not as something broken.
- The unfilled-prompt detector no longer cuts off the matched label at 80 characters, so long labels are now caught.
- `docs/03-worked-examples/skill-workflow-comparison/results-summary.md` now opens with a method banner that says the 1-to-5 scores are the author's judgment calls, and it centers the number columns.
- `docs/04-adoption/report-swot-gap-remediation.md` now clearly marks the Files, Skills, and Commands listed under Phases 1 through 4 as planned work, not things that already exist.

### Changed

- The README "What you get" CLI row lists all four `new` modes and the `migrate` command.
- The README "Public v0 status" swaps "validated worked example" for "tested worked example" (file writes stay inside the workspace, checked with pytest) and adds an "author-judged adoption comparison" line.
- `templates/quick/risk.md` now ships with a filled-in `## Selected mode` block (`- **Mode:** Quick`). The standard template already had one.
- `pyproject.toml` raises the version to `0.2.0` and switches the build backend to `hatchling`.

## [0.1.0] - 2026-05-20

### Added

- A standards foundation that is safe about its public sources, plus labels for how settled each source is.
- Quick and Standard record templates.
- A Git-native lifecycle, the modes, the thresholds that turn controls on, change records, briefing packs, token-cost control, and checker guidance.
- A finished Standard-mode worked example for keeping an AI agent's file writes inside its workspace.
- A no-dependencies Python checker for Quick and Standard records: structure, evidence status, source notes, local links, and banned overclaiming phrases.
- Pytest coverage for the checker and the worked-example path guard.
- Public positioning for keeping the approved version under control, plus active CM records.
- A namespaced `nuclear_grade` package entry point for installed console scripts.
- A prompt bank for testing whether skills trigger when they should, compared with a plain baseline.
- An HPI operating doc (small habits from Human Performance Improvement) covering task preview, self-checking, handoff, choosing how to verify, careful decisions, and learning from real operation (OPEX) for AI agents.
- Skills and command prompts for agent handoff, self-checking risky actions, OPEX learning, and trust checks for dependencies, models, and APIs.
- Golden-path templates for handoff and self-check records, plus an active supplier-trust template.
- An agent near-miss issue template.
- Issue templates for bugs and for concerns about docs, method, or source lineage.
- A pull request template with Nuclear-grade verification and overclaiming checks.
- The Contributor Covenant Code of Conduct.
- Cleanup for going public: removed planning scaffolding and stripped internal content from the knowledge-graph usage note.

### Changed

- Reworked the README into a workflow-first landing page for AI builders.
- Made the Public v0 boundaries, source-lineage rules, and non-compliance claims clearer.
- Strengthened every skill's trigger description against skill-author best practices.
- Strengthened briefing packs, verification, release decisions, templates, worked-example comparisons, and source lineage with small HPI controls.

### Not Included

- C-002 external API controls and C-003 human approval gate chains from claim to evidence.
- Rich, automatic checking for active Nuclear, Incident, Research Board, and Release records.
- A production sandbox, a compliance package, or any regulated-use assurance workflow.
