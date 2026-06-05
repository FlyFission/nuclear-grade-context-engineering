# ng-question

## Purpose

Question a change before you build it, review it, or release it. Name the one decision the work has to settle, and settle that first. This is a portable command prompt.

## Use when

- A request, plan, code change (the diff), dependency, agent action, or release call needs a hard, fact-based second look.
- The assumptions, the gaps in the evidence, or the reasons to stop and ask for help are unclear.
- You want the agent to grill your change before it builds.

## Do not use when

- An incident is live and you must contain it right now.
- The change is a tiny, low-stakes edit. The proof is obvious and it adds no new trust boundary.
- The user wants a formal guarantee, a certification, or legal advice. This prompt does not give regulatory approval.

## Inputs

- The change request, issue, pull request (PR), code change, or path to the change record.
- The files, dependencies, prompts, models, tools, permissions, data, and release items the change touches.
- What you already assume, the limits you face, the evidence you have, and the questions still open.
- Links to the source map or earlier change records, if they apply.

## Prompt text

```text
Question this change the Nuclear-grade way.

Inputs:
- request/diff/change record:
- affected items:
- known assumptions:
- evidence available:
- limits or deadlines:

Return:
- the decision question in one sentence
- the work type(s), all that apply (a production defect is brownfield and defect-fix), and the questions each forces
- the evidence that would change the decision
- the assumptions that must be true
- known facts, unknowns, danger words, and worries about how good the sources are
- facts to check before work continues
- warning signs, signs an agent is about to slip, steps where mistakes are likely, and hidden reasons to treat this as a Standard change
- evidence needed before you execute, verify, review, decide, or save the approved version (the baseline)
- conditions that should make you pause or ask for help
- the next thing to produce: Quick proof, Standard spec, context pack, handoff, self-check, a record of what stays under control (the controlled items), or a release decision

Trust facts over confidence. Do not imply formal verification and validation, compliance, certification, safety, security, or regulatory adequacy.
```

## Files created or modified

- `.nuclear/changes/<slug>/questioning-attitude.md` when you use this prompt.
- `risk.md`, `basis.md`, `plan.md`, or `ship.md` when a short section is enough.

## Expected outputs

- Which assumptions are now checked and which are still open.
- The evidence that would change the decision.
- The gaps in the evidence.
- The conditions that should make you stop or ask for help.
- A recommendation for what to produce next.
- Any danger words or source-quality worries that change the decision.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Turning the questions into open-ended brainstorming.
- Asking questions that change no decision.
- Asking many questions but never naming which facts change the decision.
- Treating an agent's confidence, or a green test run (CI), as evidence for some other claim.
- Hiding the reasons to stop and ask for help because the change seems small.

## Legal/assurance boundary note

Questioning a change helps you find facts and see the evidence. It does not create formal verification and validation, compliance, certification, safety, security, procurement adequacy, or regulatory approval.
