# ng-legal-check

## Purpose

Review the license, warranty, public-use, and assurance-limit wording before a release. This is a portable command prompt.

## Use when

- Public docs, templates, skills, commands, examples, or release notes change.
- You add wording about enterprise adoption or where the ideas come from.
- The repo is getting ready to go public.
- A public trust claim needs a self-check before release.

## Do not use when

- The user needs legal advice.
- The change has no public-use or assurance wording.

## Inputs

- The public text you changed.
- `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, and the compliance-boundary docs.
- The output of the banned-phrase scan.

## Prompt text

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

## Files created or modified

- Public docs, templates, skills, commands, or packet files.
- `DISCLAIMER.md`, `SECURITY.md`, or support docs, only when needed.

## Expected outputs

- Wording that stays inside the limits.
- Plain "no assurance" wording wherever users could form expectations.
- The scan results.

## Verification command

```bash
rg -n "formal|certified|approval|commercial-grade|NQA-1" README.md INSTALL.md QUICKSTART.md WORKFLOWS.md COMMANDS.md SKILLS.md EXAMPLES.md ROADMAP.md SUPPORT.md GOVERNANCE.md AGENTS.md docs skills commands templates tools tests
python tools/ng.py doctor .
```

## Failure modes

- Treating the MIT permission as fitness for use.
- Hiding the limits wording in only one file.
- Making "enterprise-grade" sound certified.

## Legal/assurance boundary note

This check is not legal advice. It helps keep the public-use limits clear and avoids implying formal V&V, compliance, certification, safety, security, or regulatory adequacy.
