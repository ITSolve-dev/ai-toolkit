# estimate: method

Size each task, say what each size rests on, flag the ones too big to start. You do not re-cut or
schedule. Open a cited page when a case is borderline.

## In and out

**In:** tasks as text, often written by others. They may carry an estimate already. You may also get
finished tasks with their sizes (references), the project's setup (fixed period or flow, estimates or
none, the scale, iteration capacity, the SLE) and the decision the estimates are for.

**`changeset`**, one entry per task:
- `step`: a value on the scale, or under the flow branch `fits SLE: yes/no`;
- `meaning`: the references just below and just above it, by name (not under flow);
- `rests_on`: the feature of the text that set the step, the assumptions made, and the unknowns;
- `ceiling`: `under`, or `over` with the reason, when it must be cut (`now` / `before start`) and
  `recommend re-cut`; under flow the same shape, with the scope test and the SLE check as the
  reasons. Naming a remedy's kind (split, spike) is allowed; naming the pieces is not: that is
  `decompose`'s job, done with the source document;
- `existing`: the estimate the task arrived with, if any, and whether you agree.

Put the setup you continued on and the absence of references in `assumptions`.

## Steps

1. **Read the setup.** Two switches decide it: is there a fixed period, is there a WIP control.
   Then: does the project keep estimates, on what scale, with what SLE.
   → `wiki/moving-work/board-rules-by-setup.md`. Read them from the caller's input. Missing and not
   inferable: assume iterations with no SLE, as `decompose` does, and record it (this method's own
   default, so the two skills size the same input alike).
   Branches: estimates kept → steps 2-7 and 9. Flow with no estimates → steps 3, 5, 8, 9, where 8
   replaces the scale, the references and the numeric ceiling.
   No scale named where estimates are kept: 1, 2, 3, 5, 8, with 13, 20, 40, 100 for distant work,
   labelled an assumption (*this method's own rule*; what matters is one scale per project,
   `wiki/sizing/estimation-scale.md`).
   *Output:* one line of setup in `assumptions`. *Wrong if:* a step is used that the stated scale
   lacks, or hours appear where the project counts points.

2. **Build the reference set.** Group the finished tasks by step. A step means what the tasks on it
   are; that meaning is what keeps estimates from different sessions comparable.
   → `wiki/sizing/estimation-baseline.md`, `wiki/sizing/triangulation.md`.
   No references: estimate the input as one batch so its tasks anchor one another
   (`wiki/sizing/story-points.md`). These first estimates are expert opinion
   (`wiki/sizing/estimation-techniques.md`), "the ones least worth trusting" in this wiki's reading
   (`wiki/sizing/triangulation.md`); say in `assumptions` that the steps hold only within this set.
   *Wrong if:* references mix units or scales (hours beside points). Flag it, do not convert: a
   sum across them means nothing (`wiki/sizing/size-versus-duration.md`).

3. **Read what is inside each task.** List what it contains, and estimate the whole: execution and
   the person's review of the result. A number for one part, or a sum of phases, undercounts what
   falls between them. → `wiki/sizing/story-points.md` (review in the cost is this wiki's reading),
   `wiki/sizing/one-estimate-per-task.md`. Note compound signs ("and", slashes, criteria that
   could each ship alone) for step 6 → `wiki/cutting-work/compound-task-text-signs.md`.
   Text too thin to list (a title, a line): list its plausible readings instead and size from
   their spread (`wiki/sizing/estimating-underspecified-work.md`). Thin text is not the scope test
   of step 6; that fires only when the readings describe different results. Mark such a task in
   `rests_on` as needing its content before it starts, since an estimate does not make it ready
   (same page). More than half the input that thin: add one question asking for the tasks' text,
   because the result then rests on your readings, not on theirs (this method's own rule).

4. **Place each task on a step by triangulation.** Propose a step. Check the task is a little bigger
   than a reference one step down and a little smaller than one a step up. Move it until that holds.
   A step is a bucket: a slight excess rounds down, a clear one moves up. A value between steps is
   false precision. → `wiki/sizing/triangulation.md`, `wiki/sizing/estimation-scale.md`.
   *Output:* `step`, `meaning`, and in `rests_on` the feature that decided it.
   *Wrong if:* every task is justified against the same single reference; a value is off the scale;
   a task has no reference of similar size (a sign it is too big, so go to step 6).

5. **Handle what is not known.** A loosely written task still gets a step: state the assumptions,
   bound it against a reference (under flow, against the SLE's time), and take a value for the
   spread, not the worst case. → `wiki/sizing/estimating-underspecified-work.md`. For each unknown,
   either recommend learning it first (when the task's shape or later tasks depend on the answer)
   or carry it as a larger step with the reason written down
   (`wiki/sizing/unknowns-surfaced-by-estimating.md`, this wiki's criterion). The unknown goes in
   `rests_on`, because an executor not told will guess past it. A spread too wide for one value
   raises a question: is this one task?
   *Wrong if:* a guessed step has no assumption beside it.

6. **Check the ceiling.** Cut a task when it is over the ceiling, or when its contents cannot be
   listed, whichever comes first. A large number reports missing understanding.
   → `wiki/sizing/size-ceiling.md`. The ceiling depends on the setup (resolution is this wiki's):
   - iterations with an SLE: is there a good chance it finishes inside the SLE;
   - iterations without one: iteration capacity ÷ 6, capacity from the caller's history;
   - flow: the SLE question, or the step fixed at setup where a scale is kept;
   - always: one whole period is the outer bound, and the scope test overrides any number.
   Capacity not given and no ceiling step fixed: the top of the near scale (8), labelled an
   assumption, as in `decompose` (this method's own default, drawn from the near test in
   `wiki/sizing/estimating-by-horizon.md`). Never use person-weeks or Cohn's days.
   Timing: a task near the top of the order, or one whose cut is useful today, is cut `now`. A
   distant one keeps its large step and is cut `before start`. No task over the ceiling starts.
   → `wiki/sizing/size-ceiling.md` *Cut now or leave it large*.
   A decision that changes between the low and high end of the estimate also justifies a cut now.
   *Output:* `ceiling`, plus the sign that fired. *Wrong if:* a flagged task names no reason, or a
   task you passed lists several results that could each ship alone
   (`wiki/sizing/hidden-wip-in-large-items.md`).

7. **Weigh the estimates the tasks came with.** Leave one as it is unless you believe its size
   relative to the others has changed. Slowness is velocity's business, not the estimate's.
   → `wiki/sizing/re-estimate-when-relative-size-changes.md`. When yours differs by more than a
   step, treat the difference as two readings of the task, not as noise to average: say what each
   assumed. → `wiki/sizing/independent-estimates.md`. Estimates in hours: treat as in step 2.

8. **Flow without estimates: right-size, do not point.** One question per task: is there a good
   chance it finishes within the SLE? Still estimation, of a cheaper kind; the base disagrees with
   the Playbook here (`wiki/sizing/right-sizing.md`). No points, no scale.
   - **The SLE** is a time plus a probability from the caller. Percentiles given and no SLE: take
     the 85th, labelled an assumption, because the percentile is chosen with whoever receives the
     work and most teams start there (`wiki/periods/service-level-expectation.md`, Choosing the
     percentile). Fewer than about 11 finished items: the caller's best guess, labelled, answers
     provisional (same page). No SLE and no guess: the check is unavailable
     (`wiki/sizing/right-sizing.md`), so return `status: partial` with the scope test applied and
     a question asking for a guess (*this method's own rule*).
   - **The judgement** sets the task's text against the SLE's time alone. The finished items gave
     the SLE; the check compares neither durations nor items (`wiki/sizing/right-sizing.md`, The
     test). Yes when its contents can be listed, none is an unknown the task must resolve, no
     compound sign fired, and executing plus reviewing them plausibly fits that time; otherwise
     no, naming which failed (*this method's own rule*). Thin text: judge the most likely
     reading, name the others in `rests_on`, mark the answer provisional, and list the task in the
     question asking for its text; a reading other than the likely one is not by itself an
     unknown the task must resolve (*this method's own rule*). A task that is itself an
     investigation is judged as a spike: yes when its time-box, set by you inside the SLE, is
     stated.
   - **The remedy for a no:** split when a pattern or compound sign applies
     (`wiki/cutting-work/story-splitting-patterns.md`); a spike when the no comes from not knowing
     how it would be built and no pattern applies (`wiki/cutting-work/spike-as-last-resort.md`),
     its time-box inside the SLE, since a spike is pulled like any item (*this method's own
     rule*); reducing what it delivers changes the request, so it goes to `questions`.
   - **"How big" under flow** gets yes/no, not a number; say so in `assumptions`, because the
     check yields none (`wiki/sizing/right-sizing.md`, It is still estimation).
   *Output:* `step: fits SLE yes/no`, `rests_on` naming what in the text decided it, `ceiling`.

9. **Spend effort by purpose.** Stop refining when both ends of a task's plausible range lead to the
   same decision: the one the caller named; none named, whether to cut, recorded as an assumption
   (`wiki/sizing/size-ceiling.md`, A decision depends on a better estimate). Leave tasks with no
   realistic path into the coming work coarse.
   → `wiki/sizing/estimating-effort-by-purpose.md`, `wiki/sizing/estimating-by-horizon.md`.

## When the caller asked for dates

Put this in `assumptions`. A step is an estimate, not a commitment, and goes into no due date
(`wiki/sizing/estimate-versus-commitment.md`). It converts to time only on average over many
tasks, so no date for one task comes from it (`wiki/sizing/story-points-do-not-convert-to-hours.md`);
dates for many are a velocity range, from `schedule`. A period promises its goal or selected
functionality under iterations, and under flow a per-item SLE agreed once a person picks the
percentile; a right-sizing "yes" is not that agreement (`wiki/periods/commitment-over-a-period.md`).
Steps compare only within one scale (`wiki/sizing/estimation-scale.md`), and your estimate is a
proposal for a person who remembers how similar work went (`wiki/sizing/who-estimates.md`).
