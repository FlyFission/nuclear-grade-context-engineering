## Summary

<!-- What changed, why it matters, and what evidence reviewers should inspect. -->

## Mode

<!-- Quick / Standard / stronger. One line on why a lower mode is insufficient. -->

## Change packet

<!-- Link `.nuclear/changes/<slug>/`. For trivial docs-only changes write N/A and state why. -->

## Proof command + result

```bash
# the exact command(s) that prove the change, and the actual outcome
```

## Enforcement rung

<!-- Where do the controls that gate this work live, relative to the agent's writable set?
     Rung 1 advisory print, 2 editable exit-code, 3 editable test, 4 out-of-band CI,
     5 branch protection / human review. Rung 4+ is required when the agent has authority
     over its own tests, prompts, or CI. -->

## Evidence custody and coupling

<!-- For each load-bearing claim, link the packet's custody record and state the profile:
     actor / context / mechanism / authority / resource = coupled, partially separated, or separated.
     Name the evidence pattern, the consequence-specific minimum, and any residual gap. -->

- Decisive evidence IDs / links:
- Custody/profile record:
- Verdict owner:
- Minimum profile met? yes / no; gap:

## Verification

- [ ] Tests and validator pass locally.
- [ ] Packet validation passes if this PR creates or changes a `.nuclear/changes/<slug>/`
      packet.
- [ ] HPI records are updated if turnover, self-check, OPEX, or dependency / model / API trust
      was activated.
- [ ] New claims avoid compliance, certification, regulator approval, production sandbox, or
      formal QA overclaiming.
- [ ] New source-lineage entries use public, open, linkable sources or are explicitly marked
      unresolved.
- [ ] Boundary wording was checked; residual risks are stated below.
- [ ] Decisive evidence custody and all five coupling axes are disclosed; strict-custody validation passes for migrated Standard packets.

## Residual risks or gaps

<!-- Accepted gaps, deferred work, and anything reviewers should not infer from this PR. -->
