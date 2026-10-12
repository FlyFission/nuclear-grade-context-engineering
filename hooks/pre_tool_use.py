#!/usr/bin/env python3
"""Nuclear-grade PreToolUse gate (blocking, opt-in).

Decides on structured facts only -- the tool name, a file path, and a shell
command string -- never on model-authored prose. It can DENY or ASK (route to
the human permission prompt); it never emits "allow". When no rule matches it
prints nothing and exits 0, so the host's normal permission flow applies.
Malformed input, an unreadable policy file, or any internal error fails closed
with ASK.

Pure standard library, zero network, no shell-out. It reads stdin and, if
present, `.nuclear/gate-policy.json` (read-only). The policy file can ADD deny
and ask rules; it can never remove the defaults below.

Honesty: pattern-matching a shell string is defeatable (aliases, variables,
encoding, indirection). This is an in-session rung-2/3 control, not a sandbox;
the real gate stays out-of-band CI. See HOOKS.md.
"""

import json
import os
import re
import sys

# Claude Code's PowerShell tool (Windows) carries its command in the same field as Bash.
SHELL_TOOLS = ("Bash", "PowerShell")
WRITE_TOOLS = {"Write": "file_path", "Edit": "file_path", "MultiEdit": "file_path", "NotebookEdit": "notebook_path"}

# The gate's own trust surfaces. Globs are project-root-relative; a leading "~/"
# means the user's home directory. "**" crosses directories, "*" does not.
DENY_PATHS = (
    ".github/workflows/**",
    ".claude/settings*.json",
    ".claude/hooks/**",
    "hooks/**",
    ".nuclear/charter.md",
    ".nuclear/gate-policy.json",  # the policy can only add rules; protect the additions too
    "~/.claude/settings*.json",
    "~/.claude/hooks/**",
)
ASK_PATHS = ()

# Shell commands that are irreversible or release-shaped. Each is a human gate (ASK).
_SEG = r"[^;&|\n]*"  # stay inside one simple command
_GIT = r"\bgit\s+(?:-[cC]\s+\S+\s+|--?\S+\s+)*"  # "git", global options, then the subcommand
ASK_COMMANDS = (
    (_GIT + r"push\b" + _SEG + r"(\s--force(-with-lease)?\b|\s-[a-zA-Z]*f[a-zA-Z]*\b|\s\+\S)",
     "git force push rewrites shared history"),
    # Remote deletion: --delete, -d (alone or bundled), an empty-source ":ref", or --prune.
    (_GIT + r"push\b" + _SEG + r"(\s--(tags|follow-tags|mirror|delete|prune)\b|\s-[a-zA-Z]*d[a-zA-Z]*\b|\s:\S)",
     "git push of tags, a mirror, or a ref deletion"),
    # A single tag push is how a release starts (docs/05-reference/releasing.md). Catch
    # refs/tags/ and version-shaped refspecs; an arbitrary tag name cannot be told from a branch.
    # `tag <name>` is git's explicit form of refs/tags/<name>:refs/tags/<name>.
    (_GIT + r"push\b" + _SEG + r"(\brefs/tags/|\stag\s+[^\s;&|]|\s\+?v?\d+\.\d+(\.\d+)?([-.+][\w.]+)?(:\S*)?(\s|$))",
     "git push of a release tag starts a release"),
    (_GIT + r"tag\b", "git tag creates or moves a release marker"),
    (r"\bgh\s+release\b", "gh release changes a published release"),
    (r"\btwine\s+upload\b", "package publish is irreversible"),
    (r"\b(npm|pnpm|yarn|uv|poetry|cargo)\s+publish\b", "package publish is irreversible"),
    (r"\b(curl|wget)\b[^;&\n]*\|\s*(sudo\s+)?(ba|z|da|k)?sh\b", "piping a download into a shell runs unreviewed code"),
    (r"\b(ba|z)?sh\s+<\(\s*(curl|wget)\b", "running a downloaded script runs unreviewed code"),
)
# A shell command that names a trust surface is a human gate too ("hooks/" is
# left out: it is too common a directory name to match in free text).
# rm and its PowerShell spellings (Remove-Item and aliases).
RM_VERBS = ("rm", "remove-item", "ri", "del", "erase", "rd", "rmdir")
SHELL_TRUST_TOKENS = (".github/workflows", ".claude/settings", ".claude/hooks", ".nuclear/charter.md",
                      ".nuclear/gate-policy.json")

WINDOWS_SUFFIX = re.compile(r"(\w)\.(exe|cmd|bat|com|ps1)\b", re.IGNORECASE)

# The repo-root hooks/ directory as a relative path ("hooks/x", "./hooks/x"), or the gate's
# own file by name from anywhere. A nested "src/hooks/" or "test_hooks.py" is not this surface.
SHELL_HOOKS_PATH = re.compile(r"(?<![\w./-])(\./)?hooks/|\bpre_tool_use\.py\b")

POLICY_FILE = os.path.join(".nuclear", "gate-policy.json")
POLICY_KEYS = ("deny_paths", "ask_paths", "deny_commands", "ask_commands")


def _join_quoted(command):
    """Replace each quoted string with its content as one word (inner spaces become "_")."""
    return re.sub(r'"([^"]*)"|\'([^\']*)\'',
                  lambda m: re.sub(r"\s+", "_", m.group(1) if m.group(1) is not None else m.group(2)), command)


def _ask(reason):
    return _decision("ask", reason)


def _decision(kind, reason):
    return {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": kind,
        "permissionDecisionReason": "Nuclear-grade gate: " + reason,
    }}


def _glob_regex(glob):
    out, i = [], 0
    while i < len(glob):
        if glob.startswith("**", i):
            out.append(".*")
            i += 2
        elif glob[i] == "*":
            out.append("[^/]*")
            i += 1
        elif glob[i] == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(glob[i]))
            i += 1
    return re.compile("^" + "".join(out) + "$", re.IGNORECASE)


def _load_policy(roots):
    """Return (extra rules, error). Only additive keys are read; anything else is ignored."""
    extra = {key: [] for key in POLICY_KEYS}
    for root in roots:
        path = os.path.join(root, POLICY_FILE)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
            if not isinstance(data, dict):
                raise ValueError("policy must be a JSON object")
            for key in POLICY_KEYS:
                values = data.get(key, [])
                if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
                    raise ValueError(key + " must be a list of non-empty strings")
                if key.endswith("_commands"):
                    for value in values:
                        re.compile(value)
                extra[key].extend(values)
        except (OSError, ValueError, re.error) as exc:
            return extra, "gate policy file is unreadable or invalid (" + type(exc).__name__ + ")"
    return extra, None


def _candidates(file_path, roots):
    """Root-relative and home-relative forms of a path, both literal and symlink-resolved."""
    home = os.path.expanduser("~")
    forms = set()
    for root in roots:
        joined = file_path if os.path.isabs(file_path) else os.path.join(root, file_path)
        for absolute in {os.path.normpath(joined), os.path.realpath(joined)}:
            for base, prefix in ((root, ""), (os.path.realpath(root), ""), (home, "~/")):
                rel = os.path.relpath(absolute, base)
                if rel != ".." and not rel.startswith(".." + os.sep):
                    forms.add(prefix + rel.replace(os.sep, "/"))
    return forms


def _match_paths(file_path, roots, globs):
    forms = _candidates(file_path, roots)
    return [g for g in globs if any(_glob_regex(g).match(form) for form in forms)]


def _rm_outside_cwd(command):
    """True when a recursive, forced rm targets something that is not a plain cwd-relative path."""
    for segment in re.split(r"[;&|\n]+", command):
        tokens = segment.split()
        names = [t.replace("\\", "/").rsplit("/", 1)[-1].lower() for t in tokens]
        verb = next((n for n in names if n in RM_VERBS), None)
        if verb is None:
            continue
        args = tokens[names.index(verb) + 1:]
        flags = "".join(a.lstrip("-") for a in args if a.startswith("-") and not a.startswith("--")).lower()
        long_flags = {a.lower() for a in args if a.startswith("--")}
        # Short flags (-rf) and PowerShell switches (-Recurse -Force) both land here.
        recursive = "r" in flags or "--recursive" in long_flags
        forced = "f" in flags or "--force" in long_flags
        if not (recursive and forced):
            continue
        targets = [a for a in args if not a.startswith("-")]
        for target in targets or ["<none>"]:
            stripped = target.strip("'\"").replace("\\", "/")
            if (stripped.startswith(("/", "~", "$", "`")) or re.match(r"[A-Za-z]:/", stripped)
                    or ".." in stripped.split("/")
                    or stripped in (".", "./", "*", "./*", "<none>")):
                return True
    return False


def decide(raw, project_dir=None):
    """Return a PreToolUse decision dict, or None to defer to the normal permission flow."""
    try:
        return _decide(raw, project_dir)
    except Exception as exc:  # fail closed on any internal error
        return _ask("internal error (" + type(exc).__name__ + "); failing closed")


def _decide(raw, project_dir):
    try:
        payload = json.loads(raw)
    except (ValueError, TypeError):
        return _ask("hook input is not valid JSON; failing closed")
    if not isinstance(payload, dict):
        return _ask("hook input is not a JSON object; failing closed")
    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input")
    cwd = payload.get("cwd")
    if not isinstance(tool, str) or not isinstance(tool_input, dict):
        return _ask("hook input lacks tool_name or tool_input; failing closed")
    roots = [r for r in (project_dir, cwd) if isinstance(r, str) and os.path.isabs(r)]
    if not roots:
        return _ask("no absolute project directory or cwd to resolve paths against; failing closed")

    extra, error = _load_policy(list(dict.fromkeys(roots)))
    if error and (tool in WRITE_TOOLS or tool in SHELL_TOOLS):
        return _ask(error + "; failing closed")

    if tool in WRITE_TOOLS:
        file_path = tool_input.get(WRITE_TOOLS[tool])
        if not isinstance(file_path, str) or not file_path:
            return _ask(tool + " input lacks a file path; failing closed")
        hits = _match_paths(file_path, roots, list(DENY_PATHS) + extra["deny_paths"])
        if hits:
            return _decision("deny", tool + " to a protected trust surface (" + hits[0]
                             + ") must go through human review, not the agent")
        hits = _match_paths(file_path, roots, list(ASK_PATHS) + extra["ask_paths"])
        if hits:
            return _ask(tool + " to a gated path (" + hits[0] + ") needs a human decision")
        return None

    if tool in SHELL_TOOLS:
        command = tool_input.get("command")
        if not isinstance(command, str):
            return _ask(tool + " input lacks a command string; failing closed")
        for pattern in extra["deny_commands"]:
            if re.search(pattern, command):
                return _decision("deny", "command matches a policy deny rule")
        # Built-in rules ignore case: Windows command names are case-insensitive (`Git`, `GH`),
        # and `git.exe` or an npm `.cmd` shim is the same command as `git` or `npm`.
        # A quoted word stays one word (`git -C "repo with space" push`), and a quoted program
        # path (`& "C:\\...\\git.exe" push`) is the same program unquoted.
        plain = WINDOWS_SUFFIX.sub(r"\1", _join_quoted(command))
        reasons = [why for pattern, why in ASK_COMMANDS if re.search(pattern, plain, re.IGNORECASE)]
        reasons += ["command matches a policy ask rule" for p in extra["ask_commands"] if re.search(p, command)]
        if _rm_outside_cwd(plain):
            reasons.append("recursive forced rm outside a plain cwd-relative path")
        normalized = command.replace("\\", "/").lower()  # PowerShell paths use backslashes
        project_hooks = [r.replace("\\", "/").rstrip("/").lower() + "/hooks/" for r in roots]
        if (any(token in normalized for token in SHELL_TRUST_TOKENS) or SHELL_HOOKS_PATH.search(normalized)
                or any(hooks in normalized for hooks in project_hooks)):
            reasons.append("shell command names a protected trust surface")
        if reasons:
            return _ask(reasons[0] + "; human gate required")
    return None


def main():
    try:
        raw = sys.stdin.read()
    except (OSError, ValueError):
        raw = ""
    result = decide(raw, os.environ.get("CLAUDE_PROJECT_DIR"))
    if result is not None:
        print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
