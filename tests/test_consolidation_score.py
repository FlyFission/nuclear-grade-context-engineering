"""The consolidation scores must be reproducible from the committed inputs.

`evals/skill-consolidation/REPORT.md` justifies a catalog change with these
numbers, so the published command has to run and give the committed result.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "evals" / "skill-consolidation"


def test_published_score_command_reproduces_committed_scores():
    result = subprocess.run(
        [sys.executable, str(EVAL / "score.py"), str(EVAL / "data")],
        capture_output=True, text=True, check=True, cwd=ROOT,
    )
    produced = json.loads(result.stdout)
    committed = json.loads((EVAL / "data" / "score.json").read_text(encoding="utf-8"))
    assert produced["routing"] == committed["routing"]
    assert produced["labeler_agreement"] == committed["labeler_agreement"]
    assert json.dumps(produced["fit"], sort_keys=True) == json.dumps(committed["fit"], sort_keys=True)
