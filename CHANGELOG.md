# Changelog

This file lists every notable change to Nuclear-grade.

These entries record public-facing changes. They do not claim the project is a mature product with strict semantic versions.

## [Unreleased]

### Added

- Codex plugin packaging brought to parity. `.codex-plugin/plugin.json` is now a full Codex manifest — adding the `author` and `interface` objects Codex plugin validation requires (it rejected the prior stub with `author/interface must be an object`), plus `repository`, `keywords`, and install-card display metadata (`displayName`, `developerName`, `category`, `capabilities`, and three short `defaultPrompt`s, each kept under Codex's verified 128-character limit). A repo-side helper, `tools/install-codex.py`, validates the manifest shape and prints the exact Codex install + new-thread/restart steps; the packaging tests assert the schema, the export boundary (skills only — not `agents/`/`commands/`), and the 128-character prompt cap. `INTEGRATIONS.md`, `INSTALL.md`, `README.md`, and `agents/README.md` document what Codex install does and does not cover, including that Codex users still clone the repo for the full workflow, and how it differs from the Claude Code plugin.
- One-command, cross-tool skill distribution. `nuclear-grade install <codex|claude|cursor|windsurf|vscode>` (and `python tools/ng.py install`) places the `SKILL.md` catalog where each tool auto-loads it by description, with `--core` (the `using-nuclear-grade` router + the Core 7) or `--full`, `--scope user|project`, a `--dest` override, and `--dry-run`; it prints the always-on description token cost of what it installed. `install.sh` fans out to every detected tool. Adds `.codex-plugin/plugin.json` so the repo is a publishable Codex plugin, and `INTEGRATIONS.md` documenting the per-tool paths and the CLI-vs-skills-vs-MCP token tradeoff. Claude Code continues to work via the existing plugin marketplace; no hooks are installed.
- Optional MCP server (`nuclear-grade[mcp]` extra; `python -m nuclear_grade.mcp_server`) exposing the existing checks as callable tools — `validate_change_record`, `doctor`, `status`, and `new_change_record` — wrapping the same logic the CLI uses (no shelling out). `nuclear-grade mcp-config <tool>` prints the ready-to-paste server config for each tool. The base install keeps zero runtime dependencies; the server is opt-in because MCP tool schemas load into context every session (~1k tokens/tool) while skills stay leaner.

### Changed

- Gleaned five high-confidence nuclear-leadership practices from two deep-research reports, after an adversarial review filtered out everything the repo already covers deeply or deliberately keeps out of scope, and folded each into the surface that already owns the concept. Charter Art. 19 now distinguishes protected honest error from an accountable willful violation — a knowingly bypassed gate, a disabled control, a fabricated result — reconciling no-blame learning with the no-normalization rule (charter bumped to 1.3.0; `learning-from-experience` and `ng-learn` updated to match). The HPI control stack in `configuration-management.md` now states that defense layers must fail independently (the same model acting and checking itself is one barrier, not two), with graded layering by consequence. `variance-and-drift.md` and `templates/cm/variance.md` gain a discipline for deliberate temporary modifications — feature flags, bypasses, loosened permissions, disabled checks — that stay visible to operators, carry a named back-out, and expire. `authority-and-intent.md` defines competence-to-act (qualification), closing the undefined "train before delegating." Adds `docs/02-operating-system/durable-memory.md`, the persistent counterpart to context-window discipline, with a provenance/poisoning guard. Deferred a leading-indicators metrics doc and a drill template; added no IAEA/WANO/INSAG citations, anchoring every concept to sources already in the map. No new skill, command, or template mode; the manifest is unchanged. Recorded as a dogfooded packet (`.nuclear/changes/glean-nuclear-leadership/`).
- Reworked the `README.md` landing page: led with the PRO/PROVE handle, fixed the runnable quickstart (clone + `cd`, dependency-free `ng.py validate` first, `pytest` second), made the configuration-management value explicit against plain git/CI, and added outcomes from the twelve-scenario comparison study. Softened the subtitle to a method claim ("stay in control of what ships") and updated the banner SVG to match. Reconciled the headline path to `question -> specify -> execute -> verify -> decide -> baseline -> operate -> learn` across `README.md`, `WORKFLOWS.md`, and `docs/diagrams.md`, unfolding the everyday loop from seven to eight control points so Learn is a named step alongside Baseline. Trimmed em-dash density on the landing page.
- Folded generic, tool-agnostic planning lessons from an external multi-repo review into existing controls, declining the tool-specific mechanics on the record. `questioning-attitude` now classifies the work type (greenfield/brownfield/defect-fix/refactor-migration) at the front door, orthogonal to the rigor modes; `checking-what-a-change-affects` and the CM change-impact template screen runtime/data blast radius (schema/state, API consumers, backward-compatibility, rollback-of-state); the Standard plan build sequence gains delegable handoff-slice columns (prerequisites, per-slice proof, stop/done condition) mirrored in `breaking-down-the-work`; and `docs/04-adoption/agent-authority-model.md` names the read-only plan phase versus the write-enabled build phase. Adds `docs/02-operating-system/work-type-lens.md`; command prompts and skill-evaluation prompts updated to match. No new always-on skill, template, or command, and the manifest is unchanged. Recorded as a dogfooded packet (`.nuclear/changes/incorporate-planning-lessons/`). (#26)
- Tightened the `README.md` landing page without removing content or diagrams. Consolidated the Contents from 21 sections to 17: merged "Pick how much you want" + "Which change record do I need?" into "Adopt at your pace", folded the repo map into "What you get", and combined community, sources, and author into one closing block — while keeping "What this is NOT" and "License and limits" as their own prominent sections. Reframed PRO / PROVE / the eleven-beat path as one path at three zoom levels and trimmed the repeated path narration; kept HPI and the Core 7 as pointers to `WORKFLOWS.md` / `CORE.md` rather than headline frameworks. Removed the stale "(v0)" framing and the brittle skill/command counts, and added a teaching-example boundary note to the worked-example walkthrough. Diagram text equivalents preserved for screen-reader and non-rendering (PyPI) readers.

## [0.5.0] - 2026-06-04

### Added

- Navy-nuclear leadership and high-reliability guide (`docs/01-field-guide/leadership-and-high-reliability.md`), translating Naval Reactors discipline and intent-based leadership into how people and agents run the work — concept lineage only, no program claim. (#19)

### Changed

- Reframed the core loop as seven control points in `WORKFLOWS.md`. Each step (`Question`, `Specify`, `Execute`, `Verify`, `Decide`, `Save approved version`, `Operate`) is now tabled with the failure mode it stops, the artifact it produces, and the abort condition for proceeding. A skipped step is now a named failure mode you chose to accept, not an unstated shortcut. The everyday seven-step form is reconciled with the full eleven-beat path used for standard and high-consequence work.
- `README.md` keeps the canonical eleven-step path and original lifecycle diagram, with one new sentence introducing the control-point treatment and pointing to `WORKFLOWS.md` for the detail. No simplified-vs-full duplication on the landing page.
- Restructured the adoption surface around the CORE habits, a decision matrix, and starter kits, so a team can pick the right kit by trigger (`CORE.md`, `starter-kit/`). (#21)
- Sharpened requirements discipline across the change templates. (#22)
- Recorded the token-audit follow-up decisions (#14): keep all four overlap clusters as separate skills and keep the per-file assurance disclaimer; the optional body cuts and the `core-source-rationale.md` relocation are deferred as evidence-triggered. (#23)
- Set the repository code owners (`CODEOWNERS`) and citation author (`CITATION.cff`) to `@FlyFission`. (#23)

### Fixed

- Corrected a CRLF token miscount and refreshed the token-audit baseline for current `main`. (#18)

## [0.4.0] - 2026-05-31

### Breaking

- Plain-language rename of skill and command IDs. The skill folder names and the words you type to invoke them have changed, so any saved prompt, script, or note that calls a skill or command by its old name must be updated. Nothing inside the methodology changed -- same controls, same rigor, same detail -- only the names are now plainer and easier to read. There is no automatic migration; update old references by hand using the map below.

  Skills renamed (18):

  | Old name | New name |
  | --- | --- |
  | `identifying-controlled-items` | `choosing-what-to-control` |
  | `screening-change-impact` | `checking-what-a-change-affects` |
  | `baselining-configuration` | `recording-a-known-good-version` |
  | `classifying-change-risk` | `rating-change-risk` |
  | `creating-change-packets` | `creating-change-records` |
  | `packing-agent-context` | `briefing-an-agent` |
  | `turning-over-agent-work` | `handing-off-work` |
  | `self-checking-agent-actions` | `double-checking-before-acting` |
  | `reviewing-ship-readiness` | `checking-release-readiness` |
  | `learning-from-opex` | `learning-from-experience` |
  | `checking-dependency-and-model-trust` | `vetting-outside-code-and-models` |
  | `checking-source-lineage` | `checking-source-claims` |
  | `checking-license-and-assurance-boundaries` | `checking-legal-and-safety-wording` |
  | `controlling-mission-drift` | `staying-on-mission` |
  | `red-teaming-agent-changes` | `stress-testing-agent-changes` |
  | `tracing-agent-execution` | `recording-what-an-agent-did` |
  | `decomposing-work-breakdown` | `breaking-down-the-work` |
  | `structuring-agentic-folders` | `organizing-project-folders` |

  Commands renamed (3): `ng-cm-items` -> `ng-what-to-control`, `ng-opex` -> `ng-learn`, `ng-wbs` -> `ng-breakdown`.

  Kept as-is because they were already plain: `questioning-attitude`, `using-nuclear-grade`, `proving-claims`, `reviewing-code-quality`. The `closing-stale-packets` skill and `ng-close-packet` command also keep their names, on purpose: the tool itself still calls a change record a "packet" (for example `ng status` prints `N packet(s) need attention`), so renaming only this skill would be the one piece out of step with the rest of the tool.

### Changed

- Lowered the reading level across the repo. Skill titles, descriptions, and supporting docs were rewritten in plainer prose without dropping any rigor or detail. Every test-frozen string was preserved.

### Added

- Token-cost audit and budget gate. `nuclear-grade tokens` (and `python tools/ng.py tokens`) measures the token weight of the repo's own prose surfaces -- separating a skill's always-loaded `description` cost from its on-invocation body cost -- reports a redundancy index, the assurance-disclaimer phrase frequency, and tokens-per-decision-signal (via the efficacy harness), and exits non-zero when a file exceeds the per-file budgets in `nuclear-grade.yaml` (`token_budgets:`). The counter is deterministic and stdlib-only (no new runtime dependency); CI runs it after `doctor`. It measures token cost and repetition only -- not correctness, safety, or compliance. See `docs/05-reference/skills-token-audit.md` for the measured baseline.
- `closing-stale-packets` skill and `ng-close-packet` command. Pairs with the `ng status` health tags: when a packet is flagged `scaffold` or `invalid`, this brings it to an honest terminal state -- completed (filled and validating), closed (deliberately abandoned with a recorded rationale), or deleted (never a real change). Closing with a written reason is a first-class successful outcome; the forbidden state is half-done and silent. Wired into the catalog, skill index, evaluation prompts, and contract tests.
- `ng status` gains a `closed` terminal state. A packet deliberately abandoned with a `NUCLEAR-GRADE-CLOSED:` rationale marker is reported as `closed` and no longer counted toward the "needs attention" reminder, so honestly closed packets are not nagged while half-filled drafts still are. The marker constant lives next to `PLACEHOLDER_MARKER` in `ng_validate`.
- Reproducible efficacy harness. `nuclear-grade eval` (and `python tools/ng.py eval`) mechanically checks that each worked-example artifact still surfaces the decision signals the methodology claims it teaches, exiting non-zero if a worked example drops a required signal. Eval cases live as plain JSON in `evals/cases/`; the harness is stdlib-only (no new runtime dependency). It measures presence of named decision elements, not engineering correctness, safety, or compliance; see `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md`. The simple-prompt-versus-Nuclear-grade comparison stays qualitative and is deliberately not mechanized.
- `nuclear-grade status` now tags each packet `ok`, `scaffold` (an untouched draft still carrying the placeholder marker), or `invalid`, and prints a reminder when any packet needs attention, so abandoned half-filled drafts are visible rather than silent.
- Workflow diagrams (`docs/diagrams.md`), a plain-language glossary (`docs/glossary.md`), and an agent threat model (`docs/02-operating-system/agent-threat-model.md`).

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
