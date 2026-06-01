# Boundary wording

How to write public-facing claims in this repo without overclaiming. Read once before editing
any README, release note, marketing copy, or regulator-adjacent document; consult again before
shipping.

## The rule

Public wording must stay inside its evidence and away from words it cannot back. Specifically:
do not say "compliant," "certified," "approved," "audited," "qualified," "regulator-approved,"
or "meets `<standard>`" unless an authorized organization has separately reviewed and approved
that claim under its own process. The framework's validator (`ng validate`) scans for these
patterns; use it as a tripwire, not as proof the wording is correct.

## Prohibited claim phrases (defensive list)

These phrases are flagged by the deterministic checker. Use them only inside a disclaimer or a
do-not-claim context:

- `formal verification and validation`, `formal V&V`
- `NQA-1 evidence`, `NQA-1 record`
- `certified quality assurance program`
- `regulatory approval`
- `commercial-grade dedication package`
- `<standards body> compliant` (NQA-1, ASME, EPRI, IEEE, IEC, ISO, ANSI, ANS, NEI, NRC, DOE,
  NASA, NIST, CISA, …) — and the verb-stem paraphrases (`meets`, `conforms to`, `satisfies`,
  `implements per`, `complies with`).

Add domain-specific phrases your project should avoid: `<fill-in>`.

## Allowed phrasings

Prefer wording like:

- "public-source-inspired";
- "original software workflow";
- "evidence-oriented";
- "non-compliance-claiming";
- "inspired by";
- "we do not claim X";
- "out of scope for this release";
- "non-goal."

## Source-lineage discipline

When you say where an idea comes from:

- cite a public, open, linkable source (URL preferred) — or mark the lineage as unresolved;
- do not cite paywalled, draft, or contested sources as if they were settled;
- describe the relationship as inspiration, not implementation: "inspired by," "influenced
  by," not "implements" or "meets."

## Disclaimer convention

Every public document should end with a one-paragraph source-lineage note that names what the
document is and what it does not create. See [`DISCLAIMER.md`](DISCLAIMER.md) for the skeleton.

## Source-lineage note

This guide is derived from the public Nuclear-grade boundary discipline in
`docs/00-standards-foundation/compliance-boundaries.md` and `do-not-cite-directly.md` of the
parent repository. It does not create assurance.
