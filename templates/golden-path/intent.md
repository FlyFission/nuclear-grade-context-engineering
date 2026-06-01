# Intent Declaration / Release Brief

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** State what you intend to do and why before a critical or irreversible action, so a reviewer can challenge the thinking before the action — not the wreckage after.

**Activation threshold:** Use before deploys, migrations, data changes, public claims, dependency/model swaps, releases, or any action whose blast radius is more than the immediate file.

**Minimum useful version:** the intent, the reasoning, the expected result, the falsifying signal, the abort criteria, the verified rollback, the decision rights, and the backup.

---

## Change context

- Slug:
- Owner:
- Date:
- Current golden-path phase:
- Related packet:

## Intent

- I intend to:
- On target:
- Because (reasoning / evidence preconditions are met):
- Evidence link for the preconditions:

## Expected result and falsifying signals

- Expected result:
- Signals that would mean it went wrong:
- Blast radius (who/what is affected):

## Abort and rollback

- Abort criteria (numbers where possible):
- Rollback step:
- Rollback verified? (how):

## Decision rights and backup

- Who decides / who may stop this, by when:
- Escalation trigger:
- Backup watcher:

## After action

- Actual result:
- Compared to expected (match / gap):
- Follow-up, incident, or deficiency raised:

## Required links

- Packet:
- Verification evidence:
- Decision record if public, release, or trust posture changed:

## Exit criteria

- The intent named what would prove it wrong, not only what success looks like.
- Abort criteria and a verified rollback were stated before acting.
- The actual result was compared to the expected result and any gap was recorded.

## Source-lineage note

Original Nuclear-grade template. The "I intend to" construct is concept inspiration from intent-based leadership only — paraphrased, not template lineage (a copyrighted source; see `docs/00-standards-foundation/do-not-cite-directly.md`). Its public source lineage is the deliberate-action, self-checking, and three-way-communication habits in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
