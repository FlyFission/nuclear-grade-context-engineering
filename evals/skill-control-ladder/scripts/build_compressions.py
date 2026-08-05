#!/usr/bin/env python3
"""Generate the C3 arm's compressed skill text, one entry per skill.

C3 asks: how much of a skill's effect survives compressing it to five
imperative bullets? Where C3 matches C4, the remaining prose in that SKILL.md is
carrying token cost without measured behavioral effect -- which is the concrete,
per-skill improvement lever this experiment is meant to produce.

Contamination guard: the compressor is shown ONLY the skill body. It never sees
the scenario or the pass criterion. A compressor that saw the answer key could
hand-pick the one bullet that satisfies the grader, which would make C3 an
upper bound on prompt-engineering-to-the-test rather than a fair measure of what
the skill's own text compresses to.

Output is checked into data/compressed_skills.json and keyed by a hash of the
skill body, so the compression is inspectable, diffable, and only regenerated
when the underlying SKILL.md actually changes.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from ladder_common import (
    COMPRESSIONS_PATH,
    LADDER_DIR,
    MAX_WORKERS,
    TASKS,
    skill_body,
)

COMPRESSOR_MODEL = "claude-sonnet-5"
PROVENANCE_PATH = LADDER_DIR / "data" / "compressed_skills.provenance.json"

INSTRUCTION = (
    "Below is the body of a reusable instruction document ('skill') given to an "
    "AI assistant. Compress it into AT MOST 5 imperative bullet points that "
    "preserve as much of its behavioral effect as possible.\n\n"
    "Rules:\n"
    "- Output ONLY the bullets, one per line, each starting with '- '.\n"
    "- Keep the operative instructions (what to do, what to check, what to "
    "refuse). Drop rationale, background, examples, and formatting scaffolding.\n"
    "- Do not add anything not present in the original.\n"
    "- Stay under 120 words total.\n\n"
    "Document:\n---\n{body}\n---"
)


def compress(skill: str) -> tuple[str, str]:
    body = skill_body(skill)
    cmd = [
        "claude", "-p", INSTRUCTION.format(body=body),
        "--output-format", "json",
        "--model", COMPRESSOR_MODEL,
        "--safe-mode",
        "--tools", "",
        "--no-session-persistence",
        "--max-budget-usd", "0.30",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    record = json.loads(proc.stdout.strip())
    if record.get("is_error"):
        raise RuntimeError(f"{skill}: compressor returned an error record")
    text = (record.get("result") or "").strip()
    if not text:
        raise RuntimeError(f"{skill}: compressor returned empty text")
    return text, hashlib.sha256(body.encode()).hexdigest()


def main() -> int:
    existing = json.loads(COMPRESSIONS_PATH.read_text()) if COMPRESSIONS_PATH.exists() else {}
    provenance = json.loads(PROVENANCE_PATH.read_text()) if PROVENANCE_PATH.exists() else {}

    # Only regenerate where the source skill body has actually changed. Without
    # this, every invocation rewrites all 27 compressions with fresh sampling
    # noise, and the C3 arm would silently stop being comparable across runs.
    todo = [
        s for s in TASKS
        if s not in existing
        or provenance.get(s, {}).get("body_sha256")
        != hashlib.sha256(skill_body(s).encode()).hexdigest()
    ]
    if not todo:
        print("All compressions current.", file=sys.stderr)
        return 0

    print(f"Compressing {len(todo)} skill(s): {', '.join(sorted(todo))}", file=sys.stderr)
    failures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(compress, s): s for s in todo}
        for fut in as_completed(futures):
            skill = futures[fut]
            try:
                text, body_hash = fut.result()
            except Exception as e:  # noqa: BLE001 -- reported, not swallowed
                failures.append(f"{skill}: {type(e).__name__}: {e}")
                continue
            existing[skill] = text
            provenance[skill] = {"body_sha256": body_hash, "compressor_model": COMPRESSOR_MODEL}
            print(f"  ok {skill}", file=sys.stderr)

    COMPRESSIONS_PATH.write_text(json.dumps(dict(sorted(existing.items())), indent=2) + "\n")
    PROVENANCE_PATH.write_text(json.dumps(dict(sorted(provenance.items())), indent=2) + "\n")

    if failures:
        print(f"{len(failures)} compression(s) failed:", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
