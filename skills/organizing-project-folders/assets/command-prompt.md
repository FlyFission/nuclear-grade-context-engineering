```text
Build and check a folder/file layout.

Inputs:
- WBS or scope: <wbs.md path, or the deliverable to break down>
- paradigm: <production-codebase | agent-workflow-workspace>
- existing tree to respect: <paths or none>
- naming convention: lowercase, hyphen or underscore (pick one), ISO-8601 dates,
  one dot for the extension, no spaces or special characters

Do this in order:
1. Choose the paradigm. Production codebase: one root per deliverable, plus a
   small approved set of shared parts; the folder tree is the work breakdown
   laid out on disk. Agent workflow workspace: numbered stage folders (01_,
   02_), each with a context file that states its Inputs, Process, and Outputs;
   keep lasting reference material separate from per-run output; let scripts do
   the mechanical work; put a human review gate at each stage boundary.
2. Set the source of truth: derive folders from the work breakdown's outline
   numbers, or, if there is none, reverse-engineer the implied breakdown first.
3. For each proposed folder, answer the checklist: has it earned a folder? Does
   it hold together (one reason to change)? Does little leak out of it? Does it
   map to one part of the breakdown or one over-time rule? Does it have a single
   home? Is it named safely? Is it shallow enough? Is it documented?
4. Name and bound it: enforce the naming convention; ban misc/stuff/tmp/new/old/
   backup/final and a bare utils; cap depth near 8 levels and the path near 255
   characters.
5. Give each non-trivial folder a README or dictionary note, plus a note on what
   happens to it over time.
6. Reconcile with the existing tree; propose the smallest new structure; flag
   conflicts instead of overwriting.

Return: the folder map (work-breakdown outline number -> path, with an over-time
column), the per-folder notes, and a check of the naming, the depth, and the
single source of truth. Do not overwrite a baselined tree; propose it for review.
```
