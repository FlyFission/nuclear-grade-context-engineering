# Public Citation Strategy

**Purpose:** Keep Nuclear-grade credible and tied to its sources. Do this without flooding the README with citations and without implying compliance.

---

## Citation philosophy

Citations should answer three questions:

1. Where did this engineering habit come from?
2. Why does it matter for software?
3. What is the safe boundary of the analogy?

They should never create a compliance claim.

---

## README citation strategy

The README should include only a small starter set of sources:

```text
DOE-STD-1073 — configuration management
DOE-STD-1189 — integration of safety into design
DOE-STD-3024 — design descriptions
DOE-STD-3009 — hazard analysis / safety-basis method
NRC RG 1.168–1.173 — public nuclear software lifecycle/V&V/CM/testing/requirements guidance
NIST SP 800-218 — Secure Software Development Framework
NIST SP 800-161 — cyber supply-chain risk management
NASA Software Engineering Handbook / NASA-STD-8739.8 — high-reliability software and assurance
SLSA / OpenSSF / OWASP — practical software supply-chain and security assurance
```

Then link to:

```text
docs/00-standards-foundation/source-map.md
```

---

## Template citation strategy

Each template should carry a short source-lineage note:

```text
Source lineage: Inspired by public configuration-management and software-assurance concepts from DOE-STD-1073 and NRC RG 1.169. This template is an original software workflow and does not claim compliance.
```

Keep citations near the end of templates. The user should see the workflow first, the lineage second.

---

## Field-guide citation strategy

Field-guide docs may include a fuller section:

```text
Source lineage
Concept extracted
Software translation
Activation threshold
Minimum useful version
Overhead trap
What not to claim
```

---

## Examples citation strategy

Worked examples should show practical use, not explain standards.

Use citations sparingly:

- one source-lineage box at the top;
- one source-lineage table at the end;
- no paragraph-by-paragraph standard commentary.

---

## Citation quality rules

Every public citation should be:

- linkable without purchase;
- stable enough for GitHub readers;
- official source preferred over secondary sources;
- used for concept lineage, not compliance claim;
- accompanied by boundary language when it could be misread.

---

## Citation status labels

Use these labels in `source-map.md`:

| Status | Meaning |
|---|---|
| verified-public | Official public page/link checked. |
| public-url-needed | Known public source, but official URL still needs verification. |
| supporting-context | Public but not core to the repo. |
| excluded-direct | Do not use as direct source lineage. |
