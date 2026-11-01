---
title: Just-in-Time Commitment
category: moving-work
summary: Work is committed to when it enters the process under explicit capacity, not when it enters the backlog; commitment means the item flows through to completion and a cycle-time range with a probability is communicated. Flow commits per item from measurement, Scrum per sprint from estimation.
tags: [rule, commitment, pull-system, scrum, kanban, service-level, work-states, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Just-in-Time Commitment

Just-in-time commitment places the promise to do a piece of work at the moment it is pulled under explicit capacity, as late as possible:

> In a pull system, work is not “committed to” when it is placed in the backlog! It is only committed to in a just-in-time manner as determined by the team’s explicit capacity.
>
> — [[vacanti-actionable-agile-metrics]], L2268-L2274

## Backlog versus Ready

This is the discriminating criterion the source gives for two neighbouring states, and [[backlog-versus-commitment]] holds its consequences for a chart and for Cycle Time. An item in the backlog is an option. In Vacanti's board, an item in Ready is a promise: "The placement of a work item in the Ready column means that the item has been both prioritized and committed to" (L2282). A candidate that "has not been pulled in yet" remains free to be reordered or skipped (L2318). This wiki reads that as a test for a board's columns: a column that holds items nobody has promised is not the commitment point, whatever it is called. Vacanti's Ready is also where "started" begins, since its limit bounds how many new items "can be started" (L2256), so this wiki reads a promised range as counted from that entry. See [[arrival-point]] and [[started-and-finished-points]].

## What commitment means

Vacanti's body text gives three aspects (L2276-L2280), while the chapter's takeaways count two (L2362-L2364), dropping the first, which qualifies the word rather than adding content:

1. **Small "c".** "There should be no severe penalty for missing a commitment", yet the team does everything in its power to meet it (L2276). Consequences for individuals are out of scope for this wiki. What is kept is that a miss is a data point, not a broken contract.
2. **Flow through.** Once started, the item is expected to go all the way to completion, which is [[conservation-of-flow]] stated as a promise (L2278).
3. **A range and a probability, communicated.** The customer's first question is when it will be done, and the commitment point is where it is answered (L2280), in this form:

> “we expect this item to flow all the way through the process and exit in 14 days or less with an 85% probability of success”
>
> — [[vacanti-actionable-agile-metrics]], L2282

This wiki reads the 14 days and 85% as an example of the wording, not a target. The form is what the source calls a Service Level Agreement, with setting it deferred to its Chapter 12 ([[service-level-expectation]]). "Everything in its power" starts with choosing a range and probability that are achievable ([[choosing-a-service-level-expectation]]), and with [[conditioning-flow]] (L2316).

## Signs

The source gives the principle; the signs are this wiki's transfer, and each raises a question rather than a verdict:

- A date or promise is attached to an item still in the backlog: commitment happened before capacity was known.
- Items sit in the commitment column with no range ever given.
- More items were promised than the column's bound on [[wip-control]] admits: commitment was not determined by capacity.
- Committed items are regularly dropped: the commitment came earlier than knowledge justified. Check against [[accounting-for-abandoned-work]].

## Flow versus Scrum

Vacanti rejects the claim that Kanban has no commitments and locates the difference in the unit and the basis (L2288):

| | Scrum | Flow-based |
|---|---|---|
| Unit | "made at the sprint level" | "at the individual work item level" |
| Basis | "based more on upfront estimation and planning" | "based more on measurement and observation rather than planning and estimation" |

This wiki notes that Vacanti's Scrum is a team committing to "some number of stories" (L2288). That matches Cohn's position and not the 2020 Scrum Guide, which commits to a goal and only forecasts the selection, so the table's Scrum column should be read with [[commitment-over-a-period]].

**Resolved per setup, the wiki's own reading.** The setup chosen for the project decides which form is meaningful. With iterations, commitment is over the period, in the form [[commitment-over-a-period]] sets out, and rests on estimates and past periods, so per-item dates would claim more than the method does. With pull, commitment is per item and needs a measured [[cycle-time]] history. Vacanti notes the two can mix, suggesting Scrum users adopt flow-based principles (L2288). With too little history for a pull setup, this wiki reads the honest output as the Kanban Guide's best guess, labelled as a guess, and not a range presented as measured ([[service-level-expectation]]).

## Trade-offs

The source names no cost. This wiki reads the cost as giving up early dates: a stakeholder wanting a promise before work is pulled gets none under this rule, or gets a forecast labelled as such. The opposite failure is a commitment made with little notice of what capacity held.

## Agent note

The commitment is made to a customer by whoever steers, not by an executing agent, so the concept survives. Its "all reasonable effort" part (L2282) changes meaning: for an agent it reduces to not starting what cannot be finished and surfacing a block, since an agent does not push harder. The range depends on measured history and is unaffected.
