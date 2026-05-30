# Security Policy

Nuclear-grade includes security-adjacent examples and validator tooling, but it is not a production security product, compliance framework, certification package, or formal QA program.

## Supported scope

Security reports are useful when they concern:

- validator behavior that misses obvious prohibited overclaiming or unsafe packet structure;
- example code that contradicts its stated boundaries;
- documentation that could cause users to overtrust an educational artifact;
- accidental inclusion of secrets, credentials, private data, or proprietary source material.

## Out of scope

The `ai-agent-tool-permissions` reference implementation is educational. It does not claim to be a production sandbox and does not currently cover TOCTOU, ACLs, hard links, mount boundaries, containers, hostile multi-user filesystems, Windows-specific semantics, or durable audit logging.

Reports that assume production security guarantees beyond the documented scope may be closed as documentation clarifications rather than vulnerabilities.

## Reporting

To report a sensitive issue, use GitHub's private vulnerability reporting for this repository when available. If that is not available, open a minimal issue that avoids exploit details and asks for a private contact path.

For non-sensitive issues, open a normal GitHub issue with:

- affected file/path;
- expected behavior;
- observed behavior;
- why the issue could mislead users or weaken evidence;
- suggested fix, if known.

## Agent operating posture

For the trust assumptions of an AI agent operating this workflow — packet content is untrusted input, and the validator is not a security boundary — see [`docs/02-operating-system/agent-threat-model.md`](docs/02-operating-system/agent-threat-model.md).

## Disclosure posture

We prefer precise, scoped language over broad claims. If a report identifies overclaiming, the likely fix is to narrow language, add evidence, or mark the item as a gap/deferred claim.
