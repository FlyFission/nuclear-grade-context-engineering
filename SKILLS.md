# Nuclear-grade Skills

Skills are self-contained agent instructions. Each skill has a `SKILL.md` contract with triggers, inputs, process, outputs, verification, escalation, red flags, and source-lineage boundaries.

## Catalog

| Skill | Use when | Output |
|---|---|---|
| [`questioning-attitude`](skills/questioning-attitude/SKILL.md) | Challenging assumptions before work, review, or release continues | Assumptions, evidence gaps, stop conditions |
| [`using-nuclear-grade`](skills/using-nuclear-grade/SKILL.md) | Adopting the workflow for a change or repo | Mode, packet path, evidence path |
| [`choosing-what-to-control`](skills/choosing-what-to-control/SKILL.md) | Deciding what configuration must be controlled | Controlled item list |
| [`checking-what-a-change-affects`](skills/checking-what-a-change-affects/SKILL.md) | Checking downstream impact and revalidation triggers | Impact screen |
| [`recording-a-known-good-version`](skills/recording-a-known-good-version/SKILL.md) | Recording accepted controlled configuration state | Baseline record |
| [`rating-change-risk`](skills/rating-change-risk/SKILL.md) | Selecting Quick, Standard, or stronger human-reviewed mode | Mode decision and evidence obligation |
| [`creating-change-records`](skills/creating-change-records/SKILL.md) | Creating or updating packet files | Quick or Standard packet |
| [`briefing-an-agent`](skills/briefing-an-agent/SKILL.md) | Preparing focused agent or reviewer context | Context pack |
| [`handing-off-work`](skills/handing-off-work/SKILL.md) | Handing off unfinished agent, review, verification, release, or resumed-thread work | Turnover record |
| [`double-checking-before-acting`](skills/double-checking-before-acting/SKILL.md) | Checking critical agent edits, commands, public claims, trust changes, or releases before action | Self-check record |
| [`proving-claims`](skills/proving-claims/SKILL.md) | Mapping claims to evidence and gaps | Claim-to-evidence rows |
| [`checking-release-readiness`](skills/checking-release-readiness/SKILL.md) | Deciding ship, block, defer, or ship-with-risk | Release decision record |
| [`learning-from-experience`](skills/learning-from-experience/SKILL.md) | Turning near misses, bad handoffs, review surprises, or operating signals into durable updates | OPEX action |
| [`vetting-outside-code-and-models`](skills/vetting-outside-code-and-models/SKILL.md) | Reviewing dependency, model, API, SaaS, generated artifact, or vendor trust | Intended-use trust screen |
| [`checking-source-claims`](skills/checking-source-claims/SKILL.md) | Reviewing citation and source-family claims | Source-safe wording |
| [`checking-legal-and-safety-wording`](skills/checking-legal-and-safety-wording/SKILL.md) | Reviewing license and assurance language | Boundary-safe wording |
| [`staying-on-mission`](skills/staying-on-mission/SKILL.md) | Work drifts from the objective, scope creeps, or rigor erodes one concession at a time | Re-anchor / escalate / stop decision and updated mission anchor |
| [`reviewing-code-quality`](skills/reviewing-code-quality/SKILL.md) | Reviewing a diff or module for standards drift and needless complexity | Prioritized findings and a single verdict |
| [`stress-testing-agent-changes`](skills/stress-testing-agent-changes/SKILL.md) | Adversarially probing agent tool grants, dependencies, models, or releases for injection, escalation, unsafe output, or tool misuse | Red-team findings record |
| [`recording-what-an-agent-did`](skills/recording-what-an-agent-did/SKILL.md) | Capturing agent tool calls, decisions, inputs, outputs, token use, and approval gates as structured execution evidence | Execution trace record |
| [`breaking-down-the-work`](skills/breaking-down-the-work/SKILL.md) | Decomposing an epic, feature, or subsystem into a product-oriented, 100%-rule, non-overlapping work breakdown | WBS table and dictionary |
| [`organizing-project-folders`](skills/organizing-project-folders/SKILL.md) | Laying out a repo or agent workspace, placing a file, or fixing a junk-drawer directory | Folder map and naming/depth audit |

## Contract

Every skill must include:

- YAML frontmatter with `name` and `description` (required); `license` and `compatibility` are optional.
- A `name` that is lowercase and hyphen-separated.
- A `description` that says what the skill does, when to trigger it, and a "Do not use for ..." negative clause (80 to 500 characters, no colon-space).
- Overview, use and non-use conditions, inputs, process, outputs, verification, escalation, common rationalizations, red flags, and source-lineage note.

Skills may add optional `references/`, `scripts/`, and `assets/` subfolders for progressive disclosure. See `docs/05-reference/skill-authoring-contract.md`.

## Boundary note

Skills help agents preserve evidence and boundaries. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
