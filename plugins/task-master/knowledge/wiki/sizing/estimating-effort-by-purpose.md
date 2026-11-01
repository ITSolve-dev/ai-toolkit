---
title: Estimating Effort by Purpose
category: sizing
summary: How much effort an estimate gets is chosen by the decision it feeds; past a small investment accuracy barely rises, no effort reaches certainty, and a cheap estimate is safe only where delivered results correct it soon.
tags: [rule, estimation, effort-accuracy, trade-off]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Estimating Effort by Purpose

Estimating effort is something to choose, not to maximise. Cohn's claim is that accuracy climbs fast for a small effort, then flattens, never reaches certainty, and eventually falls, so what an estimate is worth depends on the decision it feeds. This rule chooses: it decides how much thought one estimate deserves.

## The rule

Give an estimate the effort its decision needs, and stop there.

> Vary the effort you put into estimating according to purpose of the estimate. If you are trying to decide whether or not to send me a box of cookies as a gift, you do not need a very accurate estimate. If the estimate will be used to make a software build vs. buy decision, it is likely enough to determine that the project will take 6–12 months. It may be unnecessary to refine that to the point where you can say it will take 7–8 months.
>
> — [[cohn-agile-estimating-planning]], L1196

This wiki reads that as a test that can be run on a range: if both ends of the current range lead to the same decision, narrowing it buys nothing. The test is ours. The source gives the example and not the test.

## Why: the effort and accuracy curve

Cohn reads three things off his Figure 6.1:

- **Certainty is never reached.** "No amount of additional effort will make an estimate perfect." (L1198)
- **The first effort buys the most.** "As drawn in Figure 6.1, about 10% of the effort gets 50% of the potential accuracy." (L1198)
- **The curve turns down.** He says that "eventually the accuracy of the estimate declines" (L1198).

The source gives no mechanism for the decline, so this wiki keeps it as an assertion and builds nothing on it.

## Figures and their conditions

The curve is a drawing and not a measurement: "The curve in this graph is placed according to my experience, corroborated in discussions with others. It is not based on empirical measurement." (L1185). So this wiki reads 10% and 50% as the shape of that drawing and does not use them as quantities. The ranges of 6–12 and 7–8 months illustrate a build or buy decision and are not a finding about such decisions.

## What chasing accuracy costs

Cohn traces the pull toward high accuracy to "the simplistic view that we can lock down budgets, schedules, and scope" (L1206). The result he describes is signed requirements, upfront analysis and "detailed project plans that show every task a team can think of", after which "the estimates still aren’t perfect" (L1206).

His answer does not claim that the cheaper estimate is the better one:

> Even though they are less far up the accuracy/effort scale, agile teams can produce more reliable plans because they deliver small increments of fully working, tested, integrated code.
>
> — [[cohn-agile-estimating-planning]], L1208

This wiki reads that as the condition the rule rests on: a cheap estimate is safe because delivered results correct it soon. Where results come rarely, the correction comes late and the case for stopping early is weaker. That conditional is ours.

This wiki notes the trade-off: individual estimates are wrong more often. The rule accepts that and relies on measured fact instead, which is what [[velocity]] reads.

Design discussion is where Cohn locates the overspend: "Some amount of preliminary design discussion is necessary and appropriate when estimating. However, spending too much time on design discussions sends a team too far up the accuracy/effort curve of Figure 6.1." (L1336). His two-minute sand timer is a meeting device and is not kept here. The limit it enforces is.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The decision the estimate feeds: an order, fitting a period, build or drop, a date | Whatever asked for the estimate |
| The current range | The task's step on the project's [[estimation-scale]] |
| Whether the decision differs across the range | Comparing the outcome at each end of the range |

The choice was wrong in one of two ways. Too little effort shows as a decision reversed after work started, for a reason a short look would have found. Too much effort shows as a narrower estimate and an unchanged decision, or as a design produced during estimating and changed afterwards. Both signs are this wiki's reading of the source's argument.

## Agent executor note

The curve describes people thinking about work, and no source here measures it for an agent. The range test concerns the decision and not the estimator, so this wiki expects it to survive. The cost side shifts: producing an estimate becomes cheap, and the cost moves to the person who reads and corrects it. The transfer is ours: precision a decision does not use still spends the steering person's attention.

## Related

Effort is also saved by leaving distant work coarse, on [[estimating-by-horizon]]. Splitting further to get a better number can make it worse, on [[over-disaggregation]]. The size at which a large number should be cut instead of refined is on [[size-ceiling]]. Why a trade-off needs an estimate at all is on [[tradeoff-needs-cost-and-benefit]].
