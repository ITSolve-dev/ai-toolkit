---
title: Fitting Stories into a Release
category: periods
summary: Filling a release starts from which factor gives way: date-driven releases fix iterations and count velocity times iterations down an ordered list to a cut line, feature-driven ones divide the needed points by velocity, and both are tested against the conditions of satisfaction; worked through the SwimStats numbers, with a count-and-probability form where there are no points.
tags: [method, iterations, release, estimation, decision-rule, period-versus-milestone, planning-a-date, scope, commitment]
sources: [cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Fitting Stories into a Release

The core of release planning is one multiplication. Cohn calls it trivial at its simplest level: multiply expected velocity by the number of planned iterations, then select stories whose estimates fill that total ([[cohn-agile-estimating-planning]] L2947-L2951). The number of iterations alone does not give a duration: "we must also estimate the team’s rate of progress through that work" (L2745).

## Inputs and where each is read from

| Input | Read from | Source note |
|---|---|---|
| Conditions of satisfaction | The owner of the goal; see [[conditions-of-satisfaction]] | Comes first (L2802) |
| Story estimates | Estimates on every story that may be selected; see [[estimating-by-horizon]] | L2810-L2812 |
| Iteration length | A chosen constant; "from one to four weeks" is the common range; see [[period-length]] | L2816 |
| Velocity | History first | "If the team has experience working together, your best bet is often to use the velocity the team exhibited most recently." (L2820) |
| Order | A prioritized list; see [[value-order-versus-technical-necessity]] | L2824 |

Figure 13.1 fixes only the ends: conditions first, selection last. The steps in between may be done in any sequence, and the whole is iterated until the conditions can best be met (L2796).

The velocity input has a stated limit: "Naturally, if the technology or business domain changed dramatically, it may not be appropriate to use a team’s past velocity." (L2820). See [[velocity]].

## The steps

1. Fix the driver, on *Date-Driven Versus Feature-Driven* (below).
2. **Feature-driven:** sum the estimates of the needed features and divide by velocity to get the number of iterations (L2832). This is [[velocity-range-forecast]].
3. **Date-driven:** read the number of iterations from the calendar, multiply by velocity, and count that many points down the ordered list (L2834). This is the cut line of *Fixed Date, Variable Scope* (below).
4. Check the result against the conditions. "In both cases, once a team has an initial answer, it is assessed against the organization’s goals for the project" (L2777). If it misses, change a condition and repeat (L2971).
5. If stories are placed into specific iterations, sum each iteration against velocity: the point of the estimate on every card is to verify "that each iteration holds the right amount of work" (L2842-L2846). How much to place is on [[planning-horizons]].

## Worked numbers

Generic case: six months at two-week iterations is thirteen iterations; at twenty points each the release holds 13 × 20 = 260 (L2779).

SwimStats, a date-driven release with three people and a story list totalling 68 points (L2891, L2915-L2929):

- Three months gives six two-week iterations "followed by an extra week in case it’s needed" (L2937).
- Forecast velocity of 8 gives 6 × 8 = 48 points (L2907, L2937).
- The owner picks the first eight stories: 46 points (L2939).
- Developers show a 3-point story from the bottom of the list is necessary, making 49 (L2941).
- The owner drops an 8-point story: 41 points (L2943).
- The owner leaves the remaining 7 points unfilled rather than add a 3-point story, because "If the team gets even one point ahead of schedule, she’d prefer to add back the eight-point story she dropped." (L2943). Adding it back would make 49, which is one over the 48.

**Source errors in this example.** The text says "an estimated velocity of seven points per iteration" while computing with eight (L2937); the eight at L2907 is the consistent figure. The team is one programmer, one database administrator and one tester at L2891, and two programmers and a tester at L2907.

## Is the capacity a hard line?

The source presents both answers. "The 48 points is a fairly rough guess and an extra week is planned after the sixth iteration. Some teams may allow for 49 points under these circumstances." (L2941). The SwimStats team did not allow it and required a drop (L2943).

This wiki resolves that per setting. On a date-driven release with a real external date, treat capacity as a line and hold the buffer as buffer: spending the extra week on planned scope removes what protects the date, and leaves nothing to absorb variability ([[filling-a-period]]). On a feature-driven release the line has less force, since the output is a duration and one point changes little. This resolution is the wiki's reading, built on the two positions the source reports.

## What later fact shows the plan wrong

Measured velocity diverging from the assumed figure over iterations, or iteration planning surfacing large surprises; both are the triggers on [[replanning-on-new-knowledge]].

## Trade-off

The multiplication is only as good as a forecast velocity, and this wiki reads that figure as the softest input. The source calls its result "a fairly rough guess" (L2941). Precision in the sum of estimates does not make the plan more exact than that, and a single total carries the risks on [[forecast-range-and-probability]].

## Agent executor note

This wiki reads the arithmetic as carrying over, but only if velocity is measured for the actual setup of people and agent. The source's forecast rests on a human team's stable rate, and nothing here shows that rate is stable when an agent executes. Until a history exists, a capacity number from this method is an assumption to be stated, not a measurement.

## Date-Driven Versus Feature-Driven

A release usually has one preeminent condition, and Cohn says many projects are either date-driven or feature-driven ([[cohn-agile-estimating-planning]] L2804).

> A date-driven project is one that must be released by a certain date but for which the feature set is negotiable.
>
> — [[cohn-agile-estimating-planning]], L2804

> A feature-driven is one that we would probably like to release as soon as possible but consider the completion of a set of features more important.
>
> — [[cohn-agile-estimating-planning]], L2804

This wiki reads *Fixed Date, Variable Scope* (below) as the first of these. Its "When it does not hold" section is the second, the feature-driven case of L2804.

### The test

Ask which gives way when the two collide. If the date holds and stories fall out, the release is date-driven. If the stories hold and the date moves, it is feature-driven. The phrasing is this wiki's, and it is the same question as the period-versus-milestone test on [[planning-horizons]] and [[commitment-over-a-period]], asked of one release.

**Input and where it comes from.** The answer comes from whoever owns the goal for the release: it is part of the [[conditions-of-satisfaction]]. An external event is the strong case. SwimStats is date-driven because the swim season starts on a fixed date and the release has to be out a month earlier, so something must ship in three months "even if it is only the basics for small swim teams" (L2891).

### What each choice computes

| | Date-driven | Feature-driven |
|---|---|---|
| Fixed | Iterations, from the calendar | The set of needed features |
| Computed | Points that fit: iterations × velocity | Iterations needed: sum of estimates ÷ velocity |
| Output | How far down the ordered list the line falls | When it finishes |
| Computed without points | How many items by the date, at a chosen probability | Days until the items finish, at a chosen probability |

Source for both columns: L2832-L2834, and for the last row [[flow-metrics-scrum-teams]] L1392-L1408 and L1422-L1428, on [[throughput-monte-carlo]]. The mechanics and the worked numbers are on the procedure at the top of this page, and the feature-driven division on [[velocity-range-forecast]].

### What would show the choice wrong

This wiki's reading, not the source's: the board's history shows it. A release labelled date-driven whose date moved while the scope stayed intact was feature-driven in fact. One labelled feature-driven in which stories were quietly dropped to hold a date was date-driven in fact. Either way the release plan should be recomputed with the real fixed factor.

### Trade-off and limits

Both choices give up something. Date-driven accepts less than was wanted, and the order of the list decides what is lost, which makes [[value-order-versus-technical-necessity]] matter most here. Feature-driven accepts an open end date, and the source still frames it as wanting release "as soon as possible" (L2804), so this wiki does not read it as a licence to take longer.

The source says "Many", not all, and gives no test for a project where neither is preeminent. This wiki reads that as: such a project has unresolved conditions, and the question goes back to the person setting the goal rather than being settled by the plugin.

### Agent executor note

This wiki reads the split as being about what the goal-owner will give up, so it survives unchanged when an agent executes. It is a question to ask at project setup, since the plugin cannot read it from a board.

## Fixed Date, Variable Scope

Fixed date, variable scope is the view that a project's end point is usually a date, not a known quantity of work, and that the plan's job is to find how much of the most valuable work fits before it. Cohn contrasts it with a project treated as a race of known length.

> An agile project is more like a timed race than a 10-kilometer race: run as far as possible in sixty minutes. In this way, the agile project team knows when it will finish, but not what they will deliver.
>
> — [[cohn-agile-estimating-planning]], L816

Cohn qualifies the claim. He says "we often know we need to get to it or as close as we can by a known date" (L816), which is often, not always.

### Why the finish line is treated as unknown

Cohn's grounds are that "the end result is both somewhat unknown as well as unknowable in advance", so "planning becomes a process of setting and revising goals that lead to a longer term objective." (L816). This wiki reads a plan that assumes a known finish line as assuming exactly the complete knowledge that [[replanning-on-new-knowledge]] says a project does not have.

### Applying it

This wiki reads the rule as a choice with these inputs.

- The date: read from the release's [[conditions-of-satisfaction]].
- The ordered list of features: read from the board's order ([[order-by-value-not-convenience]]).
- The rate of progress: read from history of completed work in past iterations.

The output is an expected cut line in the ordered list, stated as an expectation and not a promise ([[estimate-versus-commitment]]).

Later fact that would show the choice wrong: the date arrives and the work finished lies below work left undone in the order, or the date is moved to fit the scope, which reveals that the scope was the fixed thing all along.

### When it does not hold

Cohn allows the opposite preference in the same chapter: a product owner may trade a month for more stories (L857). When the conditions of satisfaction fix the content and let the date move, this wiki reads the timed race as the wrong model, and the plan states a date range from the rate of progress instead ([[forecast-range-and-probability]]). Chapter 3 does not spell this case out; Chapter 13 calls it feature-driven (*Date-Driven Versus Feature-Driven*, above) and divides by velocity for it (L2832). Stating the result as a date range is this wiki's reading.

If date, scope and quality all stay fixed and no plan satisfies them, Cohn's answer is that "the conditions of satisfaction must change." (L859).

### Trade-offs

This wiki notes that fixing the date gives up a promise about content. Anyone needing a specific feature by that date gets a likelihood, shaped by the feature's place in the order. The order then carries the weight of the commitment, since what is at the top is what ships. A date that holds while scope gives is also the shape of a period on [[commitment-over-a-period]].

### Agent executor note

This wiki reads the rule as surviving an agent executing. The mechanism is uncertainty in the work, not human pace, although the rate of progress must come from agent-executed history and not from an earlier human team's.

Related: [[timeboxed-iteration]], [[planning-horizons]], [[replanning-on-new-knowledge]].
