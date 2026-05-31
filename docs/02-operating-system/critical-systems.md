# Critical Systems

**Purpose:** Frame the highest-consequence tier the way the Navy framed submarine survivability after the loss of USS *Thresher* (1963): a small, disciplined quality program focused on the few outcomes that must not fail. This is doctrine for Tier 0 work (see `risk-tiers-and-modes.md`); it is a framing, not an org-building mandate.

**Boundary:** Original software-workflow translation. It does not reproduce the SUBSAFE program or any standard, and it does not create formal assurance, compliance, certification, safety, or regulatory adequacy.

---

## Five pillars, translated

The public account of SUBSAFE describes a quality program with five pillars. Their software analogues for critical systems (money movement, identity, customer data, safety, critical infrastructure, or AI agents with production authority):

| Pillar | Software equivalent |
|---|---|
| Work discipline | code review, test discipline, release discipline, incident discipline |
| Material control | dependency control, artifact provenance, SBOMs, signed builds, controlled secrets |
| Documentation | design records, runbooks, diagrams, ownership records, migration plans |
| Compliance verification | CI gates, security scans, production-readiness checks, restore tests, audit trails |
| Culture | engineers tell the truth early; leaders reward surfaced risk, not hidden heroics |

The discipline is to apply this only where it is earned. Tier 0 gets the full set; everything else uses the lighter modes. Applying critical-systems ceremony everywhere is itself a failure — it trains people to treat the ceremony as theater.

## The software team as a watch team

A nuclear watch team is a trained operating unit with roles, checklists, backups, a shared language, and the authority to act — not a loose group of talented individuals. The software analogue:

| Watch-team element | Software version |
|---|---|
| Command authority | incident commander, release captain, or tech lead |
| Specialist watchstanders | service, database, infra, and security owners |
| Watchteam backup | peer reviewers, secondary on-call, platform/staff support |
| Standing orders | runbooks, SLO policy, escalation policy, deployment policy |
| Logs | incident timeline, deployment log, decision record |
| Drills | game days, failover tests, restore tests, security exercises |

## Ownership and level of knowledge

Two Rickover principles anchor the tier:

- **Technical understanding cannot be delegated.** The owner of a critical change understands the request path, failure modes, dependencies, recovery path, and the competence of whoever (or whatever) operates it — not just the summary (Charter Art. 5). "If you cannot write it down clearly, the team probably does not understand it yet."
- **Competence precedes authority.** Authority over a critical system is earned by demonstrated competence — for a person, qualification; for an agent, eval coverage and a track record — before it is primary on a risky change (see `authority-and-intent.md`).

These are framings to raise the bar on Tier 0 work, not a mandate for this repo to run qualification programs, on-call rotations, or drill schedules. That belongs to the organization, not to a per-change methodology.

## Source-lineage note

Original Nuclear-grade operating doc influenced by the public history of the SUBSAFE submarine quality program and Rickover / Naval Reactors ownership-and-level-of-knowledge culture, used as concept lineage and not as an implemented program. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
