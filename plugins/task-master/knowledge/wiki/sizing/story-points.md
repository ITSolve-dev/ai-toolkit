---
title: Story Points
category: sizing
summary: A unitless, relative measure of the overall size of a piece of work; only the ratios between items carry meaning, and the unit gains a time meaning only through velocity. Because it describes only how much there is to do, it is estimated by analogy, does not change as the executor improves, and cannot be held against the calendar.
tags: [concept, estimation, relative-estimation, scale]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Story Points

Story points are a unitless measure of the overall size of a piece of work, assigned by comparing items with one another rather than by measuring any of them. Cohn presents them as one of two measures of size, alongside [[ideal-days]] ([[cohn-agile-estimating-planning]] L933). A point has no time meaning of its own: it acquires one only through [[velocity]], which is why the chapter has to introduce velocity before unitless estimates can make sense (L1008).

## What a point value means

> Story points are a unit of measure for expressing the overall size of a user story, feature, or other piece of work.
>
> — [[cohn-agile-estimating-planning]], L953

> The raw value we assign is unimportant. What matters are the relative values. A story that is assigned a two should be twice as much as a story that is assigned a one.
>
> — [[cohn-agile-estimating-planning]], L953

Cohn's claim is therefore about ratios: a 2 is twice a 1 and two-thirds of a 3 (L953). The knowledge he says is required is only ordinal in its plainest statement:

> All I need to know is whether a particular story or feature is larger or smaller than other stories and features.
>
> — [[cohn-agile-estimating-planning]], L943-L949

This wiki notes that the two statements ask for different things. An ordering is weaker than a ratio, yet the arithmetic of [[deriving-duration-from-velocity]] sums points, and a sum is only meaningful if the ratios roughly hold.

## What a point is an amalgam of

Cohn gives no formula for size:

> a story point estimate is an amalgamation of the amount of effort involved in developing the feature, the complexity of developing it, the risk inherent in it, and so on.
>
> — [[cohn-agile-estimating-planning]], L955

His summary repeats this as a story being "twice as big, complex, or risky" (L1052), while the painting example treats points as plain effort (L1035). This wiki reads the looseness as a cost of the unit: because one number folds several dimensions together, two people can agree on a value for different reasons.

The dog-point exercise shows the same hazard on a single dimension. Cohn defines a dog point as height at the shoulder (L959) and then observes:

> However, if I had been estimating dog points based on weight, I would have given bulldogs a higher number.
>
> — [[cohn-agile-estimating-planning]], L981

This wiki draws the discriminating point from that: a value is only comparable with values produced under the same definition of what is being compared.

## What purity gives

The defining property in Cohn's Chapter 8 argument is purity: "Story points are a _pure_ measure of size. Ideal days are not." (L1580). Size comes first in his sequence, as the step before estimating how long something will take (L1580).

**The number does not move with proficiency.** "the size is what it is and doesn’t change." (L1580). Cohn calls this a desirable attribute of any measure of size. The contrast is on [[ideal-day-estimate-decay]].

**The number can only be reached by analogy.** "we can only estimate story points by analogy." (L1582). He rests this on evidence: "There is credible evidence that we are better at estimating “this is like that” than we are at estimating the absolute size of things (Lederer 1998; Vicinanza 1991)." (L1582). Ideal days can also be estimated by analogy, but then "we also tend to think of the calendar and how long a story will take to develop." (L1582). The cited studies have not been read for this wiki.

**The number cannot be held against reality.** Being abstract, there "can be no temptation to compare them to reality" (L1584). The opposite case is [[ideal-days-compared-to-actual-days]].

**The number is one figure for all the work.** It "needs to be a single number that represents all of the work for the whole team" (L1558), which is what rules out the arithmetic on [[summed-role-estimates]].

**People can agree on it while disagreeing on duration.** "Two developers of different skill or experience can agree on the size of something while disagreeing about how long it will take to do." (L1636). See [[executor-bound-estimates]].

## When a point estimate does change

Purity does not mean permanence. Cohn separates two causes (L1576): if the amount of work itself changes, for example because a framework now exists, both story points and ideal days must be updated. If the team has merely become better at something, only ideal days must change. The separate rule about relative size is on [[re-estimate-when-relative-size-changes]].

## Starting a scale

The unit has no external anchor, so a team "has to find its own baseline by estimating a few stories" (L1626), and the first few feel uncomfortable. Cohn reports that this passes quickly: "Usually within an hour" (L1628), a practitioner observation about human teams and not a measurement.

Cohn names two ways to begin (L957):

1. Pick a story expected to be among the smallest and call it 1.
2. Pick a roughly medium story and give it a value in the middle of the expected range.

He uses the second, with a medium story at 5, because of a preference stated as such: "Personally, I prefer most of my stories to be in the range of 1–10." (L957). His reason comes in Chapter 6 and is on [[estimation-scale]]. The first value is assigned "fairly arbitrarily"; every later item is estimated by comparison with that one or with any already estimated (L957), and how to compare is on [[triangulation]]. The Labrador at 5 anchors the example, with the Great Dane at 10 and the dachshund at 1 (L981, Table 4.1).

## Failure modes

These signs are this wiki's derivation from the definition above; the chapter does not state them. Each raises a question to check, not a verdict.

- **Points read as time.** A task's value is explained as days or hours, or converted by a fixed factor. If the raw value is unimportant, a fixed conversion contradicts the definition. Cohn names the trap in Chapter 7: points are not an estimate of time, "even though we often fall into the trap of thinking of them as such." (L1396).
- **Points compared across scales.** Values or totals from two projects are compared directly. Since the anchor is arbitrary, the numbers share no unit.
- **Equal points, unequal history.** Items with the same value show very different time in state on the board. That is the later fact that would show the relative estimates wrong, and only a pattern across items means anything. What to do about it is on [[re-estimate-when-relative-size-changes]].

## The range a scale can cover

Chapter 4 ends by asking, without answering, over what range an estimator can compare reliably: five times the smallest item, ten, a hundred, a thousand (L1066). Chapter 6 answers with one order of magnitude, on [[estimation-scale]]. That bound concerns how far a comparison stays reliable. The size above which a task is cut is a separate question, on [[size-ceiling]].

## Agent executor note

The transfer here is this wiki's, not Cohn's. Relative sizing works by remembering earlier items of similar size (L943). An agent has no such memory unless reference tasks are put in front of it, so a scale used by an agent needs its reference items written down. The ratio mechanism itself does not depend on who executes the work. What the chapter does not establish is whether the components of size, effort and complexity in particular, weigh the same when an agent executes and a person steers.

This wiki reads purity as surviving the move to an agent, since nothing in size depends on who does the work. The analogy evidence does not transfer automatically: it concerns human estimators, and whether the claim holds when an agent proposes the estimate is not established by this source. Choosing the unit is on [[story-points-or-ideal-days]].
