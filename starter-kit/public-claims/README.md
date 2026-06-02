# Starter kit: Public-claims

Use this when your repo says things in public that someone might rely on — claims about
safety, security, compliance, licensing, provenance, or how an AI system behaves.

## When this trigger fires

Any "yes" puts you in this kit:

- the repo's README, docs, or release notes make assurance-adjacent claims;
- the repo cites standards, regulations, or specifications by name;
- the repo describes an AI system's behavior in ways a user, customer, or auditor would rely
  on;
- the repo is published under a license whose obligations need careful wording;
- the repo's source lineage is contested, paywalled, or non-public.

## Drop this into your repo

```bash
# from this repo's root, into your repo at $TARGET:
cp -r starter-kit/core/{AGENTS.md,.nuclear} "$TARGET"/
cp starter-kit/public-claims/{BOUNDARY-WORDING.md,DISCLAIMER.md} "$TARGET"/
# Add the Claims-discipline cluster:
for s in checking-legal-and-safety-wording checking-source-claims; do
  mkdir -p "$TARGET/skills/$s"
  cp "skills/$s/SKILL.md" "$TARGET/skills/$s/SKILL.md"
done
# Add the boundary docs as required reading:
mkdir -p "$TARGET/docs/00-standards-foundation"
cp docs/00-standards-foundation/{compliance-boundaries.md,do-not-cite-directly.md,public-citation-strategy.md} \
   "$TARGET/docs/00-standards-foundation/"
```

## What this kit contains

- [`BOUNDARY-WORDING.md`](BOUNDARY-WORDING.md) — a guide and a prohibited-phrase reference,
  derived from `docs/00-standards-foundation/compliance-boundaries.md` and `do-not-cite-
  directly.md`, plus a small house-style example list.
- [`DISCLAIMER.md`](DISCLAIMER.md) — a skeleton disclaimer with `<fill-in>` markers, in the
  defensive register the framework's test suite enforces.

## The Claims-discipline cluster

| Skill | When to invoke |
|---|---|
| `checking-legal-and-safety-wording` | Before a public claim ships — README edits, release notes, marketing copy, regulator-facing material. |
| `checking-source-claims` | When the repo says where an idea comes from or what standard it tracks. |

Both invoke [`proving-claims`](../../skills/proving-claims/SKILL.md) from Core, which is the
universal map-each-claim-to-evidence-or-a-gap discipline.

## Source-lineage note

This kit packages original patterns from this repository. It does not create assurance. See
[`../../DISCLAIMER.md`](../../DISCLAIMER.md).
