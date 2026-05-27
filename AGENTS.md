# Agent Guidance

AI agents working in this repo should treat Nuclear-grade as an evidence workflow, not a branding exercise.
The public thesis is now questioning attitude, HPI micro-controls, and configuration management for AI-assisted software work: question assumptions, specify intent, brief the work, self-check critical actions, turn over cleanly, keep controlled items, evidence, decisions, baseline, and release posture linked.

## Default behavior

- Read `README.md`, `WORKFLOWS.md`, and the relevant packet before changing files.
- Use the smallest honest mode.
- Keep claims linked to evidence.
- Name controlled items when prompts, models, tools, dependencies, docs, skills, commands, templates, validators, or releases change.
- Use turnover when work is delegated, resumed, or handed to a reviewer/verifier/releaser with open work.
- Use self-checking before critical edits, commands, public claims, dependency/model/API trust changes, or release actions.
- Use OPEX when a near miss, bad handoff, review surprise, or operating signal should update a durable control.
- Prefer links and status labels over long repeated prose.
- Run relevant tests and validator commands before claiming completion.

## Authority boundaries

Agents must not assume authority to:

- change release posture without a ship-readiness record;
- broaden source-lineage claims;
- add compliance or assurance claims;
- edit security-sensitive, credential, network, or production-facing material without explicit scope;
- overwrite packets or templates silently.

## Recommended skills

- `skills/questioning-attitude/SKILL.md`
- `skills/classifying-change-risk/SKILL.md`
- `skills/identifying-controlled-items/SKILL.md`
- `skills/screening-change-impact/SKILL.md`
- `skills/creating-change-packets/SKILL.md`
- `skills/turning-over-agent-work/SKILL.md`
- `skills/self-checking-agent-actions/SKILL.md`
- `skills/baselining-configuration/SKILL.md`
- `skills/proving-claims/SKILL.md`
- `skills/reviewing-ship-readiness/SKILL.md`
- `skills/learning-from-opex/SKILL.md`
- `skills/checking-dependency-and-model-trust/SKILL.md`
- `skills/checking-license-and-assurance-boundaries/SKILL.md`

## Completion standard

An agent is not done until it can name:

- files changed;
- packet or rationale used;
- evidence run;
- turnover/self-check/OPEX/trust record used or why not activated;
- unresolved gaps;
- boundary language checked.

## Boundary note

Agent work in this repo does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, or legal advice.
