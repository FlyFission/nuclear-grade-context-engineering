# ng-legal-check

## Purpose

Review license, warranty, public-use, and assurance boundary language before release. This is a portable command prompt.

## Use when

- Public docs, templates, skills, commands, examples, or release notes change.
- Enterprise adoption or source lineage language is added.
- The repo is preparing for public visibility.
- A public trust claim needs a self-check before release.

## Do not use when

- The user needs legal advice.
- The change has no public-use or assurance wording.

## Inputs

- Changed public text.
- `LICENSE`, `DISCLAIMER.md`, `SECURITY.md`, and compliance-boundary docs.
- Prohibited phrase scan output.

## Prompt text

```text
Run a Nuclear-grade license and assurance boundary check.

Inputs:
- changed public text: <paste/link>
- license/disclaimer files: <links>
- target audience: <user/team/enterprise>
- public trust claims to self-check: <list>

Return:
- whether MIT use permission remains clear
- wording that separates use permission from assurance claims
- whether each public trust claim is supported, narrowed, or removed
- unsafe phrases and replacements
- scan commands to run
- final boundary note
```

## Files created or modified

- Public docs, templates, skills, commands, or packet files.
- `DISCLAIMER.md`, `SECURITY.md`, or support docs only when necessary.

## Expected outputs

- Boundary-safe wording.
- Explicit no-assurance language where users form expectations.
- Scan results.

## Verification command

```bash
rg -n "formal|certified|approval|commercial-grade|NQA-1" README.md INSTALL.md QUICKSTART.md WORKFLOWS.md COMMANDS.md SKILLS.md EXAMPLES.md ROADMAP.md SUPPORT.md GOVERNANCE.md AGENTS.md docs skills commands templates tools tests
python tools/ng.py doctor .
```

## Failure modes

- Treating MIT permission as fitness for use.
- Hiding boundary language in only one file.
- Making enterprise-grade sound certified.

## Legal/assurance boundary note

This check is not legal advice. It helps preserve public-use boundaries and avoid implying formal V&V, compliance, certification, safety, security, or regulatory adequacy.
