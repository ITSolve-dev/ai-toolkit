# estimate: method

Size each task relative to the others, say what each size rests on, and flag the ones too big to
start. Do not re-cut or schedule. Every step and ceiling verdict cites the page it came from; open
each page named in a step before making that step's decision.

## Input

Tasks as text, often written by others, possibly carrying an estimate already. Optionally:
finished tasks with their sizes (references), the setup (fixed period or flow, estimates or none,
the scale, iteration capacity, the SLE) and the decision the estimates are for.

## Output

In `changeset`, one entry per task:

- `step`: a value on the scale, or under flow without estimates `fits SLE: yes/no`;
- `meaning`: the references just below and just above it, by name (not under flow);
- `rests_on`: the feature of the text that set the step, the assumptions made, the unknowns;
- `ceiling`: `under`, or `over` with the reason, when to cut (`now` / `before start`) and
  `recommend re-cut`. Name the remedy's kind (split, spike), never the pieces: that is
  `decompose`'s job, done with the source document;
- `existing`: the estimate the task arrived with, if any, and whether you agree.

The setup you continued on, and any absence of references, go in `assumptions`.

## Read the setup first

Read `wiki/moving-work/board-rules-by-setup.md`: is there a fixed period, a WIP control, estimates
kept, a scale, an SLE. Missing and not inferable: assume iterations with no SLE, as `decompose`
does, so both skills size the same input alike. No scale named: assume 1, 2, 3, 5, 8, with 13, 20,
40, 100 for distant work (`wiki/sizing/estimation-scale.md`). Then follow the section for the setup.

## Estimates kept

1. **Build the reference set.** Read `wiki/sizing/estimation-baseline.md` and
   `wiki/sizing/triangulation.md`. No references: read `wiki/sizing/story-points.md` and
   `wiki/sizing/estimation-techniques.md`, estimate the input as one batch, and say the steps hold
   only within it. References in mixed units: flag, never convert (`wiki/sizing/size-versus-duration.md`).
2. **Read what is inside each task.** Read `wiki/sizing/story-points.md`,
   `wiki/sizing/one-estimate-per-task.md` and `wiki/cutting-work/compound-task-text-signs.md`.
   Size execution plus the person's review as one. Text too thin to list: read
   `wiki/sizing/estimating-underspecified-work.md` and size from the spread of plausible readings.
   If more than half the input is that thin, add one question asking for the tasks' text: the
   result would otherwise rest on your readings, not theirs.
3. **Place each task by triangulation.** Read `wiki/sizing/triangulation.md` and
   `wiki/sizing/estimation-scale.md`. Write `step`, `meaning`, and in `rests_on` the feature that
   decided it.
4. **Handle what is not known.** Read `wiki/sizing/estimating-underspecified-work.md` and
   `wiki/sizing/unknowns-surfaced-by-estimating.md`. Each unknown goes into `rests_on`, with
   "learn it first" or "carried as a larger step" and why.
5. **Check the ceiling.** Read `wiki/sizing/size-ceiling.md` and
   `wiki/sizing/hidden-wip-in-large-items.md`. With no capacity, SLE or fixed step, the ceiling is
   the top of the near scale (8), as an assumption, as in `decompose`. Never person-weeks or days.
   Thin text alone does not fail the scope test; only readings that describe different results do.
6. **Weigh the estimates the tasks came with.** Read
   `wiki/sizing/re-estimate-when-relative-size-changes.md` and `wiki/sizing/independent-estimates.md`.
7. **Spend effort by purpose.** Read `wiki/sizing/estimating-effort-by-purpose.md` and
   `wiki/sizing/estimating-by-horizon.md`. Stop refining when both ends of a task's range lead to
   the same decision: the caller's, or, none named, whether to cut.

## Flow without estimates

Read what is inside each task and handle what is not known as under *Estimates kept*, then
right-size, do not point: read `wiki/sizing/right-sizing.md` and
`wiki/periods/service-level-expectation.md`. Rules no page states:

- No SLE and no guess: return `status: partial` with the scope test applied and a question asking
  for a guess.
- Yes when the contents can be listed, none is an unknown the task must resolve, no compound sign
  fired, and executing plus reviewing plausibly fits the SLE's time; otherwise no, naming which
  failed. Thin text: judge the likeliest reading, name the others, mark it provisional.
- A task that is itself an investigation is judged as a spike: yes when you state a time-box inside
  the SLE.
- Remedy for a no: a split by `wiki/cutting-work/story-splitting-patterns.md`, or a spike by
  `wiki/cutting-work/spike-as-last-resort.md` with its time-box inside the SLE. Delivering less
  changes the request, so that goes to `questions`.

Spend effort by purpose as under *Estimates kept*.

## When the caller asked for dates

Read `wiki/sizing/estimate-versus-commitment.md`,
`wiki/sizing/story-points-do-not-convert-to-hours.md` and `wiki/periods/commitment-over-a-period.md`,
and say in `assumptions` why a step gives no date for one task. Dates for many come from `schedule`.

## Common pitfalls

- **Don't** justify every task against the same single reference. **Do** place each between two.
- **Don't** give a value off the scale or between steps. **Do** round to a step and say which way.
- **Don't** leave a guessed step without the assumption beside it.
- **Don't** pass a task that lists several results that could each ship alone.
- **Don't** average a disagreement with an existing estimate. **Do** say what each reading assumed.
