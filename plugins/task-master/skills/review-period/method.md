# review-period: method

A past period in; what was promised, what came out, and what explains the difference. Read the
question file first: it names the period, the setup, any earlier snapshot, and what the skill has
already ruled out. Each comparison and cause cites the page it rests on.

## Inputs and output

- **Passed:** the snapshot taken now, its metrics file (with `comparison` against a snapshot from the
  period's start, if one was passed), the question file.
- **Figures come from the metrics**, each with its basis; per-task rows from the snapshot. The one
  sum made here is the total of a per-task table shown beside it, so the caller can redo it. A
  figure the metrics lack: name it and what produces it.
- **Output:** the review in `findings`, conclusion in its first lines
  (`wiki/showing-work/which-chart-for-which-plan-question.md`, Failure modes). Each comparison not
  made goes to `not_covered` as "not made: <comparison>, because <missing input>". The only ops are
  `comment`s recording on a task a decision the board lacks, in
  `.task-master/changeset-review-period-<slug>.json`; a re-cut is named for `decompose`.

## Process

### Both setups

1. **Fix what can be compared.** One line per comparison, made or not and why. The plan and the
   communicated date are records of the start, never the board now
   (`wiki/reading-history/chosen-delay-versus-slip.md`, The test;
   `wiki/reading-history/iteration-summary-plan-versus-fact.md`, Limits).

   | Comparison | Needs |
   |---|---|
   | Selection at the start against what finished | History, or a snapshot taken by the period's first day |
   | Points planned and earned; velocity | An estimate on each task, and the sprint it names (`velocity`) |
   | Scope added or removed, estimates revised | History, or an earlier snapshot (`comparison`): the net change only |
   | Goal met | The goal, from the caller or the period's record |
   | Delay or slip | A communicated date, from the recorded forecast |
   | Cycle time, SLE hits, throughput in a window | Start and finish times per item (`cycle_time`, `sle`, `throughput.window`) |

2. **Name the promise** — read `wiki/periods/commitment-over-a-period.md`, The decision.
   Iterations: the goal or the selection per `[process].commitment`, else the process document or
   the caller; none says, report per task with the goal beside it and record which was assumed.
   Flow: each item carries the SLE; a set carries only a forecast the caller passes. No SLE: say
   there is no per-item promise.
3. **Weigh every sign** against the process document first
   (`wiki/reading-history/smell-is-not-a-finding.md`). A cause is never stated from a figure alone.

### Iterations

4. **Plan against fact, per task** — read `wiki/reading-history/iteration-summary-plan-versus-fact.md`
   and `wiki/reading-history/all-or-nothing-counting.md`. Table: task, result in words, planned,
   earned (whole estimates only). No finish times: say state now is not state at the period's end.
   No estimates: count tasks and label the table "by count".
5. **Velocity** from `velocity.periods` (`points`, or `points_reason` where null). Before calling
   it healthy, read `wiki/reading-history/velocity-masks-unfinished-work.md`, Observable signs. A
   forecast from it belongs to `schedule`.
6. **Unfinished work** — read `wiki/periods/unfinished-at-period-end.md` and
   `wiki/reading-history/diagnosing-unfinished-work.md`, Telling them apart. Name the candidate
   cause per task, or the input it lacks. Too large: propose a re-cut through `decompose`. Never
   propose carry-over as the default.
7. **Forces behind the gap** — read `wiki/reading-history/release-progress-forces.md`, Method. Copy
   `comparison.forces` (`completed`, `abandoned`, `added`, `removed`, `re_estimated.delta`, each
   with its `without_estimate`; `estimate_appeared_or_lost` for `re_estimated`); `residual` is the
   work unfinished now. Whether the forces account for the change needs the remaining work at the
   start, which the metrics lack: say that check is not made, and never spread a gap over the
   forces. Scope changed: say whether a decision is recorded (`wiki/periods/mid-period-change.md`,
   Sign of violation; an addition alone is not a sign).
   A communicated date missed: chosen delay, replan or slip by the tests in chosen-delay-versus-slip.

### Flow

8. **Throughput:** `throughput.window` with `arrivals.window` beside it, never in points
   (`wiki/reading-history/throughput.md`).
9. **Cycle time** of items finished in the window: `cycle_time` `n`, `percentiles` (null ones with
   `percentile_reasons`), each item's `start_source` (`wiki/reading-history/cycle-time.md`,
   `wiki/reading-history/cycle-time-percentile-lines.md`). Few items: read the dots and say the tail
   is unknown (`wiki/reading-history/how-much-flow-data.md`). No average without its spread.
10. **SLE hits** from `sle`: the share within the SLE against its stated probability — read
    `wiki/periods/service-level-expectation.md`, What later fact shows the choice wrong. Each miss
    gets its own question, never a verdict on the team. `sle.small_sample`: say the share rests on
    too few to judge.
11. **Age of started work open at the window's end:** `age.items[].work_item_age_days` at
    `age.reference_time`, against the same percentile lines (`wiki/reading-history/work-item-age.md`;
    `wiki/moving-work/percentile-intervention-triggers.md`). An item finished after the window's end
    is missing from the open set: say so. A null age is named with its `work_item_age_reason`;
    `days` since creation, if used, is labelled so.

## Common pitfalls

- **Don't** fill a planned column from the snapshot taken now.
- **Don't** count closed sub-tasks as progress, or report a goal-led period as a share of items
  with its goal unmentioned.
- **Don't** compute velocity, a percentage per task, or a forecast here.
- **Don't** forecast or report individual load: forecasts are `schedule`'s; load is outside the
  charter.
