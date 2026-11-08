# schedule: method

Order estimated tasks, lay them out over periods, and give the date or scope range that follows,
with what does not fit kept as a separate tail. Ordering is part of this method, because what comes
first and what goes in which period are one decision. Every order, velocity basis and range cites
the page it came from; open each page named in a step before making that step's decision.

## Input

From the caller, as text:

- **Tasks:** estimates on one scale (with `estimate`'s `ceiling` where it ran), stated
  dependencies, any value/urgency rating, and which are started.
- **Setup:** fixed periods or flow, period length, the calendar (period start dates, known capacity
  changes), and whether the date or the scope is fixed.
- **History, computed by the caller:** where the project's board is set up, from `board_metrics.py`
  output (`velocity.periods`, `throughput`), never asked of a person. Under iterations: points
  finished in each closed period (all-or-nothing, `wiki/reading-history/all-or-nothing-counting.md`),
  the count of closed periods since the last change of setup, and the range values for that count.
  Under flow: forecast lines at stated probabilities, their window, and how many items finished.

## Output

In `changeset`: the setup and its source; the velocity basis; the order with the reason for each
move; the named periods; the ordered bucket with its cut lines; the date or scope range; the tail.

`status` is `partial` when a figure the range needs is missing (velocity bounds, a reduced period's
figure), with the rule that produces it in `questions`; `blocked` when estimates are on different
scales. A question for a person goes in `questions`, never in `needs_caller`.

## Process

1. **Read the setup.** Read `wiki/moving-work/board-rules-by-setup.md`. Use the caller's statement;
   otherwise infer it from the history's shape (per-period points: iterations; daily finish counts:
   flow) as an assumption. Neither present: return a question. Never assume periods the caller
   never mentioned.
2. **Flow: forecast, no layout.** Read `wiki/periods/throughput-monte-carlo.md`,
   `wiki/periods/forecast-range-and-probability.md`, `wiki/reading-history/how-much-flow-data.md`,
   `wiki/sizing/size-ceiling.md` and `wiki/ordering/just-in-time-prioritization.md`. Say a layout
   does not apply, give the caller's lines (85% by default; name the window), list tasks over the
   ceiling separately, rank only the next free slots by step 5, then stop.
3. **Iterations: fix the velocity range.** Read `wiki/sizing/choosing-velocity-estimate-approach.md`
   (the table by count of closed iterations) and `wiki/periods/velocity-range-forecast.md`. Give
   the count, the values and the floor. Count only periods since the last change of agent, model or
   review practice; the caller silent on one, assume none and say so. Bounds missing: `partial`,
   with the order (steps 4–5) and the rule the caller must compute. No rate at all: no date;
   suggest running one period.
4. **Check what can be placed.** Read `wiki/sizing/choosing-velocity-estimate-approach.md` (the
   seventh question) and `wiki/sizing/size-ceiling.md`.
   - Different scales: `blocked`.
   - Unestimated: tail as "needs estimate".
   - Over the ceiling (above the velocity floor, or `ceiling: over`) or a coarse epic number: it
     counts in the running total at its place in the order, since cutting does not remove its
     work, and goes in no named period.
   - Above the floor or marked `now`: also tail as "re-cut".
5. **Order.** Read `wiki/ordering/order-by-value-not-convenience.md`,
   `wiki/ordering/ordering-by-value-and-urgency.md`, `wiki/ordering/cost-of-delay-over-duration.md`,
   `wiki/ordering/incomparable-tasks.md`, `wiki/ordering/reprioritize-before-each-iteration.md` and
   `wiki/periods/mid-period-change.md`. Rules no page states:
   - A task that cannot be rated goes to the tail with a question, not into a band.
   - No task rated at all: keep the caller's order unchanged, as an assumption, with a question;
     sorting by size without a rank orders by size, not value.
   - A dependency mentioned without its prerequisite named: keep the task in place, mark it
     "prerequisite unknown", flag its period fragile and ask which. An invented edge would read
     as one the caller stated.
6. **Fill the named periods at the floor.** Read `wiki/periods/planning-horizons.md`,
   `wiki/ordering/handoff-at-iteration-boundary.md` and `wiki/periods/iteration-capacity.md`. Name
   at most the next three periods. Take tasks in order until the next would push the sum past the
   floor; that task opens the next period. State each period's unused room. A dependent task goes in
   a later period than its prerequisite; a pair that must share one is flagged fragile. Rules no
   page states:
   - Fill a gap only with a smaller task of the same rank; with the caller's order standing in for
     ranks, fill no gap.
   - A reduced period with no figure: fill it at the floor, flag it optimistic and ask for its
     figure (`partial`); never rescale velocity.
7. **Draw the cut lines and the range.** Read `wiki/periods/velocity-range-forecast.md`,
   `wiki/periods/fitting-stories-into-a-release.md` and
   `wiki/ordering/value-order-versus-technical-necessity.md`. Keep a running total down the order.
   - **Scope fixed:** the first k at which k × value reaches the total, once at the floor (late end)
     and once at the high value (early end), mapped to dates and rounded up.
   - **Date fixed:** N periods from the calendar; mark where the total passes N × floor, N × mean
     (when given) and N × high: "at least these, probably no more than those".
   - **Driver not stated:** scope fixed, as an assumption, asking which gives way.
   - **Check the late end** by packing the bucket at the floor as in step 6; where whole tasks need
     more periods than k, the packed count is the late end.
   - **Beside the range,** name the unused room and any reduced period counted full.
   - **A prerequisite below the line** that a task above it needs moves up; enough drops to stay
     within the line, by the owner's value order, recorded as a question.
   - **No calendar:** give the range in periods.
8. **State the range, never a point.** Read `wiki/periods/forecast-range-and-probability.md`. Give
   the range, its basis and assumptions, and what would show the plan wrong. Asked when
   "everything" is done: name the tail entries the range leaves out. **Do not size a buffer** unless
   the caller asks for one; only then read `wiki/periods/choosing-a-buffer.md`.
9. **List the tail.** Everything not placed, with its reason: beyond the floor line (and how far
   mean/high reach), needs estimate, re-cut, cannot be rated, blocked by an outside prerequisite.

## Common pitfalls

- **Don't** quote one velocity figure alone, or project a trend. **Do** give the table's range.
- **Don't** let a period's sum exceed the floor, or a dependent task precede its prerequisite.
- **Don't** justify the order by what is convenient to build. **Do** state the value behind it.
- **Don't** give a single date, a fractional period count, or a date the total, the values and the
  calendar cannot reproduce.
- **Don't** fold a buffer into the estimates. **Do** show a caller's buffer as its own line.
