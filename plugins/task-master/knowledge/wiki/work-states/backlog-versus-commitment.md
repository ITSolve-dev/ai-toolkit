---
title: Backlog Versus Commitment
category: work-states
summary: A backlog is a container of candidates, not committed or prioritized work; commitment happens just in time, when capacity exists, so a backlog belongs inside a process's boundaries, and on its CFD, only if it really has been committed, a choice that moves the start of Cycle Time. Commitment means small-c effort, flow through to completion, and a communicated range with a probability; flow commits per item from measurement, Scrum per sprint from estimation. The started point is never earlier than commitment and sits where capacity is first taken.
tags: [decision-rule, work-states, ordering, cfd, flow-metrics, kanban, scrum, rule, commitment, pull-system, service-level, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Backlog Versus Commitment

A backlog holds candidates, and an item is committed only once the project has taken it on with capacity to do it. Vacanti objects less to backlogs than to what the word implies. In his experience people assume two things ([[vacanti-actionable-agile-metrics]] L1468-L1472):

1. "That items placed in a backlog are somehow committed to (or that they otherwise inherently have value)"
2. "That items placed in a backlog are somehow prioritized."

His position:

> A backlog, therefore, is merely a convenient container for these candidate ideas. Commitment does not happen until a team actually has capacity, and prioritization does not happen until at the time of commitment
>
> — [[vacanti-actionable-agile-metrics]], L1474

The just-in-time mechanics are deferred to his Chapter 8 (L1480), set out below. This wiki takes the discriminating criterion to be whether the item has been committed to, and not whether it is written down. On a board the commitment has a place: the arrivals column on [[started-and-finished-points]].

## On a chart

A backlog band is the visible form of this decision, because Property #1 of the [[cumulative-flow-diagram]] makes the top line the arrivals. Plotting a backlog says its items have arrived.

> If you do not want to signal that items in your backlog have been committed to, then do not include a backlog band on your chart. If you do want communicate that backlog items have been committed to, then, by all means, display the backlog. That decision, as we are about to see, could have serious ramifications for your Cycle Time calculation.
>
> — [[vacanti-actionable-agile-metrics]], L1482

The source holds both that "any diagram that shows a backlog is not a CFD" for the most part (L1464) and that one "could definitely have a CFD that looks like Figure 4.16" subject to all the properties (L1482). This wiki reads the second as the rule and the first as the usual case: a backlog is a legitimate band exactly when it lies inside the process boundary, and usually it does not. A backlog plot can still be useful as something other than a CFD: "I am not saying that a chart that shows a backlog is not useful—far from it." (L1484).

The Cycle Time consequence is promised and not worked through in that chapter. This wiki reads it from Property #1: if the backlog is the top band, arrival is entry into the backlog, so Cycle Time starts there and includes all the waiting among candidates. See [[started-and-finished-points]].

## The rule

| Input | Read from |
|---|---|
| Where the project says commitment happens | The project's stated [[started-and-finished-points]] |
| Whether items in the pile are in fact worked in the order and on the terms stated | Board history |

Keep anything before commitment out of the process, out of flow metrics, and off the CFD. The started point is not earlier than commitment, and [[started-and-finished-points]] places it where capacity is first taken: entry to a WIP-limited arrivals column, or the take where there is none. Under a pull setup the two coincide. Where they differ (iterations, push), the started point is the capacity test and the time between commitment and start is read separately.

**Sign of violation:** a CFD band or a metric's start falls in something that "sounds like" a backlog (L1530); or Cycle Time is dominated by the time before any active state; or a long list of unstarted items is read as a promise. Each raises a question and is no verdict, per [[smell-is-not-a-finding]].

**What would show the choice wrong:** items past the supposed commitment point are routinely dropped, which means commitment happens later than stated; or items outside it are treated as owed, which means it happens earlier.

## Which holds under which setup

The resolution here is this wiki's. The source says the principles apply to Scrum or XP style processes as well (L1248) and does not map them.

- **Flow:** commitment is the pull into the first started state, which fits the source directly, and it is also the started point.
- **Iterations:** commitment falls at the selection for the period, so the pile before it stays outside the boundary. Selection bounds what may start in the period and is not the started point: [[started-and-finished-points]] keeps the capacity test, and the wait between selection and start is time in the period's plan, not Cycle Time.
- **Push:** Vacanti's commitment is the stakeholder's expectation (L584), earlier than capacity. This wiki keeps the started point at capacity, as on [[started-and-finished-points]], and reads the time since the expectation as the wait the requester felt.

## Just-in-time commitment

Vacanti's Chapter 8 places the promise to do a piece of work at the moment it is pulled under explicit capacity, as late as possible:

> In a pull system, work is not “committed to” when it is placed in the backlog! It is only committed to in a just-in-time manner as determined by the team’s explicit capacity.
>
> — [[vacanti-actionable-agile-metrics]], L2268-L2274

### Backlog versus Ready

An item in the backlog is an option. In Vacanti's board, an item in Ready is a promise: "The placement of a work item in the Ready column means that the item has been both prioritized and committed to" (L2282). A candidate that "has not been pulled in yet" remains free to be reordered or skipped (L2318). This wiki reads that as a test for a board's columns: a column that holds items nobody has promised is not the commitment point, whatever it is called. Vacanti's Ready is also where "started" begins, since its limit bounds how many new items "can be started" (L2256), so this wiki reads a promised range as counted from that entry. See [[started-and-finished-points]].

### What commitment means

Vacanti's body text gives three aspects (L2276-L2280), while the chapter's takeaways count two (L2362-L2364), dropping the first, which qualifies the word rather than adding content:

1. **Small "c".** "There should be no severe penalty for missing a commitment", yet the team does everything in its power to meet it (L2276). Consequences for individuals are out of scope for this wiki. What is kept is that a miss is a data point, not a broken contract.
2. **Flow through.** Once started, the item is expected to go all the way to completion, which is [[conservation-of-flow]] stated as a promise (L2278).
3. **A range and a probability, communicated.** The customer's first question is when it will be done, and the commitment point is where it is answered (L2280), in this form:

> “we expect this item to flow all the way through the process and exit in 14 days or less with an 85% probability of success”
>
> — [[vacanti-actionable-agile-metrics]], L2282

This wiki reads the 14 days and 85% as an example of the wording, not a target. The form is what the source calls a Service Level Agreement, with setting it deferred to its Chapter 12 ([[service-level-expectation]]). "Everything in its power" starts with choosing a range and probability that are achievable (same page), and with [[conditioning-flow]] (L2316).

### Signs

The source gives the principle; the signs are this wiki's transfer, and each raises a question rather than a verdict:

- A date or promise is attached to an item still in the backlog: commitment happened before capacity was known.
- Items sit in the commitment column with no range ever given.
- More items were promised than the column's bound on [[wip-control]] admits: commitment was not determined by capacity.
- Committed items are regularly dropped: the commitment came earlier than knowledge justified. Check against [[non-standard-departure]].

### Flow versus Scrum

Vacanti rejects the claim that Kanban has no commitments and locates the difference in the unit and the basis (L2288):

| | Scrum | Flow-based |
|---|---|---|
| Unit | "made at the sprint level" | "at the individual work item level" |
| Basis | "based more on upfront estimation and planning" | "based more on measurement and observation rather than planning and estimation" |

This wiki notes that Vacanti's Scrum is a team committing to "some number of stories" (L2288). That matches Cohn's position and not the 2020 Scrum Guide, which commits to a goal and only forecasts the selection, so the table's Scrum column should be read with [[commitment-over-a-period]].

**Resolved per setup, the wiki's own reading.** The setup chosen for the project decides which form is meaningful. With iterations, commitment is over the period, in the form [[commitment-over-a-period]] sets out, and rests on estimates and past periods, so per-item dates would claim more than the method does. With pull, commitment is per item and needs a measured [[cycle-time]] history. Vacanti notes the two can mix, suggesting Scrum users adopt flow-based principles (L2288). With too little history for a pull setup, this wiki reads the honest output as the Kanban Guide's best guess, labelled as a guess, and not a range presented as measured ([[service-level-expectation]]).

### Trade-offs

The source names no cost. This wiki reads the cost as giving up early dates: a stakeholder wanting a promise before work is pulled gets none under this rule, or gets a forecast labelled as such. The opposite failure is a commitment made with little notice of what capacity held.

The commitment is made to a customer by whoever steers, not by an executing agent, so the concept survives. This wiki reads its "all reasonable effort" part (L2282) as changing meaning: for an agent it reduces to not starting what cannot be finished and surfacing a block, since an agent does not push harder. The range depends on measured history and is unaffected.

## Tension with ordering

The claim that "prioritization does not happen until at the time of commitment" (L1474) sits against the pages in `ordering`, which rank a pile ahead of time. This wiki reads a rank on uncommitted items as a proposal for the next commitment decision: useful, cheap to change, and owed to nobody. On that reading Vacanti's point survives as the warning that a rank is not a promise. See [[estimate-is-not-a-promise]] for the same separation applied to size.

## Agent executor note

The distinction between a candidate and a commitment does not depend on the executor. "Capacity" does. An agent can start nearly anything, so capacity on such a board is more plausibly the person's ability to steer and review, as [[wip-per-executor]] considers. That reading is ours and untested.
