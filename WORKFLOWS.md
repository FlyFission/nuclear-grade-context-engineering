# Nuclear-grade Workflows

Nuclear-grade turns AI-assisted software work into something you have questioned, kept under control, and can review.

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> baseline -> operate -> learn
```

A "baseline" (the saved approved version) is the version everyone agreed is correct.

## The core loop: eight control points

Each step is a control point. Each one stops one specific failure mode. Skip any of them and you ship a different kind of risk.

| # | Step | Stops | Produces | Abort if |
|---|---|---|---|---|
| 1 | **Question** — frame the decision before code moves | Solving the wrong problem, confidently | The fact that would change your mind | No answer would change what you do |
| 2 | **Specify** — write what must be true and what must not break | Shifting goalposts; reviewers guessing intent from the diff | Intent, boundary, must-not-break list | The spec cannot be falsified |
| 3 | **Execute** — build inside the boundary; agents work here, not before | Scope drift, surprise blast radius, silent dependency changes | The diff and the trace from spec to change | A step crosses the boundary without escalation |
| 4 | **Verify** — test the claim against reality, not against confidence | Green-tests-but-wrong-feature; persuasion over proof | Evidence, named gaps, what was not tested | The evidence does not address the spec |
| 5 | **Decide** — ship, defer, or stop, on purpose and on the record | Silent merges; evidence-shaped PRs with no decision | A decision with reasoning, leftover risk, rollback, monitoring | Nobody owns the decision |
| 6 | **Baseline** — lock the approved version everyone agreed on | Drift; "the prompt changed and nobody knew" | Controlled record of code, prompts, models, tools, deps, evals, docs | You cannot say what the controlled items are |
| 7 | **Operate** — run it in the real world and watch it | Production surprises going unseen | Signals, monitors, triggers for a new baseline | There is no owner for what to watch |
| 8 | **Learn** — feed the lesson back into the controls | Forgotten near misses; lessons dying in chat history | OPEX entries; updated tests, monitors, baselines | A near miss changes nothing |

The loop closes when what you learn feeds the next question.

This is what "nuclear-grade" buys you over prompt-and-pray: every step has a job, an artifact, and a stop condition. A skipped step is not a shortcut; it is a known failure mode you chose to accept.

These eight are the everyday form of the loop. For standard and high-consequence work the same loop fans out into eleven beats (`Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn`), splitting Question into Question/Discover, Specify into Specify/Plan, and Decide into Review/Decide. Same control points, more beats. Those eleven beats also carry a memory handle: **PROVE** (Plan · Run · Observe · Verdict · Educate), or just **PRO** (Plan · Run · Operate) zoomed out; see [`docs/diagrams.md`](docs/diagrams.md).

## Two speeds, one loop

For AI agents, we add a few small habits from Human Performance Improvement (HPI). Brief the work first. Double-check risky actions. Hand off cleanly. Get a second set of eyes when needed. Decide on the careful side. Learn from near misses.

The workflow has two speeds. While you explore and try ideas you can throw away, move fast: the loop still runs, but the artifacts are lightweight. Slow down when the work turns into something real: a piece of evidence, a claim, a file you must keep under control, public wording, a saved approved version, a release call, or a change to what the agent is allowed to do.

## Workflow catalog

| Workflow | Loop | Use when | Main artifact |
|---|---|---|---|
| Questioning attitude | question -> assumptions -> facts -> stop conditions -> next artifact | Work that is vague, high-stakes, or easy to talk yourself into | `questioning-attitude.md` or `risk.md` section |
| Quick change | question -> classify -> prove -> validate | Local, easy-to-undo work that is easy to prove | `risk.md`, `proof.md` |
| Standard change | specify -> plan -> trace -> verify -> decide | The change touches users, dependencies, security, AI behavior, operations, or a release | Standard packet |
| Controlled configuration | identify items -> impact screen -> baseline -> operate | Prompts, models, tools, dependencies, docs, releases, or agent authority need to stay under control | CM records (keeping the approved version under control) |
| Agent authority change | question -> context pack -> boundary proof -> release review | Agents can write files, call tools, use APIs, or affect releases | Packet plus context pack |
| Agent turnover | state -> changed conditions -> remaining work -> authority -> closed-loop acceptance | Work moves to another agent, reviewer, checker, releaser, support owner, or a resumed thread | `turnover.md` |
| Critical action self-check | action -> target -> expected result -> stop condition -> after-action evidence | You could hit the wrong target, overclaim in public, do something you cannot undo, or go past your authority | `self-check.md` |
| Release readiness | evidence status -> residual risk -> rollback -> monitoring -> decision | A pull request or release changes who trusts the work | `ship.md` |
| OPEX learning | event -> weak control -> durable update -> verification -> re-baseline trigger | A near miss, bad handoff, escaped defect, or review surprise should change future work. OPEX means lessons from real operation | `opex.md` |
| Trust check | intended use -> external claims -> local evidence -> controls -> release impact | A dependency, model, API, SaaS tool, generated artifact, or vendor claim affects trust | `supplier-trust.md` or packet section |
| Source/legal check | claim -> source map -> boundary wording -> validator | Public docs or examples mention assurance ideas | Source-lineage notes |
| Mission drift control | anchor -> zoom out -> test action -> loop/standards check -> re-anchor/escalate/stop | A long session drifts from its goal, scope creeps, or standards slip | `## Mission anchor`, `.nuclear/mission.md` |
| Code-quality review | objective -> delete-first -> tripwires -> abstraction check -> layering -> verdict | A diff or module risks slipping standards or needless complexity | Review findings plus verdict |
| Work breakdown and folders | deliverable -> 100%/MECE decomposition -> dictionary -> folder map -> naming/depth audit | An epic, subsystem, repo, or agent workspace needs a clean work breakdown (WBS) and folder layout. "100%/MECE" means the pieces cover the whole job with no gaps and no overlaps | `wbs.md` |
| Agentic workflow architecture | classify -> stage-contract -> authority-map -> deterministic-checks -> trace -> operate | Planning a multi-stage AI or agent workflow, workspace, or repo convention where context must be scoped per stage and the work is reviewed between stages | `stage-contract.md`, `agentic-workflow-architecture.md` |
| Authority and intent | decision rights -> intent declaration -> review window -> act unless stopped -> compare result | An agent could act on something irreversible or trust-bearing, or a deploy/migration/public claim needs a stated intent and an abort plan | `intent.md`, decision-rights line |
| Incident response | declare/command -> stabilize -> fact-vs-hypothesis timeline -> reversible-first -> corrective actions to closure | Production is broken, data is at risk, or an agent action caused harm | `incident.md` |
| Deficiency tracking | log -> age -> own -> fix-or-accept -> review trigger | A known problem will outlive a single change and must not be silently normalized | `deficiency.md` |

## Quick change

```bash
python tools/ng.py new typo-fix --mode quick
python tools/ng.py validate .nuclear/changes/typo-fix
```

Use Quick only when the change is low-stakes, easy to undo, and easy to prove, with no new trust boundary.

## Questioning attitude

Use this before the agent builds:

```bash
# Paste commands/ng-question.md into your agent, or copy the template:
cp templates/golden-path/questioning-attitude.md .nuclear/changes/<slug>/
```

The output should name the assumptions, the facts to check, the warning signs, the gaps in evidence, the stop conditions, and the next thing to produce.

The decision question comes first, not last. If the question is wrong, your proof can be clean and still back the wrong decision.

## Standard change

```bash
python tools/ng.py new add-agent-boundary --mode standard
python tools/ng.py validate .nuclear/changes/add-agent-boundary
```

Use Standard when reviewers need the spec (what the change must do and why), the plan, the trace, the verification and validation (V&V), and the release decision saved in the repo.

## Controlled configuration

Turn on CM records (keeping the approved version under control) when the change affects a controlled item: code, docs, prompts, models, dependencies, tools, credentials, context packs, evals, release artifacts, dashboards, or runbooks whose state matters to trust.

```text
controlled-items.md -> change-impact.md -> baseline.md -> variance.md -> opex.md
```

Start with `skills/choosing-what-to-control/SKILL.md` and `docs/02-operating-system/configuration-management.md`.

## Agent authority change

Agent authority changes need a clear scope:

- the files the agent may read or edit;
- the commands and tools it may run;
- its network, credential, approval, and release authority;
- the actions it must never take;
- the evidence it must produce before it is done.

Start with `skills/briefing-an-agent/SKILL.md` and `docs/02-operating-system/context-packs.md`.

## Agent turnover and self-checking

Use turnover when work moves between agents, people, checkers, releasers, support owners, or a resumed thread:

```bash
# Paste commands/ng-turnover.md into your agent, or copy the template:
cp templates/golden-path/turnover.md .nuclear/changes/<slug>/
```

Use a self-check before a critical action, when the wrong file, wrong command, public overclaim, a trust gap in a dependency, model, or API, a step you cannot undo, or a release decision could matter:

```bash
cp templates/golden-path/self-check.md .nuclear/changes/<slug>/
```

Keep these records short. They exist to stop a bad action, not to explain the theory behind the HPI habits.

Use a self-check at the moments that count: the wrong target, the wrong command, the wrong public claim, the wrong trust change to a dependency, model, or API, a step you cannot undo, or a release action. Do not slow down every edit you can easily undo.

## Release readiness

A release decision is more than "tests passed." It records the evidence status, the leftover risk, the rollback plan, what to monitor, the handoff, the decision, and what triggers a new baseline.

Use `skills/checking-release-readiness/SKILL.md`.

## OPEX and trust checks

Use OPEX (lessons from real operation) when an incident, near miss, bad handoff, escaped defect, review surprise, or user confusion should update a lasting control. A lesson is finished only when it updates a basis, test, checker, template, skill, command, doc, monitor, threshold, or baseline, or when you write down why no lasting update is needed.

Use trust checks when a dependency, model, API, SaaS tool, generated artifact, or vendor claim affects permissions, data, the release, the evidence, or public trust. Keep what someone else claims separate from what you proved yourself.

## Source and legal boundary checks

Use these checks for public text:

```bash
python tools/ng.py doctor .
rg -n "formal|certified|approval" README.md docs skills commands templates

# Standard fallback when ripgrep is not available:
grep -E -rn "formal|certified|approval" README.md docs skills commands templates
```

The phrase scan is only a starting point. The right fix is usually tighter wording and a clear boundary note.

## Source-lineage note

These workflows are original software patterns. Public sources shaped them, and those sources are mapped in `docs/00-standards-foundation/source-map.md`. They do not create formal assurance or compliance.
