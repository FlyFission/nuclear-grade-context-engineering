---
name: checking-dependency-and-model-trust
description: Use when dependencies, models, APIs, SaaS tools, generated artifacts, or vendor claims affect evidence, permissions, data, release posture, or public trust.
---

# Checking Dependency And Model Trust

## Overview

External trust is an intended-use decision. A dependency, model, API, SaaS tool, or vendor claim should be accepted only for the scope its evidence and controls support.

## When to Use

- A change adds or updates a package, model, API, SaaS service, generated artifact, build service, or data source.
- External claims are used as evidence for behavior, security, privacy, reliability, licensing, or release posture.
- A tool gains credentials, network access, data access, or release influence.

## When Not to Use

- The dependency is dev-only, reversible, and already covered by Quick proof.
- The request is only to cite a public source without adopting the source as trust evidence.
- A qualified security or procurement review is required outside this repo.

## Inputs

- Dependency/model/API/tool identity, version, provider, intended use, and affected controlled items.
- Vendor/source claims, observed evidence, compensating controls, and revalidation triggers.
- Data, credential, permission, build, release, and public-claim impacts.

## Process

1. State the intended use and consequence if the external item is wrong, unavailable, compromised, or changed.
2. Separate vendor/source claims from repo-observed evidence.
3. Identify data, credential, permission, license, release, and public-trust impacts.
4. Name compensating controls, verification evidence, owner, and revalidation trigger.
5. Route unresolved trust gaps to defer, block, or ship-with-residual-risk decisions.

## Outputs

- Supplier-trust section, `supplier-trust.md`, or packet trust table.
- Intended-use decision, evidence, gaps, compensating controls, and revalidation trigger.
- Release impact for `ship.md` or `decision.md`.

## Verification

- The repo does not treat external marketing or docs as proof of local behavior.
- Intended use is narrower than or equal to available evidence.
- Gaps flow into verification and release decision records.

## Escalation

- Escalate for credentials, production data, security/privacy claims, material dependency risk, model behavior drift, or public trust claims.
- Require qualified review when legal, security, safety, procurement, or regulated-use adequacy is being decided.

## Common Rationalizations

- "The vendor says it is secure." Vendor language is input, not local proof.
- "It is a minor version bump." Small changes can alter trust posture.
- "The model is better." Better is not evidence for this intended use.

## Red Flags

- Version, model, provider, or API surface is unnamed.
- No revalidation trigger.
- Public claims exceed observed evidence.
- Tests pass but dependency advisory, license, permission, or model-behavior evidence is missing.

## Source-lineage note

This skill is an original software-workflow translation of vendor oversight, validation of assumptions, verification practices, change management, and conservative decision making from DOE-HDBK-1028-2009 plus public software supply-chain and AI-risk source families mapped in the repo. It does not create DOE compliance, formal assurance, safety, security, certification, procurement adequacy, or regulatory adequacy.
