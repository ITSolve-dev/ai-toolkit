---
title: Cycle Time Percentile Lines
category: reading-history
summary: Horizontal lines at chosen percentiles of finished items' cycle times, usually 50, 70, 85 and 95; they need no assumption about the distribution, resist outliers, and turn history into a time-plus-probability statement.
tags: [method, cycle-time, forecast, flow-metrics, visualization]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time Percentile Lines

A percentile line is a horizontal line drawn across a [[cycle-time-scatterplot]] or a [[cycle-time-histogram]] at the cycle time below which a chosen share of finished items fall. It is the source's replacement for the mean and for standard-deviation bands ([[pseudo-control-chart]]).

The method runs against board history. It yields a time paired with a probability, which is the form a [[service-level-expectation]] needs.

## Procedure

1. Take the cycle times of finished items that are comparable, read from board history.
2. Count the dots and multiply by the percentage: "You just count up all the dots and multiply by percentages." ([[vacanti-actionable-agile-metrics]] L2724).
3. Draw the line at that dot's cycle time. At the 50th percentile, half the dots fall below and half above (L2644).
4. Read each line as a statement about an item entering the process.

> That means that 50% of the work items that have flowed through our process took twenty days or less to complete. Another way of saying that is that when a work item enters our process it has a 50% chance of finishing in twenty days or less
>
> — [[vacanti-actionable-agile-metrics]], L2650

The source defers the conditions of that second sentence to later material ("more on this concept a little later", L2650). This wiki reads the first sentence as a fact about the past and the second as a forecast that holds only as far as the process stays what it was.

## Which lines

The source's starting set in its takeaways is the 50th, 70th, 85th and 95th (L2768). In the body it calls the 50th, 85th and 95th the most popular and names the 30th and 70th as others seen (L2674). The set is a starting point, not a rule:

> Which lines to draw is mostly going to be a function of what you want to learn from your data.
>
> — [[vacanti-actionable-agile-metrics]], L2686

| Input | Read from |
|---|---|
| Cycle times of finished items | Board history, at the [[started-and-finished-points]] |
| The percentile that matters | Decided by the question, or at project setup when it feeds an SLE |
| The items that count as comparable | Items with the same started and finished points |

This wiki reads the later fact that would show a line wrong as the one on [[service-level-expectation]]: over later items, the share finishing within the line is far from the stated percentage.

## Numbers and their conditions

The figures come from one illustrative chart: 30th at 11 days, 50th at 20, 70th at 32, 85th at 43, 95th at 63 (L2650-L2674). They are not benchmarks. The text gives no count of dots, and the figure image is not in the raw, so the sample behind them cannot be checked.

This wiki notes the spread in those figures: going from a 50% to a 95% chance roughly triples the time, from 20 to 63 days. That is the source's trade-off in one example, not a general ratio.

## Why percentiles over mean and standard deviation

The source gives three reasons (L2722-L2732).

1. **No distribution assumed.** "These percentile line calculations work regardless of the underlying distribution." (L2722).
2. **Simple arithmetic.** No statistics training is needed (L2724).
3. **Robust to outliers.** The mean and standard deviation "are heavily influenced by outliers" (L2726), and with extreme cycle times "your percentile lines will not budge all that much" (L2732).

This wiki reads the mechanism behind the third reason as rank. A percentile depends on the order of the dots and not on how far the top dot sits from the rest.

## Trade-offs

- **Confidence costs time.** "as we increase our level of confidence we have to increase the amount of time it takes for work items to complete" (L2684). The source attributes this to variability, which it says will always be present and which is partly needed: "we do need a little variability in order to protect flow" (L2684). Its way of telling self-imposed variability from the kind outside one's control comes later in the book; see [[internal-and-external-variability]].
- **Robustness hides the extreme.** This wiki notes that a line that does not move also does not report the outlier, so the dots above the top line must still be read.

## Small boards: where the robustness claim runs out

The source's robustness claim and the caution on [[service-level-expectation]], that on a small board one outlier moves a percentile, can both hold. This wiki's resolution: the size of an outlier never moves a percentile, but its presence shifts the rank, and with few dots one rank is a large step.

The arithmetic is this wiki's. With 40 dots the 85th percentile is the 34th dot, and six items lie above it. With 8 dots the same percentile lands between the 6th and 7th dots, so only the board's two slowest items lie above it, and with fewer than 20 dots the 95th percentile, by nearest rank, has no finished item above it. So under flow with few items, this wiki reads the high lines as a description of the slowest item or two, not as a probability.

The source says in this passage only that one need not have "massive amounts of data" (L2818) and gives no minimum. Its later figure of 11 or 12 to 30 points for an SLE is on [[choosing-a-service-level-expectation]]; by the same arithmetic, this wiki notes that 12 dots leave only one or two items above the 85th percentile.

## Failure modes

- **Treating the line as a promise.** A 95% line is missed by design one time in twenty. See [[estimate-is-not-a-promise]].
- **Reading finished items as all items.** This wiki notes that the dots exclude open items, so when the oldest open items are older than the top line the lines are optimistic. See [[flow-metrics]].
- **Stating the time without the probability.** See [[service-level-expectation]], where both parts are required.
- **Mixing unlike items.** This wiki notes that one line over items with different finish points describes neither set.

## Agent executor note

This wiki's reasoning, unmeasured: the arithmetic is executor-independent, but the history is not. A line formed on human work says nothing about an agent's board, and changing the model or the review practice changes the process the dots describe.
