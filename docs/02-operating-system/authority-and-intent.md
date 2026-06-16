# Authority and Intent

**Purpose:** Put decision authority where the information is — bounded — and make intent explicit before critical action. This is the operating mechanics for Charter Articles 17 (authority to information) and 18 (intent before action).

**Boundary:** Original software-workflow translation. It does not create formal assurance, compliance, certification, safety, or regulatory adequacy.

---

## The decision-rights matrix

Place each decision by reversibility, evidence, and consequence. The gradient pushes work to the edge while it is cheap to undo, and slows down at the gates.

| Reversible? | Evidence | Consequence | Who decides |
|---|---|---|---|
| Yes | Proven | Low | Agent at the edge; record only |
| Yes | Partial | Meaningful | Agent proposes via intent declaration; human in the review window |
| No | Proven | Meaningful | Human gate; agent prepares the brief |
| No | Partial / asserted | Any | Escalate; do not proceed on confidence |
| Any | Any | Protected / irreversible | Named human gate, independent check |

Rules that never bend: authority is earned by demonstrated competence (evals, tests, track record) and shared clarity of intent; the gradient never removes a required human gate; an agent's confidence is not competence, and its stated intent is not proof it understood. Use the `deciding-who-decides` skill and `ng-decide-authority` to place a specific action.

## The intent ladder, for agents

The language an actor uses signals how much ownership it is taking. The pivot is "I intend to…": below it, work happens only if approved; at it, work happens unless stopped.

```text
tell me what to do  ->  I see  ->  I think  ->  I would like to  ->  I intend to  ->  I have done  ->  I have been doing
```

For an agent, "I intend to…" means: state the action, the reasoning, the expected result, the falsifying signal, the abort criteria, the verified rollback, and the backup — then act after the review window. The supervisor's job shifts from approving every move to verifying clarity and competence. Use `declaring-intent`, `ng-intent`, and `templates/golden-path/intent.md`.

The six questions a supervisor asks before granting control: What are you trying to achieve? What do you expect to happen? What could go wrong? How will you know? How will you recover? Who else needs to know? Strong answers earn control; weak answers mean train (raise competence and clarity) before delegating.

## Qualification: what "train before delegating" means

The matrix grants authority to demonstrated competence, and the six questions end in "train before delegating" — so competence has to be something you can point at, not a feeling. Qualification is the evidence that an actor (human or agent) may take on an action class. It is badges, not certificates: the lightest record that answers three columns.

| For an action class | Required demonstrated competence | Revalidation trigger |
|---|---|---|
| Release service X, run a migration, edit auth, approve agent tool grants | evals passed, tests green, the guardrails that bound it, track record on reversible runs | model/prompt swap, a new failure mode, an incident, a scope change, or an elapsed interval |

Two rules keep this honest:

- **Competence is evidence, not confidence.** For an agent, competence is eval coverage and track record, not fluent-sounding certainty (Charter Art. 17). An agent's "I can do this" does not qualify it.
- **Qualification is scoped and expires.** Being qualified for a reversible action class is not qualification for an irreversible one, and a stale qualification is re-earned, not assumed. A qualification with no revalidation trigger is itself a finding.

This evidences competence-to-act for a change; it is not an HR program or a certification scheme (see `../01-field-guide/leadership-and-high-reliability.md`).

## The intent-based release brief

Treat a high-risk release like a watch evolution, not a Slack message:

> I intend to release build X to 5% of production. Expected change: the new pricing-cache path. Preconditions: integration tests passed, cache warmed, dashboard open, rollback verified. Abort if checkout error rate > 0.4%, or p99 > 800 ms for 5 minutes. Backup: a second watcher owns the database signal.

That is formality, not bureaucracy: every claim is checkable, the abort criteria are numbers, and the rollback is verified before the cut.

## Stop-work authority

Anyone may halt unsafe or unclear work regardless of seniority, and surfacing bad news is protected, never punished (Charter Art. 19). A junior reviewer — or a critic agent — must be able to block a release when risk is unclear. This is forceful backup: the person doing the work is not the only one grading it, and independent backup uses a different model or context so it does not inherit the same blind spots. The same independence rule governs every layer of defense, not just review — tests, evals, monitors, and policies only add up when they fail independently (the control stack in `configuration-management.md`). See `double-checking-before-acting` and `critical-systems.md`.

## Source-lineage note

Original Nuclear-grade operating doc influenced by intent-based leadership (authority to information, the intent ladder, leader-leader), naval mission-command and forceful-backup practice, and the deliberate-action, self-checking, and conservative-decision habits in DOE-HDBK-1028-2009, used as concept lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
