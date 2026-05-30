# Efficacy Harness

**Purpose:** Make one part of this comparison *reproducible*. Anyone can run a
single command and mechanically check that each worked-example artifact actually
surfaces the decision signals the methodology claims it teaches.

```bash
python tools/ng.py eval .
```

The rest of the comparison (`methodology.md`, `results-summary.md`,
`trial-records/`) is author-judged and qualitative. This harness adds a small,
honest, runnable layer on top of it.

## What it measures

For each eval case, the harness reads the real trial-record artifact, isolates
the `## Nuclear-Grade Trial` section, and checks whether each declared decision
signal is present (any of several accepted phrasings counts). It reports
per-case coverage and an overall total, and exits non-zero if any case is
missing a required signal.

A *signal* is a decision element drawn from that scenario's stated risks, for
example:

- U02 (agent workspace boundary): bounds agent write authority; states
  adversarial proof claims; makes a public non-claim.
- U07 (payment webhook idempotency): escalates mode for money-moving impact;
  bounds payment credentials; conditions release on rollback and a risk owner.
- U04 (public assurance wording): separates source inspiration from satisfied
  requirements; separates license permission from assurance; conditions release
  on a prohibited-claim scan.

The cases live in [`evals/cases/`](../../../evals/cases) as plain JSON so they
are easy to read, review, and extend.

## What it does NOT measure

- It does **not** prove the underlying engineering is correct, safe, secure,
  compliant, certified, or production-ready.
- A present signal means the artifact *names* the decision element. It is not
  evidence that the element is adequately handled in the real world.
- It is **not** an A/B benchmark or a user study, and it does not score a live
  model. The simple-prompt-versus-Nuclear-grade comparison stays qualitative in
  `results-summary.md`; it is deliberately not mechanized here, because those
  author-written meta-sections describe gaps using the same vocabulary as the
  signals and cannot be scored by substring presence without inflating the
  result.

## Why it is useful anyway

- **Regression guard.** If a worked example is later edited and a decision
  element is dropped, the harness fails. The examples cannot silently drift away
  from what the methodology claims they demonstrate.
- **Reproducibility.** A skeptic does not have to trust the author's 1-5 scores
  to confirm the artifacts contain the named decision structure. They run the
  command.
- **Extensibility.** Adding a worked example means adding one JSON case with
  signals grounded in that scenario's risks.

## Adding a case

Create `evals/cases/<id>-<slug>.json`:

```json
{
  "id": "U13",
  "title": "Short scenario name",
  "artifact": "docs/03-worked-examples/.../trial-records/<file>.md",
  "section": "## Nuclear-Grade Trial",
  "signals": [
    { "name": "Alternatives: any phrasing counts", "any": ["phrase one", "phrase two"] },
    { "name": "Conjunctive gates: all must appear", "all": ["rollback path", "monitoring query", "residual risk owner"] }
  ]
}
```

Use `any` for genuine alternatives (several ways to name the same element) and
`all` for distinct gates that must each be present (so a multi-part release
decision cannot score as satisfied when only one gate is named). Author the
signals from the scenario's stated risks, not by copying the prose back out of
the artifact. Each signal should be a decision a reviewer would want surfaced,
with phrasings robust to small wording changes.

## Boundary Note

This harness checks the presence of named decision signals in artifacts. It does
not establish safety, security, compliance, certification, formal verification,
formal validation, production suitability, or regulatory adequacy.

## Source-Lineage Note

This harness is an original Nuclear-grade adoption artifact using the repo
operating model and public-source lineage summarized in
`docs/00-standards-foundation/source-map.md`.
