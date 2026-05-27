# Nuclear Grade Context Engineering

[![CI](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml/badge.svg)](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml)

> Questioning attitude and configuration management for AI-assisted software work.

AI agents no longer just suggest code. They edit files, change prompts, call tools, update dependencies, produce evidence, and prepare releases. Nuclear-grade gives that work a controlled path: question assumptions, discover facts, specify required behavior, execute inside authority, verify claims, review evidence, decide, baseline the accepted configuration, and learn from operation.

It also adds HPI for AI agents: small control behaviors that make fast agent work reviewable. Brief the work, self-check critical actions, turn over cleanly, verify independently when consequence demands it, decide conservatively, and learn from near misses.

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> baseline -> operation
```

Public v0 is a usable skill and workflow product: agent-operable skills, portable command prompts, Quick/Standard change packages, activated configuration-management records, a local CLI, a validator, a public source foundation, and one validated worked example.

## Try it in 60 seconds

```bash
python tools/ng.py doctor .
python tools/ng.py list
python tools/ng.py new demo-change --mode quick
python tools/ng.py validate .nuclear/changes/demo-change
```

Inspect the included evidence path:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

If your shell only has `python3`, use `python3`.

## What you get

| Surface | What it does | Start |
|---|---|---|
| Workflows | Questioning-attitude, HPI overlays, and controlled-change loops for Quick, Standard, CM, agent authority, release review, and source/legal checks | [`WORKFLOWS.md`](WORKFLOWS.md) |
| Skills | Agent-operable instructions with inputs, outputs, verification, escalation, and red flags | [`SKILLS.md`](SKILLS.md) |
| Portable command prompts | Pasteable prompt cards for questioning, classification, CM impact, baselining, evidence review, release review, source checks, and legal boundaries | [`COMMANDS.md`](COMMANDS.md) |
| Templates | Quick, Standard, activated CM, and golden-path records | [`templates/`](templates/) |
| CLI | `init`, `new`, `validate`, `doctor`, `list`, and `status` | [`docs/05-reference/cli-reference.md`](docs/05-reference/cli-reference.md) |
| Validator | Dependency-free Quick and Standard packet checks | [`tools/ng_validate.py`](tools/ng_validate.py) |
| Worked example | Standard packet proving an AI-agent workspace boundary | [`EXAMPLES.md`](EXAMPLES.md) |
| Source foundation | Public source map and citation boundaries | [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) |

## How it differs

| Common pattern | Nuclear-grade pattern |
|---|---|
| Ask an agent, inspect the diff, run tests. | Question assumptions, identify controlled items, specify intent, verify evidence, decide, and baseline. |
| PR prose tries to persuade reviewers. | A change package links intent, protected outcomes, controlled items, evidence, gaps, and decision. |
| Agents receive broad context and fuzzy authority. | Agents receive role, allowed actions, forbidden actions, evidence obligations, turnover state, and stop conditions. |
| Green CI becomes a release argument. | Release readiness records evidence status, residual risk, rollback, monitoring, decision, and baseline trigger. |
| Lessons vanish into chat history. | OPEX records feed future basis, tests, monitors, controls, or re-baselines. |

The central shift is:

```text
diff review -> configuration review
prompt memory -> controlled change record
agent authority -> focused context and evidence obligation
green CI -> explicit release decision and baseline trigger
```

## Core workflow

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

Short launch version:

```text
Question -> Specify -> Execute -> Verify -> Decide
```

Quick and Standard packets are the Git-native way to record that lifecycle. `Classify` stays inside the risk/mode screen so the public path stays teachable. Activated CM records add controlled items, change impact, baseline, variance, and OPEX detail only when consequence justifies it.

HPI overlays sit underneath that path. Use them when they change the work: task preview before consequential execution, self-check before critical actions, turnover before another agent or human continues, independent verification before high-trust decisions, and OPEX after near misses or review surprises.

## Packet modes

Public v0 validates Quick and Standard packets.

```text
.nuclear/changes/<slug>/
```

| Mode | Use when | Files |
|---|---|---|
| Quick | Low consequence, reversible, obvious proof, no new trust boundary | `risk.md`, `proof.md` |
| Standard | User, dependency, permission, data, AI, operational, or release consequence | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md` |

Nuclear, Incident, Research Board, and Release are documented operating patterns in Public v0. Treat them as human-reviewed until project-specific validation exists.

## Who this is for

Use Nuclear-grade if you are:

- building AI agents that write files, call APIs, use credentials, approve actions, or affect releases;
- using coding agents on changes that matter more than a disposable script;
- reviewing AI-assisted PRs and need evidence instead of persuasion;
- leading a team that wants speed without losing control of risk and release posture;
- creating internal workflows where humans and agents need focused context and evidence obligations.

## What this is not

Nuclear-grade is not a compliance framework, certification product, regulated quality assurance program, safety analysis method, production sandbox, regulatory submittal package, legal advice, or substitute for qualified engineering, legal, security, safety, or compliance review.

It does not claim that a system is safe, secure, compliant, approved, certified, or suitable for regulated use.

Read before using:

- [`DISCLAIMER.md`](DISCLAIMER.md)
- [`docs/00-standards-foundation/compliance-boundaries.md`](docs/00-standards-foundation/compliance-boundaries.md)
- [`docs/00-standards-foundation/do-not-cite-directly.md`](docs/00-standards-foundation/do-not-cite-directly.md)

## Repo map

```text
skills/                         agent-operable workflow skills
commands/                       portable command prompts
templates/                      Quick, Standard, golden-path, and activated CM templates
tools/                          local CLI and validator
tests/                          validator, CLI, contract, and public-doc tests
docs/00-standards-foundation/   source map, citation safety, compliance boundaries
docs/01-field-guide/            source-to-concept translation
docs/02-operating-system/       lifecycle, HPI overlays, modes, packets, thresholds, validators, context packs
docs/03-worked-examples/        flagship worked example
docs/04-adoption/               rollout, agent authority, reviewer playbook
docs/05-reference/              skill, command, and CLI contracts
```

## Public v0 status

Included now:

- action-first onboarding and repo WBS;
- Quick and Standard templates;
- activated CM templates for controlled items, change impact, baseline, variance, and OPEX;
- golden-path templates for questioning attitude, specification, turnover, self-check, and decision records;
- local CLI and dependency-free validator;
- agent-operable skills and portable command prompts;
- public source foundation and source status labels;
- validated worked example for an AI-agent workspace boundary;
- tests for validator, CLI, skill contracts, command contracts, public docs, and worked example code.

Not included yet:

- packaged marketplace integration for a specific agent harness;
- full worked examples for external API controls and human approval gates;
- rich deterministic validation for Nuclear, Incident, Research Board, and Release patterns;
- a production sandbox, compliance package, or regulated-use assurance workflow.

## License and boundaries

Nuclear-grade is released under the [`MIT License`](LICENSE). You may use, copy, modify, publish, distribute, sublicense, and sell copies subject to the license terms.

That permission is not an assurance claim. Use of this repo does not create formal V&V, formal verification and validation, NQA-1 evidence, NQA-1 record, compliance, certification, regulatory approval, safety, security, procurement adequacy, production suitability, warranty, or support obligation.

The public sources named here are influences and concept lineage, not requirements this repo satisfies.

## Source-lineage note

Nuclear-grade is an original, public-source-inspired software workflow. Source families are mapped in [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) and translated in [`docs/01-field-guide/source-to-concept-crosswalk.md`](docs/01-field-guide/source-to-concept-crosswalk.md).
