# Nuclear-grade Skills

Skills are self-contained agent instructions. Each skill has a `SKILL.md` contract with triggers, inputs, process, outputs, verification, escalation, red flags, and source-lineage boundaries.

## Catalog

| Skill | Use when | Output |
|---|---|---|
| [`questioning-attitude`](skills/questioning-attitude/SKILL.md) | Challenging assumptions before work, review, or release continues | Assumptions, evidence gaps, stop conditions |
| [`using-nuclear-grade`](skills/using-nuclear-grade/SKILL.md) | Adopting the workflow for a change or repo | Mode, packet path, evidence path |
| [`identifying-controlled-items`](skills/identifying-controlled-items/SKILL.md) | Deciding what configuration must be controlled | Controlled item list |
| [`screening-change-impact`](skills/screening-change-impact/SKILL.md) | Checking downstream impact and revalidation triggers | Impact screen |
| [`baselining-configuration`](skills/baselining-configuration/SKILL.md) | Recording accepted controlled configuration state | Baseline record |
| [`classifying-change-risk`](skills/classifying-change-risk/SKILL.md) | Selecting Quick, Standard, or stronger human-reviewed mode | Mode decision and evidence obligation |
| [`creating-change-packets`](skills/creating-change-packets/SKILL.md) | Creating or updating packet files | Quick or Standard packet |
| [`packing-agent-context`](skills/packing-agent-context/SKILL.md) | Preparing focused agent or reviewer context | Context pack |
| [`turning-over-agent-work`](skills/turning-over-agent-work/SKILL.md) | Handing off unfinished agent, review, verification, release, or resumed-thread work | Turnover record |
| [`self-checking-agent-actions`](skills/self-checking-agent-actions/SKILL.md) | Checking critical agent edits, commands, public claims, trust changes, or releases before action | Self-check record |
| [`proving-claims`](skills/proving-claims/SKILL.md) | Mapping claims to evidence and gaps | Claim-to-evidence rows |
| [`reviewing-ship-readiness`](skills/reviewing-ship-readiness/SKILL.md) | Deciding ship, block, defer, or ship-with-risk | Release decision record |
| [`learning-from-opex`](skills/learning-from-opex/SKILL.md) | Turning near misses, bad handoffs, review surprises, or operating signals into durable updates | OPEX action |
| [`checking-dependency-and-model-trust`](skills/checking-dependency-and-model-trust/SKILL.md) | Reviewing dependency, model, API, SaaS, generated artifact, or vendor trust | Intended-use trust screen |
| [`checking-source-lineage`](skills/checking-source-lineage/SKILL.md) | Reviewing citation and source-family claims | Source-safe wording |
| [`checking-license-and-assurance-boundaries`](skills/checking-license-and-assurance-boundaries/SKILL.md) | Reviewing license and assurance language | Boundary-safe wording |

## Contract

Every skill must include:

- YAML frontmatter with `name` and `description`.
- A description that starts with `Use when`.
- Overview, use and non-use conditions, inputs, process, outputs, verification, escalation, common rationalizations, red flags, and source-lineage note.

See `docs/05-reference/skill-authoring-contract.md`.

## Boundary note

Skills help agents preserve evidence and boundaries. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
