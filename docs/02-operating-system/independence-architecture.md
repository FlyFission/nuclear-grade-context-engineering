# Independence Architecture

**Purpose:** Say what actually makes a second check independent, so "we had a reviewer"
is not mistaken for independence. This page gives a single home to ideas the repo already
applies in scattered form — it consolidates and extends the control-stack paragraph in
[`configuration-management.md`](configuration-management.md) and the forceful-backup rule in
[`authority-and-intent.md`](authority-and-intent.md); it does not replace them.

**Boundary:** Bounded software-workflow translation. It does not create formal verification
and validation, compliance, certification, or any safety, security, or regulatory guarantee.

---

## Independence is not one dial

A check counts as independent only on the axis you actually varied. Name three:

- **Technical independence** — the check uses a different method, not a re-run of the
  builder's own tests. A second pass by the same agent, in the same context, on the same
  model inherits the same blind spots; it is one barrier wearing two hats, not two.
- **Managerial independence** — the reviewer's scope and its authority to block are not set
  by the thing under review. If the orchestrator that briefed the builder also tells the
  judge what to look at and whether to accept the verdict, the judge is captured even on a
  different model. (See the judge's own note in [`../../agents/judge.md`](../../agents/judge.md).)
- **Financial independence** — for agents this is the **budget axis**: a verifier whose
  token or time budget the builder (or a deadline) controls can be starved into a shallow
  pass. A rushed or truncated judge is captured. Protect the verifier's budget, or let it
  block for lack of room to decide.

A reviewer can be independent on one axis and blind on the others. High-consequence work
needs all three named, not assumed.

## Diversity, not repetition

An LLM defect is **systematic**: the same model, on the same prompt, in the same context,
fails the same way every time. So "run it twice," "sample and vote," or "have the agent
check its own work" is redundancy *without diversity* — structurally unable to catch the
model's own errors. Real independence requires a named **diversity axis**: a different model
family, a different mechanism (a test, a type check, static analysis), or a human. If you
cannot name the axis you varied, treat the two checks as one. This is the failure-mode-level
reading of the control stack in [`configuration-management.md`](configuration-management.md).

## Decomposing checks: when two cheap checks replace one expensive check

It is legitimate to satisfy a high-rigor requirement with two lower-rigor checks — but only
if you can state **why they cannot fail together**. Two LLM checks from the same model family
on the same prompt are common-cause-coupled and do not decompose. A unit test plus a type
check do decompose: different mechanisms, different blind spots. The test for a substitution
is one sentence — *name the common-cause analysis* — and if you cannot, the decomposition is
on paper only.

## Qualify what you rely on to check

A tool or agent that builds or verifies your work is itself a risk, and the rigor it must
earn scales with **how much you rely on it**. The sharp case: the moment you drop the
independent human check and lean on an agent to *catch* errors, that agent has become a
verification tool whose qualification must rise to match the reliance — exactly where
LLM-as-judge is weakest (self-preference, inflated scores for same-family output). Removing
the backstop does not remove the work; it transfers the work onto qualifying the agent. "We
have guardrails / the agent reviews itself" is the unqualified-tool trap.

## Grading independence by mode

Independence is graded, not binary:

- **Quick** — a self-check is enough; the work is local and reversible.
- **Standard** — technical independence: a different method or reviewer, not a re-run.
- **Nuclear / Tier 0** — all three axes named, a stated diversity axis, and the verifier
  backed by the rung-4 CI gate and a human (see [`critical-systems.md`](critical-systems.md)).

Red flag at any tier: *the work under review controls what the reviewer examines, how long
it runs, or whether its verdict is accepted.*

## How it connects

- [`configuration-management.md`](configuration-management.md) — the control stack and the
  "layers only add up when they fail independently" rule this page expands.
- [`authority-and-intent.md`](authority-and-intent.md) — forceful backup and stop-work.
- [`actor-evidence-independence.md`](actor-evidence-independence.md) — the managerial axis applied
  to the verify/decide step: the decider and the load-bearing evidence are independent of the
  actor that produced the change.
- [`program-self-assessment.md`](program-self-assessment.md) — independent review scaled to
  release-bearing outcomes.
- [`../../skills/deciding-who-decides/SKILL.md`](../../skills/deciding-who-decides/SKILL.md),
  [`../../skills/double-checking-before-acting/SKILL.md`](../../skills/double-checking-before-acting/SKILL.md)
  — placing authority and getting a forceful backup.

## Source-lineage note

Original Nuclear-grade operating doc. Concept lineage: the three independence axes
(technical, managerial, financial) from NASA SWE-141; tool/agent qualification proportional
to reliance from NASA SWE-136; the diversity taxonomy from NUREG/CR-6303; independent,
diverse protection from NIST SP 800-160 Vol. 1/2; and independent verification from
DOE-HDBK-1028-2009 — all mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). No
compliance claim is made.
