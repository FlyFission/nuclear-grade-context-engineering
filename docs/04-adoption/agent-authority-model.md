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

The rule: **at a trust-bearing gate, the input must have an author independent of the actor, or be
reproducible by an independent party.** The actor's narration of its own evidence is a claim, not
evidence — it is the thing to verify, not the verification.

### Independence rungs (weak to strong)

The dual of the enforcement rungs. Where enforcement rungs ask *where the gate lives* relative to
the writable set, independence rungs ask *who authored the input the gate reads* relative to the
actor.

| Rung | Who authored the gate's input | Agent can defeat by | Use when |
|---|---|---|---|
| 1 | The actor narrates ("tests pass, change is correct") | being wrong, fluently | drafting only |
| 2 | The actor shows primary artifacts it selected (raw output, diff) | selective or fabricated artifacts | reversible local work |
| 3 | An independent party re-runs the actor's deterministic check | a check that does not address the claim; non-reproducible evidence | low stakes, reproducible evidence |
| 4 | An independent verifier authors the evidence — a separate agent with no stake, or out-of-band CI | a shared brief that biases both actor and verifier | authority over its own working set |
| 5 | An independent human authors or witnesses the decisive evidence and owns the decision | nothing in-loop | irreversible or trust-bearing |

Match the rung to the consequence, exactly as with enforcement rungs. Anything below the rung the
stakes call for is a self-check: label it as one and carry the gap as residual risk; do not let it
stand in for the independent check. The full treatment — the three coupled gates, how the PROVE
subagents encode the seam, and the honest limits — is in
[`../02-operating-system/actor-evidence-independence.md`](../02-operating-system/actor-evidence-independence.md).

## Plan-phase vs build-phase authority

Planning and building are different authority phases, and naming the line keeps a
read-only planner from sliding into an unreviewed writer. During the question,
specification, and plan phases the agent is read-only over product code: its writes are
confined to the change-record packet, and it prepares, but does not take, release
actions. Build authority over product code opens only after the plan clears its
human-approved gate (the `plan.md` review checkpoints — Requirements / Design / Tasks
approved). This is the self-modification boundary above, applied in time: the control
that approves the plan must sit where the planning agent cannot rewrite it. See the
agent-drafts-spec workflow in `CORE.md`.

## Exit criteria

Agent authority is acceptable when a reviewer can see six things: what the agent was allowed to do, what it actually changed, what evidence it produced, what it was forbidden to claim, **where the controls that gate its work live relative to its writable set** (rung 4 or higher when the agent has authority over its own tests, prompts, or CI), and **who authored that evidence relative to the actor** (independence rung 4 or higher on the load-bearing claim when the work is trust-bearing — the actor's own narrative is not the independent check).

## Source-lineage note

This model is an original workflow pattern. Public sources on AI risk, secure development, configuration, and software assurance shaped it. Those sources are mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
