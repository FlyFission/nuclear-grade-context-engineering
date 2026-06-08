#!/usr/bin/env python3
"""Nuclear-grade UserPromptSubmit hook (advisory, opt-in).

Appends ONE static line reminding the agent to classify the change before
acting. Pure standard library, zero network. The injected text is a fixed
constant: the user's prompt is read from stdin only to drain it and is never
reflected back, so this hook cannot be used to launder injected instructions.
Advisory only -- it injects a reminder and cannot block anything. See HOOKS.md.
"""

import json
import sys

CLASSIFY_LINE = (
    "Nuclear-grade reminder: before acting, state the mode (Quick or Standard+) "
    "and the one fact that sets it. Treat authentication, data or migrations, "
    "dependencies, model ids, CI or .github/, releases, or public wording as "
    "Standard+ -- size is not stakes."
)


def main() -> int:
    try:
        json.load(sys.stdin)  # drain stdin; the prompt is intentionally not used
    except (json.JSONDecodeError, ValueError):
        pass
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": CLASSIFY_LINE,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
