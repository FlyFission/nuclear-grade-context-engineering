---
name: vetting-outside-code-and-models
description: Checks dependencies, models, APIs, SaaS tools, generated files, and vendor claims against how you will actually use them, the proof you have, the gaps, and the release impact. Use when any of these affect evidence, permissions, data, releases, or public trust. Do not use for an internal cleanup with no outside dependency, or for a does-it-work question.
---

# Vetting Outside Code and Models

## Overview

Trusting outside code is really a decision about how you will use it. A dependency, model, API, SaaS tool (software you rent online), or vendor claim should be accepted only for the job its evidence and controls actually support. Trust it for that job. Do not trust it past that.

## Decision contract

- **Claim checked:** the dependency, model, API, or SaaS is accepted only for a use no broader than repo-side evidence supports, vendor claims kept apart from proof, each gap given a re-check trigger or routed to a release decision.
- **Artifact observed:** the named dependency/version/provider, vendor claims, and own-repo evidence -> a supplier-trust section or `supplier-trust.md` with the use decision, gaps, backup controls, and release impact.
- **Decision affected:** block -- whether to trust and use the dependency, model, API, or SaaS; unresolved gaps feed `ship.md` defer/block/ship-with-risk.
- **Failure class:** boundary-overreach (trust stated past repo-side evidence, or vendor marketing treated as proof).
- **Next action:** route the unresolved gap to `ship.md`; credentials, production data, or security/privacy claims escalate to a qualified review.

## When to Use

- A change adds or updates a package, a model, an API, an online service, a generated file, a build service, or a data source.
- You are leaning on an outside claim as proof of behavior, security, privacy, reliability, licensing, or release readiness.
- A tool gets credentials, network access, data access, or a say in releases.

## When Not to Use

- The dependency is for development only, easy to undo, and already covered by a quick proof.
- The request is only to cite a public source, not to lean on it as trust evidence.
- A qualified security or purchasing review is needed, which happens outside this repo.

## Inputs

- The dependency, model, API, or tool: its name, version, provider, intended use, and which controlled items it touches.
- The vendor or source claims, the evidence you saw yourself, the backup controls, and what would force a re-check.
- The effects on data, credentials, permissions, the build, the release, and public claims.

## Process

1. State how you will use it, and what happens if it is wrong, missing, hacked, or changed.
2. Keep vendor and source claims separate from evidence you saw in your own repo.
3. Find the effects on data, credentials, permissions, license, release, and public trust.
4. Name the backup controls, the proof, the owner, and what would force a re-check.
5. Send any unresolved trust gap to a decision: defer, block, or ship with known risk.

## Outputs

- A supplier-trust section, a `supplier-trust.md` file, or a trust table in the change record.
- The use decision, the evidence, the gaps, the backup controls, and the re-check trigger.
- The release impact for `ship.md` or `decision.md`.

## Verification

- The repo never treats outside marketing or docs as proof of how the code behaves here.
- The intended use is no broader than the evidence you have.
- Gaps flow into the verification and release records.

## Escalation

- Escalate for credentials, production data, security or privacy claims, real dependency risk, model behavior drifting, or public trust claims.
- Require a qualified review when legal, security, safety, purchasing, or regulated-use fitness is being decided.

## Common Rationalizations

- "The vendor says it is secure." Vendor wording is input, not proof from your own repo.
- "It is just a minor version bump." Small changes can still shift trust.
- "The model is better." Better is not proof it fits this use.

## Red Flags

- The version, model, provider, or API surface is not named.
- There is no re-check trigger.
- Public claims go past the evidence you actually saw.
- Tests pass, but the dependency advisory, license, permission, or model-behavior evidence is missing.

## Prompt

```text
Check Nuclear-grade dependency/model/API trust.

Inputs:
- packet:
- external item:
- provider/source:
- version/model/API surface:
- intended use:
- consequence if wrong/unavailable/compromised/changed:
- data/credential/permission/network impact:
- vendor/source claims:
- repo-observed evidence:
- compensating controls:
- revalidation trigger:

Keep the outside claims separate from your local evidence. Return a decision for how you intend to use it, the gaps, the controls that make up for them, the effect on the release, and whether to ship, defer, block, or require a qualified review.
```

## Source-lineage note

This skill is an original software-workflow translation of vendor oversight, validation of assumptions, verification practices, change management, and conservative decision making from DOE-HDBK-1028-2009 plus public software supply-chain and AI-risk source families mapped in the repo. It does not create DOE compliance, formal assurance, safety, security, certification, procurement adequacy, or regulatory adequacy.
