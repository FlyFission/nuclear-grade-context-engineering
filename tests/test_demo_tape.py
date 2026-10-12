"""Replay the README demo tape so the rendered GIF cannot drift from reality.

Every `Type` line in docs/assets/demo/demo.tape runs, in order, in one bash
session from the repository root; the output must still show each beat.
"""

import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TAPE = ROOT / "docs" / "assets" / "demo" / "demo.tape"
EXPECTED = (
    "DENY  Write .github/workflows/ci.yml",
    "ASK  Bash git push --force origin main",
    "FAILED:",
    '"open_evidence_items"',
    '"label": "evidence records"',
)


def tape_commands(text: str) -> list[str]:
    commands = []
    for line in text.splitlines():
        match = re.match(r"^Type\s+(`(.*)`|\"(.*)\"|'(.*)')\s*$", line)
        if match:
            commands.append(next(group for group in match.groups()[1:] if group is not None))
    return commands


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required to replay the tape")
def test_demo_tape_still_shows_every_beat():
    commands = tape_commands(TAPE.read_text(encoding="utf-8"))
    assert len(commands) >= 8
    script = "shopt -s expand_aliases\nclear() { :; }\n" + "\n".join(commands) + "\n"
    result = subprocess.run(["bash", "-c", script], cwd=ROOT, capture_output=True, text=True, timeout=120, check=False)
    output = result.stdout + result.stderr
    for expected in EXPECTED:
        assert expected in output, f"demo beat missing: {expected!r}\n--- output ---\n{output}"


def test_readme_embeds_the_rendered_demo():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    output = re.search(r"^Output\s+(\S+)$", TAPE.read_text(encoding="utf-8"), re.MULTILINE).group(1)
    assert output in readme
    assert (ROOT / output).is_file()
