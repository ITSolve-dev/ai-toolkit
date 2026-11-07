# Dimension: wip-limit

Is more started than the project's bound allows? Read `README.md`, *Every dimension*, first.
Findings here are per status or kind and per board, not per task.

**Reads:** `[project].wip_control`; `limits` (`declared`, `breaches`, `unknown_keys`) and `wip`,
each with its `basis`. A status limit counts every issue in that status, whatever its kind.

## Steps

1. **Is a bound stated?** `limits.declared` true: go to step 2 (beside `wip_control = false` the
   config contradicts itself: `needs_caller`). `wip_control = true` with no `[limits]`: a bound is
   stated but its numbers are not written; one board-level question asking that the process
   document hold them, then stop. Neither:
   - flow: one board-level finding. A flow setup requires a bound,
     because it is the only start signal (`wiki/moving-work/wip-control.md`, Which holds under which
     setup);
   - iterations: one board-level question, not a defect. Where `[project].executor` is `agent`
     or `mixed`, the
     period restrains the total and not the moment, so the base suggests adding a bound
     (`wiki/moving-work/board-rules-by-setup.md`, Agent executor note). If the process document
     records the choice, say nothing (`wiki/reading-history/smell-is-not-a-finding.md`, step 5).
   Stop here when no bound is stated.
2. **Each breach is a finding**: the key, its scope (status or kind), the limit and the count,
   copied from `limits.breaches` (`wiki/moving-work/wip-control.md`, Sign of violation, board
   state). A count at the limit is not over it.
3. **Check for a declared exception.** An excess the process document allows in advance (an
   expedite, a named class of work) is not a finding
   (`wiki/moving-work/wip-control.md`, The rule). An expedite lane with its own limit is counted
   against that limit, not the board's (`wiki/moving-work/expedite-lane.md`).
4. **Blocked tasks count.** If the process document excludes blocked tasks from the count, follow it
   and say once where the base disagrees: a stop that leaves the count stops nothing
   (`wiki/moving-work/blocked-work-counts-against-wip.md`, Why). The metrics count by position, so
   the breach list already includes them; never subtract them yourself.
5. **Stale keys.** Each `limits.unknown_keys` entry names a limit matching no status or kind: put it
   in `needs_caller` (the config needs correcting), not as a finding about the board.
6. **Propose.** For a breach: a question to the people steering on what finishes first, and that
   nothing new starts in that state until the count is under the bound
   (`wiki/moving-work/what-may-move.md`, Kanban Guide: a capacity signal). Never a move.

## Not a finding

- A count at or under the limit, or no limit on a state the bound does not cover when a
  workflow-wide bound exists (`wiki/moving-work/wip-control.md`: one number for the span is an
  allowed form).
- Tasks of a kind outside `[project].started_kinds` against the workflow total: WIP is between
  the started and finished points only (`wiki/moving-work/wip-control.md`); `wip` counts by that
  key. A limit the project set on
  a queued status is still checked, through step 2.
- Running under the bound: its sign needs history over time, which a snapshot does not show.
- Which tasks are old or stopped: that is `stuck`.
