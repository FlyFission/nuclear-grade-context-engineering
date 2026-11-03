"""Path globs shared by the consequence policy and the PreToolUse gate.

``glob_regex`` is a copy of ``hooks/pre_tool_use.py:_glob_regex``: the hook may not
import this package (it stays stdlib-only and self-contained), so the two copies are
pinned together by ``tests/test_globmatch.py``.

Semantics: ``**`` matches across directories, ``*`` stays inside one directory, ``?``
matches one non-slash character, and matching ignores case. ``**`` compiles to ``.*``,
so ``docs/**.md`` matches ``docs/x.md`` but ``docs/**/*.md`` does not.
"""

from __future__ import annotations

import re


def glob_regex(glob: str) -> re.Pattern[str]:
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


def match_any(path: str, globs: list[str] | tuple[str, ...]) -> list[str]:
    """Return the globs that match ``path`` (a repo-relative, slash-separated path)."""

    return [glob for glob in globs if glob_regex(glob).match(path)]
