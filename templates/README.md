# Templates

Templates are the minimum useful records for Nuclear-grade packets. Copy them into `.nuclear/changes/<slug>/` and keep them short enough to review.

## Quick mode

Use for low-consequence, reversible changes:

```text
templates/quick/risk.md
templates/quick/proof.md
```

## Standard mode

Use for meaningful product/software/configuration changes:

```text
templates/standard/risk.md
templates/standard/basis.md
templates/standard/plan.md
templates/standard/trace.md
templates/standard/verification.md
templates/standard/ship.md
```

Standard templates are intentionally lightweight. If an artifact does not need much detail, keep it short rather than deleting it.

Use `templates/standard/supplier-trust.md` only when a dependency, model, API, SaaS tool, generated artifact, or vendor claim affects evidence, permissions, data, release posture, or public trust. It is an activated extension, not part of every Standard packet.

## Activated CM records

Use `templates/cm/` when a change affects controlled configuration: prompts, models, tools, dependencies, docs, releases, runbooks, evals, or other items whose approved state matters.

```text
templates/cm/controlled-items.md
templates/cm/change-impact.md
templates/cm/baseline.md
templates/cm/variance.md
templates/cm/opex.md
```

Do not activate all CM records by default. Add only the record that answers a decision question.

## Golden path

Use `templates/golden-path/` when a change needs the public Questioning Attitude path in addition to the Standard packet.

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

Keep `Classify` inside the risk/mode screen. Keep `Baseline` late, after review and decision, as accepted configuration state.

Use `turnover.md` when responsibility transfers to another human or agent. Use `self-check.md` before a critical action where wrong target, exceeded authority, public overclaim, irreversible state, or release confusion is plausible.

## Validation

Run the validator against a completed packet:

```bash
python tools/ng_validate.py .nuclear/changes/<slug>/
```

See the completed example packet under:

```text
docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions/
```
