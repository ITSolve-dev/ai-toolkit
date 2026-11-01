---
title: Iteration Capacity
category: periods
summary: Plan against what is left after standing obligations are taken out, not against nominal hours; Cohn's team of seven plans 4 to 6 hours a person a day, 280 to 420 of 560 hours, his case study assumes six and its people doubt it, and unpredictable support comes out first.
tags: [rule, iterations, capacity, filling, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iteration Capacity

Iteration capacity is the amount of work a project can plan into a period once everything that is not planned work has been taken out. Cohn's point is that it is well below nominal time, for reasons that can be named in advance.

## The rule

Start from what the period holds, take out unchangeable obligations first, and plan into what remains, leaving a margin because estimates are wrong.

## Numbers and their conditions

Cohn's worked example is seven people on two-week iterations: 7 people x 10 days x 8 hours is 560 hours ([[cohn-agile-estimating-planning]] L3307). Cohn says the team cannot plan that much, since time goes to activities not on task cards and "they are, after all, estimates, not guarantees" (L3307, emphasis dropped). His figure is:

> most teams are successful when their planned work (the sum of their task cards) represents between four and six hours per day
>
> — [[cohn-agile-estimating-planning]], L3307

Cohn gives 280 to 420 hours for that team (L3307). This wiki notes that the figure is coaching experience, with no measurement behind it, and that it counts a human working day at the level below this wiki's task. Cohn says where a team lands depends on how well it identifies tasks, how accurate its estimates are, outside commitments and corporate overhead, and "After as few as a couple of iterations most teams begin to get a feel" for the number (L3307). He adds that the sum carries uncertainty but "still gives some indication of the overall size of the work" (L3305).

### Six hours in the case study

The fictional case study in Chapter 23 (L4961) picks one value inside that band and says what fills the rest of the day:

> Based on what I’ve seen after being here a couple of days, I think you should plan on six hours per day per person of productive work. The rest of each day goes to answering emails, talking to other project teams, your own daily meetings, the half day every other week we’ll spend doing this planning, and so on.
>
> — [[cohn-agile-estimating-planning]], L5767

The figure's conditions are these: it is an outsider's judgement after a couple of days and not a measurement, it assumes a two-week iteration, so "With 6 hours a day for 10 days, I’ve got 60 hours available." (L5783), and declared absences come off separately (L5789-L5797).

The people in the case doubt the number. One says "It might be closer to 5 but I can try to get 6 a day on this project" (L5773), and another "I know we’re saying I’ve got 60 but that seems high to me." (L5851). This wiki reads those objections as the useful part: the figure is an assumption to be corrected, and what corrects it is the velocity observed afterwards ([[planned-velocity]]), not a timesheet.

**Sign:** capacity computed from a full working day, or a planned-hours figure reused from another setting with no check on what filled the rest of the day. This sign is this wiki's.

## Unplanned obligations come out first

Cohn's image is an iteration as an empty glass: "The first things poured into the glass are the team’s unchangeable commitments, such as to support and maintenance of other products." (L3329). A team starting 10% full can commit to more than one starting 90% full (L3333).

The discriminating criterion is whether the work can be ranked in advance. General bug fixes that can be prioritized go through normal prioritization, as on [[defect-inside-or-outside-the-iteration]]. Only "those unpredictable but required parts of many team’s lives" go in the glass (L3327).

An average does not make that work predictable: "averaging twenty hours of support per week is not the same as having twenty hours every week" (L3342). A team that overruns in one period should try to exceed its commitment in a lighter one, and Cohn calls this variability "inescapable on teams with significant support and maintenance obligations" (L3342). That is the trade-off: the rule reduces misses and does not remove them.

## Check the bottleneck as well as the total

Cohn also asks whether the sum hides overload on one function, such as stories easy to program but costly to test (L3309-L3315). This wiki keeps the check and drops his staffing remedies as people management. The transfer here is ours: the function to check is whatever one stage everything has to pass through. A worked case with its numbers is on [[filling-a-period]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Nominal capacity | The calendar of the people steering and the agent setup |
| Standing obligations | Project configuration, and history of unplanned items |
| Unplanned load, as an average with its spread | Board history: items that entered mid-period |
| Planned amount that has held | Board history: what was finished in earlier periods |

The choice was wrong if periods keep missing with the misses following unplanned load, which means too little was reserved. It was also wrong if periods keep ending early, which means too much was reserved. Capacity comes from board history and not from logged hours, which this wiki does not rely on.

## Agent executor note

The figures of four to six hours, the case study's six, and the 50 to 75 percent they imply do not transfer, because they describe a person's day: email, meetings, overhead. The mechanism does: nominal capacity is not plannable capacity, and work that cannot be ranked must be reserved before planning. This wiki reads the limiting capacity as what the people steering can review in a period ([[filling-a-period]]), and that reading is unmeasured. Support load that lands on the people steering takes from that same capacity, so it belongs in the glass even when an agent does the planned work.

## Related

How the amount is then filled is on [[velocity-versus-commitment-planning]]. What counts as planned work, including meetings about the project, is on [[all-work-to-finished-is-in-the-plan]]. Why a margin is kept at all is on [[utilization-versus-slack]]. Mid-period arrivals are on [[mid-period-change]] and [[interrupting-started-work]].
