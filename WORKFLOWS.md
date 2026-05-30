# Nuclear-grade Workflows

Nuclear-grade turns AI-assisted software work into questioned, controlled, reviewable configuration.

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> baseline -> operation
```

HPI for AI agents adds the micro-controls under that path: brief the work, self-check critical actions, turn over cleanly, verify independently when needed, decide conservatively, and learn from near misses.

The workflow is two-speed. Exploration and reversible candidate work should stay fast; acceptance slows down when a candidate becomes evidence, a claim, a controlled item, public wording, a baseline, a release decision, or an agent-authority boundary.

## Workflow catalog

| Workflow | Loop | Use when | Main artifact |
|---|---|---|---|
| Questioning attitude | question -> assumptions -> facts -> stop conditions -> next artifact | Vague, consequential, or easy-to-rationalize work | `questioning-attitude.md` or `risk.md` section |
| Quick change | question -> classify -> prove -> validate | Local, reversible, easy-to-prove work | `risk.md`, `proof.md` |
| Standard change | specify -> plan -> trace -> verify -> decide | User, dependency, security, AI, operational, or release consequence | Standard packet |
| Controlled configuration | identify items -> impact screen -> baseline -> operate | Prompts, models, tools, deps, docs, releases, or agent authority become controlled | CM records |
| Agent authority change | question -> context pack -> boundary proof -> release review | Agents can write files, call tools, use APIs, or affect releases | Packet plus context pack |
| Agent turnover | state -> changed conditions -> remaining work -> authority -> closed-loop acceptance | Work transfers to another agent, reviewer, verifier, releaser, support owner, or resumed thread | `turnover.md` |
| Critical action self-check | action -> target -> expected result -> stop condition -> after-action evidence | Wrong target, public overclaim, irreversible state, or exceeded authority is plausible | `self-check.md` |
| Release readiness | evidence status -> residual risk -> rollback -> monitoring -> decision | A PR or release changes trust posture | `ship.md` |
| OPEX learning | event -> weak control -> durable update -> verification -> re-baseline trigger | Near misses, bad handoffs, escaped defects, or review surprises should change future work | `opex.md` |
| Trust check | intended use -> external claims -> local evidence -> controls -> release impact | Dependencies, models, APIs, SaaS, generated artifacts, or vendor claims affect trust | `supplier-trust.md` or packet section |
| Source/legal check | claim -> source map -> boundary wording -> validator | Public docs or examples cite assurance concepts | Source-lineage notes |
| Mission drift control | anchor -> zoom out -> test action -> loop/standards check -> re-anchor/escalate/stop | A long session drifts from its objective, scope creeps, or rigor erodes | `## Mission anchor`, `.nuclear/mission.md` |
| Code-quality review | objective -> delete-first -> tripwires -> abstraction check -> layering -> verdict | A diff or module risks standards drift or needless complexity | Review findings plus verdict |
| Work breakdown and folders | deliverable -> 100%/MECE decomposition -> dictionary -> folder map -> naming/depth audit | An epic, subsystem, repo, or agent workspace needs a clean scope breakdown and folder layout | `wbs.md` |

## Quick change

```bash
python tools/ng.py new typo-fix --mode quick
python tools/ng.py validate .nuclear/changes/typo-fix
```

Use Quick only when the change is low consequence, reversible, and easy to prove without a new trust boundary.

## Questioning attitude

Use this before the agent builds:

```bash
# Paste commands/ng-question.md into your agent, or copy the template:
cp templates/golden-path/questioning-attitude.md .nuclear/changes/<slug>/
```

The output should name assumptions, facts to verify, warning signs, evidence gaps, stop conditions, and the next artifact.

The decision question is the first output, not an afterthought. If the question is wrong, the proof can be clean and still support the wrong decision.

## Standard change

```bash
python tools/ng.py new add-agent-boundary --mode standard
python tools/ng.py validate .nuclear/changes/add-agent-boundary
```

Use Standard when reviewers need specification/design-basis, plan, trace, verification, and release decision in the repo.

## Controlled configuration

Activate CM records when the change affects a controlled item: code, docs, prompts, models, dependencies, tools, credentials, context packs, evals, release artifacts, dashboards, or runbooks whose state matters to trust.

```text
controlled-items.md -> change-impact.md -> baseline.md -> variance.md -> opex.md
```

Start with `skills/choosing-what-to-control/SKILL.md` and `docs/02-operating-system/configuration-management.md`.

## Agent authority change

Agent authority changes need explicit scope:

- files the agent may read or edit;
- commands and tools it may run;
- network, credential, approval, and release authority;
- forbidden actions;
- evidence required before completion.

Start with `skills/briefing-an-agent/SKILL.md` and `docs/02-operating-system/context-packs.md`.

## Agent turnover and self-checking

Use turnover when work moves between agents, humans, verifiers, releasers, support owners, or resumed threads:

```bash
# Paste commands/ng-turnover.md into your agent, or copy the template:
cp templates/golden-path/turnover.md .nuclear/changes/<slug>/
```

Use self-checking before critical actions where the wrong file, wrong command, public overclaim, dependency/model/API trust gap, irreversible state, or release decision could matter:

```bash
cp templates/golden-path/self-check.md .nuclear/changes/<slug>/
```

These records should stay short. They exist to stop bad action, not to explain HPI theory.

Use self-checking at cut points: wrong target, wrong command, wrong public claim, wrong dependency/model/API trust change, irreversible state, or release action. Do not slow every reversible edit.

## Release readiness

A release decision is not "tests passed." It records evidence status, residual risk, rollback, monitoring, handoff, decision, and baseline trigger.

Use `skills/checking-release-readiness/SKILL.md`.

## OPEX and trust checks

Use OPEX when an incident, near miss, bad handoff, escaped defect, review surprise, or user confusion should update a durable control. A lesson is complete only when it updates a basis, test, validator, template, skill, command, doc, monitor, threshold, or baseline, or when closure explicitly explains why no durable update is warranted.

Use trust checks when dependencies, models, APIs, SaaS tools, generated artifacts, or vendor claims affect permissions, data, release posture, evidence, or public trust. Separate external claims from local proof.

## Source and legal boundary checks

Use these checks for public text:

```bash
python tools/ng.py doctor .
rg -n "formal|certified|approval" README.md docs skills commands templates

# Standard fallback when ripgrep is not available:
grep -E -rn "formal|certified|approval" README.md docs skills commands templates
```

The phrase scan is a starting point. The correct fix is usually narrower wording and an explicit boundary note.

## Source-lineage note

These workflows are original software operating patterns influenced by public sources mapped in `docs/00-standards-foundation/source-map.md`. They do not create formal assurance or compliance.
