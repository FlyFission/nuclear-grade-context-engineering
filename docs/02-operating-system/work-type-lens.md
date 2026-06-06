# Work-Type Lens

**Purpose:** Classify what *kind* of change this is, so the front-door questions match the work. The work type is orthogonal to the Quick/Standard/Nuclear rigor mode: the mode grades how much rigor a change earns by consequence; the work type sets which questions and outputs matter by kind. A brownfield change can be Quick; a greenfield change can be Standard.

Use this from `questioning-attitude`, before picking a mode in `rating-change-risk`.

## The four types

- **Greenfield** — net-new code or a new subsystem with few existing callers. Force interface, contract, and acceptance questions: what "done" looks like, who consumes it, what is explicitly out of scope.
- **Brownfield** — a change inside an existing, depended-on system. Force blast-radius questions: which callers, schemas, and stored state are touched, and what must stay backward-compatible.
- **Defect-fix** — repair of wrong behavior. Force a reproduction first, then a regression guard: a failing test that captures the defect before the fix, and the narrowest change that turns it green.
- **Refactor-migration** — behavior held constant while structure, storage, or platform moves. Force rollback-of-state and cutover questions: how to move data or traffic in reversible steps, and how to roll back after partial progress.

**Types can overlap.** A change is often several at once — a production defect fix is brownfield and defect-fix; a live migration is brownfield and refactor-migration. Name every type that fits and ask the union of the questions they force; do not let one label excuse the questions another would raise.

## Why it changes the questions

The same prompt — "add a field to the user record" — is a greenfield acceptance question on a new service and a backward-compatibility-plus-migration question on a live one. Naming the type up front is what surfaces the migration and rollback questions a generic plan would skip. For the runtime detail a brownfield or migration change must screen, see `change-impact.md`.

## Exit criteria

Every applicable work type is named, and the union of the questions they force is asked before a mode is chosen or a plan is written.

## Source-lineage note

This lens is an original Nuclear-grade workflow distinction. It draws on public software-lifecycle and configuration-management practice mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
