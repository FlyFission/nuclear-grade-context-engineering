# Report SWOT, Gap Analysis, and Remediation Plan

**Purpose:** Compare Nuclear-grade against the downloaded report, "Nuclear-Inspired Agent Skills for Software Development," and against current public surfaces of adjacent agent-skill and agent-workflow repos. This is a product-readiness audit, not a claim of external standard conformance.

**Date:** 2026-05-23

**Research inputs reviewed:**

- Maintainer-supplied Markdown research report.
- Maintainer-supplied DOCX research report.
- Current repository files under `FlyFission/nuclear-grade-context-engineering`

**External public surfaces inspected:**

- Superpowers: https://github.com/obra/superpowers
- Addy Osmani agent-skills: https://github.com/addyosmani/agent-skills
- Matt Pocock skills: https://github.com/mattpocock/skills
- Continue: https://github.com/continuedev/continue
- Cline: https://github.com/cline/cline
- browser-use: https://github.com/browser-use/browser-use
- Aider: https://github.com/aider-ai/aider
- OpenHands: https://github.com/OpenHands/OpenHands

## Executive Diagnosis

The report's central claim is that a successful repo in this space should not be a bag of prompts. It should be a visible, repeatable development operating system with intake, specification, risk scaling, test-first execution, independent verification, configuration control, evidence packaging, and disciplined closure.

Nuclear-grade already has a distinctive and defensible core: configuration management for AI-assisted work. It has Quick/Standard packets, CM templates, boundary language, skills, command cards, a CLI, a validator, and one worked example. That is materially stronger than a generic prompt pack.

The gap is that the repo still reads more like a rigorous method library than an immediately demoable operating system. It needs a short golden path, more explicit evidence-producing artifacts, better trace/scenario/TDD primitives, CI-visible checks, first-class installation/adaptation paths, and more examples.

The best positioning is not to abandon configuration management. It is to sharpen it:

```text
Configuration management and evidence gates for AI-assisted software work.
```

This keeps the repo differentiated while absorbing the report's strongest recommendation: make the output visible as evidence bundles, not just docs.

## SWOT Analysis

### Strengths

| Strength | Evidence in repo | Why it matters |
|---|---|---|
| Clear differentiated thesis | `README.md` says "Configuration management for AI-assisted software work." | This is more specific than generic "senior engineer skills" positioning. |
| Real artifact model | `.nuclear/changes/<slug>/`, Quick packets, Standard packets, CM records | Reviewers can inspect durable records instead of relying on chat history. |
| Strong boundary discipline | `DISCLAIMER.md`, source-lineage docs, public-doc tests, command/skill boundary notes | The repo avoids implying formal compliance or regulated adequacy. |
| Git-native and lightweight | Markdown templates plus local Python CLI | Low adoption friction for teams that already work in PRs. |
| Config management backbone | `templates/cm/`, `docs/02-operating-system/configuration-management.md`, CM skills and commands | This is the repo's most original wedge. |
| Machine-checkable contracts | skill/command contract tests, packet validator, doctor command | The repo already has more executable discipline than many doc-only skill repos. |
| Public source foundation | source map, crosswalk, compliance boundaries | Helps defend "inspired by" language without overclaiming. |

### Weaknesses

| Weakness | Evidence in repo | Product consequence |
|---|---|---|
| No single golden-path demo | README has core workflow and commands, but not a compact artifact-producing chain | First-time users do not instantly see the full before/after delta. |
| Missing report's top-six primitives | No first-class intake, CAE spec, BDD scenario authoring, traceability matrix, TDD executor, independent verifier skills | The repo is strongest at CM, weaker at feature-delivery workflow. |
| Evidence bundle is implicit | Packets exist, but "evidence bundle" is not a named product surface | Harder to share, demo, and make memetic. |
| CI enforcement is thin | Validator checks packet shape, not trace completeness, hold points, evidence coverage, or link integrity | Continue-style team adoption is underdeveloped. |
| Integration story is mostly generic | Portable prompts exist, but no first-class harness pages for Claude Code, Codex, Cline/Cursor, Continue, etc. | The repo is portable in principle but not yet frictionless in practice. |
| Worked examples are sparse | One flagship worked example | The repo cannot yet show pattern transfer across API, frontend, dependency/tool, and release scenarios. |
| Community/social proof is absent | No testimonials, public PR examples, demo clips, or adoption metrics | Lower viral pull and less immediate trust. |
| Some docs are concept-dense | Strong source foundation, but many files read as internal method docs | Public readers may not quickly identify the first useful action. |

### Opportunities

| Opportunity | How to exploit it |
|---|---|
| Own the "AI configuration control" lane | Emphasize prompts, models, tools, context packs, dependencies, permissions, evals, and release records as controlled items. |
| Make evidence bundles shareable | Add `evidence-bundle.md`, `ng evidence`, and example bundles that users can copy into PRs. |
| Borrow the report's golden path | Add `Intake -> Spec -> Scenarios -> Trace -> TDD -> Independent Verify -> Evidence Bundle -> Ship` as a public workflow chain. |
| CI as the adoption bridge | Add GitHub Actions examples and validators that fail orphan requirements, missing evidence statuses, and broken packet links. |
| Starter kits | Create API, frontend, and dependency/tool worked examples that show the same discipline across different work. |
| Harness adapters | Provide install/adaptation guides for Codex, Claude Code, Cursor/Cline, Continue checks, Gemini/OpenCode as plain Markdown. |
| Team lead audience | Position as a PR/release governance tool for teams using coding agents, not only as personal agent skills. |

### Threats

| Threat | Why it matters | Mitigation |
|---|---|---|
| Generic skill repos absorb attention | Superpowers, Addy, and Matt Pocock have clearer install loops and larger audiences | Narrow the wedge: CM plus evidence gates for agentic change control. |
| Over-complexity turns users away | Nuclear language can sound heavy or performative | Keep Quick path tiny and make activation thresholds obvious. |
| Regulatory misunderstanding | Readers may infer more assurance than the repo grants | Preserve explicit boundary language and avoid regulated-use claims. |
| Evidence fabrication by agents | Agents can write confident but unsupported proof | Prefer command-generated evidence, CI checks, and independent verification records. |
| Integration fragmentation | Each agent harness handles skills/rules/plugins differently | Treat adapters as docs plus tested install recipes, not a monolithic integration. |
| Security concerns around skills | Skill ecosystems have prompt-injection and tool-authority risks | Add secure-boundary, supplier/dependency qualification, and permission logs. |

## Top-Down Gap Analysis

### 1. Positioning and Promise

**Report ideal:** One-line clarity plus a concrete product promise: a nuclear-inspired QA discipline for agent-assisted software development.

**Repo state:** Strong but narrower: configuration management for AI-assisted software work.

**Gap:** The current promise is precise, but it does not yet expose the user's felt outcome: turning AI-coded changes into reviewable evidence bundles.

**Recommended public promise:**

```text
Configuration management and evidence gates for AI-assisted software work.
```

**README hook to add:**

```text
Turn an AI-coded change into a packet reviewers can trust:
questioning attitude, specification/design basis, scenarios, traceability, verification, decision, and baseline.
```

### 2. First-Run Activation

**Comparator pattern:** Matt Pocock has a 30-second setup. browser-use has one-line install plus doctor/setup commands. Addy has marketplace and multi-agent setup instructions. Continue starts with a pasteable prompt and then makes checks visible in PR status.

**Repo state:** README has a 60-second command path using `python tools/ng.py`.

**Gap:** The current first run proves the CLI exists, but it does not generate the report's recommended artifact chain. The user sees a packet skeleton, not the full value.

**Remediation:** Add a one-command or two-command "golden path demo" that scaffolds a sample evidence bundle from a tiny example.

### 3. Golden Path Workflow

**Report ideal:**

```text
Hazard-Scoped Intake -> Claim-Argument-Evidence Spec -> Acceptance Scenarios
-> Traceability Matrix -> Red-Green-Refactor -> Independent Verifier
-> Evidence Bundle + PR Gate
```

**Repo state:**

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

**Gap:** The repo lifecycle is more complete, but the report's chain is more teachable and demoable. Nuclear-grade needs both:

- lifecycle for doctrine;
- golden path for adoption.

**Remediation:** Add `docs/02-operating-system/golden-path.md` and summarize it in README/WORKFLOWS.

### 4. Skill Architecture

**Report ideal:** Twelve workflow primitives, with top six creating the quality signature.

**Repo state:** Eleven skills, strongest around CM, risk classification, packet creation, context packs, proof, ship readiness, source/legal boundaries.

**Top-six gap:**

| Report skill | Current equivalent | Gap |
|---|---|---|
| Hazard-Scoped Intake | partial: `classifying-change-risk`, `using-nuclear-grade` | No dedicated intake artifact with assumptions, hazards, impacted components, and hold points. |
| Claim-Argument-Evidence Spec | partial: `proving-claims`, `basis.md` | No CAE spec template that precedes implementation. |
| Acceptance Scenario Author | missing | No BDD/Given-When-Then skill or scenario template. |
| Traceability Matrix Builder | partial: `trace.md` | No matrix artifact linking requirement -> scenario -> test -> code -> evidence. |
| Red-Green-Refactor Executor | missing | No skill preserving TDD red/green evidence. |
| Independent Verifier | partial: ship/review language | No separate verifier role or independent-review record. |

**Remediation:** Add the top-six skills before adding lower-priority extras.

### 5. Templates and Records

**Report ideal:** `INTAKE.md`, `FEATURE_SPEC.md`, `SCENARIOS.feature`, `traceability.yaml/csv`, `BASELINE_MANIFEST.json`, `EVIDENCE_BUNDLE.md`, hold-point records, qualification records, RCA records.

**Repo state:** Quick, Standard, and CM templates exist. No scenario, traceability matrix, evidence bundle, baseline manifest JSON, hold-point, dependency qualification, or RCA templates.

**Gap:** Existing records answer "what is the packet?" but not yet "how does this become a feature-delivery operating system?"

**Remediation:** Add `templates/golden-path/` or activate these as optional records under `templates/advanced/`:

- `intake.md`
- `spec.md`
- `scenarios.md`
- `traceability.yaml`
- `evidence-bundle.md`
- `independent-review.md`
- `hold-points.md`
- `qualification.md`
- `corrective-action.md`

### 6. CLI and Validator

**Comparator pattern:** Continue makes checks source-controlled and PR-visible. browser-use ships doctor/setup/template commands. Aider integrates with git and commits. Superpowers enforces verification-before-completion as a workflow rule.

**Repo state:** CLI supports `init`, `new`, `validate`, `doctor`, `list`, and `status`. Validator checks Quick/Standard structure and boundary phrases.

**Gap:** The CLI validates form, not enough relationships. It does not assemble evidence bundles, validate trace completeness, or emit CI-ready outputs.

**Remediation:**

- Add `ng evidence <packet>` to assemble a reviewer-facing evidence bundle.
- Add `ng check-links` for public docs and packet links.
- Add `ng trace-check <packet>` for claim/evidence linkage.
- Add GitHub Action examples.

### 7. Examples and Demos

**Comparator pattern:** browser-use shows concrete demos, templates, and example tasks. Microsoft learning repos scale through lessons/translations. Aider uses social proof and real-world testimonials.

**Repo state:** One worked example for AI-agent workspace-only file writes.

**Gap:** One example proves depth but not transferability.

**Remediation:** Add three starter examples:

1. `api-service-change`: user-visible endpoint with spec/scenarios/trace/tests.
2. `frontend-feature-change`: UI behavior with acceptance scenarios and screenshots/evidence.
3. `dependency-tool-introduction`: library/model/MCP/tool addition with qualification, boundary, rollback, and baseline.

### 8. Integration and Portability

**Comparator pattern:** Superpowers documents multiple harness installs. Addy documents Claude, Cursor, Gemini, Windsurf, OpenCode, Copilot, Kiro, Codex/other agents. Cline exposes CLI, IDE, SDK, plugins, and teams.

**Repo state:** Command cards are portable Markdown. Install docs are repo-local Python focused.

**Gap:** Portability is asserted but not packaged as first-class adoption paths.

**Remediation:** Add `docs/04-adoption/integrations/`:

- `codex.md`
- `claude-code.md`
- `cursor-cline.md`
- `continue.md`
- `generic-agent.md`

### 9. Community and Growth Surface

**Report ideal:** Social proof, support community, starter kits, visible metrics, contribution loops.

**Repo state:** Contribution, support, governance, and code-of-conduct files exist. No social proof, demos, public examples, issue labels, community call, or metric loop.

**Gap:** Public scaffolding exists, but growth mechanics are not yet designed.

**Remediation:** Add:

- issue templates for example requests and adapter requests;
- a "share your evidence bundle" section;
- curated examples table;
- roadmap metrics for activation, evidence-bundle completion, CI-gate usage, and contributed adapters.

## Bottom-Up Gap Analysis by Repo Surface

### README.md

**Current appropriateness:** B+

**What works:**

- Strong one-line thesis.
- Quick commands are visible.
- Clear "what this is not" boundary.
- Good repo map and status.

**Gaps against report/comparators:**

- No named "golden path" in the first screen.
- No before/after artifact tree.
- No screenshots, diagrams, demo output, or evidence bundle sample.
- No adapter/install matrix like Superpowers/Addy.
- No social proof or concrete "real PR" narrative like Aider.

**Remediation:**

- Add a 6-line golden path and generated artifact tree above or near "What you get."
- Rename or supplement "Try it in 60 seconds" with "Create your first evidence bundle."
- Add one Mermaid workflow diagram or simple text diagram.

### INSTALL.md and QUICKSTART.md

**Current appropriateness:** B-

**What works:**

- Local CLI is simple.
- Boundary language is explicit.
- Manual fallback exists.

**Gaps:**

- No first-class install paths for agent harnesses.
- No `pipx`, `uvx`, or packaged CLI path yet.
- First run does not guide a user into a real artifact chain.

**Remediation:**

- Add "Repo-local," "editable Python," and "agent prompt only" install lanes.
- Add a future `pipx`/`uvx` lane only when packaging is ready.
- Link to integration guides.

### WORKFLOWS.md

**Current appropriateness:** B

**What works:**

- Clear workflow catalog.
- CM loop is now explicit.
- Source/legal and agent authority workflows are useful.

**Gaps:**

- The report's feature-delivery and dependency-introduction chains are not first-class.
- No hold-point decision model.
- No evidence bundle endpoint.

**Remediation:**

- Add "Golden path feature delivery."
- Add "Dependency/tool introduction."
- Add "Incident/corrective-action loop."

### SKILLS.md and skills/

**Current appropriateness:** B-

**What works:**

- Skills have consistent contracts.
- CM skills are distinctive.
- Red flags and rationalizations are valuable.

**Gaps:**

- Missing report's top-six quality-signature skills.
- Existing skills are more review/CM oriented than build-flow oriented.
- Skills do not include harness-specific trigger metadata beyond generic descriptions.

**Remediation priority:**

1. `hazard-scoped-intake`
2. `claim-argument-evidence-spec`
3. `acceptance-scenario-author`
4. `traceability-matrix-builder`
5. `red-green-refactor-executor`
6. `independent-verifier`

### COMMANDS.md and commands/

**Current appropriateness:** B

**What works:**

- Prompt cards are portable.
- Commands map well to existing packet operations.

**Gaps:**

- No `/spec`, `/scenario`, `/trace`, `/evidence`, `/verify-independent`, or `/hold-point` equivalents.
- Existing commands are not grouped into lifecycle chains.

**Remediation:**

- Add command cards for the top-six skills.
- Add a command chain table: "Feature delivery," "Dependency introduction," "Release readiness."

### templates/

**Current appropriateness:** B

**What works:**

- Quick/Standard/CM records are coherent.
- CM records are a real differentiator.

**Gaps:**

- No scenario/traceability/evidence-bundle/hold-point/qualification/RCA templates.
- No machine-readable schema for traceability or baseline manifest.

**Remediation:**

- Add optional `templates/golden-path/`.
- Add JSON/YAML schemas for traceability and baseline manifest after Markdown templates stabilize.

### tools/ and nuclear_grade/

**Current appropriateness:** B-

**What works:**

- Namespaced package exists.
- Doctor/list/status/new/validate provide a useful local spine.
- Tests guard basic contracts.

**Gaps:**

- Validator is mostly structural.
- No CI-friendly JSON output.
- No evidence-bundle builder.
- No link checker.
- No trace matrix checker.

**Remediation:**

- Add `--json` output to `doctor`, `status`, and `validate`.
- Add `evidence`, `trace-check`, and `check-links` subcommands.
- Add GitHub Actions examples under `.github/workflows/` or docs.

### docs/00 and docs/01 source foundation

**Current appropriateness:** A-

**What works:**

- Strong boundary discipline.
- Public source lineage is unusually careful.

**Gaps:**

- The source foundation can feel heavier than the product.
- It is not yet tied tightly enough to the new golden path artifacts.

**Remediation:**

- Add short "Use these concepts, avoid these claims" summary.
- Add a source-to-artifact map: graded approach -> risk, design control -> spec, CM -> baseline, independent review -> verifier, OPEX -> learn.

### docs/02 operating system

**Current appropriateness:** B+

**What works:**

- Lifecycle, modes, packets, context packs, validators, CM docs are strong.

**Gaps:**

- No `golden-path.md`.
- No `evidence-bundles.md`.
- No `traceability-matrices.md`.
- No `hold-points.md`.
- No `supplier-and-dependency-qualification.md`.
- No `corrective-action.md`.

**Remediation:**

- Add the missing operating-system docs in the same concise style as CM docs.

### docs/03 worked examples

**Current appropriateness:** C+

**What works:**

- The first example is well chosen and relevant.
- It demonstrates agent authority boundary proof.

**Gaps:**

- Only one example.
- The example does not yet show full golden-path artifacts.
- No API/frontend/dependency examples.

**Remediation:**

- Upgrade current example to include intake/spec/scenarios/traceability/evidence bundle.
- Add two more examples before any loud public launch.

### docs/04 adoption

**Current appropriateness:** C+

**What works:**

- Enterprise rollout, agent authority, and reviewer playbook exist.

**Gaps:**

- No integration guides.
- No community or metrics guide.
- No "team CI adoption" recipe with copy-paste workflow.

**Remediation:**

- Add `integrations/`.
- Add `ci-adoption.md`.
- Add `community-and-metrics.md`.

### .github/ and project metadata

**Current appropriateness:** B

**What works:**

- PR template asks for packets, verification, CM updates, and boundary checks.
- CI badge is present.

**Gaps:**

- PR template does not yet ask for scenarios, traceability matrix, evidence bundle, or independent verification.
- No issue template for adapter/example requests.
- No starter GitHub Action documented for downstream users.

**Remediation:**

- Update PR template after new artifacts exist.
- Add issue templates for examples, adapters, methodology gaps, and evidence-bundle showcase.

## Most Applicable Use Cases

### Best-fit use cases now

| Use case | Why Nuclear-grade is already strong |
|---|---|
| AI-agent authority changes | Context packs, authority docs, packet model, verification, and ship review already fit. |
| Prompt/model/tool configuration changes | CM controlled-item logic maps naturally to prompts, models, tools, evals, and context packs. |
| Dependency or MCP/tool introduction | CM and impact records are strong, though qualification templates are missing. |
| Public docs with assurance-adjacent language | Source-lineage and boundary checks are strong. |
| Release readiness reviews | `ship.md`, reviewer playbook, and release decision language are already useful. |
| Team pilot for AI-assisted PR discipline | Packets plus PR template give teams a lightweight governance path. |

### High-potential use cases after remediation

| Use case | Needed remediation |
|---|---|
| Feature delivery from vague request to PR | Add intake, CAE spec, scenarios, traceability, TDD, independent verifier, evidence bundle. |
| CI-enforced AI change governance | Add trace/evidence/hold-point validators and GitHub Action recipe. |
| Dependency/model/MCP governance | Add supplier/dependency qualification skill/template and baseline manifest. |
| Incident and recurrence prevention | Add corrective-action manager, RCA template, and OPEX-to-test loop. |
| Cross-harness skill adoption | Add integration guides and install recipes. |
| Viral public demo | Add starter kits and visible before/after artifacts. |

### Poor-fit or explicitly excluded use cases

| Use case | Why not |
|---|---|
| Formal regulated QA program out of the box | The repo is public-source-inspired workflow tooling, not a qualified external program. |
| Safety/security certification | The repo can organize evidence but does not certify adequacy. |
| Generic "make my agent code better" prompt pack | The repo's advantage is controlled change governance, not broad coding tips. |
| Heavyweight process for trivial edits | Quick mode should stay tiny; overuse would damage adoption. |

## Comparator Appropriateness Matrix

| Dimension | Superpowers | Addy agent-skills | Matt Pocock skills | Continue | Cline | browser-use | Aider | Nuclear-grade current | Target |
|---|---|---|---|---|---|---|---|---|---|
| One-line promise | Very strong | Strong | Strong/personality-led | Very strong | Strong | Strong/demo-led | Strong | Strong but narrow | Strong plus artifact outcome |
| Install friction | Very low, many harnesses | Low, many harnesses | Very low via skills.sh | Low CLI | Low product installs | Low CLI/templates | Mature CLI | Repo-local Python | Multi-lane install/adapt |
| Golden path | Strong methodology | Lifecycle commands | Small composable workflows | PR checks | Plan/Act | Demo workflows | Git edit/commit loop | Broad lifecycle | Explicit golden path chain |
| Machine checks | Workflow/process checks | Quality gates | Mostly skill-driven | Core differentiator | Product approvals/hooks | Doctor/setup | Git commits/tests | Basic validator/tests | Trace/evidence/hold-point CI |
| Examples/demos | Good | Good | Personal examples | Check examples | Product demos | Excellent | Social proof | One worked example | Three starter kits |
| Portability | Excellent | Excellent | Good | CI/editor | Product platform | Skill plus CLI | CLI/product | Markdown portable | First-class adapters |
| Community proof | Very strong | Strong creator credibility | Strong creator audience | Product adoption | Product community | Demos/cloud | Testimonials | None yet | Evidence-sharing loop |
| Safety boundaries | Strong process | Quality gate language | Practical/human | CI governance | Approval model | API key/session docs | Git auditability | Very strong legal/source boundaries | Keep strength, add execution-boundary artifacts |

## Remediation Plan

### Phase 0: Public Surface Reframe

**Goal:** Make the repo's value legible in the first screen.

**Files to update:**

- `README.md`
- `WORKFLOWS.md`
- `QUICKSTART.md`
- `docs/README.md`
- `ROADMAP.md`

**Changes:**

- Add tagline: "Configuration management and evidence gates for AI-assisted software work."
- Add "Golden path" section:

```text
Intake -> Spec -> Scenarios -> Trace -> Build/Test -> Independent Verify -> Evidence Bundle -> Ship
```

- Add before/after artifact tree:

```text
Before: prompt -> diff -> test output -> persuasive PR
After: intake -> basis/spec -> scenarios -> traceability -> verification -> evidence bundle -> baseline/ship
```

- Add "best first use cases" section: agent authority, dependency/tool introduction, release readiness, prompt/model/config change.

**Exit criteria:**

- A new reader can say what the repo produces in one sentence.
- README points to one full demo path, not just a command list.

### Phase 1: Golden-Path Artifacts

**Goal:** Add the report's missing quality-signature outputs without bloating Standard packets by default.

**Files to create:**

- `docs/02-operating-system/golden-path.md`
- `docs/02-operating-system/evidence-bundles.md`
- `docs/02-operating-system/traceability-matrices.md`
- `docs/02-operating-system/hold-points.md`
- `templates/golden-path/intake.md`
- `templates/golden-path/spec.md`
- `templates/golden-path/scenarios.md`
- `templates/golden-path/traceability.yaml`
- `templates/golden-path/evidence-bundle.md`
- `templates/golden-path/independent-review.md`
- `templates/golden-path/hold-points.md`

**Files to modify:**

- `templates/README.md`
- `nuclear-grade.yaml`
- `tests/test_ng_cli.py`

**Exit criteria:**

- `python tools/ng.py list` shows golden-path artifacts.
- Doctor checks required golden-path templates exist.

### Phase 2: Top-Six Skills and Commands

**Goal:** Close the biggest gap against the report's recommended skill set.

**Skills to add:**

- `skills/hazard-scoped-intake/SKILL.md`
- `skills/claim-argument-evidence-spec/SKILL.md`
- `skills/acceptance-scenario-author/SKILL.md`
- `skills/traceability-matrix-builder/SKILL.md`
- `skills/red-green-refactor-executor/SKILL.md`
- `skills/independent-verifier/SKILL.md`

**Commands to add:**

- `commands/ng-intake.md`
- `commands/ng-spec.md`
- `commands/ng-scenarios.md`
- `commands/ng-trace.md`
- `commands/ng-tdd.md`
- `commands/ng-independent-review.md`

**Tests to update:**

- `tests/test_skill_contracts.py`
- `tests/test_command_contracts.py`

**Exit criteria:**

- Skill/command contract tests pass.
- README and WORKFLOWS show how the skills chain together.

### Phase 3: Evidence and CI Tooling

**Goal:** Turn packets from structured records into CI-visible checks.

**CLI additions:**

- `python tools/ng.py evidence <packet>`
- `python tools/ng.py trace-check <packet>`
- `python tools/ng.py check-links .`
- `--json` for `doctor`, `status`, and `validate`

**Potential test files:**

- `tests/test_ng_evidence.py`
- `tests/test_ng_trace_check.py`
- `tests/test_doc_links.py`

**Docs to add:**

- `docs/04-adoption/ci-adoption.md`
- `.github/workflows/nuclear-grade-example.yml` or documented downstream workflow snippet

**Exit criteria:**

- CI can fail a packet with orphan claims, missing evidence status, or broken local links.
- Evidence bundle command emits a stable Markdown artifact.

### Phase 4: Starter Kits and Worked Examples

**Goal:** Show transferability across common engineering surfaces.

**Examples to add:**

- `docs/03-worked-examples/api-service-change/`
- `docs/03-worked-examples/frontend-feature-change/`
- `docs/03-worked-examples/dependency-tool-introduction/`

**Current example upgrade:**

- Add intake/spec/scenarios/traceability/evidence-bundle records to `ai-agent-tool-permissions`.

**Exit criteria:**

- Each example has runnable verification.
- Each example validates its packet.
- README links directly to the examples.

### Phase 5: Integration Guides

**Goal:** Make portability practical.

**Files to create:**

- `docs/04-adoption/integrations/codex.md`
- `docs/04-adoption/integrations/claude-code.md`
- `docs/04-adoption/integrations/cursor-cline.md`
- `docs/04-adoption/integrations/continue.md`
- `docs/04-adoption/integrations/generic-agent.md`

**Exit criteria:**

- A user can adapt at least three skills and three command prompts into their agent harness in under ten minutes.
- README has an integration table.

### Phase 6: Growth and Community Loop

**Goal:** Design for adoption without overclaiming.

**Files to create or modify:**

- `docs/04-adoption/community-and-metrics.md`
- `.github/ISSUE_TEMPLATE/example-request.yml`
- `.github/ISSUE_TEMPLATE/adapter-request.yml`
- `.github/ISSUE_TEMPLATE/evidence-bundle-showcase.yml`
- `ROADMAP.md`

**Metrics to track:**

- install-to-first-packet completion;
- evidence bundle completion;
- packet validation success rate;
- CI gate adoption;
- contributed adapters/examples;
- recurring issue themes that trigger OPEX updates.

**Exit criteria:**

- The repo has a credible contribution loop for examples, adapters, and evidence bundles.

## Recommended Execution Order

1. Public surface reframe.
2. Golden-path docs/templates.
3. Top-six skills/commands.
4. CLI evidence/trace/link tooling.
5. Worked examples.
6. Integration guides.
7. Community/metrics loop.

Do not add all twelve report skills at once. Add the top six first, then use real example friction to decide whether hold points, supplier qualification, corrective action, OPEX harvesting, and secure execution boundary need separate skills or can remain docs/templates.

## Source-Lineage and Boundary Note

This audit translates a local research report and public repo observations into product-readiness recommendations for Nuclear-grade. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory adequacy.
