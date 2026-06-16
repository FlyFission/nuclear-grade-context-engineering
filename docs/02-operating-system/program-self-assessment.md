# Program Self-Assessment

**Purpose:** Periodically step back and check whether the method itself — the workflow and its controls — is actually being followed and is actually working, separate from verifying any single change. It names the standing self-assessment habit and routes what it finds into the OPEX learning loop (`learning-from-experience`, `templates/cm/opex.md`) and the deficiency register (`tracking-deficiencies`, `deficiency-register.md`). It supports Charter Art. 3 (rising standards) and the honest-self-assessment habit in `learning-from-experience`.

**Boundary:** Original software-workflow translation. It does not create formal assurance, compliance, certification, safety, or regulatory adequacy. No compliance claim is made; naming the mechanism is in scope, building organizational audit machinery, mandated cadences, or staffing and drills is not.

---

## Why periodic, separate from event-driven OPEX

The learning loop fires on a surprise: a near miss, an incident, or an escaped defect produces a lesson and a durable control update. Per-change verification fires on each packet: it proves *that* change. Neither one asks the standing question — *are we still running the method the way we said, and is the method still earning its keep?* Controls decay quietly when nothing is visibly broken: a gate that is always skipped, a validator everyone overrides, a template that no longer matches how work is really done. A periodic self-assessment is the scheduled look that catches that drift before an incident does.

## What an assessment looks at

- **Is the workflow being followed?** Are packets actually produced for the changes that warrant them, or routed around? Are intent declarations and human gates real, or rubber-stamped?
- **Are the controls effective?** Do the validators and reviews catch what they are meant to, or do they mostly produce overrides and noise?
- **Inputs already in the repo** — read what exists rather than launching a survey: `ng doctor` and `ng status` output, recent change-control packets, open OPEX entries, the deficiency register, and adherence to the Charter articles that matter for the work being done.

## How it connects (reuse, not a new artifact)

A self-assessment produces findings, not a new register. Each finding routes to a mechanism that already exists:

- A lesson that should change a durable control becomes an OPEX entry (`templates/cm/opex.md`).
- A known problem that will outlive this look becomes a deficiency-register entry — with an owner, a disposition, and a review trigger (`deficiency-register.md`).
- A finding touching safety, security, data integrity, or a protected outcome escalates rather than waiting for the next assessment.

## Independence, proportionate to consequence

Who performs the assessment scales with what is at stake. Routine, low-consequence work can be
self-assessed reflexively. **Release-bearing or protected-outcome work is assessed — or
independently reviewed — by someone not responsible for the work being graded**, with findings
routed to the deciding authority, so a team cannot quietly pass its own adherence. This applies
the graded, independent-verification principle the repo already uses for high-tier proof
(`deciding-who-decides`, `proving-claims`) on a schedule; it adds no new independence machinery.

## The discipline

An assessment that raises nothing is the finding worth distrusting most. Name a real gap against the standard, or record why none is warranted this time — silence is not evidence of health. Keep it lightweight and proportionate: the point is honest actual-vs-standard correction routed to an owner, not assessment theater and not a second copy of the mechanical checks `ng doctor` already runs. Raise the work to meet the standard; do not quietly lower the standard to match how the work has drifted.

## Source-lineage note

Original Nuclear-grade operating doc influenced by public assessment-and-correction concepts: 10 CFR 830 Subpart A (quality work processes, assessment, and correction), the public DOE quality assurance page / DOE O 414.1E context (assessment and corrective action under a graded approach), DOE O 413.3B (independent reviews at decision points), and the operating-experience and honest-self-assessment habits in DOE-HDBK-1028-2009 and public Navy "Get Real, Get Better" framing, used as concept lineage only. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
