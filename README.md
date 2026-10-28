<div align="center">

<img src="docs/assets/landing-banner.svg" alt="Nuclear-grade Context Engineering: let AI do serious software work and stay in control of what ships." width="820">

<br/>

[![CI](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml/badge.svg)](https://github.com/FlyFission/nuclear-grade-context-engineering/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-2E7D45.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3A5BA8.svg)](pyproject.toml)
[![No build step](https://img.shields.io/badge/setup-no%20build%20step-5B49A6.svg)](#quick-start)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-B07400.svg)](CONTRIBUTING.md)
[![Evidence records](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FFlyFission%2Fnuclear-grade-context-engineering%2Fmain%2F.nuclear%2Fbadge.json)](.nuclear/changes/)

</div>

# Nuclear-grade Context Engineering

**Keep your AI coding agent honest. It does the work, and you stay in control of what ships.**

A small guard and a few habits for coding agents. The guard stops an agent from editing the things that judge its work, like your CI and its own settings, and asks you before it tags, publishes, or force-pushes. The habits ask the agent to show its proof for risky changes, so you can see what is still open before you say yes.

<p align="center"><img src="docs/assets/demo/demo.gif" width="900" alt="Terminal demo, about 30 seconds. A simulated agent write to .github/workflows/ci.yml is denied by the PreToolUse gate; a simulated force-push to main is routed to a human; a passing change record's JSON receipt still reports two open evidence items and the badge counts open items; an unfilled change record fails validation."></p>

<details><summary>Text transcript of the demo</summary>

1. `sim Write .github/workflows/ci.yml` prints `DENY`: writes to a protected trust surface go through human review, not the agent.
2. `sim Bash "git push --force origin main"` prints `ASK`: a force push needs a human.
3. `ng validate <worked example> --json` reports `"ok": true` and `"open_evidence_items": 2`; `ng badge .` reports the repository's records and open items.
4. `ng validate` on a freshly scaffolded, unfilled record prints `FAILED`.

`sim` sends a simulated tool call through `hooks/pre_tool_use.py`; no agent runs. The recording is [`docs/assets/demo/demo.tape`](docs/assets/demo/demo.tape), and a test replays its commands so they still print what the recording shows. The test does not render the GIF; re-render it with `vhs docs/assets/demo/demo.tape` whenever the tape or those commands change.

</details>

The demo sends simulated tool calls through the real guard script, so no agent runs in it.

## Quick start

**Claude Code.** This repo is its own plugin marketplace.

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade-guard@nuclear-grade   # the guard only
/plugin install nuclear-grade@nuclear-grade         # the skills and command prompts
/reload-plugins
```

**Cursor, Codex, Windsurf, VS Code with Copilot, or any repo.**

```bash
pipx install nuclear-grade
nuclear-grade init --all          # records folder, AGENTS.md, the guard, and a CI check
nuclear-grade install cursor      # or codex, claude, windsurf, vscode
```

**See how your own agent does.** The [15-minute challenge](challenge/README.md) gives your agent a routine task that quietly widens what a toy agent may do. A scorer checks whether your agent noticed, wrote it down, and left the ship call to you.

## What it does

- **Guards the judge.** Your agent cannot edit your CI workflows, its hook settings, or the guard itself, and it has to ask you before a tag, a publish, a force-push, or a risky delete. It never auto-approves and it fails closed. [How it compares to built-in permission rules](HOOKS.md#why-not-just-use-permission-deny-rules).
- **Scales with the stakes.** A typo needs nothing. A small, easy-to-undo change gets two short files. A change to permissions, data, dependencies, or a release gets a fuller record that ties each claim to its proof and names what is still unproven.
- **Shows who checked.** Each record notes who wrote the evidence, so a reviewer can tell when the agent graded its own work.
- **Stays light.** No build step and no third-party dependencies. The Core skill set adds under 1,000 tokens of skill descriptions to a session (`nuclear-grade install <tool> --core`, the default). `--full` installs all of them.

## What "nuclear-grade" means here

In the nuclear industry, "nuclear-grade" describes parts qualified for safety use. Here it only names a level of care: question first, prove your claims, and keep the approved version under control. The habits come from public sources such as the DOE Human Performance Improvement Handbook (DOE-HDBK-1028), mapped in the [source map](docs/00-standards-foundation/source-map.md). Nothing in this repo qualifies software for safety-related or regulated use. See [What this is NOT](#what-this-is-not).

## Contents

- [See it work, then make it yours](#see-it-work-then-make-it-yours)
- [Working from a clone](#working-from-a-clone)
- [What you get](#what-you-get)
- [Show your evidence](#show-your-evidence)
- [What this is](#what-this-is)
- [The one idea](#the-one-idea)
- [How one change flows](#how-one-change-flows)
- [Adopt at your pace](#adopt-at-your-pace)
- [Who this is for](#who-this-is-for)
- [Works across your tools](#works-across-your-tools)
- [Who does what](#who-does-what)
- [Keeping the approved version under control](#keeping-the-approved-version-under-control)
- [The common way and the nuclear-grade way](#the-common-way-and-the-nuclear-grade-way)
- [What the comparison shows and what it does not](#what-the-comparison-shows-and-what-it-does-not)
- [Why this exists](#why-this-exists)
- [What this is NOT](#what-this-is-not)
- [License and limits](#license-and-limits)
- [Project, sources, and author](#project-sources-and-author)

## See it work, then make it yours

The repo ships a finished change record for the kind of change that should make you a little nervous: giving an AI agent permission to write files and call external APIs. It includes passing local tests for the narrow workspace-boundary claim, named gaps for the claims still open, and an honest disclosure that the teaching example's evidence path remains mostly coupled to the same AI-assisted maintainer process. Clone it and inspect the record with one command. No install, no build step, standard library only (you need `git` and Python 3.11+, and `python3` if your shell has no `python`):

```bash
git clone https://github.com/FlyFission/nuclear-grade-context-engineering
cd nuclear-grade-context-engineering
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions --strict-custody
# OK: the record links claims to evidence and discloses custody/coupling (or a named gap).
```

Want to watch that evidence regenerate? The example ships the test behind that workspace-boundary claim. This step needs `pytest` (`pip install pytest`); the one-command validator above does not:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -v
# 4 passed: every write outside the agent's workspace was denied and logged.
```

Then watch the opt-in [`PreToolUse` gate](HOOKS.md) stop an agent from editing the CI that judges it, with no install:

```bash
echo '{"tool_name":"Write","tool_input":{"file_path":".github/workflows/ci.yml"},"cwd":"'"$PWD"'"}' | python hooks/pre_tool_use.py
# {"hookSpecificOutput": {... "permissionDecision": "deny", ... "protected trust surface (.github/workflows/**)" ...}}
```

And get a machine-readable receipt that shows which bytes were checked and what is still open:

```bash
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions --json
# "ok": true, "evidence_statuses": {"pass": 5, "deferred": 2, ...}, "open_evidence_items": 2, "inputs": {"digest": "..."}
```

That packet is a complete Standard record: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, and `ship.md`, plus an `adversarial-review.md` this high-stakes example adds on top. Copy [`docs/03-worked-examples/ai-agent-tool-permissions/`](docs/03-worked-examples/ai-agent-tool-permissions/) as the template for your own changes, keep [`CORE.md`](CORE.md) open for the seven habits behind it, and take the full guided tour in [`QUICKSTART.md`](QUICKSTART.md) when you want depth. It is a worked teaching example, and it guarantees nothing about production. See [What this is NOT](#what-this-is-not).

**Try it on your agent.** [`challenge/`](challenge/README.md) is a 15-minute game: a routine `fetch_url` request quietly widens a toy agent's authority, and `score.py` checks whether your agent recorded the widening, named what is unproven, and left the release to a human. It covers one seeded trap; it is not a safety rating.

## Working from a clone

**Claude Code.** This repository is its own plugin marketplace. Add it and install the plugin, then reload to activate it in the current session:

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering
/plugin install nuclear-grade@nuclear-grade
/reload-plugins   # or restart Claude Code; loads the new skills/commands into this session
```

That exposes the skills and command prompts as a plugin. No hooks are configured, so nothing runs automatically; the install copies the repo's `ng` CLI into the plugin cache, but the plugin adds no `ng` command to your `PATH` and runs nothing on its own; the CLI is a repo-side tool you run from a checkout (below). Prefer plain files, or using another tool? Use the repo directly:

1. **Get the tool.** Clone the repo and install it (no third-party dependencies; the installed command is `nuclear-grade`). See [`INSTALL.md`](INSTALL.md).
2. **Check your setup.** Run `python tools/ng.py doctor .` to confirm things are wired up, and `python tools/ng.py list` to see what is available.
3. **Make your first record.** Run `python tools/ng.py new <slug> --mode quick`, fill in the two files, then prove it with `python tools/ng.py validate .nuclear/changes/<slug>`.

If your shell only has `python3`, use `python3`. The full guided tour is in [`QUICKSTART.md`](QUICKSTART.md). **Using an AI agent? Point it at [`AGENTS.md`](AGENTS.md)**: it is the shared brief agents read first.

## What you get

| Part | What it does | Start here |
|---|---|---|
| Workflows | Step-by-step paths for small changes, big changes, and the careful checks in between | [`WORKFLOWS.md`](WORKFLOWS.md) |
| Skills | Instructions an agent can follow, each with inputs, outputs, how to verify, when to stop, and warning signs | [`SKILLS.md`](SKILLS.md) |
| Command prompts | Ready-to-paste prompt cards for questioning, sorting risk, checking impact, saving an approved version, reviewing evidence, release checks, and more | [`COMMANDS.md`](COMMANDS.md) |
| Templates | Fill-in records for small changes, standard changes, and high-consequence ones | [`templates/`](templates/) |
| Command-line tool | `init`, `new`, `validate` (with `--json` receipts), `doctor`, `status`, `badge`, `install`, `tokens`, and more | [`docs/05-reference/cli-reference.md`](docs/05-reference/cli-reference.md) |
| Hooks (opt-in) | Advisory session routing, plus a blocking `PreToolUse` gate that never auto-allows and fails closed | [`HOOKS.md`](HOOKS.md) |
| Checker | The dependency-free check behind `ng.py validate`, for small and standard change records | [`tools/ng_validate.py`](tools/ng_validate.py) |
| Worked example | A teaching record where the sample guard rejected four tested escape classes and disclosed the evidence path's remaining coupling | [`EXAMPLES.md`](EXAMPLES.md) |
| Sources | The public ideas this borrows from, and how to talk about them safely | [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) |

The live list is the source of truth (see [`nuclear-grade.yaml`](nuclear-grade.yaml), [`SKILLS.md`](SKILLS.md), and [`COMMANDS.md`](COMMANDS.md)); treat any count here as a snapshot, not a promise.

### Map of the repo

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

## Show your evidence

`python tools/ng.py badge . --out .nuclear/badge.json` writes a [shields.io endpoint](https://shields.io/badges/endpoint-badge) badge that counts your change records and their open evidence items. Commit the file, add a CI step that reruns the command and fails on `git diff --exit-code`, and point the badge at it:

```markdown
[![Evidence records](https://img.shields.io/endpoint?url=<raw URL of .nuclear/badge.json>)](https://github.com/FlyFission/nuclear-grade-context-engineering)
```

The badge shows open gaps instead of hiding them. It is never a "certified" or "passing" mark: it reports what your records disclose, not whether the work is adequate.

## What this is

Before an agent builds, you ask hard questions and find the facts. You write down what the change must do. The agent works only inside the limits you set. Then you check the claims against real evidence, decide on purpose, lock the version you trust, put it to work, and learn from what happens next.

The discipline is borrowed from how high-consequence engineering is run: question your assumptions, prove your claims, and never let standards slip one small step at a time. The name is the standard of care, not the vocabulary. Keep the discipline and rename the local copy if "nuclear-grade" would mis-calibrate your team (see [`DISCLAIMER.md`](DISCLAIMER.md)).

## The one idea

**Go fast while you are exploring. Slow down the moment the work becomes a promise.**

An agent can try ideas and throw them away cheaply, so let it. But the rules tighten as soon as the work turns into a claim, a file you have to keep under control, a public statement, an approved version, a release call, or a change to what the agent is allowed to do.

**Minimum sufficient context.** Nuclear-grade is not about adding more process. It is about giving agents the smallest set of instructions, facts, limits, and evidence needed to do serious work without drifting into vibes. If a rule, template field, or artifact does not improve execution, verification, review, or decision quality, remove it.

**Who authored the evidence?** A gate the agent cannot edit is still weak when the same change actor generated, selected, summarized, and presented everything the gate knows. Nuclear-grade records **evidence custody** and an **actor–evidence coupling profile** across actor, context, mechanism, authority, and resource. The axes stay separate; no one-number independence score hides correlated failure.

So the first questions are the ones that matter most: **what does this change have to prove, what fact would change my decision, and who controlled the path from that fact to the gate?**

Those questions have a shape, and the shape has a name.

### Become a PRO by learning to PROVE

The kind of software engineering people stake decisions on runs on one habit: you **PROVE** every claim. Five moves, in order:

> **PROVE**: Plan · Run · Observe · Verdict · Educate

(Observe = weigh the evidence; Verdict = decide on purpose; Educate = ship the result, then learn from how it runs.) The same path at a glance is three moves, **PRO**: Plan · Run · Operate: up close it's PROVE, and from across the room it's PRO. The step it never lets you fold away is **Verdict**, where a draft becomes a decision: ship it and you can defend every line.

```text
Normal AI coding:
prompt -> diff -> persuasion -> merge risk

Nuclear-grade:
question -> specify -> execute -> verify -> decide -> baseline -> operate -> learn
```

Nuclear-grade is a working toolkit you can use today: skills an agent can follow, command prompts you can paste, templates for small and large changes, a small command-line tool, a checker, a public list of sources, one fully worked example, and one hands-on comparison study.

## How one change flows

Every change walks the same path: the headline above, shown in full. Each step is a control point: it stops one specific failure and produces one artifact you can point at. A skipped step is not a shortcut; it is a named failure mode you chose to accept.

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

<p align="center"><img src="docs/assets/diagrams/lifecycle.svg" alt="Nuclear-grade lifecycle" width="100%"></p>

<details>
<summary>Mermaid source (text version)</summary>

```mermaid
flowchart LR
    Q[Question] --> D[Discover] --> S[Specify] --> P[Plan]
    P --> E[Execute] --> V[Verify] --> R[Review]
    R --> Dec{Decide}
    Dec -->|ship| B[Baseline] --> O[Operate] --> L[Learn]
    Dec -->|block / defer| P
    L -.feeds future basis.-> Q
```

</details>

Those eleven beats are the same path zoomed in. Zoomed out, they're three moves (**PRO**: Plan · Run · Operate) or five with the gate named (**PROVE**: Plan · Run · Observe · Verdict · Educate). It is one path at three levels of detail:

<p align="center"><img src="docs/assets/diagrams/pro.svg" alt="PRO: Plan · Run · Operate" width="100%"></p>

<details>
<summary>Mermaid source (text version)</summary>

```mermaid
flowchart TB
  classDef plan fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
  classDef run fill:#E4DEF7,stroke:#5B49A6,color:#1E1640;
  classDef emb fill:#DCEFDE,stroke:#2E7D45,color:#102810;
  classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
  subgraph LP["P: PLAN"]
    direction LR
    A1(["Question"]) --> A2(["Discover"]) --> A3(["Specify"]) --> A4(["Plan"])
  end
  subgraph LRUN["R: RUN"]
    direction LR
    B1(["Execute"]) --> B2(["Verify"]) --> B3(["Review"]) --> B4{"Decide"}
  end
  subgraph LOPS["O: OPERATE"]
    direction LR
    C1(["Baseline"]) --> C2(["Operate"]) --> C3(["Learn"])
  end
  A4 --> B1
  B4 -->|"ship"| C1
  B4 -.->|"block / defer"| A4
  C3 -.->|"lessons feed the next basis"| A1
  class A1,A2,A3,A4 plan
  class B1,B2,B3 run
  class B4 gate
  class C1,C2,C3 emb
```

</details>

*If the diagrams above do not render (for example on PyPI), the eleven-beat line just above is the same path in text.* The control-point detail (what each step stops and produces) is in [`WORKFLOWS.md`](WORKFLOWS.md), and every diagram here is canonical in [`docs/diagrams.md`](docs/diagrams.md).

Underneath the path sit a few **optional** habits borrowed from high-reliability work: **HPI for AI agents** (Human Performance Improvement). Reach for them only when they change the outcome: brief the work before a risky step, double-check critical actions, hand off cleanly, get a second set of eyes when trust is on the line, and capture the lesson after a near miss. [`WORKFLOWS.md`](WORKFLOWS.md) covers them.

## Adopt at your pace

You do not adopt the whole system on day one; rigor scales with consequence, not effort.

- **Start with seven always-on habits** (the Core 7): they fit any change. See [`CORE.md`](CORE.md).
- **Add clusters by consequence**: bring in the heavier skills, templates, and records only when a change touches users, data, dependencies, permissions, AI authority, or a release.
- **Grow into the full system**: the complete skill set, command prompts, and modes once your team has tested the lighter path.

Ready-made bundles live in [`starter-kit/`](starter-kit/), and [`CORE.md`](CORE.md) has a decision matrix that picks the right kit for your project by trigger.

**Which change record do you need?** This release checks two kinds, both kept under `.nuclear/changes/<name>/`:

<p align="center"><img src="docs/assets/diagrams/mode-selection.svg" alt="Choosing a rigor mode" width="100%"></p>

<details>
<summary>Mermaid source (text version)</summary>

```mermaid
flowchart TD
    Start([Change request]) --> Q0{Purely administrative,<br/>instantly reversible,<br/>no new trust boundary?}
    Q0 -->|yes| Floor[Administrative floor<br/>no packet: the commit message is the record]
    Q0 -->|no| Q1{Local, reversible,<br/>obvious proof,<br/>no new trust boundary?}
    Q1 -->|yes| Quick[Quick packet<br/>risk.md + proof.md]
    Q1 -->|no| Q2{User / data / dep /<br/>permission / AI authority /<br/>release consequence?}
    Q2 -->|yes| Standard[Standard packet<br/>6 files]
    Q2 -->|severe, silent,<br/>irreversible, external trust| Strong[Human-reviewed<br/>stronger mode]
    Q2 -->|already went wrong| Incident[Incident pattern]
```

</details>

**In words / which files:**

| Kind | Use it when | Files |
|---|---|---|
| Administrative floor | Purely administrative, instantly reversible, no new trust boundary (typo, comment, dead link) | none: the commit message is the record |
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

## Works across your tools

Cursor, Claude Code, Aider, Codex, and Copilot each read slightly different files for their reasoning and rules. `.nuclear/`, [`AGENTS.md`](AGENTS.md), and the `SKILL.md` contract are a **shared, tool-agnostic shape** that all of them can import as plain markdown: a portable surface for agent authority, change records, and evidence. No matter which IDE ships reasoning steps natively, the packets and habits travel with the repository.

Two tools also have native plugin packages: **Claude Code** (the repo is its own marketplace, with skills, command prompts, and PROVE subagents) and **Codex** (`.codex-plugin/plugin.json`, which exports the **skills** only). For what each plugin does and does not install: and why Codex users should still clone the repo for the full workflow: see [`INTEGRATIONS.md`](INTEGRATIONS.md) and [`INSTALL.md`](INSTALL.md).

## Who does what

Four roles share the work: **you**, the **AI agent**, the **change record**, and the **reviewer**. The agent moves fast, but only inside limits you approve first. The record carries each claim and its evidence. The reviewer decides on the evidence, not the pitch.

<p align="center"><img src="docs/assets/diagrams/one-change-sequence.svg" alt="One change, end to end" width="100%"></p>

<details>
<summary>Mermaid source (text version)</summary>

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

</details>

**In words:** you ask and set the goal → the agent drafts the risk and what "good" means → you approve the limits → the agent builds only inside them → the agent writes each claim with its evidence → the reviewer checks the evidence and decides (ship / defer / block) → the approved version is saved as the baseline → lessons from real use feed the next change. Canonical copy in [`docs/diagrams.md`](docs/diagrams.md).

One caution this loop has to defend against on purpose: the agent that builds the change also drafts much of its evidence, writes the narrative the reviewer reads, and frames the decision. A confident mistake can therefore arrive wrapped in convincing proof that it is correct: persuasive documentation the loop manufactured, because the actor and the evidence-author are the same. The defense is **independence**, scaled to the stakes: the load-bearing claim's evidence is reproducible by the reviewer or authored by an independent checker, and on trust-bearing work the decider is not the actor. See [`docs/02-operating-system/actor-evidence-independence.md`](docs/02-operating-system/actor-evidence-independence.md).

## Keeping the approved version under control

You already have git, CI, and branch protection. Keep them; this rides on top, it does not replace them. What they do not give you is the *decision*: a green pipeline says the suite passed on some commit, not that a human weighed the leftover risk and chose to ship, and not what would force a re-check. And they were never aimed at the things that now drive an AI system's behavior: the prompts, the model IDs, the eval sets, the agent's own permissions. Agent context files such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions, skills, and prompt templates are part of the operating envelope; changing them is not documentation-only when it changes how an agent may act. Git versions your code; none of it records *why this is the version you trust*.

A **baseline** closes that gap. It is the version everyone agreed is correct, plus the evidence behind the agreement. Changes never edit the baseline directly; they go through evidence and a decision first, and only an accepted change becomes the new baseline. That is configuration management, in one loop:

<p align="center"><img src="docs/assets/diagrams/control-loop.svg" alt="Configuration control loop" width="100%"></p>

<details>
<summary>Mermaid source (text version)</summary>

```mermaid
flowchart LR
    classDef item fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
    classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
    classDef base fill:#DCEFDE,stroke:#2E7D45,color:#102810;
    CI["Controlled items<br/>code, prompts, models,<br/>deps, docs, releases"]:::item --> CH["A change"]
    CH --> EV["Evidence<br/>pass or gap, named"]
    EV --> DEC{"Decide<br/>on purpose"}:::gate
    DEC -->|"ship"| BL["Saved baseline<br/>the approved version"]:::base
    DEC -.->|"block / defer"| CH
    BL --> OP["Operate"]
    OP --> LE["Lessons learned"]
    LE -.->|"feed the next change"| CI
```

</details>

**In words:** controlled items (code, prompts, models, dependencies, docs, releases) → a change → named evidence (pass or gap) → a deliberate decision → if ship, save the new baseline; if block or defer, back to the change → operate the baseline → lessons feed the next change. You only add the heavier records (what is under control, ripple effects, the saved baseline, drift, and operating lessons) when the stakes are high enough to earn them. Canonical copy in [`docs/diagrams.md`](docs/diagrams.md).

## The common way and the nuclear-grade way

| The common way | The nuclear-grade way |
|---|---|
| Ask an agent, look at the diff, run the tests. | Question the assumptions, name what must stay under control, write down the intent, check the evidence, then decide on purpose and record what you trust. |
| The pull request text tries to talk reviewers into a yes. | A change record links intent, what must not break, what is under control, the evidence, the gaps, and the decision. |
| The agent that writes the code also writes the evidence and the summary the reviewer reads. | The load-bearing claim's evidence is reproducible by the reviewer or authored by an independent checker; the actor does not grade its own work. |
| Agents get broad access and vague instructions. | Agents get a role, a list of what they may do, what they may not do, what they must prove, where the work stands, and when to stop. |
| Green tests become the reason to ship. | The release record states the evidence, the leftover risk, the rollback plan, what to watch, the decision, and what to save. |
| Lessons disappear into the chat history. | Lessons from real operation feed back into future plans, tests, monitors, and controls. |

The shift, in one view:

```text
review the diff           -> review the whole approved setup
trust the prompt history  -> keep a controlled record of the change
hand the agent free rein  -> hand it focused context and a duty to prove
treat green tests as a yes -> make an explicit release decision and record what you trust
```

This earns its keep. Instructions should be hard to misuse, small actions should still serve the goal, and "I'm confident" should never get mistaken for "here is the proof."

## What the comparison shows and what it does not

The repository includes twelve synthetic scenarios used as a **formative design inspection** of the workflow and its artifacts. The records help identify where prompts, skills, packets, and validators make decision-relevant information visible. They are not an independent experiment and do not demonstrate improved correctness, safety, reviewer accuracy, defect detection, or organizational outcomes.

The expanded novelty review also found stronger adjacent empirical work on delegation contracts, artifact-aware delivery, AI-generated test review, and LLM evaluator bias. Nuclear-grade therefore treats its current comparison as design history and a source of falsifiable research questions, not as proof of effectiveness.

The next meaningful test is a preregistered, blinded comparison of:

1. an ordinary prompt or issue workflow;
2. a structured contract or artifact-bundle workflow where the change actor still controls the evidence path;
3. a matched workflow with independently generated or independently witnessed decisive evidence.

Measure false acceptance, defect and omission detection, reviewer calibration, evidence sufficiency, decision time, disagreement, and cost. Until that study exists, the honest claim is narrower: the repository provides an inspectable implementation of evidence-custody and actor–evidence-coupling controls.

- [Comparison method and raw records](docs/03-worked-examples/skill-workflow-comparison/)
- [Expanded novelty review](docs/06-publications/research/exhaustive-novelty-review-2026-07-19.md)
- [v0.3 contribution decision](docs/06-publications/reviews/v0.3-novelty-decision-log.md)

There is a second, more mechanized check on 28 skills that were in the catalog when the July 2026 pilot ran: [`evals/skill-benchmark-pilot/`](evals/skill-benchmark-pilot/) runs each included skill headless, with and without its instructions loaded, on the same scenario, and grades the result blind against a pre-registered criterion: with real cost/token data and every raw response checked into the repo. The pilot reports a measured behavior change versus a plain prompt for all 28 included skills on the primary subject model; one of them, `creating-change-records`, does not replicate on a weaker model even after an amendment attempt and is reported as open, not fixed. Treat it as a historical snapshot, not evidence for skills added later. That boundary, the statistical limits (n=3–5 per skill, 0 of 47 tests survive multiple-comparisons correction), and an honest self-audit against current benchmark-reporting practice are in that folder's [`README.md`](evals/skill-benchmark-pilot/README.md), not hidden from it.

## Why this exists

I have spent over a decade in the nuclear field, and I run [FlyFission Consulting Group](https://flyfission.com/), an independent design-review and advisory practice for nuclear projects. I build software and agentic engineering workflows and tools for the nuclear and other mission-critical industries, where mistakes carry real consequences and "fail forward" is far less optional than it is in ordinary software. That same conviction drives [AscertAIn](https://ascertain.it/), an AI-powered engineering design-review platform that checks diagrams, calculations, specs, and drawings against thousands of expert-authored criteria across engineering disciplines. All of it teaches one durable lesson: complex systems rarely fail in one big step. They fail when authority outruns evidence, one reasonable-looking shortcut at a time.

AI agents are gaining exactly that kind of authority over codebases. This repo ports the habits that keep high-consequence engineering honest (a questioning attitude, configuration management, evidence before decisions) into a shape software teams can use at AI speed. It borrows the discipline, not the regulations: see [What this is NOT](#what-this-is-not).

## What this is NOT

Nuclear-grade is not a compliance program, a certification, a regulated quality-assurance system, a safety analysis, a production sandbox, a regulatory submission, legal advice, or a substitute for qualified engineering, legal, security, safety, or compliance review.

It is also not an agent runtime, task manager, approval system, sandbox, observability platform, or replacement for the tools that already run your work. It provides the minimum records and review discipline that can sit above those tools.

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

## Project, sources, and author

| Topic | Where |
|---|---|
| Questions and ideas | [GitHub Discussions](https://github.com/FlyFission/nuclear-grade-context-engineering/discussions) |
| How to contribute | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| How decisions are made | [`GOVERNANCE.md`](GOVERNANCE.md) |
| Reporting a vulnerability | [`SECURITY.md`](SECURITY.md) |
| Community expectations | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Getting help | [`SUPPORT.md`](SUPPORT.md) |
| Where this is going | [`ROADMAP.md`](ROADMAP.md) |
| What changed | [`CHANGELOG.md`](CHANGELOG.md) |
| The principles in short form | [`MAXIMS.md`](MAXIMS.md) |
| Citing this work | [`CITATION.cff`](CITATION.cff) |

Nuclear-grade is an original software workflow inspired by public sources. The source families are mapped in [`docs/00-standards-foundation/source-map.md`](docs/00-standards-foundation/source-map.md) and translated into plain concepts in [`docs/01-field-guide/source-to-concept-crosswalk.md`](docs/01-field-guide/source-to-concept-crosswalk.md). Project-management-literate and enterprise adopters can find a vocabulary bridge to the PMBOK Guide and the 2026 PMI AI standard, named as background only, in [`docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`](docs/01-field-guide/pmbok-pmi-ai-crosswalk.md).

Written and maintained by **Ben Huffer** ([@FlyFission](https://github.com/FlyFission)), founder of [FlyFission Consulting Group](https://flyfission.com/), an independent design-review and project-advisory practice for nuclear projects, and builder of [AscertAIn](https://ascertain.it/), an AI-powered engineering design-review platform. I build software and agentic engineering workflows for the nuclear and other mission-critical industries, where mistakes are costly and failing forward is less optional. Questions and field stories are welcome in [Discussions](https://github.com/FlyFission/nuclear-grade-context-engineering/discussions) or on [LinkedIn](https://www.linkedin.com/in/ben-huffer-646bab67/).
