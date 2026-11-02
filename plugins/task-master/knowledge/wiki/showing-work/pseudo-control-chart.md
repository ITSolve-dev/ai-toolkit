---
title: Pseudo Control Chart
category: showing-work
summary: A cycle time chart with mean and standard-deviation bands labelled UCL and LCL, sold as a Control Chart; it and any percentage printed beside its lines assume normally distributed data that a Histogram of real cycle times does not show, it is pulled by outliers, and it flags items as out of control on that false footing.
tags: [failure-mode, visualization, cycle-time, flow-metrics, charts, percentiles, statistics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Pseudo Control Chart

A pseudo control chart is a cycle time chart that draws the arithmetic mean and horizontal bands at one, two and three standard deviations, calls the outer lines the Upper and Lower Control Limits, and names the result a Control Chart ([[vacanti-actionable-agile-metrics]] L2694-L2696). The source calls this a misnomer and says the approach has a fatal flaw. Chapter 16 repeats the warning for tools: "Your tool may call its Scatterplot a “Control Chart”—which it most certainly is not" (L3908).

## Observable sign

A report or tool shows cycle time with any of these:

- lines labelled mean, ±1σ, ±2σ, ±3σ, UCL or LCL, or "something like “mean plus one standard deviation” or “µ + σ”" (L3908)
- a claim that 68.2% of dots lie within one standard deviation, or over 99% within three (L2698)
- a percentage printed next to such a line, which "is going to be based on an assumption that your data is normally distributed" (L3908)
- items named "out of control" because they sit above the UCL or below the LCL (L2698)

The sign raises a question and is not a verdict ([[smell-is-not-a-finding]]). The check is below.

## Why it breaks

> These charts—especially the calculations for the UCLs and LCLs—assume that your data is normally distributed. I can all but guarantee you that your Cycle Time data is not and will not be normally distributed.
>
> — [[vacanti-actionable-agile-metrics]], L2710

The consequence the source draws is that "the conclusions based on the standard deviation calculations above when applied to your non-normally distributed data will be incorrect" (L2710). The shape it describes for cycle times is "a big hump on the left and a long tail to the right" (L2796); see [[cycle-time-scatterplot]].

Chapter 16 states the cost: "Using the mean plus a standard deviation (or the mean plus any number of standard deviations) approach and then associating the result with percentiles is dangerous given that your data is not normally distributed. You will get calculation errors that are not insignificant and you will potentially make poor decisions based on bad data." (L3916). The source gives no size for that error. This wiki's reading is that the harm reaches planning when such a line is read as a commitment, for example "85% of tasks finish within N days" taken from a σ line and not from the data. See [[service-level-expectation]].

The second defect is that "both of those statistics are heavily influenced by outliers" (L2726). The source's illustration is the saying that if Bill Gates walks into a bar, everyone there is a millionaire on average. So one very long item shifts the mean and widens the bands.

The name is also wrong. The source says these charts are not Control Charts in the Shewhart tradition (L2708), and gives its reason for the method's spread as familiarity: "that is the type of statistics that that most of us are familiar with" (L2712).

## What the source does and does not reject

It separates two claims, and this wiki keeps them separate.

- **Firm:** the mean-and-deviation chart is mislabelled and rests on a false assumption.
- **Open:** whether true Shewhart charts apply to knowledge work: "I am not saying they are definitely not; I am just saying I have not yet been convinced" (L2708). Statistical process control is outside the book (L2588), and Chapter 16 again leaves why they are "probably not applicable to knowledge work" as "beyond the scope of this book" (L3908).

So a finding should not say Control Charts are invalid for this work. It should say that this chart's limits assume a distribution the data does not have.

## How to check it

The source's own test is the Histogram: "the shape of a normal distribution is a bell curve. When you look at your Histogram you will see that your data does not follow a bell curve pattern" (L3914). The source "can guarantee" the data is not normal (L3908). This wiki keeps the check and not the guarantee, since a sign here is a question: plot the histogram of the project's own cycle times ([[cycle-time-scatterplot]], its histogram form), and if it is not bell-shaped, the printed percentages do not mean what they say.

This wiki's further checks, derived from the source's argument, need only the same cycle times.

1. **Count the band.** Compare the claimed 68.2% with the actual share of dots inside ±1σ. The source says the claim is unreliable on this data and does not give a test; this is the test.
2. **Look at the lower limit.** With a long right tail, the mean minus two or three deviations can fall below zero, which is an impossible cycle time and a visible sign the model does not fit.
3. **Remove the longest item and redraw.** If the mean and limits move visibly while the percentile lines do not, the chart was reporting the outlier.

## What to do instead

Replace the bands with [[cycle-time-percentile-lines]], which need no assumption about the distribution (L2722). [[capturing-flow-data]] covers the check on a tool's output.

## Cost of the fix

This wiki notes what is lost. The pseudo chart at least offers a one-line verdict about which items are unusual, and percentile lines offer none: a dot above the 95th line is expected about one time in twenty. Deciding which dots deserve a question then falls to reading the chart, and the source takes that up as qualitative analysis in its next chapter (L2738); see [[reading-a-cycle-time-scatterplot]].

## Agent executor note

The defect is arithmetic and does not depend on the executor. This wiki adds one caution, unmeasured: agent-run items that wait on human review may have a more pronounced tail, which would make a normal assumption worse.
