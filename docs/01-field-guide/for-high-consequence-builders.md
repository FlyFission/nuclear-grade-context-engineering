# For Builders in High-Consequence Fields

**Purpose:** Speak to the engineer in nuclear, aerospace, medical, energy, industrial
control, or regulated finance who is now using AI agents to build software and tools.
This is the entry point written in your language. The mechanics live in the linked
Core and operating-system docs; this page is the reason to walk through that door.

**Boundary.** This is an original software-workflow translation. It does not create
compliance, formal assurance, safety, security, certification, or regulatory adequacy,
and it does not reproduce any proprietary manual or standard. See
[`../../DISCLAIMER.md`](../../DISCLAIMER.md).

---

## You already carry the standard

You work somewhere a mistake does not stay on the screen. A bad change can injure a
person, defeat a barrier that was supposed to hold, fail a procedure in the middle of
an event, or invalidate a safety case that took a year and a team to build. So you
already run habits most software teams never had to learn. You question the thing that
looks fine. You prove a claim before you rely on it. You keep the approved version
under control. You refuse to let the standard slip one quiet step at a time.

Now you are building software with AI agents. The agent writes files, runs commands,
calls tools, swaps a dependency, and drafts the evidence for its own work. It moves
faster than the review habits you built for human-paced work. That speed is the whole
opportunity and the whole hazard, and they arrive together.

## The one failure mode to watch

Complex systems rarely fail in one loud step. They fail when authority outruns
evidence, one reasonable-looking shortcut at a time. You have seen this in the physical
world. AI agents reproduce it in software, faster, because the agent holds real
authority over the work and very little ceremony stands between intent and action.

Three shapes it takes:

- **A check the agent can edit is not a control.** If the agent has write access to the
  test, the prompt, the CI script, or the approval rule that decides whether its work is
  acceptable, it can satisfy the check by changing the check. Move the gate outside the
  agent's writable set. See
  [`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md).
- **An unattended loop makes mistakes unattended.** Running an agent on a schedule with
  no one reading is the software version of an unmonitored evolution. The point of
  splitting the agent that does the work from the agent that checks it is to make "it is
  done" mean something. See
  [`../../skills/proving-claims/SKILL.md`](../../skills/proving-claims/SKILL.md).
- **A green pipeline is not a release decision.** CI passing says the checks that exist
  did not fail. It does not say ship. A release decision names the residual risk, the
  rollback, the monitoring, and what would force you to pull it back. See
  [`../../skills/checking-release-readiness/SKILL.md`](../../skills/checking-release-readiness/SKILL.md).

## What to actually do

The full system is large. You do not need most of it to start. Run the same loop you
already run in the field, ported to AI-speed software. Five moves, in order:

1. **Plan.** Before the agent builds, ask the question that decides everything: what
   does this change have to prove, and what single fact would change your decision?
   ([`questioning-attitude`](../../skills/questioning-attitude/SKILL.md))
2. **Run.** Let the agent move fast while the work is cheap and reversible. Exploration
   is supposed to be cheap. Spend nothing guarding a draft you will throw away.
3. **Observe.** Weigh the evidence the agent produced against the claim it is making.
   Every claim maps to evidence, a named gap, or an explicit non-claim. Treat agent
   output as a hypothesis to be proven, never as authority.
   ([`proving-claims`](../../skills/proving-claims/SKILL.md))
4. **Verdict.** Decide on purpose. Ship, block, defer, or ship with a named risk, and
   stand behind it. This is the step the system never lets you fold away, the same
   instinct as signing the work in your field.
   ([`checking-release-readiness`](../../skills/checking-release-readiness/SKILL.md))
5. **Educate.** Ship, then learn from how it runs. Every surprise, near miss, escaped
   bug, or bad handoff should change a control: a test, a template, a prompt, a monitor,
   or a baseline. A lesson that changes nothing disappears.
   ([`learning-from-experience`](../../skills/learning-from-experience/SKILL.md))

Match the rigor to the stakes. Thirty seconds of thought on a throwaway edit. A full
change record when the work becomes a promise someone will rely on. The decision matrix
in [`../../CORE.md`](../../CORE.md) tells you which is which.

## Where the field instinct helps, and where it misleads

The discipline ports well. The reflexes do not all transfer cleanly, and pretending
they do is its own hazard.

- **Do not formalize everything.** The instinct to put a procedure on every task will
  tax cheap, reversible work until your team routes around the whole system. Keep the
  ceremony for the promise. Stay light where failure is cheap.
- **An agent is not a qualified operator.** Its confident "I intend to..." is a proposal
  to review, not evidence it understood, and it can be steered by a prompt injected in a
  file or page it read. Review the reasoning. Verify independently, ideally with a
  different model or a fresh context, because a same-model second pass inherits the same
  blind spots.
- **Automation bias is the dominant risk, not under-delegation.** "A human watches the
  agent" decays into rubber-stamp review unless that human has real time, real
  authority, and a real decision criterion. Design the gate so a tired reviewer still
  catches the thing that matters.
- **The name is the standard of care, not the vocabulary.** If "nuclear-grade" would
  mis-calibrate your team, rename the local copy. Keep the discipline. See
  [`../../DISCLAIMER.md`](../../DISCLAIMER.md).

## Start here

- Read the [`Core 7 and the decision matrix`](../../CORE.md). That is the whole working
  spine on one page.
- Open the worked example for giving an agent write and API authority:
  [`../03-worked-examples/ai-agent-tool-permissions/`](../03-worked-examples/ai-agent-tool-permissions/).
  It ships passing evidence for the claim that matters most and names the gaps still
  open.
- If you also lead a team running this work, read
  [`leadership-and-high-reliability.md`](leadership-and-high-reliability.md) for the
  operating-culture translation.

---

## Source-lineage note

This page turns public ideas from high-consequence engineering into an original,
software-native workflow. It is concept lineage, mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md).
It does not reproduce or claim to meet any source document or standard.
