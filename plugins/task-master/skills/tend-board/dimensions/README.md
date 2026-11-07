# tend-board: dimensions

One file per dimension; `board-inspector` follows one of them per run. Read this file's
*Every dimension* section first: it holds the steps all eight share.

| Dimension | The question it asks | Metrics it reads | Native history | Owns |
|---|---|---|---|---|
| [`stuck`](stuck.md) | Which started task has stopped or outlived its expectation, and nobody has acted? | `age`, `wip` | Uses it for time in state; without it runs on age since creation and says so | Age and stop signs |
| [`wip-limit`](wip-limit.md) | Is more started than the project's bound allows? | `limits`, `wip` | No | Counts per state or kind |
| [`acceptance`](acceptance.md) | Which task near or in work states no check of done? | `missing_acceptance_criteria`, `counts` | No | Missing or untestable criteria |
| [`duplicates`](duplicates.md) | Which tasks are one defect or one change, and which duplicate closings lost a fact or a reference? | `counts` | No | Every `duplicates` link and pair |
| [`state-mapping`](state-mapping.md) | Where do the board's statuses and the project's mapping disagree, and how far does it reach? | `counts` | No | Unmapped statuses and tasks |
| [`unit-of-work`](unit-of-work.md) | Which task fails one of the two tests: finishes without waiting, presented once? | none | No | Waits inside a task, criteria that stand alone |
| [`unwritten-decisions`](unwritten-decisions.md) | Which task points at a decision its text does not hold? | none | No | References to talk, memory, "TBD" |
| [`link-contradictions`](link-contradictions.md) | Which linked tasks sit in states the link rules out? | none | No | Parent, subtask and blocking links |

**Adding one.** A dimension exists only where a base page states a rule with a sign readable from a
snapshot (the design's rule for growth). Its file names that page at each step, says what does not
count, and gets a row here. A rule whose sign needs a status transition list, which the snapshot
does not carry (backward moves, `wiki/moving-work/backward-movement.md`), or a per-assignee count,
which the metrics do not compute (`wiki/moving-work/wip-per-executor.md`), waits for that data.

## Every dimension

1. **Read the inputs.** The question file names the dimension, the scope, the config path and the
   process document. Read `[project].setup` from the config: dimension steps branch on it. Tasks
   whose `kind` is null belong to `state-mapping`; every other dimension leaves them out and says
   how many it left (from `age.skipped_unmapped` or `counts.unmapped`).
2. **Pass each sign through the smell check** before it becomes a finding
   (`wiki/reading-history/smell-is-not-a-finding.md`, The rule): is it prevented by the stated
   workflow, intended by it, or limited to a stage, kind or property the task is outside? A pattern
   the process document declares intended is not reported. A survivor is a question to the people
   steering, carrying what the sign does not establish.
3. **One finding per task** (or per status, for state-level dimensions): the task id and title, the
   sign seen, the page it rests on, what it does not establish, and the question or proposed
   change. Several signs on one task make one finding listing them.
4. **Stay inside the dimension.** A sign another dimension owns (table above) is left to it.
5. **Propose only what the `board` skill can apply**: a comment, a marker or label, a link, a text
   edit, a move. Closing, cancelling and re-cutting are proposed as a person's decision; a re-cut
   names `decompose`. Nothing invents content the task lacks (criteria, a decision, a kind): it
   drafts a question, or a draft marked for the requester to confirm.
6. **No findings is a result.** On a board in order the right answer is none. Return `status: done`
   with `no findings`, how many tasks were examined and which were left out and why, so an empty
   answer cannot be read as a dimension that did not run.

*Wrong if:* a finding has no page, a finding restates another dimension's sign, or a sign the
process document declares intended is reported.
