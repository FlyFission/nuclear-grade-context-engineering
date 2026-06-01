# Incident Response

**Purpose:** Run a live incident the way a submarine runs a casualty — stabilize first, analyze second. This is the operating mechanics behind the `responding-to-incidents` skill, `ng-incident`, and `templates/standard/incident.md`.

**Boundary:** Original software-workflow translation. It does not create formal assurance, compliance, certification, safety, or regulatory adequacy.

---

## The loop

1. **Declare and command.** Name one incident commander; everyone else takes a defined role. One source of truth, one decision-maker.
2. **Stabilize.** Take the safest reversible action that stops or limits the harm before chasing the root cause.
3. **Timeline with labels.** Keep a running log and label every line FACT or HYPOTHESIS. Acting on an unconfirmed cause is how a small incident becomes a large one.
4. **Reversible-first.** Prefer reversible moves while the cause is unconfirmed; record every decision and who made it. Hold an irreversible fix until the cause is confirmed or the risk is explicitly accepted by a named owner.
5. **Communicate on a cadence.** Post status on a fixed interval, even when the status is "no change yet."
6. **Hand off cleanly.** Across shifts, transfer state, open actions, and authority limits (`handing-off-work`).
7. **Close to closure.** End the live phase only when stable, then open corrective actions — each with an owner and a closure trigger — and route the lesson to the learning record (`learning-from-experience`) and the deficiency register (`deficiency-register.md`).

## Watch-team roles in an incident

| Submarine role | Software incident role |
|---|---|
| Officer of the deck / command | Incident commander |
| Specialist watchstanders | Service, database, infra, and security owners |
| Watchteam backup | Secondary on-call, staff/platform support |
| Logs | The incident timeline and decision record |

## Reliability framing

SRE practice complements this: monitor service indicators against objectives (SLOs), spend the error budget deliberately, and act through a control loop. The caution travels with it — insisting on 100% reliability suppresses innovation and breeds over-conservative systems. Stabilize-first is about recovering from failure, not pretending it never happens.

## Source-lineage note

Original Nuclear-grade operating doc influenced by naval damage-control / casualty-control practice and the procedure-use, place-keeping, three-way-communication, turnover, and operating-experience habits in DOE-HDBK-1028-2009, with public SRE reliability practice as supporting context, used as concept lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
