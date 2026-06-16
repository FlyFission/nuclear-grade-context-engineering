---
name: checking-legal-and-safety-wording
description: Reviews public text for license, warranty, compliance, safety, security, certification, and fitness claims that go too far, then rewrites them to stay inside the real limits. Use when shipping or editing public docs, READMEs, or rollout copy. Do not use for internal code comments, or for deciding actual legal fitness, which needs a qualified lawyer.
---

# Checking Legal and Safety Wording

## Overview

This skill keeps two things apart: what the MIT license lets people do, and what the repo proves. People may use the repo. But using it does not create formal verification and validation, compliance, certification, safety, security, or fitness for regulated use.

## Decision contract

- **Claim checked:** public text stays inside the assurance boundary -- "you may use it" kept apart from "it is proven fit", banned claim phrases only in negative or disclaimer sentences, and `python tools/ng.py doctor .` passes.
- **Artifact observed:** the changed public text against `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, and `compliance-boundaries.md` -> bounded wording, updated docs/templates, and the scan results or list of gaps.
- **Decision affected:** block -- whether public text stays inside the assurance boundary; an overreaching license/safety/compliance claim blocks until reworded.
- **Failure class:** assurance-overreach (public copy promising safe, secure, compliant, approved, or certified results the repo has not proven).
- **Next action:** reword to evidence-tied wording before release; requests for legal advice or regulated-use approval escalate to a qualified professional.

## When to Use

- You are editing the README, install docs, public docs, templates, skills, commands, examples, or release notes.
- You are adding source families, assurance-sounding wording, or enterprise rollout wording.
- You are getting the repo ready to be public.
- A public claim needs a self-check before release, or a line that points hard claims to a qualified outside review.

## When Not to Use

- The work is a private detail with no public-use wording.
- The user needs legal advice; point them to a qualified lawyer.

## Inputs

- The changed public text.
- `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, and `docs/00-standards-foundation/compliance-boundaries.md`.
- The checker's starting list of banned claim phrases.

## Process

1. Confirm the license wording is still MIT.
2. Keep "you may use it" separate from "it is proven fit."
3. Self-check the exact claim against the evidence you have and against a qualified authority.
4. Add clear "this does not create..." wording near onboarding, templates, commands, and command-line help.
5. Swap broad assurance words for wording tied to evidence anyone can review.
6. Scan the public text for banned phrases and for leftover internal text.

## Outputs

- Wording that stays inside the limits.
- Updated docs or templates.
- Scan results, or a list of the gaps you found.

## Verification

- Public text says the repo does not create formal assurance, compliance, certification, safety, security, or fitness for regulated use.
- Banned phrases appear only in negative or disclaimer sentences.
- `python tools/ng.py doctor .` passes.

## Escalation

- Stop when asked to give legal advice, approve regulated use, confirm purchasing fitness, or promise customer assurance beyond the repo.
- Escalate to qualified legal, compliance, security, or safety professionals for project-specific claims.

## Common Rationalizations

- "MIT means people can use it for anything." MIT grants permission and disclaims warranty; it does not prove the work is fit.
- "Disclaimers in one file are enough." The boundary wording has to appear where users form their expectations.
- "Enterprise-grade means certified." Here it means testable, easy to navigate, and reviewable.

## Red Flags

- Public copy promises safe, secure, compliant, approved, or certified results.
- The command-line or command help has no boundary wording.
- Examples imply more proof than they actually show.

## Prompt

```text
Run a Nuclear-grade license and assurance-limit check.

Inputs:
- changed public text: <paste/link>
- license/disclaimer files: <links>
- target audience: <user/team/enterprise>
- public trust claims to self-check: <list>

Return:
- whether the MIT license permission stays clear
- wording that keeps the permission to use separate from any assurance claim
- whether each public trust claim is supported, narrowed, or removed
- the unsafe phrases and what to replace them with
- the scan commands to run
- the final limits note
```

## Source-lineage note

This skill is an original public-use boundary workflow informed by the repo license, disclaimer, and source-foundation docs. It is not legal advice.
