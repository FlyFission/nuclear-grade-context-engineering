# ng-prove

## Purpose

Map important packet claims to evidence, status, gaps, and release impact. This is a portable command prompt.

## Use when

- Tests pass but reviewers cannot see what claim they prove.
- A packet contains broad assertions that need narrowing.
- Evidence gaps need status and ship impact.

## Do not use when

- There is no material claim to prove.
- The user needs formal verification, certification, or legal assurance.

## Inputs

- `basis.md`, `trace.md`, `verification.md`, `ship.md`.
- Test commands, CI output, reviews, logs, screenshots, diffs, and known gaps.

## Prompt text

```text
Prove the important Nuclear-grade claims in this packet.

Inputs:
- packet: .nuclear/changes/<slug>/
- claims: <list or source file>
- evidence available: <commands/links/reviews/logs>
- known gaps: <list>

Return:
- claim -> basis -> control/design feature -> verification type -> evidence -> status -> ship posture
- narrowed wording for overbroad claims
- explicit gaps, deferrals, or blockers
- validator command to run
```

## Files created or modified

- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/ship.md`

## Expected outputs

- Claim-to-evidence table.
- Evidence status.
- Verification type: self-check, peer-check, concurrent verification, independent verification, peer review, test, or eval.
- Updated release posture.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating CI as proof of unrelated claims.
- Treating a self-check as independent verification.
- Hiding gaps.
- Using "safe", "secure", "approved", or "compliant" beyond the evidence.

## Legal/assurance boundary note

Claim proof is scoped engineering evidence. It is not formal V&V, safety proof, security assurance, certification, or regulatory approval.
