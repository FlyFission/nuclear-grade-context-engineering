# Variance Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Record a known gap from the accepted baseline (the version everyone agreed is correct) before it turns into uncontrolled drift.

**Activation threshold:** Use when the real state differs from the baseline, but the team is not making a new baseline right away.

**Minimum useful version:** the gap, the affected item, the impact, the owner, an end date or recheck trigger, and the disposition. For a deliberate temporary modification (feature flag, bypass, loosened permission, disabled check), also record a named back-out and keep it visible to whoever operates the system.

**Overhead trap:** Do not use variance records to make a stale baseline look normal. If the gap is here to stay, make a new baseline.

---

## Variance

| Affected item | Baseline state | Actual state | Impact | Disposition | Owner | Recheck trigger | Back-out / removal |
|---|---|---|---|---|---|---|---|
| | | | | accept / mitigate / defer / block | | | |

## Required links

- Baseline record:
- Related packet or issue:
- Verification or monitoring evidence:

## Exit criteria

- The gap is visible and owned.
- The trigger for the next review or new baseline is named.

## Source-lineage note

Original Nuclear-grade variance template inspired by public sources on configuration management and lessons from real operation, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
