---
title: Started and Finished Points
category: work-states
summary: The two defined moments between which a task counts as work in progress, which Vacanti calls a process's arrival and departure points and tells a team to name first; every flow metric hangs from them, so each has to be an event the board can show and not a claim by the executor. Started is where capacity is first taken: entry to a WIP-limited arrivals column where the board has one, otherwise when the agent takes the task; an arrivals column is optional when nobody outside must be coordinated. Finished is where the process's responsibility ends, counted even if not shown. Crossings are counted on their real dates, whatever an iteration is doing.
tags: [decision-rule, work-states, definition-of-done, kanban, scrum, commitment-point, pull, push, flow, arrivals-column, arrivals, departures, done, done-column, ready-column, backlog, explicit-policy, throughput, board-setup, wip-limit, flow-metrics, wip]
sources: [kanban-guide, scrum-guide-2020, montgomery-tracker-smells, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Started and Finished Points

A task is work in progress from the moment it crosses a defined started point until it crosses a defined finished point. The Kanban Guide makes these points part of the minimum definition of a workflow:

> A definition for when work items are started and finished within the workflow. Depending on the work item, your workflow may have more than one started or finished point.
>
> — [[kanban-guide]], L111

The Guide's next element gives the points their consequence: "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). The Guide then ties all four metrics to them: "For these four mandatory flow metrics, started and finished refer to how the Kanban system members have established those points in their DoW." (L166).

This wiki reads that as saying the points are the most consequential choice on a board. They decide what [[wip-control]] counts and what every number on [[flow-metrics]] means. Vacanti treats the same two points as a process's boundaries, its arrival point and departure point, and calls defining them "the crucial starting point in predictable process design" ([[vacanti-actionable-agile-metrics]] L596). He adds that the step is "a necessary (but unfortunately not sufficient) step down the road to predictability" ([[vacanti-actionable-agile-metrics]] L592). Without them the arrival rate of [[conservation-of-flow]] cannot be counted: "Any predictable process needs a clear, unambiguous point at which it considers items to have “arrived”." ([[vacanti-actionable-agile-metrics]] L2202), and the same holds for "departed" (L2204).

## The decision

The Guide lets each project define the points and does not say where they belong. The test below is this wiki's.

- **Started** is the first moment the task takes up capacity. On a board with a WIP-limited arrivals column, that is entry to that column, because a slot on a limited column is capacity (see the arrivals column, below). Otherwise, with an agent executing, it is when the agent takes the task.
- **Finished** is the first moment nothing more is owed on the task, and the board can show it as an event. An executor's report that it is done is not such an event, because it only states what a check is supposed to establish ([[testable-acceptance]]).

## Name the boundaries first

Vacanti tells a team beginning with flow metrics to name the boundaries before anything else: "the very first thing you need to do to get started is define the boundaries of your process" ([[vacanti-actionable-agile-metrics]] L3786). Decide three things, in this order.

1. **The arrival point.** "you must first decide on a point at which you consider work to have entered (or arrived to) your process" (L3786).
2. **The departure point.** The matching point at which work is considered to have exited (L3786).
3. **Which items between them count as WIP.** The choice belongs to the people running the process, and it is meant to be revisited: "make that choice and start tracking. As with anything, you can always tweak that decision later as you learn more" (L3798).

The boundaries are what make WIP a countable thing: "any work items between these two boundaries can be considered WIP" (L3786). Without them, the arrival rate, the departure rate and Cycle Time have no defined start or end, so [[flow-metrics]] cannot be read. This wiki reads the same dependency downstream: a malformed [[cumulative-flow-diagram]] is often a boundary problem, because the top and bottom lines of the chart are defined as cumulative arrivals and departures (L3904).

## Arrival: pull against push

Vacanti's arrival point is where "a unit of work transforms from being just some arbitrary idea into being a legitimate work item that is to immediately be acted on and completed" ([[vacanti-actionable-agile-metrics]] L574-L580). Before it the item is a candidate, and after it the item counts as WIP until it departs. He gives two ways of placing it.

| | Pull system | Push system |
|---|---|---|
| What starts work | The team has capacity and takes the item | A request, regardless of capacity |
| Arrival point | The team's first pull transaction ([[vacanti-actionable-agile-metrics]] L582) | When any stakeholder has a reasonable expectation that the work is committed ([[vacanti-actionable-agile-metrics]] L584) |
| How hard to define | Fairly easy | Much harder |

The discriminating test is whether the people doing the work chose to take the item. In a pull system an item counts only "if it has been voluntarily pulled into the process by the individual, team, or organization responsible for operating that process" ([[vacanti-actionable-agile-metrics]] L582). In a push system the expectation counts "whether the team responsible for performing the work knows about it or agrees to it or not", and it may arise because the work was requested, a project was funded, or a manager thinks it is a good idea to start ([[vacanti-actionable-agile-metrics]] L584). For a push system he says the best first exercise is to define the boundaries at all ([[vacanti-actionable-agile-metrics]] L592). He also calls the pull arrival point the point of "commitment", deferring the details to his Chapter 8 ([[vacanti-actionable-agile-metrics]] L582); that is on [[backlog-versus-commitment]].

Most backlog items fall outside: "for the most part—when I talk about WIP, I do not include backlog items in that discussion" ([[vacanti-actionable-agile-metrics]] L624). He flags this as a subtlety tied to the point of commitment and does not resolve it in this chapter.

## The arrivals column

On most boards the arrival point has a board form: "an explicit and obvious entry point where teams can pull in new work such that it is counted as WIP" (L2014). It usually takes the form of a WIP-limited first column named “Input”, “Ready”, “To Do” or the like (L2014-L2020). Placing an item there is “a clear, unambiguous signal to the world that the team has accepted work.” (L2026)

### The three policies

The source makes these explicit (L2036):

1. An item has arrived only once it is placed on the arrivals column.
2. The column has a WIP limit, and new work is pulled in only when that limit signals capacity. How the limit is set is on [[constant-wip]].
3. Work can arrive only through this column, so downstream steps may pull only from it.

### Arrivals column versus backlog

This wiki takes the discriminating criterion to be whether the place represents capacity or demand. [[backlog-versus-commitment]] holds the argument about the backlog itself.

| | Arrivals column | Backlog |
|---|---|---|
| Purpose | Work the team has accepted | Candidate requests |
| Size | Bounded by a WIP limit | Unbounded |
| Counts as WIP | Yes | No |
| Shown on a CFD | Yes | No (L2028) |

The column “is not meant to be an ever-expanding repository for all candidate customer requests.” (L2028) Its limit represents “the real-time capacity of the system to take on new work” (L2028).

### Why it matters

The source ranks this as one of the most important columns, if not the most important, for two reasons (L2184-L2188):

- **Throttle.** It is “the throttle by which we constrain the amount of work that can arrive to our system at any given time.” (L2186)
- **Commitment.** It acts as "our “commitment” point to start new work", with the implication that "when new work is committed to, we expect it will flow completely through the process and depart the system." (L2188)

This wiki reads the commitment clause as the meaning of moving an item here: placing an item on the column is a claim that it will be finished, not a note that it might be.

### Where the clock starts on such a board

Vacanti counts an item as WIP from the column, before anyone has touched it; its limit bounds how many new items "can be started" (L2256). This wiki reconciles that with the capacity test by reading a slot on a limited column as capacity, so on a board with such a column the clock starts at the column, and time waiting there counts as Cycle Time. The reconciliation is ours. On an unlimited first column the slot means nothing, so the column is a backlog under another name and the started point falls later, when the agent takes the task.

### Signs on the arrivals column

Each sign raises a question to check. These signs are this wiki's application of L2014-L2036; the source states the policies, not their signs.

- The first column has no limit, or its count only grows: it is probably a backlog under another name.
- Items appear in a working column without having passed through the first column: policy 3 is not held, and arrivals are being undercounted.
- Items sit on the first column for a long time, or are often removed from it: the column may be storing candidates and not commitments.
- Nothing on the board distinguishes requested from accepted, so the Arrival Rate cannot be read at all.

Which items go on the column, and in what order they leave it, is deliberately left out of Vacanti's Chapter 7 (L2176). The definition concerns a boundary, not who does the work, so this wiki keeps it unchanged for a person steering an agent.

## When an arrivals column is needed

A board usually has an explicit arrivals column, but “an explicit arrivals column is neither prescribed nor required for predictable process design.” (L2170)

**The test.** The input is whether pulling new work needs coordination with someone outside the team. It is read from how the project's priorities are set.

- **The column may be superfluous** when a team can “pull new work items in an immediate, ad hoc manner”, because “you need no coordination with any external stakeholder to prioritize items or you have a proxy for those stakeholders embedded with your team.” (L2162)
- **Keep the column** otherwise. This wiki reads the default this way because the column is then where the coordinated decision lands, a reading the source implies but does not state.

**What holds balance without the column.** The requirement does not go away. Dropping the column means arrivals are matched to departures by [[constant-wip]] alone: per-step limits, one global limit, or a mix (L2168). The arrival point itself also remains required, since Arrival Rate must still be counted (L2202). This wiki reads the first working column as taking that role, so the moment an item is pulled into it is the moment it arrives.

**Trade-offs.** The source says even such a team “could benefit from an arrivals column” but does not say why here (L2170). What is lost, per the two reasons it gives elsewhere, is a named throttle and a visible commitment signal (L2186-L2188).

**What would show the choice wrong.** This wiki reads these as the later facts, unsourced: WIP drifts upward, since nothing visible throttles intake; or people outside the team begin asking which items have been accepted, so the signal the column gave turns out to be needed.

**Setup note.** A few people steering an agent, with priorities decided by those same people, fit the first case on the source's test. This wiki reads the column there as optional and not forbidden: the choice should be made at project setup and stated, not left implicit.

## Departure

Departure may be delivery to an end user or to a downstream team or process ([[vacanti-actionable-agile-metrics]] L594). His example is a choice by responsibility: a team that deploys its own work counts an item as departed once deployed to production, and a team that does not counts it as departed once handed off to operations ([[vacanti-actionable-agile-metrics]] L594). Chapter 7 repeats the requirement: "define the exact point of the system where work departs, (hopefully) never to return" (L2050), with the same two examples (L2050). The source gives no test beyond these examples; this wiki reads the examples as one, where the process's responsibility ends, read from the project's setup and not from column names. The examples also show that the line need not mean the work reached a user, so a board's cycle time and throughput are only comparable to figures measured with the same line.

### What the departure point requires

- **It must be counted, not necessarily shown.** Items past the point “do not necessarily have to be visualized” but “they do need to be counted” (L2050). Most teams give it board space, titled “Done”, “Deployed” or similar.
- **It has no WIP limit.** If shown, the column typically carries none (L2050, L2082).
- **It needs an explicit policy.** The expectation is that the team “has put in place a set of policies for what it means for items to move from Test to Deployed” (L2060); see [[column-doneness-criteria]].
- **It releases capacity.** Once across, “they no longer count against the capacity of the team; i.e., they no longer count as WIP.” (L2060)

The source ties value and measurement to this line: “It is only when work departs our system that customer value can truly be recognized and our predictability be assessed.” (L2188) This wiki adds the consequence: without the line, items leave WIP at no defined moment, so neither the Departure Rate nor the finish date of an item means anything. The Departure Rate, and with it [[throughput]], is a count of items crossing this line.

For a person steering an agent, the choice is whether acceptance of an agent's result falls inside the system. This wiki chooses a finished point that sits with a check or with the person reviewing, and not with the executor's own statement (agent note, below); see also the note on [[conservation-of-flow]].

## Boundaries are independent of iterations

The boundaries do not move with a sprint. "it is possible for work to arrive at any time during the sprint and it is possible for work to depart at any time during the sprint" (L3788). So: "any time work comes into your process—regardless of whether it is the beginning of a sprint or not—you need to count that work as arrived" (L3788), and the same holds for departure (L3788-L3796). Vacanti acknowledges this "may seem anathema to Scrum purists" (L3788).

This wiki resolves that per setup. Under an iteration setup, the commitment over the period and the counting of flow are two separate things: the period's plan stays on [[timeboxed-iteration]] and on its plan-versus-fact reading, while arrival and departure are recorded on their actual dates. Selection for the period bounds what may start in it and is not the started point. Under a continuous setup there is no conflict to resolve.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the board has a WIP-limited arrivals column | Board configuration |
| When capacity is first taken up | Entry to that column, if there is one; otherwise board history against the record of runs |
| What has to be true for nothing more to be owed | The project's stated workflow and the task's acceptance check |

The started point is too late if work happens before it: activity on a task appears in history before its started timestamp. The finished point is too early if tasks past it come back, so that history shows a finished task returning to an earlier state. It is too late if tasks sit in the last state with nothing owed on them.

In this wiki's reading, a point is also wrong if the numbers it produces fail to answer the question asked. If a promised date is met by the metric and the customer has received nothing, the finished point sits before the customer's definition of done. If the started point precedes real commitment, waiting that belongs to intake shows up as cycle time. A boundary is also badly placed when a large share of items sit long before or after it in a state nobody counts, since that time is then real waiting that no metric sees; the inputs are the workflow states and the time items spend in each, read from board history. Vacanti names no test beyond continued tuning (L3798).

## Sign of violation

These signs are this wiki's; each raises a question to check and is not a finding ([[smell-is-not-a-finding]]).

- **In board history:** a finished task returning to an earlier state.
- **In board history:** two tasks of the same kind reach the finished point with visibly different evidence, so the point does not mean one thing.
- **In board history:** a task's started timestamp comes after the first activity on it.
- **In board state:** nothing on the board or in its description says which transition means work has started.
- **In board history:** start dates equal creation dates, so items are counted from the moment they were filed. That is the push definition in effect, whatever the board is called.
- **In board history:** items past the started point wait a long time before their first further move. Vacanti's arrival point is for work "to immediately be acted on" ([[vacanti-actionable-agile-metrics]] L580), so this wiki takes that wait as a sign that the point sits too early, or that more has been committed than can start.
- **In board history:** some items leave at merge, some at deploy and some at acceptance, so their cycle times do not measure the same thing.
- **In board history:** no single transition that all finished items cross.
- **In board state:** a "Done" column has no stated policy for entering it, so two items in it may mean different things.
- **In board history:** finished work waits in a state before the line with nobody acting on it: the line may sit past the point where the team's part ended.
- **In board state:** WIP cannot be counted from the board without someone judging which items are in.
- **In board history:** arrival dates cluster on the first day of a sprint and departure dates on the last day, which suggests that work is being counted at the iteration edge and not at the boundary.
- **In reports:** two reports of the same period give different WIP or Cycle Time because each assumed a different start point.

The interviews behind [[montgomery-tracker-smells]] support the first sign, as a perception. Nine participants said scoping is hard, and the authors report that "users might incorrectly assume issues to be done and close them too early, leading to issues needing to be reopened." (L487). Five named the same trouble with status names: P05 asked "what does ‘resolved’ actually mean?" (L431), and P06 said their team "has a definition of ‘done’/‘ready’ that cannot be made transparent in Jira" (L431). This wiki reads the second as a requirement on the plugin: the definition has to be stated somewhere it can read. The study gives no rate of reopening, and a reopened task alone does not show a bad point, since a real defect can surface later.

## More than one point

The Guide allows several started or finished points depending on the item (L111). This wiki reads that as permission for a bug and a feature to differ, and as a warning for comparison: metrics from items with different points do not measure the same thing, so history compares like with like only when the points match. That caution is ours.

## Positions

**Kanban Guide:** both points are the project's to define, per workflow and per kind of item, as above.

**Scrum Guide:** finished is fixed, and started does not exist. The Guide defines one standard across all items: "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product." ([[scrum-guide-2020]] L315). The effect is immediate: "The moment a Product Backlog item meets the Definition of Done, an Increment is born." (L317). The Guide has no started point, because it has no count of open work. This wiki reads selection for a Sprint as not the same as being started; the Guide describes selection and the Sprint Backlog (L226-L228, L295-L297) without saying either way.

Scrum's standard also differs in kind from a task's acceptance check. The Definition of Done applies to every item, while [[testable-acceptance]] is specific to one task, and the Guide does not mention acceptance criteria. This wiki reads the two as complementary: a task is finished when it passes its own check and meets the shared standard.

**Vacanti:** the project defines both, as boundaries of its process, and the definition of departure "holds true whether you are operating a pull or a push system" ([[vacanti-actionable-agile-metrics]] L594). The arrival point differs by system, as above. Crossings are counted on their real dates, whatever a sprint is doing.

## Which holds under which setup

- **Flow setup:** define both points. Every metric needs them. A flow setup pulls, so Vacanti's first pull and this page's capacity test name the same moment: entry to the limited arrivals column if the board has one, otherwise the take.
- **Iteration setup:** one shared standard of done is required. A started point is optional for the guide, but this wiki wants one, because history cannot show age without it. Selection for the period is the period's commitment ([[backlog-versus-commitment]]) and bounds what may start; the started point is the capacity test above, not the selection.
- **Iterations with a WIP control:** both, as a count needs a started point.
- **Work promised before anyone takes it:** the two tests differ, since Vacanti's push arrival comes earlier than capacity is taken up. This wiki keeps the capacity test for the started point, because a count that includes untouched promises gives a bound nothing to restrain, and it reads the time since the promise separately as the wait the requester felt. This departs from Vacanti for push systems, and the departure is ours.

## Trade-offs

This wiki's reading, not a source's: narrow points give shorter, cleaner numbers that omit the waits outside them, and wide points give numbers closer to what the customer feels but mix in time the project does not control. An early arrival point makes Cycle Time include queueing, and it brings a backlog inside the process ([[backlog-versus-commitment]]); a late one gives shorter numbers and hides that wait. A person steering an agent can accept either, provided the choice is written down. Vacanti's related point is that every such figure is relative to perspective ([[vacanti-actionable-agile-metrics]] L680; see [[cycle-time]]).

## Agent executor note

The definitions concern the work and survive. The risk grows with an agent, because an agent reports completion readily and nobody across the desk notices that it did not really finish. This wiki therefore wants a finished point that sits with a check or with the person reviewing, and not with the executor's own statement.

The transfer of Vacanti's "capacity" is ours: with an agent executing, a pull is limited less by the executor than by the attention of the person steering to brief it and check its results, so the pull decision stays with that person.

The charter treats review of a presented result as no wait inside a task, because the executor's part has ended. That concerns where a task is cut, and it does not settle where the finished point sits. This wiki treats the two as separate: if the finished point is set after acceptance, review time counts as cycle time even though it is not a wait inside the task.

See also [[littles-law-assumptions]] and [[capturing-flow-data]].
