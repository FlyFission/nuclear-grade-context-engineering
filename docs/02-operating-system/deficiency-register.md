# Deficiency Register

**Purpose:** Keep known problems aged, owned, and either fixed or formally risk-accepted, so deviations are not quietly normalized into the new standard. This is the operating mechanics behind the `tracking-deficiencies` skill, `ng-deficiency`, and `templates/golden-path/deficiency.md`. It implements the standing half of Charter Art. 19 and supports Art. 3 (rising standards).

**Boundary:** Original software-workflow translation. It does not create formal assurance, compliance, certification, safety, or regulatory adequacy.

---

## Why a standing register, separate from OPEX

The learning loop (`learning-from-experience`, OPEX) is event-driven: a near miss or incident produces a lesson and a durable control update. But some problems are not closed by a single change — a flaky test, a noisy alert, an unowned service, a dead dashboard, a recurring incident, deferred hardening. Left in chat and memory, they become "the way things are." The register is the standing list that keeps each one owned and decided.

## What every entry carries

- a one-line description with a link to where it shows up;
- the date first seen, so its **age** is visible;
- an **owner** — an unowned deficiency is itself a finding;
- a **disposition** — fix by a date, or formally accept the risk with a named owner and a revisit date;
- a **review trigger**, so an accepted risk does not become permanent by default.

## How it connects

- An incident's corrective actions that will outlive the incident become register entries (`incident-response.md`).
- An OPEX lesson that cannot be closed now is parked here with an owner, not dropped.
- A deficiency touching safety, security, data integrity, or a protected outcome escalates rather than waiting.
- The same deficiency recurring across incidents is a finding about standards slipping, not a rounding error.

## The discipline

Not living with deficiencies is the countervailing force to normalization of deviation: raise the deficiency to meet the standard, do not lower the standard to match the deficiency. Tolerated noise — a chronically flaky test, an alert everyone mutes — trains people and agents to ignore real signals, which is how the next real failure goes unnoticed.

## Source-lineage note

Original Nuclear-grade operating doc influenced by not-living-with-deficiencies and rising-standards culture (naval-reactor practice and the public normalization-of-deviation literature) and the operating-experience and corrective-action habits in DOE-HDBK-1028-2009, used as concept lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
