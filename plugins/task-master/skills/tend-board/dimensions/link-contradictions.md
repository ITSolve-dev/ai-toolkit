# Dimension: link-contradictions

Which linked tasks sit in states the link rules out? Read `README.md`, *Every dimension*, first.

**Reads:** every task's `kind`, `parent`, `subtasks`, `links` (the types `[links].blocks`,
`[links].blocked_by`, `[links].relates`; one the config lacks: its step is `not_covered`), `markers`.

## Steps

1. **Parent finished, child open.** A task of kind `finished` whose subtask is not, or a subtask whose
   parent is finished: finding. The source's example is "A is a linked as a sub-task of B, but B is
   closed and A is still open." (`wiki/moving-work/what-may-move.md`, Sign of violation). The sign
   shows that a move ignored a stated relation; it does not show which task is wrong.
2. **Finished before what it was blocked by.** A `finished` task linked `blocked_by` a task that is
   not finished, or an open task marked blocked whose every `blocked_by` task is finished: finding
   (this method's own application of the same sign to blocking links).
3. **Started while blocked.** A task of kind `active` linked `blocked_by` an unfinished task, with no
   blocked marker: question, whether the link is stale or the start ignored it (this method's own
   application).
4. **Ask which side is wrong.** Propose a question per pair: close the child or reopen the parent,
   drop a stale link or mark the stop. Never choose, and propose no move: the question carries both
   options.
   Practitioners split on whether out-of-sync status matters (same page, two of 10 disagreed), so
   apply the smell check strictly.

## Not a finding

- A `relates` link between tasks in any states.
- A `duplicates` or `duplicated_by` link: the `duplicates` dimension owns every one.
- A cancelled parent with open children the process document says are kept on purpose.
- An empty `links`, `subtasks` or null `parent`: in a composed snapshot the tool may not have read
  them; record under `not_covered` which of them the snapshot lacks, never infer no link.
