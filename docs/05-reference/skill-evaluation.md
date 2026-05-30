# Skill Evaluation Prompts

**Purpose:** Keep skill changes grounded in realistic trigger behavior instead of taste.

Use these prompts when changing a skill description or process. Run the same prompt with a simple baseline and with the relevant skill, compare the outputs, and record whether the skill adds useful structure, proof discipline, or decision clarity. The negative prompts are near-misses; they should usually be handled by another skill, a normal answer, or no skill at all.

Do not treat this file as proof that a skill is effective. It is the minimum prompt bank for future baseline-vs-skill evaluation.

## Evaluation Method

1. Snapshot the current skill before changing it.
2. Run at least three `Should trigger:` prompts and two `Should not trigger:` prompts.
3. Compare baseline, old-skill, and revised-skill outputs when improving an existing skill.
4. Prefer concrete artifacts, decisions, and evidence links over long prose.
5. Update the skill only when the revised behavior is clearly better, or when the trigger description fixes a clear miss.

## Prompt Bank

### `questioning-attitude`

- Should trigger: Before this agent changes the billing webhook, grill the assumptions and stop conditions.
- Should trigger: Review this plan for hidden risks before we let the coding agent edit files.
- Should trigger: What facts would change the release decision for this dependency update?
- Should trigger: The agent is asking many plausible questions but has not named the decision question the evidence must answer.
- Should not trigger: Fix a README typo and show the diff.
- Should not trigger: Explain what this small Python helper function does.

### `using-nuclear-grade`

- Should trigger: Use Nuclear-grade for an AI-assisted API behavior change and tell me the packet and evidence path.
- Should trigger: Set up the Nuclear-grade workflow for this repo before we let an agent change permissions.
- Should trigger: Walk this proposed coding-agent change through the workflow from question to release decision.
- Should not trigger: Summarize the README in five bullets.
- Should not trigger: What license does this repository use?

### `identifying-controlled-items`

- Should trigger: Which prompts, dependencies, docs, and CI files become controlled items for this release?
- Should trigger: Identify the controlled items for an agent tool-permission change.
- Should trigger: After this public launch, what approved-state tracking do we need?
- Should not trigger: Run the unit tests and paste the failing assertion.
- Should not trigger: Convert these notes into cleaner prose.

### `screening-change-impact`

- Should trigger: This lifecycle rename may stale docs, skills, commands, validators, and examples; screen the impact.
- Should trigger: If we change the packet template, what downstream artifacts need revalidation?
- Should trigger: Does a prompt/model baseline update affect release docs or evidence?
- Should not trigger: Create an empty Standard packet folder.
- Should not trigger: What does the changelog say changed last week?

### `baselining-configuration`

- Should trigger: Record the accepted prompt, model, tool, doc, and validator state after this release.
- Should trigger: Baseline this dependency update after review and verification pass.
- Should trigger: Create the accepted configuration record for the public docs and validator change.
- Should not trigger: Brainstorm better names for the workflow phases.
- Should not trigger: Classify whether this typo fix is Quick or Standard.

### `classifying-change-risk`

- Should trigger: Classify whether this API permission plus docs change is Quick, Standard, or stronger.
- Should trigger: Pick the right mode for a dependency bump that changes authentication behavior.
- Should trigger: This small diff touches agent authority; classify the risk and evidence obligation.
- Should trigger: The decision question is clear, but we do not know whether Quick proof is enough to answer it.
- Should not trigger: Fill out the verification table for already-selected Standard mode.
- Should not trigger: Write the source-lineage note for a citation change.

### `creating-change-packets`

- Should trigger: Create the packet files for a Standard change that updates skills and tests.
- Should trigger: Update this Quick packet now that the proof command changed.
- Should trigger: Prepare an evidence-backed PR packet for an AI-assisted workflow change.
- Should not trigger: Decide whether this packet should ship.
- Should not trigger: Only identify which files are controlled items.

### `packing-agent-context`

- Should trigger: Build a focused context pack for an agent that can edit tests and run commands.
- Should trigger: Prepare one-screen reviewer context with authority, proof, and stop conditions.
- Should trigger: Distill this long implementation thread into what the next agent may do and must prove.
- Should trigger: Package this work for a downstream agent with the decision question, work phase, forbidden claims, and stop conditions.
- Should not trigger: Run the packet validator.
- Should not trigger: Classify the change mode only.

### `turning-over-agent-work`

- Should trigger: Hand this half-finished validator change to a new agent with last completed action, changed conditions, proof gaps, and stop criteria.
- Should trigger: Prepare a release handoff for support after this Standard packet ships with residual risk and monitoring.
- Should trigger: We are resuming a long thread after CI changed; create a turnover record before the next agent edits files.
- Should not trigger: Summarize this README section without assigning follow-up work.
- Should not trigger: Run a Quick proof command for a completed typo fix.

### `self-checking-agent-actions`

- Should trigger: Before running this broad file move command, self-check the exact target, expected result, stop condition, and after-action proof.
- Should trigger: Self-check this public README claim before release because it says the workflow is secure.
- Should trigger: The agent is about to update dependency and API permission files; check the intended action and evidence first.
- Should trigger: This candidate doc wording is about to become accepted public baseline wording; check the target, expected result, and stop condition.
- Should not trigger: Explain what this shell command would do without running it.
- Should not trigger: Create a whole Standard packet for a normal feature change.

### `proving-claims`

- Should trigger: Map these release claims to evidence, gaps, and narrowed non-claims.
- Should trigger: Tests passed, but which claims do they actually prove?
- Should trigger: Turn this basis and trace into a verification table with pass, gap, and deferred statuses.
- Should trigger: Separate these claims into fact, assumption, unknown, source claim, local proof, and decision authority before ship review.
- Should not trigger: Create the packet directory structure.
- Should not trigger: Make the README more concise.

### `reviewing-ship-readiness`

- Should trigger: Review this Standard packet and decide ship, defer, block, or ship-with-risk.
- Should trigger: CI is green; decide whether the dependency update is release-ready and name residual risk.
- Should trigger: Is this agent-authority change ready to release with the evidence we have?
- Should trigger: This fast candidate is being promoted to an accepted baseline; slow-audit the evidence, rollback, monitoring, and residual risk.
- Should not trigger: Identify controlled items before implementation starts.
- Should not trigger: Draft the risk.md threshold screen.

### `learning-from-opex`

- Should trigger: An agent edited outside its context pack but tests caught it; create an OPEX record and durable control update.
- Should trigger: A reviewer found a hallucinated source claim after merge; turn the near miss into a template or validator update.
- Should trigger: Users misunderstood the release note and support needed a workaround; capture operating experience and rebaseline triggers.
- Should trigger: A doctrine update produced nice prose but no durable control change; turn the review surprise into OPEX.
- Should not trigger: Fix the failing unit test immediately during incident containment.
- Should not trigger: Assign blame for who approved the PR.

### `checking-dependency-and-model-trust`

- Should trigger: A dependency bump changes authentication behavior; separate vendor claims from local evidence and release impact.
- Should trigger: We are switching models for an agent workflow; check intended use, eval evidence, gaps, and revalidation triggers.
- Should trigger: This SaaS API will receive credentials and affect release automation; screen trust before shipping.
- Should not trigger: Cite a public DOE handbook as source lineage for a docs paragraph.
- Should not trigger: Fix a local typo in package comments with no dependency behavior change.

### `checking-source-lineage`

- Should trigger: This doc cites DOE and NIST concepts; check whether the wording is source-safe.
- Should trigger: Review these source-lineage claims before public launch.
- Should trigger: Does this adoption doc imply we satisfy external standards?
- Should not trigger: Fix the Python test failure.
- Should not trigger: Create a context pack for the next coding agent.

### `checking-license-and-assurance-boundaries`

- Should trigger: Review the README for license, warranty, compliance, and assurance boundary problems.
- Should trigger: This public copy may overpromise safety, security, certification, or adequacy; clean it up.
- Should trigger: Does this text confuse MIT license permission with formal engineering adequacy?
- Should not trigger: List changed files in the PR.
- Should not trigger: Run the worked-example tests.

### `controlling-mission-drift`

- Should trigger: We are twenty steps into this task and I cannot tell if the current edit still serves the original goal.
- Should trigger: The agent keeps adding features no one asked for; check whether we have drifted from the objective.
- Should trigger: We have retried this fix three times without progress; should we re-anchor, escalate, or stop?
- Should trigger: This small edit looks useful locally, but I cannot trace it to a mission success criterion.
- Should not trigger: Fix a README typo and show the diff.
- Should not trigger: Explain what this small helper function does.

### `reviewing-code-quality`

- Should trigger: Review this 1500-line module for needless complexity and tell me what to delete.
- Should trigger: Does this new wrapper earn its keep, or is it just indirection?
- Should trigger: Check whether feature-specific logic is leaking into the shared layer in this diff.
- Should not trigger: Confirm the unit test passes and paste the output.
- Should not trigger: Cite a public DOE handbook as source lineage for a docs paragraph.
### `red-teaming-agent-changes`

- Should trigger: Before releasing an agent that can write files and call APIs, enumerate the adversarial classes, state probe intents, and record outcomes.
- Should trigger: A dependency update changes how the agent processes user input; adversarially review for prompt injection and retrieval poisoning before shipping.
- Should trigger: This change expands the agent's network access; run a red-team review and link the posture note to ship.md.
- Should not trigger: Fix a README typo with no agent authority component.
- Should not trigger: Run a formal penetration test or produce a certified security report.

### `tracing-agent-execution`

- Should trigger: The packet claims the agent only edited auth.py but the release reviewer cannot see the step-level execution evidence; trace the run and link each step to a verification claim.
- Should trigger: Capture execution evidence from this agent run — tool calls, decision points, token use, and approval gates — and structure it for trace.md.
- Should trigger: A post-incident review needs to reconstruct what the agent did without reading a raw chat log; produce a structured execution trace.
- Should not trigger: The agent read a config file and printed a summary with no side effects.
- Should not trigger: Produce a formal audit trail or certified compliance record of agent behavior.

## Source-lineage note

This evaluation prompt bank is an original Nuclear-grade artifact informed by public skill-authoring practice: concise skills, realistic trigger prompts, baseline-vs-skill comparison, and iterative trigger-description improvement. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
