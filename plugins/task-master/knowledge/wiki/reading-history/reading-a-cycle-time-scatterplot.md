---
title: Reading a Cycle Time Scatterplot
category: reading-history
summary: A procedure for turning the shapes on a cycle time scatterplot — a triangle that never flattens, high or low clusters, gaps and boundary stacks, extreme outliers, dots just past a percentile line — into questions about the policy that produced them; the chart shows variation but does not classify it. High dots tend to have outside causes and low ones inside causes; every dot stays in history, and only a named temporary condition may be left out of a forecast sample.
tags: [method, scatterplot, cycle-time, variation, visualization, failure-mode, decision-rule, flow-debt, wip, batch-transfer, iterations, outliers, forecasting, data-quality]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading a Cycle Time Scatterplot

Reading a [[cycle-time-scatterplot]] means inspecting the shapes formed by finished items, plotted by finish date (X) and cycle time (Y), and turning each shape into a question about the policy that produced it. Vacanti treats the chart as a way to reach the right question sooner, not as a detector that returns an answer. That matches this wiki's stance that a sign raises a question, not a verdict: see [[smell-is-not-a-finding]]. The walk over a CFD's shapes is the sibling page, [[reading-a-cfd]].

## Procedure

1. **Look for a shape, not at single dots first.** The chapter's checklist has five things to look for ([[vacanti-actionable-agile-metrics]] L2992-L3006): a triangle that never flattens, clusters of dots, high or low, long periods of gaps, extreme outliers, and dots that just cross a percentile line. Each has a section below.
2. **Ask which policy produced it.** Vacanti's first question for any anomaly is “What policy (either explicit or implicit) do we have in place that is causing our data to look like this?” (L2852). Implicit counts: a habit nobody wrote down is a policy for this purpose.
3. **Ask whether it is good or bad.** The chapter's questions are “What’s going on with our Cycle Time?”, “Is what’s going on a good thing or bad thing?”, “If good, how can we keep doing it?” and “If bad, what interventions could make things better?” (L2982). The second one cannot be skipped, because a pattern that looks like an improvement can be a defect, as with a low cluster.
4. **Change the policy, then check it on later data.** Vacanti's loop is to use the data to suggest a policy change, “then verify the change had the intended effect by further collecting and re-examining future data” (L2852). A change with no later reading of the same chart is unverified.

**Inputs, and where each is read from.** The finish date and cycle time of each finished item come from board history; the percentile lines are computed from the same history ([[cycle-time-percentile-lines]]). The CFD reading used to separate causes comes from the same transitions ([[cumulative-flow-diagram]]). Nothing here needs logged hours.

**What would show a reading wrong.** The policy change is made and the shape persists on later data, which is step 4's check.

## Why policy comes first, and where it stops

The chapter's maxim is “Your policies shape your data and your data shape your policies” (L2850), and Vacanti closes on “most of the causes of randomness are things we do to ourselves” (L2984). The same chapter also says that extreme outliers are usually caused from outside the team (L2960).

This wiki reads those two claims as compatible: shapes formed by many dots point at policy, while the few extreme dots at the top point outside. A reader who applies “it's our policy” to a 181-day item, or “it's external” to a triangle, has picked the wrong default for that kind of signal. The split is the wiki's reading and the chapter does not state it in that form.

## Triangle that never flattens

A wedge of dots whose upper edge rises over time. Vacanti says it appears “in any situation where Cycle Time increases over” time (L2858-L2866, joined across a page break). The pattern on its own is not a defect: it is expected while a process fills from empty. The sign to act on is a triangle that keeps growing, which the chapter lists as “A triangle pattern that never flattens out” (L2994).

**Why the shape is a triangle.** The explanation rests on the chart's basic property, that a dot appears only when an item finishes. Vacanti: “the longer the Cycle Time (the dot’s Y- component) the longer the amount of time we are going to have to wait (the dot’s X-component) to see that data point” (L2872). Long-lived items therefore land late on the chart, which pushes the top of the scatter up and to the right.

This wiki adds a consequence: the right-hand edge of any scatterplot under-represents long items, because the ones still in progress have not landed yet. A chart read at its right edge looks better than the process is.

**The cases, and how to separate them.**

| Case | What the CFD shows | What it raises |
|---|---|---|
| Starting from zero WIP | Lines start together while steps fill | Nothing, if it flattens |
| Arrivals exceed departures, WIP never at zero | Top and bottom lines diverge | Why intake outruns finishing; see [[wip-control]] |
| Flow debt | Lines stay matched, and the triangle is there anyway | A question: is the debt serviceable? See [[flow-debt]] |

The table's first column is Vacanti's two major cases, with the start-up situation split out from the first. The discriminating test is his too: “If Arrival Rate and Departure Rate are matched, then the only way you will not see a triangle on your Scatterplot is if you control Flow Debt.” (L2896). Vacanti does not want the reader "to conclude that all Flow Debt is bad" (L2456), so the third row is a question, not a verdict.

**Starting from empty.** While steps fill, “work will be pulled in faster than it departs—even if we are limiting WIP” (L2882), so a WIP limit does not prevent this triangle. Once stable flow occurs, “the expectation is that the triangle will eventually flatten out into a more predictable arrangement” (L2882); Figure 11.2 shows this happening when the process stabilizes (L2888).

**Arrivals exceed departures.** When WIP never reaches zero, “a triangle will form whenever you have a nontrivial period of time where the top line and bottom line on your CFD diverge” (L2890). Vacanti suggests his example could be due to a team that did not control WIP: “The pattern in Figure 11.1 could be due to the fact that for almost the whole timeline of the process represented here, this team did not control WIP.” (L2890). He adds: “Not controlling WIP will only cause Cycle Times to get longer and longer and longer.” (L2890). The mechanism is on [[starting-more-work]], the CFD form on [[reading-a-cfd]], and the response is [[wip-control]].

**Flow debt.** “Even if a team explicitly controls WIP, Flow Debt can occur.” (L2896). Vacanti's reading of the shape: “The items at the bottom of the triangle were those items that were pulled preferentially through the process (for whatever reason) whereas items toward the top of the triangle were left to age unnecessarily (again, for whatever reason).” (L2896). The named causes of arbitrary aging are blocks, too much WIP, and poor or misunderstood pull policies (L2896). This case is the trap: a team that holds its WIP limit and sees a triangle has not ruled out a pull-order problem. See [[flow-debt]] and [[blocked-work-counts-against-wip]].

**Sign and check.**

- **Sign:** on the scatterplot, the top of the dots keeps rising with no plateau, past the point when the process should have filled.
- **Check first:** read the CFD for the same interval. Divergent lines point at intake exceeding finishing. Matched lines point at pull order and aged items.
- **Later fact that settles it:** after WIP is held or the aged items are pulled through, later dots should flatten. A triangle that continues means the cause was not the one assumed.

The chapter gives no duration after which a triangle counts as not flattening, and this page does not invent one.

**How the reading goes wrong.**

- **Calling a start-up triangle a defect.** A project read before it has reached stable flow shows a triangle whatever its policies. This wiki notes that a short project may never leave this phase, so its whole history can be a triangle with nothing wrong in it; the plugin should say so and not raise a finding.
- **Stopping at “we limit WIP, so it isn't that”.** That excludes one cause only. Flow debt remains.

**Under an agent.** This wiki's judgement is that the mechanism survives: dots land at finish whoever executes, and the shape is arithmetic. The causes shift. An agent does not pick favourites, so preferential pulling, in this setting, would come from the order the person or the plan sets, or from easy tasks being re-prioritized past older ones. Arrivals exceeding departures would come from tasks being generated faster than presented results get reviewed. Both transfers are the wiki's own and are unsourced.

## Clusters, high or low

A cluster is a group of dots sitting well away from the usual scatter over a short interval. Clusters of any height are a thing to look for (“Clusters of dots (either high or low)”, L2996), and the chapter's sharper claim is about the pleasant-looking kind: “not all clusters of very low Cycle Times are good.” (L2912). A drop in cycle time is an event to explain before it is accepted as an improvement.

**What to ask.** Vacanti's order for any cluster is “what’s going on here?”, then “is this a good thing or a bad thing?”, then what can be done if it is bad (L2910). The chapter then presses the reader on the second question: “Are you only thinking of good reasons? What might be some bad reasons that would cause this to happen?” (L2912). Only the low case is explored; the chapter names high clusters and does not work through one.

**Why a temporary gain poisons the data.** The bad reason Vacanti names is mandatory overtime. His arithmetic is that moving from 8-hour days and 5-day weeks to 12-hour days and 7-day weeks will probably improve cycle time, on the condition that WIP stays limited (L2912-L2918). The damage is to predictability: “Not only are long periods of mandatory overtime not sustainable but it also skews our data.” (L2918). He then puts the question that makes the point: “Do you really want to be offering an SLA or making a forecast with mandatory overtime as one of the upfront assumptions that is baked in?” (L2918).

This wiki keeps that mechanism and drops the practice. Overtime as a way of managing people is out of scope; what is in scope is that history used for a forecast or a [[service-level-expectation]] silently assumes the conditions it was produced under.

**Sign and check.**

- **Sign:** a band of dots clearly below the surrounding scatter, in a bounded interval, with the scatter returning afterwards or not yet returned.
- **Check:** name what changed in that interval. Inputs are the finish dates on the board, plus whatever the project records about who was available and what kind of tasks ran then.
- **Choice that follows:** whether those dots belong in the sample used for forecasting. The rule for that is in the section on which dots feed a forecast, below.
- **Later fact that shows the choice wrong:** cycle time stays at the new level after the supposed temporary condition ended, so the change was real and belonged in the data.

**Under an agent.** The overtime mechanism itself does not survive: an agent has no overtime, and its hours are not the constraint. This wiki's judgement is that the general form does survive. Any temporary change in capacity or in the mix of work lowers cycle time for a while, and a forecast reads it as the process. In a setting with a few people steering an agent, the plausible equivalents are a burst of unusually available review, or a run of tasks much smaller than usual. Those equivalents are the wiki's own and are unsourced.

**Source note.** The book refers to the cluster chart as “Figure 8.11” at L2910 and L2912, while introducing and describing it as Figure 11.3 at L2900 and L2910. The discussion is plainly about the one chart; this reads as a stale cross-reference in the source. See also [[velocity-trend-is-not-a-forecast]].

## Gaps, and stacks at a boundary

A gap is an interval with no dots. Vacanti defines it plainly: “Gaps in the dots on your Scatterplot means that no work items finished in that particular time interval.” (L2922). It measures finishing, not working, so a gap does not show that nothing happened, only that nothing completed.

A gap is the same event as a flat section on the [[cumulative-flow-diagram]] ([[reading-a-cfd]]): “Flat lines on the CFD mean nothing completed; if nothing has completed then no dots will show up on your Scatterplot.” (L2922). This wiki reads the two charts as confirming each other, so the interval should match.

The causes Vacanti lists are the ones that flatten throughput on a CFD: “public holidays, external blockers, batch transfer, etc.” (L2922). The chapter's checklist says “Long periods of gaps in the data” (L3002) and gives no duration.

| Cause | How to tell |
|---|---|
| Holiday or planned absence | The interval matches a known calendar date; no action |
| External blocker | Items sat in place through the interval and share an outside dependency; see [[waiting-versus-blocked]] |
| Batch transfer | Gaps repeat on a rhythm, with stacks of dots between them |

The “how to tell” column is this wiki's, built on the causes Vacanti names. The inputs all come from board history and the project's calendar.

**Batch transfer: stacks at the boundary.** Vacanti singles out the batch-transfer form, common on Scrum boards: “The stacks of dots that you see here are at the sprint boundaries when there is a mad rush to complete work items. But look at how the data thins out between those stacks.” (L2934). He leaves the assessment as questions: whether it is good or bad, and “what impact is this having on our predictability?” (L2934). The same event on a CFD is stair steps ([[reading-a-cfd]]).

This wiki answers those per project setup, and the answer is ours rather than the source's.

- **Timeboxed setup.** Stacks at the boundary are the visible form of [[end-of-period-crunch]]. The question is which of two things is happening: work really finishing in a rush, or work finished earlier and only marked at the boundary. A rush is a process finding; a late mark means the dates misreport and the cycle times are inflated by the wait for the boundary.
- **Flow setup, no period boundary.** There is no boundary to explain a stack, so a repeating stack points at a batched handoff somewhere, such as review or release done on a rhythm.
- **In either setup, the effect on predictability.** The wiki reads stacked dots as measuring the cadence as much as the work: an item's cycle time then depends on where in the cycle it started. Percentiles taken from such data describe that mix, which is worth stating when a [[service-level-expectation]] is drawn from it.

**Later fact that would show the reading wrong:** if finish dates stay stacked after the handoff or the boundary habit changes, the stacks did not come from that policy.

**Under an agent.** The gap survives unchanged, since it reads finish events. This wiki's judgement is that the batch-transfer form becomes more likely with an agent executing and a person steering: an agent can finish several tasks while the person is away, so if “finished” means accepted, the dots land together on the review day. Whether such a stack is a defect depends on where the board's finished point sits; see [[started-and-finished-points]]. That transfer is the wiki's own and is unsourced.

## Extreme outliers and dots just past a line: where the cause tends to lie

Internal and external variability is Vacanti's working split for where to look for the cause of a dot, based on its height. High up, the cause is more likely outside the team; low down, more likely inside it. It decides where an investigation starts and who can act on the result. It is a tendency to start from, not a classifier (see what the chart cannot say, below).

**The rule.**

- **Up the stack, start outside.** “More often than not, those outliers will be caused by circumstances that are outside of the team’s control.” (L2960).
- **Down the stack, start inside.** “As you move “down the stack” the work items that took less time to complete were generally due to reasons that were totally under the team’s control.” (L2962).
- **Just past a percentile line, act.** Of dots that barely cross the 85th percentile, Vacanti asks whether the team could have prevented the violation, and answers “Probably” (L2962-L2968, joined across a page break), naming “swarm or break up the item” (L2968). The chapter's checklist lists “Dots that just cross a give percentile line” (L3006).

**Worked figures.** The example is Figure 11.5: 50th percentile 20 days, 85th percentile 44 days, one item at 181 days (L2960). These are one illustrative data set in the book, not a benchmark. The external reasons offered for the 181-day item are a dependency on an external vendor or another internal team, no test environment immediately available, and a customer not immediately available for sign-off (L2960); the book offers these as possibilities for that dot, not as findings.

**Keep the outliers.** Vacanti's position is that “while those points are outliers, they obviously happened and probably warrant some deeper investigation” (L2958), and that even if statistically insignificant “there might be some good contextual or qualitative reasons to keep them in from an analysis perspective” (L2958). Proving a dot statistically irrelevant is therefore not a reason to stop asking about it.

**Where the rule fails.** Vacanti gives the exceptions himself: “Will all outliers be due to external causes? Certainly not.” (L2970). His internal examples at the top are “Maybe the team allowed an item that ended up being too big into the process. Maybe the team ignored an item once it had been pulled.” (L2970). In the other direction, “will there be external issues hiding in the shorter Cycle Times? Almost certainly.” (L2970).

The rule also has a condition: “the more you adhere to the assumptions of Little’s Law, the more confident we can be that the “up the stack” dots are due to outliers, and the “down the stack” dots are due to team policies.” (L2970). This wiki reads the converse as the practical warning: on a process that breaks those assumptions, for example with uncontrolled WIP ([[littles-law]]), height says less about cause, so the split should be stated with less confidence.

**Applying it.**

- **Inputs.** Cycle time per finished item and the [[cycle-time-percentile-lines]] come from board history. Causes come from what the board recorded about the item: blocks, waiting, comments.
- **Output.** A question to check per dot, starting from the side the height suggests. A high dot with no recorded outside cause raises the “too big” or “ignored after pull” question; see [[diagnosing-unfinished-work]].
- **What later fact shows the choice wrong.** The investigation of a high dot finds an internal cause, or of a low one an external one. Vacanti's exceptions say to expect some of each, so one such result does not break the rule; a run of them says the process does not meet the condition above.
- **Cost.** Attention goes to the extreme dots, which are the ones least under the team's control by this same rule. The dots just past the line are where action is cheapest, and this wiki reads that as a reason to look at both groups and not only the dramatic one.

**Under an agent.** This wiki's judgement is that the split survives, with “the team” redefined. For a few people steering an agent, a wait on the steering person is inside the team's policy, so such a dot does not count as external even when it looks external from the agent's side. Of Vacanti's two remedies, breaking up the item carries over directly ([[story-splitting-patterns]]); swarming assumes several executors on one item and may not carry over to a single agent. Both notes are the wiki's own and are unsourced.

## Which dots feed a forecast

The low cluster and the outlier pull in opposite directions: one suggests leaving dots out, the other keeping them. This wiki settles it by what the data is for; the source states no rule for excluding dots.

- **History and analysis keep every dot.** That follows L2958 directly.
- **A forecast or SLE sample may leave dots out only for a named temporary condition,** such as the overtime in Vacanti's low-cluster case (L2918), and the report says what was left out and why.
- **A high outlier from an external cause stays in the forecast sample by default.** The instance may not recur, but such causes recur as a class: vendors, environments and sign-offs are Vacanti's own list for one dot (L2960).

What would show this wrong: forecasts made from the trimmed sample are missed in the direction the dropped dots pointed.

## What the chart cannot say

**It does not classify variation.** Vacanti writes: “I believe that it is mostly impossible to classify variation of your data into things like “special causes” or “common causes” simply by looking at a Scatterplot” (L2936), and “Use the Scatterplot as a powerful way to visualize variation. But do not think it will magically categorize that variation for you.” (L2972). A finding that says a dot *is* special-cause overstates what the chart can support.

**Variation is not the enemy.** Vacanti's position is that variation “will always exist”, and that “the point is not to always try to drive variation out; rather, the point will be to understand the causes of that variation” (L2944). This wiki reads that as ruling out a goal stated as a narrower scatter with no cause named. Chapter 12's aim to shift the percentile lines down by removing "unnecessary variability" (L3036, L3050; [[cycle-time-percentile-lines]]) agrees with this once a cause is required.

**It avoids the SPC argument on purpose.** The chapter deliberately drops the language of Statistical Process Control, not from disagreement with Shewhart and Deming, but because for most people the path “leads to academic debates” over control limits, and “These types of debates only serve to cause confusion and miss the point of what we are trying to accomplish anyway.” (L2972). Control limits on a cycle time chart are therefore not part of this procedure; see [[pseudo-control-chart]].

**It cannot show open work.** The chart's fundamental property is that “dots do not actually show up until a work item has finished” (L2872). This wiki draws the consequence: an item stuck right now is absent from this chart, and it arrives later as a single high dot, after the moment to act has passed. A question about what is stuck now needs age of open work, not this chart; see [[work-item-age]] and [[which-chart-for-which-plan-question]].

## Trade-offs and limits

- Reading shapes is a judgement. Vacanti says as much: “you are still going to have to think for yourself in order to get more predictable” (L2972-L2978, joined across a page break).
- The chapter gives no minimum number of dots for a shape to be meaningful, so a small board's shape is weaker evidence than the book's multi-year charts. The book's figures run over many months.

## Survival under an agent

This wiki's judgement is that the procedure survives an agent executing and a person steering: it reads board history and depends on no human memory. What moves is what a “policy” is. In this setting the likely policies are how tasks are cut, what order they are pulled in, and when the person reviews a presented result. That list is the wiki's own and is unsourced.
