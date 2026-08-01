# Quality, Verdict, Accountability

**Purpose:** Separate three things this repository already does but has been naming inconsistently. Most arguments about "quality" are actually arguments about which of these three is missing.

**Rule:** A check produces evidence. A person produces a verdict. A packet is what lets that verdict be explained later. Never let one of the three stand in for another.

---

## The three terms

**Quality is a system of checks that produces evidence.** Tests, linters, type checks, `tools/ng_validate.py`, CI, review passes. Quality is a *system*, not a feeling and not a score — it is the machinery whose output is evidence. A check can pass, fail, or be inconclusive. It cannot accept anything. See [`validators.md`](validators.md).

**Verdict is the accountable decision made from that evidence.** Ship / block / defer / ship-with-named-risk on a release; VERIFIED / NOT VERIFIED / INCONCLUSIVE on a review. A verdict has a name attached to it. That is the whole difference: evidence is produced, a verdict is *owned*. See [`../../agents/judge.md`](../../agents/judge.md), [`../../skills/checking-release-readiness/SKILL.md`](../../skills/checking-release-readiness/SKILL.md), and [`../../skills/reviewing-code-quality/SKILL.md`](../../skills/reviewing-code-quality/SKILL.md).

**Accountability is the ability to explain and stand behind the verdict later.** Not who gets blamed — whether the reasoning can be reconstructed months later by someone who was not there. It lives in the packet: `trace.md`, `verification.md`, `ship.md`, the evidence custody record, and the coupling profile. See [`actor-evidence-independence.md`](actor-evidence-independence.md).

**An agent can be delegated the verdict. It cannot be delegated the accountability.** Decision rights may be placed at the edge for reversible, well-evidenced work — that is [`deciding-who-decides`](../../skills/deciding-who-decides/SKILL.md), and the PROVE judge stage is what it looks like in tool form. What does not move with the delegation is the standing behind the call: a named human remains accountable for placing the decision there and for what comes out. This is why the three terms scale differently. Quality scales with the agent. Verdict can be placed. **Accountability never moves** — which is the whole reason it is a separate term rather than a synonym for the other two.

The three terms have separate machinery, which is the clearest sign they are separate things. Quality is checked by `ng validate` and CI. The verdict's *placement* — who holds prepare, recommend, verify, validate, verdict, accept, apply, reopen, and close, and on which evidence — is recorded in [`../../templates/standard/decision-authority.md`](../../templates/standard/decision-authority.md) and structurally checked by `ng validate <packet> --strict-authority`. Accountability's machinery is `--strict-custody`. None of the three checks substitutes for either of the others, and none of them decides adequacy.

---

## What breaks when two of them collapse

| Collapse | What it looks like | Where the doctrine already refuses it |
|---|---|---|
| **Quality mistaken for Verdict** | "CI is green, so we ship." A green pipeline says the checks that exist did not fail. It does not say the checks that exist were the right ones. | [`../../MAXIMS.md`](../../MAXIMS.md) — "CI passing is not a release decision"; [`validators.md`](validators.md) §1 |
| **Verdict without Quality** | A signature on top of nothing — confident acceptance with no evidence underneath. | [`../../skills/reviewing-code-quality/SKILL.md`](../../skills/reviewing-code-quality/SKILL.md) returns INCONCLUSIVE precisely to refuse this, and must name the missing evidence |
| **Verdict without Accountability** | The decision was fine at the time and cannot be reconstructed now. Discovered at the incident review, which is the worst moment to discover it. | [`change-control-packets.md`](change-control-packets.md), [`../../skills/proving-claims/SKILL.md`](../../skills/proving-claims/SKILL.md) |
| **Accountability without Verdict** | A complete, tidy record of a decision nobody actually made. Process theater. | [`modes.md`](modes.md) — the mode exists to force a stated decision, not to generate files |

---

## Why the distinction tightens under AI authorship

An agent can produce checks and evidence at a rate no review capacity matches. A 2026 developer survey (n > 1,100, run by a code-quality vendor, self-reported rather than measured from telemetry) reports that roughly 42% of committed code is already AI-generated or significantly assisted, that 96% of developers do not fully trust AI-generated code to be functionally correct, and that only about half always verify it before committing. Treat the exact figures as survey self-report; the shape — authorship outrunning verification — is what this doctrine responds to.

The asymmetry is the point. **Quality scales with the agent. Verdict does not.** The number of people who can honestly stand behind a decision is unchanged by how fast the evidence arrives. That is why the answer is not more checks; it is keeping the verdict a named, owned act, and keeping the record good enough to defend it later.

It also sharpens the coupling problem. When the agent that wrote the change also authors the evidence, the review narrative, and the framing the decider reads, the verdict is being made from material the actor controls. See [`actor-evidence-independence.md`](actor-evidence-independence.md) and the maxim "a confident hallucination clears every gate it also wrote the input to."

---

## Exit criteria

For any change:

- the checks that ran are named, and what they do *not* cover is stated;
- the verdict is one of the frozen labels, with a name attached — not a summary, not a vibe;
- the packet holds enough that someone absent at the time could reconstruct why the verdict was reasonable on the evidence available then.

---

## Source-lineage note

This page is an original Nuclear-grade synthesis. It names a distinction already carried in the repository's validator principle, release-readiness skill, and judge stage. The AI-authorship figures come from a public vendor-run developer survey registered in [`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md); they are self-reported survey data, not measured telemetry, and the vendor sells a code-quality product. It draws on public human-performance and software-assurance practice mapped in the same source map. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
