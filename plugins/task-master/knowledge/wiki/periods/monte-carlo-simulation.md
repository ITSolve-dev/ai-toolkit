---
title: Monte Carlo Simulation
category: periods
summary: Forecasting a finish by sampling real flow data many times; the output is a set of outcomes with probabilities and not one date, Siemens HS committed near the 85th percentile, and the method is only as good as its data, its assumptions and the stability of the history behind it.
tags: [method, forecasting, flow-metrics, planning-a-date, release, probabilistic]
sources: [vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Monte Carlo Simulation

Monte Carlo simulation is a forecasting method that reaches a result by running many experiments with random inputs and not by computing the answer directly. Vacanti describes it at its simplest as "experiments with random numbers" and says it is "normally applied to highly uncertain problems where direct computation is difficult, impractical, or impossible" ([[vacanti-actionable-agile-metrics]] L3658). In this wiki it is one way to answer when work will finish from board history, next to the velocity route in [[velocity-range-forecast]], and it is the method for several items where [[single-item-forecast]] covers one.

## The procedure

The source gives the general pattern by quoting Wikipedia (L3670-L3676):

> 1. Define a domain of possible inputs.
> 2. Generate inputs randomly from a probability distribution over the domain.
> 3. Perform a deterministic computation on the inputs.
> 4. Aggregate the results.

Vacanti does not teach the modelling itself: "The intricacies and practices about how to model and simulate knowledge work using the Monte Carlo Method are well beyond the scope of this book", and he sends readers to Troy Magennis' work on Lean Forecasting (L3678). This page therefore records what makes a simulation usable and how one organization ran it, not how to build one. The chapter uses "Monte Carlo Simulation" and "The Monte Carlo Method" interchangeably (L3684), and this page follows it. A later book by the same author does teach the modelling for one input, counts of items finished per day, and that recipe is on [[throughput-monte-carlo]].

## What it produces

The output is a spread of outcomes, not an answer. In Vacanti's words, "there is no one predicted outcome", and "Sampling a probability distribution will lead to thousands of possible outcomes" (L3746), each of which then has to be analysed for how likely it is. The chapter's worked figures are accordingly read at a stated percentile, the 85th (L3730).

This wiki reads a Monte Carlo forecast handed over as a bare date as having lost what the method produced: the percentile is part of the claim. See [[forecast-range-and-probability]] and [[single-date-plan]].

## Data or an assumed distribution

The chapter splits simulations into two cases, with data and without (L3684). Without data "you are forced to choose a probability distribution", a choice Vacanti says "quickly gets into a philosophical debate" and sets aside as academic (L3684). His advice for both cases is one rule:

> if you have the data, use the data. If you do not have the data, then get the data (mine it or measure it), and use the data.
>
> — [[vacanti-actionable-agile-metrics]], L3688

A chosen distribution is allowed only as a stopgap: a first simulation may start from one, but "you should quickly do what you can to gather real data to replace the original artificial distribution in your model" (L3688).

The discriminating test is therefore whether the project has flow history at all. That data also has a condition: to "gather real data" means to measure "the basic metrics of flow" (L3690, see [[flow-metrics]]) from a process that is not unstable, which [[forecast-needs-a-stable-process]] covers.

## How Siemens HS ran it

Siemens HS adopted the method after its Cycle Times stabilized ([[siemens-hs-case]]). The argument against the alternative: "velocity forecasts attempt to apply a deterministic methodology to an inherently uncertain problem" (L4214). The source contrasts two inputs: the simulation "provides a distribution of likely completion timeframes instead of an average velocity linear based forecast", and Cycle Time metrics "are not based on an average" but "on distributions of actual Cycle Times" (L4202). See [[single-date-plan]] and [[velocity-trend-is-not-a-forecast]].

1. Reach a stable Cycle Time first; see [[conservation-of-flow]].
2. Take the distribution of historical Cycle Times, as a histogram from best to worst case (L4202-L4214). The chapter's example covers 30% of stories at 9 days or less, 410 stories, and the next 20% at 10 to 16 days, 225 stories.
3. Simulate the project "hundreds of times" (L4214).
4. Read completion dates at different percentiles.
5. Commit: "Our practice is to commit to the date which is closest to the 85<sup>th</sup> percent likelihood" (L4214).
6. Rerun during the release for risk analysis and what-if questions (L4224).

The chapter does not list the other inputs, such as remaining item count or how parallel work is modelled, and it names no tool configuration, so it does not suffice as a recipe. The Throughput form on [[throughput-monte-carlo]] does.

**The commitment rule's input and test.** The rule takes the forecast distribution as input, built from board history. What would show it wrong is a run of committed dates missed well beyond the expected rate. This wiki notes that an 85% date means roughly one commitment in seven is late by design, so one miss proves nothing. The source reports the model "proved extremely predictive" (L4224), with no hit rate and over one release run in parallel with points, so this is a report and not a measurement.

**What-if use.** Facing a large scope increase, the program planned to add two Programmers, but "The modelling tool pointed to adding a Tester to the team rather than adding programming." (L4224). The source does not explain how the tool reached this, so this wiki keeps it as an example of the use and not as evidence for the capacity choice. See [[bottleneck-on-the-cfd]].

**A simpler neighbour.** The source also describes taking average Throughput from the CFD to "calculate an end date based on the number of stories remaining in the backlog" (L4192). This wiki notes the tension: it is the same linear, average-based arithmetic the chapter faults in velocity forecasts, only with item counts and not points. It is cheap and usable as a rough check, and it gives one date with no likelihood; see [[straight-line-projection]] and [[forecast-from-an-average]].

## When to rely on it

This wiki assembles the chapter's advice into a rule that chooses. The assembly is ours; each input is the source's.

- **Input, flow metrics of finished work.** Read from board history. The chapter's examples use Cycle Time (L3698, L3730).
- **Input, whether the process is stable.** Read from the cumulative flow diagram and the Cycle Time scatterplot, per [[forecast-needs-a-stable-process]].
- **Input, the policies actually in use.** Read from the project's stated rules and from what board history shows against them, per [[forecast-assumption-mismatch]].
- **What later fact shows the choice wrong.** Realised Cycle Times at the forecast percentile run past the forecast. The chapter's example is 100 days realised against 65 forecast at the 85th percentile (L3730).

## Cost and limits

- **It has to be kept up.** "Once you have obtained a forecast using Monte Carlo, your job is not done. It is not just set it and forget it." (L3752). The assumptions need managing for as long as the forecast is used, as in [[forecast-assumption-mismatch]].
- **It does not replace judgement.** "No forecasting method is going to be a suitable substitute for either (a) common sense thinking or (b) active management interventions as suggested by new information." (L3758)
- **It depends on a tool.** Vacanti assumes one is in use (L3702), and the tool brings assumptions of its own.
- **It needs a stable history.** Siemens' input was history "that were stable and predictable" (L4232), and this wiki reads a rising Cycle Time trend as making the past a poor sample.
- **This chapter states no minimum amount of data.** Its one remark on scale is rhetorical, about "hundreds of items in your backlog" (L3730). For a few people with few finished tasks, this wiki has no sourced threshold from this chapter below which a simulation stops meaning anything; a source giving one would close this gap. The transfer here is ours: the Siemens histogram rests on roughly a thousand stories across 15 teams, a few people steering an agent may have dozens of finished items, so the tail of the distribution is poorly known ([[how-much-flow-data]]), and [[velocity-range-forecast]] may be all the history supports. [[flow-metrics-scrum-teams]] gives a rule of thumb for the Throughput form, in days and with no derivation, which narrows this gap and does not close it ([[how-much-flow-data]]).
- **False precision.** A percentile date printed without its likelihood is read as a promise; see [[estimate-is-not-a-promise]] and [[stating-plan-uncertainty]].

The chapter on Siemens also uses the model to attach costs to each percentile (L4214); that is dropped here as outside this wiki's purpose.

## Agent executor note

This wiki's reading: the method samples whatever history it is given, so it survives an agent executing. The limit is on [[forecast-needs-a-stable-process]]: history from before a change of executor or model is a poor sample of the process after it.
