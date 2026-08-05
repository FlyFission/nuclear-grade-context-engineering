#!/usr/bin/env python3
"""Prove every committed grade corresponds to the committed transcript it graded.

Why this exists
---------------
Grading rows carry `_source_sha256` precisely so a verdict can be tied to the
exact response text it was computed from. That guarantee was silently broken:
transcripts were later edited to scrub absolute sandbox paths, which changed
their text without re-grading them. Seven rows in the negative pool ended up
pointing at text that no longer exists in the repository, so the authoritative
dataset could not be reproduced from the committed files.

Worse, the first check for this looked at ONE pool's file, found it clean, and
reported the whole dataset as clean. This script exists so that check is
exhaustive, mechanical, and cannot be satisfied by sampling.

Exit codes: 0 all rows verified, 1 at least one broken row (details on stdout).
Run it before publishing any number, and after ANY edit to a transcript.
"""

from __future__ import annotations

import hashlib
import importlib
import json
import os
from pathlib import Path

LADDER_DIR = Path(__file__).resolve().parent.parent

# (graded artifact, pool it belongs to). Every file that carries `_source_sha256`
# rows must be listed; an unlisted artifact is an unverified artifact.
ARTIFACTS = [
    ("data/graded.json", "v1"),
    ("data/rubric-graded-v1.json", "v1"),
    ("data/hard-pool/graded.json", "hard"),
    ("data/rubric-graded-hard.json", "hard"),
    ("data/rubric-graded-hard-retest.json", "hard"),
    ("data/rubric-graded-hard-claude-sonnet-5.json", "hard"),
    ("data/negative-pool/graded.json", "negative"),
    ("data/rubric-graded-negative.json", "negative"),
    ("data/v1-contemporaneous/graded.json", "v1c"),
    ("data/rubric-graded-v1c.json", "v1c"),
]


def check(rel: str, pool: str) -> tuple[int, int, list[str]]:
    path = LADDER_DIR / rel
    if not path.exists():
        return 0, 0, []
    os.environ["NG_LADDER_POOL"] = pool
    import ladder_common
    importlib.reload(ladder_common)

    try:
        rows = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as e:
        return 0, 1, [f"{rel}: unreadable ({e})"]
    if not isinstance(rows, list) or not rows or "skill" not in rows[0]:
        return 0, 0, []

    broken = []
    for r in rows:
        run = ladder_common.run_path(r["skill"], r["arm"], r["trial"])
        if not run.exists():
            broken.append(f"{rel}: {r['skill']}/{r['arm']}/t{r['trial']} transcript MISSING")
            continue
        text = ladder_common.response_text(json.loads(run.read_text()))
        actual = hashlib.sha256(text.encode()).hexdigest()
        recorded = r.get("_source_sha256")
        if recorded is None:
            broken.append(f"{rel}: {r['skill']}/{r['arm']}/t{r['trial']} has no _source_sha256")
        elif actual != recorded:
            broken.append(
                f"{rel}: {r['skill']}/{r['arm']}/t{r['trial']} HASH MISMATCH "
                f"(recorded {recorded[:12]}, transcript now {actual[:12]})"
            )
    return len(rows), len(broken), broken


def main() -> int:
    total = total_broken = 0
    all_broken: list[str] = []
    for rel, pool in ARTIFACTS:
        n, nb, broken = check(rel, pool)
        if n:
            status = "OK" if nb == 0 else f"{nb} BROKEN"
            print(f"{rel:48} pool={pool:9} rows={n:4}  {status}")
        total += n
        total_broken += nb
        all_broken.extend(broken)

    print(f"\n{total} grading rows checked, {total_broken} broken")
    if all_broken:
        print("\nBroken lineage — these grades do NOT correspond to the committed "
              "transcripts, so the dataset is not reproducible from this branch:")
        for line in all_broken:
            print(f"  {line}")
        print("\nFix: re-grade the affected cells (the grader re-runs any row whose "
              "source hash no longer matches), then re-run every downstream report.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
