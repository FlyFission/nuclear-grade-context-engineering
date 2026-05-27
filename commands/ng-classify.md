# ng-classify

## Purpose

Classify a proposed change into the smallest honest Nuclear-grade mode after questioning assumptions, and name the proof needed before work continues. This is a portable command prompt.

## Use when

- A new change request arrives.
- A PR scope changed.
- Reviewers are unsure whether Quick evidence is enough.
- Work is routine, procedural, novel, interrupted, resumed, delegated, or critical enough to require an HPI control.

## Do not use when

- Incident containment is active.
- The mode decision is already current and scope has not changed.

## Inputs

- User request, issue, PR, or diff.
- Affected files, dependencies, prompts, data, tools, credentials, and release artifacts.
- Questioning-attitude screen or known assumptions, if available.
- `docs/02-operating-system/activation-thresholds.md`.

## Prompt text

```text
Classify this change using Nuclear-grade.

Inputs:
- Request or diff: <paste/link>
- Affected files/assets: <list>
- User/security/dependency/data/AI/release impact: <known facts>

Return:
- selected mode: Quick, Standard, or human-reviewed stronger mode
- consequence, reversibility, exposure, detectability, uncertainty
- work mode and HPI control recommendation: none, context pack, turnover, self-check, independent verification, OPEX, or trust check
- assumptions or facts that changed the mode
- required packet files
- minimum proof required
- escalation triggers
- boundary note: do not claim formal assurance, compliance, certification, safety, security, or regulatory adequacy
```

## Files created or modified

- `.nuclear/changes/<slug>/risk.md`

## Expected outputs

- Selected mode.
- Mode rationale.
- Proof obligation.
- HPI control recommendation when activated.
- Escalation triggers.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Classifying by effort instead of consequence.
- Ignoring AI authority, dependency trust, data exposure, or release impact.
- Selecting Quick while unresolved Standard triggers remain.

## Legal/assurance boundary note

This prompt supports evidence visibility only. It does not create compliance, formal V&V, certification, safety, security, or regulatory adequacy.
