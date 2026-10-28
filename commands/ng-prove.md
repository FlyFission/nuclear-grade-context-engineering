---
description: "Builds claim-to-evidence trace rows with statuses, gaps, tests, evals, reviews, and narrower non-claims."
disable-model-invocation: true
---

# ng-prove

Portable command prompt generated from `skills/proving-claims/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- A change record makes claims about the code, says something about safety or security, claims release readiness, or claims a dependency can be trusted.
- Tests pass, but reviewers cannot see which claim each test backs up.
- Evidence gaps have to be accepted, put off, or treated as blockers.
- The proof needs the right kind of check. The kinds are self-check, peer-check, concurrent verification (a second person checks as you go), independent verification (a separate person checks afterward), peer review, a test, or an eval.

## Do not use when

- The request is to make the final ship/defer/block decision; use `checking-release-readiness` after the trace is built.
- The request is to judge public legal, safety, security, certification, or compliance wording; use `checking-legal-and-safety-wording`.
- The request is to validate citation lineage or source authority; use `checking-source-claims`.

## Inputs

- `basis.md`, `trace.md`, `verification.md`, and `ship.md`.
- Test commands, CI runs, reviews, logs, diffs, screenshots, and source links.
- Known gaps and leftover risks.

## Prompt text

```text
Prove the important Nuclear-grade claims in this packet.

Inputs:
- packet: .nuclear/changes/<slug>/
- claims: <list or source file>
- evidence available: <commands/links/reviews/logs>
- known gaps: <list>

Return:
- claim -> basis -> control/design feature -> support type -> verification type -> evidence -> status -> ship posture
- for each load-bearing claim: evidence custody (generated, selected, transformed/summarized, executed/captured, retained, presented)
- the five-axis actor–evidence coupling profile (actor, context, mechanism, authority, resource), the consequence-specific minimum, and any residual coupling or blocker
- narrower wording for any claim that is too broad
- the gaps, deferrals, or blockers, stated plainly
- the validator command to run
```

## Verification

- `python tools/ng.py validate .nuclear/changes/<slug>` passes for Quick or Standard records.
- Every important claim has evidence, a stated gap, or a deliberate deferral.
- No test result is used to imply unrelated safety, security, compliance, or approval.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/proving-claims/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
