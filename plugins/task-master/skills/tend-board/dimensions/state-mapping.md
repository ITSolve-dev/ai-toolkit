# Dimension: state-mapping

## What it looks for

Where the board's statuses and the kinds derived from them disagree, and how far it reaches: the
tool reports a mismatch on the first task it reads; this shows the extent. Findings per status.

- **Unmapped statuses** (`unmapped_statuses`): no category and no `[process.kinds]` entry. Give how
  many tasks sit in it (`counts.by_status`), left out of every other dimension.
- **Declared statuses the board lacks** (`mapping_unknown_statuses`): named in `review_statuses` or
  `[process.kinds]`, renamed or removed. List each task in `issues_without_status`.
- **A stop drawn as a state:** a status named Blocked, On Hold, Waiting or alike, holding a kind.
- **Markers the board cannot show** (`markers_undeclared`): a label `[board.labels]` does not
  declare, so `stuck` reads it as absent. One board-level question.
- **An entry against the category** (`mapping_sources`): an unfinished kind given to a `done` or
  `canceled` status, or `finished` to a `todo` one. The base has no page on tool categories; the
  snapshot cannot say whether the entry or the board is wrong.

**Scope:** the snapshot's mapping fields above and `marker_specs`; each task's `status`, `category`
and `kind`; `counts`. How a kind is derived: `skills/init/settings.md` under the plugin root.

## Read

- `wiki/work-states/distinguishable-work-states.md` — What the plugin can treat as canonical (five
  kinds and two markers, a classification and not a column list); Reading the result (criteria 2,
  3 and 9 break the numbers); Judging a Board's Columns ("no board police").
- `wiki/work-states/column-versus-attribute.md`, Sign of violation — a stop is an attribute.

## Not a finding

- A mapped status with no tasks; two statuses mapped to one kind; column names that differ from
  the kind names.
- A kind that differs from the category where the two are not opposite (an `in_progress` status
  declared `queued` or `handed_off`): categories are coarser than kinds.

## Finding shape

The README's shape, per status. Name no kind for an unmapped status: ask which kind it is, or
whether it is an attribute drawn as a column. For a stop drawn as a state, say counting may be
affected. Nothing goes on the board: each finding goes to `needs_caller` (a board category, or
`[process.kinds]`, `review_statuses`, `[board.labels]` through `init`) or to `questions`.
