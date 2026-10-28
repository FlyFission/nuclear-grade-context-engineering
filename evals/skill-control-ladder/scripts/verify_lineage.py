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
import sys
from pathlib import Path

LADDER_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from grade_rubric import rubric_hash  # noqa: E402

_RUBRIC_CACHE: dict[str, dict] = {}


def _rubrics_for(pool: str) -> dict:
    """The rubric file a pool is graded with. v1c shares v1's by design."""
    key = {"v1c": "v1"}.get(pool, pool)
    if key not in _RUBRIC_CACHE:
        path = LADDER_DIR / "data" / f"rubrics-{key}.json"
        _RUBRIC_CACHE[key] = json.loads(path.read_text()) if path.exists() else {}
    return _RUBRIC_CACHE[key]


def _grader_of(row: dict, rel: str) -> str:
    """The grader model a row was scored by. The replicate files encode it in
    their filename; everything else used the default."""
    if "claude-sonnet-5" in rel:
        return "claude-sonnet-5"
    return "claude-haiku-4-5-20251001"

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

        # Rubric lineage, not just transcript lineage.
        #
        # A rubric-graded row records `_rubric_sha256`, the fingerprint of the
        # checks it was scored against. Checking only the transcript hash left a
        # whole class of drift invisible: regenerating a rubric changes the
        # checks without touching any transcript, so the grades would silently
        # describe a rubric no longer in the repository and this validator would
        # still report everything clean. That happened once, from an accidental
        # re-run, and was caught by inspecting a diff rather than by this check.
        rec_rubric = r.get("_rubric_sha256")
        if rec_rubric is not None:
            rubrics = _rubrics_for(pool)
            entry = rubrics.get(r["skill"])
            if entry is None:
                broken.append(f"{rel}: {r['skill']} graded against a rubric that no "
                              f"longer exists")
            else:
                live = rubric_hash(entry["checks"], _grader_of(r, rel))
                if live != rec_rubric:
                    broken.append(
                        f"{rel}: {r['skill']}/{r['arm']}/t{r['trial']} RUBRIC MISMATCH "
                        f"(recorded {rec_rubric[:12]}, rubric now {live[:12]})"
                    )
    return len(rows), len(broken), broken


def check_run_specs() -> tuple[int, list[str]]:
    """Every committed transcript must still match ladder_spec_hash().

    This is the gap that let 27 stale C4 cells ship. The validator checked
    grade-to-response and rubric-to-grade lineage, but never response-to-SPEC:
    when a SKILL.md changed on main, the C4 transcripts generated from the old
    body kept their recorded hash, no grade or rubric moved, and the validator
    reported everything clean while the hard and negative pools partly measured
    superseded skill text. run_ladder refuses to ADOPT a stale transcript, but
    nothing re-checked one already committed.
    """
    broken = []
    checked = 0
    for pool, runs in (("v1", "data/runs"),
                       ("v1c", "data/v1-contemporaneous/runs"),
                       ("hard", "data/hard-pool/runs"),
                       ("negative", "data/negative-pool/runs")):
        base = LADDER_DIR / runs
        if not base.exists():
            continue
        os.environ["NG_LADDER_POOL"] = pool
        import ladder_common
        importlib.reload(ladder_common)
        comp = ladder_common.load_compressions()
        for path in sorted(base.glob("*.json")):
            rec = json.loads(path.read_text())
            skill, arm = rec.get("_skill"), rec.get("_arm")
            if skill not in ladder_common.TASKS or arm is None:
                continue
            try:
                want = ladder_common.ladder_spec_hash(skill, arm, comp)
            except KeyError:
                broken.append(f"{runs}/{path.name}: no compression for {skill}")
                continue
            checked += 1
            if rec.get("_input_spec_sha256") != want:
                broken.append(
                    f"{runs}/{path.name}: SPEC MISMATCH — generated from inputs that "
                    f"no longer match the checked-in SKILL.md/scenario/compression"
                )
    return checked, broken


def report_pins() -> None:
    """Print which skill text each pool was measured against.

    Informational, not a gate. A pool whose pin differs from current HEAD is not
    broken -- it is a result about the text that produced it. The pin makes that
    a stated fact instead of silent drift, and tells a reader when a pool would
    need regenerating to speak about today's skills.
    """
    os.environ["NG_LADDER_POOL"] = "v1"
    import ladder_common
    importlib.reload(ladder_common)
    pins = ladder_common.load_pins()
    head = ladder_common.skills_tree_hash()
    print(f"\nskills/ tree at HEAD: {head or 'unknown (not a git tree)'}")
    if not pins:
        print("  no pins recorded")
        return
    for pool, tree in sorted(pins.items()):
        mark = "matches HEAD" if tree == head else "DIFFERS from HEAD"
        print(f"  {pool:9} measured against {tree[:12]}  ({mark})")


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

    run_checked, run_broken = check_run_specs()
    print(f"\n{run_checked} transcripts checked against ladder_spec_hash, "
          f"{len(run_broken)} stale")
    all_broken.extend(run_broken)
    total_broken += len(run_broken)

    print(f"{total} grading rows checked, {total_broken} broken")
    report_pins()
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
