---
name: managing-change-records
description: Creates, updates, and closes Quick or Standard change records - adds the required files, keeps what each claim must prove current, and brings an abandoned or half-filled record (ng status shows scaffold or invalid) to an honest end state by completing, closing with a reason, or deleting it. Use when starting, revising, or cleaning up a change record. Do not use for a throwaway script, or to silence the validator on work you mean to ship.
---

# Managing Change Records

## Overview

A change record keeps the whole story in Git, together: the scope, what the change must do, the plan, the trace from claim to evidence, the proof, and the release decision. Use the smallest record that still lets a doubting reviewer decide. Every record also has to end honestly. A record that was started and abandoned looks like work in progress, hides an unproven claim, and misleads the next reader. Completed and validating, or closed with a written reason, are both good outcomes. Half-done and silent is not.

## Decision contract

- **Claim checked:** a live record carries every file its mode requires, with required links, exit criteria, source-lineage notes, plain status labels, and resolving links; a stale record reached one terminal state (completed, closed with reason and decider, or deleted as an empty scaffold).
- **Artifact observed:** the mode and `templates/quick/` or `templates/standard/` -> the record plus `ng validate` result; for cleanup, `ng status .` -> a `NUCLEAR-GRADE-CLOSED:` line or an `ok` status.
- **Decision affected:** block -- whether the record is structurally complete, and whether `ng status` reports every record `ok` or `closed`.
- **Failure class:** incomplete-record, or silent-stale-packet (including a pass faked by deleting the placeholder marker).
- **Next action:** add the missing file or link and re-validate; complete, close, or delete a stale record; ask the owner before deleting anything not confirmed dead.

## When to Use

- Starting a real AI-assisted change, or updating a record after scope, proof, risk, or release posture changed.
- Preparing a pull request that needs evidence beyond usual review notes.
- `ng status` flags a `scaffold` or `invalid` record, a session left a draft behind, or the underlying change was dropped or superseded.

## When Not to Use

- Work that leaves no lasting artifact and needs no review, or a request only to explain docs.
- Picking the mode only (use `rating-change-risk`).
- A record being actively worked right now is in progress, not stale.

## Inputs

- The mode from `risk.md` or `rating-change-risk`, the affected files, and the proof commands.
- An existing record, if any; for cleanup, `python tools/ng.py status .` output and the originating issue, PR, or anchor.

## Process

**Create or update:**

1. Run `python tools/ng.py new <slug> --mode quick|standard`.
2. Name the required files in your reply. Quick: `risk.md`, `proof.md`. Standard: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
3. Fill only the parts that help someone decide. Add habit records (self-check, turnover, OPEX, supplier trust) only when they change a decision.
4. Link affected files, tests, reviews, source-map rows, and known gaps. Keep statuses plain: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.
5. Run `python tools/ng.py validate .nuclear/changes/<slug>`.

**Close out a stale record:**

6. Find who owns it and whether the change is still wanted, from its issue, PR, or anchor.
7. Pick one end state. **Complete:** fill it and make `validate` pass; the marker goes because the record is filled. **Close:** add `NUCLEAR-GRADE-CLOSED: <why dropped, what replaced it, who decided>` on one line and keep the record. **Delete:** only a genuinely empty scaffold with nothing to learn. Prefer close over delete.
8. Re-run `ng status .` until every record is `ok` or `closed`. Add an OPEX note when abandonment keeps recurring.

## Outputs

- Quick (`risk.md`, `proof.md`) or Standard (six files) record, habit records when warranted, and the validator result.
- For cleanup: each stale record completed, closed with a rationale line, or deleted, and a clean `ng status .`.

## Verification

- Required files, links, exit criteria, and source-lineage notes are present; the evidence file states statuses; links resolve.
- Every closed record names why and who decided; no completed record passes only because its marker was deleted.

## Escalation

- Move Quick to Standard when Quick proof cannot answer the reviewer; move to human review when a stronger mode applies.
- Ask the owner before deleting any record whose change is not confirmed dead; deletion is the one irreversible option.
- Stop when a dropped record's change may have shipped without proof; closing the record does not close the risk.

## Common Rationalizations

- "We will fill it in after the pull request." Evidence should shape the work, not dress it up afterward.
- "Deleting the marker makes it pass." That fakes the gate; fill it or close it with a reason.
- "Closing it means I failed." A recorded decision to drop a change is a success; silent abandonment is the failure.

## Red Flags

- A missing proof command or evidence link, or claims that reach past the evidence.
- Record files that repeat each other instead of linking.
- `scaffold` or `invalid` records no one can explain, or ones deleted to tidy the listing.

## Prompt

```text
Create, update, or close out a Nuclear-grade change record.

Inputs:
- slug and mode (quick|standard):
- task: create / update / close out a stale record
- scope, affected files, and what the change must prove (create/update):
- ng status line and originating issue/PR, and is the change still wanted? (close out):

Create/update: use the repo templates, name the required files for the mode, keep the record short and linked to evidence, and run validate.
Close out: choose exactly one of complete, close with a NUCLEAR-GRADE-CLOSED: rationale line, or delete an empty scaffold; never fake a pass by deleting the marker.

Return the files (or the chosen end state and closure line) and the validate or status result. Do not imply formal assurance or compliance.
```

## Source-lineage note

An original Git-native change-record workflow drawing on public configuration, lifecycle, assurance, and release-readiness sources and on the work-control and self-checking practices in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. It does not create a certified quality assurance program.
