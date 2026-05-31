# ng-deficiency

## Purpose

Log a known deficiency so it is aged, owned, and either fixed or formally accepted as risk instead of quietly normalized. Turns "we all know about that" into an owned, dated, decided entry. This is a portable command prompt.

## Use when

- A known problem will outlive the current change: a flaky test, a noisy alert, an unowned service, a dead dashboard, a recurring incident, or deferred hardening.
- A review or incident surfaced something real that is not being fixed right now.
- You want to stop the slow normalization of a tolerated problem.

## Do not use when

- A lesson is already fully closed inside a packet and needs no standing tracking.
- The work is brand-new with no accepted deficiency yet.
- The item is an active incident needing response, not logging.

## Inputs

- The deficiency, where it shows up, and how it was found.
- Its consequence and how often it bites.
- Who could own it, and whether a fix or a formal risk-acceptance is right.
- Any related incident, OPEX lesson, or controlled item.

## Prompt text

```text
Log this deficiency the Nuclear-grade way.

Inputs:
- deficiency and where it shows up:
- how it was found:
- consequence and frequency:
- candidate owner:
- related incident / OPEX / controlled item:

Return:
- a one-line description with a link to where it shows up
- the date first seen, so its age is visible
- the assigned owner (an unowned deficiency is itself a finding)
- the disposition: fix by a date, or formally accept the risk with a named owner and a revisit date
- the review trigger so an accepted risk does not become permanent by default
- links to related incident, OPEX, and controlled-item records

Decide fix-or-accept; never leave it as a silent "known issue." Do not imply formal assurance.
```

## Files created or modified

- A row in `deficiency.md` from `templates/golden-path/deficiency.md`.
- Links from `opex.md`, `incident.md`, or controlled-item records.

## Expected outputs

- A deficiency entry with description, age, owner, disposition, and review trigger.
- A clear fix-or-accept decision.
- Links that keep the register navigable.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating shared awareness as ownership or a decision.
- Accepting a risk with no owner, no date, and no review trigger.
- Letting the same deficiency recur across incidents with no standing entry.
- Lowering the standard to match the deficiency instead of raising the deficiency to the standard.

## Legal/assurance boundary note

Tracking deficiencies helps you keep known problems owned and decided. It does not create formal verification and validation, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
