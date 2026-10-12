# Hooks (opt-in)

Nuclear-grade ships two **advisory** session hooks that make the dispatcher always-on, and one
**blocking** `PreToolUse` gate. All three are **opt-in**: this repo ships **no** `hooks/hooks.json`,
so installing the plugin does **not** auto-activate them. The no-hooks install stays the default — a deliberate security posture (the
in-session hooks are rungs 1–3 and defeatable; the real gate is the out-of-band CI from
`ng scaffold-ci`). Enable them yourself when you want them.

## What they do

| Hook | Event | Reads | Returns | Effect |
|---|---|---|---|---|
| `hooks/session_start.py` | SessionStart | stdin session metadata (drained, unused) | a static routing preamble as `additionalContext` | injects the classify-first rule + two-speed + the cluster map at session start |
| `hooks/user_prompt_submit.py` | UserPromptSubmit | stdin (the prompt is drained, **never echoed**) | one static classification line as `additionalContext` | reminds the agent to state the mode before acting |
| `hooks/pre_tool_use.py` | PreToolUse | `tool_name`, `tool_input` path or command, `cwd` | `deny` or `ask`, or **nothing** | blocks writes to trust surfaces; routes irreversible commands to a human |

## Session-hook security properties (enforced by `tests/test_hooks.py`)

- **Pure standard library, zero network** — the two session hooks import only `json` and `sys`. A test
  AST-parses each hook and fails the build if anything beyond `json`/`sys` is imported (a
  banned-substring scan also rejects `socket`, `urllib`, `requests`, `http`, `subprocess`, etc.).
- **Static output** — the injected text is a fixed constant. The UserPromptSubmit hook never
  reflects the user's prompt (a seeded prompt is asserted absent from the output), so it cannot be
  used to launder injected instructions.
- **No file reads, no side effects** — the hooks read stdin and print JSON; a test fails the build if
  a hook calls `open`, `exec`, `eval`, or `compile`. The matcher includes `clear` and `compact` so the
  preamble is re-injected after `/clear` or context compaction, not only at startup/resume.
- **Advisory (rung 1)** — the two session hooks inject *text*; they block nothing. Blocking is the
  separate `PreToolUse` gate below, held to its own tests in `tests/test_pre_tool_use_hook.py`.

## The PreToolUse gate

It decides on structured facts only, fails closed, and never auto-allows:

- **Structured facts only.** It reads the tool name, the `file_path`/`notebook_path`, and the
  `command` string. It never reads model prose (descriptions, plans, transcripts).
- **Never `allow`.** It emits `deny` or `ask`; when nothing matches it prints nothing, so the
  host's normal permission flow applies. A test sweeps many inputs and finds no `allow`.
- **Fails closed.** Malformed input, a missing path, an invalid policy file, or an internal error
  returns `ask`.
- **Stdlib, read-only.** It imports only `json`, `os`, `re`, `sys`, runs nothing, and opens one
  file read-only. An AST test enforces this.

Default policy (constants in the script):

| Decision | Matches |
|---|---|
| `deny` | `Write`/`Edit`/`MultiEdit`/`NotebookEdit` to `.github/workflows/**`, `.claude/settings*.json`, `.claude/hooks/**`, `hooks/**`, `.nuclear/charter.md`, `.nuclear/gate-policy.json`, `~/.claude/settings*.json`, or `~/.claude/hooks/**`. Paths are normalized, symlink-resolved, and case-folded. |
| `ask` | `Bash`: force push (`--force`, `-f`, `--force-with-lease`, `+ref`); `git push --tags/--mirror/--delete`; `git tag`; `gh release`; `twine upload`; `npm`/`pnpm`/`yarn`/`uv`/`poetry`/`cargo publish`; `rm -rf` on an absolute, `~`, `$VAR`, `..`, `.` or `*` target; `curl`/`wget` piped to a shell; any command naming a protected path. |

**Policy file.** `.nuclear/gate-policy.json` may add rules: `deny_paths` and `ask_paths` (globs),
`deny_commands` and `ask_commands` (regexes). No key removes a default. The gate also denies agent
writes to the policy file, so the agent cannot drop rules you added.

## Enable them

Copy the scripts you want into your repo (for example `.claude/hooks/`) and register them in
`.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "startup|resume|clear|compact", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/session_start.py"] } ] }
    ],
    "UserPromptSubmit": [
      { "matcher": "*", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/user_prompt_submit.py"] } ] }
    ],
    "PreToolUse": [
      { "matcher": "Write|Edit|MultiEdit|NotebookEdit|Bash", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/pre_tool_use.py"] } ] }
    ]
  }
}
```

The commands use **exec form** (`command` + `args`) so a project path containing spaces or shell
metacharacters is passed as a single argument and the hook starts correctly.

The preamble mirrors the decision matrix in [`CORE.md`](CORE.md); a test asserts the cluster names
stay in sync.

## Honesty

The session hooks are advisory — an agent can ignore them. The gate is stronger but still
in-session (rung 2/3), not a sandbox. Matching a shell string is defeatable: aliases, variables,
`eval`, encoded commands, a script that does the write, or an MCP tool the matcher does not name all
get past it. Whoever controls the host settings can turn it off. None of this is a compliance claim.
Trust-bearing work still needs the out-of-band CI gate (`ng scaffold-ci`) and human review.
