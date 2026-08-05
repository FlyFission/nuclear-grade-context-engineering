## Summary

<!-- What changed, why it matters, and what evidence should reviewers inspect. -->

## Mode

<!-- Administrative floor / Quick / Standard / stronger. Name why this is the lightest honest mode. -->

## Change packet

<!-- Link .nuclear/changes/<slug>/, or write N/A when the administrative floor applies and explain why. -->

## Proof command + result

```bash
# the exact command(s) that prove this change, and the actual outcome (e.g. test names + status)
```

## Verification

- [ ] Tests and validator pass locally:

  ```bash
  python -m pytest -q
  python tools/ng.py doctor .
  ```

- [ ] Packet validation passes if this PR creates or changes a `.nuclear/changes/<slug>/` packet.
- [ ] CM impact/baseline records are updated if controlled items changed.
- [ ] HPI records are updated if turnover, self-check, OPEX, or dependency/model/API trust is activated.
- [ ] `git diff --check` passes.
- [ ] New public docs contain no private paths, internal codenames, or stale launch residue.
- [ ] New claims avoid compliance, certification, regulator approval, production sandbox, or formal QA overclaiming.
- [ ] New source-lineage entries use public, open, linkable sources or are explicitly marked as unresolved.

## Residual risks or gaps

<!-- State accepted gaps, deferred work, and anything reviewers should not infer from this PR. -->
