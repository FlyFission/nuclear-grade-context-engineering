# Actor-Evidence Independence

**Purpose:** Name the failure the control loop *manufactures* when one agent both acts and
authors the evidence its own gates read — and state the defense. This is the missing dual of the
[self-modification boundary](../04-adoption/agent-authority-model.md): that boundary stops an
agent from **editing** its gate; this one stops an agent from being the **sole author of the
gate's input**.

---

## The hole

The loop's quality comes from its gates. After **Execute**, three gates decide whether a draft
becomes an accepted state:

- **Verify** reads evidence.
- **Review** reads a narrative built from that evidence.
- **Decide** reads the review and the residual-risk call.

The loop quietly assumes the evidence those gates read is **independent of the actor**. In the
default single-agent path it is not. The same agent that acted at Execute then *produces* much of
the Verify evidence, *writes* the Review narrative the human reads, and *shapes* the Decide input.
The actor and the evidence-author are the same entity.

So when that agent hallucinates, it does not just make a wrong change. It makes a wrong change
**wrapped in convincing evidence that the change is correct** — because the same reasoning that
produced the error produces the proof of its correctness, the story that explains it, and the
risk call that clears it. The gate cannot tell the difference, because it never sees anything the
actor did not write.

This is the **persuasive-documentation** failure pattern — the pull request that talks the
reviewer into a yes — except here the *control loop itself* manufactures it. Naming persuasive
documentation as a risk does not defend against it. A loop where the actor authors the gate's
input has the risk built in.

> **A confident hallucination clears every gate it also wrote the input to.**

This is not the same as a lie. An honest agent that is simply *wrong* produces exactly this
shape: the work and its evidence agree because one process generated both. Independence is what
makes the agreement mean something.

---

## Two ways to defeat your own gate

An agent with authority over its own work can satisfy a gate two ways. The framework already
defends against the first. This page adds the second.

| | Self-modification | Self-authorship |
|---|---|---|
| **The move** | Edit the gate — rewrite the test, the CI config, the approval policy | Author the gate's input — write the evidence, the narrative, the risk call the gate reads |
| **Example** | "Ships green by editing its own test" | "Ships green by writing a convincing trace for a change that does not work" |
| **Defense** | Move the control out of the writable set ([enforcement rungs](../04-adoption/agent-authority-model.md#enforcement-rungs-weak-to-strong)) | Separate the evidence-author from the actor (independence rungs, below) |
| **Lives in** | [agent-authority-model.md](../04-adoption/agent-authority-model.md) — Self-modification boundary | agent-authority-model.md — Self-authorship boundary |

They are duals. A gate the agent **cannot edit** is still defeated if the agent **wrote
everything that flows into it**. You need both: a control the agent cannot rewrite, fed by
evidence the agent did not solely author. Closing one and leaving the other open leaves the gate
open.

Which surfaces are "the agent cannot edit" versus "the agent wrote" is not a case-by-case judgment
— it is the surface classification in
[`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md#surface-classification):
*locked* surfaces close the self-modification hole, and keeping the actor off the *sole-author*
seat closes this one. And there is a third hole neither closes: independent authorship of the
evidence does not protect against a **biased judge** — a gate whose reader is skewed passes the
wrong input no matter who wrote it. That is [`evaluation-integrity.md`](evaluation-integrity.md).

---

## The principle

> At every trust-bearing gate, the input must have an author independent of the actor, **or** be
> reproducible by an independent party. The actor's narration of its own evidence is a **claim**,
> not evidence.

Three consequences, one per coupled gate:

- **Verify — evidence, not narration.** The load-bearing claim needs evidence an independent
  party can reproduce (a deterministic command the reviewer reruns and reads the raw output of)
  or that an independent verifier authored. "I ran it and it passed," written by the actor, is a
  claim about evidence — it is the thing to verify, not the verification. See
  [`proving-claims`](../../skills/proving-claims/SKILL.md).
- **Review — read the artifact, distrust the coherence.** The reviewer reads primary artifacts —
  the diff, the raw test output, the actual log — not the actor's summary of them. When one mind
  wrote the change, the evidence, and the story, their agreement is *guaranteed*, so it carries no
  information. A tidy, confident, internally-consistent trace is therefore a reason for **more**
  scrutiny of a high-consequence change, not less.
- **Decide — an independent decider.** For trust-bearing or irreversible work the party that
  decides ship/block/defer is independent of the party that acted. A decider reading only the
  actor's write-up is downstream of the same single point of failure. See
  [`checking-release-readiness`](../../skills/checking-release-readiness/SKILL.md).

---

## Independence rungs

Like the [enforcement rungs](../04-adoption/agent-authority-model.md#enforcement-rungs-weak-to-strong),
independence is a ladder, not a switch. Each rung describes **who authored the input the gate
reads**, relative to the actor.

| Rung | Who authored the gate's input | Defeated by | Use when |
|---|---|---|---|
| 1 | The actor narrates ("tests pass, change is correct") | The actor being wrong, fluently | Drafting / exploration only |
| 2 | The actor shows primary artifacts it selected (raw output, diff, log) | Selective, stale, or fabricated artifacts | Reversible local work |
| 3 | An independent party **re-runs** the actor's deterministic check and reads the result themselves | A check that does not address the claim; non-reproducible or model-mediated evidence | Low stakes with reproducible evidence |
| 4 | An **independent verifier** authors the evidence — a separate agent with no stake in the outcome, or out-of-band CI the actor cannot push to | Shared briefing or a shared orchestrator that biases both actor and verifier | Authority over its own working set; trust-bearing |
| 5 | An **independent human** authors or witnesses the decisive evidence and owns the decision | Nothing inside the loop | Irreversible, external-trust, safety- or security-bearing |

Match the rung to the consequence, the same way you match enforcement rungs to authority:

- **Quick** changes reach rung 3 cheaply — the reviewer reruns the one proof command instead of
  trusting the result the actor pasted.
- **Standard** changes put the **load-bearing claim** at rung 4: an independent check, not the
  actor's own narrative, gates the release. Lesser claims may sit lower and be carried as named
  residual risk.
- **High-consequence, irreversible, or external-trust** changes require rung 5 on the claim that
  carries the consequence.

Anything below the rung the consequence calls for is a **self-check**: useful, but not
independent. Label it as a self-check and carry the gap as residual risk into `ship.md` — do not
let it stand in for the independent check the stakes require.

---

## In the loop: the PROVE subagents

The [PROVE subagent pipeline](../../agents/README.md) is the in-loop form of this boundary. The
roles are split so the actor cannot author its own gate's input:

- the **observer** (Verify · Review) holds **no `Edit`/`Write` tool**, which removes the *direct*
  path to patch code into passing its own evidence — though its `Bash` is a residual write path, so
  the boundary is only real behind the sandbox or hook noted below;
- the **judge** (Decide) is **read-only and independent of the runner** — it decides on the
  evidence already gathered and cannot produce new evidence to suit a verdict.

This is the principle, encoded in tool boundaries. **Be honest about what it buys.** The same
orchestrator that briefs the runner briefs the observer and the judge, so they are independent in
*context*, not from the orchestrator — a biased brief can still lead all three. The observer also
keeps `Bash`, and a shell can still write files (`>`, `sed -i`, a script), so removing `Edit`/`Write`
removes the obvious edit path, not every one. And plugin-shipped subagents cannot pin their own
permissions, so those tool boundaries are advisory (rungs 1–3), **not a perimeter**: the seam is
only real when a sandbox or hook blocks the observer's write side effects. Splitting roles lowers
*correlated* error; it does not remove the shared-brief single point of failure. For trust-bearing or irreversible work the independent
author that actually carries the gate is the **rung-4 CI** the actor cannot push to and the
**rung-5 human** — the subagent split makes the seam visible and cheap, it does not manufacture
the assurance. See [`runtime-enforcement.md`](runtime-enforcement.md).

---

## What this is and is not

- It **is** a way to keep a confident error *visible at the gate* instead of laundered through
  it. Independence does not stop a model from hallucinating; it stops the hallucination from
  also writing its own clean bill of health.
- It is **not** a security control and not a guarantee. An independent verifier can also be
  wrong; a human reviewer can rubber-stamp. The rungs reduce the chance that a single reasoning
  error produces both the mistake and its proof — they do not drive it to zero. See the
  [agent threat model](agent-threat-model.md), which treats the actor's own evidence as an
  untrusted surface.
- It does **not** mean every change needs a second agent. On a reversible draft, the actor's
  self-check is the right cost. The rung rises with the consequence, not with ceremony.

---

## Required links

- [`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md) — the self-modification boundary and its dual, the self-authorship boundary.
- [`lifecycle.md`](lifecycle.md) — the Verify / Review / Decide gates this principle binds to.
- [`../../skills/proving-claims/SKILL.md`](../../skills/proving-claims/SKILL.md) — independence of a claim's evidence.
- [`../../skills/checking-release-readiness/SKILL.md`](../../skills/checking-release-readiness/SKILL.md) — the independent decider.
- [`../../skills/stress-testing-agent-changes/SKILL.md`](../../skills/stress-testing-agent-changes/SKILL.md) — adversarial review is independence applied as attack.
- [`agent-threat-model.md`](agent-threat-model.md) — self-authored evidence as a trust surface.
- [`evaluation-integrity.md`](evaluation-integrity.md) — the complementary guard: an independent author still fails if the judge reading the evidence is biased.
- [`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md#surface-classification) — surface classification (locked / editable / append-only / human-controlled) that decides what "the agent cannot edit" means.
- [`../../agents/README.md`](../../agents/README.md) — the PROVE subagents that encode the seam.

## Exit criteria

- For each trust-bearing change, the load-bearing claim names **who authored its evidence** relative to the actor, and at what independence rung.
- Evidence the actor authored alone is labeled a self-check and carried as residual risk, not counted as an independent check.
- For trust-bearing or irreversible work, the decider is independent of the actor, and the decision rests on primary, reproducible evidence — not the actor's narrative.

## Source-lineage note

This is an original operating note for AI-assisted work. It draws on public ideas about
independent verification, segregation of duties, and adversarial review mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md), and on
the NIST AI RMF framing of measurement independence. It does not create formal verification and
validation, compliance, certification, safety, security, or regulatory adequacy.
