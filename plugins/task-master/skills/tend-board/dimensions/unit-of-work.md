# Dimension: unit-of-work

## What it looks for

A task that fails one of the charter's two tests: once started, it finishes without waiting; its
result is presented once.

- **A known wait in the text:** the scope includes getting something from an outside party and also
  building on it, or needs a decision only another person can make during the work.
- **A known wait on the board:** an `active` task marked blocked or waiting on a dependency its text
  already named. The stop itself is `stuck`'s; here the finding is the cut.
- **Separable parts:** parts, or acceptance criteria, that could each be delivered alone; or a
  catch-all titled by one broad quality of the whole product.

**Scope:** open tasks of kind `before_start`, `queued`, `active`, `handed_off`: title, description,
`markers`, `subtasks`. A task with subtasks only groups; judge its leaves. An empty `subtasks` in a
composed snapshot: judge the task as a leaf and say so in `assumptions`.

## Read

- `wiki/cutting-work/unit-of-work.md` — The working tests, and A task that fails (what each failure
  calls for).
- `wiki/ordering/sequence-versus-wait.md` — Sign of violation; A handoff at the end is not a wait
  inside; The rule that follows (cut at the wait).
- `wiki/cutting-work/compound-task-text-signs.md` — Sign of violation (conjunctions, plurals and
  generic terms are signals to look, not the sign; "when"/"if" and "and" inside one result are not
  signs) and Catch-All Task.

## Not a finding

- A handoff after the executor's part is done, such as review by the person steering.
- A condition on releasing or enabling the result rather than on building it (read as a handoff at
  the end; not from the base).
- A quality with a threshold: a legitimate task, not a catch-all.
- A hold written in the task's Boundaries ("Not to start until <party> delivers…"): `decompose`
  kept it whole on purpose. If the task is `active`, ask whether it started before the delivery.
- A "can ship alone" or "presented once" verdict in Boundaries, unless a marker or the history
  shows the parts delivered separately.
- A thin `before_start` task: its cut is checked, its missing detail is not
  (`wiki/task-content/conversation-moves-into-the-task.md`, When to do it).
- A decision the text points at but does not hold: `unwritten-decisions`. This dimension takes a
  wait only when the text names who outside holds it.

## Finding shape

The common shape (README), naming the test failed and the wait or the separable parts. Propose a
re-cut through `decompose`; tend-board does not cut. For a known wait, say the part after it becomes
a task that starts once the outside party delivers. For an `active` task the re-cut is the person's
decision.
