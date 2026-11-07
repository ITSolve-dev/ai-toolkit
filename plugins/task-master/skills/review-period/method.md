# review-period: method

A past period in; what was promised, what came out, and what explains the difference. Read the
question file first: it names the period, the setup, any earlier snapshot, and what the skill has
already ruled out. Open a cited page when a case is borderline. "This wiki's reading" means the base
marks the rule as its own, not a source's.

## Inputs and output

- **Passed:** the snapshot taken now, its metrics file (with `comparison` made against a snapshot
  taken at the period's start, if one was passed), the question file.
- **Figures come from the metrics files**, each with its basis: counts, throughput, cycle times,
  percentiles, ages, the share within the SLE. Per-task rows are read from the snapshot. The one sum
  made here is the total of a per-task table whose rows are shown beside it (this method's own rule,
  so the caller can redo it). A figure missing from the metrics: name it and what produces it.
- **Output:** the review in `findings`, conclusion in its first lines
  (`wiki/showing-work/which-chart-for-which-plan-question.md`, Failure modes). Each comparison not
  made goes to `not_covered` as "not made: <comparison>, because <missing input>". The only ops are
  a `comment` recording on a task a decision the board lacks, in
  `.task-master/changeset-review-period-<slug>.json`; a re-cut is named for `decompose` in `findings`.

## Steps (both setups)

1. **Fix what can be compared.** Check each comparison's inputs against the question file and the
   snapshot header (`source`, `taken_at`).

   | Comparison | Needs |
   |---|---|
   | Selection at the start against what finished | History, or a snapshot taken by the period's first day |
   | Points planned and earned; velocity in points | An estimate on each task, and the sprint it names (`velocity`) |
   | Scope added or removed, estimates revised | History, or an earlier snapshot (`comparison`): the net change, not when it happened |
   | Goal met | The goal, from the caller or the period's record |
   | Delay or slip | A communicated date, from the recorded forecast |
   | Cycle time, SLE hits, throughput in a window | Start and finish times per item (`cycle_time`, `sle`, `throughput.window`) |

   The plan and the communicated date are records of the start, not board state now
   (`wiki/reading-history/chosen-delay-versus-slip.md`, The test;
   `wiki/reading-history/iteration-summary-plan-versus-fact.md`, Limits). *Output:* one line per
   comparison, made or not and why. *Wrong if:* a planned column is filled from the snapshot taken now.

2. **Name the promise.** Iterations: the goal or the selection, per `[process].commitment`, else
   the process document or the caller (`wiki/periods/commitment-over-a-period.md`, The decision);
   none says, report per task,
   the goal beside it if given, and record which was assumed. A list of sub-steps is never the
   promise. Flow: no period promise exists; each item carries the SLE, and a set carries only a
   forecast the caller passes (same page). No SLE in the settings: say there is no per-item promise.
   *Wrong if:* sub-tasks closed are counted as progress, or a goal-led period is reported as a share
   of items with its goal unmentioned.

3. **Signs are questions.** Every finding below names what to check and why, and is weighed against
   the process document first: the workflow may prevent, intend or limit what the sign suggests
   (`wiki/reading-history/smell-is-not-a-finding.md`). *Wrong if:* a cause is stated from a figure
   alone.

## Steps: `setup = "iterations"`

4. **Plan against fact, per task.** Table: task, result in words, planned, earned
   (`wiki/reading-history/iteration-summary-plan-versus-fact.md`). Earned is the full estimate for a
   task finished by the period's end, otherwise zero; a result handed off and awaiting its verdict
   earns nothing (`wiki/reading-history/all-or-nothing-counting.md`, Settings and executors). An
   overrun is written in the result, not in the points. No finish times: state now is not state at
   the period's end, so say so. No estimates: count tasks and label the table "by count".
   *Wrong if:* a fraction or percentage stands against a task, or the earned total is not a sum of
   whole estimates.

5. **Velocity.** Take it from `velocity.periods` (`points`, or `points_reason` where null; by
   count where the settings have no `[board.size]`), counted all-or-nothing by the sprint each task names now. Then check what it can mask:
   tasks finished while their parents stay open, or blocked and unfinished work accumulating, is
   read before velocity is called healthy (`wiki/reading-history/velocity-masks-unfinished-work.md`,
   Observable signs). A forecast from it belongs to `schedule`. *Wrong if:* a velocity is computed
   here, or reported as on plan with no look at open work.

6. **Unfinished work.** It earns nothing and has no automatic claim on the next period
   (`wiki/periods/unfinished-at-period-end.md`). For each, name the candidate cause the board
   supports, too large, underestimated or too much selected, by the inputs in
   `wiki/reading-history/diagnosing-unfinished-work.md` (Telling them apart); a cause whose input is
   absent is named with that input. Too large: propose a re-cut through `decompose`. *Wrong if:* a
   carry-over is proposed as the default, or the same task unfinished across periods gets no cause.

7. **Forces behind the gap.** Copy the split from `comparison.forces`: `completed`, `abandoned`,
   `added`, `removed` and `re_estimated.delta`, each with its `without_estimate` (for
   `re_estimated`, `estimate_appeared_or_lost`); its `residual` is
   the work unfinished now. Whether the forces account for the change needs the remaining work at
   the start, which the metrics do not give: say that check is not made, and never spread a gap
   over the forces (`wiki/reading-history/release-progress-forces.md`, Method). No comparison:
   step 1 already ruled this out. Scope changed in the period: say whether a decision is recorded for it
   (`wiki/periods/mid-period-change.md`, Sign of violation; an addition alone is not a sign). A
   communicated date missed: chosen delay, replan or slip by the three tests
   (`wiki/reading-history/chosen-delay-versus-slip.md`). *Wrong if:* a residual is absorbed into one
   force, or "chosen delay" stands with no dated decision behind it.

## Steps: `setup = "flow"`

8. **Throughput:** `throughput.window` (items finished in the window), and `arrivals.window`
   beside it (`wiki/reading-history/throughput.md`). *Wrong if:* it is stated in points or called
   velocity.

9. **Cycle time** of the items finished in the window: `cycle_time` `n`, `percentiles` (null ones
   with `percentile_reasons`) and each item's `start_source` (`wiki/reading-history/cycle-time.md`, `wiki/reading-history/cycle-time-percentile-lines.md`).
   Few items: read the dots and say the tail is unknown (`wiki/reading-history/how-much-flow-data.md`).
   *Wrong if:* an average stands without its spread.

10. **SLE hits:** the share finished within the SLE against its stated probability; a share well
    below it asks whether the SLE or the process is off, and each miss gets its own question
    (`wiki/periods/service-level-expectation.md`, What later fact shows the choice wrong), from
    `sle`. `sle.small_sample`: say the share rests on too few to judge, with its reason. *Wrong if:* a miss is reported
    as a failure of the team.

11. **Age of started work open at the window's end**: `age.items[].work_item_age_days` at
    `age.reference_time`, against the same percentile lines (`wiki/reading-history/work-item-age.md`;
    questions by line, `wiki/moving-work/percentile-intervention-triggers.md`). The open set is the
    snapshot's: an item finished after the window's end is missing, so say so. A null age is named
    with its `work_item_age_reason`; `days` since creation, if used, is labelled so.
    *Wrong if:* age is read as time to finish, or as naming a cause.

## Notes

- No forecast and no individual load: the first is `schedule`'s, the second is outside the charter.
