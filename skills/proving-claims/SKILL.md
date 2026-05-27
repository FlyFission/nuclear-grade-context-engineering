---
name: proving-claims
description: Use when mapping claims to evidence, statuses, gaps, tests, evals, reviews, traces, release posture, or narrowed non-claims.
---

# Proving Claims

## Overview

Evidence should answer named claims, not create a general feeling that the change is fine. This skill turns claims into traceable proof status.

## When to Use

- A packet has implementation claims, safety/security wording, release readiness, or dependency trust assertions.
- Tests pass but reviewers cannot see which claim each test supports.
- Evidence gaps need to be accepted, deferred, or treated as blockers.
- The proof needs the right verification type: self-check, peer-check, concurrent verification, independent verification, peer review, test, or eval.

## When Not to Use

- The claim is purely editorial and has no engineering or trust consequence.
- The requested output is formal verification or certification.

## Inputs

- `basis.md`, `trace.md`, `verification.md`, and `ship.md`.
- Test commands, CI runs, reviews, logs, diffs, screenshots, and source links.
- Known gaps and residual risks.

## Process

1. Extract each important claim.
2. Select the verification type needed for each claim.
3. Link each claim to basis, control/design feature, implementation, evidence, and ship posture.
4. Assign evidence status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
5. Narrow overbroad claims until the evidence genuinely supports them.
6. Record gaps and release impact.

## Outputs

- Claim-to-evidence rows in `trace.md` or `verification.md`.
- Reproducible evidence commands or artifact links.
- Verification type for each important claim.
- Updated ship posture when evidence changes.

## Verification

- `python tools/ng.py validate <packet>` passes for Quick or Standard packets.
- Every important claim has evidence, explicit gap, or deliberate deferral.
- No test result is used to imply unrelated safety, security, compliance, or approval.

## Escalation

- Stop when evidence is absent but the packet wants to ship.
- Escalate when claims affect public trust, regulated use, procurement, security, or safety.

## Common Rationalizations

- "CI passed, so all claims pass." CI only proves what it checks.
- "A reviewer can inspect the code." Review is evidence only when scope and result are recorded.
- "The same agent checked itself." That may be a self-check, but not independent verification.
- "We should not mention gaps." Hidden gaps create worse release decisions.

## Red Flags

- Evidence status is missing.
- A claim says "safe", "secure", "compliant", or "approved" without qualified scope.
- Release decision ignores failed or deferred evidence.

## Source-lineage note

This skill is an original claim-evidence workflow influenced by public software assurance, verification discipline, and secure development sources mapped in `docs/00-standards-foundation/source-map.md`. It is not formal verification.
