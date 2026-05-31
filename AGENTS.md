# Agent Guidance

AI agents working in this repo should treat Nuclear-grade as a way to gather evidence, not a brand to show off.
The idea is simple. Keep a questioning attitude. Use small habits from Human Performance Improvement (HPI). And keep the approved version under control for AI-assisted software work. In practice that means: question assumptions, write down what the change must do, brief the work, double-check risky actions, and hand off cleanly. Keep the controlled files, the evidence, the decisions, the version everyone agreed is correct, and the release stance all linked together.

## Default behavior

- Read `README.md`, `WORKFLOWS.md`, and the right change record before you edit files.
- Use the lightest mode that is still honest.
- Tie every claim to evidence.
- Name the controlled items when you change prompts, models, tools, dependencies, docs, skills, commands, templates, checkers, or releases.
- Hand off the work when you delegate it, pick it back up, or pass it to a reviewer, checker, or releaser with work still open.
- Double-check yourself before risky edits, risky commands, public claims, a trust change to a dependency, model, or API, or a release action.
- Use lessons from real operation (OPEX) when a near miss, a bad handoff, a review surprise, or an operating signal should update a lasting control.
- Declare your intent and reasoning before a critical action, so a reviewer can challenge the thinking, not just the result.
- Match authority to the evidence: decide reversible, well-evidenced work at the edge; escalate anything irreversible, trust-bearing, or thinly evidenced to a person.
- Halt unsafe or unclear work and surface the concern; raise known deficiencies so they are owned, not normalized.
- Hand off so the next owner is more capable, not more dependent.
- Prefer links and short status labels over long, repeated text.
- Run the right tests and checker commands before you say the work is done.

## Authority boundaries

Agents must not assume they may:

- change the release stance without a ship-readiness record;
- make bigger claims about where the ideas come from;
- add compliance or assurance claims;
- edit security-sensitive, credential, network, or production-facing material without clear permission;
- invoke "authority to information" to skip a required human gate on an irreversible or trust-bearing action;
- treat their own confidence or a fluent intent statement as evidence, or rubber-stamp another agent's output as an independent check;
- overwrite change records or templates without saying so.

## Recommended skills

- `skills/questioning-attitude/SKILL.md`
- `skills/rating-change-risk/SKILL.md`
- `skills/choosing-what-to-control/SKILL.md`
- `skills/checking-what-a-change-affects/SKILL.md`
- `skills/creating-change-records/SKILL.md`
- `skills/handing-off-work/SKILL.md`
- `skills/double-checking-before-acting/SKILL.md`
- `skills/recording-a-known-good-version/SKILL.md`
- `skills/proving-claims/SKILL.md`
- `skills/checking-release-readiness/SKILL.md`
- `skills/learning-from-experience/SKILL.md`
- `skills/vetting-outside-code-and-models/SKILL.md`
- `skills/checking-legal-and-safety-wording/SKILL.md`
- `skills/deciding-who-decides/SKILL.md`
- `skills/declaring-intent/SKILL.md`
- `skills/responding-to-incidents/SKILL.md`
- `skills/tracking-deficiencies/SKILL.md`

## Completion standard

An agent is not done until it can name:

- the files it changed;
- the change record or reasoning it used;
- the evidence it ran;
- the handoff, self-check, OPEX, or trust record it used, or why it did not need one;
- the intent it declared and the decision rights or escalation it used for any critical action;
- the gaps still open;
- the boundary wording it checked.

## Boundary note

Agent work in this repo does not create formal verification and validation, compliance, certification, safety, security, regulatory adequacy, or legal advice. None of those.
