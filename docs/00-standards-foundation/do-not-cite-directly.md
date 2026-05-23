# Do Not Cite Directly / Do Not Derive Templates From

**Purpose:** Protect the public repo from paywalled, proprietary, copyrighted, or compliance-sensitive source misuse.

---

## Rule

Do not use the following as direct template lineage, do not reproduce or closely paraphrase their language, and do not structure Nuclear-grade artifacts to mirror them unless the specific source is publicly available and we are making only a high-level conceptual mention.

---

## Excluded as direct inputs

```text
ASME NQA-1
EPRI reports
IEEE standards
IEC standards
ISO standards
ANSI/ANS standards
NEI documents
proprietary QA manuals
proprietary procurement manuals
utility procedures
vendor proprietary qualification packages
customer confidential procedures
```

---

## Allowed high-level context

It is acceptable to say, when necessary:

> Regulated industries often use formal consensus standards and proprietary guidance for quality assurance, procurement, dedication, software qualification, and safety analysis. Nuclear-grade does not reproduce those materials or claim compliance with them.

It is not acceptable to say:

> This template is based on NQA-1.

or:

> This dependency trust basis implements commercial-grade dedication.

---

## Why this matters

Nuclear-grade should be:

- public;
- linkable;
- inspectable;
- remixable;
- GitHub-native;
- legally clean;
- useful outside regulated settings;
- free from fake compliance claims.

Using paywalled/proprietary standards as hidden template lineage would undermine that mission.

---

## If a contributor wants to add a source

Ask:

1. Is the source public/open/linkable?
2. Can every reader verify it without a login or purchase?
3. Are we using it only for concept lineage, not compliance?
4. Are we creating an original software-native workflow?
5. Would a reader think we are claiming formal compliance?

If any answer is unsafe, classify the source as context-only or excluded.
