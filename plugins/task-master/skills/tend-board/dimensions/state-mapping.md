# Dimension: state-mapping

Where do the board's statuses and the kinds derived from them disagree, and how far does it
reach? The tool names a mismatch on the first task it reads; this dimension shows its extent across
the scope (design, "Агенты"). Read `README.md`, *Every dimension*, first. Findings are per status.

**Reads:** the snapshot's `mapping`, `mapping_sources`, `unmapped_statuses`,
`mapping_unknown_statuses`, `issues_without_status`, `marker_specs`, `markers_undeclared`, each
task's `status` (with its `category`) and `kind`; `counts.by_status`, `counts.unmapped`. How a kind
is derived: `${CLAUDE_PLUGIN_ROOT}/skills/init/settings.md`, How a task's kind is decided.

## Steps

1. **Unmapped statuses.** Each entry of `unmapped_statuses` is a status the board shows with no
   category and no entry in `[process.kinds]`: a finding with how many tasks sit in it
   (`counts.by_status`), and that those tasks were left out of every other dimension. Name no kind
   for it: it is reported, never guessed (`wiki/work-states/distinguishable-work-states.md`, What
   the plugin can treat as canonical; the design's "Значение состояний принадлежит плагину"). The
   question is which kind it is, or whether it is an attribute drawn as a column (step 3).
2. **Declared statuses the board lacks.** Each `mapping_unknown_statuses` entry is a status
   `review_statuses` or `[process.kinds]` names and the board lacks: renamed or removed. Finding,
   with `needs_caller`. Each task in `issues_without_status` is listed: its state cannot be read.
3. **A stop drawn as a state.** A status named Blocked, On Hold, Waiting or alike, with a kind:
   a stop is an attribute marked on the task where it stands, not a column
   (`wiki/work-states/column-versus-attribute.md`, Sign of violation). Ask whether it should be a
   marker; counting may be affected, so say so
   (`wiki/work-states/distinguishable-work-states.md`, Reading the result: criteria 2, 3 and 9
   break the numbers).
4. **Markers the board cannot show.** Each `markers_undeclared` entry is a marker whose label
   `[board.labels]` does not declare: until it does, `stuck` reads that marker as absent. One
   board-level question (`wiki/work-states/distinguishable-work-states.md`, The distinctions).
5. **An entry against the category.** A `[process.kinds]` entry (`mapping_sources`) giving an
   unfinished kind to a `done` or `canceled` status, or `finished` to a `todo` one: question; the
   entry or the board is wrong, and the snapshot cannot say which (this method's own rule; the base
   has no page on tool categories).
6. **Propose.** Nothing on the board. Each finding goes to `needs_caller` (a category on the board
   or `[process.kinds]`, `review_statuses`, `[board.labels]`, through `init`) or to `questions`;
   changing the board's columns is the team's choice
   (`wiki/work-states/distinguishable-work-states.md`, Judging a Board's Columns: no "board police").

## Not a finding

- A mapped status with no tasks in it.
- Two statuses mapped to one kind: the five kinds are a classification, not a column list
  (`wiki/work-states/distinguishable-work-states.md`).
- A board whose column names differ from the plugin's kind names.
- A kind that differs from the category where the two are not opposite (an `in_progress`
  status declared `queued` or `handed_off`): the tool's categories are coarser than the kinds.
