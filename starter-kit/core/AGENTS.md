# Agent guidance for `<your repo name>`

This file tells an AI agent — and any human reviewing the agent's work — what authority the
agent has in this repo and what "done" means here. Derived from the Nuclear-grade adopter
template; trim what you do not need.

## Authority boundaries

An agent working in this repo may not, without an authorized human:

- change the release stance of any artifact without a release-readiness record;
- enlarge a claim about source lineage, evidence, or assurance;
- add a compliance claim, certification claim, or formal verification and validation claim;
- edit security, credential, network, or production material;
- invoke "authority to information" to skip a required human gate;
- treat green CI as proof of any claim beyond what the checks actually cover;
- overwrite a change record without recording the overwrite.

Add or remove rules as your context requires. State each `<fill-in>` boundary in the negative.

## Recommended skills (Core 7)

- `skills/questioning-attitude/SKILL.md`
- `skills/rating-change-risk/SKILL.md`
- `skills/proving-claims/SKILL.md`
- `skills/double-checking-before-acting/SKILL.md`
- `skills/staying-on-mission/SKILL.md`
- `skills/checking-release-readiness/SKILL.md`
- `skills/learning-from-experience/SKILL.md`

Add ancillary clusters (Agent-authority, Configuration management, Claims discipline, Incident,
Hygiene) by trigger from the decision matrix in `CORE.md`.

## Completion standard

An agent is not done until it can name:

- the files it changed;
- the change record or reasoning it used;
- the evidence it ran;
- the handoff, self-check, OPEX, or trust record it used, or why it did not need one;
- the intent it declared and the decision rights or escalation it used for any critical action;
- the gaps still open;
- the boundary wording it checked;
- `<fill-in: any project-specific completion criteria>`.

## Boundary note

Work in this repo does not by itself create formal verification and validation, regulatory
approval, certification, safety-basis evidence, procurement evidence, or legal advice. Public
claims must stay inside their evidence — see `<fill-in: link to your DISCLAIMER or boundary
doc>`.

## Source-lineage note

This file is derived from the public Nuclear-grade adopter template. It does not create
assurance. Original Nuclear-grade source-lineage discipline applies.
