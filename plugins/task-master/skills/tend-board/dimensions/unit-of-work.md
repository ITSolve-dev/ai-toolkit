# Dimension: unit-of-work

Which task fails one of the two tests: once started, it finishes without waiting; its result is
presented once? Read `README.md`, *Every dimension*, first.

**Reads:** open tasks of kind `before_start`, `queued`, `active`, `handed_off`: title, description,
`markers`, `subtasks`. The tests are the charter's own (`wiki/cutting-work/unit-of-work.md`, The
working tests).

## Steps

1. **Leave out the group nodes.** A task with subtasks only groups; its leaves are the units.
   An empty `subtasks` in a composed snapshot may mean not read: then judge the task as a leaf and
   say so in `assumptions`.
2. **First test, in the text.** A task whose scope includes getting something from an outside party
   and also building on it holds a known wait (`wiki/ordering/sequence-versus-wait.md`, Sign of
   violation). So does one whose text needs a decision only another person can make during the
   work (`wiki/cutting-work/unit-of-work.md`, The working tests).
   *Wrong if:* a predecessor finished first, or review of the presented result, is read as a wait.
3. **First test, on the board.** An `active` task marked blocked or waiting on a dependency its text
   already named: the wait was knowable when it was cut (`wiki/ordering/sequence-versus-wait.md`,
   Sign of violation, history sign read from the current marker). The stop itself is `stuck`'s; here
   the finding is the cut.
4. **Second test.** Conjunctions ("and", "or"), separators, unnamed plurals and generic terms in the
   title or text are signals to look, not the sign. The sign is parts that could each be delivered
   alone, including acceptance criteria that could each ship alone
   (`wiki/cutting-work/compound-task-text-signs.md`, Sign of violation). A title whose substance is
   one broad adjective for the whole product is a catch-all (same page, Catch-All Task). A
   "can ship alone" or "presented once" verdict in Boundaries stands unless a marker, the history
   or a later comment shows the parts delivered separately.
5. **Propose** a re-cut through `decompose`, naming the wait or the separable parts; tend-board does
   not cut (`wiki/cutting-work/unit-of-work.md`, A task that fails). For a known wait, the part
   after it becomes a task that starts once the outside party delivers
   (`wiki/ordering/sequence-versus-wait.md`, The rule that follows). For an `active` task the re-cut
   is the person's decision.

## Not a finding

- A handoff after the executor's part is done, such as review by the person steering
  (`wiki/ordering/sequence-versus-wait.md`, A handoff at the end is not a wait inside).
- "When" or "if" stating a condition inside one behaviour; "and" joining two parts of one result
  (`wiki/cutting-work/compound-task-text-signs.md`, Sign of violation).
- A condition on releasing or enabling the result, not on building it (this method's reading,
  as in `decompose`, of the handoff-at-the-end section).
- A quality with a threshold: a legitimate task, not a catch-all.
- A task whose Boundaries read "Not to start until <party> delivers…": `decompose`'s hold, kept
  whole because nothing before the wait has anything to show (its step 5). If it is `active`, ask
  whether it started before the delivery.
- A thin `before_start` task: detail closes as the task nears its start
  (`wiki/task-content/conversation-moves-into-the-task.md`, When to do it). Its cut is still
  checked; its missing detail is not.
- A decision the text points at but does not hold ("as discussed", "TBD"): `unwritten-decisions`.
  This dimension takes a wait only when the text names who outside holds it.
