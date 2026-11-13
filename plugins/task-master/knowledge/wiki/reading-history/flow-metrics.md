---
title: Flow Metrics
category: reading-history
summary: What the flow measures count and do not; the Kanban Guide requires WIP, Throughput, Work Item Age and Cycle Time, Vacanti treats three of them as common to all flow implementations and claims a chain between them, and all can be read from board history without logged hours.
tags: [concept, flow-metrics, board-history, kanban, wip, cycle-time, throughput]
sources: [kanban-guide, scrum-guide-2020, kanban-playbook-right-sizing, zimmermann-good-bug-report, vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Flow Metrics

Flow metrics are the counts and elapsed times that describe work moving through a workflow. The Kanban Guide requires four measures and calls them "mandatory" (L157). This page is descriptive: it fixes what each one counts, so that other pages can use the names. [[work-in-progress]], [[cycle-time]], [[throughput]] and [[work-item-age]] each have a page of their own.

> - **WIP**: The number of work items started but not finished.
> - **Throughput**: The number of work items finished per unit of time. Note the measurement of throughput is the exact count of work items.
> - **Work Item Age**: The elapsed time between when a work item started and the current date.
> - **Cycle Time**: The elapsed time between when a work item started and when a work item finished.
>
> — [[kanban-guide]], L159-L162

Vacanti names three of the same measures, in the order he reasons about them:

> 1. **Work In Progress** (the number of items that we are working on at any given time),
> 2. **Cycle Time** (how long it takes each of those items to get through our process), and
> 3. **Throughput** (how many of those items complete per unit of time).
>
> — [[vacanti-actionable-agile-metrics]], L448-L452

These are his informal statements, and Chapter 2 gives the definitions ([[vacanti-actionable-agile-metrics]] L600, L652, L722). He calls the three "the metrics common to all flow implementations" and says other metrics may be tracked on top ([[vacanti-actionable-agile-metrics]] L750). Work Item Age is not on his list, although his fourth assumption for [[littles-law]] concerns the average age of WIP ([[vacanti-actionable-agile-metrics]] L974). His later book with Will Seele calls it "by far the most important of all the Flow Metrics to track" ([[flow-metrics-scrum-teams]] L374), and [[work-item-age]] resolves the two rankings.

## What each measures and does not

| Metric | Reads | Applies to | What it does not say |
|---|---|---|---|
| WIP | A count now | Open items | Whether any of them is moving |
| Throughput | A count over a time | Finished items | How large or how valuable the items were, because it counts items and the count depends on the cut |
| Work Item Age | Elapsed time so far | Open items only | How long the item will take; it can only rise while the item is open |
| Cycle Time | Elapsed time, complete | Finished items only | Anything about items still open, so it lags: the oldest open items are not in it yet |

The right-hand column is this wiki's reading, drawn from the definitions. The Guide states the definitions and leaves their limits to the reader.

## Which question each answers

The questions are Vacanti's ([[vacanti-actionable-agile-metrics]] L440-L444, L550).

| Metric | Question |
|---|---|
| Cycle Time | "How long to complete?", which he also gives as “When will it be done?” |
| Throughput | "How many new features am I going to get in the next release?" |
| WIP | No customer question directly; in Chapter 1 it is how a queue is measured |

WIP is the exception among the three. It "does not directly answer any particular customer question, but it is the metric that will most greatly influence the other two" ([[vacanti-actionable-agile-metrics]] L550). He therefore calls it the most important, on two grounds: it is the best predictor of system performance, a claim he defers to later chapters, and the other two are defined in terms of it ([[vacanti-actionable-agile-metrics]] L554-L562). This sets an order of work: boundaries first, then WIP, then the two that follow from it. "Cycle Time and Throughput are always defined in terms of WIP" ([[vacanti-actionable-agile-metrics]] L780).

## The model underneath

Vacanti models a process as a queue: work arrives, work departs, and what lies between is counted. He states this as an assumption and not a result: "one of the fundamental hypotheses of this chapter is that all processes can be modeled as queuing systems" ([[vacanti-actionable-agile-metrics]] L762). The claimed payoff is that the three metrics become linked by [[littles-law]] ([[vacanti-actionable-agile-metrics]] L762-L764).

## The chain he claims

Vacanti links the three in order. A large buildup means "all of that queued work itself takes longer to complete" ([[vacanti-actionable-agile-metrics]] L442). Then:

> The direct consequence of elongated Cycle Times is a decrease in Throughput.
>
> — [[vacanti-actionable-agile-metrics]], L444

This wiki reads the order of cause as running from WIP to Cycle Time to Throughput, which makes WIP the one to act on, since it is the one a project sets directly. Two limits apply to the chain.

- **The throughput step goes beyond the law.** Chapter 1 calls the fall in Throughput a direct consequence, and Chapter 3 says less: "All Little’s Law will say is that an increase in average WIP will result in a change to one or both of average Cycle Time and average Throughput" ([[vacanti-actionable-agile-metrics]] L1086). This wiki reads the second statement as the limit of what the law supports: a project can pile up work and still finish items at the same rate. So read a fall in throughput as a finding to check, and do not infer it from a longer cycle time.
- **Throughput is not value.** The source continues "The less work that gets done, the less value we deliver." ([[vacanti-actionable-agile-metrics]] L444). This wiki reads that as holding only if the items are equally worth finishing, and the table above records that the count depends on the cut.

## What the numbers rest on

All four depend on where a project put its [[started-and-finished-points]]: "started and finished refer to how the Kanban system members have established those points in their DoW." (L166). Two projects' cycle times are not comparable unless those points match.

The Guide also limits their use: "In and of themselves, these metrics are meaningless unless they can inform one or more of the three Kanban practices." (L168). This wiki reads that as a test for reporting: a number that changes no decision about limiting, aging or improving should not be reported as a finding. [[actionable-metrics]] states the fuller test, and it also holds Vacanti's claim that these metrics "will suggest specific interventions" ([[vacanti-actionable-agile-metrics]] L454), which his Chapter 1 supports with a single intervention, stopping new starts ([[wip-control]]).

## Names and definitions

Both sources put the definition above the name. The Guide allows other names for the same measures (L164), so a board calling Cycle Time "Flow Time" means the same thing. Vacanti says "it is the definitions of these concepts that are important—not the names" ([[vacanti-actionable-agile-metrics]] L760). He accepts Work in Process for WIP; Lead Time, Flow Time or Time In Process for Cycle Time; and Completion Rate or Departure Rate for Throughput. His one exclusion is "so long as you do not use the term Velocity!" ([[vacanti-actionable-agile-metrics]] L758), for the reason on [[throughput]].

**Sign (this wiki's reading):** a report or request uses one of these names with no stated boundaries and no stated unit. The question to ask is what starts and stops the clock and what is being counted. Two figures with the same name and different boundaries are not comparable.

## Two ways the numbers mislead

Because the metrics count items, the cut can distort them in both directions. A large task hides work under a count of one ([[hidden-wip-in-large-items]]). Tasks that deliver nothing close fast and look healthy, which the Kanban Playbook calls "the opposite illusion" ([[kanban-playbook-right-sizing]] L20, and see [[component-task-masquerading]]). The Playbook says the two "look completely different in your data" (L20). This wiki reads the second as the harder case: a large task at least shows up as an outlier, while tasks that deliver nothing show up as health, so only reading the tasks catches them.

## What a task's life does not say about its text

Cycle Time does not read the quality of a task. [[zimmermann-good-bug-report]] tested this on 289 developer-rated bug reports from Apache, Eclipse and Mozilla: Spearman correlations between rating and lifetime were between 0.002 and 0.068 (L871). The authors' explanation:

> Often a bug report that gets addressed quicker can be of poor quality, but describes an urgent problem. Also, a well-written bug report can be complicated to deal with and take more time to resolve.
>
> — [[zimmermann-good-bug-report]], L871

This wiki reads that as a limit on any audit by history: a long-lived task is not thereby a badly written one, and a fast one is not thereby well written. The figures concern bug reports and human developers. The mechanism, that urgency and difficulty both move lifetime, does not depend on the executor.

## Read from history

All four come from timestamps of state changes. That matches the charter's position that the time a task lived is read from board history and that logged hours are out of scope. Vacanti agrees on the cost: the metrics "are very inexpensive to gather" and "very easy to manually track using a simple spreadsheet" ([[vacanti-actionable-agile-metrics]] L478). Both ages are elapsed time, so they include nights, weekends, and time nobody touched the item. For an agent-run task that is the point, because the elapsed time includes the time a result sat waiting for a person.

## Positions

**Kanban Guide:** the four are required, and a project may add others (L170). All are measured against its own points.

**Vacanti:** three, and the chain above. He agrees that others may be added ([[vacanti-actionable-agile-metrics]] L750). This wiki sees no conflict, since a project that keeps the three can read age from the same timestamps.

**Scrum Guide:** no metric is required, and the word "velocity" does not occur in it. It mentions forecasting practices and declines to rank them: "Various practices exist to forecast progress, like burn-downs, burn-ups, or cumulative flows. While proven useful, these do not replace the importance of empiricism." ([[scrum-guide-2020]] L202). The input it does name is "past performance" (L222), left undefined. This wiki reads the empirical stance as compatible with all four metrics, and an iteration setup can keep them for free, since they come from the same timestamps.

## Agent executor note

The definitions are counts and timestamps, so they survive an agent executing. Their interpretation does not transfer: a figure formed on a human team says nothing about an agent's board, and Throughput in particular is cheap to raise by cutting finer.

The chain's first step depends on where the queue sits, and this wiki expects it at review and not at execution ([[starting-more-work]]). The second step is weaker still with an agent, because throughput can be held up by parallel runs while individual items wait longer. That reading is unmeasured. The customer questions in the table do not change with the executor, which is why the framing still fits a few people steering an agent.
