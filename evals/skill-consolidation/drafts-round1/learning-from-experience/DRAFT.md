---
name: learning-from-experience
description: After something went wrong or nearly did, routes it to what it needs - a lasting control fix (OPEX lesson), an owned and dated entry for a known problem you will live with for now (flaky test, noisy alert, unowned service), or an outward notice when the defect is in a shared prompt, skill, dependency, model, or template others use. Do not use during a live incident, which comes first, or to blame someone.
---

# Learning From Experience

## Overview

Lessons from real operation (OPEX) only help if they change future work. After an incident, near miss, review surprise, escaped bug, or operating signal, ask three separate questions. Which control should change so this does not repeat? Is a problem being left in place that must not quietly become normal? Does anyone else carry the same defect? Answer only the ones that apply. Each has its own record, and none substitutes for another.

No-blame applies to honest error and at-risk slips: fix the control, not the person or the model. It does not cover a willful violation, such as knowingly disabling a control, fabricating a passing result, or routing around a required gate. Surface that as a finding and fix the gate that allowed it (Charter Art. 3, 19).

## Decision contract

- **Claim checked:** each applicable path closed: a lesson with an owned, verified control fix or a reasoned waiver; a standing deficiency with age, owner, and fix-by date or formal risk acceptance plus revisit trigger; a shared defect notified to named consumers or recorded as not reportable with a reason.
- **Artifact observed:** the event and the control, item, or shared artifact it touched -> an OPEX record, a `deficiency.md` row, and/or a shared-defect notice.
- **Decision affected:** block -- whether a durable control changes, a known problem is owned or formally accepted, and downstream consumers are told.
- **Failure class:** unlearned-lesson, normalized-deviation, or silent-local-fix.
- **Next action:** assign owners and recheck triggers; a repeated weak control or a security-relevant shared defect escalates.

## When to Use

- A bad handoff, wrong-file edit, made-up claim, agent overreach, escaped bug, review surprise, or misread release happened.
- A known problem will outlive this change: a flaky test, noisy alert, dead dashboard, unowned service, deferred hardening.
- A defect you found lives in something others consume: a shared prompt, skill, template, dependency pin, model, eval, or config.

## When Not to Use

- A live incident still needs containment (use `responding-to-incidents` first).
- The defect is local to your change, has no lesson that would repeat, and nothing is being left in place; that is an ordinary fix.
- The request is to assign blame rather than improve a control.

## Inputs

- The event or signal, its evidence, impact, and any quick fix already made.
- The control, record, or artifact it touched, and who else consumes that artifact.
- Who could own each follow-up.

## Process

1. Contain first if anything is live. Then state the actual condition and the standard it fell short of, in plain words and without blame. Separate honest error from willful violation.
2. Triage. Take every path that applies, and only those.

**Lesson (a control should change):**

3. Name the root cause and the weak or missing control, and which approved version or file it touched.
4. Pick a lasting fix: a basis, test, checker, template, skill, command, doc, monitor, threshold, or approved version. Regret or explanation is not a fix when a control could change.
5. Give the fix an owner and verify it, or close the lesson on purpose with the reason no fix is warranted.

**Standing deficiency (a problem stays for now):**

6. Record it in one line with where it shows up, when it was first seen, and an owner. An unowned deficiency is itself a finding.
7. Choose fix-by-date or formal risk acceptance with a named owner and a revisit trigger, so acceptance never becomes permanent by default.

**Shared defect (others carry it):**

8. Confirm it lives in a shared or supplied artifact, and evaluate who consumes it and how it could fail for them.
9. Fix your copy and, separately, notify the affected consumers or owners with severity and the fix or workaround. Give the notice an owner and a tracking link, or record why it is not reportable.

Then link the records to each other and feed the lesson into future questioning, planning, and handoffs.

## Outputs

- An OPEX record with finding, fix, owner, and evidence or close-out reason.
- A `deficiency.md` row: description, age, owner, disposition, revisit trigger.
- A shared-defect notice: consumers, severity, when sent, owner, tracking link; or a not-reportable reason.

## Verification

- Every finding has an action, an owner, and evidence or a reason; the lesson changes a controlled item or says why not.
- No deficiency sits as "known, untracked"; accepted risks carry an owner and a revisit trigger.
- Every reportable shared defect names its consumers; a local patch alone does not close it.

## Escalation

- Escalate when the event touched users, data, security, credentials, releases, public claims, or repeated agent power.
- Require a second, independent reviewer when the same weak control shows up more than once, or a shared defect reaches external consumers.
- Stop normalizing when one deficiency drives repeat incidents; raise it as a finding. Report upward when no one will own a fix, an acceptance, or a notice.

## Common Rationalizations

- "The agent just made a mistake." Ask what prompt, context, checker, or power limit let it happen.
- "We fixed the bug." A fix with no lesson can return by another path, and your fix does not reach other consumers.
- "Everyone knows about it." Shared awareness is not ownership or a decision.
- "No-blame means no accountability." It covers honest error, not a knowingly bypassed gate.

## Red Flags

- An OPEX record with no lasting fix and no reason it was closed, or a lesson stuck in chat.
- A known problem living in memory, or an accepted risk with no owner, date, or trigger.
- A shared-artifact defect fixed in one place with no notice to other consumers.
- A willful bypass filed as "just a mistake."

## Prompt

```text
Run a Nuclear-grade after-the-fact review.

Inputs:
- event, near miss, or signal, with evidence and impact:
- immediate correction already made:
- control, record, or artifact it touched, and who else consumes that artifact:
- is a problem being left in place for now? (yes/no)
- owner candidates:

Triage, and take only the paths that apply:
- Lesson: root cause, weak control, lasting fix, owner, verification or reasoned close-out.
- Standing deficiency: one-line entry, first seen, owner, fix-by date or formal risk acceptance with revisit trigger.
- Shared defect: consumers, severity, notice sent with owner and tracking link, or a not-reportable reason.

No-blame covers honest error, not a willful violation; surface those as findings. Do not imply formal assurance.
```

## Source-lineage note

An original software-workflow translation of operating experience, post-job review, error and near-miss reporting, corrective action, and no-blame learning from DOE-HDBK-1028-2009; of not living with deficiencies and the normalization-of-deviation literature, as concept lineage; and of the evaluate-and-notify duty for defects in supplied items, informed by 10 CFR Part 21 (§21.21). All are mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE, NRC, or any compliance, formal assurance, safety, security, certification, or regulatory adequacy.
