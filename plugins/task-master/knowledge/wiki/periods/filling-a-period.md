---
title: Filling a Period
category: periods
summary: How much to select for an iteration: the Scrum Guide names past performance, upcoming capacity and the Definition of Done; Cohn fills one story at a time until the team will not commit, checks the tightest stage, keeps velocity as a release gauge because 3 to 12 stories are too few for errors to average out, and leaves slack; Vacanti and Seele read a count off a Throughput simulation, whose percentile is itself the margin. One table by setup says what stops the selection. Selection applies only under an iteration setup.
tags: [rule, iterations, forecast, capacity, scrum, cohn, throughput, decision-rule, velocity, filling, human-mechanism]
sources: [scrum-guide-2020, montgomery-tracker-smells, cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Filling a Period

Filling a period means choosing how much work to select for it. This rule chooses a quantity, and the Scrum Guide gives it inputs and no formula:

> Selecting how much can be completed within a Sprint may be challenging. However, the more the Developers know about their past performance, their upcoming capacity, and their Definition of Done, the more confident they will be in their Sprint forecasts.
>
> — [[scrum-guide-2020]], L222

The Guide calls the result a forecast, and this wiki holds it to that: it is not a promise ([[commitment-over-a-period]]). This wiki also reads the three inputs as a rule: selection is judged against history and against what has to be true for an item to count, and not against how much someone would like to get done.

## The rule

Select from what is ready, up to what history says can be finished to the project's standard of done in a period of this length, adjusted for known changes in capacity.

An item is ready for selection on a size test: "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event." (L278). See [[size-ceiling]]. This is a narrower meaning of "ready" than this wiki uses for task content, because it says nothing about what the task text carries ([[recoverable-versus-task-only-facts]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Past performance | Board history: what was finished in earlier periods, counted only if it met the standard of done |
| Upcoming capacity | The calendar of the people steering and any known change in the agent setup |
| The standard of done | The project's stated definition; a stricter one means less fits |

The selection was too large if tasks repeatedly go back unfinished at the period's end ([[unfinished-at-period-end]]), or if the goal is reached only by relaxing the standard of done. It was too small if the selection is finished well before the period ends, period after period. That test applies where judgement or velocity stops the selection. Where a count from Throughput stops it, a count at 85% finishes early in most periods by design (12 at 85% against a median of 18 in the book's example, [[flow-metrics-scrum-teams]] L924, L938), and the test is the one under the table below: too low if periods regularly pass even the forecast's 50% line.

A related board sign is weak. The study behind [[montgomery-tracker-smells]] lists "Too many difficult or complex issues have been added to a sprint." (L209) as a smell, and 4 of 14 disagreed or said it depends (L552). The reasons given were that "you can just delay issues to the next sprint without repercussions", and that the count alone says little if the work is well distributed between people (L552). The first reason describes the carry-over that [[unfinished-at-period-end]] rejects, so this wiki does not accept it as a defence. The second concerns people and falls away with an agent. Since the study gives no number for "too many", this page relies on the history test above and does not count complex tasks.

## Why

Empiricism is the Guide's stated reason: "Only what has already happened may be used for forward-looking decision making." (L202). What breaks if it is ignored is the forecast's meaning, because a selection chosen by hope tells the people steering nothing about what will happen.

## Leave slack

Cohn adds a limit on the selection, as one of his guidelines:

> Especially when planning an iteration, do not plan on using 100% of every team member’s time. Just as a highway experiences gridlock when filled to 100% capacity, so will a development team slow down when every person’s time is planned to be used.
>
> — [[cohn-agile-estimating-planning]], L4941

The highway is an analogy and not a finding, and no figure comes with it. The rule, its signs and its cost are on *Utilization Versus Slack* (below). This wiki reads the mechanism as the one on [[starting-more-work]]: with no spare capacity, any delay queues everything behind it. The margin comes from the project's own history, since no source here gives one. Under a count from Throughput this wiki reads the chosen percentile as already being the margin, so no further slack is taken off it.

The case study below gives one more reason for stopping short: "you’re better off adding something mid-way through the iteration than dropping something." (L5931). The source states no mechanism. This wiki reads the implied cost as a commitment broken in the open against capacity left idle for a while; see [[mid-period-change]].

## Cohn's case: the tightest stage

Chapter 23 of [[cohn-agile-estimating-planning]] runs the commitment-driven form from *Velocity Versus Commitment Planning* (below) on a fictional project, and its figures are illustrations (L4961). Line references in this section are to that source. One story at a time is taken in priority order ([[ordering-by-value-and-urgency]]) and split into estimated pieces, including the test work; the hours are summed per skill against that skill's capacity until the tightest skill says it is close to full, and the aggregate is checked last, as a sanity check only. The chapter's "tasks" sit one level below this wiki's ([[unit-of-work]]), and its per-person hours and absences are individual load, outside this wiki's scope, so only the check is kept here.

The aggregate looks comfortable, and the case explicitly distrusts it:

> It’s 224 hours in total now. With five of us on the project— Allan, Prasad, Rose, Delaney, and me—this works out closer to five hours a day. But that’s if all the work and each of us is interchangeable. We’re not.
>
> — [[cohn-agile-estimating-planning]], L5929

In the case, testing stood at 88 hours against its 60 under that comfortable total, and it held only because two others offered to help (L5909-L5913).

**Failure mode, overflow at one stage.** Sign: the total fits while one stage's sum exceeds its capacity. The same check is on [[iteration-capacity]].

## Filling by count, from Throughput

[[flow-metrics-scrum-teams]] answers this page's question with a number. Forecast how many items finish in the period from daily Throughput, choose a probability, and read the count ([[throughput-monte-carlo]]). Its example is "8 or more items with 85% chance of success", which means pulling 8 (L1020). Line references in this section and the next are to that source.

> To be clear, however, the MCS does not tell you which items you should pull in, only that you have capacity for up to 8.
>
> — [[flow-metrics-scrum-teams]], L1020

This wiki reads that as leaving the order to decide which items go in ([[reprioritize-before-each-iteration]]). Two conditions come with the count. It holds only for items that pass the size check, since the results say how many right-sized items can be done (L1022, [[right-sizing]]). And the goal stays above it: "The Goal always supersedes whatever scope you’ve pulled" (L838). This wiki reads that as agreeing with [[commitment-over-a-period]].

This wiki reads the method as a concrete form of the Guide's inputs and not a replacement for them. History is the sample, and only what reached the standard of done counts in it. Upcoming capacity has no term of its own and enters through which days are sampled (L872), so a known change the sample does not reflect is still a reason to adjust by hand.

## Which way of filling holds under which setup

This section is this wiki's reading, on sourced positions. The Guide names inputs and no stopping rule, Cohn stops at what the team will commit to, and Vacanti and Seele stop at a count. They differ in what stops the selection, and the setup decides it.

| Setup | What stops the selection | Reason |
|---|---|---|
| Iterations, stable Throughput history, and a size check available | The count at the chosen probability | It reads history and needs no estimate. Size variation remains, and the size check carries it |
| The same, with estimates kept | The count, with summed points as a cross-check | A disagreement between them is a question to raise, and a comparison over a release feeds [[dropping-estimates-for-flow-forecasts]] |
| Iterations, twenty or more tasks a period, stable velocity on one scale, and no Throughput forecast in use | Summed estimates up to recent velocity | Cohn's own condition for estimate errors to average out is met (L3346-L3348) |
| Iterations, the usual small selection of 3 to 12 tasks, with thin or unstable history or a process that has just changed | One task at a time in priority order, until the people steering will not commit, with velocity as a cross-check | There is no sample to trust ([[how-much-flow-data]], [[throughput-monte-carlo]]), and too few tasks for estimate errors to average out (L3346-L3354) |
| Iterations, no history yet | One task at a time | There is no velocity and no Throughput to read |
| A selection much heavier than usual on one stage, under any of the above | The tightest stage, as in Cohn's case | The count reflects the mix in its history, so it cannot see this selection's overflow |
| Flow setup | Nothing, and this page does not apply | Nothing is selected for a period, since the Kanban Guide replenishes on a capacity signal ([[what-may-move]]). The same forecast can still answer how many by a date |

Where a period holds twenty or more tasks and both a Throughput forecast and a stable velocity exist, the first two rows govern; filling to velocity would give about the same answer there, and a gap between the two is the question in the second row. This table merges the two that this base used to keep, one here and one on velocity against commitment planning, and the merge is this wiki's resolution.

The count was too high if periods reach it less often than the stated probability says. At 85% about one period in seven falls short by design, so a longer run of misses is the signal. It was too low if periods regularly pass even the forecast's 50% line.

Cohn's worry about small selections does not disappear, in this wiki's reading. At 3 to 12 items (*Velocity Versus Commitment Planning* (below)) item sizes still differ and a count treats items as alike, so the size check carries that risk, and one item is a large step in the count.

## Agent executor note

The Guide's inputs survive as inputs. Their contents shift.

- **Past performance** only counts if it comes from the same setup. A changed model or a changed way of reviewing makes older periods a poor guide.
- **Capacity** in the Guide means the Developers' time. With an agent executing, this wiki reads the limiting capacity as what the people steering can review in a period, not what an agent can run. That reading is unmeasured.
- **Sizing** is the Developers' job: "The Developers who will be doing the work are responsible for the sizing." (L280). This assumes the estimator also executes. No source in this wiki says whether an agent's own estimate can fill that place ([[size-ceiling]]), so the rule's source and its setting do not match here.
- **Hours per person and per skill** in Cohn's case do not transfer, and the plugin does not produce the level they count. The structure does: find the stage everything has to pass through, which for a few people steering an agent is likely the review of presented results, and fill against that and not against a total.
- **A count from Throughput** reads finished items, and an item finishes when the people steering accept it ([[started-and-finished-points]]). So the count already measures the constraint this page expects, which is this wiki's reason to prefer it where the history exists. That reading is unmeasured.
- **Slack** in Cohn's words protects "every team member’s time" (L4941), and an agent has no time of that kind to protect. This wiki applies the rule to the capacity that limits the project, as above. That reading is unmeasured.

## Velocity Versus Commitment Planning

Cohn describes two ways to decide how much goes into an iteration. They share their first steps, adjusting priorities and identifying a goal, and differ in what stops the selection. He notes they "can be combined to varying degrees" ([[cohn-agile-estimating-planning]] L3091) and "will often result in the creation of the same iteration plan" (L3383).

### Velocity-driven

The team sets a target velocity, then selects top-priority stories that support the goal: "As many stories are selected as necessary for the sum of their ideal day or story point estimates to equal the target velocity." (L3093). Stories are split into tasks and estimated only after that. The target usually comes from one of two figures: "The default assumption by most teams is that their velocity in the next iteration will equal the velocity of the most recent iteration" (L3120), called yesterday's weather, or a moving average over perhaps the last three iterations. A team new to working together must forecast velocity instead (L3122).

### Commitment-driven

The stopping rule is a judgement repeated per story: "the team is asked to add stories to the iteration one-by-one until they can commit to completing no more" (L3276). Each story is selected, split and estimated before the next is considered, because "after each story is split into tasks and the tasks estimated, the team decides whether or not they can commit to delivering that story during the iteration" (L3289). Near the limit, a team may drop a story and replace it with a smaller one (L3301). The check on capacity is on [[iteration-capacity]].

### Why Cohn prefers commitment

Cohn gives two reasons (L3346-L3348). Velocity measures coarse estimates and "is not accurate enough for planning the work of short iterations". And "a team would need to complete twenty to thirty user stories per iteration for errors in the story point or ideal day estimates to average out". He sets that against the count that actually occurs: "most teams plan between three and a dozen stories into each iteration" (L3354).

His illustration is a team with a velocity of thirty over five iterations. Deliberately picking six slightly easy five-point stories could raise that to forty, and picking slightly hard ones could lower it, so a small draw can land lucky or unlucky by chance (L3352-L3354). The conclusion is about scope of use: "since these differences do average out over the course of a release, velocity works extremely well for release planning" (L3356). The same reasoning, applied to a single item, is on [[story-points-do-not-convert-to-hours]].

### Velocity is a gauge and not a quota

The fictional case study in Chapter 23 (L4961) draws the line between the two uses. A team with a velocity of 16 plans 18, and when asked why, the coach answers:

> We use velocity as a guide for measuring our progress against the release plan
>
> — [[cohn-agile-estimating-planning]], L6296

> We don’t automatically plan each new iteration to have exactly the velocity of the last iteration or the average velocity of the last few iterations. We plan each iteration based on how much work we can commit to.
>
> — [[cohn-agile-estimating-planning]], L6296

The points are summed only after the commitment is reached, and the total is expected to land "somewhere close to our historical average, but it’s going to vary" (L6296). The team names what changed: the artist returns to art and away from testing, and one story already has a head start (L6300). Its second plan is also "15 total hours less than the last iteration" (L6304). The plan held, since they "had completed each of the stories they’d planned" (L6310).

This wiki reads a total far from history as a reason to ask what changed, and not as an error. The rule costs a judgement per period where a quota needs only arithmetic, and that judgement can be optimistic, so velocity stays as the check on it.

### Numbers and their conditions

The figures of twenty to thirty and of three to a dozen are Cohn's coaching experience, stated without measurement. The thirty-to-forty swing is a thought experiment and not a recorded result. The 16 and 18 of the case study are invented.

### The decision, by setup

This decision is merged into the table *Which way of filling holds under which setup*, above, so that one table answers for every setup. Two points from Cohn's comparison stand here. A total above recent velocity is acceptable when something named has changed, as in the case above, and otherwise it is a reason to stop. Cohn's hour sum is unavailable to the plugin, because it does not produce the level below a task ([[unit-of-work]]), so the stopping judgement in the one-at-a-time rows rests on the people steering.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Tasks per period | Board history |
| Velocity, and whether it is stable | Board history, on one scale |
| Top-priority tasks supporting the goal | The ordered backlog and the period's record |
| What changed since the last period | Named by whoever plans |

The choice was wrong if selections equal to velocity keep over- or under-running while the velocity figure itself stays steady. This wiki reads Cohn's mechanism as predicting exactly that when the selection is small. One-at-a-time filling was wrong if the people steering repeatedly commit past what history supports, or if a plan set above recent velocity ends with tasks unfinished.

### Trade-off

Commitment-driven filling costs more, because every story is examined before the next is added. Velocity-driven filling is cheap and can overfill or underfill a period by chance.

### Agent executor note

The averaging argument is statistical and holds for any executor. The value of asking a team whether it can commit depends on people answering for work, and an agent cannot do that ([[commitment-over-a-period]]). A velocity measured before a change of model or review practice is a poor guide (the rule at the top of this page). The case's first reason for going above velocity rests on one person's specialism and its hours on a human capacity estimate, and this wiki reads neither as transferring. The rule underneath does: a plan total may differ from past velocity when something named has changed, such as prior work on a carried task.

### Related

The stage this section fills is defined on [[planning-horizons]]. The measure itself is on [[velocity]].

## Utilization Versus Slack

A plan can aim at keeping everyone busy or at keeping room for tasks that run differently than expected, and Cohn holds that these pull against each other. He names the pursuit of full use as one of two reasons multitasking arises on a traditional project.

> Second, it encourages focusing on achieving a high level of utilization of all individuals on the project rather than on maintaining sufficient slack to cope with the inherent variability in typical project tasks. Loading everyone to 100% of capacity has the same effect as loading a highway to 100% of capacity: no one can make any forward progress.
>
> — [[cohn-agile-estimating-planning]], L646

Chapter 22 repeats the point as a guideline at the level of a period: "Especially when planning an iteration, do not plan on using 100% of every team member’s time." (L4941). The text is on the rule at the top of this page.

This wiki treats the highway as an analogy and not as evidence. Cohn reports no measurement and gives no figure for how much slack is sufficient.

### The rule

Do not fill a period to the full capacity figure. Leave a margin for tasks that run long, and do not plan that margin away with other work. The wording is this wiki's, from Cohn's reasoning.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Capacity for the period | As on the rule at the top of this page |
| How much finishes vary | Board history: spread of time in state for tasks of one size step |

The margin was too small if tasks repeatedly go back unfinished ([[unfinished-at-period-end]]). It was too large if the margin is never used, period after period. This wiki reads the test above for a selection that is too small as compatible with holding slack, since a real margin gets used by variability in most periods.

### Sign of violation

- **In a plan:** a selection built by adding estimates until they equal capacity, with nothing set aside.
- **In board history:** any overrun in a period forces something else out or late, because nothing could absorb it.

These signs are this wiki's. The charter excludes individual load, so they are read at the level of the period and not per person.

### Why

What breaks, on Cohn's account, is the ability to absorb variation. This wiki reads the consequence as an overrun on a fully loaded plan having nowhere to go, so it falls on other tasks, and it invites the partial deliveries described on [[multitasking]].

### Cost

This wiki notes the plain cost: a plan with a margin promises less than one without, and it reads as idle capacity to anyone counting.

### Which setup this applies under

Under an iteration setup, as above. Under a flow setup nothing is selected for a period ([[what-may-move]]), so this rule has no direct form there, and this wiki has no sourced equivalent.

### Agent executor note

Cohn's concern is individuals at full utilization. An idle agent costs almost nothing, so keeping an agent busy is not a goal and the human form of the argument does not transfer. This wiki reads the scarce resource as the review of the people steering, as on [[wip-control]] and the rule at the top of this page, and the margin as belonging there: results arriving at the full rate those people can review leave no room for one that takes longer. That reading is unmeasured.
