# Nuclear-grade Context Engineering — Domain Context

This file defines the repository's current domain language for agents and contributors. It is a vocabulary map, not an assurance or compliance claim.

## Core concepts

- **Candidate change:** the specific code, configuration, prompt, model, dependency, documentation, or operational state proposed for acceptance.
- **Trust-bearing claim:** a claim whose acceptance materially affects whether the candidate may proceed.
- **Evidence item:** an artifact admitted in support of a claim: test output, trace, review, analysis, measurement, source, or witnessed observation.
- **Evidence custody:** who generated, selected, transformed, summarized, executed or captured, retained, and presented an evidence item.
- **Change actor:** the person, agent, or coupled process that produced the candidate change.
- **Actor–evidence coupling:** the degree to which the change actor also controls the evidence path used to accept the change.
- **Coupling profile:** a five-axis record of actor, context, mechanism, authority, and resource separation. The axes form a partial order; do not collapse them into a single score or rung.
- **Evidence verdict:** a judgment about what the admitted evidence supports.
- **Apply clearance:** current authorization to mutate a particular target with a particular candidate under present conditions. A verdict is not standing apply authority.
- **Accepted baseline:** the candidate state accepted at a decision point, together with the evidence, authority, and conditions that supported acceptance.
- **Revalidation trigger:** an event that makes prior evidence, verdict, clearance, or baseline reliance stale.

## Coupling-profile axes

Each axis is recorded as `coupled`, `partially separated`, or `separated`, with a short basis:

1. **Actor:** who generated or witnessed the decisive evidence relative to the change actor.
2. **Context:** whether the verifier reconstructed the case independently or inherited the actor's framing, omissions, and summary.
3. **Mechanism:** whether actor and verifier rely on the same tests, oracle, model family, prompt pattern, tools, or execution path.
4. **Authority:** who controls evidence scope, acceptance thresholds, sufficiency, verdict, and apply decision.
5. **Resource:** who controls the verifier's budget, runtime, credentials, environment, storage, and ability to publish adverse results.

## Invariants

- Provenance and hashes establish linkage and integrity, not truth, adequacy, identity, independence, or authorization.
- A self-check can reduce error but does not become independent evidence by being well written.
- Every trust-bearing claim exposes evidence custody and residual coupling.
- Consequence determines the minimum acceptable coupling profile; there is no universal linear independence ladder.
- Evidence verdict and apply clearance remain separate records.
- Any stale baseline, changed target, expired authority, altered environment, or invalidated evidence triggers revalidation.

## Source boundary

The model translates established ideas from professional self-review threats, independent verification, assurance cases, provenance, policy enforcement, and AI-evaluation bias into a software-agent acceptance workflow. The repository claims an open operational synthesis, not invention of those underlying disciplines and not formal V&V, compliance, safety, security, certification, or regulatory adequacy.
