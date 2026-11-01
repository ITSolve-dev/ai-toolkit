---
title: Monte Carlo from Daily Throughput
category: periods
summary: Forecast how many items fit by a date, or when a number of items will finish, by sampling days of finished-item counts; one run adds a sampled count per day, a thousand or two runs give a spread, and the probability is read from the high end for a count and from the low end for a date. It takes no estimate as input, and its count covers right-sized items only.
tags: [method, forecasting, throughput, flow-metrics, iterations, probabilistic]
sources: [flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Monte Carlo from Daily Throughput

This method answers two questions from the same history: how many items will finish in a span of time, and when a given number of items will finish. Its input is the count of items finished per day. [[monte-carlo-simulation]] records the general method and Siemens' version, which samples Cycle Time and gives no recipe. This page is the recipe, from [[flow-metrics-scrum-teams]], where a question of "how many" calls for a rate: "you should immediately think “Throughput”." (L860).

The alternative it replaces is dividing remaining items by the average rate. The book's example is ten items in two weeks and fifty left, which gives ten weeks and no chance attached (L804-L812). That failure is on [[forecast-from-an-average]].

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

The book wants the choice shared: "both the Developers and the PO should have equal input into what percentile each Sprint should be planned to." (L966). On a project of a few people that is one person ([[choosing-a-service-level-expectation]]). This wiki reads the plugin's job as reporting several lines with a stated default, so the choice stays with the person steering.

## Choosing the window

This rule also chooses. Its input is which stretch of history resembles what is coming, and it is read from board history and from what the people steering know has changed. The book gives two heuristics and calls the practice "definitely more art than science" (L862).

- **Recent over old.** More data is not simply better, because of recency. The amount is "a minimum of 10-12 data points and ideally as much as 20 points as a comfortable minimum" (L864), and the data point is a day, so two two-week periods give 28 of them (L870). The book calls the figure a rule of thumb and gives no derivation. What it does and does not settle is on [[how-much-flow-data]].
- **Recent is not always right.** The book's cases are a period following Christmas and New Year, and November in America (L872). This wiki transfers the point: for a few people steering an agent, the likely break is a change of model or of review practice, and a window should not cross it ([[forecast-needs-a-stable-process]]).

Because a run costs nothing, several windows can be tried (L872). This wiki reads a large gap between two defensible windows as something to report, and not to average away.

## Conditions on the result

- **The future has to resemble the past.** "The dirty little secret of MCS is that we are assuming that the future we are modeling roughly looks like the past we have data for." (L862). The book then calls this safe under professional Scrum. This wiki does not accept that, and the check stays on [[forecast-needs-a-stable-process]].
- **The count covers right-sized items.** The results say how many right-sized items can be done, and not that any item can be pulled (L1022). See [[right-sizing]].
- **It does not name items.** "the MCS will not tell you which items you can get done in the next Sprint, it will only give you the minimum capacity to plan for." (L1020). This wiki leaves that to the order ([[reprioritize-before-each-iteration]]).
- **It counts the cut.** A count means what it meant in the history only while items are cut the same way. This wiki notes that a change in how finely work is cut changes the rate without changing the work ([[flow-metrics]]).
- **Days are drawn independently.** The book calls this algorithm "just one such option" (L876). This wiki notes what it assumes: a project that finishes in batches, closing items at a review sitting or a period's end ([[stair-steps-on-a-cfd]]), does not have independent days, and sampling days one at a time spreads the batches evenly and narrows the result. Sampling whole weeks or whole periods would keep the batches at the cost of fewer points. That remedy is ours and is untested.
- **Some events are not in any history.** The book's example is a pandemic, and it adds that such events "would undermine any forecasting technique" (L996).

## Comparing a fixed scope with a forecast

Where scope is fixed, read it against the lines. The book's example projects 60 days out (L1428).

| Scope | Against the forecast | Reading |
|---|---|---|
| 120 items | 95% chance of at least 129 (L1434) | Inside the high-confidence line, so the date looks safe |
| 170 items | The 50% line is at 172 (L1436) | "almost a coin-flip" (L1436) |

At the second reading the book's options are to delay a release, cut scope, remove delays, or add people, of which it says "That last one (almost) never works." (L1436). The levers are on [[changing-the-plan-without-changing-the-date]] and [[reduce-wip-before-raising-throughput]]. Which form applies at all depends on which factor is fixed ([[date-driven-vs-feature-driven]]). The book says a fixed scope is the real case only sometimes, naming "legislative requirements or contractual agreements" (L1384).

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

## Agent executor note

This wiki's reading, unmeasured. The arithmetic needs only finish dates, so it survives an agent executing and needs nothing from anyone. What the input means changes. An item finishes when the people steering accept it ([[started-and-finished-points]]), so on an agent board the history counts accepted results, and it measures the review rate more than the run rate. A board of a few people also has many zero days, so 28 days can hold few finishes, the count moves in coarse steps, and the tail is poorly known ([[how-much-flow-data]]). People who review in sittings produce the batches noted above.
