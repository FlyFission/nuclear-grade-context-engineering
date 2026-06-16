---
name: proving-claims
description: Maps claims to evidence, statuses, gaps, tests, evals, reviews, and traces, and narrows anything unsupported into an explicit non-claim. Use when a packet asserts something a reviewer must trust. Do not use to invent evidence that does not exist, or to treat green CI as proof of unrelated claims.
---

# Proving Claims

## Overview

Evidence should answer named claims. It should not just create a vague sense that the change is fine. This skill turns each claim into a proof you can trace. It keeps six things apart: a fact, an assumption, an unknown, a source claim (something a source says), local proof (something you checked yourself), and decision authority (who gets to decide).

## Decision contract

- **Claim checked:** every material claim is tied to evidence, a stated gap, or a deliberate deferral, and no claim reaches past its evidence.
- **Artifact observed:** `basis.md`, test, and review evidence -> claim-to-evidence rows with a status (`pass`/`fail`/`gap`/`deferred`/`not applicable`/`planned`) in `trace.md`/`verification.md`.
- **Decision affected:** warn -- the release posture the `ship.md` decision weighs.
- **Failure class:** overreaching-claim (a claim stated past its evidence, or a `fail`/unowned `gap` carried as shippable).
- **Next action:** record the gap as residual risk for `ship.md`; a `fail` or unowned `gap` escalates to block.

## When to Use

- A change record makes claims about the code, says something about safety or security, claims release readiness, or claims a dependency can be trusted.
- Tests pass, but reviewers cannot see which claim each test backs up.
- Evidence gaps have to be accepted, put off, or treated as blockers.
- The proof needs the right kind of check. The kinds are self-check, peer-check, concurrent verification (a second person checks as you go), independent verification (a separate person checks afterward), peer review, a test, or an eval.

## When Not to Use

- The claim is purely about wording and carries no engineering or trust weight.
- The request is for formal verification and validation or certification. This skill does not provide those.

## Inputs

- `basis.md`, `trace.md`, `verification.md`, and `ship.md`.
- Test commands, CI runs, reviews, logs, diffs, screenshots, and source links.
- Known gaps and leftover risks.

## Process

1. Pull out each important claim.
2. Pick the kind of check each claim needs.
3. Sort the support behind each claim into one of these: fact, assumption, unknown, source claim, local proof, or decision authority.
4. Link each claim to its basis, the control or design feature, the code, the evidence, and the release posture.
5. Give each claim an evidence status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
6. Trim any claim that reaches too far, until the evidence truly backs it.
7. Record the gaps and how they affect the release.

## Outputs

- Claim-to-evidence rows in `trace.md` or `verification.md`.
- A clear split between fact, source, and proof for each important claim.
- Evidence commands anyone can rerun, or links to the artifacts.
- The kind of check used for each important claim.
- An updated release posture when the evidence changes.

## Verification

- `python tools/ng.py validate .nuclear/changes/<slug>` passes for Quick or Standard records.
- Every important claim has evidence, a stated gap, or a deliberate deferral.
- No test result is used to imply unrelated safety, security, compliance, or approval.

## Escalation

- Stop when the evidence is missing but the record still wants to ship.
- Escalate when claims affect public trust, regulated use, procurement, security, or safety.

## Common Rationalizations

- "CI passed, so all claims pass." CI only proves what it checks.
- "A reviewer can read the code." Review counts as evidence only when its scope and result are written down.
- "The same agent checked itself." That can be a self-check, but it is not an independent check.
- "We should not mention gaps." Hidden gaps lead to worse release decisions.

## Red Flags

- The evidence status is missing.
- A claim says "safe", "secure", "compliant", or "approved" with no scope around it.
- The release decision ignores failed or deferred evidence.

## Prompt

```text
Prove the important Nuclear-grade claims in this packet.

Inputs:
- packet: .nuclear/changes/<slug>/
- claims: <list or source file>
- evidence available: <commands/links/reviews/logs>
- known gaps: <list>

Return:
- claim -> basis -> control/design feature -> support type -> verification type -> evidence -> status -> ship posture
- narrower wording for any claim that is too broad
- the gaps, deferrals, or blockers, stated plainly
- the validator command to run
```

## Source-lineage note

This skill is an original claim-evidence workflow influenced by public software assurance, verification discipline, and secure development sources mapped in `docs/00-standards-foundation/source-map.md`. It is not formal verification.
