---
title: Ideal Days as a Measure of Size
category: sizing
summary: An ideal day is uninterrupted work under three counterfactual assumptions and counts as size, less strictly than points; it converts to duration only through velocity. Its failures: it decays as the executor improves (5 to 1 ideal days at flat velocity), it is read as a deadline (start plus estimate), and it is pressed toward actual days until it becomes elapsed time. For an agent executing and a few people steering, this wiki chooses relative size.
tags: [concept, estimation, ideal-days, size, velocity, ideal-time, elapsed-time, overhead, decision-rule, story-points, project-setup, failure-mode, dates, pressure]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Ideal Days as a Measure of Size

An **ideal day** is a unit for estimating work: how many uninterrupted days a user story would take to develop, test and accept ([[cohn-agile-estimating-planning]] L1133), under the assumptions listed on *Ideal Time Versus Elapsed Time* (below). A discussion question in the chapter takes one ideal day as "8 hours of uninterrupted, focused work" (L1161). Cohn's claim is that once overhead is left out, the number measures size rather than duration.

## Why it counts as size

When estimating in ideal days "it is not necessary to consider the impact of the overhead of the environment in which the team works" (L1133). Cohn's example is a screen that takes one ideal day whether he works at a startup with no overhead or at a huge bureaucracy. Only the elapsed time differs, and as demands on his time grow, "the amount of elapsed time to complete one ideal day of work will increase" (L1137).

> When considerations of organizational overhead are ignored, ideal days can be thought of as another estimate of size, just as story points are.
>
> — [[cohn-agile-estimating-planning]], L1139

Cohn draws the conversion from that: "an estimate of size expressed as a number of ideal days can be converted into an estimate of duration using velocity in exactly the same way as with story points" (L1139). See [[velocity]], [[story-points]] and [[size-versus-duration]].

The claim is qualified in the chapter summary: "ideal days are an estimate of size, although less strictly so than story points" (L1155). That chapter does not say why. Chapter 8 does: "Story points are a _pure_ measure of size. Ideal days are not." (L1580), because an ideal-day number also moves with how good the executor is. See *Ideal-Day Estimate Decay* (below) and [[who-estimates]].

## Why estimate this way rather than in elapsed days

Cohn's reasoning is about what the estimator must consider: "Estimating in elapsed days requires us to consider all of the interruptions that might occur while working on the story." (L1155). An ideal estimate considers only the time the story itself takes (L1155). This wiki reads the difference as a forecast of the environment: an elapsed estimate has to make one, which makes it harder and ties the number to current conditions.

## Telling a size from a disguised duration

This wiki reads the startup-versus-bureaucracy example as a test: a size estimate should not change when the environment does. The sign of a violation is an estimate raised or lowered because of something outside the task, such as a week of meetings, a holiday or support duty. That sign raises a question and is not a verdict: check whether the task itself changed. If it did not, the number was carrying elapsed time, and the overhead will be counted twice once velocity converts it.

## One number per task

Cohn gives the estimate as a single aggregate figure and not one per role. That rule and its exception are on [[one-estimate-per-task]].

## Trade-offs

This wiki reads the unit's strength as being easy to explain, since it is a day, and that as also its weakness, because the same word invites reading the number as calendar time. That is the failure described at *Ideal Estimate Read as a Deadline* (below), and its pressure form is on *Ideal Days Compared to Actual Days* (below). Which unit to use is on *Story Points or Ideal Days* (below).

## Agent executor note

This wiki reads the separation of size from duration as surviving and the unit's anchor as not surviving. An ideal day is calibrated on a person's focused day, and a day of agent execution is not that quantity. The transfer here is ours: because velocity is measured from fact, the conversion to duration still works if the numbers are used consistently as a relative scale. It stops working once anyone treats them as literal days of a person's work. This wiki would answer the chapter's discussion question about how many elapsed hours make one ideal day (L1161) from how long tasks lived on the board, not from logged hours.

## Ideal Time Versus Elapsed Time

**Ideal time** is how long a piece of work takes with everything around it removed. **Elapsed time** is how long passes on a clock or calendar until it is done. Cohn's illustration is American football: four fifteen-minute quarters make a sixty-minute game that takes around three hours to sit through, and both answers are correct ([[cohn-agile-estimating-planning]] L1080).

> Ideal time is the amount of time that something takes when stripped of all peripheral activities.
>
> — [[cohn-agile-estimating-planning]], L1080

> Elapsed time, on the other hand, is the amount of time that passes on a clock (or perhaps a calendar).
>
> — [[cohn-agile-estimating-planning]], L1080

### Each answers a different question

The officials need ideal time to know when the game is over. Someone asked how long they will be gone needs elapsed time, and answering "sixty minutes" does them no good (L1082). This wiki reads the discriminating question as who is asking and for what: how much work this is calls for ideal time, and when it will be finished calls for elapsed time. Neither value can stand in for the other without a conversion. For software that conversion is [[velocity]], as the definition at the top of this page explains.

### Why ideal time is easier to predict

> It is almost always far easier and accurate to predict the duration of an event in ideal time than in elapsed time.
>
> — [[cohn-agile-estimating-planning]], L1084

Cohn's reasoning is that ideal time depends on few inputs. A quick answer of 60 minutes is available off the cuff, and historical overtime figures refine it (his illustrative result is 62.3 minutes). Elapsed time depends on many inputs. Games ran from 2½ hours to over four, driven by injuries, playing style, penalties, televised timeouts and weather, and matching the off-the-cuff ideal estimate would mean weighing each of them (L1084-L1092). Those figures illustrate the argument and are not measurements of software work.

### What fills the gap in software

On a software project the gap comes from "the natural overhead we experience every day" (L1100). Table 5.1 lists its sources: supporting the current release, training, sick time, email, meetings, reviews and walk-throughs, demonstrations, interviewing, personnel issues, task switching, phone calls, bug fixing in current releases, special projects and management reviews (L1104-L1113).

Cohn cites a figure for interruptions: "managers are able to work an average of only five minutes between interruptions (Hobbs 1987)" (L1117). The measured population is managers. The figure of one interruption every fifteen minutes for a developer is Cohn's supposition of a third of that rate, not a measurement (L1117).

Cohn adds that multitasking widens the gap further: "A software developer who is told to multitask loses a great deal of efficiency while switching between two (or more) tasks." (L1121). This chapter gives no magnitude for that loss. Cohn's study of it is on [[multitasking]].

### The assumptions behind an ideal estimate

An ideal estimate holds under three stated assumptions (L1123-L1129):

- the story being estimated is the only thing you'll work on
- everything you need will be on hand when you start
- there will be no interruptions

These are counterfactual: Cohn asks the estimator to assume them, not to make them true. This wiki notes that the second resembles the plugin's working test for a task, "once started, it can be finished without waiting" ([[unit-of-work]]). The resemblance is not a grounding: that test comes from the plugin's design and has no source, and Cohn's line is an estimating assumption, not a criterion for cutting work.

### Agent executor note

This wiki reads the distinction as surviving, with the contents of the gap changing. The mechanism here is a person's day: most of Table 5.1 (sick time, email, training, interviewing, phone calls) does not apply to an agent, though it still applies to the person steering. The transfer here is ours and unsourced: for agent-executed work the expected remaining gap is waiting on that person, such as a presented result sitting unreviewed, rather than interruption during execution. Time in state read from board history would show whether that holds, and the [[flow-metrics]] count that time; logged hours are not needed and are out of scope.

This wiki does not carry the interruption figures above over to agent-executed work at all.

Related: [[size-versus-duration]].

## Story Points or Ideal Days

The choice of estimating unit decides whether a number states how much work there is or how long someone expects it to take. Cohn treats both as workable: "Each is a viable choice with advantages to recommend it." ([[cohn-agile-estimating-planning]] L1648). His own preference is settled: "My preference is for story points." (L1636).

### The considerations

In favour of [[story-points]] (L1538-L1546):

- They push an estimate to cover the whole of a task instead of a sum of parts; see [[one-estimate-per-task]].
- They do not go stale as the executor improves; see *Ideal-Day Estimate Decay* (below).
- They are a pure measure of size, so they are estimated by analogy and invite no comparison with the calendar; see *Ideal Days Compared to Actual Days* (below).
- Estimating is usually faster. Cohn offers this as experience and gives a mechanism, not a magnitude: "when estimating in ideal days it is easier to think about the individual tasks necessary to develop a story, rather than thinking in terms of the size of the story relative to other stories." (L1596). The design discussion runs deeper as a result.
- They can be compared between people; see [[who-estimates]].

In favour of ideal days (L1612-L1616):

- They are easy to explain outside the team, because of the intuitive reading "This is the amount of time it would take me if it’s all that I worked on." (L1622).
- They are easier at the start. A team on story points has no ready baseline and "has to find its own baseline by estimating a few stories" (L1626). Cohn bounds this cost: "Usually within an hour, many teams estimate in story points as naturally as if they’d been doing it for years." (L1628).
- They make an initial velocity prediction easier. This chapter only states the claim and defers the reasoning to the chapter on estimating velocity (L1632); see [[velocity]].

### How Cohn weighs them

Cohn discounts two of the three points for ideal days. Starting costs are short-lived, and of explaining the unit he writes: "we probably shouldn’t choose based on how hard it will be to explain to outsiders." (L1640). He also turns the intuitive feel against the unit, since it is what invites pressure on the number (L1640). The third point, the early velocity forecast, is not rebutted in his recommendation.

He allows one exception: "I usually only do this with a team that cannot accept that it is beneficial to separate estimates of size and duration." (L1642). The separation is the rule on [[size-versus-duration]].

### The rule, per setting

The resolution below is this wiki's own reading, built on Cohn's positions. He writes for a human team and does not address an agent.

| Input | Read from | Choice |
|---|---|---|
| Who executes | Project setup | An agent executing and a few people steering: relative size. An ideal day is anchored on a person's uninterrupted working day, and this wiki sees no such anchor for an agent. |
| Whether the executor's capability will shift during the project | Project setup: new technology, a domain new to the team, a change of model or tooling | A shift expected: relative size, because the estimates survive it. |
| Whether a duration forecast is required before any history exists | The request; board history showing no completed sized work | Required now: ideal days are the easier route per Cohn, with [[velocity]] as the place to work it out. |
| Whether the people involved can separate size from duration | How estimates are given and discussed in task text | They cannot yet: start in ideal days and shift, as below. |

Audience outside the team is deliberately not an input, following Cohn (L1640).

### What would show the choice wrong

These signs are this wiki's derivation from Cohn's mechanisms. Each raises a question rather than a verdict.

- Ideal days were chosen, and later: [[velocity]] stays flat while completed items multiply, comparable tasks get smaller numbers over time, or the numbers are argued against the calendar.
- Story points were chosen, and later: every point is routinely translated into a fixed number of days. The unit is then duration under another name, and its advantages over ideal days are gone.

### Moving from ideal days to points

Cohn's route is to change the question asked, not to announce a new unit: "How big is this one compared to the one we estimated five minutes ago?" (L1644). The aim is to move talk from how long the pieces take to relative size, and "Most teams hardly notice the gradual switch" (L1658). This wiki keeps that as a statement of what changes, not as a script for a meeting: an estimate phrased relative to an earlier task is a point estimate in practice, whatever it is called.

### Trade-offs

This wiki sums up the two sides. Choosing points costs a short period without a baseline, a unit that is harder to explain, and, per Cohn, a harder initial velocity forecast. Choosing ideal days costs everything listed on the linked failure pages.

## Ideal-Day Estimate Decay

An ideal-day estimate embeds how good the executor currently is, so it ages as that changes. "An estimate expressed in story points has a longer shelf life than an estimate in ideal days." ([[cohn-agile-estimating-planning]] L1564). The causes Cohn names are "the team’s experience with the technology, the domain, and themselves, among other factors" (L1564).

### What breaks

The first damage is to comparability: two pieces of work of exactly the same size carry different estimates (L1564). The second is that the measurement meant to catch this does not catch it. Cohn is direct: "We would like to think that measuring velocity over time would correct or account for this problem. It won’t. Instead, we’ll see a consistent velocity even though more work is being done." (L1566).

### The worked figures and their conditions

The figures belong to a constructed illustration, not a measurement. The setting is one programmer alone on the team, one-week iterations, and an environment where a calendar day equals an ideal day (L1566-L1572).

| | Estimate for one application | Applications finished in the iteration | Velocity |
|---|---|---|---|
| Learning the language | 5 ideal days | 1 | 5 |
| A few months later | 1 ideal day | 5 | 5 |

Five times the work produces the same velocity (L1572). This wiki notes the corollary, which is implied and not stated by Cohn: in story points the same application keeps its size, so velocity would rise and show the gain.

Cohn limits the weight of this: "For some projects, especially those adopting new technologies or on which the team is new to the domain, this can be a consideration." (L1574).

### Observable signs

These signs are this wiki's derivation, since Cohn gives the mechanism and no board sign. Each raises a question to check.

- In board history, comparable tasks carry falling ideal-day estimates over time.
- Velocity in ideal days is flat while the count of completed tasks of similar scope rises.
- A backlog holds estimates of different ages for like work. This wiki adds that such a backlog does not add up: old numbers overstate what remains if the executor has improved since.

### Discriminating criterion: did the work change, or the executor?

Re-estimate both units if the size of the effort changed, for example "based on the development of a framework" (L1576). Only ideal days need changing "when the team" gets better at something (L1576). This wiki's test before touching an estimate is whether the same work remains to be done. If it does, a story point stays put.

### With an agent executing

Cohn's mechanism is human learning. This wiki reads it as surviving in a changed form: an agent's capability does not grow gradually, but moves in steps when a model, the tooling or the context available to it changes. A day-denominated estimate is then stale across the whole backlog at once. A caveat that the source does not cover: if such a step helps some kinds of task more than others, relative sizes may shift too, and the claim that size is unaffected would need checking.

The remedy is the unit choice on *Story Points or Ideal Days* (above); the unit that avoids this is [[story-points]]. See also the definition at the top of this page and [[velocity]].

## Ideal Estimate Read as a Deadline

An estimate given as uninterrupted work is received as calendar time, and a date is set from it directly. Cohn's scene: a manager asks "How long will this take?", a team member says "five days", and "the manager counts off five days on her calendar and marks the day with a big red X" ([[cohn-agile-estimating-planning]] L1119). The team member meant something else:

> Five days if that’s all I do; but I do a lot of other things so probably two weeks.
>
> — [[cohn-agile-estimating-planning]], L1119

This wiki reads the two-week figure as an illustration of the shape of the problem, not a measured ratio.

### Why it happens

This wiki reads the two people as using different quantities under the same word; see *Ideal Time Versus Elapsed Time* (above). Neither states which. It reads the ideal-day unit as making the confusion easier, because its name is a calendar word.

### The sign

- A due date equals a start date plus the estimate, with no conversion in between. [[estimate-versus-commitment]] reads the same sign for a different failure: a date nobody decided to hold to.
- An estimate appears as a bare number of days, with no statement of whether it means ideal or elapsed.
- Board history shows tasks finishing late by a consistent factor. This wiki reads a steady ratio as pointing at an unconverted estimate rather than at poor estimating, and a scattered one as pointing elsewhere. That reading is ours, and the sign is a question to check.

### What to do

This wiki derives two steps from the chapter. State the quantity whenever a number is given, so a size is never mistaken for a duration. Produce a date only through [[velocity]], which is the conversion Cohn names for ideal days (L1139), by the method on [[velocity-range-forecast]].

### Agent executor note

This wiki reads the failure as surviving, and possibly as worse. The mechanism is two readers of one number, and a person planning around an agent's output is still a reader. The transfer here is ours: a task that executes quickly but then waits for review looks like it should finish on the day it starts, so a date set from execution time alone leaves out the wait.

Related: [[forecast-range-and-probability]], where the problem is what a date is taken to mean and not which quantity it holds; *Ideal Days Compared to Actual Days* (below), where the comparison with the calendar becomes pressure on the unit itself.

## Ideal Days Compared to Actual Days

An ideal day has the name and intuitive feel of a calendar day, and that likeness is the defect. The ease of understanding that favours the unit also "causes problems" ([[cohn-agile-estimating-planning]] L1640). The failure runs in two stages. A neighbouring failure, *Ideal Estimate Read as a Deadline* (above), is one date set from one number; this one is a running comparison of the unit with the calendar.

### Stage one: the comparison

"Teams that estimate in ideal days almost inevitably have their ideal days compared to actual days. They then find themselves justifying why they “only” completed eight ideal days of work in a ten-day iteration." (L1584). The eight-in-ten figure is an illustration of the conversation, not a benchmark.

### Stage two: the unit is redefined

Cohn separates legitimate pressure from the harmful kind: "Pressure for more focus and concentration on our work is fine." (L1640). The harm comes from pressure for each actual day to approach an ideal day, which has "the effect of causing us to estimate in actual time while calling it an ideal day." (L1640). An ideal day then becomes "a day where I make six hours of progress and do other things for two hours." (L1640).

This wiki reads the end state as the worst of both units: the label promises an effort measure, the value is elapsed time, and estimates from before and after the drift are not comparable.

### Observable signs

These signs are this wiki's derivation from Cohn's mechanism. Each raises a question to check.

- Commentary on a board or in a report sets ideal days done against days elapsed, particularly with a word like "only".
- The ratio of ideal to calendar days is treated as a target to raise.
- A definition of an ideal day that includes overhead or a fixed allowance for other activity.
- A step in estimates per task with no change in the work, around the time such a discussion began.

### Trade-off and how it is avoided

The protection comes from the unit: [[story-points]] are abstract, so "there can be no temptation to compare them to reality" (L1584). The price is losing the easy explanation to people outside the team, which Cohn accepts (L1640). See *Story Points or Ideal Days* (above).

### With an agent executing

The mechanism depends on organizational pressure on people, and an agent feels none. This wiki reads the risk as moving, not vanishing: a person steering reports the numbers, and day-shaped numbers still invite comparison with the calendar. No source here tests this for an agent.
