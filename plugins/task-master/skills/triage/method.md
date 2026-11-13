# triage: method

Turn incoming, unread items into triaged ones: each gets an outcome, and an accepted item also gets
a kind, a value and an urgency band, and a size class. Nothing is cut and nothing is written to the
board. Start from `wiki/intake/triage-procedure.md`: its procedure is the order below and its
*Outcomes* table is the set of outcomes. Every outcome, band and size cites the page it rests on.

## Inputs and output

- **Passed:** the snapshot (or a file of text items), the metrics file (or `none`), the question,
  and the settings path. The question says which ops, link relations and close reasons the tool's
  help shows a way for. No settings means no board: skip what needs one, list each skipped step in
  `not_covered`, write no changeset, and keep the proposals in `findings`.
- **`findings`:** one block per item, oldest first: id (or `new-N` for a text item), outcome, kind,
  bands with their sentences, size class, and the `ref` of each op proposed for it.
- **The changeset** at `.task-master/changeset-triage-<slug>.json`, each op with `why`, `page` and,
  on an existing task, `updated_at`; all task text in `.task-master/body-<ref>.md`:

  | Proposal | Op |
  |---|---|
  | type or priority | `set_type`, `set_priority`, each with `decide` |
  | size | `add_label` of its `[board.size]` key; no `[board.size]`: reported, not applied |
  | a `label:` marker in `marker_specs` | `add_label` / `remove_label`, name without the prefix |
  | a `status:` marker | `move` with `expected`, to the status the process document names; none named: ask |
  | new text | `edit` with the whole text |
  | a question to a reporter | `comment` (not in `questions`) |
  | a relation | `link` with `blocks`, `duplicates` or `relates` |
  | closing | `close` with `decide` and reason `done`, `duplicate` or `abandoned` |
  | an accepted text item | `create` |

  An op, relation or reason the question says the tool lacks goes to `needs_caller`.
- **Questions instead of assumptions:** a closing that rests on a fact only the requester holds,
  and a rating with no sentence behind it.

## Process

1. **Read the setup.** From the settings: `[process].setup`, `doc`, `ceiling`, `sle`,
   `[process.markers]`, `[board.size]`, `[board.labels]`; from the snapshot, `marker_specs` and
   `markers_undeclared`. Read the process document if named: it may hold an assignment rule, a
   review interval or the release rhythm. A later step never uses a scale, ceiling or interval this
   step found absent. An item with a null kind is reported as unmapped, not triaged.
2. **Select and order.** Items carrying the untriaged marker. If that marker is in
   `markers_undeclared`: items of kind `before_start` with no priority (triage-procedure, step 7),
   saying the board cannot show the difference, with a marker proposed in `needs_caller`. Oldest
   first, by `age.items[].days` where its basis is `since_created`, else the snapshot's
   `created_at`; never compute an age. If every request comes from the person steering and nothing
   else waits, steps 5 to 7 suffice (triage-procedure, Cost).
3. **Close the cheap cases first** — triage-procedure, *Outcomes*. An item reporting a failure is
   never closed as a question.
4. **Look for a duplicate** among open and closed items — read `wiki/intake/duplicate-reports.md`
   (the test, the kinds, and what to carry before the close). A defect in a task still open goes to
   that task — read `wiki/intake/defect-inside-or-outside-the-iteration.md`.
5. **Check the classification** — triage-procedure, step 5. Classify as defect, new behaviour, or
   placeholder (`wiki/ordering/incomparable-tasks.md`). Set the board's type only to a value the
   snapshot shows in use; any other goes to `needs_caller`.
6. **Check the content and clarify.** Read `wiki/intake/incoming-report-content.md` (defects),
   `wiki/task-content/task-must-justify-itself.md` and `wiki/task-content/testable-acceptance.md`
   (new behaviour), `wiki/intake/clarifying-questions.md` and
   `wiki/task-content/recoverable-versus-task-only-facts.md` (what to ask, and only what the
   repository cannot show). A decision stranded in a comment cannot be seen: the snapshot carries
   no comments, so that check is `not_covered` (`wiki/task-content/conversation-moves-into-the-task.md`).
   One `comment` per item holding all its questions. An item awaiting its
   answer keeps the untriaged marker and gets the waiting marker if declared (not from the base).
   A defect cannot be reproduced from files: give its steps in `needs_caller` and leave it accepted
   pending reproduction (`wiki/intake/reproduce-before-accepting.md`).
7. **Rate what is accepted.** Read `wiki/ordering/ordering-by-value-and-urgency.md`,
   `wiki/ordering/urgent-versus-important.md` and `wiki/ordering/a-date-is-not-urgency.md`: one
   band each for value and urgency, each with one sentence. An item nobody can rate is a placeholder
   outside the order. The bands are proposals: they belong to the person steering.
8. **Give a size class; do not cut.** Read `wiki/sizing/estimating-by-horizon.md`,
   `wiki/sizing/estimating-underspecified-work.md`, `wiki/sizing/size-ceiling.md` and
   `wiki/sizing/who-estimates.md`. Use `[board.size]`, with the basis stated. Mark `needs cutting →
   decompose` when the item is above `ceiling` or its contents cannot be listed; never list its
   pieces. No `ceiling` in the settings: ask, and meanwhile take the `[board.size]` step below the
   largest, saying so (not from the base).
9. **Propose closing what no longer applies** — read `wiki/intake/closing-what-no-longer-applies.md`.
   The metrics give no time since last activity, so judge staleness only against a review interval
   the process document states; none stated, put the interval in `questions` and use no borrowed
   figure.
10. **Assign only by a written rule** — read `wiki/moving-work/tasks-are-not-assigned-at-planning.md`.
    A process-document rule wins: cite the passage and say once where the base disagrees. An
    assignment is an op only where the question says the tool can assign; else `needs_caller`.
11. **Close each item's block.** An item whose outcome is decided leaves the untriaged marker, by
    the table above. Every item from step 2 ends with an outcome or a question.

## Common pitfalls

- **Don't** follow the reporter's label when the text describes something else. **Do** classify by
  the text.
- **Don't** let a value sentence talk about time, or an urgency sentence about size.
- **Don't** propose a `close`, `set_priority` or `set_type` without `decide`: closing, rating and
  type are the person's decision (triage-procedure, *Who decides*).
- **Don't** ask what the repository already shows, or what nobody could answer ("any workarounds?").
