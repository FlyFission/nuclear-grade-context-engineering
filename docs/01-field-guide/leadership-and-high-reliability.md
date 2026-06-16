# Leadership and High-Reliability Operating Culture

**Purpose:** Translate the operating culture of the nuclear-submarine world — Rickover's Naval Reactors discipline and David Marquet's intent-based leadership — into how people and AI agents run software work that matters. This is the narrative home for that translation; the mechanics live in the linked operating-system docs.

**The one lesson.** The useful lesson from the nuclear Navy is not "make software teams more military." It is this: build teams that move fast because they are technically competent, procedurally disciplined where risk is high, brutally honest about reality, and trained to recover when complex systems fail. The same discipline applies when the "operator" is an AI agent with authority over files, tools, dependencies, and releases.

**Boundary.** This is an original software-workflow translation. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy, and it does not reproduce any proprietary book or standard. Sources are concept lineage, mapped in `../00-standards-foundation/source-map.md`.

---

## Distilled doctrine

A nuclear-submarine-inspired software practice operates by these rules. Each maps to a charter article, a skill, or an operating-system doc.

1. Own the full lifecycle — question through operate and learn.
2. Know the system deeply; understanding cannot be delegated (Charter Art. 5).
3. Use formal procedure where failure is expensive; keep lightweight flow where failure is cheap and reversible (Art. 9, 15).
4. Write down intent, assumptions, evidence, and rollback (Art. 8, 18).
5. Push authority to where the information is — bounded, never past a human gate (Art. 17).
6. Let anyone challenge unsafe work; protect bad news (Art. 19).
7. Face facts; report the actual condition, not the hoped-for one (Art. 2, 6).
8. Never normalize a deficiency; raise the deficiency to the standard (Art. 3).
9. Drill and review against real evidence, not theater.
10. Create capability in the next operator, not dependence (Art. 18).
11. Measure to expose reality, not to perform.
12. Treat AI output as a hypothesis to be proven, never as authority.

---

## Control, competence, clarity (for human↔agent supervision)

Marquet's model gives away **control** only as **competence** and **clarity** rise to match. For supervising agents:

- **Control** = decision rights. Push reversible, well-evidenced decisions to the agent at the edge; escalate irreversible, trust-bearing, or thinly evidenced ones. See `../02-operating-system/authority-and-intent.md`.
- **Competence** = demonstrated capability — evals, tests, a track record — not fluent-sounding confidence. For an agent, competence is eval coverage, not character.
- **Clarity** = mission, constraints, and "what good looks like," supplied through context engineering (system prompts, `CLAUDE.md`, success criteria) so the agent can decide well instead of being micromanaged. Clarity is the alignment mechanism that lets decentralized decisions still serve the mission (the commander's-intent analogue).

The pivot move is the intent declaration — "I intend to X because the checks show Y" — which flips the default from *ask permission* to *act unless stopped*, while forcing the actor to make the why and the abort criteria explicit.

---

## Where this breaks down for AI agents (healthy skepticism)

The leadership metaphor is useful scaffolding and actively misleading in specific ways. Adopt these principles only as ways to **increase rigor at trust boundaries** — never to remove a human gate or over-delegate to an agent.

- **An agent is not a person.** "View people as purpose" applies to the humans in the loop, not the agent. Anthropomorphizing an agent's "intent," "competence," or "trust" risks granting it authority it has not earned. These are operational metaphors for system properties (encoded permissions, eval scores, context completeness), not psychological states.
- **Authority is encoded, not felt.** For an agent, "push authority to the information" is a design-time decision about permissions and escalation thresholds, not an in-the-moment act of empowerment.
- **Stated intent is not understanding.** An agent's confident "I intend to…" is a proposal to review, not evidence it comprehended — and it can be hijacked by prompt injection in a file or web page it read. Review the reasoning; verify independently.
- **"Psychological safety" has no agent referent.** Design instead for default uncertainty-surfacing: the agent should escalate, refuse, or flag when confidence is low.
- **Automation bias is the dominant failure, not under-delegation.** "Push authority to the edge and a human watches" degrades into rubber-stamp theater unless the human has real time, authority, and decision criteria. Independent backup must use a different model or context; a same-model second pass inherits the same blind spots.

---

## Anti-patterns (what not to copy)

Copy: rigorous qualification, technical ownership, clear standards, formal communication during risk, peer backup, stop-work authority, root-cause learning, evidence-based reviews, lifecycle accountability, high standards for critical systems.

Do not copy: command-and-control approval for every decision; fear-based leadership; status theater; excessive ceremony for low-risk work; hero worship; secrecy that blocks learning; punishment for surfacing bad news; "process compliance" without technical understanding. The best version is high-trust, high-standards engineering — which is exactly the repo's two-speed model (Art. 15).

---

## The eight mechanisms, mapped to this repo

| Mechanism | Where it lives here |
|---|---|
| Risk-tiered change control | `../02-operating-system/risk-tiers-and-modes.md` (tiers mapped onto modes) |
| Intent-based release protocol | `declaring-intent` skill, `ng-intent`, `templates/golden-path/intent.md` |
| Watchteam backup / stop-work | Charter Art. 19, `double-checking-before-acting`, `../02-operating-system/critical-systems.md` |
| Deficiency log | `tracking-deficiencies` skill, `ng-deficiency`, `../02-operating-system/deficiency-register.md` |
| Evidence-based retrospectives | `learning-from-experience` (Get-Real-Get-Better structure) |
| Service ownership doctrine | framed in `../02-operating-system/critical-systems.md` (doctrine only — this repo governs changes, not org charts) |
| Qualification / level of knowledge | competence-to-act, defined in `authority-and-intent.md` (qualification section): action class → demonstrated competence → revalidation trigger. Change-scoped and agent-facing — this repo evidences competence, it does not run an HR or certification program |
| Operational drills | framed only; adversarial drilling of agent changes is `stress-testing-agent-changes` |

Two of the last three remain deliberately doctrine-only: service ownership and organization-wide operational drills are about how a company staffs and rehearses, not how a change is run. Qualification is the exception — competence-to-act is now defined as a change-scoped, agent-facing mechanism in `../02-operating-system/authority-and-intent.md`, and the durable record an agent learns from between runs is its own doctrine in `../02-operating-system/durable-memory.md`. The line stays crisp: change-scoped and agent-facing learning mechanisms are in scope; a company-wide HR, certification, or training program is not.

---

## Measuring the program (with cautions)

Delivery metrics (DORA: lead time, deployment frequency, change fail rate, failed-deployment recovery time) and reliability practice (SRE: SLOs, error budgets) are useful public reference points. Two cautions are part of the doctrine: DORA itself warns that metrics turned into targets get gamed (Goodhart), and SRE warns that chasing 100% reliability kills innovation. Measure to expose reality, not to perform a number. This repo does not ship a metrics dashboard; it points at these public sources as lineage.

---

## AI-era note

Research on AI-assisted development finds that AI amplifies an organization's existing strengths and weaknesses: weak engineering systems get weaker faster, strong ones scale better. That makes this discipline more relevant, not less. Treat AI output as a hypothesis; require human review for AI-authored critical changes; record why generated code was accepted; and never let AI increase code volume faster than review, testing, and ownership can absorb.

---

## Index

- Decision rights, the intent ladder, release briefs, stop-work: `../02-operating-system/authority-and-intent.md`
- Risk tiers mapped onto modes: `../02-operating-system/risk-tiers-and-modes.md`
- Stabilize-first incident response: `../02-operating-system/incident-response.md`
- SUBSAFE-style critical-systems framing and watch-team roles: `../02-operating-system/critical-systems.md`
- Standing deficiency register: `../02-operating-system/deficiency-register.md`
- Qualification (competence-to-act) and durable memory: `../02-operating-system/authority-and-intent.md`, `../02-operating-system/durable-memory.md`
- Skills: `deciding-who-decides`, `declaring-intent`, `responding-to-incidents`, `tracking-deficiencies`
- Commands: `ng-decide-authority`, `ng-intent`, `ng-incident`, `ng-deficiency`

## Source-lineage note

Original Nuclear-grade field guide influenced by Rickover and Navy nuclear practice, David Marquet's intent-based leadership and leader-leader idea, naval mission-command doctrine, the human-performance practices in DOE-HDBK-1028-2009, public safety-culture traits, and public software-delivery and reliability practice (DORA, SRE) — all as concept lineage, not implemented programs, and mapped in `../00-standards-foundation/source-map.md`. No proprietary text is reproduced. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
