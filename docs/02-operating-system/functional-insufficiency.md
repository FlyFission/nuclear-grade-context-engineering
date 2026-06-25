# Functional Insufficiency

**Purpose:** Name the failure where nothing is broken and the outcome is still wrong — the
system did exactly what it was built to do, and the intended function was simply not enough
for the situation. This is the dominant shape of harm from AI systems, and a packet that only
guards against *faults* is blind to it.

**Boundary:** Original software-workflow translation. It does not create formal assurance,
compliance, certification, or any safety, security, or regulatory guarantee.

---

## Harm without a fault

Most of the repo's machinery defends against **faults**: a bug, a bypassed permission, a
corrupted migration — something failed. But an LLM that confabulates a plausible-but-wrong
answer, follows an unsafe-but-reasonable instruction, or handles a slightly novel prompt badly
has **no fault**: it ran in-distribution and did what it was designed to do. The harm came from
the intended function being **insufficient** for that case. You cannot test your way out of this
with "does it fail safely?" checks, because nothing failed.

## The known/unknown map

Sort possible situations on two axes — do you *know* about them, and are they *safe*:

- **Known-safe.** The cases you designed for and verified. Keep them.
- **Known-unsafe.** Cases you know are bad. Engineer them away or guard them. Your red-team
  attack classes (injection, jailbreak, tool misuse) live here.
- **Unknown-unsafe.** Cases nobody wrote a probe for. **This is where real AI risk lives.**
- **Unknown-safe.** Fine by luck; not yet relied upon.

The work is to **shrink the unknown-unsafe region** by dragging unknowns into the known —
through scenario discovery, not just by re-running the probes you already have. "All known
probes pass" says nothing about the frontier.

## Why a passing red-team is not enough

A fixed set of attack probes can only test the **known-unsafe** region, and its coverage
erodes as the model improves and the input space grows. Treating "the red-team is green" as
"the system is safe" mistakes the lit area for the whole map. For high-stakes AI work, add a
**scenario-discovery** step whose exit criterion is coverage of the unknown frontier — new
situations found and judged — not a count of passing known cases.

## In the packet

- In [`../../templates/standard/basis.md`](../../templates/standard/basis.md), split
  **Unacceptable outcomes** into two kinds: **fault-mode** hazards (something breaks — guard
  with failure-mode tests, invariants, rollback) and **performance-insufficiency** hazards
  (nothing breaks and it is still wrong — guard with scenario coverage, evals on the hard
  cases, and human review on the novel ones). Most packets fill only the first today.
- For Nuclear-mode AI changes, make scenario discovery an obligation, and state the exit as
  *coverage of the unknown frontier*, not *all known probes pass*.
- Carry a one-line maxim into review: **no bug is not the same as no hazard.**

## How it connects

- [`../../templates/standard/basis.md`](../../templates/standard/basis.md) — the
  unacceptable-outcomes split.
- [`../../skills/stress-testing-agent-changes/SKILL.md`](../../skills/stress-testing-agent-changes/SKILL.md)
  — known attack classes, now paired with frontier scenario discovery.
- [`activation-thresholds.md`](activation-thresholds.md) — the detectability dimension, read
  for insufficiency as well as faults.

## Source-lineage note

Original Nuclear-grade operating doc. Concept lineage: the framing that some risks are unknown
and others known-but-hard-to-estimate, from NIST AI 600-1 (Generative AI Profile); the erosion
of fixed-probe coverage as systems improve, from public work on capability-based red-teaming
(arXiv:2505.20162); and hazard/failure analysis that names unacceptable outcomes and their
controls, from DOE-STD-3009-2014 — all mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). No
compliance claim is made.
