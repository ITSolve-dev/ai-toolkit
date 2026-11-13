---
title: Estimating Velocity
category: sizing
summary: Velocity before a usable history is estimated in a ranked order (observe one to three iterations, then a related project's actuals if seven comparability questions pass, then a see-what-fits forecast, with planned velocity as a labelled stop-gap) and always stated as a range whose width follows the evidence (0.6-1.6 on one observation or doubtful history, 0.8-1.25 at two, the observed range at three iterations); from four closed iterations, the step at which Cohn's own table stops at 0.90-1.10, this wiki uses the three-value forecast instead, and observed values replace any estimate as soon as they exist.
tags: [decision-rule, velocity, release-planning, iterations, method, forecast, release, cohn, history, capacity, numbers, human-executor, rule, range, false-precision]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Estimating Velocity

Three sources can supply a [[velocity]] estimate, and they are ranked, not interchangeable. Cohn notes that "Circumstances often guide you and constrain your options" ([[cohn-agile-estimating-planning]] L3785) and gives the order of desirability (L3787-L3791):

1. Run one or more iterations before giving the number, if at all possible. "There’s no estimate like an actual and seeing the team’s actual velocity is always your best choice" (L3787).
2. Use the actual velocity from a related project by this team.
3. Estimate by seeing what fits.

The chapter presents historical values first (L3590-L3596), but that is section order; the ranking above is what governs.

## Inputs and where they come from

| Input | Read from | Effect |
|---|---|---|
| Can an iteration finish before the number is due? | The date the estimate is demanded, against iteration length and project start | Yes: *Run Iterations to Observe Velocity* (below) |
| Does this team have actuals from related work? | Board history of the earlier project | Yes: test it with *When Historical Velocity Can Be Reused* (below) |
| Does the project exist yet? | Whether it is funded, contracted and staffed | No: *Forecast Velocity by Seeing What Fits* (below) |

The forecast path is for cases where running iterations is impossible or pointless: a project starting in twelve months, one that starts only if a client signs (L3684), or a team that does not exist yet (L3779). Cohn says "Forecasting velocity is rarely your first option" (L3686). When a project has started and a schedule is wanted before its first iteration ends, the fallback is *Planned Velocity* (below).

## What later fact shows the choice wrong

The first observed iterations land outside the stated range (*A Velocity Estimate Is a Range*, below). This wiki reads that as pointing to one of three things: history that was not comparable, a forecast sample that was not representative, or a range that was too narrow.

## Replace it with actuals

The choice is temporary whichever way it goes: "Regardless of which approach you use, switch to using actual, observed values for velocity as soon as possible" (L3793). Cohn's example is a see-what-fits estimate given six months ahead for a rough answer, replaced by measured velocity once the project starts (L3793-L3797). How often a plan is then recomputed is on [[replanning-on-new-knowledge]].

## Sign of violation

Board history shows completed iterations, while the plan's dates are still computed from the pre-project forecast or from a previous project's mean. This sign is this wiki's, and it raises a question: check whether the plan was recomputed and simply kept the same figure.

## Agent executor note

The transfer here is ours. The ranking rests on observation beating prediction, which does not depend on who executes, so it survives. An iteration may also be cheaper to run than it was for the teams Cohn describes, which would push the first option further forward, but this source says nothing on that and the plugin should not assume it.

## Run Iterations to Observe Velocity

Instead of predicting [[velocity]], run one to three iterations and estimate from what was observed. Cohn says "Because the best way to predict velocity is to actually observe velocity, this should always be your default approach" ([[cohn-agile-estimating-planning]] L3647). In the ranking at the top of this page this option ranks first.

### Procedure

1. Hold off giving a velocity figure for at least one iteration; Cohn holds that most project managers can do this (L3655).
2. Run the iteration on the real project.
3. Turn the observation into a range (*A Velocity Estimate Is a Range*, below):
   - After one iteration: multiply by 0.6 and 1.6. A velocity of 15 gives 9-24 (L3655).
   - After two: the mean times 0.8 and 1.25, the [[cone-of-uncertainty]] step for two in Table 16.1 (L3666). The prose beside the table says 80% to 120% (L3659); this wiki uses the table, as [[cone-of-uncertainty]] explains.
   - After three: use the range of observed values, or the mean with the cone step for that count. 12, 15, 16 gives 12-16 (L3657).
   - From four closed iterations this wiki hands over to the three-value forecast on [[velocity-range-forecast]]; see the table by count of closed iterations, below.
4. Plan the release date from the range (L3653).

### Reasoning

The time is spent anyway. Cohn's argument is that traditional projects use their early weeks on "obvious" requirements and on assembling a plan, "often as long as a few iterations on an agile project" (L3647). The early iterations are not only a measurement. Their stated purpose is "to assess the dark corners of the system, better understand the technologies involved, refine the understanding of the requirements, and measure how quickly the team can make progress on this project" (L3680).

The evidence offered is one anecdote: a development director whose yearlong projects set deadlines about two months in, with plans "always off at least 50% and often more" (L3653). This wiki keeps the mechanism and not the 50%: one company's experience, stated by one person.

### Trade-off

The cost is having no number at the start. Cohn expects resistance from organizations unwilling to start without any idea of duration, and advises stressing that the delay stems "not from a desire to avoid making an estimate but to avoid making an estimate without adequate foundation" (L3680). When a number cannot wait, or the iteration cannot be funded, this method is unavailable and *Forecast Velocity by Seeing What Fits* (below) applies.

### Failure mode

**Measuring an unrepresentative start.** This failure mode is this wiki's inference and not in the source. The sign is that the first iterations are filled with one kind of work, such as setup or infrastructure, so their velocity describes that work rather than the backlog. Check what the first iterations contained before extrapolating.

### What later fact shows it wrong

Later iterations land outside the range built from the early ones. The source expects velocity to keep moving and warns against treating it as settled even after six iterations (L3674).

### Agent executor note

The transfer here is ours. The method does not depend on human pace, so it survives. The first iteration of an agent-run project may overstate later velocity if it contains only the tasks easiest to specify, which is a reason to check the mix and not to skip the measurement.

## Planned Velocity

Planned velocity is a stand-in for [[velocity]] before any has been observed: the sum of the points on the stories committed to the first iteration. It exists because someone needs a schedule before any data does. The method comes from the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

Velocity itself is defined there by finished work:

> After each iteration we can add up the story points for the stories that are finished. We call that velocity. Velocity will change from iteration to iteration, but its average is relatively stable over time.
>
> — [[cohn-agile-estimating-planning]], L6153

### The choice, in order of preference

1. **Wait three iterations.** "After three iterations we should have a good measure of how fast the team is progressing. We can divide the total amount of work remaining by the velocity and that will tell us how long to expect" (L6157).
2. **Wait for one.** "wait _at least_ two weeks, let the team run one iteration, and then base this initial plan off at least one observation of actual velocity" (L6187).
3. **Plan now, and label it.** "You’ve planned to do four stories in this first iteration. We can add up the points associated with each and call that our planned velocity. We have no idea if it will be, but it’s our initial guess." (L6167).

This wiki reads the first two as *Run Iterations to Observe Velocity* (above), and the third as the forecast on *Forecast Velocity by Seeing What Fits* (below) run on the project's real first selection and not on a sample. The order agrees with the ranking at the top of this page.

### Procedure

1. Commit to a first iteration, by [[filling-a-period]].
2. Sum the points of the committed stories. In the case: 8 + 5 + 2 + 3 = 18 (L6169).
3. Divide the points wanted in the release by that sum. In the case 132 points divided by 18 gives just over 7 iterations (L6173). The 132 comes from the walk on [[kano-model]].
4. Publish the result as a range and name its velocity as planned, on [[forecast-range-and-probability]].
5. Replace it with an observed figure as soon as one exists. The message for those waiting on the schedule is "we can provide better information every two weeks" (L6191).

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Points committed to the first period | Story estimates on the board |
| Total points wanted | The release list |

The first observed velocity is what tests the guess. In the case it came in at 16 against a planned 18 (L6263), and the forecast was recomputed from the observed figure (L6267).

### Failure mode: a guess treated as a measurement

**Signs:** a published schedule with no finished iteration behind it and no note that its velocity is planned, or a planned velocity still being quoted after observed values exist. These signs are this wiki's. The second is the same defect as the sign under *Sign of violation* at the top of this page.

### Points do not convert evenly to hours

This wiki's calculation from the case's own tables gives three different ratios. The rings story is 8 points for 84 hours, about 10.5 hours a point. The bridges story is 5 points for 82 hours, about 16.4. Human versus human together with the winning-shape story is 5 points for 30 hours, about 6. So bridges was rated smaller than rings and came out about the same size in hours (L5752-L5763, L5838-L5845, L5865-L5880).

This wiki reads that spread as the reason planning hours check a commitment on [[filling-a-period]] and do not calibrate points. The general claim is on [[story-points-do-not-convert-to-hours]].

The count also has an edge. The team committed to three stories (L5933), yet the sum names four, because the winning-shape story had been absorbed into another. That is on [[independent-tasks]].

### Which setup this applies under

The resolution is this wiki's. It needs iterations and an estimate on every task. Under a flow setup there is no first selection to sum, and a forecast comes from history once there is any ([[flow-metrics]], [[service-level-expectation]]).

### Agent executor note

The method transfers, since it needs only points and finished stories. The claim that the average is stable concerns a human team and is untested for an agent, and "three iterations" is a remark in a case study and not a measured threshold. Those readings are this wiki's. A first selection of an agent-run project may also hold the tasks easiest to specify, as *Run Iterations to Observe Velocity* (above) warns.

## When Historical Velocity Can Be Reused

A team's past [[velocity]] predicts the next project only to the degree the two situations match. Cohn says historical values are "of the greatest value when very little has changed between the old project and team and the new project and team", and "Any personnel or significant technology changes will reduce the usefulness of historical measures of velocity" ([[cohn-agile-estimating-planning]] L3608).

### The test

Ask of the old and new situation whether each is the same (L3610-L3622):

- Technology
- Domain
- Team
- Product owner
- Tools
- Working environment
- The people who made the estimates

### Decision

| Answers | Action | Source |
|---|---|---|
| All yes, typically a new release of the product the team just worked on | Use the history, still as a range: mean plus or minus a few points, or best and worst iterations over two or three months | L3624 |
| Any no | "think twice", or keep the history and widen it: prior-release mean times 0.6 and 1.6 | L3626-L3634 |

Worked example: 150 points over ten iterations is a mean of 15, which becomes 9-24 (L3626-L3634). The multipliers and their limits are on [[cone-of-uncertainty]].

The source does not say how many nos should rule the history out altogether. This wiki reads that as a judgement left to the planner, where the choice between the two responses to a no is not settled by the count.

### Why the last question matters

This wiki reads the seventh question as carrying a mechanism the others do not: velocity counts points, and points are relative to whoever assigned them. A mean taken in one team's [[story-points]] says nothing about another estimator's scale, even where the executors are unchanged.

### Where the inputs come from

Team, tools and technology are read from the project's own records. The history itself is read from the earlier project's board. If the earlier board has no finished iterations to average, there is no history, and the ranking at the top of this page falls through to the next option.

### What later fact shows the choice wrong

The first observed iterations fall outside the range built from history. That is the signal to drop the history and use actuals, as the ranking at the top of this page requires in any case.

### Agent executor note

The transfer here is ours, and it is a reading, not a finding. The questions map onto an agent-run project as: the same repository and stack, the same domain, the same people writing and accepting tasks, the same agent setup, and the same estimators. A change of model or agent tooling would count as a no under "tools" or "team". Cohn's source cannot say how much such a change moves velocity, so the plugin should treat it as a reason to widen the range, not as a known correction.

## Forecast Velocity by Seeing What Fits

This method derives [[velocity]] with no history and no iteration, by simulating one: expand stories into estimated tasks until an iteration's capacity is full, then count the points that fit. Cohn calls it "very similar to iteration planning" ([[cohn-agile-estimating-planning]] L3801). It is the last resort in the ranking at the top of this page: "Forecasting velocity is rarely your first option" (L3686). It applies when the project is too far off or too uncertain to spend on, such as one that starts in twelve months or only once a contract is signed (L3684), and in strategic planning and budgeting ahead of a project (L3781).

### Procedure

The steps are at L3688-L3694.

1. Estimate the hours each person can give the project per day.
2. Multiply out the hours for the iteration. Four people at six hours for ten days is 240 (L3718).
3. Pick stories, expand them into tasks and estimate those, until capacity is reached.
4. Sum the points or ideal days of what fit, and convert that to a range (*A Velocity Estimate Is a Range*, below).

The SwimStats example fits nine stories, 25 points and 221 hours, against 240 hours available, and the 25 becomes 15-40 (L3728, L3732-L3736, L3740-L3751). The stopping point is a judgement: the team "could commit to this but probably no more" (L3728). Capacity is not filled to the hour. This wiki reads that as the forecasting form of adding stories until no more can be committed ([[filling-a-period]]).

These are planning hours, estimated ahead. They are not logged hours, which this wiki excludes.

### Rules inside the procedure

**The sample must be representative.** Priority order is not needed: "What you really want is a fairly random assortment of stories" (L3724). Do not expand only the one- and two-point stories, and do not expand only user-interface or database stories (L3724). Sign: the expanded set is all one size or one layer of the system.

**Capacity is capped by the scarcest skill, not by the total.** Hours do not pool across people who cannot do each other's work: "Select stories until one skill set on the team can’t handle any more work" (L3726). Sign: the total fits, but the tasks needing one specialist exceed that person's hours. The same check appears on [[iteration-capacity]].

**No adjustment for holidays or sickness.** "Don’t bother; it’s not worth the extra effort and it’s unlikely to be more accurate anyway" (L3720). The availability figure already allows for them.

**Part-time members need a per-person table.** With a uniform figure the SwimStats team gets 240 hours; listing Sergey at 4, Yury at 6, Carina at 2 and Sasha at 6 gives 180 (L3757-L3773). Carina is the mechanism to note: split across two projects, she could give nearly six hours in total, yet is shown at two on this project, because she moves between them many times a day and "this multitasking impacts her productivity" (L3759-L3763). See [[wip-per-executor]].

### Numbers and their conditions

| Figure | Setting | Standing |
|---|---|---|
| 4-6 hours per day | Individuals assigned full-time to one project | Cohn's opinion, "From observation and discussion with colleagues" (L3704) |
| 55% of time on project activities | An empirical measurement | Citation unresolved in this copy, printed as "(TBD: REFBOEHM)" (L3704) |
| 80% | Toyota engineers, under a lean process | Kennedy 2003, cited as the high end (L3704) |

A large bureaucracy sits at the low end and a three-person startup at the high end (L3706).

Story points and task hours do not move in lockstep. In Table 16.2 a 1-point story has 14 hours while a 2-point story has 12 (L3745, L3748), so this wiki warns against converting a points total into hours from an average ratio ([[story-points-do-not-convert-to-hours]]).

### What later fact shows it wrong

Actual velocity from the first real iterations falls outside the range, at which point the actuals replace it (L3793).

### Agent executor note

The transfer here is ours. The hours arithmetic, the 4-6 hour figure and the Carina case all rest on a human's divided day, and they do not survive an agent executing: an agent has no meetings or e-mail eating its day. Two parts of the method do survive. Sampling representatively still prevents a biased estimate, and the scarcest-skill cap still applies with a different resource, which this wiki expects to be the steering person's attention for review and acceptance. That last point is a hypothesis with no support in this source. It should not be used as a number.

This wiki reads the method, for a few people steering agents, as mostly a fallback for budgeting before any iteration is possible, since an iteration there is likely cheap enough to run instead; see *Run Iterations to Observe Velocity* (above).

## A Velocity Estimate Is a Range

An estimate of [[velocity]] is given as a range whose width reflects how much is actually known, not as a single figure. Cohn holds this across every way of arriving at the number: "regardless of which approach you are using, if you need to estimate velocity you should consider expressing the estimate as a range" ([[cohn-agile-estimating-planning]] L3598). The chapter's summary repeats it as the closing rule (L3803). This is [[forecast-range-and-probability]] applied to the rate and not to a date.

### Reasoning

A point estimate is almost certain to miss: of a figure of 20, Cohn writes, "You have a very limited chance of being correct" (L3598). The chapter's epigraph names the trade being made: "It is better to be roughly right than precisely wrong" (L3588). This wiki reads what breaks as follows: a release date divided out of one velocity figure looks exact ([[velocity-range-forecast]]), and the error only appears when the date is missed.

### How wide

The width follows the evidence.

| What the estimate rests on | How the range is made | Source |
|---|---|---|
| History from the same team on a stable product | Mean plus and minus a few points, or the best and worst iterations over the past two or three months; Chapter 21 uses three values from the last eight, on [[velocity-range-forecast]] | L3624, L4658-L4664 |
| History with any comparability doubt | Mean times 0.6 and 1.6; 15 becomes 9-24 | L3626-L3634 |
| One observed iteration | Same multipliers; 15 becomes 9-24 | L3655 |
| Three or more observed iterations | The range of observed values (12, 15, 16 gives 12-16), or the [[cone-of-uncertainty]] step for that count | L3657-L3659 |
| Forecast with no observation | Any technique; Cohn prefers 0.6 and 1.6, so 25 becomes 15-40 | L3732-L3736 |

The multipliers and their limits are on [[cone-of-uncertainty]]. Which row applies is decided by the ranking at the top of this page.

### Which range by count of closed iterations

Chapter 16 and Chapter 21 give two methods for a project's own observed velocity, and on the same 12, 15, 16 they give different floors: 12 from the observed range (L3657), and 14.3 from the mean of the slowest three (L4660-L4664), which with three iterations is simply the mean. The resolution below is this wiki's, and [[velocity-range-forecast]] applies the same boundary.

| Closed iterations on this project | The range | The floor that may be promised |
|---|---|---|
| None | A related project's history or a forecast, times 0.6 and 1.6 (L3626-L3634, L3732-L3736) | The low end |
| One | Observed velocity times 0.6 and 1.6 (L3655) | The low end |
| Two | The mean times 0.8 and 1.25 (Table 16.1, L3666; the prose at L3659 says 80% to 120%, and [[cone-of-uncertainty]] gives why this wiki uses the table) | The low end |
| Three | The observed range, lowest to highest (L3657), or the cone step for three | The slowest iteration. The slowest-three mean equals the mean here, so it is no floor |
| Four or more | The three values on [[velocity-range-forecast]]: most recent, mean of up to the last eight, mean of the slowest three (L4658-L4666). Table 16.1's own row would give the mean times 0.90 and 1.10 (L3668) | The slowest-three mean, Cohn's "comfortable" figure (L4684), with the slowest single iteration stated as possible below it |

The boundary at four is Cohn's, not this wiki's. Table 16.1 already treats four or more iterations as one step, the mean times 0.90 and 1.10 (L3668), and Cohn says "I normally don’t extend this analysis past three or four iterations" (L3674). This wiki's choice is which method to use from that point: the Chapter 21 three values and not the table's last row. On Table 21.1's figures (mean of the last eight 17, slowest three 14, most recent 19; L4672-L4678) the table row gives 15.3-18.7 and the three values give 14-19. The reasons for the choice are this wiki's. The three values state a floor drawn from the project's own slowest iterations, which Cohn calls the figure the product owner "should feel comfortable" with (L4684), while the 0.90-1.10 row is a fixed width that Cohn himself declines to narrow further, since he will not "pretend that after six iterations the team precisely knows their velocity" (L3674). Four is also the first count at which the slowest-three mean differs from the overall mean, so the three values say something the mean does not. In this wiki's tests, what would show the choice wrong is delivery below the stated floor in more than an occasional period, the test on [[velocity-range-forecast]], or a run of periods in which the three-value floor sits below the table's low end without delivery ever reaching down to it.

### Sign of a violation

This sign is this wiki's. A plan, release date or commitment quotes one velocity figure, or a date with no spread around it. This raises a question rather than a verdict: check whether a range exists somewhere and was dropped on the way to the plan, and whether the single figure is a stated midpoint or the whole estimate.

### What later fact shows it wrong

Observed velocity keeps falling outside the stated range. The source gives no confidence level for its ranges: the actual figure will "probably" fall inside (L3672). This wiki reads a single miss as proving little, and repeated misses as meaning the width or the midpoint was wrong.

### Trade-off

A defensible range is uncomfortably wide. Cohn concedes that "This range may feel large, but given the likely uncertainty at this point it is probably appropriate" (L3643). The cost is a date expressed as a spread, which someone asking for one date will resist.

### Agent executor note

The transfer here is ours. The rule's mechanism is forecast uncertainty, not human pace, so the rule survives an agent executing and a person steering. The specific widths do not automatically transfer: they come from human project experience, and nothing in this source tests them on agent-executed work.

The chapter assumes iterations. A project set up without them has no iteration count to apply; see [[flow-metrics]] for what is measured instead.
