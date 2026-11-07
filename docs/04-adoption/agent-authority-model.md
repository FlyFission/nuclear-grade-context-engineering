# Agent Authority Model

**Purpose:** Spell out what an AI agent is allowed to do before it can cause any side effects.

## Authority dimensions

| Dimension | Questions |
|---|---|
| Files | What may the agent read, create, modify, or delete? |
| Commands | What commands may run locally? |
| Network | May the agent browse, call APIs, fetch packages, or upload data? |
| Credentials | May the agent see, use, rotate, or request secrets? |
| Review | What human approval is required before changes, commits, pushes, or release? |
| Release | May the agent prepare, tag, merge, deploy, or publish? |
| Claims | What public claims are forbidden? |

## Context pack requirement

When an agent gets real authority, write a context pack that states:

- objective;
- decision question;
- packet path;
- allowed and forbidden actions;
- approval gates;
- required proof;
- stop conditions.

## Denial rule

If an action goes beyond what the agent is allowed to do, the agent must stop. It must record the approval it needs, or the path to escalate.

At a cut point, the agent must pause before acting if any of these is unclear: the exact target, the expected result, the forbidden claim, or the stop condition. A cut point includes file writes, broad commands, public claims, changes to trust in a dependency, model, or API, release actions, and other steps that are hard to undo.

For an **unattended** agent there is no human to ask mid-run. "Ask first" degrades to **stop, record the needed approval, and halt** (or hard-block the action). Design the gate as block / escalate / record, not as a prompt for permission that nothing will answer.

## Self-modification boundary

An agent with write or run authority over its own tests, prompts, approval policy, or CI config can satisfy a gate by changing the gate. "Ships green by editing its own test" is not proof; it is the control failing silently. A guard inside the agent's writable working set is not enforcement — it is a suggestion the agent can edit.

The rule: the control that decides whether the agent's work is acceptable must sit where the agent cannot rewrite it.

### Enforcement rungs (weak to strong)

| Rung | Mechanism | Agent can defeat by | Use when |
|---|---|---|---|
| 1 | Advisory print or log | ignoring the output | drafting only |
| 2 | Exit code in a script the agent can edit | editing the script | reversible local work |
| 3 | Tests the agent can edit | rewriting the test | low stakes, trusted loop |
| 4 | Out-of-band CI the agent cannot push to | nothing in-repo | authority over its own working set |
| 5 | Branch protection or required human review | nothing | irreversible or trust-bearing |

Match the rung to the authority. An agent that can edit files at rungs 1-3 has no real gate; promote to rung 4-5 before granting write or run authority over its own controls.

## Self-authorship boundary

The self-modification boundary stops an agent from **editing its gate**. Its dual stops an agent
from being the **sole author of the gate's input**. Both let a confident error clear the gate;
closing one and leaving the other open leaves the gate open.

The trap: the agent acts at Execute, then the same agent produces the Verify evidence, writes the
Review narrative the human reads, and frames the Decide call. A gate it cannot edit is still
defeated when it wrote everything that flows in — because the same reasoning that produced a wrong
change produces the proof, the story, and the risk call that say the change is right. The gate
never sees anything the actor did not author, so it cannot tell a sound change from a confident
hallucination. This is persuasive documentation, manufactured by the loop.

The rule: **at a trust-bearing gate, expose who controlled the evidence path and require a
consequence-appropriate reduction in actor–evidence coupling.** The actor's narration of its own
evidence is a claim, not the verification.

### Actor–evidence coupling profile

Evidence independence is not a linear ladder. Record five axes separately as `coupled`,
`partially separated`, or `separated`, with a concrete basis:

| Axis | Question |
|---|---|
| Actor | Who generated or witnessed the decisive evidence relative to the change actor? |
| Context | Did the verifier reconstruct the case, or inherit the actor's framing and omissions? |
| Mechanism | Do actor and verifier share tests, oracle, model family, prompts, tools, or execution path? |
| Authority | Who controls scope, thresholds, sufficiency, verdict, and apply decision? |
| Resource | Who controls verifier budget, runtime, credentials, storage, and publication of adverse results? |

The profiles form a partial order; do not add or average the axes, and do not assume human
witnessing always dominates diverse deterministic verification. Match the minimum acceptable
profile to consequence. Anything below it is a self-check or a named residual coupling: carry the
gap into the release decision rather than silently counting it as independent. The full treatment
— evidence custody, named evidence patterns, the three coupled gates, and honest limits — is in
[`../02-operating-system/actor-evidence-independence.md`](../02-operating-system/actor-evidence-independence.md).

## Surface classification

The enforcement boundary and coupling profile both turn on one prior question: *of everything the agent
can touch, which surfaces may it change, and how?* Answer it once, up front, by sorting every
artifact the agent can reach into four classes. This inventory exposes where the gate lives and
which parts of the evidence path the actor controls.

| Surface class | The agent may... | Examples | Bound by |
|---|---|---|---|
| **Locked** | not modify at all | tests, CI config, the approval policy, the gate that grades the work | Self-modification boundary; keep at enforcement rung 4–5 |
| **Editable-under-review** | change, but only through the normal change flow | product code, drafts, the packet it is filling | plan-phase/build-phase gate; coupling profile on the load-bearing claim |
| **Append-only** | extend, never rewrite | logs, lessons/OPEX, the deficiency register, baselines grown by delta | the append-only-delta rule in [`../02-operating-system/durable-memory.md`](../02-operating-system/durable-memory.md) and [`../02-operating-system/context-window-discipline.md`](../02-operating-system/context-window-discipline.md) §3 |
| **Human-controlled** | not touch; only a human mutates it | the charter, the release/ship decision, credentials and secrets | denial rule; separated authority axis |

Two rules make the classes load-bearing rather than decorative:

- **A gate must never sit in an editable or append-only surface the actor controls.** If the thing
  that grades the work is in the agent's writable set, it is a suggestion, not a gate — promote it
  to *locked* (rung 4–5). This is the self-modification boundary, stated as a placement rule.
- **Append-only is not a soft lock.** "Grow by appended, dated entries; never rewrite" is what keeps
  durable memory from [context collapse](../02-operating-system/context-window-discipline.md). An
  agent that rewrites a lesson log to "clean it up" has defeated the class.

State the class of each reachable surface in the context pack, next to the authority dimensions
above. An agent that cannot name which surfaces are locked, append-only, and human-controlled does
not yet have a bounded authority.

## Plan-phase vs build-phase authority

Planning and building are different authority phases, and naming the line keeps a
read-only planner from sliding into an unreviewed writer. During the question,
specification, and plan phases the agent is read-only over product code: its writes are
confined to the change-record packet, and it prepares, but does not take, release
actions. Build authority over product code opens only after a human explicitly authorizes
execution of the accepted plan. Acceptance of the plan's contents alone is not permission
to act; an approval signal must preserve whether it accepts the artifact, authorizes execution,
or does both. The `plan.md` review checkpoints cover Requirements / Design / Tasks acceptance.
This is the self-modification boundary above, applied in time: the control
that approves the plan must sit where the planning agent cannot rewrite it. See the
agent-drafts-spec workflow in `CORE.md`.

## Exit criteria

Agent authority is acceptable when a reviewer can see six things: what the agent was allowed to do, what it actually changed, what evidence it produced, what it was forbidden to claim, **where the controls that gate its work live relative to its writable set** (enforcement rung 4 or higher when the agent has authority over its own tests, prompts, or CI), and **who controlled the evidence path relative to the actor** (custody plus all five coupling axes on each load-bearing claim; the actor's own narrative is not the independent check).

## Source-lineage note

This model is an original workflow pattern. Public sources on AI risk, secure development, configuration, and software assurance shaped it. Those sources are mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
