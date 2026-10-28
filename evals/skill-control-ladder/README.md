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

## Results

Four pools, all rubric-scored, plus a measured grader baseline.

| Pool | What it asks | C4 − C1 | p (perm) |
|---|---|---|---|
| **`v1c` (27 skills)** | **the confirmatory run: all arms generated contemporaneously** | **+0.102** | **<0.0001** |
| `v1` (27 skills) | same scenarios, but C0/C4 adopted from an earlier pilot run | +0.132 | 0.0008 |
| `hard` (7 skills) | scenarios pre-screened to be hard for the control | −0.065 | 0.31 |
| `negative` (29 skills) | do skills over-fire where they declare they should not? | +0.030 | 0.32 |

**Cite `v1c`, not `v1`.** `v1` adopted 81 of 81 C0 cells and 69 of 81 C4 cells
from a pilot run weeks earlier while generating C1/C2/C3 fresh. `claude-sonnet-5`
is an alias to a hosted model, so the input-spec hash proves the prompt and flags
matched but cannot prove the serving backend did. Both reused arms came out lower
on the clean rerun (C0 −0.028, C4 −0.039) while the always-fresh arms barely moved
(≤0.014) — the drift signature, worth about a quarter of the original estimate.
`v1` is kept as the preliminary, cost-saving analysis.

The claim this supports:

> On 27 repository-authored scenarios evaluated against repository-derived
> criteria, direct injection of the matching full skill raised Claude Sonnet 5's
> mean rubric score by **0.102** over one fixed generic reviewer prompt
> (19 skills better, 1 worse, 7 tied; sign and permutation p < 0.0001) in a
> contemporaneous run with no transcript reuse. It did **not** replicate on seven
> newly calibrated hard scenarios, and it does not measure skill selection,
> external correctness, or production outcomes.

That is narrower than "the skills work", deliberately. It measures **instruction
adherence on scenarios and criteria authored inside this repository** — see
[Circularity](#circularity-the-biggest-limitation) below.

Supporting numbers:

- A strong generic paragraph alone buys **+0.030** (sign p=0.049, permutation
  p=0.18). The two tests disagree, so this is unresolved — but it is no longer
  the clean null that `v1` showed, and "any instruction helps" is not ruled out
  as firmly as an earlier draft of this file claimed.
- **Compression: C4 − C3 = −0.000** (8 better / 7 worse, p=1.0). At the pool
  level the full `SKILL.md` and a five-bullet compression are indistinguishable.
  This says nothing about *which* skills are safe to compress — per-skill
  intervals are far too wide for that.
- Grader reliability: **κ=0.811** test-retest, **κ=0.782** cross-model
  ([`GRADER-RELIABILITY-hard.md`](GRADER-RELIABILITY-hard.md)). Reliability, not
  validity: a stable grader can consistently reward the wrong thing.
- Evidence integrity: `scripts/verify_lineage.py` proves all **1,983** grading
  rows hash-match the committed transcripts they graded, all **1,263** transcripts
  still match the inputs that produced them, and every rubric grade matches the
  rubric it was scored against.
- Skill pin: all four pools were measured against `skills/` tree
  **`621fc0c1`** (`data/skill-pins.json`). Skill bodies change on main, and a
  result is a statement about the text that produced it — so the pin is recorded
  rather than chased. When it differs from HEAD, that is a stated fact, not a
  defect; a pool needs regenerating only to speak about today's skills.

## Circularity, the biggest limitation

The `v1`/`v1c` criteria were authored by the same effort that wrote the skills,
and the binary rubrics decompose those criteria into several separately scored
checks. Several criteria ask for this repository's own vocabulary and process
(a named owner, a recheck trigger, a closed packet with attribution). The
matching skill is then injected directly, bypassing selection entirely.

So a positive result demonstrates that a skill **successfully transmits its own
instructions** — not that those instructions are correct, necessary, efficient,
or better than other professional practice. No blinded human grading has been
done, so there is no evidence the rubric tracks expert judgment.

Closing this needs scenarios and criteria authored by people who have not read
the skills, scored on observable consequences rather than repository phrases.
That is second-generation work and is not in this directory.

## What this does NOT measure

- **Skill selection.** Arms inject one skill directly into the system prompt,
  bypassing retrieval. In real use the model sees all 29 descriptions and must
  pick. Trigger precision/recall across the full library is unmeasured — which
  is why the `briefing-an-agent`/`handing-off-work` overlap had to be found by
  hand during grading rather than by the harness. This is the largest remaining
  gap: real over-firing happens when the wrong skill is *selected*, and every
  pool here hands the model the right one.
- **Real-world over-firing.** The `negative` pool is a *forced-load
  proportionality test*, not an over-firing test: it injects a skill the scenario
  declares out of scope and asks whether the response stays proportionate. It
  also carries a known confound — several scenarios ask the model to edit project
  files while the isolated work directory is empty and tools are read-only, so
  the response asks clarifying questions and the rubric partly scores a missing
  fixture as disproportionate. **Treat "no over-firing cost" as unsupported, not
  merely caveated**, until the pool is rebuilt with real repository fixtures.
- **Per-skill verdicts.** Bootstrap intervals over three trials are too wide to
  resolve individual skills, and a bootstrap at n=3 reports an artificially tight
  interval whenever the three trials agree. Two earlier per-skill claims
  ("four skills are harmful", "cut ~14,000 words of skill text") were drawn from
  this table against a threshold that was not statistically valid, and both were
  retracted.
- **Validity of the grader**, as distinct from its reliability. No blinded human
  gold-standard sample exists.
- **Interaction.** Effects measured one skill at a time may not survive with the
  whole library loaded.
- **Anything beyond Sonnet**, one scenario per skill, and 3 trials per cell.

`verifying-final-artifacts` and `reviewing-code-quality` have no trigger-case
scenario and so are absent from the `v1`/`v1c` and `hard` numbers. Both are
covered in the `negative` pool, which is built from every skill on disk.

## Reports

Generated — rerun `analyze_ladder.py` rather than editing them.

| File | Pool | Scoring |
|---|---|---|
| [`REPORT-v1c-rubric.md`](REPORT-v1c-rubric.md) | `v1c` (confirmatory) | binary rubric |
| [`REPORT-rubric.md`](REPORT-rubric.md) | `v1` (preliminary) | binary rubric |
| [`REPORT.md`](REPORT.md) | `v1` | compound criterion |
| [`REPORT-hard-rubric.md`](REPORT-hard-rubric.md) | `hard` | binary rubric |
| [`REPORT-negative-rubric.md`](REPORT-negative-rubric.md) | `negative` | binary rubric |
| [`GRADER-RELIABILITY-hard.md`](GRADER-RELIABILITY-hard.md) | `hard` | κ, test-retest + cross-model |

The compound-criterion and binary-rubric runs are **two scoring resolutions of
the same criteria**, not two independent grading methods: the rubrics are
decomposed from those same criteria by a model that was shown them. The rubric
is the higher-resolution view, and the `v1` effect persisting under it is a
robustness check, not external validation.
