# Templates

Templates are the smallest useful records for Nuclear-grade packets. Copy them into `.nuclear/changes/<slug>/` and keep them short enough to review.

## Quick mode

Use for low-stakes changes you can undo:

```text
templates/quick/risk.md
templates/quick/proof.md
```

## Standard mode

Use for real product, software, or setting changes:

```text
templates/standard/risk.md
templates/standard/basis.md
templates/standard/plan.md
templates/standard/trace.md
templates/standard/verification.md
templates/standard/ship.md
```

Standard templates are kept light on purpose. If a record does not need much detail, keep it short rather than delete it.

Use `templates/standard/supplier-trust.md` only when a dependency, model, API, SaaS tool, generated file, or vendor claim affects the evidence, permissions, data, release stance, or public trust. It is an add-on you turn on, not part of every Standard packet.

## Activated CM records

Use `templates/cm/` (records for keeping the approved version under control, CM) when a change affects controlled items: prompts, models, tools, dependencies, docs, releases, runbooks, evals, or anything else whose approved state matters.

```text
templates/cm/controlled-items.md
templates/cm/change-impact.md
templates/cm/baseline.md
templates/cm/variance.md
templates/cm/opex.md
```

Do not turn on every CM record by default. Add only the record that answers a real decision question.

## Golden path

Use `templates/golden-path/` when a change needs the public Questioning Attitude path on top of the Standard packet.

```text
templates/golden-path/questioning-attitude.md
templates/golden-path/spec.md
templates/golden-path/turnover.md
templates/golden-path/self-check.md
templates/golden-path/decision.md
```

The golden path is:

```text
Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn
```

Keep `Classify` inside the risk and mode screen. Keep `Baseline` late, after review and the decision, as the accepted state everyone agreed is correct.

Use `turnover.md` when the work passes to another person or agent. Use `self-check.md` before a risky action where you could hit the wrong target, go past your authority, overclaim in public, reach a state you cannot undo, or get confused about the release.

## Validation

Run the validator against a completed packet:

```bash
python tools/ng_validate.py .nuclear/changes/<slug>/
```

See the completed example packet under:

```text
docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions/
```
