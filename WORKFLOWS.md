# Nuclear-grade Workflows

Nuclear-grade turns AI-assisted software work into questioned, controlled, reviewable configuration.

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> baseline -> operation
```

## Workflow catalog

| Workflow | Loop | Use when | Main artifact |
|---|---|---|---|
| Questioning attitude | question -> assumptions -> facts -> stop conditions -> next artifact | Vague, consequential, or easy-to-rationalize work | `questioning-attitude.md` or `risk.md` section |
| Quick change | question -> classify -> prove -> validate | Local, reversible, easy-to-prove work | `risk.md`, `proof.md` |
| Standard change | specify -> plan -> trace -> verify -> decide | User, dependency, security, AI, operational, or release consequence | Standard packet |
| Controlled configuration | identify items -> impact screen -> baseline -> operate | Prompts, models, tools, deps, docs, releases, or agent authority become controlled | CM records |
| Agent authority change | question -> context pack -> boundary proof -> release review | Agents can write files, call tools, use APIs, or affect releases | Packet plus context pack |
| Release readiness | evidence status -> residual risk -> rollback -> monitoring -> decision | A PR or release changes trust posture | `ship.md` |
| Source/legal check | claim -> source map -> boundary wording -> validator | Public docs or examples cite assurance concepts | Source-lineage notes |

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

Start with `skills/identifying-controlled-items/SKILL.md` and `docs/02-operating-system/configuration-management.md`.

## Agent authority change

Agent authority changes need explicit scope:

- files the agent may read or edit;
- commands and tools it may run;
- network, credential, approval, and release authority;
- forbidden actions;
- evidence required before completion.

Start with `skills/packing-agent-context/SKILL.md` and `docs/02-operating-system/context-packs.md`.

## Release readiness

A release decision is not "tests passed." It records evidence status, residual risk, rollback, monitoring, handoff, decision, and baseline trigger.

Use `skills/reviewing-ship-readiness/SKILL.md`.

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
