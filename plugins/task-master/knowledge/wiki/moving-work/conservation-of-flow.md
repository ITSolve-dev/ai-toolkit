---
title: Conservation of Flow
category: moving-work
summary: Work entering a process should leave it, so start work at about the rate old work finishes, from the outset, and finish what is started; arrivals outpacing departures grow WIP and Cycle Time until no delivery question can be answered, and abandoned work skews the data, though stopping work that is no longer needed is still the right call.
tags: [rule, failure-mode, flow, littles-law, predictability, arrival-rate, departure-rate, abandoned-work, vacanti, stability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Conservation of Flow

Conservation of Flow (CoF) is the principle, in Daniel Vacanti's *Actionable Agile Metrics*, that work entering a process comes out of it. It has two parts, and each is also an assumption of [[littles-law]]: a process takes in work no faster than it lets work out, on average, and nothing started gets lost.

> Little’s Law Assumption #1: The average input or Arrival Rate of a process should equal the average output or Departure Rate.
>
> — [[vacanti-actionable-agile-metrics]], L2006

> Little’s Law Assumption #2: All work that is started will eventually be completed and exit (depart) the system.
>
> — [[vacanti-actionable-agile-metrics]], L2236

“Any time that flow is not conserved, predictability suffers.” (L2008) Checking both against board history is on [[littles-law-assumptions]], and the policies that serve them are on [[process-policies-from-littles-law]].

## First part: arrivals match departures

In plain terms, “we only start work at about the same rate at which we finish old work (on average)” (L2008). This wiki reads the rule as being about averages, so a single week of imbalance does not break it and a sustained gap does.

The source's analogy is an airport where landings exceed take-offs: gates fill, then every reasonable parking space, then the runways, and at that point neither landings nor take-offs are possible (L1990). The general form is that “any time you try to shove items into a system at a faster rate than items can exit the system, you are met with disastrous consequences.” (L2002)

The causal chain in knowledge work runs in three steps (L2174):

1. Arrival Rate above Departure Rate produces “a steady—if not dramatic—increase in WIP”.
2. By Little's Law, the increase in WIP is matched by an increase in [[cycle-time]]. This wiki notes that the step assumes throughput does not rise to absorb the extra WIP, which the source does not state.
3. If WIP grows without bound, so does cycle time, and “how long before this work item will done?” can no longer be answered.

The source calls such a process unpredictable “by definition” (L2174) and says of it: “you have almost no chance at predictability.” (L2128)

### Install it at the start

Matching the two rates is the plainest form of a WIP limit, and the [[siemens-hs-case]] treats it as the precondition for everything else: "limiting WIP can be as simple as making sure that work is not started at a faster rate than work is completed" (L4098). The same passage goes on: "Matching arrival rates to departure rates is the necessary first step to stabilizing a system. Only by operating a stable system could we hope to achieve our goal of predictability." (L4098). The conclusion adds the reason to do it before improvement work: "Continuous improvement in a system that is unstable always runs the risk of improvement initiatives that result in sub-optimizations." (L4260)

Siemens' first Kanban release ran without limits at first, because teams and management resisted them, and it delayed so that they would become "more amenable" (L4100). The old problems returned:

> The delay in implementing WIP limits cost us and in retrospect we should have pushed harder to impose WIP limits from the outset.
>
> — [[vacanti-actionable-agile-metrics]], L4102

Once limits came in, they had "the almost immediate effect of stabilizing the system such that Cycle Times no longer continued to grow" (L4120-L4126), and the process "reached a stable state at about 41 days almost immediately" (L4132). The chapter gives conflicting dates for when this happened; see [[siemens-hs-case]]. This wiki reads delay as having less to offer a few people: there is no 15-team acceptance problem, so the plugin can propose the limit when the board is set up ([[wip-control]], [[board-rules-by-setup]]).

Forecasting depends on the same condition. Siemens' simulations rested on "historical Cycle Time metrics that were stable and predictable" (L4226-L4232), and this wiki reads that as meaning [[throughput-monte-carlo]] should not be trusted on an unstable history.

## Second part: nothing started gets lost

Vacanti's framing image is a skydiver: everything before the jump can still cancel the commitment, the jump happens at the last responsible moment, and after it the expectation is arrival at the ground (L2218-L2222). Two practices follow from a pull system ([[what-may-move]]) and protect this part: [[just-in-time-prioritization]] and [[backlog-versus-commitment]] (L2238, L2360).

The two parts meet. Cycle times do not in practice grow forever: “Projects get cancelled and features get abandoned when they take too long to complete.” (L2190) The source's point is that this makes things worse and not better, because “you cannot even be certain if a certain item that is started will ever finish” (L2196).

Vacanti gives two costs of breaking this part. Effort already spent on a discarded item is lost:

> If work flows only part way through the system and gets kicked out or discarded—for whatever reason—then any effort that was expended on the eliminated item immediately becomes waste.
>
> — [[vacanti-actionable-agile-metrics]], L2334

The second cost is to measurement. When partly finished work is repeatedly dropped in favour of new starts, "the Cycle Time metrics are going be skewed, and the system you are operating becomes infinitely unpredictable" (L2340). This wiki takes "infinitely" as rhetoric and not as a measurement, so it keeps the mechanism and not the magnitude: [[cycle-time]] figures only describe a process if the items measured are the items that entered it.

## Signs

Each sign raises a question and none is a verdict. The source states the violations and gives no detection procedure, so these signs are this wiki's reading.

- **In board history:** over the same interval, more items entered the process than left it, across several intervals, measured as in [[throughput]].
- **On a chart:** the arrival line diverges from the departure line on a CFD, as Siemens saw: "our teams were starting to work on items at a faster rate than we were finishing them" (L4104). See [[cumulative-flow-diagram]] and [[reading-a-cfd]].
- **On a chart:** Cycle Times trend upward across a period on a [[cycle-time-scatterplot]] (L4078, L4102).
- **In board state:** total open work keeps growing, and the age of open items rises with it.
- **In board history:** items cancelled or abandoned after long ages (L2190).
- **In board history:** an item that reached a started state is missing from the board or its history later, so it was deleted and not accounted for. See [[non-standard-departure]].
- **In board state:** a started item keeps ageing with no movement and no decision about it. It has not exited, so whether it ever will is open.
- **In board history:** new items are pulled while earlier started items are discarded, repeatedly. This is the failure Vacanti names: work "constantly started but never finished" (L2334).

## When abandoning is right anyway

CoF is not a rule to finish everything. Vacanti allows exceptions when new knowledge makes work "unnecessary, duplicative, or otherwise wasteful" (L2292), and goes further in his conclusion:

> Some might argue—and I certainly would not debate them if they did—that it is even more waste to continue to work on an item once we have gained information that the item is no longer necessary.
>
> — [[vacanti-actionable-agile-metrics]], L2342

This wiki reads the test as forward-looking: the input is whether the outcome is still needed, as stated in what was learned since the pull, and effort already spent is not an input. Two obligations come with the choice. Ask why it happened and whether something upstream could have caught it (L2292-L2298), and keep the item in the data ([[non-standard-departure]]). Vacanti treats a violation as a learning opportunity (L2306).

## Trade-offs and limits

- **The cost of the first part** is refusing to start work that has been requested, which is why balance needs an explicit control: [[constant-wip]].
- **The second part does not hold alone where commitments are made too early.** This wiki reads the less that was known when work started as the more that can arrive mid-flight, and that as the reason the rule is paired with just-in-time practices and not with pressure to finish.
- **Balance is only a first step.** The source calls it “the first—and probably most important—step” toward balancing demand and supply (L2160), and warns that a balanced picture does not prove health; see [[cumulative-flow-diagram]].
- **Both parts together do not finish the job.** Arrival-departure matching and conserved flow make metrics more reflective of real capability, yet "doing these two things alone still does not guarantee that our system is completely stable" (L2344).
- **Selection is left out.** Vacanti's Chapter 7 deliberately says nothing about which items are chosen at replenishment or the order they are pulled in (L2176-L2182); those belong to `ordering`.

## Agent executor note

The rule is queueing arithmetic and concerns what a board's data can say, not human pace or memory, so this wiki keeps it for a person steering an agent. The transfer here is ours: on such a board the Departure Rate is set by whichever is slower, the agent or the person accepting its results, so a fast agent does not by itself raise departures if finished work waits for acceptance on the wrong side of the departure point ([[started-and-finished-points]]). This wiki also reads discarded agent output as cheaper than discarded human effort, so the waste argument weakens with an agent while the measurement argument stands unchanged.
