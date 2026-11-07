# Dimension: unwritten-decisions

Which task points at a decision its text does not hold? Before an agent starts, every decision the
task depends on is made and written, or explicitly left to the executor
(`wiki/task-content/conversation-moves-into-the-task.md`, The rule). Read `README.md`, *Every
dimension*, first.

**Reads:** tasks of kind `queued`, `active`, `handed_off`: title and description. Comments only if
the snapshot carries them.

## Steps

1. **Take the stage.** The deadline for closing a task is the moment an agent would take it
   (`wiki/task-content/conversation-moves-into-the-task.md`, When to do it). So `queued` tasks are in
   scope, and `active` or `handed_off` ones are stronger findings: the run already guessed.
2. **Find the pointer.** The text refers to a conversation or memory it does not contain: "as
   discussed", "TBD", "details to follow", "the usual way", "handle edge cases appropriately", or
   their equivalent in the task's language (same page, Sign of violation). The words are in the text,
   so the sign does not rest on a missing field.
3. **Check it is task-only.** A pointer to something the executor can recover by reading the
   repository, or to a linked document that holds the decision, is not a gap
   (`wiki/task-content/recoverable-versus-task-only-facts.md`, The decision). Expected behaviour,
   constraints and choices that live in someone's head are task-only.
4. **Comments, if present.** A decision recorded in a comment that contradicts or is missing from
   the text is a fact stranded outside the task (same page, Fact Stranded Outside the Task). If the
   snapshot has no comments, put this check under `not_covered`.
5. **Propose** a question to the person who holds the decision, naming the phrase and what it leaves
   open, and a text edit once answered. Never fill in the decision.

## Not a finding

- A `before_start` task left thin: it closes as it nears the start (step 1).
- A decision explicitly left to the executor ("implementer's choice").
- "TBD" or similar inside quoted logs, code or a copied report.
- A link to a written decision the executor can open.
- A wait on a named outside party: `unit-of-work`. A missing check of done: `acceptance`.
