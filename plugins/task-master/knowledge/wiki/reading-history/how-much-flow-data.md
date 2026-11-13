---
title: How Much Flow Data Is Enough
category: reading-history
summary: Far fewer finished items than people assume are enough to start reading a process; five bracket the median at 93.75%, the source's eleven-sample figure needs correcting, and a small sample says little about the tail.
tags: [decision-rule, flow-metrics, sampling, cycle-time, rule-of-five]
sources: [vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# How Much Flow Data Is Enough

A process can be read from a handful of finished items, and months of data are not required. Vacanti's answer to "How much data do I need?" is that "less (often much less) data can be good enough" ([[vacanti-actionable-agile-metrics]] L3846), and his closing advice is: "Do not think you need to collect hundreds or thousands of samples over several months to have any confidence in what your data is telling you" (L3864).

## The Rule of Five

The rule comes from Douglas Hubbard's *How to Measure Anything* (L3848):

> Rule of Five – There is a 93.75% chance that the median of a population is between the smallest and largest values in any random sample of five from that population.
>
> — [[vacanti-actionable-agile-metrics]], L3852

This wiki checked the figure: the median escapes only if all five values fall on one side of it, which has probability 2 × (1/2)^5 = 6.25%. The condition is in the wording: a **random** sample from one population. Vacanti's bridge is to "think of your process as a random Cycle Time number generator" (L3854).

This wiki's reading of what that condition excludes:

- **Finish-order bias.** The first five items to finish are not a random sample while longer items are still open, because the short ones finish first. Read the bracket next to the age of open work ([[work-item-age]]).
- **A changed process.** Items finished before a policy or boundary change come from a different population.

## The eleven-sample figure, corrected

The source states that with eleven samples from a uniform distribution "there is a 90% probability that the next sample (i.e., the 12<sup>th</sup> sample) will be between the min and the max of the previous eleven samples" (L3862).

This wiki does not carry that number forward. Its own arithmetic gives a different result: among twelve independent draws, each is equally likely to be the largest or the smallest, so the twelfth falls outside the first eleven with probability 2/12, leaving about 83.3% inside. A 90% result needs nineteen prior samples. The same argument holds for any continuous distribution, so this property is not special to the uniform case, and the source's step from it to "we are going to need more than eleven samples" (L3862) does not follow from non-uniformity alone. This wiki holds that conclusion sound on other grounds, set out under the limit below.

## The decision

The thresholds below are this wiki's reading of the source's numbers, not the source's.

**Input:** the number of items finished inside [[started-and-finished-points]] since the process last changed, read from board history.

| Finished items | What may be said |
|---|---|
| Fewer than five | Show the raw values. State no range. |
| Five or more | The smallest and largest bracket the median, with the Rule of Five's confidence, under its conditions. |
| Eleven or twelve and up | The min and max start to describe the range: with n finished items, the chance of the next one landing inside is (n-1)/(n+1). A first SLE can be read, as on [[service-level-expectation]]. |

**What would show the choice wrong:** the median of a later, larger sample falling outside the first bracket. In a stable process that should happen about one time in sixteen. If it recurs, suspect a changed process or a non-random sample.

## The limit of a small sample

The source is explicit that the rule "only gets us to the median of our population" (L3856), and that non-uniform Cycle Times need "more than eleven samples to gain insight to our world, but not much more" (L3862). This chapter gives no number for that. Its Chapter 12 gives one for a related question, how many points an SLE needs: "As few as maybe 11 or 12. Probably no more than 30." (L3054), conditional on how well the process obeys [[littles-law]].

This wiki's reading is that a small sample says little about the tail: long-running items are rare, so a sample may contain none, and a high percentile drawn from five or ten items should not be quoted as a forecast. The rank arithmetic is on [[cycle-time-percentile-lines]].

## Days of Throughput are not finished items

A later book gives a figure for a simulation:

> the general rule of thumb is a minimum of 10-12 data points and ideally as much as 20 points as a comfortable minimum.
>
> — [[flow-metrics-scrum-teams]], L864

This wiki reads that figure as counting something other than the table above, despite the similar numbers. The book's data point is a day of Throughput, with weekends included, so two two-week periods give 28 (L864-L870). The table counts finished items. A quiet board can meet the first and not the second: fourteen days with three finishes passes the book's minimum and is below this page's five. This wiki applies both, the days so that the simulation has a sample and the items for what may be said about the result. The book gives no derivation for its figure.

The book rejects "more data is better than less data" on grounds of recency (L864). This wiki reads that as agreeing with this page's input, which counts only since the process last changed.

## Agent executor note

The claim is probabilistic and has no human mechanism, so this wiki holds that it survives an agent executing. It matters more at small scale: a few people finish few items, and this rule is what lets the plugin report from them and not decline until a large sample exists. A mix of agent-run and person-run work may be two populations, which is a reason to keep a type attribute ([[capturing-flow-data]]).

## See also

[[service-level-expectation]], [[capturing-flow-data]], [[cycle-time-scatterplot]], [[throughput-monte-carlo]]
