# ng-trust-check

## Purpose

Check a dependency, model, API, SaaS service, generated file, or vendor before it backs your evidence, permissions, data, release, or public claims. This is a portable command prompt.

## Use when

- A change adds or updates an outside package, model, API, SaaS tool, build service, generated file, or data source.
- You are leaning on a vendor's or a source's claims as evidence.
- Credentials, network access, data handling, the release, or public trust may change.

## Do not use when

- The dependency is for development only, is easy to undo, and a Quick proof already covers it.
- A qualified security, legal, procurement, or regulated-use review must happen outside this repo.

## Inputs

- The outside item's name, its version/model/API surface, the provider, how you intend to use it, the claims you are relying on, the local evidence, the gaps, the controls, and the re-check trigger.

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

Keep the outside claims separate from your local evidence. Return a decision for how you intend to use it, the gaps, the controls that make up for them, the effect on the release, and whether to ship, defer, block, or require a qualified review.
```

## Files created or modified

- `supplier-trust.md`, or a trust section in `basis.md`, `verification.md`, `ship.md`, or `decision.md`.

## Expected outputs

- A decision for how you intend to use it, a table of evidence and gaps, the controls that make up for the gaps, the owner, and the re-check trigger.
- The effect on the release.

## Verification command

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

## Failure modes

- Treating vendor wording as local proof.
- Leaving the version, model, provider, or API surface unnamed.
- Tests pass while the evidence on advisories, license, permissions, or behavior is missing.

## Legal/assurance boundary note

Trust checks support a review of how you intend to use something. They do not create formal supplier qualification, security assurance, procurement adequacy, compliance, certification, safety, security, or regulatory approval.
