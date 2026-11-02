---
title: Monte Carlo Forecast from Flow History
category: periods
summary: Forecast how many items fit by a date, or when a number of items will finish, by sampling days of finished-item counts; one run adds a sampled count per day, a thousand or two runs give a spread, and the probability is read from the high end for a count and from the low end for a date. It takes no estimate as input, and its count covers right-sized items only. The output is a set of outcomes with probabilities, not one date (Siemens HS committed near the 85th percentile); it is only as good as its data, needs a stable process (arrivals far outpacing departures, or a triangle on the scatterplot, say to question the history first; balanced arrivals are not enough), and fails when the model assumes a policy the process does not follow (one unmodelled pull order moved an 85th-percentile forecast from 65 to 100 days).
tags: [method, forecasting, throughput, flow-metrics, iterations, probabilistic, planning-a-date, release, rule, board-health, flow-debt, failure-mode, pull-order, wip-limit, policies]
sources: [flow-metrics-scrum-teams, vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Monte Carlo Forecast from Flow History

This method answers two questions from the same history: how many items will finish in a span of time, and when a given number of items will finish. Its input is the count of items finished per day. The section on Vacanti's earlier book, below, records the general method and Siemens' version, which samples Cycle Time and gives no recipe. This page is the recipe, from [[flow-metrics-scrum-teams]], where a question of "how many" calls for a rate: "you should immediately think “Throughput”." (L860).

The alternative it replaces is dividing remaining items by the average rate. The book's example is ten items in two weeks and fifty left, which gives ten weeks and no chance attached (L804-L812). That failure is on [[forecast-range-and-probability]].

## The procedure

1. **Collect finished counts per calendar day.** "The probability distribution is simply the set of historical daily completion rates of PBIs." (L860). The unit is the day, and "Yes, weekends count" (L870). The book's sample history is "2, 1, 2, 2, 0, 1" (L1392). This wiki reads a day with no finish as data, so leaving out the zeros overstates the rate, and it leaves out tagged exits for the same reason ([[non-standard-departure]]).
2. **Choose the window of history**, as below.
3. **Make one run.** For each day of the span, draw a random day from the history and add its count, for example a 3 on the first day and a 5 on the second (L874). The total at the end of the span is one possible outcome.
4. **Repeat.** "For most Sprint Planning, we’ve found 1,000-2,000 runs gives pretty good results." and "Anything much more than 10,000 doesn’t usually provide much better quality." (L886).
5. **Tally the totals into a histogram.** The chance of one outcome is the height of its bar divided by the number of runs (L902).
6. **Read it at a chosen probability**, as below.

For a fixed number of items, step 3 counts down instead of adding up. A run ends when the items are gone, and its result is the number of days. The book's worked run takes 10 items from that six-day history and draws 2, 0, 2, 1, 2, 2, 1, which finishes on day 7 (L1394-L1402). The book adds "But this isn’t a probabilistic forecast yet." (L1408) and goes on to repeat the run.

## Reading the result

The two forms read in opposite directions.

| Question | Fixed | A run ends at | Read from | More confidence means |
|---|---|---|---|---|
| How many by this date? | The span | The end of the span | The high end: runs reaching this count or more (L932) | Fewer items (L938) |
| When will these finish? | The number of items | The items running out | The low end: runs finished by this day (L1408) | More days |

This wiki states the consequence for anyone computing it: the 85% count is the 15th percentile of the run totals in ascending order, and the 85% date is the 85th percentile. **Sign of a misread:** a count that rises with its stated probability.

The book names the forms "How Many" (L1422) and "When" (L1390), and it uses the first for two spans, a period and the time until "your time and/or budget runs out" (L1422).

Its figures show what a reader needs to be told. They are one illustration, with 10,000 runs of a 14-day period (L910), and the charts behind them are lost.

| Reading | Figure |
|---|---|
| Exactly 18, the single likeliest outcome | 6.56% (L910) |
| 18 or more | 50% (L924) |
| 12 or more | 85% (L938) |
| About 1 or more | 99% (L952) |

A forecast states the range and its probability, as in "We have a 50% chance of getting 18 or more PBIs to done in this Sprint" (L958). The rule is on [[forecast-range-and-probability]]. The wording of a middle line also needs care: the book warns that "in 50% of the projections you delivered UP TO 172 items. This is not a 50/50 chance of delivering exactly 172 items." (L1436).

## Choosing the probability

This rule chooses a level of risk. The book offers these settings from practice, with no measurement (L954).

| Setting | Probability |
|---|---|
| Starting out | The 85th percentile, which "many teams" find a balance (L954) |
| Prototyping or greenfield work | "something like 70% (or even 50%)" (L954) |
| Government regulations, or fines or penalties for being late | "up closer to 95%" (L954) |
| Most situations | Not 99%: "planning to 99% is absurd." (L954) |

The book wants the choice shared: "both the Developers and the PO should have equal input into what percentile each Sprint should be planned to." (L966). On a project of a few people that is one person ([[service-level-expectation]]). This wiki reads the plugin's job as reporting several lines with a stated default, so the choice stays with the person steering.

## Choosing the window

This rule also chooses. Its input is which stretch of history resembles what is coming, and it is read from board history and from what the people steering know has changed. The book gives two heuristics and calls the practice "definitely more art than science" (L862).

- **Recent over old.** More data is not simply better, because of recency. The amount is "a minimum of 10-12 data points and ideally as much as 20 points as a comfortable minimum" (L864), and the data point is a day, so two two-week periods give 28 of them (L870). The book calls the figure a rule of thumb and gives no derivation. What it does and does not settle is on [[how-much-flow-data]].
- **Recent is not always right.** The book's cases are a period following Christmas and New Year, and November in America (L872). This wiki transfers the point: for a few people steering an agent, the likely break is a change of model or of review practice, and a window should not cross it (see the stability precondition, below).

Because a run costs nothing, several windows can be tried (L872). This wiki reads a large gap between two defensible windows as something to report, and not to average away.

## Conditions on the result

- **The future has to resemble the past.** "The dirty little secret of MCS is that we are assuming that the future we are modeling roughly looks like the past we have data for." (L862). The book then calls this safe under professional Scrum. This wiki does not accept that, and the check stays, in the stability precondition below.
- **The count covers right-sized items.** The results say how many right-sized items can be done, and not that any item can be pulled (L1022). See [[right-sizing]].
- **It does not name items.** "the MCS will not tell you which items you can get done in the next Sprint, it will only give you the minimum capacity to plan for." (L1020). This wiki leaves that to the order ([[reprioritize-before-each-iteration]]).
- **It counts the cut.** A count means what it meant in the history only while items are cut the same way. This wiki notes that a change in how finely work is cut changes the rate without changing the work ([[flow-metrics]]).
- **Days are drawn independently.** The book calls this algorithm "just one such option" (L876). This wiki notes what it assumes: a project that finishes in batches, closing items at a review sitting or a period's end ([[reading-a-cfd]]), does not have independent days, and sampling days one at a time spreads the batches evenly and narrows the result. Sampling whole weeks or whole periods would keep the batches at the cost of fewer points. That remedy is ours and is untested.
- **Some events are not in any history.** The book's example is a pandemic, and it adds that such events "would undermine any forecasting technique" (L996).

## Comparing a fixed scope with a forecast

Where scope is fixed, read it against the lines. The book's example projects 60 days out (L1428).

| Scope | Against the forecast | Reading |
|---|---|---|
| 120 items | 95% chance of at least 129 (L1434) | Inside the high-confidence line, so the date looks safe |
| 170 items | The 50% line is at 172 (L1436) | "almost a coin-flip" (L1436) |

At the second reading the book's options are to delay a release, cut scope, remove delays, or add people, of which it says "That last one (almost) never works." (L1436). The levers are on [[replanning-on-new-knowledge]] and [[starting-more-work]]. Which form applies at all depends on which factor is fixed ([[fitting-stories-into-a-release]]). The book says a fixed scope is the real case only sometimes, naming "legislative requirements or contractual agreements" (L1384).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Finished items per day | Board history: the date each item crossed the finished point, with tagged exits left out |
| The window | Chosen, and stated in the output |
| The span, or the number of items | The calendar, or the open items |
| The probability | The person steering, with a stated default |

The forecast was wrong if, over later periods, the share reaching the stated count sits far from the stated probability. At 85%, about one period in seven falls short by design, so a single miss proves nothing. A run of misses points at the window or at a process that has changed.

## Cost

It needs a history before it can say anything, and it replaces a point estimate's sum with one number per probability. It also moves work and does not remove it, since the size check remains ([[dropping-estimates-for-flow-forecasts]]). The book's claim that a good tool does this in minutes (L1000) concerns meeting time, and it does not apply to a plugin that computes it from history.

## Monte Carlo in Vacanti's earlier book, and Siemens HS

Monte Carlo simulation is a forecasting method that reaches a result by running many experiments with random inputs and not by computing the answer directly. Vacanti describes it at its simplest as "experiments with random numbers" and says it is "normally applied to highly uncertain problems where direct computation is difficult, impractical, or impossible" ([[vacanti-actionable-agile-metrics]] L3658). In this wiki it is one way to answer when work will finish from board history, next to the velocity route in [[velocity-range-forecast]], and it is the method for several items where [[service-level-expectation]] covers one.

### The procedure

The source gives the general pattern by quoting Wikipedia (L3670-L3676):

> 1. Define a domain of possible inputs.
> 2. Generate inputs randomly from a probability distribution over the domain.
> 3. Perform a deterministic computation on the inputs.
> 4. Aggregate the results.

Vacanti does not teach the modelling itself: "The intricacies and practices about how to model and simulate knowledge work using the Monte Carlo Method are well beyond the scope of this book", and he sends readers to Troy Magennis' work on Lean Forecasting (L3678). This page therefore records what makes a simulation usable and how one organization ran it, not how to build one. The chapter uses "Monte Carlo Simulation" and "The Monte Carlo Method" interchangeably (L3684), and this page follows it. A later book by the same author does teach the modelling for one input, counts of items finished per day, and that recipe is the one at the top of this page.

### What it produces

The output is a spread of outcomes, not an answer. In Vacanti's words, "there is no one predicted outcome", and "Sampling a probability distribution will lead to thousands of possible outcomes" (L3746), each of which then has to be analysed for how likely it is. The chapter's worked figures are accordingly read at a stated percentile, the 85th (L3730).

This wiki reads a Monte Carlo forecast handed over as a bare date as having lost what the method produced: the percentile is part of the claim. See [[forecast-range-and-probability]].

### Data or an assumed distribution

The chapter splits simulations into two cases, with data and without (L3684). Without data "you are forced to choose a probability distribution", a choice Vacanti says "quickly gets into a philosophical debate" and sets aside as academic (L3684). His advice for both cases is one rule:

> if you have the data, use the data. If you do not have the data, then get the data (mine it or measure it), and use the data.
>
> — [[vacanti-actionable-agile-metrics]], L3688

A chosen distribution is allowed only as a stopgap: a first simulation may start from one, but "you should quickly do what you can to gather real data to replace the original artificial distribution in your model" (L3688).

The discriminating test is therefore whether the project has flow history at all. That data also has a condition: to "gather real data" means to measure "the basic metrics of flow" (L3690, see [[flow-metrics]]) from a process that is not unstable, which the stability precondition below covers.

### How Siemens HS ran it

Siemens HS adopted the method after its Cycle Times stabilized ([[siemens-hs-case]]). The argument against the alternative: "velocity forecasts attempt to apply a deterministic methodology to an inherently uncertain problem" (L4214). The source contrasts two inputs: the simulation "provides a distribution of likely completion timeframes instead of an average velocity linear based forecast", and Cycle Time metrics "are not based on an average" but "on distributions of actual Cycle Times" (L4202). See [[forecast-range-and-probability]] and [[velocity-range-forecast]].

1. Reach a stable Cycle Time first; see [[conservation-of-flow]].
2. Take the distribution of historical Cycle Times, as a histogram from best to worst case (L4202-L4214). The chapter's example covers 30% of stories at 9 days or less, 410 stories, and the next 20% at 10 to 16 days, 225 stories.
3. Simulate the project "hundreds of times" (L4214).
4. Read completion dates at different percentiles.
5. Commit: "Our practice is to commit to the date which is closest to the 85<sup>th</sup> percent likelihood" (L4214).
6. Rerun during the release for risk analysis and what-if questions (L4224).

The chapter does not list the other inputs, such as remaining item count or how parallel work is modelled, and it names no tool configuration, so it does not suffice as a recipe. The Throughput form at the top of this page does.

**The commitment rule's input and test.** The rule takes the forecast distribution as input, built from board history. What would show it wrong is a run of committed dates missed well beyond the expected rate. This wiki notes that an 85% date means roughly one commitment in seven is late by design, so one miss proves nothing. The source reports the model "proved extremely predictive" (L4224), with no hit rate and over one release run in parallel with points, so this is a report and not a measurement.

**What-if use.** Facing a large scope increase, the program planned to add two Programmers, but "The modelling tool pointed to adding a Tester to the team rather than adding programming." (L4224). The source does not explain how the tool reached this, so this wiki keeps it as an example of the use and not as evidence for the capacity choice. See [[reading-a-cfd]].

**A simpler neighbour.** The source also describes taking average Throughput from the CFD to "calculate an end date based on the number of stories remaining in the backlog" (L4192). This wiki notes the tension: it is the same linear, average-based arithmetic the chapter faults in velocity forecasts, only with item counts and not points. It is cheap and usable as a rough check, and it gives one date with no likelihood; see [[forecast-range-and-probability]].

### When to rely on it

This wiki assembles the chapter's advice into a rule that chooses. The assembly is ours; each input is the source's.

- **Input, flow metrics of finished work.** Read from board history. The chapter's examples use Cycle Time (L3698, L3730).
- **Input, whether the process is stable.** Read from the cumulative flow diagram and the Cycle Time scatterplot, per the stability precondition below.
- **Input, the policies actually in use.** Read from the project's stated rules and from what board history shows against them, per the section on mismatched assumptions below.
- **What later fact shows the choice wrong.** Realised Cycle Times at the forecast percentile run past the forecast. The chapter's example is 100 days realised against 65 forecast at the 85th percentile (L3730).

### Cost and limits

- **It has to be kept up.** "Once you have obtained a forecast using Monte Carlo, your job is not done. It is not just set it and forget it." (L3752). The assumptions need managing for as long as the forecast is used, as in the section on mismatched assumptions below.
- **It does not replace judgement.** "No forecasting method is going to be a suitable substitute for either (a) common sense thinking or (b) active management interventions as suggested by new information." (L3758)
- **It depends on a tool.** Vacanti assumes one is in use (L3702), and the tool brings assumptions of its own.
- **It needs a stable history.** Siemens' input was history "that were stable and predictable" (L4232), and this wiki reads a rising Cycle Time trend as making the past a poor sample.
- **This chapter states no minimum amount of data.** Its one remark on scale is rhetorical, about "hundreds of items in your backlog" (L3730). For a few people with few finished tasks, this wiki has no sourced threshold from this chapter below which a simulation stops meaning anything; a source giving one would close this gap. The transfer here is ours: the Siemens histogram rests on roughly a thousand stories across 15 teams, a few people steering an agent may have dozens of finished items, so the tail of the distribution is poorly known ([[how-much-flow-data]]), and [[velocity-range-forecast]] may be all the history supports. [[flow-metrics-scrum-teams]] gives a rule of thumb for the Throughput form, in days and with no derivation, which narrows this gap and does not close it ([[how-much-flow-data]]).
- **False precision.** A percentile date printed without its likelihood is read as a promise; see [[forecast-range-and-probability]].

The chapter on Siemens also uses the model to attach costs to each percentile (L4214); that is dropped here as outside this wiki's purpose.

### Agent executor note on the earlier book's method

This wiki's reading: the method samples whatever history it is given, so it survives an agent executing. The limit is in the stability precondition below: history from before a change of executor or model is a poor sample of the process after it.

## Precondition: a stable process

A forecast built from past flow data is only worth what that data says about the future, so the process that produced it has to be predictable before the forecast is run. Vacanti puts the order plainly: "The first step in building a reliable forecast is to put in place a predictable process such that you can have confidence in the data that you are collecting." ([[vacanti-actionable-agile-metrics]] L3758). The rule is stated for Monte Carlo simulation, but his conclusion applies it to forecasting methods generally: "Even the best forecasting methods, however, are going to be only as good as the data they are based on." (L3758).

### What breaks when it is ignored

A simulation samples the past to stand in for the future. If Cycle Times are climbing, the past is not a sample of what comes next:

> Ever increasing Cycle Times mean that any selection of data from a past timeframe is a poor indication of what might happen in a future timeframe.
>
> — [[vacanti-actionable-agile-metrics]], L3696

The result still comes out looking like a forecast. Of the unstable data in Figure 11.1 Vacanti asks: "Could you throw the Cycle Time data from Figure 11.1 into a Monte Carlo Simulation? Yes. Would the resulting forecast be reasonable? Probably not." (L3698). This wiki reads that as the reason the check has to happen before the run: on this account nothing in the output itself says the input was bad.

The source names this GIGO: "A forecast put together using bad data (from an unstable system, for example) produces something that either no one will like or no one will believe" (L3758).

### The two signs

Each sign raises a question about the data; neither is a verdict. Vacanti hedges them himself, saying such a process "might not be a great candidate" and calling the second one a "smell" (L3690, L3698).

- **Arrivals far outpacing departures on a cumulative flow diagram.** This is the shape of his Figure 7.5, which shows Cycle Times constantly increasing (L3696). Read from board history. What to check: whether work is entering faster than it leaves over the window the forecast would sample. See [[reading-a-cfd]].
- **A triangle-shaped Cycle Time scatterplot.** This is the shape of his Figure 11.1, also "the result of an inherently unstable process" (L3698). Read from board history. What to check: whether items have been left to age while newer ones finish, which is the Flow Debt he blames. See [[reading-a-cycle-time-scatterplot]] and [[flow-debt]].

### Discriminating criterion: balanced arrivals are not enough

The first sign clearing does not clear the second. Matching arrivals to departures, the shape of Figure 7.8, mostly removes the problem of rising Cycle Times (L3696), "However, getting to a process that produces a CFD like Figure 7.8 is not necessarily good enough" (L3698). A balanced diagram can sit alongside a triangle scatterplot, and the culprit there is Flow Debt:

> Large accumulations of Flow Debt destabilize a process and make it imminently unpredictable.
>
> — [[vacanti-actionable-agile-metrics]], L3698

A check therefore has to read both charts. This wiki treats a pass on only one as an unfinished check.

### Applying the rule

This wiki states the rule for the plugin this way, as a reading of the passages above. When a date is to be forecast from history, read both charts over the window to be sampled. If either sign appears, say what it puts in doubt and do not present the forecast as sound until it has been checked. The later fact that would show the data was unsuitable is realised Cycle Times running past the forecast percentile.

### Trade-off

The source accepts that a project may have no suitable data yet, but only as a first step towards gathering it (L3688). This wiki reads the cost as follows: stabilising first delays a forecast someone may be asking for now. Producing one anyway from unstable data buys a number the source expects nobody to believe. A stated range with its doubt named may serve better than either, which is our suggestion and not the source's.

### A claim that the check is unnecessary

A later book by the same author makes the assumption sound free under Scrum: the future looking like the past is, it says, "a safe assumption" in most contexts for professional Scrum (L862), and "you are generally safe (pun intended) to use past data for future predictions" (L1088), both in [[flow-metrics-scrum-teams]]. This wiki does not accept that. The book offers no evidence for it, the claim is conditional on following the framework, and what a few people run here is not Scrum by the Guide's own definition ([[scrum-guide-2020]]). The book also concedes the point in practice by having a project pick its window of history (choosing the window, above). The check above stays, on any setup.

### Agent executor note on stability

The mechanism is statistical and does not depend on a human executor, so it survives an agent executing and a person steering. The transfer here is ours: the same logic suggests that history from before a change in who or what executes the work is a poor sample of the process after it, since the past window no longer describes the process being forecast. The chapter does not discuss this case.

## When the model assumes a policy the process does not follow

A forecast assumption mismatch is the gap between what a forecasting model assumes about how work moves and how work actually moves. Vacanti treats closing it as the main determinant of accuracy:

> Your model’s ability to produce an accurate forecast is going to depend on how well you match your process policies to your model’s assumptions.
>
> — [[vacanti-actionable-agile-metrics]], L3712

He defines process policies as "the day-to-day rules around how you operate your process" (L3708). The point is made about Monte Carlo simulation.

### Assumptions live in two places

The source separates "the assumptions built into your model" from "the assumptions built into how whatever tool that you use" implements them (L3702). The second kind is the harder to see, because a tool can fill in what nobody modelled. In the first example below the tool "defaults to a strict FIFO pull order in the absence of any other policy being modeled" (L3728). Policies can be unstated on the process side too: the same example's random pull order is used "without explicitly stating it" (L3728). This wiki reads that pair as the shape of the failure: an unstated tool default meeting an unstated team habit, with neither visible in the model.

### Case 1: pull order (65 versus 100 days)

The scenario, from the book's Class of Service chapter (L3714), is a Kanban board with Standard and Expedite items, at most one Expedite item on the board, and Expedite items allowed to violate WIP limits and block Standard items (L3726). All of that is modelled correctly. The pull order between Standard items that finish at the same time is not modelled (L3726). The tool assumes FIFO; the real process pulls at random (L3728). See [[fifo-pull-order]].

The result, for Standard items at the 85th percentile: 65 days forecast, 100 days realised (L3730). "Due to that one missed assumption, you have over-optimistically forecast by up 35 days _per item_" (L3730).

These figures belong to that simulated scenario and are not portable. Vacanti adds that the problem "gets multiplied if you have hundreds of items in your backlog" (L3730) but gives no figure. This wiki notes that a per-item percentile gap does not simply add up across items that run in parallel, so the 35 days should not be multiplied by a backlog count.

The discriminating point is that nothing else in the model had to be wrong: the rest of the scenario was specified correctly, and one policy moved the percentile.

### Case 2: open WIP slot not pulled

In Figure 15.2 the Test column has a WIP limit of three and holds one item, three items wait in Development Done, and the board has stayed that way for several days (L3742). The simulation tool never allows that state, since it "automatically and immediately pulls an item from Dev Done to Test whenever Test has space under its WIP Limit" (L3742). Real items therefore age longer than the simulated ones (L3742). See [[wip-control]].

### Observable signs

Each sign raises a question to check, not a finding ([[smell-is-not-a-finding]]).

- **Board state:** a column below its WIP limit while the preceding done column holds waiting items, lasting days (L3742). What to check: whether the model assumes immediate pull.
- **Forecast against fact:** items aging past what the simulation showed (L3742), or realised percentiles running past the forecast ones (L3730). What to check: which policy in use is absent from the model.
- **Board history (our operationalisation, not the source's):** items entering work in an order other than the one they queued in, while the model assumes FIFO. What to check: what order the project actually means to pull in.
- **Tool configuration (our operationalisation, not the source's):** a policy with no modelled counterpart. What to check: what the tool does by default in its absence.

### What to do about a mismatch

The source gives two responses and requires one of them:

> you have to use the assumptions in your model (both explicit or implicit) as actionable interventions to take while you are actually operating your process, or you have to take action to change the assumptions in the model to match the real world as it unfolds.
>
> — [[vacanti-actionable-agile-metrics]], L3744

The source does not say how to choose. This wiki reads it this way: if the modelled policy is what the project wants, make the process follow it, as with pulling promptly into an open slot. If the model describes something the project does not intend or cannot hold, change the model and let the forecast move.

Either way the work continues after the forecast: "You need to actively manage to the assumptions in the model or change the model assumptions based on new information." (L3752). The chapter's takeaways rank this highest: "Most importantly, you have to manage to those assumptions!" (L3778). The trade-off, as this wiki reads it, is that a forecast obliges someone to watch the process it assumed for as long as it is relied on, or it stops being a forecast of that process.

### Agent executor note on mismatched assumptions

The mechanism does not depend on human pace or memory: it depends on any gap between modelled and actual policy, so it survives an agent executing and a person steering. The transfer here is ours: with an agent executing, a person may still be the one who decides what is pulled next or who takes a presented result, so an assumption of immediate pull can fail at those points even where execution itself is quick. The chapter does not discuss this.

## Agent executor note

This wiki's reading, unmeasured. The arithmetic needs only finish dates, so it survives an agent executing and needs nothing from anyone. What the input means changes. An item finishes when the people steering accept it ([[started-and-finished-points]]), so on an agent board the history counts accepted results, and it measures the review rate more than the run rate. A board of a few people also has many zero days, so 28 days can hold few finishes, the count moves in coarse steps, and the tail is poorly known ([[how-much-flow-data]]). People who review in sittings produce the batches noted above.
