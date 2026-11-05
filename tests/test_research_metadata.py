"""Keep research citations useful without redistributing unreviewed abstracts."""

import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "docs/06-publications/research/data"


def test_research_metadata_excludes_copied_abstracts():
    """Re-importing API abstracts must fail the public-release data check."""
    offenders = []

    def inspect(value, location):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"abstract", "summary"}:
                    offenders.append(f"{location}.{key}")
                inspect(child, f"{location}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                inspect(child, f"{location}[{index}]")

    for path in sorted(DATA.glob("*.json")):
        inspect(json.loads(path.read_text(encoding="utf-8")), path.name)

    assert not offenders, (
        "Copied abstracts require a separate reuse review; keep citation metadata only: "
        + ", ".join(offenders[:10])
    )
