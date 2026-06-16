# Durable Memory

**Purpose:** Name what an agent's work should *remember between runs*, where it lives, and
how a later agent retrieves it safely. This is the persistent counterpart to
`context-window-discipline.md`: that doc keeps the live window small; this one keeps the
durable record useful. No compliance claim is made.

**Status:** Operating doctrine over records this repo already produces. It adds discipline,
not storage technology.

---

## 1. Core idea

The context window is ephemeral; the durable record is the memory. A lesson that lives only
in a chat transcript is lost the moment the thread ends — which is exactly the failure
`learning-from-experience` warns about: "the lesson is stuck in chat history." Durable memory
is the small set of records that survive a run and can be *retrieved* by the next one.

`context-window-discipline.md` §2 already names a "persistent cross-run memory" lifetime and
points it at baselines, OPEX records, and the deficiency register. This page develops the
other half of that row — how a later agent *finds and trusts* that memory — because keeping
the window small is worthless if the durable record is unreadable, unfindable, or poisoned.

---

## 2. What durable memory holds

Durable memory is not a new store to build. It is the records the repo already creates,
treated as a retrievable whole:

| Memory | Record | What a future run learns |
|---|---|---|
| Approved state | baselines | the version everyone agreed is correct, and its evidence |
| Lessons | OPEX records | what went wrong or nearly did, and the control that changed |
| Known problems | the deficiency register | open gaps, their age, owner, and disposition |
| Decisions and evidence | change packets | why a change was made and what proved it |
| Competence-to-act | qualifications | which actor may take which action class, and when that lapses |

Anything a future agent would have to re-derive from scratch, or would get wrong without, is
a candidate for durable memory. Anything run-scoped is not (see the lifetime table in
`context-window-discipline.md`).

---

## 3. Retrieval discipline

Memory only helps if the right slice is loaded at the right moment — and only the right
slice, because the window is a budget, not a bucket.

- **Pull memory at Question, Discover, and Plan.** Before questioning assumptions, load the
  relevant prior lessons, open deficiencies, and the current baseline. The Discover phase
  already asks for "prior packets … and operating experience"; this is where memory enters a
  run.
- **Retrieve by relevance, not by volume.** Load the lessons and deficiencies that touch this
  change, not the whole history. Just-in-time retrieval beats pre-loading everything
  (`context-window-discipline.md` §6).
- **Name it so it can be found.** A lesson no one can locate is the same as no lesson. Give
  durable entries stable names and links, and index them by the controlled item or failure
  mode they touch, so the next run finds them by the thing it is about to change.

---

## 4. Provenance, or memory poisons the future

A durable, agent-retrieved store is a poisoning target: a wrong "fact" written once is
re-cited as settled by every run that loads it. The guards in `context-window-discipline.md`
§3 apply with more force here, because the blast radius is every future run, not one window.

- **Every durable entry carries its evidence and source.** A lesson cites what happened and
  how it was verified; a baseline links its verification. Confidence is not a source.
- **Retrieved memory is a hypothesis, not authority.** A later agent treats a recalled lesson
  the way it treats any input — something to confirm against the current system, not a
  settled instruction. This matters most when the recalled "fact" traces back to an untrusted
  input an earlier run read.
- **Grow by appended deltas, never wholesale rewrite.** Durable records are extended with
  small, dated, itemized entries; re-summarizing a long record erodes the load-bearing detail
  (`context-window-discipline.md` §3, context collapse). Append the lesson; leave the rest
  alone.

---

## 5. Tool-agnostic

This page is discipline, not a product. The durable store can be an issue tracker, a docs
folder, a wiki, a database, or a vector store — the repo supplies *what* to remember, *how* to
retrieve it, and *how* to keep it honest, not the storage. Whatever backs it must preserve
provenance, support retrieval by relevance, and grow by appended entries; a store that loses
those properties has lost the point.

---

## 6. Exit criteria

Durable memory is working when:

1. A lesson, deficiency, or baseline survives the run that produced it, in a named place
   outside the transcript.
2. A later agent loads the relevant slice at Question/Discover/Plan — not the whole history,
   and not nothing.
3. Every durable entry carries evidence and a source, and is treated as a hypothesis on
   recall.
4. Durable records grow by appended deltas, not rewrites.
5. The store can change (a tool migration) without losing provenance, retrievability, or
   append-only growth.

---

## Source-lineage note

This page is an original Nuclear-grade operating doctrine and the persistent counterpart to
`context-window-discipline.md`. It draws on the same public context-engineering sources mapped
in [`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md)
(Tier 9) — in particular LangChain's persistent cross-run memory lifetime, the Agentic Context
Engineering (ACE) finding that incremental delta updates beat wholesale rewrites, and the
context-poisoning failure mode — together with the operating-experience and
configuration-management habits already used across this repo. No compliance claim is made.
