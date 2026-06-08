#!/usr/bin/env python3
"""Nuclear-grade SessionStart hook (advisory, opt-in).

Injects a static routing preamble at session start. Pure standard library,
zero network, static output: it reads stdin only to drain it, never reads
project files, and never echoes any untrusted text. Advisory only (rung 1) --
it injects guidance and cannot block anything. See HOOKS.md.
"""

import json
import sys

PREAMBLE = """\
Nuclear-grade is active. Route every change by consequence.

BEFORE your first action, state the mode and the one fact that sets it. This is a declaration of intent -- you name the mode and act, you do not ask permission.
- Quick: local, reversible, obvious proof, no new trust boundary.
- Standard+ (Standard, or a stronger human-reviewed mode): anything touching authentication, permissions, or secrets; user-visible behavior; data, schema, or a migration; a dependency; a model id, a prompt, or what a tool or agent may do; CI or .github/; a release or saved baseline; or public wording. When unsure, choose Standard.

Two speeds: move fast while the work is throwaway; slow down the moment it becomes a promise -- a claim, a controlled file, public wording, a baseline, a release, or a change to what an agent may do.

Invoke a cluster only when its trigger fires (the default is the Core habits -- question, rate risk, prove claims, double-check cut-points, stay on mission, check release readiness, learn from misses):
- Agent authority: the agent can write, run, use the network, or approve actions in its working set.
- Configuration management: you produce controlled artifacts -- packets, baselines, pinned configs.
- Claims discipline: public claims about safety, security, compliance, licensing, or provenance.
- Incident & deficiency: a production failure, data loss, or agent-caused harm.
- Hygiene: a repo-layout decision, or code-quality drift in a diff.

Do not talk yourself down a tier: "it's a small change" (size is not stakes), "it's only docs" (public wording makes claims), "I'll classify later" (the mode call is the cheapest control -- say it first).

Honesty: this guidance is advisory -- it can be ignored, and it is not enforcement. Trust-bearing work still needs the out-of-band CI gate and human review. "Nuclear-grade" is a standard of care, not a compliance claim.
"""


def main() -> int:
    try:
        json.load(sys.stdin)  # drain stdin; the content is not used
    except (json.JSONDecodeError, ValueError):
        pass
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": PREAMBLE,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
