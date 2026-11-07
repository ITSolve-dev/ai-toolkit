# Dimension: state-mapping

Where do the board's statuses and the project's mapping disagree, and how far does it reach? The
tool names a mismatch on the first task it reads; this dimension shows its extent across the scope
(design, "Агенты"). Read `README.md`, *Every dimension*, first. Findings are per status.

**Reads:** the snapshot's `mapping`, `unmapped_statuses`, `mapping_unknown_statuses`,
`issues_without_status`, `markers_unreadable`, each task's `status` (with its `category`) and
`kind`; `counts.by_status`, `counts.unmapped`; the config's `[states]`, `[markers]` and
`[board.categories]`.

## Steps

1. **Unmapped statuses.** Each entry of `unmapped_statuses` is a finding: the status, how many tasks
   sit in it (`counts.by_status`), and that those tasks were left out of every other dimension. Name
   no kind for it: a status missing from the mapping is reported, never guessed
   (`wiki/work-states/distinguishable-work-states.md`, What the plugin can treat as canonical; the
   design's "Значение состояний принадлежит плагину"). The question is which of the five kinds it
   is, or whether it is an attribute drawn as a column (step 3).
2. **Stale mapping.** Each `mapping_unknown_statuses` entry is a status the config maps and the board
   lacks: renamed or removed. Finding, with `needs_caller`: the mapping is redone through `init`.
   Each task in `issues_without_status` is listed: its state cannot be read at all.
3. **A stop drawn as a state.** A status named Blocked, On Hold, Waiting or alike, mapped to a kind:
   a stop is an attribute marked on the task where it stands, not a column
   (`wiki/work-states/column-versus-attribute.md`, Sign of violation). Ask whether it should be a
   marker; counting may be affected, so say so
   (`wiki/work-states/distinguishable-work-states.md`, Reading the result: criteria 2, 3 and 9
   break the numbers).
4. **Kinds the board cannot show.** No `[markers].blocked` (or `waiting`) in the config: the board
   cannot tell a stopped task from a moving one, so `stuck` reads markers as absent. A marker in
   `markers_unreadable` is declared in a form the scripts cannot read: `needs_caller`. One board-level
   question (`wiki/work-states/distinguishable-work-states.md`, The distinctions).
5. **Mapping against the tool's category.** A status whose category `[board.categories]` calls
   `finished` mapped to an unfinished kind, or one it calls `unstarted` mapped to `finished`:
   question; the mapping or the board is wrong, and the snapshot cannot say which (this method's
   own rule; the base has no page on tool categories). No `[board.categories]`: `not_covered`.
6. **Propose.** Nothing on the board. Each finding goes to `needs_caller` (correct `[states]` or
   `[markers]` through `init`) or to `questions`; changing the board's columns is the team's choice
   (`wiki/work-states/distinguishable-work-states.md`, Judging a Board's Columns: no "board police").

## Not a finding

- A mapped status with no tasks in it.
- Two statuses mapped to one kind: the five kinds are a classification, not a column list
  (`wiki/work-states/distinguishable-work-states.md`).
- A board whose column names differ from the plugin's kind names.
- A tool category that differs from the kind where the two are not opposite (a `started`
  category mapped to `queued` or `handed_off`): the tool's categories are coarser than the kinds.
