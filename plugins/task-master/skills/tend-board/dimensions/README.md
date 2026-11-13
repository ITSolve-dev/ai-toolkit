# tend-board: dimensions

One file per dimension; `board-inspector` follows one per run, after *Every dimension* below.

| Dimension | The question it asks | Metrics it reads | Native history | Owns |
|---|---|---|---|---|
| [`stuck`](stuck.md) | Which started task has stopped or outlived its expectation, and nobody has acted? | `age`, `cycle_time`, `sle` | Uses it for Work Item Age; without it runs on age since creation and says so | Age and stop signs |
| [`wip-limit`](wip-limit.md) | Is more started than the project's bound allows? | `limits`, `wip` | No | Counts per state or kind past the started point |
| [`acceptance`](acceptance.md) | Which task near or in work states no check of done? | `missing_acceptance_criteria`, `counts` | No | Missing or untestable criteria |
| [`duplicates`](duplicates.md) | Which tasks are one defect or one change, and which duplicate closings lost a fact or a reference? | `counts` | No | Every `duplicates` link and pair |
| [`state-mapping`](state-mapping.md) | Where do the board's statuses and the kinds derived from them disagree, and how far does it reach? | `counts` | No | Unmapped statuses and tasks |
| [`unit-of-work`](unit-of-work.md) | Which task fails one of the two tests: finishes without waiting, presented once? | none | No | Waits inside a task, criteria that stand alone |
| [`unwritten-decisions`](unwritten-decisions.md) | Which task points at a decision its text does not hold? | none | No | References to talk, memory, "TBD" |
| [`link-contradictions`](link-contradictions.md) | Which linked tasks sit in states the link rules out? | none | No | Parent, subtask and blocking links |

## Every dimension

1. **Read the inputs**: the question file, the whole `[process]` section of the settings, and the
   process document if named. Then the pages the dimension lists under *Read*; every finding cites
   one. A case none settles: say the base has no page on it.
2. **Leave out unmapped tasks** (null `kind`): they are `state-mapping`'s; say how many
   (`counts.unmapped`). Tasks examined: `counts.by_kind` over the kinds read, or `counts.total`.
3. **Pass each sign through `wiki/reading-history/smell-is-not-a-finding.md`**, The rule. A pattern
   the process document declares intended is not reported; a survivor is a question to the people
   steering.
4. **Stay inside the dimension**: a sign another dimension owns (table) is left to it.
5. **Read empty fields with care.** In a composed snapshot an empty `links`, `subtasks` or null
   `parent` may mean not read: `not_covered`, never "no link". Comments are never in the snapshot.
6. **Propose only what `board` can apply**, each op with `why`, `page`, and `updated_at` from the
   snapshot on an edit, label or close: `comment`; `edit` with the whole new text; `add_label` for a
   `label:` marker in `marker_specs` (name without the prefix); `link` (`id` <relation> `other`)
   with `blocks`, `duplicates` or `relates`; `close` with `decide` and reason `done`, `duplicate` or
   `abandoned`. A `status:` marker is a column: a `move` with `expected`, to the status the process
   document names; none named: ask. All task text goes to `.task-master/body-<ref>.md`. A re-cut
   is no op: name `decompose`. Never invent content the task lacks: ask, or draft it marked for
   the requester to confirm.

## Finding shape

One per task (per status or board for state-level dimensions); several signs on a task make one:
task id and title; the sign; the page and section; what the sign does not establish; the question
or the op's `ref`. **No findings is a result:** return `status: done`, `findings: no findings`, how
many tasks were examined and which were left out and why.
