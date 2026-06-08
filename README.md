<div align="center">

<img src="docs/assets/landing-banner.svg" alt="Nuclear-grade Context Engineering — let AI do serious software work without losing control. Go fast while exploring; slow down when the work becomes a promise." width="820">

<br/>

**A simple, evidence-first way to let AI do serious software work — without losing control.**

[![CI](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml/badge.svg)](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-2E7D45.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3A5BA8.svg)](pyproject.toml)
[![No build step](https://img.shields.io/badge/setup-no%20build%20step-5B49A6.svg)](#quick-start)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-B07400.svg)](CONTRIBUTING.md)

</div>

# Nuclear Grade Context Engineering

AI agents no longer just suggest code. They edit files, change prompts, call tools, swap dependencies, write the evidence, and help ship releases. That is a lot of power with very little ceremony. Nuclear-grade gives that work a clear, safe path — so you can move fast and still trust what ships.

You do not need to read the whole repo to start. Run the two commands in [See it work in 30 seconds](#see-it-work-in-30-seconds), then copy one folder.

## Contents

- [What this is](#what-this-is)
- [The one idea](#the-one-idea)
- [See it work in 30 seconds](#see-it-work-in-30-seconds)
- [How one change flows](#how-one-change-flows)
- [Who does what](#who-does-what)
- [Keeping the approved version under control](#keeping-the-approved-version-under-control)
- [The common way vs. the nuclear-grade way](#the-common-way-vs-the-nuclear-grade-way)
- [What you get](#what-you-get)
- [Pick how much you want](#pick-how-much-you-want)
- [Which change record do I need?](#which-change-record-do-i-need)
- [Who this is for](#who-this-is-for)
- [Quick start](#quick-start)
- [Works across your tools](#works-across-your-tools)
- [Project and community](#project-and-community)
- [Map of the repo](#map-of-the-repo)
- [What this is NOT](#what-this-is-not)
- [License and limits](#license-and-limits)
- [Where the ideas come from](#where-the-ideas-come-from)

## What this is

Before an agent builds, you ask hard questions and find the facts. You write down what the change must do. The agent works only inside the limits you set. Then you check the claims against real evidence, decide on purpose, save the approved version, and learn from what happens next.

The discipline is borrowed from how high-consequence engineering is run: question your assumptions, prove your claims, and never let standards slip one small step at a time. The name is the standard of care, not the vocabulary — keep the discipline and rename the local copy if "nuclear-grade" would mis-calibrate your team (see [`DISCLAIMER.md`](DISCLAIMER.md)).

## The one idea

**Go fast while you are exploring. Slow down the moment the work becomes a promise.**

An agent can try ideas and throw them away cheaply, so let it. But the rules tighten as soon as the work turns into a claim, a file you have to keep under control, a public statement, an approved version, a release call, or a change to what the agent is allowed to do.

The very first question is the most important one: **what does this evidence have to prove, and what fact would change my decision?**

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> save approved version -> operate
```

This first release (v0) is a working toolkit you can use today: skills an agent can follow, command prompts you can paste, templates for small and large changes, a small command-line tool, a checker, a public list of sources, one fully worked example, and one hands-on comparison study.

## See it work in 30 seconds

Watch an AI agent prove it stayed inside its workspace, then read the change record that backs the result:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -v
# 4 passed — every write attempt outside the agent's workspace was denied and logged.
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
# OK — the change record exposes the evidence behind that result.
```

That packet is your template, not a curiosity. Copy [`docs/03-worked-examples/ai-agent-tool-permissions/`](docs/03-worked-examples/ai-agent-tool-permissions/) to start your own, and see [`CORE.md`](CORE.md) for the seven habits behind it. The longer guided tour lives in [`QUICKSTART.md`](QUICKSTART.md). If your shell only has `python3`, use `python3`.

## How one change flows

Every change walks the same path. Each step is a control point: it stops one specific failure and produces one artifact you can point at. A skipped step is not a shortcut — it is a named failure mode you chose to accept.

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

```mermaid
flowchart LR
    Q[Question] --> D[Discover] --> S[Specify] --> P[Plan]
    P --> E[Execute] --> V[Verify] --> R[Review]
    R --> Dec{Decide}
    Dec -->|ship / defer| B[Baseline] --> O[Operate] --> L[Learn]
    Dec -->|block| P
    L -.feeds future basis.-> Q
```

Zoomed out, those eleven beats are three moves — **PRO**: Plan · Run · Operate — or five with the gate named — **PROVE**: Plan · Run · Observe · Verdict · Educate. One label, two zoom levels:

```mermaid
flowchart TB
  classDef plan fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
  classDef run fill:#E4DEF7,stroke:#5B49A6,color:#1E1640;
  classDef emb fill:#DCEFDE,stroke:#2E7D45,color:#102810;
  classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
  subgraph LP["P — PLAN"]
    direction LR
    A1(["Question"]) --> A2(["Discover"]) --> A3(["Specify"]) --> A4(["Plan"])
  end
  subgraph LRUN["R — RUN"]
    direction LR
    B1(["Execute"]) --> B2(["Verify"]) --> B3(["Review"]) --> B4{"Decide"}
  end
  subgraph LOPS["O — OPERATE"]
    direction LR
    C1(["Baseline"]) --> C2(["Operate"]) --> C3(["Learn"])
  end
  A4 --> B1
  B4 -->|"ship / defer"| C1
  B4 -.->|"block"| A4
  C3 -.->|"lessons feed the next basis"| A1
  class A1,A2,A3,A4 plan
  class B1,B2,B3 run
  class B4 gate
  class C1,C2,C3 emb
```

*If the diagrams above do not render (for example on PyPI), the eleven-beat line just above is the same path in text.* The control-point detail — what each step stops and produces — is in [`WORKFLOWS.md`](WORKFLOWS.md), and every diagram here is canonical in [`docs/diagrams.md`](docs/diagrams.md).

Underneath the path sit a few habits borrowed from high-reliability work — what we call **HPI for AI agents** (Human Performance Improvement). Use them when they change the outcome: brief the work before a risky step, double-check critical actions, hand off cleanly, get a second set of eyes when trust is on the line, and capture the lesson after a near miss.

## Who does what

Four roles share the work: **you**, the **AI agent**, the **change record**, and the **reviewer**. The agent moves fast — but only inside limits you approve first. The record carries each claim and its evidence. The reviewer decides on the evidence, not the pitch.

```mermaid
sequenceDiagram
    actor You
    participant Agent as AI agent
    participant Record as Change record
    actor Reviewer
    You->>Agent: Ask the hard question, set the goal
    Agent->>Record: Draft the risk and what "good" means
    Record-->>You: You read the draft
    You->>Agent: Approve the limits (may / may not do)
    Agent->>Agent: Build only inside the limits
    Agent->>Record: Write each claim with its evidence
    Record-->>Reviewer: Show evidence, gaps, decision
    Reviewer->>Record: Decide on purpose (ship / defer / block)
    Record->>Record: Save the approved version (baseline)
    Note over You,Reviewer: Lessons from real use feed the next change
```

**In words:** you ask and set the goal → the agent drafts the risk and what "good" means → you approve the limits → the agent builds only inside them → the agent writes each claim with its evidence → the reviewer checks the evidence and decides (ship / defer / block) → the approved version is saved as the baseline → lessons from real use feed the next change. Canonical copy in [`docs/diagrams.md`](docs/diagrams.md).

## Keeping the approved version under control

A **baseline** is just the version everyone agreed is correct and wants to protect. Changes never edit the baseline directly — they go through evidence and a decision first, and only an accepted change becomes the new baseline. That is configuration management, in one loop:

```mermaid
flowchart LR
    classDef item fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
    classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
    classDef base fill:#DCEFDE,stroke:#2E7D45,color:#102810;
    CI["Controlled items<br/>code, prompts, models,<br/>deps, docs, releases"]:::item --> CH["A change"]
    CH --> EV["Evidence<br/>pass or gap, named"]
    EV --> DEC{"Decide<br/>on purpose"}:::gate
    DEC -->|"ship / defer"| BL["Saved baseline<br/>the approved version"]:::base
    DEC -.->|"block"| CH
    BL --> OP["Operate"]
    OP --> LE["Lessons learned"]
    LE -.->|"feed the next change"| CI
```

**In words:** controlled items (code, prompts, models, dependencies, docs, releases) → a change → named evidence (pass or gap) → a deliberate decision → if ship or defer, save the new baseline; if block, back to the change → operate the baseline → lessons feed the next change. You only add the heavier records — what is under control, ripple effects, the saved baseline, drift, and operating lessons — when the stakes are high enough to earn them. Canonical copy in [`docs/diagrams.md`](docs/diagrams.md).

## The common way vs. the nuclear-grade way

| The common way | The nuclear-grade way |
|---|---|
| Ask an agent, look at the diff, run the tests. | Question the assumptions, name what must stay under control, write down the intent, check the evidence, decide, and save the approved version. |
| The pull request text tries to talk reviewers into a yes. | A change record links intent, what must not break, what is under control, the evidence, the gaps, and the decision. |
| Agents get broad access and vague instructions. | Agents get a role, a list of what they may do, what they may not do, what they must prove, where the work stands, and when to stop. |
| Green tests become the reason to ship. | The release record states the evidence, the leftover risk, the rollback plan, what to watch, the decision, and what to save. |
| Lessons disappear into the chat history. | Lessons from real operation feed back into future plans, tests, monitors, and controls. |

The shift, in one view:

```text
review the diff           -> review the whole approved setup
trust the prompt history  -> keep a controlled record of the change
hand the agent free rein  -> hand it focused context and a duty to prove
treat green tests as a yes -> make an explicit release decision and save the result
```

This is practical, not decorative. Instructions should be hard to misuse. Small actions should still serve the goal. And "I'm confident" should never be confused with "here is the proof."

## What you get

| Part | What it does | Start here |
|---|---|---|
| Workflows | Step-by-step paths for small changes, big changes, and the careful checks in between | [`WORKFLOWS.md`](WORKFLOWS.md) |
| Skills | Instructions an agent can follow, each with inputs, outputs, how to verify, when to stop, and warning signs | [`SKILLS.md`](SKILLS.md) |
| Command prompts | Ready-to-paste prompt cards for questioning, sorting risk, checking impact, saving an approved version, reviewing evidence, release checks, and more | [`COMMANDS.md`](COMMANDS.md) |
| Templates | Fill-in records for small changes, standard changes, and high-consequence ones | [`templates/`](templates/) |
| Command-line tool | `init`, `new`, `validate`, `doctor`, `list`, `status`, `migrate`, `tokens` | [`docs/05-reference/cli-reference.md`](docs/05-reference/cli-reference.md) |
| Checker | A no-dependencies check for small and standard change records | [`tools/ng_validate.py`](tools/ng_validate.py) |
| Worked example | A real change record proving an AI agent stayed inside its workspace | [`EXAMPLES.md`](EXAMPLES.md) |
| Sources | The public ideas this borrows from, and how to talk about them safely | [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) |

As of v0.5.0 that is **27 skills** and **26 command prompts**. The live list is the source of truth — see [`nuclear-grade.yaml`](nuclear-grade.yaml), [`SKILLS.md`](SKILLS.md), and [`COMMANDS.md`](COMMANDS.md) — so treat any count here as a snapshot, not a promise.

## Pick how much you want

You do not adopt the whole system on day one. It scales with the stakes:

- **Start with the Core 7** — seven always-on habits that fit any change. See [`CORE.md`](CORE.md).
- **Add clusters by consequence** — bring in the heavier skills, templates, and records only when a change touches users, data, dependencies, permissions, AI authority, or a release.
- **Grow into the full system** — the complete skill set, command prompts, and modes once your team has tested the lighter path.

Ready-made bundles live in [`starter-kit/`](starter-kit/), and [`CORE.md`](CORE.md) has a decision matrix that picks the right kit for your project by trigger.

## Which change record do I need?

Rigor scales with consequence, not effort. This release checks two kinds of change records, both kept under `.nuclear/changes/<name>/`:

```mermaid
flowchart TD
    Start([Change request]) --> Q1{Local, reversible,<br/>obvious proof,<br/>no new trust boundary?}
    Q1 -->|yes| Quick[Quick packet<br/>risk.md + proof.md]
    Q1 -->|no| Q2{User / data / dep /<br/>permission / AI authority /<br/>release consequence?}
    Q2 -->|yes| Standard[Standard packet<br/>6 files]
    Q2 -->|severe, silent,<br/>irreversible, external trust| Strong[Human-reviewed<br/>stronger mode]
    Q2 -->|already went wrong| Incident[Incident pattern]
```

**In words / which files:**

| Kind | Use it when | Files |
|---|---|---|
| Quick | Low stakes, easy to undo, obvious proof, no new trust boundary | `risk.md`, `proof.md` |
| Standard | It touches users, dependencies, permissions, data, AI behavior, operations, or a release | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md` |

The heavier patterns (high-consequence, incident, research-board, and release) are written down here, but for now treat them as human-reviewed until your own project has tested them.

## Who this is for

Use Nuclear-grade if you are:

- building AI agents that write files, call APIs, use credentials, approve actions, or affect releases;
- using coding agents on work that matters more than a throwaway script;
- reviewing AI-assisted pull requests and want evidence instead of a sales pitch;
- leading a team that wants speed without losing the plot on risk and releases;
- building internal workflows where people and agents both need focused context and a duty to prove their claims.

## Quick start

1. **Get the tool.** Clone the repo and install it (no third-party dependencies). See [`INSTALL.md`](INSTALL.md).
2. **Check your setup.** Run `python tools/ng.py doctor .` to confirm things are wired up, and `python tools/ng.py list` to see what is available.
3. **Make your first record.** Run `python tools/ng.py new <slug> --mode quick`, fill in the two files, then prove it with `python tools/ng.py validate .nuclear/changes/<slug>`.

If your shell only has `python3`, use `python3`. The full guided tour is in [`QUICKSTART.md`](QUICKSTART.md). **Using an AI agent? Point it at [`AGENTS.md`](AGENTS.md)** — it is the shared brief agents read first.

## Works across your tools

Cursor, Claude Code, Aider, Codex, and Copilot each read slightly different files for their reasoning and rules. `.nuclear/`, [`AGENTS.md`](AGENTS.md), and the `SKILL.md` contract are a **shared, tool-agnostic shape** that all of them can import as plain markdown: a portable surface for agent authority, change records, and evidence. No matter which IDE ships reasoning steps natively, the packets and habits travel with the repository.

## Project and community

| Topic | Where |
|---|---|
| How to contribute | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| How decisions are made | [`GOVERNANCE.md`](GOVERNANCE.md) |
| Reporting a vulnerability | [`SECURITY.md`](SECURITY.md) |
| Community expectations | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Getting help | [`SUPPORT.md`](SUPPORT.md) |
| Where this is going | [`ROADMAP.md`](ROADMAP.md) |
| What changed | [`CHANGELOG.md`](CHANGELOG.md) |
| The principles in short form | [`MAXIMS.md`](MAXIMS.md) |
| Citing this work | [`CITATION.cff`](CITATION.cff) |

## Map of the repo

```text
skills/                         skills an agent can follow
commands/                       paste-ready command prompts
templates/                      fill-in records for small, standard, and high-consequence changes
starter-kit/                    ready-made bundles to drop into a project
tools/                          the command-line tool and the checker
tests/                          tests for the checker, the tool, the contracts, and the public docs
docs/00-standards-foundation/   sources, safe citation, compliance boundaries
docs/01-field-guide/            how each source idea maps to a plain concept, incl. the leadership and high-reliability guide
docs/02-operating-system/       the path, the habits, the modes, the records, the checks, authority and intent, incidents, deficiencies
docs/03-worked-examples/        the flagship worked example and the comparison study
docs/04-adoption/               rollout, agent permissions, reviewer playbook
docs/05-reference/              the skill, command, and tool contracts
docs/diagrams.md                visual maps of the path, modes, skills, and records
docs/glossary.md                plain-language decoding of terms and idioms
```

## What this is NOT

Nuclear-grade is not a compliance program, a certification, a regulated quality-assurance system, a safety analysis, a production sandbox, a regulatory submission, legal advice, or a substitute for qualified engineering, legal, security, safety, or compliance review.

It does not claim that any system is safe, secure, compliant, approved, certified, or fit for regulated use.

Read these before you use it:

- [`DISCLAIMER.md`](DISCLAIMER.md)
- [`docs/00-standards-foundation/compliance-boundaries.md`](docs/00-standards-foundation/compliance-boundaries.md)
- [`docs/00-standards-foundation/do-not-cite-directly.md`](docs/00-standards-foundation/do-not-cite-directly.md)

The comparison study is honest about its limits: it is author-judged across twelve scenarios, design evidence not proof of effectiveness. See [`docs/03-worked-examples/skill-workflow-comparison/methodology.md`](docs/03-worked-examples/skill-workflow-comparison/methodology.md) for what the trials measure and what they do not.

## License and limits

Nuclear-grade is released under the [`MIT License`](LICENSE). You may use, copy, change, publish, distribute, sublicense, and sell copies under the license terms.

That permission is not a promise about quality. Using this repo does not create formal verification and validation, NQA-1 evidence, NQA-1 record, compliance, certification, regulatory approval, or any safety, security, procurement, production, warranty, or support guarantee.

The public sources named here are influences and idea lineage. They are not standards this repo claims to meet.

## Where the ideas come from

Nuclear-grade is an original software workflow inspired by public sources. The source families are mapped in [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) and translated into plain concepts in [`docs/01-field-guide/source-to-concept-crosswalk.md`](docs/01-field-guide/source-to-concept-crosswalk.md).
