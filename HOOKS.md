# Hooks (advisory, opt-in)

Nuclear-grade ships two **advisory** session hooks that make the dispatcher always-on. They are
**opt-in**: this repo ships **no** `hooks/hooks.json`, so installing the plugin does **not**
auto-activate them. The no-hooks install stays the default — a deliberate security posture (the
in-session hooks are rungs 1–3 and defeatable; the real gate is the out-of-band CI from
`ng scaffold-ci`). Enable them yourself when you want the always-on routing.

## What they do

| Hook | Event | Reads | Returns | Effect |
|---|---|---|---|---|
| `hooks/session_start.py` | SessionStart | stdin session metadata (drained, unused) | a static routing preamble as `additionalContext` | injects the classify-first rule + two-speed + the cluster map at session start |
| `hooks/user_prompt_submit.py` | UserPromptSubmit | stdin (the prompt is drained, **never echoed**) | one static classification line as `additionalContext` | reminds the agent to state the mode before acting |

## Security properties (enforced by `tests/test_hooks.py`)

- **Pure standard library, zero network** — the scripts import only `json` and `sys`. A test
  AST-parses each hook and fails the build if anything beyond `json`/`sys` is imported (a
  banned-substring scan also rejects `socket`, `urllib`, `requests`, `http`, `subprocess`, etc.).
- **Static output** — the injected text is a fixed constant. The UserPromptSubmit hook never
  reflects the user's prompt (a seeded prompt is asserted absent from the output), so it cannot be
  used to launder injected instructions.
- **No file reads, no side effects** — the hooks read stdin and print JSON; a test fails the build if
  a hook calls `open`, `exec`, `eval`, or `compile`. The matcher includes `clear` and `compact` so the
  preamble is re-injected after `/clear` or context compaction, not only at startup/resume.
- **Advisory only (rung 1)** — these hooks inject *text*; they do not block anything. The blocking
  `PreToolUse` gate is a separate, deliberately-deferred tier (it must decide on structured facts
  only, fail closed, and never auto-allow).

## Enable them

Copy the two scripts into your repo (for example `.claude/hooks/`) and register them in
`.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "startup|resume|clear|compact", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/session_start.py"] } ] }
    ],
    "UserPromptSubmit": [
      { "matcher": "*", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/user_prompt_submit.py"] } ] }
    ]
  }
}
```

The commands use **exec form** (`command` + `args`) so a project path containing spaces or shell
metacharacters is passed as a single argument and the hook starts correctly.

The preamble mirrors the decision matrix in [`CORE.md`](CORE.md); a test asserts the cluster names
stay in sync.

## Honesty

This guidance is advisory — an agent can ignore it. It is **not** enforcement and **not** a
compliance claim. Trust-bearing work still needs the out-of-band CI gate (`ng scaffold-ci`) and
human review.
