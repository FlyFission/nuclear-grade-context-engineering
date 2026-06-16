# Core habits and the decision matrix

A strategic spine for adopting Nuclear-grade *without* adopting all of it.

The full system has 27 skills, command prompts, templates, a checker, change-control packets,
governance docs, and an operating model. Most projects need a few of those at once. This page
names the **Core 7** habits every disciplined AI-agent change uses, and the **decision matrix**
that says which **ancillary cluster** to invoke for which kind of change.

Default is Core only. Ancillaries fire by trigger, not by default.

---

## The one idea

> Go fast while you are exploring. Slow down the moment the work becomes a promise.
> *(see [`README.md`](README.md) — "The one idea")*

The Core 7 are the habits that make that slowdown cheap.

---

## The Core 7

**Three always-on dispositions.** Every change uses these, no matter how small.

| # | Skill | What it carries |
|---|---|---|
| 1 | [`questioning-attitude`](skills/questioning-attitude/SKILL.md) | The one fact that would change the decision. |
| 2 | [`rating-change-risk`](skills/rating-change-risk/SKILL.md) | Quick / Standard / stronger — the fork that sets every downstream cost. |
| 3 | [`proving-claims`](skills/proving-claims/SKILL.md) | Every claim maps to evidence, a gap, or an explicit non-claim. |

**Four cut-point habits.** Universal as patterns; fire at specific moments.

| # | Skill | Fires when |
|---|---|---|
| 4 | [`double-checking-before-acting`](skills/double-checking-before-acting/SKILL.md) | An irreversible cut-point is about to happen — file write, broad command, credential use, model swap, public claim, release action. |
| 5 | [`staying-on-mission`](skills/staying-on-mission/SKILL.md) | Work drifts, the same fix repeats, or standards slip one small step at a time. |
| 6 | [`checking-release-readiness`](skills/checking-release-readiness/SKILL.md) | A change approaches merge or release. Ship / block / defer / ship-with-named-risk — pick one and back it. |
| 7 | [`learning-from-experience`](skills/learning-from-experience/SKILL.md) | Something went wrong or nearly did, and a safeguard should change. |

**Core habits are dispositions, not artifacts.** Their cost matches the change. 30 seconds of
thought on a tiny edit. Longer on a hard one.

---

## The decision matrix

Scan the triggers. For every "yes," invoke that cluster. Default is Core only.

| When this is true... | ...invoke this cluster | Skills |
|---|---|---|
| **Every change** (no trigger required) | **Core** | the 7 above |
| Agent has write / run / network / approval authority over its own working set | **Agent authority** | [`deciding-who-decides`](skills/deciding-who-decides/SKILL.md), [`declaring-intent`](skills/declaring-intent/SKILL.md), [`stress-testing-agent-changes`](skills/stress-testing-agent-changes/SKILL.md), [`vetting-outside-code-and-models`](skills/vetting-outside-code-and-models/SKILL.md), [`recording-what-an-agent-did`](skills/recording-what-an-agent-did/SKILL.md), [`briefing-an-agent`](skills/briefing-an-agent/SKILL.md), [`handing-off-work`](skills/handing-off-work/SKILL.md) |
| You produce controlled artifacts — packets, baselines, multi-PR threads, owned configurations | **Configuration management** | [`creating-change-records`](skills/creating-change-records/SKILL.md), [`choosing-what-to-control`](skills/choosing-what-to-control/SKILL.md), [`checking-what-a-change-affects`](skills/checking-what-a-change-affects/SKILL.md), [`recording-a-known-good-version`](skills/recording-a-known-good-version/SKILL.md), [`closing-stale-packets`](skills/closing-stale-packets/SKILL.md), [`breaking-down-the-work`](skills/breaking-down-the-work/SKILL.md) |
| The change makes public claims about safety, security, compliance, licensing, or provenance | **Claims discipline** | [`checking-legal-and-safety-wording`](skills/checking-legal-and-safety-wording/SKILL.md), [`checking-source-claims`](skills/checking-source-claims/SKILL.md) |
| Production failure, data loss, or agent-caused harm | **Incident & deficiency** | [`responding-to-incidents`](skills/responding-to-incidents/SKILL.md), [`tracking-deficiencies`](skills/tracking-deficiencies/SKILL.md) |
| Repo layout / structure decision, or visible code-quality drift in a diff | **Hygiene** | [`organizing-project-folders`](skills/organizing-project-folders/SKILL.md), [`reviewing-code-quality`](skills/reviewing-code-quality/SKILL.md) |
| Planning a multi-stage AI / agentic workflow (workspace, orchestration, repo convention) | **Workflow architecture** — a composing path, not a new cluster (see [`docs/02-operating-system/agentic-workflow-architecture.md`](docs/02-operating-system/agentic-workflow-architecture.md)) | [`organizing-project-folders`](skills/organizing-project-folders/SKILL.md), [`breaking-down-the-work`](skills/breaking-down-the-work/SKILL.md), [`briefing-an-agent`](skills/briefing-an-agent/SKILL.md), [`recording-what-an-agent-did`](skills/recording-what-an-agent-did/SKILL.md) |

All 27 skills are accounted for: 7 Core + 19 ancillary across 5 clusters + 1 router
([`using-nuclear-grade`](skills/using-nuclear-grade/SKILL.md)). The workflow-architecture
trigger above composes existing skills rather than adding a sixth cluster or a new skill — its
home is the doctrine page, not a new `SKILL.md`.

### What each ancillary trigger feels like in practice

- **Agent authority.** Your agent can write files, run commands, call APIs, hold credentials, or
  approve actions in its working set. This cluster is *main-path*, not overlay, for that adopter
  — the trigger is permanent for you. Start from the worked example at
  [`docs/03-worked-examples/ai-agent-tool-permissions/`](docs/03-worked-examples/ai-agent-tool-permissions/);
  read [`docs/04-adoption/agent-authority-model.md`](docs/04-adoption/agent-authority-model.md)
  (especially its self-modification boundary section).
- **Configuration management.** You have artifacts whose accepted version matters — prompts,
  evals, dependency pins, model identifiers, release notes, public docs. The cluster keeps the
  "what is the version we agreed on, and what would invalidate it" question answerable.
- **Claims discipline.** Your repo says things in public that someone might rely on. The cluster
  keeps wording inside its evidence and away from words it cannot back. See
  [`DISCLAIMER.md`](DISCLAIMER.md) and
  [`docs/00-standards-foundation/compliance-boundaries.md`](docs/00-standards-foundation/compliance-boundaries.md).
- **Incident & deficiency.** Real failures (production outage, data loss, agent did harm) — not
  ordinary bugs. The cluster also covers known problems that will outlive a single change.
- **Hygiene.** Repo layout, naming, and code-quality drift inside a diff. Lightweight; runs
  often.

---

## The agent-drafts-spec workflow

The packet templates ship empty on purpose, but filling them by hand is *not* the intended
loop. The intended loop is:

```text
user prompt
  -> agent drafts risk.md / proof.md from the query
  -> human edits and approves
  -> agent writes code against the approved spec
  -> human reviews via the validator + the Core habits
```

The human is editor and approver, not typist. This is what makes Quick mode feel like a
speed-up rather than a tax.

For a Standard change the loop runs in **stages, with a gate between each** — the agent
drafts a phase, the human approves it, and only then does the next phase open:

```text
requirements draft -> human approves
  -> design draft   -> human approves
  -> tasks/plan draft -> human approves
  -> agent builds against the approved spec
```

Staging keeps a late discovery from silently rewriting an earlier decision, and it gives
the human a small, reviewable artifact at each step instead of one large one at the end.
The gates map to the `plan.md` review checkpoints (Requirements approved / Design approved
/ Tasks approved).

**Caution.** An agent that drafts its own spec *and* self-validates it against a structural
check is the "ships green by editing its own test" trap in new clothing. Trust-bearing specs
need an independent approver — a human, or an out-of-band check the agent cannot rewrite. See
the self-modification boundary section in
[`docs/04-adoption/agent-authority-model.md`](docs/04-adoption/agent-authority-model.md).

---

## Where doctrine lives

Different files hold different layers of guidance. Keep each light.

| Layer | Holds | Loaded |
|---|---|---|
| Always-on context (e.g. `CLAUDE.md`, system prompt) | One-line pointers to the vendored skills + a link to your charter | Always-on |
| Adopter [`AGENTS.md`](AGENTS.md) | Authority boundaries + completion standard | When an agent reads repo guidance |
| `.nuclear/charter.md` | The few lasting rules — authority envelope, mission anchor | Per change |
| Per-task context pack | Role, mode, allowed/forbidden actions, required proof, stop conditions | Per task |

This repo's own [`AGENTS.md`](AGENTS.md) is the reference shape: its **completion standard**
(an agent is not done until it can name files changed, the change record, the evidence, the
handoff used or why it was not needed, the intent declared, the gaps still open, and the
boundary wording it checked) is the strongest exportable artifact. The starter kits ship it
trimmed and `<fill-in>`-marked.

---

## The always-on packaging rule

Vendor each Core skill as a file (e.g. `skills/<name>/SKILL.md`) so its **body loads only when
the skill fires**. In always-on context put only a **one-line pointer per skill** — the
description-sized cost.

The framework's own measurement (see [`docs/05-reference/skills-token-audit.md`](docs/05-reference/skills-token-audit.md)):
the 27 skill descriptions sit at ~104 tokens each (gated 80-500 characters), and the ~35k of
skill *bodies* are loaded only on invocation. Pasting a fat doctrine block into always-on
context multiplies that cost across every subagent in a fan-out. The framework rejects that
pattern by measurement.

---

## Starter kits

Files beat documentation. Commands beat files. Three drop-in directories:

- [`starter-kit/core/`](starter-kit/core/) — minimum universal kit (Core 7 pointers,
  `AGENTS.md` skeleton, `.nuclear/charter.md` skeleton, Quick templates).
- [`starter-kit/agent-authority/`](starter-kit/agent-authority/) — Core + the Agent-authority
  cluster vendored + context-pack template + a pre-filled PR template.
- [`starter-kit/public-claims/`](starter-kit/public-claims/) — Core + the Claims-discipline
  cluster vendored + a boundary-wording note + a DISCLAIMER skeleton.

Each kit's `README.md` states the trigger condition and a five-line "drop this in" command.

---

## What the validator does and does not do

`python tools/ng.py validate` is a structural lint — it checks that required sections are
present, the placeholder marker is gone, internal links resolve, evidence statuses are set,
and public wording stays inside its boundary. It is not a judgment on whether the code does
what the change record claims. That judgment is [`proving-claims`](skills/proving-claims/SKILL.md)
plus [`checking-release-readiness`](skills/checking-release-readiness/SKILL.md) plus a human
review. See [`docs/02-operating-system/validators.md`](docs/02-operating-system/validators.md)
("human judgment decides engineering adequacy; the validator checks whether the packet exposes
the evidence needed for that judgment").

---

## A note on tone

"Nuclear-grade" names the *standard of care*, not a compliance claim (see
[`DISCLAIMER.md`](DISCLAIMER.md)). When you adopt this, you do not have to adopt the
vocabulary. If the name would mis-calibrate your team — or sound like an assurance claim you
cannot back — rename the local copy. Keep the discipline; drop the branding.

---

## Source-lineage note

This page is an original synthesis of patterns from the wider Nuclear-grade repository. It
does not create assurance, certification, audit evidence, or any guarantee about how a system
should behave. See [`DISCLAIMER.md`](DISCLAIMER.md) and
[`docs/00-standards-foundation/`](docs/00-standards-foundation/) for the boundary discipline
this page sits inside.
