# Dimension: unwritten-decisions

## What it looks for

A task whose text points at a decision it does not hold: "as discussed", "TBD", "details to
follow", "the usual way", "handle edge cases appropriately", or their equivalent in the task's
language. The words are in the text, so the sign does not rest on a missing field.

**Scope:** tasks of kind `queued`, `active`, `handed_off`: title and description. `active` and
`handed_off` are the stronger case: the run already guessed.

## Read

- `wiki/task-content/conversation-moves-into-the-task.md` — The rule (every decision made and
  written, or explicitly left to the executor), Sign of violation, When to do it (the deadline is
  the moment an agent would take the task), and *Fact Stranded Outside the Task*.
- `wiki/task-content/recoverable-versus-task-only-facts.md`, The decision — a pointer to what the
  executor can recover from the repository, or to a linked document holding the decision, is not a
  gap.

A decision recorded in a comment and missing from the text is a stranded fact, but the snapshot
carries no comments: that check goes under `not_covered`.

## Not a finding

- A `before_start` task left thin.
- A decision explicitly left to the executor ("implementer's choice").
- "TBD" or similar inside quoted logs, code or a copied report.
- A link to a written decision the executor can open.
- A wait on a named outside party: `unit-of-work`. A missing check of done: `acceptance`.

## Finding shape

The common shape (README), quoting the phrase and saying what it leaves open. Propose a question to
the person who holds the decision, and a text `edit` once answered. Never fill in the decision.
