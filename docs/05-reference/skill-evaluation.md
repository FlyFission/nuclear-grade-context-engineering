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

## The existence decision: evidence-based, not declared

A skill carries two separate decisions (see `skill-authoring-contract.md`): the receipt it must emit, and -- separately -- whether it deserves to exist at all. The receipt's tier (`block` / `warn` / `observe`) is author-declared; the existence decision is not. Whether a skill earns its keep comes from the numbers, because a guard inside the writable set is a suggestion the author can edit.

To measure it, extend the baseline-vs-skill comparison above:

1. For each `Should trigger:` prompt, run the baseline and the skill, and record one bit -- did the skill change a real decision (merge, rollback, escalation, or review scope), or only reword the same outcome?
2. Track that bit over real runs, not a single sample.
3. A skill whose decision-changing rate stays at or near zero is demoted to the `observe` tier -- it stays in telemetry, out of the operator receipt -- and becomes a **relocation candidate**: its content is reference, not a control, and belongs in `docs/` (the move already applied to `core-source-rationale.md`). Open the relocation or deletion as its own change with its own evidence; no skill is removed on one run, and the call is a human's.

If a skill changes decisions but says so only in vague prose, amend its receipt until it is machine-checkable rather than dropping it.

`ng decisions` prints the operator receipt (`block`/`warn`) and, with `--all`, the `observe`-tier skills held in telemetry; `ng tokens` reports tokens-per-decision-signal for the worked examples. Together they point a reviewer at the skills paying the most prose for the least decision movement.

## Prompt Bank

### `questioning-attitude`

- Should trigger: Before this agent changes the billing webhook, grill the assumptions and stop conditions.
- Should trigger: Review this plan for hidden risks before we let the coding agent edit files.
- Should trigger: What facts would change the release decision for this dependency update?
- Should trigger: The agent is asking many plausible questions but has not named the decision question the evidence must answer.
- Should trigger: This is a brownfield change to the billing schema — classify the work type and name the migration and rollback questions it forces.
- Should not trigger: Fix a README typo and show the diff.
- Should not trigger: Explain what this small Python helper function does.

### `using-nuclear-grade`

- Should trigger: Use Nuclear-grade for an AI-assisted API behavior change and tell me the packet and evidence path.
- Should trigger: Set up the Nuclear-grade workflow for this repo before we let an agent change permissions.
- Should trigger: Walk this proposed coding-agent change through the workflow from question to release decision.
- Should not trigger: Summarize the README in five bullets.
- Should not trigger: What license does this repository use?

### `choosing-what-to-control`

- Should trigger: Which prompts, dependencies, docs, and CI files become controlled items for this release?
- Should trigger: Identify the controlled items for an agent tool-permission change.
- Should trigger: After this public launch, what approved-state tracking do we need?
- Should not trigger: Run the unit tests and paste the failing assertion.
- Should not trigger: Convert these notes into cleaner prose.

### `checking-what-a-change-affects`

- Should trigger: This lifecycle rename may stale docs, skills, commands, validators, and examples; screen the impact.
- Should trigger: If we change the packet template, what downstream artifacts need revalidation?
- Should trigger: Does a prompt/model baseline update affect release docs or evidence?
- Should trigger: This change alters a database schema other services read — screen the runtime blast radius and backward-compatibility, not just repo docs.
- Should not trigger: Create an empty Standard packet folder.
- Should not trigger: What does the changelog say changed last week?

### `recording-a-known-good-version`

- Should trigger: Record the accepted prompt, model, tool, doc, and validator state after this release.
- Should trigger: Baseline this dependency update after review and verification pass.
- Should trigger: Create the accepted configuration record for the public docs and validator change.
- Should not trigger: Brainstorm better names for the workflow phases.
- Should not trigger: Classify whether this typo fix is Quick or Standard.

### `rating-change-risk`

- Should trigger: Classify whether this API permission plus docs change is Quick, Standard, or stronger.
- Should trigger: Pick the right mode for a dependency bump that changes authentication behavior.
- Should trigger: This small diff touches agent authority; classify the risk and evidence obligation.
- Should trigger: The decision question is clear, but we do not know whether Quick proof is enough to answer it.
- Should not trigger: Fill out the verification table for already-selected Standard mode.
- Should not trigger: Write the source-lineage note for a citation change.

### `creating-change-records`

- Should trigger: Create the packet files for a Standard change that updates skills and tests.
- Should trigger: Update this Quick packet now that the proof command changed.
- Should trigger: Prepare an evidence-backed PR packet for an AI-assisted workflow change.
- Should not trigger: Decide whether this packet should ship.
- Should not trigger: Only identify which files are controlled items.

### `briefing-an-agent`

- Should trigger: Build a focused context pack for an agent that can edit tests and run commands.
- Should trigger: Prepare one-screen reviewer context with authority, proof, and stop conditions.
- Should trigger: Distill this long implementation thread into what the next agent may do and must prove.
- Should trigger: Package this work for a downstream agent with the decision question, work phase, forbidden claims, and stop conditions.
- Should not trigger: Run the packet validator.
- Should not trigger: Classify the change mode only.

### `handing-off-work`

- Should trigger: Hand this half-finished validator change to a new agent with last completed action, changed conditions, proof gaps, and stop criteria.
- Should trigger: Prepare a release handoff for support after this Standard packet ships with residual risk and monitoring.
- Should trigger: We are resuming a long thread after CI changed; create a turnover record before the next agent edits files.
- Should not trigger: Summarize this README section without assigning follow-up work.
- Should not trigger: Run a Quick proof command for a completed typo fix.

### `double-checking-before-acting`

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

### `checking-release-readiness`

- Should trigger: Review this Standard packet and decide ship, defer, block, or ship-with-risk.
- Should trigger: CI is green; decide whether the dependency update is release-ready and name residual risk.
- Should trigger: Is this agent-authority change ready to release with the evidence we have?
- Should trigger: This fast candidate is being promoted to an accepted baseline; slow-audit the evidence, rollback, monitoring, and residual risk.
- Should not trigger: Identify controlled items before implementation starts.
- Should not trigger: Draft the risk.md threshold screen.

### `learning-from-experience`

- Should trigger: An agent edited outside its context pack but tests caught it; create an OPEX record and durable control update.
- Should trigger: A reviewer found a hallucinated source claim after merge; turn the near miss into a template or validator update.
- Should trigger: Users misunderstood the release note and support needed a workaround; capture operating experience and rebaseline triggers.
- Should trigger: A doctrine update produced nice prose but no durable control change; turn the review surprise into OPEX.
- Should not trigger: Fix the failing unit test immediately during incident containment.
- Should not trigger: Assign blame for who approved the PR.

### `vetting-outside-code-and-models`

- Should trigger: A dependency bump changes authentication behavior; separate vendor claims from local evidence and release impact.
- Should trigger: We are switching models for an agent workflow; check intended use, eval evidence, gaps, and revalidation triggers.
- Should trigger: This SaaS API will receive credentials and affect release automation; screen trust before shipping.
- Should not trigger: Cite a public DOE handbook as source lineage for a docs paragraph.
- Should not trigger: Fix a local typo in package comments with no dependency behavior change.

### `checking-source-claims`

- Should trigger: This doc cites DOE and NIST concepts; check whether the wording is source-safe.
- Should trigger: Review these source-lineage claims before public launch.
- Should trigger: Does this adoption doc imply we satisfy external standards?
- Should not trigger: Fix the Python test failure.
- Should not trigger: Create a context pack for the next coding agent.

### `checking-legal-and-safety-wording`

- Should trigger: Review the README for license, warranty, compliance, and assurance boundary problems.
- Should trigger: This public copy may overpromise safety, security, certification, or adequacy; clean it up.
- Should trigger: Does this text confuse MIT license permission with formal engineering adequacy?
- Should not trigger: List changed files in the PR.
- Should not trigger: Run the worked-example tests.

### `staying-on-mission`

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
### `stress-testing-agent-changes`

- Should trigger: Before releasing an agent that can write files and call APIs, enumerate the adversarial classes, state probe intents, and record outcomes.
- Should trigger: A dependency update changes how the agent processes user input; adversarially review for prompt injection and retrieval poisoning before shipping.
- Should trigger: This change expands the agent's network access; run a red-team review and link the posture note to ship.md.
- Should not trigger: Fix a README typo with no agent authority component.
- Should not trigger: Run a formal penetration test or produce a certified security report.

### `recording-what-an-agent-did`

- Should trigger: The packet claims the agent only edited auth.py but the release reviewer cannot see the step-level execution evidence; trace the run and link each step to a verification claim.
- Should trigger: Capture execution evidence from this agent run — tool calls, decision points, token use, and approval gates — and structure it for trace.md.
- Should trigger: A post-incident review needs to reconstruct what the agent did without reading a raw chat log; produce a structured execution trace.
- Should not trigger: The agent read a config file and printed a summary with no side effects.
- Should not trigger: Produce a formal audit trail or certified compliance record of agent behavior.

### `breaking-down-the-work`

- Should trigger: Break this billing-revamp epic into a clean deliverable breakdown that covers all the scope with no overlaps before we plan.
- Should trigger: We keep discovering work mid-sprint; give me a product WBS with a dictionary for this new ingestion subsystem.
- Should trigger: Decompose this feature into work packages and check that the children actually sum to the whole.
- Should trigger: We are handing these work packages to separate agents — turn the WBS leaves into delegable build-sequence slices with prereqs, per-slice proof, and stop conditions.
- Should not trigger: Fix this typo in the README and show the diff.
- Should not trigger: This backlog item is already broken down and owned; just start coding it.

### `organizing-project-folders`

- Should trigger: Lay out the folder and file structure for this new service derived from our WBS, with safe sortable names.
- Should trigger: Our shared utils folder has become a junk drawer; restructure it by what changes together.
- Should trigger: Design this sequential agent workflow as numbered stage folders with a context contract per stage.
- Should not trigger: Rename this one file from helper to parser in an already-clean tree.
- Should not trigger: Run the unit tests and paste the failing assertion.

### `closing-stale-packets`

- Should trigger: `ng status` shows three scaffold packets nobody can explain; decide what to do with each.
- Should trigger: This long session left a half-filled packet behind and the change was dropped; close it properly.
- Should trigger: Our `.nuclear/changes` directory is full of abandoned drafts; bring each to a terminal state.
- Should trigger: That packet's feature was cut last sprint but its packet is still sitting there as invalid.
- Should not trigger: I am actively filling this packet right now and about to validate it.
- Should not trigger: Delete the placeholder marker so this packet I am shipping passes validation.

### `deciding-who-decides`

- Should trigger: The agent wants to delete a production table; decide whether it may act or must escalate, and name the trigger.
- Should trigger: Set this coding agent's standing authority so reversible edits proceed but releases and permission changes escalate.
- Should trigger: Who should decide this dependency bump given the evidence is only the vendor's changelog?
- Should not trigger: Fix a typo in a comment and show the diff.
- Should not trigger: The director already approved this; just record that approval.

### `declaring-intent`

- Should trigger: Before the agent deploys the new pricing path to 5% of traffic, state intent, expected result, and abort criteria.
- Should trigger: Write the release brief for this schema migration so a reviewer can challenge the plan before it runs.
- Should trigger: The agent is about to rotate the signing key; declare the intent and the verified rollback first.
- Should not trigger: Reformat this file with the linter and commit it.
- Should not trigger: Summarize what this helper function returns.

### `responding-to-incidents`

- Should trigger: Checkout is failing for 30% of users right now; run this as an incident.
- Should trigger: An agent deleted rows it should not have and customers are affected; stabilize and coordinate.
- Should trigger: The canary tripped its abort threshold and the release is half-rolled-out; take it as a live incident.
- Should not trigger: Plan next quarter's reliability roadmap.
- Should not trigger: Write the postmortem for the outage that was fully resolved last week.

### `tracking-deficiencies`

- Should trigger: This test has been flaky for months and everyone ignores it; log it so it is owned and dispositioned.
- Should trigger: We keep getting paged by the same noisy alert; put it on the deficiency register with an owner.
- Should trigger: Review surfaced an unowned service we have all been avoiding; record it as fix-or-accept.
- Should not trigger: I just fixed this bug and closed the packet; no standing tracking is needed.
- Should not trigger: Start a brand-new feature that has no known deficiencies yet.

## Source-lineage note

This evaluation prompt bank is an original Nuclear-grade artifact informed by public skill-authoring practice: concise skills, realistic trigger prompts, baseline-vs-skill comparison, and iterative trigger-description improvement. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
