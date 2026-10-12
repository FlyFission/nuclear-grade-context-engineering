"""Evidence badge: a shields.io endpoint summary of a repository's change records.

`ng badge [repo] [--out .nuclear/badge.json]` writes JSON that shields.io renders:

    https://img.shields.io/endpoint?url=<raw URL of .nuclear/badge.json>

The message counts records and open evidence items; it never says "certified",
"compliant", or "passing". Open items are the declared fail/gap/deferred/planned
statuses, so a repo that discloses its gaps shows them instead of hiding them.
Generate it in CI: a badge the change actor writes and commits by hand is
self-reported evidence.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from nuclear_grade.receipt import OPEN_STATUSES, _effective_mode, _status_counts

LABEL = "evidence records"


def summarize(repo: Path, health_of: Callable[[Path], str]) -> dict[str, int]:
    changes = repo / ".nuclear" / "changes"
    summary = {"records": 0, "closed": 0, "attention": 0, "open_items": 0}
    if not changes.is_dir():
        return summary
    for packet in sorted(path for path in changes.iterdir() if path.is_dir()):
        health = health_of(packet)
        if health == "closed":
            summary["closed"] += 1
            continue
        summary["records"] += 1
        if health != "ok":
            summary["attention"] += 1
            continue
        counts = _status_counts(packet, _effective_mode(packet))
        summary["open_items"] += sum(counts[status] for status in OPEN_STATUSES)
    return summary


def build_badge(summary: dict[str, int]) -> dict[str, Any]:
    records = summary["records"]
    if records == 0:
        message, color = "none yet", "lightgrey"
    elif summary["attention"]:
        message, color = f"{records} · {summary['attention']} need attention", "red"
    elif summary["open_items"]:
        message, color = f"{records} · {summary['open_items']} open items", "yellow"
    else:
        message, color = f"{records} · 0 open items", "brightgreen"
    return {"schemaVersion": 1, "label": LABEL, "message": message, "color": color}
