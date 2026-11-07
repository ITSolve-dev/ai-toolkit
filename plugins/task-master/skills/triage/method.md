# triage: method

Turn incoming, unread items into triaged ones: each gets an outcome, and an accepted item also gets a
kind, a rating and a size class. Nothing is cut and nothing is written to the board. Open a cited
page when a case is borderline. "This wiki's reading" below means the base marks the rule as its
own, not a source's.

## Inputs and output

- **Passed by the skill:** the snapshot (or a file of items passed as text), the metrics file (or
  `none`), the question, and the path of `.claude/task-master.toml`. No config means no board: skip
  the steps that need one, and record each one skipped in `not_covered`; with no commands to name,
  no changeset file is written and the proposals stay in `findings`.
- **`findings`:** one block per item, oldest first: item id (or `new-N` for a text item not on the
  board), outcome, kind, bands, size class, and the ops proposed for it by `ref`.
- **The changeset** goes to `.task-master/changeset-triage-<slug>.json` in the `board` method's form,
  each op with `why` (one line) and `page`, and an op on an existing task with its `updated_at`
  from the snapshot. Ops by what they do: type or priority, `set_type` or `set_priority`; a size,
  `add_label` where `[fields].estimate` is a `label:` form, else its own recorded command, else
  `needs_caller`; a `label:` marker, `add_label` or `remove_label` with its name without the prefix
  (a `status:` marker is a column: ask, do not propose it); a text edit, `edit` with the whole new
  text; a question to a reporter, `comment`; `link` of a `[links]` type; `close`, with `decide` and
  a `[board.close_reasons]` value; an accepted text item, `create`. An op whose key
  `[board.commands]` (or whose value `[links]`, `[board.close_reasons]`) lacks goes to
  `needs_caller`, not into the file.
- **Questions instead of assumptions:** a closing that rests on a fact only the requester holds,
  and a rating with no sentence behind it. Comments to reporters go in the changeset, not in
  `questions`.

## Steps

1. **Read the setup.** From the config: `[project].setup`, `process_doc`, `scale`, `scale_far`,
   `ceiling`, `sle`, `[markers]`, `[fields]`, `[labels.meaning]`, `[states]`, and which keys
   `[board.commands]` has. Read the process document if one is named. It may hold an assignment
   rule (step 10), a review interval (step 9) or the release rhythm (step 7). An item whose status is not in `[states]` is reported as unmapped and is not
   triaged as any kind.
   *Wrong if:* a later step uses a scale, ceiling or interval that this step found absent.

2. **Select and order.** Items carrying `[markers].untriaged`. With no marker declared: items of
   kind `before_start` with no priority set, because an absent rating means the item has not been
   reviewed (`wiki/intake/triage-procedure.md`, step 7). Say that the board cannot show the
   difference, and propose a marker for the process document in `needs_caller`. Order oldest first:
   by `age.items[].days` where its basis is `since_created`, else by the snapshot's `created_at`;
   text items as given. This is the order of triage, not of work (same page, step 2). If every
   request comes from the person steering and nothing else waits untriaged, steps 5 to 7 suffice.
   Otherwise run all the steps (same page, Cost; this wiki's reading).
   *Wrong if:* an age is computed here rather than read from the metrics.

3. **Close the cheap cases first** (`wiki/intake/triage-procedure.md`, Outcomes). A question or a
   request for help gets an answer or a redirect and no task. An item that is abandoned or in the
   wrong place gets a `close`, or one sentence on why it stays.
   *Wrong if:* an item reporting a failure is closed as a question.

4. **Look for a duplicate** among open and closed items (`wiki/intake/duplicate-reports.md`). Two
   reports are duplicates when one change would close both. Similar wording does not make them
   duplicates. Before the `close`, add a `comment` on the original carrying what the duplicate knows
   and the original lacks, then a `link` from the duplicate to it. A resubmission saying it was
   raised before is evidence about the original: report the original as stalled. An unclear case
   is proposed as a candidate, to be confirmed at reproduction. A defect in a task that is still
   open goes to that task, not to a new item. Under iterations that holds while the task's period
   is open; under flow it holds before the task's finish point
   (`wiki/intake/defect-inside-or-outside-the-iteration.md`).
   *Wrong if:* the close has no reference to the original, or a fact in the duplicate reaches
   neither the original nor a comment.

5. **Check the classification.** A requester's "bug" is a claim (`wiki/intake/triage-procedure.md`,
   step 5). Classify each item as defect, new behaviour, or placeholder (something possibly useful
   with nothing yet behind it, `wiki/ordering/incomparable-tasks.md`). Set the board's type only
   to a value the snapshot shows in use. Any other value goes to `needs_caller`.
   *Wrong if:* the kind follows the reporter's label when the text describes something else.

6. **Check the content and clarify.** A defect report must say how to reach the failure, what
   happened and what should have happened. An environment is required only if the failure depends
   on it (`wiki/intake/incoming-report-content.md`). A request for new behaviour says why it exists
   and what would show it done (`wiki/task-content/task-must-justify-itself.md`,
   `wiki/task-content/testable-acceptance.md`). A decision stranded in a comment cannot be seen:
   the snapshot carries no comments, so that check is `not_covered`
   (`wiki/task-content/conversation-moves-into-the-task.md`). Before asking, read the repository.
   Ask only what it cannot show, about behaviour and failure, in terms the reporter can answer
   (`wiki/intake/clarifying-questions.md`; `wiki/task-content/recoverable-versus-task-only-facts.md`).
   Send one `comment` per item holding all of its questions, and ask once
   (`wiki/intake/triage-procedure.md`, Outcomes). An item awaiting its answer keeps the untriaged
   marker and gets `[markers].waiting` if declared (this method's own rule). A defect cannot be
   reproduced from files. Give its steps in `needs_caller` and leave it accepted pending
   reproduction (`wiki/intake/reproduce-before-accepting.md`).
   *Wrong if:* a question's answer is in the repository, or the question is one nobody could
   answer ("any workarounds?").

7. **Rate what is accepted.** Rate value and urgency separately, one band each, and give each band
   one sentence (`wiki/ordering/ordering-by-value-and-urgency.md`). Value is how much the result
   would be worth now. Urgency is what share of that worth waiting would lose
   (`wiki/ordering/urgent-versus-important.md`). If the project ships in releases, an incoming
   defect or request is ASAP when it would block the release under way. Without releases, use the
   two ratings as they stand (same page). A date raises urgency only if something outside the
   project changes at it (`wiki/ordering/a-date-is-not-urgency.md`). An item nobody can rate is
   held outside the order as a placeholder, not forced into a band
   (`wiki/ordering/incomparable-tasks.md`). Propose the bands and their rank: the band belongs to
   the person steering (`wiki/ordering/ordering-by-value-and-urgency.md`, Agent executor note).
   *Wrong if:* a value sentence is about time or an urgency sentence is about size, or across the
   items the two bands always move together.

8. **Give a size class; do not cut.** Use the project's scale, `scale_far` for work not near
   starting (`wiki/sizing/estimating-by-horizon.md`). A vague item still gets a size, with its
   assumption stated (`wiki/sizing/estimating-underspecified-work.md`). The item needs cutting
   when it is above `ceiling`, or when its contents cannot be listed, whichever comes first. Under
   flow with no scale, ask whether it has a good chance of finishing within the SLE
   (`wiki/sizing/size-ceiling.md`). With no ceiling in the config, use the top of the near scale
   and say so (this method's own default, as in decompose). Mark such an item `needs cutting →
   decompose`. Do not list its pieces. The size is a proposal (`wiki/sizing/who-estimates.md`).
   *Wrong if:* the block for an item lists subtasks, or a size has no stated basis.

9. **Propose closing what no longer applies.** For an item that has stopped, ask what it waits for
   (`wiki/intake/closing-what-no-longer-applies.md`). If it awaits a requester's answer that never
   came, close it with a comment saying how to reopen. If it waits for nobody in particular, ask
   the requester whether the need still stands. If it is kept on purpose, it must say why and what
   would promote it, and one with no such statement is a candidate. How long is too long is the
   project's own: the metrics give no time since last activity, so use the review interval the
   process document states, against the item's age. None stated: leave the time unjudged, put the
   interval in `questions`, and use no borrowed figure (same page).
   *Wrong if:* a closing rests on a number of days the process document does not state.

10. **Assign only by a written rule.** By default an item is not assigned until it starts
    (`wiki/moving-work/tasks-are-not-assigned-at-planning.md`). If the process document states an
    assignment rule, apply it, cite the passage, and say once where the base disagrees.
    An assignment is an op only where `[board.commands]` records `assign`; otherwise it goes to
    `needs_caller`.
    *Wrong if:* an assignee appears in the changeset with no process-document passage behind it.

11. **Close each item's block.** An item whose outcome is decided gets `remove_label` for a
    `label:` untriaged marker; for a `status:` one, a `move` with `expected` to the status the
    process document names for triaged work, none named a question. Every `close` in the changeset carries `decide`: it is the person's decision
    (`wiki/intake/triage-procedure.md`, Who decides).
    *Wrong if:* an item from step 2 has no outcome and no question.
