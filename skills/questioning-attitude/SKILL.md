---
name: questioning-attitude
description: Use when a change request, diff, plan, dependency, agent action, or release decision needs skeptical fact-finding before work continues.
---

# Questioning Attitude

## Overview

Questioning attitude is the Nuclear-grade front door: challenge assumptions before an agent builds, merges, or releases. Prefer facts over confidence, surface uncertainty, and stop when a doubt changes the decision.

## When to Use

- A request is vague, consequential, or easy to rationalize.
- A diff, plan, dependency, prompt, model, tool, or release claim needs skeptical review.
- A reviewer asks "what are we assuming?" or "what would make this wrong?"
- An agent is about to receive file, command, network, credential, approval, or release authority.

## When Not to Use

- The task is a tiny Quick edit with obvious proof and no new trust boundary.
- Incident containment must happen before analysis.
- The user is asking for formal assurance, certification, safety analysis, or regulatory approval.

## Inputs

- User request, issue, PR, diff, or packet path.
- Affected files, dependencies, prompts, models, tools, data, and release artifacts.
- Known assumptions, constraints, evidence, and gaps.
- Relevant prior packets, OPEX notes, or source-map rows when invoked.

## Process

1. Restate the change as a falsifiable decision question.
2. List assumptions that must be true for the change to work.
3. Identify uncertainty, warning signs, error-likely steps, and hidden Standard-mode triggers.
4. Ask what evidence would change the decision.
5. Validate facts before relying on memory, confidence, or agent-generated claims.
6. Name stop conditions, hold conditions, and escalation triggers.
7. Route the next artifact: Quick proof, Standard spec, context pack, CM record, or release decision.

## Outputs

- Questioning-attitude screen or `questioning-attitude.md`.
- Validated assumptions and unresolved uncertainties.
- Mode/escalation triggers.
- Evidence needed before execute, verify, review, decide, or baseline.

## Verification

- Assumptions are explicit and either validated, gap-labeled, or assigned.
- The selected mode follows the evidence, not preference or effort.
- Stop conditions are concrete enough for an agent or reviewer to obey.
- The next packet artifact is named.

## Escalation

- Escalate when facts are missing for user, data, security, dependency, AI-authority, operational, or release consequence.
- Stop when a claim cannot be supported by available evidence.
- Require independent review when confidence depends on one agent's interpretation.

## Common Rationalizations

- "It worked last time." Past success is not evidence that this state is still controlled.
- "The agent seems confident." Confidence is not a source.
- "We can classify later." Mode selection depends on assumptions and uncertainty now.
- "It is just docs." Public wording can change trust and adoption behavior.

## Red Flags

- Unverified assumptions drive implementation.
- The packet names proof after the work is already done.
- Standard triggers are dismissed because the diff is small.
- Release language says "safe", "secure", "approved", or "compliant" without qualified external authority.

## Source-lineage note

This skill is an original software-workflow translation of questioning attitude, validate-assumptions, pause-when-unsure, and review practices from DOE-HDBK-1028-2009, Human Performance Improvement Handbook, Volumes 1 and 2, as public source lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
