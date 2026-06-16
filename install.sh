#!/usr/bin/env sh
# One-command installer for Nuclear-grade skills.
#
# Skills are plain SKILL.md files that each agent tool auto-surfaces by their
# `description`; this script just places them where each tool looks. It wraps
# `python tools/ng.py install` -- run that directly for --scope / --dest.
#
#   ./install.sh                # Core set into every detected tool
#   ./install.sh --full         # all skills into every detected tool
#   ./install.sh codex          # one named tool, Core set
#   ./install.sh codex --full   # one named tool, all skills
set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ng="$here/tools/ng.py"
py=$(command -v python3 || command -v python || true)
if [ -z "$py" ]; then
  echo "error: python3 not found on PATH" >&2
  exit 1
fi

# A named tool? Pass every argument straight through to the CLI.
case "${1:-}" in
  codex | claude | cursor | windsurf | vscode)
    exec "$py" "$ng" install "$@"
    ;;
esac

# Otherwise treat the args (e.g. --full) as profile flags and fan out to every
# detected tool. Windsurf is project-scoped, so it is not auto-detected here.
detected=0
for pair in "codex:$HOME/.codex" "claude:$HOME/.claude" "cursor:$HOME/.cursor"; do
  tool=${pair%%:*}
  dir=${pair#*:}
  if [ -d "$dir" ]; then
    "$py" "$ng" install "$tool" "$@"
    detected=1
  fi
done

if [ "$detected" -eq 0 ]; then
  echo "No supported tool home found (~/.codex, ~/.claude, ~/.cursor)." >&2
  echo "Install one explicitly, e.g.: ./install.sh codex" >&2
  echo "Windsurf is project-scoped: python tools/ng.py install windsurf --scope project --repo ." >&2
  exit 1
fi
