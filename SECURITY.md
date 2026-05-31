# Security Policy

Nuclear-grade includes security-related examples and a checker tool. It is not a production security product, a compliance framework, a certification package, or a formal QA program.

## Supported scope

Security reports help when they are about:

- a checker that misses obvious banned overclaiming or an unsafe packet structure;
- example code that breaks its own stated limits;
- docs that could make users trust an educational tool more than they should;
- secrets, credentials, private data, or proprietary source material left in by accident.

## Out of scope

The `ai-agent-tool-permissions` example is educational. It does not claim to be a production sandbox. It does not yet cover time-of-check/time-of-use races (TOCTOU), access-control lists (ACLs), hard links, mount boundaries, containers, hostile multi-user filesystems, Windows-specific behavior, or lasting audit logs.

If a report assumes production-grade security beyond the documented scope, we may close it as a docs clarification rather than a vulnerability.

## Reporting

To report a sensitive issue, use GitHub's private vulnerability reporting for this repository when it is available. If it is not, open a short issue that leaves out exploit details and asks for a private way to make contact.

For issues that are not sensitive, open a normal GitHub issue with:

- the affected file or path;
- the expected behavior;
- the observed behavior;
- why it could mislead users or weaken the evidence;
- a suggested fix, if you have one.

## Agent operating posture

For the trust assumptions of an AI agent operating this workflow — packet content is untrusted input, and the validator is not a security boundary — see [`docs/02-operating-system/agent-threat-model.md`](docs/02-operating-system/agent-threat-model.md).

## Disclosure posture

We prefer precise, narrow wording over broad claims. If a report finds overclaiming, the likely fix is to tighten the wording, add evidence, or mark the item as a gap or a deferred claim.
