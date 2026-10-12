"""Demo helper: send one simulated agent tool call through the PreToolUse gate.

    python simulate_tool_call.py Write .github/workflows/ci.yml
    python simulate_tool_call.py Bash "git push --force origin main"

It builds the same JSON a Claude Code PreToolUse hook receives, runs
`hooks/pre_tool_use.py` on it, and prints the decision in one line. It is a
simulation for the README demo; no agent is running.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
COLORS = {"DENY": "\033[1;31m", "ASK": "\033[1;35m"}


def main(argv: list[str]) -> int:
    tool, target = argv[1], argv[2]
    tool_input = {"command": target} if tool == "Bash" else {"file_path": target}
    payload = json.dumps({"tool_name": tool, "tool_input": tool_input, "cwd": str(ROOT)})
    result = subprocess.run(
        [sys.executable, str(ROOT / "hooks" / "pre_tool_use.py")],
        input=payload,
        capture_output=True,
        text=True,
        check=False,
    )
    if not result.stdout.strip():
        print(f"(no objection)  {tool} {target}  -> normal permission flow")
        return 0
    decision = json.loads(result.stdout)["hookSpecificOutput"]
    reason = decision["permissionDecisionReason"].removeprefix("Nuclear-grade gate: ")
    kind = decision["permissionDecision"].upper()
    if sys.stdout.isatty():
        kind = COLORS.get(kind, "") + kind + "\033[0m"
    print(f"{kind}  {tool} {target}\n  {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
