# Dimension: wip-limit

## What it looks for

More started than the project's bound allows. Findings are per status or kind, or per board, not
per task.

- **No bound stated** (`limits.declared` false, no `[process.wip]`). Then stop: there is nothing to
  count against.
- **A breach:** each entry of `limits.breaches`, copied as given: the key, its scope (status or
  kind), the limit and the count. A count at the limit is not over it.
- **Stale keys:** each `limits.unknown_keys` entry names a limit matching no status or kind.

**Scope:** `limits` (`declared`, `breaches`, `unknown_keys`) and `wip`, each with its `basis`. A
status limit counts every task in that status, whatever its kind. The metrics count by position, so
blocked tasks are already in the breach list; never subtract them yourself.

## Read

- `wiki/moving-work/wip-control.md` — The rule (an exception is stated in advance), Sign of
  violation, and Which holds under which setup (flow requires a bound; iterations with an agent
  executing should add one).
- `wiki/moving-work/board-rules-by-setup.md`, Agent executor note — why the period does not restrain
  the moment.
- `wiki/moving-work/expedite-lane.md` — an expedite lane with its own limit counts against that
  limit, not the board's.
- `wiki/moving-work/blocked-work-counts-against-wip.md`, Why — blocked tasks count. If the process
  document excludes them, follow it and say once where the base disagrees.
- `wiki/moving-work/what-may-move.md`, Kanban Guide: a capacity signal — what a breach asks for.

## Not a finding

- No bound under iterations: a board-level question, not a defect; and nothing at all if the
  process document records the choice.
- A count at or under the limit, or no limit on a state when a workflow-wide bound exists.
- An excess the process document allows in advance (an expedite, a named class of work).
- Unstarted tasks (outside `wip.started_statuses`) against the workflow total. A limit the project
  set on a queued status is still checked.
- Running under the bound: its sign needs history over time, which a snapshot does not show.
- Which tasks are old or stopped: that is `stuck`.

## Finding shape

No bound under flow: one board-level finding. Each breach: the common shape (README) per key, with
a question to the people steering on what finishes first, and that nothing new starts in that state
until the count is under the bound. Never a move. Stale keys go to `needs_caller`:
`[process.wip]` needs correcting.
