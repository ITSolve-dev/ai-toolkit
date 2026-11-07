# schedule — method

Estimated tasks in, a layout over periods and the date range that follows from it out. Deciding the
order is part of this method, because what comes first and what goes in which period are one decision.
Open a cited page when a case is borderline.

## Inputs and output

**From the caller, as text:**
- Tasks: estimate on one scale (with `estimate`'s `ceiling` where it ran), stated dependencies, any
  value/urgency rating, and which are started.
- Setup: fixed periods or flow, period length, the calendar (period start dates, known capacity
  changes), and whether the date or the scope is fixed.
- History, computed by the caller. Under iterations: points finished in each closed period
  (all-or-nothing, `wiki/reading-history/all-or-nothing-counting.md`), the count of closed periods
  since the last change of setup, and the range values for that count (step 3). Under flow:
  forecast lines at stated probabilities, the window they came from, and how many items finished.

**Into `changeset`:** the setup and its source; the velocity basis; the order with the reason for
each move; named periods; the ordered bucket with its cut lines; the date or scope range; the tail.

**Status:** `partial` when a figure the range needs is missing (velocity bounds, a reduced period's
figure), with the rule that produces it in `questions`; `blocked` when estimates are on different
scales. A question for a person goes in `questions`, never in `needs_caller`.

## Steps

1. **Read the setup.** Use the caller's statement. Otherwise infer it from the shape of the history
   (per-period points mean iterations, daily finish counts mean flow) and record that as an
   assumption. If neither is present, return a question: no source supports a setup with neither a
   period nor a WIP control (`wiki/moving-work/board-rules-by-setup.md`).
   *Output:* one line naming the setup and where it came from. *Wrong if:* the layout assumes
   periods the caller never mentioned.

2. **Flow setup: no layout.** There are no periods to lay out over, so say that a layout does not
   apply. Give a forecast as a range with a probability, taken from the caller's lines
   (`wiki/periods/throughput-monte-carlo.md`): several lines (50/85/95%), 85% by default, because
   the risk level is the steering person's choice; name the window. A count that grows with its
   probability was misread. The count covers only right-sized items, so list any task above the
   size ceiling separately (`wiki/sizing/size-ceiling.md`). Fewer than five finished items: show
   the raw values, no range (`wiki/reading-history/how-much-flow-data.md`). With no finished-work history,
   say no forecast can be given yet; never put an average or a single date in its place
   (`wiki/periods/forecast-range-and-probability.md`). Rank only the next free slots, by the rules
   of step 5, because a ranking further ahead expires before it is used
   (`wiki/ordering/just-in-time-prioritization.md`). Then stop.

3. **Iterations: fix the velocity range by the number of closed periods.** Use the row of
   `wiki/sizing/choosing-velocity-estimate-approach.md` (table by count of closed iterations):
   - **none:** a related project's history that passes the seven comparability questions, or a
     planned velocity explicitly labelled as planned, times 0.6–1.6. Low end is the floor.
   - **one:** observed velocity times 0.6–1.6.
   - **two:** mean times 0.8–1.25.
   - **three:** lowest to highest observed. The slowest period is the floor. This row has no
     middle value; quote a mean only if the caller gives one.
   - **four or more** (this boundary is this wiki's): most recent, mean of up to the last eight,
     mean of the slowest three (`wiki/periods/velocity-range-forecast.md`). The slowest-three mean
     may be promised, the mean caps public statements, and the slowest single period is stated as
     a possible outcome below the floor.
   Count periods only since the last change of agent, model or review practice, because velocity
   from another arrangement measures something else. The caller silent on such a change: assume
   none and record it. Never project a trend. Bounds missing: `partial`, with the order (steps
   4–5) and the rule the caller must compute. No rate at all: no date; suggest running one period,
   the method ranked first.
   *Output:* the count, the values, the floor. *Wrong if:* one velocity figure is quoted alone, or
   a value lies above everything in the window.

4. **Check what can be placed.** A task needs an estimate on the velocity's scale. Points from
   different estimators do not add up (`wiki/sizing/choosing-velocity-estimate-approach.md`, seventh
   question): scales differ, `blocked`. Every task is ordered in step 5, placed or not. Unestimated:
   tail as "needs estimate", and the total, so the date, understates the work by it
   (`wiki/periods/velocity-range-forecast.md`). Over the ceiling (above the velocity floor, or `ceiling:
   over`) or a coarse epic number: it counts in the running total at its place in the order, since
   cutting does not remove its work (this method's reading of the same page), and goes in no named
   period, because it cannot finish inside one (`wiki/sizing/size-ceiling.md`,
   `wiki/sizing/estimating-by-horizon.md`). Above the floor or marked `now`: also tail as "re-cut".

5. **Order.** Order by value to the receiver, on the assumption that not everything will finish
   (`wiki/ordering/order-by-value-not-convenience.md`). Rank by the value and urgency bands
   (`wiki/ordering/ordering-by-value-and-urgency.md`; ranks 2–8 are this wiki's derivation).
   Within one rank, the smaller task goes first (`wiki/ordering/cost-of-delay-over-duration.md`).
   Break remaining ties as `wiki/ordering/incomparable-tasks.md` says. A task that cannot be rated
   goes to the tail with a question; it is not forced into a band. No task rated at all: the
   caller's order is the order, unchanged, as a stated assumption with a question, because sorting
   by size without a rank orders by size, not value (*this method's own rule*). Unfinished work
   from a closed period is ranked again, not put first by default
   (`wiki/ordering/reprioritize-before-each-iteration.md`). Leave the current period's selection
   where it is and start the layout at the next period (`wiki/periods/mid-period-change.md`).
   A dependency mentioned without its prerequisite named: keep the task at its place, mark it
   "prerequisite unknown", flag its period fragile (step 6) and ask which, because an edge you
   invent would read as one the caller stated (*this method's own rule*).
   *Wrong if:* the order is justified by what is convenient to build, with no statement of value.

6. **Fill the named periods at the floor.** Name tasks for the next period, and at most the next
   three, because placement further out is made with less knowledge than the next planning will
   have (`wiki/periods/planning-horizons.md`, Release Plan Level of Detail). Take tasks in order
   until the next one would push the period's sum past the floor. That task opens the next period.
   Fill a gap only with a smaller task of the same rank; pulling from a lower rank would order by
   size rather than value (`wiki/ordering/cost-of-delay-over-duration.md`; this limit is the
   method's own reading). With the caller's order standing in for ranks, no gap is filled. State
   each period's unused room. Put a dependent task in a later period than its prerequisite. Where
   both must share a period, flag the pair as fragile, because a commitment resting on an
   unfinished input inherits that input's error (`wiki/ordering/handoff-at-iteration-boundary.md`).
   A reduced period with no figure: fill it at the floor, flag it optimistic, ask for its figure
   (`partial`); do not rescale velocity, since nominal capacity is not plannable capacity
   (`wiki/periods/iteration-capacity.md`; the fill is the method's own rule).
   *Output:* each period with its tasks and their sum against the floor. *Wrong if:* a sum exceeds
   the floor, or a dependent task sits before its prerequisite.

7. **The rest is an ordered bucket; draw the cut lines and the range.** Keep a running total of the
   estimates down the order, past the named periods.
   - **Scope fixed:** find the number of periods k at which k × value first reaches the total,
     adding the value one period at a time. Do this once with the floor (the late end, which may be
     promised) and once with the high value (the early end). Map both to dates from the calendar.
     Round up. Round down only with a named cut. Rounding is not a buffer.
   - **Date fixed:** take N, the periods before the date, from the calendar. Mark where the running
     total passes N × floor (what may be promised), N × mean when given, and N × high. State the
     result as "at least these, probably no more than those". With a real external date, the floor
     line is hard (`wiki/periods/fitting-stories-into-a-release.md`).
   - **Driver not stated:** the scope-fixed form, as an assumption, asking which gives way; the
     layout does not change, so the assumption is cheap to correct.
   k × value counts every period as full. Check the late end by packing the bucket at the floor
   as in step 6; where whole tasks need more periods than k, the packed count is the late end,
   since what may be promised cannot rest on periods no task fits (method's own rule). Name beside
   the range the unused room and any reduced period counted full, since each makes it early.
   Then walk the tasks above the line for prerequisites below it. A needed one moves up, and enough
   drops to stay within the line. The owner's value order decides what drops; record the drop as a
   question (`wiki/ordering/value-order-versus-technical-necessity.md`).
   Without a calendar, give the range in periods.

8. **State the range, never a point.** Give the range, its basis (the step 3 row and the window),
   and its assumptions. Under iterations, say that no probability was computed
   (`wiki/periods/forecast-range-and-probability.md`). Do not size a buffer. If the caller supplies
   one, show it as its own line; never fold it into the estimates (`wiki/periods/choosing-a-buffer.md`).
   Asked when "everything" is done: the range covers the total, and the answer names the tail
   entries it leaves out ("needs estimate", "cannot be rated", outside prerequisites), because a
   date read as covering them would understate (`wiki/periods/velocity-range-forecast.md`).
   Add what would show the plan wrong: delivery below the floor, or a change in the total; either
   calls for rerunning this method, not for re-estimating (same page).
   *Wrong if:* the result has a single date, a fractional period count, or a date that cannot be
   reproduced from the total, the values and the calendar.

9. **The tail.** Everything not placed is listed with its reason, because one date covering it
   would promise precision the estimate lacks: beyond the floor line (with how far mean/high
   reach), needs estimate, re-cut, cannot be rated, or blocked by an outside prerequisite.
