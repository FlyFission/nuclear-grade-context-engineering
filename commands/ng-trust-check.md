# ng-trust-check

## Purpose

Check dependency, model, API, SaaS, generated-artifact, or vendor trust before it supports evidence, permissions, data, release posture, or public claims. This is a portable command prompt.

## Use when

- A change adds or updates an external package, model, API, SaaS tool, build service, generated artifact, or data source.
- Vendor/source claims are being used as evidence.
- Credentials, network access, data handling, release posture, or public trust may change.

## Do not use when

- The dependency is dev-only, reversible, and already covered by Quick proof.
- A qualified security, legal, procurement, or regulated-use review is required outside this repo.

## Inputs

- External item identity, version/model/API surface, provider, intended use, claims relied on, local evidence, gaps, controls, and revalidation trigger.

## Prompt text

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

Separate external claims from local evidence. Return intended-use decision, gaps, compensating controls, release impact, and whether to ship, defer, block, or require qualified review.
```

## Files created or modified

- `supplier-trust.md` or a trust section in `basis.md`, `verification.md`, `ship.md`, or `decision.md`.

## Expected outputs

- Intended-use decision, evidence/gap table, compensating controls, owner, and revalidation trigger.
- Release posture impact.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Vendor language is treated as local proof.
- Version, model, provider, or API surface is unnamed.
- Tests pass while advisory, license, permission, or behavior evidence is missing.

## Legal/assurance boundary note

Trust checks support intended-use review. They do not create formal supplier qualification, security assurance, procurement adequacy, compliance, certification, safety, security, or regulatory approval.
