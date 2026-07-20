import json
from pathlib import Path

from tests.test_skill_contracts import EXPECTED_SKILLS

ROOT = Path(__file__).resolve().parents[1]
ROUTING_CASES = ROOT / "evals" / "skill-routing-cases.jsonl"
OUTPUT_CASES = ROOT / "evals" / "skill-output-cases.jsonl"


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_deterministic_efficacy_manifests_cover_initial_seed_skills():
    """The first deterministic route/output manifests must cover the known hard cluster.

    This is intentionally weaker than all-28 coverage; it verifies the new scaffolding
    starts with PR #62's weakest and highest-overlap evidence gaps.
    """

    covered = set()
    for row in _load_jsonl(ROUTING_CASES):
        covered.add(row["skill"])
    for row in _load_jsonl(OUTPUT_CASES):
        covered.update(row.get("skill_set", []))

    assert {
        "briefing-an-agent",
        "checking-legal-and-safety-wording",
        "checking-release-readiness",
        "proving-claims",
        "rating-change-risk",
    } <= covered


def test_every_skill_has_some_deterministic_efficacy_coverage():
    """Ratchet for the exhaustive benchmark: every skill needs BOTH routing and
    output coverage. Tracking a single union would let a future edit drop all of
    one dimension for a skill while the other still satisfied the assertion,
    leaving that benchmark dimension untested."""

    routing_covered = {row["skill"] for row in _load_jsonl(ROUTING_CASES)}
    output_covered = set()
    for row in _load_jsonl(OUTPUT_CASES):
        output_covered.update(row.get("skill_set", []))

    missing_routing = sorted(EXPECTED_SKILLS - routing_covered)
    missing_output = sorted(EXPECTED_SKILLS - output_covered)

    assert not missing_routing, (
        "skills lack routing coverage in evals/skill-routing-cases.jsonl: "
        f"{missing_routing}"
    )
    assert not missing_output, (
        "skills lack output coverage in evals/skill-output-cases.jsonl: "
        f"{missing_output}"
    )
