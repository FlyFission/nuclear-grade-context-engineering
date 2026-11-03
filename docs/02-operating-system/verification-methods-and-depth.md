# Verification Methods and Depth

**Purpose:** Give one vocabulary for *how hard* a check looked and *by what means*, so "it was
reviewed" is never mistaken for "it was verified." [`independence-architecture.md`](independence-architecture.md)
answers **who** checked and on which axis they were separate. This page answers the other two
questions a reviewer has to ask: **how deep** did the check go, and **did it reach the answer by a
different route**?

**Boundary:** Bounded software-workflow translation of public nuclear quality and human-performance
vocabulary. It does not create formal verification and validation, design verification under any
regulation, compliance, certification, or any safety, security, or regulatory guarantee.

---

## Two words that are not synonyms

- **Checked** means a second party followed the originator's path and found it executed correctly:
  the arithmetic, the transcription, the inputs matching their sources, the steps matching the plan.
  A check inherits the originator's method, and therefore its blind spots.
- **Verified** means the result was confirmed to be *right for its purpose*, either by judging the
  basis itself (design review) or by reaching the result another way (alternate method, qualification
  test). Verification can disagree with a flawless check.

Public nuclear QA language keeps this distinction explicit. 10 CFR 50 Appendix B, Criterion III,
calls for "verifying or checking the adequacy of design, such as by the performance of design
reviews, by the use of alternate or simplified calculational methods, or by the performance of a
suitable testing program," performed "by individuals or groups other than those who performed the
original design, but who may be from the same organization." Three distinct methods, and a
separation rule that is about the *originator*, not the organization.

## The ladder

Each rung names what is examined and what it can catch. Higher rungs do not replace lower ones;
they catch different failures.

| Rung | Method | What is examined | Catches | Cannot catch | Software / agent form |
|---|---|---|---|---|---|
| 0 | **Self-check** | your own action or output, by you | slips and lapses at the point of action | anything your framing hides | STAR before a risky command; re-reading your own diff |
| 1 | **Check** | the originator's work, along the originator's path | execution errors: wrong input copied, off-by-one, step skipped | a wrong method, a wrong assumption, a wrong requirement | a second party re-runs the author's tests and reads the diff against the plan |
| 2 | **Design review** (deep review) | the basis: requirements, inputs, assumptions, method choice, and whether the conclusion follows | a correct calculation of the wrong thing; unstated assumptions; a method that does not fit the purpose | defects that only appear when the thing runs | a reviewer given the basis and the candidate, *not* the author's conclusion, who must state whether the approach is right |
| 3 | **Alternate method** | the same result, reached by a different route, then compared | errors common to the original method, including ones a reviewer would also read past | errors common to *both* methods (name the common cause) | an independent oracle or second implementation; a property test beside example tests; a hand derivation against the code's output; a second primary source for a fact; a different model family for a judgment |
| 4 | **Qualification test** | the real artifact under the most adverse credible conditions | behavior the source and the review both predicted wrongly | conditions nobody thought to include | run the produced artifact on worst-case, boundary, and fault-injected inputs ([`verifying-final-artifacts`](../../skills/verifying-final-artifacts/SKILL.md), [`stress-testing-agent-changes`](../../skills/stress-testing-agent-changes/SKILL.md)) |

Appendix B states that when a test program is used *in lieu of* other verifying or checking
processes, it "shall include suitable qualifications testing of a prototype unit under the most
adverse design conditions." The software reading: a happy-path test run is not a substitute for
review or an alternate method; only a deliberately adverse test can stand in for them.

## Timing and separation of the second party

The human-performance vocabulary in DOE-HDBK-1028-2009 grades *when* and *how separately* a second
person confirms:

- **Peer-check** — a second person watches the performer *before* the action, to stop a wrong one.
- **Concurrent verification** — two people, same time and place, separately confirm a condition
  before, during, and after an action.
- **Independent verification** — one person, separated in time and distance from the performer,
  confirms the result afterward, without relying on the performer's observation or say-so. The
  handbook's test: "Independence exists when the verifier has freedom of thought from the performer."
- **Peer review** — a fresh set of eyes reads another's work product to catch errors before it is
  complete, or to confirm a decision or plan is appropriate before proceeding.

For agents, "freedom of thought" is the operative condition. A verifier that is handed the actor's
summary, preferred answer, or chosen evidence does not have it, whatever its role label. Brief the
verifier from the basis and the raw artifacts; withhold the actor's conclusion where feasible
([`evaluation-integrity.md`](evaluation-integrity.md) §2).

## Independent review means more than one means

An *independent review* in this repo is not one more reader. It is a result that has been reached
by **at least two methods that can fail differently**, at least one of them by a party other than
the originator. Two passes of the same method by two agents of one model family on one brief are
one method ([`independence-architecture.md`](independence-architecture.md) — "name the common-cause
analysis").

Worked contrast, for the claim "the retry budget caps total wait at 30 s":

- *Check:* a reviewer reads the backoff loop and confirms it matches the plan. Agrees.
- *Design review:* a reviewer asks whether 30 s is the right cap for the caller's timeout. Finds the
  caller times out at 20 s. The check could not have found this.
- *Alternate method:* a property test sums the actual sleeps over random seeds and jitter. Finds
  jitter can push the total to 34 s. Neither reader found this.

## Graded by mode

| Mode | Minimum for a load-bearing claim |
|---|---|
| Quick | self-check (rung 0), recorded |
| Standard | a check (rung 1) **and** at least one of design review or alternate method (rung 2 or 3), performed by someone other than the originator |
| Nuclear / Tier 0 | design review (rung 2) **and** an alternate method or qualification test (rung 3 or 4) that cannot share the first method's common cause; the verifier has freedom of thought from the actor; a human is in the verification path; a trust-bearing verdict goes to a [panel](../../skills/running-a-review-panel/SKILL.md) |

Where a mode's minimum is not met, the gap is recorded as residual risk in `ship.md`, not hidden
behind a `pass`.

## Recording it

- `verification.md` → **Verification type** column: name the rung (`check`, `design review`,
  `alternate method`, `qualification test`) rather than just "review."
- Custody classification ([`actor-evidence-independence.md`](actor-evidence-independence.md)):
  a second party re-running the author's path is `independent reproduction`; an alternate method or
  qualification test by a separated party is `diverse verification`; a second party watching the
  action as it happens is `direct witnessing`.
- `ng validate --two-party` fails a `pass` claim with no declared verifier distinct from the change
  actor. It compares declared identities; it cannot tell whether the rung was really climbed.
  That judgment stays with the reviewer.

## Red flags

- "Reviewed" or "verified" with no rung named.
- A design review whose brief included the author's conclusion.
- An "alternate" method that reuses the original's tests, oracle, or source.
- A test program used in place of review that contains only expected-path cases.
- The verifier relied on the actor's narration of the result instead of the artifact.

## How it connects

- [`independence-architecture.md`](independence-architecture.md) — who is separate, and on which axis.
- [`actor-evidence-independence.md`](actor-evidence-independence.md) — custody roles and the five-axis profile.
- [`evaluation-integrity.md`](evaluation-integrity.md) — judge bias and panels.
- Skills: [`proving-claims`](../../skills/proving-claims/SKILL.md) (claim → evidence),
  [`checking-facts`](../../skills/checking-facts/SKILL.md) (facts against primary sources by two means),
  [`reviewing-code-quality`](../../skills/reviewing-code-quality/SKILL.md) (rung 1–2 for code),
  [`verifying-final-artifacts`](../../skills/verifying-final-artifacts/SKILL.md) and
  [`stress-testing-agent-changes`](../../skills/stress-testing-agent-changes/SKILL.md) (rung 4),
  [`running-a-review-panel`](../../skills/running-a-review-panel/SKILL.md) (several methods on one verdict).

## Source-lineage note

Original Nuclear-grade operating doc. Concept lineage: the three design-verification methods
(design review, alternate or simplified calculation, qualification testing under the most adverse
design conditions) and the originator-separation rule from 10 CFR 50 Appendix B, Criterion III; the
peer-check, concurrent verification, independent verification ("freedom of thought from the
performer"), and peer review definitions from DOE-HDBK-1028-2009 Volume 2. Both are mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md); quotations were
checked against the eCFR text and the DOE handbook PDF on 2026-11-03. This page borrows vocabulary;
it does not claim to meet either source.
