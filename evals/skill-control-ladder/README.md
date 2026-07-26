# Skill Control Ladder

**Question:** how much of a Nuclear-grade skill's measured effect is the
specific knowledge the skill carries, and how much is the mere presence of *any*
structured instruction in the system prompt?

The existing [`skill-benchmark-pilot`](../skill-benchmark-pilot/) answers a
different question than it appears to. Its `without_skill` condition appends
nothing to the system prompt at all
([`run_pilot_all.py`](../skill-benchmark-pilot/scripts/run_pilot_all.py)), so
every result in it is **skill versus nothing**, not skill versus prompting.
Those two conflate:

1. the specific knowledge in the skill changed behavior, and
2. any structured instruction would have changed behavior.

This directory adds the intermediate arms that separate them.

## The ladder

Every arm runs through an identical harness — same subject model, same tool
allowlist, same budget cap, same isolation flags, same scenario, same grader,
same pre-registered pass criterion. **The only thing that varies is the text
appended to the system prompt.** That is what makes the between-arm deltas
attributable to prompt content rather than to harness differences.

| Arm | Appended | What its delta isolates |
|---|---|---|
| `C0_bare` | nothing | the pilot's original baseline |
| `C1_generic_nudge` | one fixed skill-agnostic paragraph, identical for all 27 skills | **the "simple prompting" bar** |
| `C2_description_only` | the skill's `name` + frontmatter `description` | whether the label alone cues the behavior |
| `C3_compressed` | the skill compressed to ≤5 imperative bullets | how much of the skill text is load-bearing |
| `C4_full_skill` | the full `SKILL.md` body | the pilot's original treatment |

The headline number is **C4 − C1**, not C4 − C0.

**C4 − C3 is the improvement lever.** Where a skill scores the same compressed
to five bullets as it does at full length, the remaining prose is carrying token
cost without a measured behavioral effect — a concrete, per-skill edit backed by
evidence rather than taste.

### The C1 control is deliberately strong

`GENERIC_NUDGE` in [`scripts/ladder_common.py`](scripts/ladder_common.py) is one
paragraph, identical for all 27 skills, containing no domain vocabulary from any
of them. It was written to be a demanding bar on purpose. A weak control
("be thorough") would inflate every skill's measured effect, which is the exact
failure this experiment exists to detect. A skill that cannot beat one reusable
generic paragraph is not carrying knowledge the model lacks.

## Statistics

The pilot ran one significance test per skill, then had to correct 47 of them,
after which [nothing survived](../skill-benchmark-pilot/STATISTICAL_ANALYSIS.md).
That is the predictable result of treating each skill as its own hypothesis at
n=3.

This analysis instead pre-registers **one** primary hypothesis — across the
27-skill pool, C4 > C1 on paired per-skill scores — tested once. The paired
design supplies the power that per-skill tests cannot have at n=3. Per-skill
numbers are reported as descriptive effect sizes for triage, explicitly not as
27 additional hypotheses. Both tests used (exact sign test, paired permutation
test) are distribution-free.

## Reproducing

```bash
cd scripts
python3 run_ladder.py --dry-run     # plan + estimated spend, no calls made
python3 build_compressions.py       # generates the C3 arm text (cached by skill-body hash)
python3 run_ladder.py               # all arms; adopts valid pilot transcripts for C0/C4
python3 grade_ladder.py             # blind grading, same grader/criteria as the pilot
python3 analyze_ladder.py           # writes REPORT.md
```

Every script is cache-safe: a cell is only re-spent when a hash of everything
that determines its output (scenario, appended text, model, harness flags)
has actually changed. `--dry-run` reports how many live calls a given
invocation would make and what it would cost before any money is spent.

### Transcript reuse, and where it is refused

C0 and C4 are identical in construction to the pilot's `without_skill` and
`with_skill` conditions, so valid pilot transcripts are adopted rather than
re-spent — 150 of 162 at time of writing. The other 12 are **refused and re-run**:
four skills (`briefing-an-agent`, `checking-release-readiness`,
`deciding-who-decides`, `proving-claims`) had their `SKILL.md` amended after the
pilot ran, so their cached `with_skill` transcripts were produced from
superseded skill text. Adopting them would have quietly seeded the C4 arm with
text that no longer exists in the repo. `run_ladder.py` verifies each candidate
against the pilot's own recorded input-spec hash rather than trusting the
filename.

## What this does NOT measure

- **False positives.** Every scenario is a trigger case where firing the skill
  is correct. Nothing here measures the cost of a skill firing on a trivial
  change where the right answer is to stay light.
- **Skill selection.** Arms inject one skill directly into the system prompt,
  bypassing retrieval. In real use the model sees all 29 descriptions and must
  pick. Trigger precision/recall across the full library is unmeasured — which
  is why the `briefing-an-agent`/`handing-off-work` overlap had to be found by
  hand during grading rather than by the harness.
- **Interaction.** Effects measured one skill at a time may not survive with the
  whole library loaded.
- **Anything beyond Sonnet**, one scenario per skill, and 3 trials per cell.

`verifying-final-artifacts` has no scenario in the pool and is therefore absent
from every number here.

Results: [`REPORT.md`](REPORT.md) (generated — rerun `analyze_ladder.py` rather
than editing it).
