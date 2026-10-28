# Hooks (opt-in)

Nuclear-grade ships two **advisory** session hooks that make the dispatcher always-on, and one
**blocking** `PreToolUse` gate. All three are **opt-in**. The main `nuclear-grade` plugin ships
**no** `hooks/hooks.json`, so installing it does **not** turn any of them on. The no-hooks install
stays the default. That is a deliberate security posture: the in-session hooks are rungs 1 to 3
and can be defeated, and the real gate is the out-of-band CI from `ng scaffold-ci`.

Turn them on yourself when you want them. The gate takes one plugin install or one
`init --hook` ([Turn on the gate](#turn-on-the-gate)). The two session hooks are set up by hand
([Enable them by hand](#enable-them-by-hand)).

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
| `deny` | `Write`/`Edit`/`MultiEdit`/`NotebookEdit` to `.github/workflows/**`, `.claude/settings*.json`, `.claude/hooks/**`, `hooks/**`, `.nuclear/charter.md`, `.nuclear/gate-policy.json`, `~/.claude/settings*.json`, `~/.claude/hooks/**`, or `~/.claude/plugins/**` (where a plugin install keeps its copy of the gate). Paths are normalized, symlink-resolved, and case-folded. |
| `ask` | `Bash` or `PowerShell`: force push (`--force`, `-f`, `--force-with-lease`, `+ref`); `git push --tags/--follow-tags/--mirror/--delete`, or a push of `refs/tags/...` or a version-shaped tag (`v1.2.3`); `git tag`; `gh release`; `twine upload`; `npm`/`pnpm`/`yarn`/`uv`/`poetry`/`cargo publish`; `rm -rf` (or PowerShell `Remove-Item -Recurse -Force` and its aliases) on an absolute (including `C:\`), `~`, `$VAR`, `..`, `.` or `*` target; `curl`/`wget` piped to a shell; `claude plugin disable`, `uninstall`, or `remove`, and `claude plugin marketplace remove`, since any of them can switch off a gate that came from a plugin; any command naming a protected path (including `.claude/plugins`). Built-in command rules ignore case, because Windows command names do; your policy-file regexes match exactly as written. |

**Fail closed when the hook itself cannot run.** Every way of turning on the gate below sets `"onFailure": "block"` (Claude Code v2.1.295 or later). Without it, a missing `python3`, a crash, a timeout, or invalid output lets the tool call proceed, because the host's default is `continue`. On older versions, that failure mode stays open. Each also sets `"timeout": 10`, so a stuck gate blocks the call after 10 seconds and does not hold the session for the 600 second default.

**Policy file.** `.nuclear/gate-policy.json` may add rules: `deny_paths` and `ask_paths` (globs),
`deny_commands` and `ask_commands` (regexes). No key removes a default. The gate also denies agent
writes to the policy file, so the agent cannot drop rules you added.

## Turn on the gate

Pick one of these. Each registers the same `PreToolUse` entry, and you can run both, though the
gate then runs twice per call.

**Claude Code plugin, for you on every project.** The marketplace that ships the skills also lists
a second, separate plugin, `nuclear-grade-guard`. Its only job is to register the gate:

```bash
/plugin marketplace add FlyFission/nuclear-grade-context-engineering   # once, if not added yet
/plugin install nuclear-grade-guard@nuclear-grade
/reload-plugins   # or restart Claude Code
```

It adds no skills, commands, or agents. It needs `python3` on your `PATH`, and with
`onFailure: block` a missing `python3` blocks every matched call until you fix it or remove the
plugin. On Windows, a python.org install may give you only `python` or `py`, so check that
`python3 --version` works in a terminal first. To turn it off, run `/plugin disable nuclear-grade-guard@nuclear-grade`, or remove it with
`/plugin uninstall nuclear-grade-guard@nuclear-grade`. If an agent tries either step from the
shell (`claude plugin disable` or `uninstall`), the gate asks you first.

**Project settings, for everyone on one repo.** `nuclear-grade init --hook` (or
`python tools/ng.py init <repo> --hook` from a checkout) copies the gate to
`.claude/hooks/pre_tool_use.py` and adds the `PreToolUse` entry shown in the next section to
`.claude/settings.json`, keeping every
other setting and hook in that file. Commit both files and the gate goes with the repo. To remove
it, delete that entry and the script. Add `--dry-run` first to see what would change.

## Enable them by hand

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
      { "matcher": "Write|Edit|MultiEdit|NotebookEdit|Bash|PowerShell", "hooks": [ { "type": "command", "command": "python3", "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/pre_tool_use.py"], "timeout": 10, "onFailure": "block" } ] }
    ]
  }
}
```

The commands use **exec form** (`command` + `args`) so a project path containing spaces or shell
metacharacters is passed as a single argument and the hook starts correctly.

The preamble mirrors the decision matrix in [`CORE.md`](CORE.md); a test asserts the cluster names
stay in sync.

## Why not just use permission deny rules?

Claude Code's own permission rules are a good first layer, and for some teams they are enough.
They are checked by Claude Code itself, deny rules hold in every permission mode (including
`bypassPermissions`), and the gate never weakens them: Claude Code still applies your deny and ask
rules whatever a hook answers. They also already do several things well:

- They split compound commands, so an ask rule still fires inside `cd x && git push --force`.
- A deny rule on a path also blocks a symlink that points to it.
- `Edit` deny rules also cover shell output redirects (`>`) and `tee`.
- Claude Code treats writes under `.claude/` and `.git/` as protected paths and asks before them
  in the default mode.

If that covers your risk, this lighter option in `.claude/settings.json` covers the most common
spellings of what the gate guards, with no script to run:

```json
{
  "permissions": {
    "deny": [
      "Edit(/.github/workflows/**)",
      "Edit(/.claude/settings*.json)",
      "Edit(/.claude/hooks/**)",
      "Edit(/hooks/**)",
      "Edit(/.nuclear/charter.md)",
      "Edit(~/.claude/settings*.json)",
      "Edit(~/.claude/hooks/**)",
      "Edit(~/.claude/plugins/**)"
    ],
    "ask": [
      "Bash(git push *--force*)",
      "Bash(git push -f*)",
      "Bash(git push * -f*)",
      "Bash(git push *--tags*)",
      "Bash(git tag *)",
      "Bash(gh release *)",
      "Bash(npm publish *)",
      "Bash(twine upload *)",
      "Bash(cargo publish *)"
    ]
  }
}
```

What the gate adds on top, each of it checked by `tests/test_pre_tool_use_hook.py`:

- **It reads the whole command.** A Bash rule matches the words it starts with, and Claude Code's
  own docs note that `Bash(git push *)` misses `git -C . push` and `git 'push'`. The gate skips
  git's global options, joins quoted words, drops `.exe` and other Windows suffixes, and ignores
  case, so those spellings still ask.
- **It looks at flags and targets.** It asks on a force flag anywhere in a push (`--force`, `-f`,
  `--force-with-lease`, `+branch`), on a push of a version-shaped tag (`git push origin v1.2.3`), on
  npm's short spellings of publish (`npm pub`), and on `rm -rf` when the target is outside the
  working folder or is the whole folder (`.` or `*`), so cleaning `build/` does not prompt.
- **It asks when any shell command names a protected path**, for example
  `sed -i ... .github/workflows/ci.yml` or `cp x .claude/settings.json`. Claude Code documents its
  `Edit` rules for shell redirects and `tee`; the gate's text check adds other programs, though it
  is still only a text check.
- **It fails closed and never says allow.** Bad input, a broken policy file, or an internal error
  gives `ask`, and with `onFailure: block` a crash or timeout blocks the call. It has no `allow`
  answer, so it can only add prompts and blocks.
- **It protects its own off switches.** It denies edits to the settings, hook, and plugin files
  that run it, and asks before `claude plugin disable` or `uninstall`.
- **Each repo can add its own rules** in `.nuclear/gate-policy.json`, and the gate blocks the
  agent's file tools from editing that file.

It reads Claude Code's `PreToolUse` input and Claude Code's tool names, so it is built for Claude
Code. We have not tested it in other hosts.

## Honesty

The session hooks are advisory — an agent can ignore them. The gate is stronger but still
in-session (rung 2/3), not a sandbox. Matching a shell string is defeatable: aliases, variables,
`eval`, encoded commands, a script that does the write, or an MCP tool the matcher does not name all
get past it. Whoever controls the host settings can turn it off. None of this is a compliance claim.
Trust-bearing work still needs the out-of-band CI gate (`ng scaffold-ci`) and human review.
