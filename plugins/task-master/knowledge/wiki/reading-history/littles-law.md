---
title: Little's Law
category: reading-history
summary: The relationship of averages that locks WIP, Cycle Time and Throughput together over a completed period; its value lies in its assumptions, which are checked against board history for a window (exact when WIP is zero at both ends, five assumptions otherwise), written as policies on starting, finishing, unblocking and pull order, and audited in a running process. Mixing velocity into it as Throughput is the classic unit error.
tags: [concept, flow-metrics, wip, cycle-time, throughput, retrospective, method, predictability, conservation-of-flow, stability, rule, policy, pull, board-rules, policies]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Little's Law

Little's Law is the relationship among average [[work-in-progress]], average [[cycle-time]] and average [[throughput]] that holds for a queuing system over a period, provided the law's assumptions hold. John Little gave the first rigorous proof of the arrival form in 1961 ([[vacanti-actionable-agile-metrics]] L830, L850). Vacanti's position is that the arithmetic is the least useful part: "It is all about the assumptions." (L1002). Those assumptions are checked on *Checking Little's Law's Assumptions* (below) and turned into rules on *Process Policies from Little's Law* (below).

## The forms

| Equation | Form | Stated in terms of |
|---|---|---|
| (1) | L = λ * W | Arrival Rate. L is average items in the system, λ is average arrivals per unit time, W is average wait time in the system (L834-L842) |
| (2) | CT = WIP / TH | Departure Rate, the form the Lean and Kanban community adopted (L876, L904) |
| (3) | TH = WIP / CT | Rearrangement of (2) (L890) |
| (4) | WIP = CT * TH | Rearrangement of (2) (L896) |

Equations (1) and (2) are logically equivalent as mathematics (L922), but they are not equivalent in what must be true for them to apply. Vacanti gives this its own callout:

> Looking at Little’s Law from the perspective of Throughput rather than from the perspective of Arrival Rate necessitates a change in the assumptions required for the law to be valid.
>
> — [[vacanti-actionable-agile-metrics]], L950

This wiki reads the consequence as follows: the everyday form on a board, Equation (2), is the one with the longer list of conditions.

## What it asserts

It is a relationship of averages, and "average" here means arithmetic mean (L830, L844). Vacanti says most knowledge-work discussions neglect this, and that the fact is only harmful when the law is used for something it was not meant for (L844). Little's own framing, as quoted by Vacanti:

> Little’s Law will not tell the managers how to handle trade-offs or provide innovations to improve their chosen measures, but it lays down a necessary relation.
>
> — [[vacanti-actionable-agile-metrics]], L850

Given any two of the three averages, the third follows (L852). Little's example is a wine rack that holds 100 bottles on average and is replenished at 2 bottles a week. A bottle therefore spends 50 weeks in the rack on average. The result needs no individual dates, no knowledge of ordering, no probability distributions and no bottle sizes (L854, L860).

This any-two property matters little on a board, because history already holds all three: "the three flow metrics’ data is so easy to capture that you should never have to compute one of them—just go look at the data!" (L998). This wiki reads that as follows: computing a value the board already records is not analysis. The useful act is comparing the board's behaviour with the assumptions.

## What it does not assert

- **It does not forecast.** The exact relation applies looking back over a completed period: "Little’s Law is about examining what has happened in the past." ([[vacanti-actionable-agile-metrics]] L3550). Its use on a forecast stops at a qualitative gut check; see [[forecast-range-and-probability]].
- **It does not say which metric moves.** Changing one metric will almost certainly affect one or both of the others (L908), and the law does not determine which. See [[starting-more-work]] for what this does to the usual advice.
- **It does not require equal-sized items.** See [[size-spread]].

## Segmenting by work type

WIP may be split into types such as user stories, production defects and maintenance requests, and the law then applies to the whole system "as well as to each type or groups of types" (L1036). The practical use Vacanti names is diagnostic: ask which segment is violating the assumptions, for example defects alone, or defects grouped with maintenance requests (L1038). He defers segmenting by [[class-of-service]] to his Chapter 13 and warns that its effect on predictability is "usually bad" (L1040).

## Agent executor note

This wiki's reading, not the source's: the relation does not depend on who or what performs the service. Little's definition covers any stream of discrete items that arrive, wait, receive service and depart, and it explicitly allows for service that is not the bottleneck (L822). The arithmetic therefore carries over unchanged to an agent executing and a person steering. What changes is where the queue forms, which is likely at the person's review rather than at execution. That placement is an untested transfer. A team should read it from its own board history, not assume it.

## Checking Little's Law's Assumptions

This method tests whether the Throughput form of the law can be trusted for a chosen window of board history. Vacanti treats the assumptions, not the formula, as the substance of the law, and every process policy he derives from it comes from them ([[vacanti-actionable-agile-metrics]] L1000-L1004, L1016).

### Step 1: find which case applies

| Situation | What is required | Standing of the result |
|---|---|---|
| Arrival form, Equation (1) | Steady state (stationary processes), an arbitrarily long observation period, consistent units (L934-L938) | Holds under those conditions |
| Throughput form, WIP is zero at both ends of the window | A start and end with zero WIP, and everything that enters eventually exits (L954) | Exact |
| Throughput form, WIP never reaches zero | All five assumptions below (L966-L976) | Holds if they hold; otherwise an estimate |

The second case is the strong one: "Little’s Law is exact between any two time instances where total process WIP is zero" (L954). It needs no assumption about stability or about the length of the period. Vacanti notes separately that consistent units are needed in every form (L988).

### Step 2: check each assumption over the window

The five assumptions and their grouping are Vacanti's (L968-L976, L986). The signs are this wiki's reading of where each one shows in board history, because the source defers how to read them to its Chapters 7-9. A sign raises a question, not a verdict.

| # | Assumption | Notion | Sign to read from board history |
|---|---|---|---|
| 1 | Average Arrival Rate equals average Departure Rate | [[conservation-of-flow]] | Items entering the process exceed items leaving it across the window |
| 2 | All work started eventually completes and exits | Conservation of flow | Items closed without finishing, or items open since long before the window with no movement |
| 3 | WIP is roughly the same at the start and the end of the window | Stability | The open-item count differs noticeably between the two ends |
| 4 | Average age of WIP is neither rising nor falling | Stability | Mean age of open items at the end of the window differs from the start |
| 5 | Cycle Time, WIP and Throughput use consistent units | Arithmetic | A calculation mixes units; see below |

### Step 3: read the result by project setup

This section is the wiki's own resolution, built on the source's cases.

- **A sprint or project that closes with an empty board:** the exact case applies. Vacanti's examples are an ideal project and canonical Scrum, where "by definition you start each sprint with zero WIP and you end each sprint with zero WIP", with the caveat that "practice usually falls far short of prescription" (L954).
- **A sprint with carry-over:** this is the five-assumption case. Unfinished sprint work is one of Vacanti's own examples of never running out of WIP (L962). The Scrum label does not earn the exact result; an empty board at both ends does.
- **Continuous flow, or several concurrent streams:** the five-assumption case applies (L962).
- **A few people steering an agent:** this wiki's unverified expectation is that a small batch may genuinely drain to zero between batches, which would make the exact case more common than Vacanti's teams found it. The check is the board: whether the open count actually reached zero.

### When an assumption fails

A failed assumption does not void the calculation: the law "can still be used as an estimation", but "the “goodness” of the estimation depends on how badly the assumptions have been violated" (L978-L984). Vacanti's stronger claim is that the cost is paid whether or not anyone computes the law:

> Every time you violate an assumption of Little’s Law your process becomes less predictable.
>
> — [[vacanti-actionable-agile-metrics]], L1006

He says the cost may appear as longer Cycle Times, more variability or both, and that it may not appear at once: the data "may be showing you a rosier picture of the world than is really occurring", and a forecast built on it can be much too optimistic (L1006-L1012). This wiki reads one way that can happen as follows: Cycle Time is measured on finished items, so items left ageing do not yet count against it, and the finished set looks healthy while assumption 4 is failing. The source does not give this mechanism in this chapter.

### The same checks as a policy audit

The steps above test a window of data. Vacanti's *Getting Started* chapter turns the assumptions on the policies that produce the data, asking which "are in direct violation of the assumptions of Little’s Law" (L3800). The stake is the same: "each violation of one of Little’s Law’s assumptions hampers your ability to be predictable" (L3800).

The questions appear at L3800, and the same three appear as rules in the book's closing summary (L3934-L3938). The right column is this wiki's reading of where each shows up. *Process Policies from Little's Law* (below) states the positive form.

| Policy check | Rule | Where to look |
|---|---|---|
| Are arrivals explicitly controlled? | "Do not start new work at a faster rate than you finish old work." (L3934) | Items started per period against items finished per period; a WIP count that keeps rising |
| Does everything started complete? | "Minimize the amount of work that is started but never finishes." (L3938) | Items cancelled after their arrival date; items abandoned in an active state with no recorded outcome |
| Do items age arbitrarily? | "Do not allow items to age arbitrarily due to blockages, too much WIP or poor pull policies (Class of Service)." (L3936) | Open items much older than others of their kind, especially ones blocked or passed over by newer work |

The source gives softer forms that matter for reading the result. The second check allows a fallback: make sure everything started completes, "or at least tag and track items that do not complete properly" (L3800). This wiki reads that as follows: an item cancelled with a tag stays explainable in history, and an untagged one looks like an ordinary completion ([[capturing-flow-data]], [[non-standard-departure]]). Ageing is listed with its causes: "Class of Service, blockages, queuing, etc." (L3800).

The instruction is modest: "you may want to think about changes to implement to get your process more aligned with that law" (L3800). It sets no threshold, so a breach here is a question about a policy and not a defect to be scored ([[smell-is-not-a-finding]]). The chapter states the checks without deriving them, and it gives no figure for what a violation costs.

This wiki's reading for a few people steering an agent: an agent can start tasks faster than a person can review them, so the first check is the one most likely to fail between execution and review, and reading it means counting work waiting on the person as open ([[blocked-work-counts-against-wip]]).

### Failure mode: mixed units

Vacanti reports a Scrum team that plugged velocity in story points per sprint in as Throughput, used the count of stories completed in the sprint as WIP, and expected a Cycle Time in days (L988-L994). The numbers did not come out as they expected. Throughput must be items per the same time unit in which Cycle Time is expressed, and average WIP must be averaged over that same unit (L988).

- **Sign:** a flow calculation takes [[velocity]] as its Throughput, or its inputs carry different time units or different counted things.
- **What breaks:** the output has no meaning in the unit it is reported in.
- **Discriminating test:** velocity counts points; Throughput here counts items.

### Trade-offs

The check needs a chosen window, and its result may change with that choice, because assumptions 3 and 4 compare the window's two ends. This wiki suggests recording the window alongside any finding. Violations can also be legitimate: Vacanti allows that they are sometimes "unavoidable or even necessary" (L1014). The aim of the check is to know a violation is happening and what it costs, not to forbid it.

## Process Policies from Little's Law

The assumptions of the law can be stated as explicit policies for how a board runs. Vacanti's argument is that predictability is designed through such policies and not computed from a formula: "The design of your process is really just the sum of all the policies you have in place" ([[vacanti-actionable-agile-metrics]] L1024). A process that conforms, or mostly conforms, gives data the team can start to trust, and only then is it probabilistically predictable (L1088-L1094).

### The policies

Vacanti offers four, as examples and not a complete list (L1018). The pairing with assumptions is this wiki's reading, because the source derives them from the assumptions as a set; the numbers refer to *Checking Little's Law's Assumptions* (above).

| Policy (L1018) | Assumption served | Sign of violation in board history |
|---|---|---|
| "We will only start new work at about the same rate that we finish old work." | 1, arrivals equal departures | Starts exceed finishes across a window |
| Finish what is started and minimize discarded items, which needs "some notion of late-binding “commitment”" | 2, everything started exits | Items abandoned part-way, especially late in the flow |
| Unblock blocked work as quickly as possible | 3 and 4, stable WIP and age | Blocked items whose age keeps rising |
| "We will closely monitor our policies around the order in which we pull items through our system so that some work items do not sit and age unnecessarily." | 4, age not rising | Old items passed over while newer ones finish |

The chapter's conclusion puts the same matters as questions to ask of a running process: why work flows in faster than it flows out, why items age through blockages or poor pull policies, and why work is abandoned part-way "(and how you account for that abandonment)" (L1112). The audit of a running process's policies against these is on *Checking Little's Law's Assumptions* (above), and the pull-order policy is on [[fifo-pull-order]].

### What breaks when they are ignored

Vacanti says every violation reduces predictability, and that the data may hide this for a while (L1006-L1012). Interventions then stop producing the results expected of them: the payoff of conformance is that actions "will result in outcomes more closely aligned with our expectations" (L1106).

### The loop

Vacanti quotes Frank Vega: "your policies shape your data and your data shape your policies" (L1026). In Vacanti's account, policies influence the data collected, and that data then points at where the policies are deficient (L1026).

### Trade-offs and limits

- **Following them has a cost.** Vacanti says that lowering WIP "feels uncomfortable" (L906) and that taking control of these policies "will mean saying no to customer requests to start new work immediately" (L234). Requests wait outside the process while the team finishes.
- **Violations will happen.** Some are "unavoidable or even necessary"; the aim is not to "compound those uncontrollable events" with ones that could have been prevented (L1014).
- **Unmeasured abandonment.** This wiki reads the parenthetical about accounting for abandonment (L1112) as a warning: if discarded items simply vanish from the data, assumption 2 appears to hold when it does not.

### Which setup this applies under

The resolution is this wiki's. The first policy is a rate, and [[wip-control]] is a bound on a count; a project under a bound that holds meets the rate as a consequence, since nothing starts until something finishes. So under a flow setup the first policy is checked through the bound. Under an iteration setup with no WIP control there is no bound to rely on, so the policy is read directly from starts against finishes inside the period.

### Agent executor note

This wiki's reading, not the source's: starting is close to free for an agent, so the first policy is easier to violate, not harder. Several items can begin at once while finishes stay gated by the person who reviews them. On that reading, the rate to match is the rate at which results get accepted, not the rate at which the agent produces them. This transfer is untested. It would be shown wrong if a board's finishes kept pace with its starts at much higher concurrency.

## Steps to Predictability

The closing summary of *Actionable Agile Metrics for Predictability* compresses the book into a four-step loop: set policies, collect data, visualize it, act on it ([[vacanti-actionable-agile-metrics]] L3930-L3962). Its goal is an answer to the question "When will it be done?" (L3964); see [[good-plan-test]].

### The steps

1. **Set process policies** "based on the assumptions of Little’s Law—including policies around how you define the boundaries of your process" (L3932). Do not start work faster than old work finishes, do not let items age arbitrarily, and minimize work that is started and never finished (L3934-L3938). See *Checking Little's Law's Assumptions* (above), *Process Policies from Little's Law* (above) and [[started-and-finished-points]].
2. **Collect the basic metrics of flow** as the process runs: Work In Progress, Cycle Time, Throughput (L3940-L3946). See [[capturing-flow-data]] and [[flow-metrics]].
3. **Visualize them** in Cumulative Flow Diagrams and in Cycle Time Scatterplots and Histograms (L3948-L3950). See [[cumulative-flow-diagram]], [[cycle-time-scatterplot]] and [[capturing-flow-data]].
4. **Use the analytics to take action:** "Intervene when your process goes awry", "Identify improvements to policies to improve performance", and "Make forecasts" (L3952-L3962). See [[percentile-intervention-triggers]], [[actionable-metrics]] and [[forecast-range-and-probability]].

### Why the order matters

The source lists the steps without arguing for the sequence. This wiki reads it as a dependency chain, since each step consumes the one before: metrics are undefined without boundaries, a chart inherits the faults of its data ([[capturing-flow-data]]), and an action or forecast inherits the faults of its chart.

The sign of a skipped step, in this wiki's reading, is a chart or forecast nobody can trace back to a stated boundary or to per-state dates. That raises a question to check; see [[smell-is-not-a-finding]].

### What is not kept

The source says "I promise that you will be predictable" (L3964). This wiki drops that as an assertion with no mechanism, so the page's weight rests on the individual steps.

The source's other point is about timing: "any delay in implementing these principles severely hampers your ability to be predictable" (L3966). This wiki reads the usable part as [[how-much-flow-data]]: starting does not have to wait for a large sample.

### Agent executor note

This wiki's reading: the loop does not depend on a human executor. For the plugin, its first three steps are preparation of material and the fourth is the person's call: charts can flag a problem, and the decision to intervene stays with whoever steers.

### See also

[[good-plan-test]], [[diagnosing-unfinished-work]], [[what-may-move]], [[vacanti-actionable-agile-metrics]]
