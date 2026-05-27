---
name: checking-license-and-assurance-boundaries
description: Use when reviewing public text for license, warranty, compliance, assurance, safety, security, certification, or adequacy overclaims.
---

# Checking License and Assurance Boundaries

## Overview

This skill keeps the MIT license permission separate from engineering assurance. People may use the repo, but use does not create formal verification, compliance, certification, safety, security, or regulatory adequacy.

## When to Use

- Updating README, install docs, public docs, templates, skills, commands, examples, or release notes.
- Adding source families, assurance language, or enterprise adoption language.
- Preparing the repo for public visibility.
- A public claim needs a self-check before release or a qualified external review boundary.

## When Not to Use

- The work is a private implementation detail with no public-use wording.
- The user needs legal advice; recommend qualified counsel.

## Inputs

- Changed public text.
- `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, and `docs/00-standards-foundation/compliance-boundaries.md`.
- Validator prohibited-claim seed list.

## Process

1. Confirm license language remains MIT.
2. Separate permission to use from claims about adequacy.
3. Self-check the exact claim against available evidence and qualified authority.
4. Add clear negative boundary language near onboarding, templates, commands, and CLI help.
5. Replace broad assurance words with reviewable evidence wording.
6. Run public scans for prohibited phrases and internal residue.

## Outputs

- Boundary-safe wording.
- Updated docs or templates.
- Scan results or named gaps.

## Verification

- Public text says the repo does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
- Prohibited phrases appear only in negative or disclaimer contexts.
- `python tools/ng.py doctor .` passes.

## Escalation

- Stop when asked to provide legal advice, regulated-use approval, procurement adequacy, or customer assurance beyond the repo.
- Escalate to qualified legal, compliance, security, or safety professionals for project-specific claims.

## Common Rationalizations

- "MIT means people can use it for anything." MIT grants permissions and disclaims warranty; it does not prove fitness.
- "Disclaimers in one file are enough." Boundary language must appear where users form expectations.
- "Enterprise-grade means certified." Here it means testable, navigable, and reviewable.

## Red Flags

- Public copy promises safe, secure, compliant, approved, or certified outcomes.
- CLI or command help lacks boundary language.
- Examples imply broader proof than they demonstrate.

## Source-lineage note

This skill is an original public-use boundary workflow informed by the repo license, disclaimer, and source-foundation docs. It is not legal advice.
