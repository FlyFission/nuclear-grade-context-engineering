# ng-prove

## Purpose

Tie each important claim in the change record (the packet) to its evidence, its status, its gaps, and what it means for the release. This is a portable command prompt.

## Use when

- Tests pass, but reviewers cannot see which claim they prove.
- A packet makes broad claims that need to be narrowed.
- Gaps in the evidence need a status and a read on how they affect the release.

## Do not use when

- There is no real claim to prove.
- The user needs formal verification, certification, or legal assurance.

## Inputs

- `basis.md`, `trace.md`, `verification.md`, `ship.md`.
- Test commands, test-run output (CI), reviews, logs, screenshots, diffs, and the gaps you know about.

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
- narrower wording for any claim that is too broad
- the gaps, deferrals, or blockers, stated plainly
- the validator command to run
```

## Files created or modified

- `.nuclear/changes/<slug>/trace.md`
- `.nuclear/changes/<slug>/verification.md`
- `.nuclear/changes/<slug>/ship.md`

## Expected outputs

- A table linking each claim to its evidence.
- For each important claim, whether it is a fact, an assumption, an unknown, a source's claim, or local proof.
- The status of the evidence.
- The kind of verification (V&V): self-check, peer-check, concurrent verification, independent verification, peer review, test, or eval.
- An updated read on whether it is ready to ship.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating a green test run (CI) as proof of an unrelated claim.
- Treating confidence, a source's claim, or vendor wording as local proof.
- Treating a self-check as independent verification.
- Hiding the gaps.
- Using "safe", "secure", "approved", or "compliant" beyond what the evidence shows.

## Legal/assurance boundary note

Proving a claim gives you scoped engineering evidence. It is not formal V&V, a safety proof, security assurance, certification, or regulatory approval.
