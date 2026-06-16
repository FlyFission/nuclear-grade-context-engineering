---
name: tracking-deficiencies
description: Keeps a standing register of known deficiencies so flaky tests, noisy alerts, unowned services, and recurring incidents get aged, owned, and fixed or formally risk-accepted instead of quietly normalized. Use when a known problem will outlive a single change. Do not use for a one-off lesson already closed inside a packet, or for brand-new work with no accepted deficiency yet.
---

# Tracking Deficiencies

## Overview

A deficiency you have decided to live with quietly becomes the new standard. This skill keeps a standing register of known problems so each one is aged, owned, and either fixed or formally accepted as risk with a named owner and a revisit date. The aim is to stop the slow normalization of deviation — the small erosions that, uncorrected, become the culture.

## Decision contract

- **Claim checked:** every tracked deficiency has a visible first-seen age, a named owner, and a disposition -- a fix-by date or a formal risk-acceptance with a named owner and a concrete revisit trigger -- never "known, untracked."
- **Artifact observed:** the deficiency, where it shows up, its consequence and frequency, and any related incident/OPEX/controlled item -> a deficiency entry or `deficiency.md` row (description, age, owner, disposition, review trigger) linked to those records.
- **Decision affected:** block -- per deficiency, fix by a date or formally risk-accept it with a named owner and a revisit date.
- **Failure class:** normalized-deviation (a known problem living in chat/memory, or an accepted risk with no owner, date, or trigger).
- **Next action:** assign an owner and a fix-or-accept disposition; escalate when it touches safety, security, data integrity, or drives repeat incidents.

## When to Use

- A known problem will outlive the current change: a flaky test, a noisy alert, an unowned service, a dead dashboard, a recurring incident, or deferred hardening.
- A review or incident surfaced something real that is not being fixed right now.
- You want to convert "we all know about that" into an owned, dated, decided entry.

## When Not to Use

- A lesson is already fully closed inside a packet and needs no standing tracking.
- The work is brand-new and has no accepted deficiency yet (rate it as a normal change instead).
- The item is an active incident needing response, not logging (use `responding-to-incidents`).

## Inputs

- The deficiency, where it shows up, and how it was found.
- Its consequence and how often it bites.
- Who could own it, and whether a fix or a formal risk-acceptance is the right disposition.
- Any related incident, OPEX lesson, or controlled item.

## Process

1. Describe the deficiency in one concrete line and link where it shows up.
2. Record when it was first seen so its age is visible.
3. Assign an owner; an unowned deficiency is itself a finding.
4. Choose a disposition: fix by a date, or formally accept the risk with a named owner and a revisit date.
5. Set a review trigger so accepted risks do not become permanent by default.
6. Link related incidents, lessons, and controlled items so the register is navigable.

## Outputs

- A deficiency entry, or a `deficiency.md` register row, with description, age, owner, disposition, and review trigger.
- A clear fix-or-accept decision, never a silent normalization.
- Links to related incident, OPEX, and controlled-item records.

## Verification

- Every entry has an owner and a disposition; none sit as "known, untracked."
- Accepted risks carry a named owner and a concrete revisit trigger.
- The age of each deficiency is visible, so old accepted risks resurface for review.

## Escalation

- Escalate when a deficiency touches safety, security, data integrity, or a protected outcome.
- Stop normalizing when the same deficiency drives repeat incidents; raise it as a finding.
- Get a decision owner when no one will accept the risk and no one will fund the fix.

## Common Rationalizations

- "Everyone knows about it." Shared awareness is not ownership or a decision.
- "It's been like that for ages." Age is the argument for action, not for acceptance.
- "We'll fix it eventually." "Eventually" with no owner or date is silent normalization.
- "It's just a flaky test." Tolerated noise trains people to ignore real signals.

## Red Flags

- Known problems live in chat and memory, not in a register.
- Accepted risks have no owner, no date, and no review trigger.
- The same deficiency appears in incident after incident with no standing entry.
- Standards quietly lower to match the deficiency instead of the deficiency rising to meet the standard.

## Prompt

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

## Source-lineage note

This skill is an original software-workflow translation of not-living-with-deficiencies and rising-standards culture (concept lineage from naval-reactor practice and the normalization-of-deviation literature), grounded in the operating-experience and corrective-action habits in DOE-HDBK-1028-2009, used as public idea lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
