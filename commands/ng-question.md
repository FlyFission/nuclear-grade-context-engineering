# ng-question

## Purpose

Apply a questioning attitude to a change before work, review, or release continues. This is a portable command prompt.

## Use when

- A request, plan, diff, dependency, agent action, or release decision needs skeptical fact-finding.
- Assumptions, evidence gaps, or escalation triggers are unclear.
- You want the agent to "grill my change" before it builds.

## Do not use when

- Incident containment must happen immediately.
- The change is a tiny Quick edit with obvious proof and no trust boundary.
- The user needs formal assurance, certification, legal advice, or regulatory approval.

## Inputs

- Change request, issue, PR, diff, or packet path.
- Affected files, dependencies, prompts, models, tools, permissions, data, and release artifacts.
- Known assumptions, constraints, evidence, and open questions.
- Relevant source-map or prior packet links if invoked.

## Prompt text

```text
Apply a Nuclear-grade questioning attitude to this change.

Inputs:
- request/diff/packet:
- affected items:
- known assumptions:
- evidence available:
- constraints or deadlines:

Return:
- decision question in one sentence
- assumptions that must be true
- known facts, unknowns, danger words, and source-quality concerns
- facts to verify before work continues
- warning signs, agent error precursors, error-likely steps, and hidden Standard-mode triggers
- evidence needed before execute, verify, review, decide, or baseline
- pause conditions and escalation triggers
- recommended next artifact: Quick proof, Standard spec, context pack, turnover, self-check, CM record, or release decision

Prefer facts over confidence. Do not imply formal assurance, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- `.nuclear/changes/<slug>/questioning-attitude.md` when activated.
- `risk.md`, `basis.md`, `plan.md`, or `ship.md` when a compact section is enough.

## Expected outputs

- Validated and unresolved assumptions.
- Evidence gaps.
- Stop/escalation conditions.
- Next artifact recommendation.
- Danger words or source-quality concerns that change the decision.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Turning questioning attitude into generic brainstorming.
- Asking many questions without naming which facts change the decision.
- Treating agent confidence or green CI as evidence for unrelated claims.
- Hiding escalation triggers because the change seems small.

## Legal/assurance boundary note

Questioning attitude supports fact-finding and evidence visibility. It does not create formal V&V, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
