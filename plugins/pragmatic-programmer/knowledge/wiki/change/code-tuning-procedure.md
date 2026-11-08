---
title: Code tuning procedure
category: change
summary: "Use when working code is too slow and changes are being made for speed: keep a known-good version, profile to find hot spots, rule out design, data and algorithm causes, change one thing, measure it, revert anything that did not help, repeat and keep trying variants past the first win."
tags: [method, performance, code-tuning, profiling, measurement, reversibility]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

A procedure McConnell gives for deciding whether and how to tune code that already works (p. 591). This wiki reads it as treating each tuning change as an experiment on correct code: most experiments fail, so the method is built around measuring each one and undoing the failures. It is the step that [[premature-code-tuning]] defers to, and this wiki sees in it [[small-steps-with-feedback]] and [[reversibility]] applied to performance work.

## Procedure

1. **Write good, clear code that is easy to change.** The book calls this the best preparation for later speed work (p. 594).
2. **If performance is unacceptable:**
   1. Save a working version, so you can return to «последнему нормальному состоянию» (p. 591). This wiki maps it to a commit or a tag.
   2. Measure the system to find the hot spots. Do not guess: «Не выполнив оценку, вы не найдете этот код» (p. 594).
   3. Decide whether the slowness comes from inadequate design, wrong data types or a poor algorithm. If it does, tuning is the wrong tool and the book sends you back to step 1 (p. 591), which this wiki reads as redesigning at that level. See [[fix-performance-at-the-right-level]].
   4. Tune the bottleneck found in steps 2.2-2.3.
   5. Measure each improvement on its own, one at a time.
   6. If a change did not improve things, revert to the version saved in step 2.1. The book expects this more than half the time: tuning attempts mostly bring a marginal gain or a loss (p. 591).
3. **Repeat from step 2.** The book says one technique rarely gives a tenfold gain, but techniques combine, so keep trying after a first success (p. 590). Chapter 26 repeats it: the first optimization found is often not the best one, and further variants are worth trying (p. 631). In its integer `Log2` case a 30-40% gain from removing one `log()` call was dwarfed by the second and third attempts (p. 620). When one variant fails, a seemingly similar one can succeed: precomputing the loan formula into a table slowed Python by 20% (p. 622), while precomputing only the hard part of the expression outside the loop sped Python up by 66% (pp. 623-624).

## Fowler's version: tunable code first

Fowler's *Refactoring* sets the procedure against refactoring: refactoring may make software slower, but it makes it more amenable to performance tuning, and, in his words, "The secret to fast software, in all but hard realtime contexts, is to write tunable software first and then tune it for sufficient speed" (2nd ed., ch. 2, PDF p. 77). He distinguishes three approaches (PDF pp. 77-79):

1. **Time budgeting.** Each component gets a budget of time and footprint it must not exceed. Essential where late data is always bad data, such as pacemakers; inappropriate for corporate information systems.
2. **Constant attention.** Every programmer always does what they can to keep performance high. Fowler says it does not work very well: performance changes make code harder to work with, the improvements are spread everywhere, each made with a narrow view of the program. That is the case [[premature-code-tuning]] owns.
3. **Profile-driven tuning.** Most of a program's time is spent in a small fraction of its code, so optimizing everything equally wastes about 90 percent of the work (PDF p. 79). Build well factored, ignore performance until a deliberate optimization exercise, then profile, tune the hot spots in small steps, compile, test and rerun the profiler after each, back out any change that did not help, and stop when performance satisfies the users (PDF p. 79).

Well-factored code helps twice: it leaves time for tuning because features come faster, and it gives finer granularity, so the profiler points at smaller parts that are easier to tune (PDF p. 80). Whether a refactoring may proceed despite a cost it adds is [[refactor-first-tune-afterwards]].

Ron Jeffries' sidebar in the same chapter (PDF pp. 78-79) is the case for step 2.2. A team speculated at length about why a payroll process was slow; the profiler showed half the time went into creating date instances, most of them for empty date ranges. Empty-range creation had already been extracted into a factory method for clarity; making it return one shared constant doubled the system's speed in about five minutes. The lesson: "Even if you know exactly what is going on in your system, measure performance, don't speculate" (PDF p. 79). This wiki reads the story as a before/after for the procedure: a clarity refactoring created the single place where the hot spot could be fixed.

```
// before: empty ranges built inline, through string conversion, everywhere
range = DateRange(parseDate("2000-01-02"), parseDate("2000-01-01"))
```

```
// after: refactoring for clarity gave one place; profiling then made it a constant
EMPTY = DateRange(...)
function DateRange.empty(): return EMPTY
range = DateRange.empty()
```

This wiki adds the condition a reviewer checks before sharing an instance like this: the shared constant is sound only because the range is immutable ([[immutable-objects]]).

## Chapter 26's version: the low-level rewrite

For rewriting slow code in a lower-level language, McConnell gives a standard path (p. 626): write the whole application in the high-level language; test it fully and confirm it is correct; if performance is then not enough, profile to find the hot spots, which will usually be small fragments, because about 50% of a program's run time usually falls in about 5% of its code; and rewrite only those fragments. For a hand rewrite he advises checking correctness and measuring the improvement at each stage (p. 628). This wiki reads that path as the same procedure as above, with step 2.4 done by a rewrite, and applies its last step to any of the chapter's techniques, not only to a change of language; the generalisation is ours.

## Measuring so the numbers mean something

- Use a profiler or a system timer, not a stopwatch (p. 590).
- Time only the code being tuned, and count processor time given to the program rather than wall-clock time, so another process does not charge its time to your routine (p. 590).
- Keep the cost of measuring and of program start-up out of both the before and the after (p. 590).
- Re-measure after any change of compiler, library, runtime or hardware. A gain on one setup can turn into a loss on another (p. 579).

## Where to look first

A profile decides. For a first hypothesis, run the checks on [[fix-performance-at-the-right-level]], which owns the book's usual suspects: I/O, system calls, unneeded work and errors that cost time (pp. 583-586). One suspect from the same pages is not there: **traversal against memory layout.** A nested loop whose outer index runs over columns of a row-major table touches a new page on every inner iteration, and swapping the loops cut page faults from rows times columns to rows (p. 584).

## Trade-off

The book reports that aggressive tuning costs readability nearly every time. Its own DES implementation went from 21:40 to 0:22 through about ten combined changes, and ended as a 500-line assembler routine its author is afraid to look at (pp. 590-591). At least two thirds of the techniques tried there did not help (p. 591). This wiki reads that as the reason step 2.6 exists: a change that did not pay for itself in a measurement should not be left to pay its readability cost.

## Limits

McConnell observes that machines have become so fast that for many common kinds of programs the chapter 26 techniques have become irrelevant: most of his tests had to run 1 to 100 million times to give a measurable result, and he asks whether anyone would notice such a gain in a real program (p. 629). Embedded, real-time and resource-constrained systems still need them (p. 629). This wiki reads that, for desktop and server code, as: step 2.2 will often show no hot spot worth tuning, and the procedure then ends there.

Fowler's exception runs the other way: hard real-time systems, where late data is always bad data (heart pacemakers), need time budgeting, in which each component gets a budget of time and footprint it must not exceed, rather than tuning afterwards (ch. 2, PDF p. 77). There the procedure above does not replace the budget.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], chapter 25: the procedure p. 591; measurement pp. 588-590; iteration and the DES case pp. 590-591; the memory-layout case p. 584, with the other common sources of inefficiency (pp. 583-586) left to [[fix-performance-at-the-right-level]]; key points pp. 593-594. Chapter 26: the low-level rewrite path and the 50%/5% figure p. 626; checking each stage p. 628; irrelevance on fast machines and the constrained-system exception p. 629; continuing after the first win pp. 620, 631; the Python precomputation figures pp. 622-624. Quotations were transcribed from the extracted text. The experiment reading, the mapping of the saved version to a commit, the links to [[small-steps-with-feedback]] and [[reversibility]], the reading of step 2.3 as redesign at that level, the reading of the trade-off, the reading of the low-level path as this procedure with its generalisation beyond a change of language, and the reading of the limits are this wiki's own. The rule that a tuned form stays only with a measurement is [[premature-code-tuning]].

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2, "Refactoring and Performance", PDF pp. 77-80, including Ron Jeffries' sidebar (pp. 78-79): tunable software first, the three approaches, the 90 percent figure, the profile-driven loop, the two benefits of well-factored code, the date-range case, and the hard real-time exception under Limits. This wiki's own for that part: the before/after reading of the sidebar, the pseudocode and the immutability condition.
