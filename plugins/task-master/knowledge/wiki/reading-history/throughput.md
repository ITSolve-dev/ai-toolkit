---
title: Throughput
category: reading-history
summary: Throughput is the count of work items completed per unit of time, compared with the arrival rate in the same unit (a shared unit does not need a shared cadence), in any chosen period; it is not Velocity, which is Story Points per iteration. On a CFD its average over a range is the slope of the bottom line, an exact figure, and each interior line is at once one step's departures and the next step's arrivals, so comparing rates exposes predictability problems and constraints.
tags: [concept, throughput, velocity, arrival-rate, flow, metrics, cfd, retrospective-analysis, vacanti, method, departure-rate, cadence]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Throughput

Throughput is "the amount of WIP (number of work items) completed per unit of time" ([[vacanti-actionable-agile-metrics]] L722), that is, how fast items depart a process (L724). It answers "How many features am I going to get in the next release?" (L738) and is one of the [[flow-metrics]]. An item is completed when it crosses the finished point of the [[started-and-finished-points]].

## Measuring it

Count discrete items that departed in a period. The period is the team's choice: per day, week, iteration or month, as in "three stories per day" or "five features per month" (L724). Like [[work-in-progress]], it may be segmented by type (L634). The comparison with arrivals is run as in measuring arrival and departure rates, below.

## Exact, but an average

On a [[cumulative-flow-diagram]] the average Throughput over a date range is the slope of the bottom line between those dates, and the same calculation on the top line gives the arrival rate (L1656-L1658). The steps are on the same page. The source draws the line between this and the horizontal reading deliberately:

> If the bottom line of your CFD represents the departures from your process, then the slope of that line between any two points (reporting intervals) is your _exact_ average Throughput between those two points.
>
> — [[vacanti-actionable-agile-metrics]], L1656

This wiki's explanation, where the source states only the contrast: the slope needs no assumption about which items are which, because it uses only counts of departures. That is why it can be exact where [[cumulative-flow-diagram]] cannot. Exactness holds for the average over the stated range, and on a chart obeying all six properties (L1720). This wiki reads a slope over a long range as able to conceal changes of pace within it, so the range belongs with the number.

The book's figure is 517 items over 148 days, or 3.49 items per day (L1682). The setting is one example process that starts from zero departures on June 21, so the figure is an illustration and not a benchmark.

## Counting the run

The worked example takes the run as a plain date subtraction, November 16 minus June 21 equals 148 days (L1682). The add-one rule on [[cycle-time]] is stated for Cycle Time. This wiki's advice is to keep the run a plain subtraction when reproducing the book's figures and to state it either way.

## Throughput is not Velocity

Vacanti separates the two sharply: Velocity is "measured in terms of Story Points per sprint or iteration", while Throughput counts actual work items, "_not_ Story Points" (L726-L732). They differ on two independent axes.

| | Throughput | [[velocity]] |
|---|---|---|
| What is counted | Items | Story Points |
| Period | Any | The sprint or iteration |

The period difference has a practical consequence: "your choice of a time period need not necessarily coincide with an iteration boundary" (L732). So Throughput needs neither estimates nor iterations, only departure events. The source notes that "many agile coaches and consultants use the words “Velocity” and “Throughput” interchangeably" (L732) and insists they are definitely _not synonymous_ (L732).

**Sign:** a figure called throughput whose unit is points, or that can only be reported per sprint. Ask whether items or points are being counted. The two can move apart, so one must not be used to check the other. A calculation that feeds velocity in as Throughput fails outright ([[littles-law]]).

For a project set up with iterations and estimates, this wiki's resolution is that both can coexist, since they measure different things. For a project set up as continuous flow with no estimates, only Throughput exists, because Velocity has no input. Which of them a report should use is on [[points-or-time-and-count]].

## Arrival Rate

"If Throughput is how fast items depart from a process, then Arrival Rate is how fast items arrive to a process." (L734) On a CFD the slope of the top line represents "how fast work is coming into our system", and the slope of the bottom line how fast it leaves (L1658).

The comparison is what matters. The source says that comparing the Arrival Rate of one step to the Throughput of another "may give you some much needed insight into predictability problems" (L736), deferring the detail to later chapters; [[littles-law]] makes their balance the first assumption and [[conservation-of-flow]] the rule. Its immediate point is that "how fast things arrive to your process could be just as important as how fast things depart" (L736).

This wiki derives a consequence from Property #3: if arrivals outpace departures over a range, the vertical distance between the two lines widens, which means total WIP grew over that range. The sign is visible on the chart as the top and bottom lines diverging; see [[reading-a-cfd]].

**Sign (this wiki's reading):** over a stretch of history, items enter a step faster than they leave it. Ask whether the step is accumulating work ([[starting-more-work]]).

## One line, two rates

Depending on perspective the two rates are the same flow: Throughput from Development can be read as Arrival Rate to Test when the steps are adjacent (L734). The CFD states this as a property. Property #6 says the slope of any line is the exact Average Arrival Rate of the state in the succeeding band (L1668), and its corollary is that the same slope is the exact average Throughput of the preceding step (L1670). Vacanti also calls this the Departure Rate or Completion Rate (L1670) and notes that Property #6 follows directly from Property #1 (L1670).

This wiki reads the consequence as follows: between two adjacent steps there is one rate, not two. A difference between adjacent steps has to be sought between different lines, not within one.

## Per-step Throughput and constraints

Throughput at each step "will help you to identify the constraints in your workflow (assuming variability has been taken into account—but more on that later)" (L746). Vacanti states this despite being on record as skeptical of applying the Theory of Constraints to knowledge work (L740), and the variability condition is part of the claim: he does not offer a bare low step count as proof. The result points to where process improvement should look, for example whether to introduce automation (L746). The source's staffing questions from the same passage are out of scope under the charter.

A chart alone is a weaker basis for this: Vacanti says it is "impossible to spot a systemic bottleneck" by looking at a CFD (L1944; see [[cumulative-flow-diagram]]). This wiki reads the two together: per-step rates raise a question about a constraint, and neither names one.

## What it does not measure

This wiki's reading from the definition: Throughput counts departures and says nothing about value, about how long any item took, or about what remains in progress. Those need [[cycle-time]] and [[work-in-progress]]. Because it counts items and not size, a higher number can mean smaller cuts rather than more delivered. Its relation to WIP and Cycle Time runs through [[littles-law]].

## Measuring arrival and departure rates

This method tells whether [[conservation-of-flow]] holds, by comparing how fast work enters the process with how fast it leaves. Both rates are counts, read from board history, and need no logged time.

### Procedure

1. Fix the arrival and departure points ([[started-and-finished-points]]); the rates are meaningless without them.
2. Choose a unit of time. It “is completely up to you (day, week, every two weeks)” ([[vacanti-actionable-agile-metrics]] L2038).
3. Count new items placed on the arrivals column per unit (L2038). Count items crossing the departure line per unit, in the same way (L2062).
4. Average both and compare. “If those two averages come out to be the same, then you are in good shape.” The source's guess is that they will differ (L2064-L2070).

A CFD does the same comparison better and is the source's preferred form (L2074); see [[cumulative-flow-diagram]].

### How much history

The period is “arbitrarily long”, though what is needed may be “perhaps as little as a few weeks” (L2064). The source gives this with no setting behind it, so this wiki treats it as a starting point and not a threshold. At a low item count, a few weeks may hold very few items, and this wiki reads a small gap between averages there as noise before reading it as imbalance.

### Unit versus cadence

These are two different things, and confusing them is the main trap here.

- **Unit of measurement** must be identical: “the unit of time you choose to measure the Arrival Rate must match the unit of time that you choose to measure your Departure Rate” (L2038).
- **Cadence** need not be: “choosing the same interval of time to measure arrivals and departures does not mean that the cadence of arrivals and departures must be the same.” (L2040)

A team may deploy every two weeks and replenish every week, and that “might be optimal given your specific context” (L2040). The cost is a conversion: data in two-week and one-week intervals must be brought to one unit before comparing, in either direction (L2040-L2046). Further, “whatever unit of time you choose for your reporting must be consistent across all metrics.” (L2046)

### Signs of a bad measurement

These are this wiki's application; each raises a question to check.

- Rates compared across different units, for example per-sprint departures against per-week arrivals.
- Arrivals counted from a backlog and not the arrivals column, which counts demand and not commitment.
- A departure average taken over intervals with batch deployment, in a unit shorter than the batch, which gives many zeros and spikes. Convert to the batch length first.

### What it cannot say

Equal averages say the rates match over the period. This wiki reads them as saying nothing about whether the process is healthy; see [[cumulative-flow-diagram]].

## Agent executor note

The definition survives: it needs only departure events. The transfer to a few people steering an agent is ours: departures still depend on the person who accepts results, so with an agent executing, step-level Throughput is more likely to show the constraint at briefing or review than at execution.
