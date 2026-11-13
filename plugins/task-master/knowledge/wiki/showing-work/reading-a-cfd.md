---
title: Reading a Cumulative Flow Diagram
category: showing-work
summary: A fixed walk over the shapes of a CFD — mismatched arrival and departure lines, bulging bands, disappearing bands, flat lines, stair steps, S-curves, a persistent queue band read as a possible bottleneck — that turns each shape present into a question to check against context and item history, never into a verdict; each shape carries its sign, the causes the source names, and what would show the reading wrong.
tags: [method, cfd, visualization, flow, board-review, failure-mode, wip, queue, predictability, stability, batch, cadence, zero-wip, bottleneck, reporting-interval, methodology-difference]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading a Cumulative Flow Diagram

Reading a [[cumulative-flow-diagram]] (CFD) is the qualitative pass over the chart: walk a short list of shapes and, for each one present, ask the question that shape raises about the process. Vacanti states the purpose as asking and not concluding: "the reason we visualize flow via a CFD is so that we can begin to ask the right questions sooner" ([[vacanti-actionable-agile-metrics]] L1778). The output of a reading is a list of things to check, not a list of faults.

## Preconditions

- **Context.** "If you look at a CFD without understanding the context in which it was created, then all you are doing is looking at a picture." (L1776) Vacanti calls the diagrams "very context specific" (L1776).
- **The quantitative reading comes first.** Vacanti says qualitative analysis of a CFD requires sound knowledge of how to do the quantitative analysis, and sends readers who skipped it back to his Chapters 4 and 5 (L1780-L1788). See [[cumulative-flow-diagram]].
- **Little's Law assumptions, for any forecast.** "the predictive power of your CFDs depends almost entirely on how well your process obeys the assumptions behind Little's Law" (L1964-L1970). See [[littles-law]].

## The walk

The checks below follow the closing list of his Chapter 6 (L1974-L1986). Each has its own section below.

| Check | Sign on the chart | Question it raises |
|---|---|---|
| Arrival rate against departure rate | Top line steeper than bottom line | Why is more starting than finishing? |
| Bulges | A band widens | What is causing the increased WIP, and is the cause really in this step? |
| Disappearing bands | A band thins out to nothing | Is it the reporting interval, starvation, or a skipped step? |
| Flat lines | A line stays horizontal over a long period | Why is nothing getting done, and what gets it flowing? |
| Stair steps | A flat stretch followed at once by a jump | How is this batch affecting predictability? |
| S-curve | Flat, then steep, then flat, between two moments of zero WIP | Does the setup need WIP to reach zero? |
| A queue band that stays wide | A done sub-state ahead of a limited column stays thick | Is the next step short of capacity, or starved or disrupted? |
| Nothing wrong | Lines look even and close | What could improve next, and what could the picture be hiding? See [[cumulative-flow-diagram]] |

For anything found, Vacanti's closing questions apply: "What's going on with our flow?" "Is it a good thing or bad thing?" "If good, how can we keep doing it?" "If bad, what interventions can we take to make things better?" (L1948-L1954).

## Mismatched arrivals and departures

Work enters the process faster than it leaves. It is the first check in the walk, and the chart's form of a breach of [[conservation-of-flow]].

**Sign.** "the slope of the top-most line is steeper than the slope of the bottom-most line" (L1800). In board history, this wiki reads that as the count of items entering the first tracked state rising faster than the count reaching the last one, over the same window.

**What breaks.** When items arrive faster than they depart, WIP grows over time, and Vacanti says an increase in WIP "will almost certainly lead to an increase in Cycle Time" (L1802-L1808). Arrival rate equalling departure rate on average is also one of the key assumptions behind [[littles-law]] (L1808), so the arithmetic that would support a forecast stops holding.

"It is impossible to be predictable in a world where WIP constantly increases and Cycle Times elongate." (L1808)

"By definition, a process that exhibits a shape similar to Figure 6.1 is unstable." (L1810) Vacanti calls stability "fundamental to process predictability" (L1810), and defers causes and remedies to his Chapter 7. There, as the arrival line pulls away, "the amount of WIP in the system got larger and larger and the Approximate Average Cycle Times got longer and longer" (L2118). The action is to "get arrivals to match departures" (L2128), which starts with the limit on the arrivals column on [[constant-wip]].

**Dating the onset.** The earlier part of a diverged chart is also evidence: "When the Arrival Rate and Departure Rate lines were much closer together, you can see that WIP was much smaller and Approximate Average Cycle Times were much shorter" (L2118). This wiki reads that as a way to date when the imbalance began.

**The opposite shape: parallel lines.** Lines running roughly parallel mean average arrivals equal average departures (L2146-L2148). The source says any process that limits WIP throughout, and honors the limits, gets this picture (L2150); see [[constant-wip]]. A balanced chart is necessary and not sufficient; [[cumulative-flow-diagram]] holds the limit.

**What separates it from a neighbouring case.** The assumption is about rates "on average" (L1808), so a short mismatch is not this pattern. His Chapter 6 gives no window length. This wiki reads the sign as a slope difference that persists, with the gap between the lines still widening at the end of the window. The steep start and flat end of an S-curve are temporary mismatches of a different kind (below).

A later fact would show the reading wrong: the two slopes converge without any change to the process.

**With an agent executing.** The mechanism is arithmetic on counts, so this wiki holds that it survives an agent executing. The transfer here is ours: where an agent finishes work and a person accepts it, whether the bottom line means "agent finished" or "person accepted" decides what the pattern says. A gap measured to acceptance may be a gap in the person's review and not in execution, which is worth settling before asking why work is not leaving.

## Bulging band

A workflow step's band widening over time. Any such bulge "clearly signals an explosion of WIP in that particular workflow step" (L1860). The band's thickness at a date is the [[work-in-progress]] in that step.

**Sign.** A band visibly wider than its own earlier width. Vacanti gives no ratio.

**What breaks.** "large WIP is bad because it almost always results in longer Cycle Times and poorer predictability" (L1866). Vacanti's first question is "what is causing our increased WIP" (L1866).

**Causes the source names.** Vacanti's answer depends on the situation, and he offers examples (L1872):

- The team is ignoring WIP limits and starting new work arbitrarily.
- Several key team members have gone on holiday for extended periods.
- Work is progressing slowly due to poor requirements or poor design.

**The cause may not be in the step that bulges.** "the cause of the increased WIP may not necessarily be found in the workflow step where the bulge appears" (L1874). Vacanti names a push from a previous step, or a blockage in one or more downstream steps, and warns: "Do not be lulled into thinking the problem is always in the obvious place." (L1874)

This wiki turns that into a check on the neighbouring lines. If the line entering the step steepened while the line leaving it held, look upstream at what pushed the work in. If the line leaving it flattened, either the step itself or a downstream step stopped moving work: the in-step causes above (slow work from poor requirements or design, absence) produce exactly that signature. Before looking downstream, check whether the next queue band is thick, which points to a downstream block, or the next active band starved, which points back into the step. This test is ours, and the chart only says where to look next.

**Queue bands are the worse case.** Vacanti recommends splitting each workflow step into "Active" and "Done" sub-steps and graphing both. The "Done" sub-steps are queuing columns: "columns where no value add work is happening; work is just sitting there waiting to be pulled" (L1876). See [[active-versus-queued]].

"while a bulging band in general is bad, a bulging band in a queuing step can be especially bad" (L1876). Queue bands should be "as thin as possible", and "Whenever those bands are constantly thick or whenever they bulge, then that pattern is suggesting something is going wrong with our process" (L1876).

This wiki reads that as giving queue bands a second sign that active bands lack: a band need not grow to raise the question, because staying thick is enough. The section on a persistent queue band below takes that sign to a procedure.

**With an agent executing.** This wiki reads the causes differently under an agent. Starting past a limit survives if the limit is what the person dispatching work ignores. Poor requirements survive and probably sharpen, since an executor that guesses cannot fill the gap from context. The holiday cause survives only for the person. A queue band in front of a person's review measures that person's part, so a thick one there says something about review and not about execution.

## Disappearing band

A workflow step whose band thins out to nothing. Vacanti says such bands "could be telling us one of several things" (L1884), and names three. The chart alone does not separate them.

| Cause | Source's account | Test (this wiki's) |
|---|---|---|
| Reporting interval too coarse | "the reporting interval that we have chosen is too big" (L1884). With weekly reporting and a Test column passing work in a day or two, any given reporting point will likely show zero WIP there, so the band does not appear (L1884). | Item history shows entries into the state, but each lasted less than one interval. Redrawing at a finer interval brings the band back. |
| Downstream starvation | "some upstream variability in our process is causing downstream steps to be starved" (L1890). | No items entered the state during the gap, and earlier steps show uneven delivery. Work resumes through the step later. |
| Skipped step | "the team frequently decides to skip a certain step in the workflow altogether" (L1892). Vacanti's deliberately exaggerated example is a team near the end of a release skipping Test and pushing work from Development straight to production (L1892-L1898). | Items reached later states with no entry into this one in their history. |

This wiki reads the first cause as a defect of the chart and the other two as facts about the process.

For the skipped step, Vacanti does not rule: "It would be up to you to decide given your particular context whether this is good or bad." (L1898)

This wiki adds what would show a reading wrong. A chart redrawn at a finer interval that still has no band rules out the first cause, and a history showing every item passed through the state rules out the third.

**With an agent executing.** The transfer here is ours. An agent can pass through a step in far less time than a person would, so the coarse-interval cause is likely to be more common on such a board, and a state that has become too quick to show may no longer be a step worth drawing. A skipped step keeps its meaning, with the added question of who decided to skip it, the person or the agent.

## Flat lines

A stretch over which a cumulative line does not rise, meaning no item crossed that boundary during the stretch. Because the lines are cumulative, "lines can never go down" (L1814), so flat is the lowest reading they can give. This wiki treats a line that does go down as a defect in the chart or its data and not as a process shape; see the signs on [[cumulative-flow-diagram]].

**Sign.** "any lines that flatten out over long periods of time" (L1814). Vacanti gives no length for "long". In a board history, this wiki reads it as no item crossing a state boundary across the stretch.

**Which line is flat.** Vacanti says such lines can represent "either periods of zero arrivals or periods of zero departures", and that the usual concern is departures (L1824): "zero departures means nothing is getting done", so "no value is being delivered to the customer (or to a downstream step)" (L1824).

This wiki's reading of the parenthesis is that an inner line can show this too. An inner flat line means a step has stopped passing work on, even if the bottom line is still moving for a while on what is already past that step. All lines flat together means nothing moved anywhere.

**What breaks.** Vacanti leaves the effect as questions: what happens to the Approximate Average Cycle Time drawn as a horizontal line, and what happens when zero Throughput is put into Little's Law while WIP is nonzero (L1828). This wiki's answer is that the horizontal distance grows for every item in progress during the stretch, and that WIP divided by a Throughput of zero has no finite value, so [[littles-law]] stops giving a usable Cycle Time for that period.

**What to ask.** Vacanti says "an emergent flat line on a CFD should trigger some type of urgent conversation" and names two questions (L1830):

- "Why isn't anything getting done?"
- "What can we do to get things flowing again?"

This wiki keeps these as the finding's content. Running the conversation is out of scope.

**Causes the source names.**

- Holidays with most staff away, such as "the two weeks around Christmas and New Year's in the U.S." (L1826).
- An external block, such as "the whole test environment being down such that testing cannot complete" (L1826).

The source lists these as examples, not as a complete set: "There are all kinds of circumstances that could cause this pattern to emerge" (L1826).

**What separates it from stair steps.** A flat stretch followed immediately by a jump is a batch transfer, not a stop (L1834-L1840; next section). This wiki's test is to look at what comes after. A jump that clears the accumulated work points to a batch, and a return to the old slope with nothing made up points to a real stop.

**With an agent executing.** This wiki reads the external block as surviving unchanged. The holiday cause survives only in altered form: an agent does not take leave, but a person it waits on does, so a flat line may mark the person's absence and not the executor's.

## Stair steps

The shape a batch transfer leaves: "a flat period on a line (as discussed above) immediately followed by a jump up in arrival rate" (L1834-L1840). This wiki reads the mechanism as items that move together crossing the line together, so the line waits and then rises at once.

**Examples with their settings.**

- Daily reporting interval, input column replenished every five days: "five straight days of a flat input line followed by an immediate increase when the column is replenished" (L1846).
- The bottom line represents a production deployment that happens every three months (L1846). Vacanti leaves the resulting shape as a question.

**Cadence is not required.** Vacanti corrects a common attribution: "Any batch transfer—whether due to a regular cadence or not—will cause these stair steps to form." (L1848) The two cases differ in appearance:

- Regular cadence: "the stair steps will be of roughly uniform size and shape" (L1848).
- Nonregular batch: "a more uneven appearance to the steps" (L1848).

**A sign, not a defect.** "batch in and of itself is not necessarily a bad thing" (L1856). Vacanti asks how the batch affects predictability, "positively or negatively", and then:

> Can those periods of batch be reduced? Eliminated? Should they be? What would it take to do that? What would the impact to Cycle Time be?
>
> — [[vacanti-actionable-agile-metrics]], L1856

**Per project setup.** This paragraph is this wiki's reading, not Vacanti's. On a setup with a fixed period, uniform steps are what the chosen cadence produces, so finding them is not a finding against the board, and the question left is whether the period suits the work. On any setup, uneven steps show a transfer that follows no stated rhythm, which is the more useful thing to check. A flat stretch with no following jump belongs to flat lines, above.

**With an agent executing.** This wiki holds that the shape survives an agent executing, because it comes from when items cross a line and not from who does the work. Where a person replenishes the input or accepts finished work in sittings, the batch belongs to the person's rhythm, so that is where this wiki would look first.

## S-curve

"the typical pattern that emerges on CFD between any two time instances of zero WIP" (L1904). It "is characterized by a flat beginning section, followed by a steep middle section, and finishing again with a flat end period" (L1904). Vacanti says the cause of the shape is beyond the scope of the section (L1914), so this section holds its sign and its consequence, not its mechanism.

**Where it appears.** Vacanti gives two settings, both the special case of Little's Law where system WIP may reach zero (L1902), which [[littles-law]] calls the exact case.

- A project, which "usually begins with zero WIP and (ideally) ends with zero WIP".
- An "ideal Scrum sprint", which "starts with zero WIP and ends with zero WIP".

**What it costs.** Vacanti asks whether, on such a curve, it is easy or even possible to match arrival and departure rates (L1914), which is the assumption the mismatch check depends on. He then states: "those flat spots add inefficiencies and kill predictability" (L1918-L1924).

His argument runs on as questions: whether managing projects this way is optimal, whether it is "predicatively optimal" to repeat the effect through zero-WIP-bounded sprints, and "How might we become more predictable day to day, week to week, month to month by never allowing WIP to go to zero?" (L1916). He limits the claim: "I am talking about predictability here, not necessarily about how accounting or finance sees the world" (L1916). He ends the section with "Just something to think about…" (L1926). This wiki reads this as a position argued from Little's Law's assumptions, not a measured result, and notes that no figure is given.

**Per project setup.** This paragraph is this wiki's reading. Scrum's ideal and Vacanti's preference disagree about whether WIP should reach zero at a boundary.

- **Setup with a fixed period that empties.** A repeating S-curve is what the setup produces. It is not a finding, and a forecast within the period should allow for the flat ends and not use the steep middle's rate.
- **Continuous setup with no emptying boundary.** A repeated return to zero WIP is unplanned, so it is worth asking why: arrivals may be batched, or the queue may be running dry.
- **Small board with an agent executing.** WIP may reach zero simply because nothing is waiting. Vacanti does not address this scale, and the argument against zero WIP assumes a steady supply of work, so this wiki would not read that case as a defect.

What would show the first reading wrong: the same work run without an emptying boundary gives steadier delivery with no loss elsewhere.

## A queue band that stays wide: a possible bottleneck

The Siemens case ([[vacanti-actionable-agile-metrics]]) gives the pattern. Management saw higher Throughput in developing than in testing across all teams and decided to invest in test automation to rebalance capacity. The case credits the CFD itself: "Cumulative flow diagrams provided a full picture at the individual team and program levels where our capacity weaknesses lay", and "at the enterprise level using the Cumulative Flow Diagram the management team was able to see higher Throughput in “developing” versus “testing” across all teams" (L4192). The case says the sign was easy to see, because "the “developing done” state on the CFD consistently had stories queued up waiting for the “testing” column WIP limits" (L4192). A separate instance in the same case analyzed "Throughput (story run rate) and Cycle Time for each column (specifying, testing and developing)" to see "where we were experiencing capacity problems" (L4184).

### A disagreement inside the book

The case and the author do not say the same thing. Of looking at a CFD alone, Chapter 6 says: "It is impossible to spot a systemic bottleneck." (L1944), and [[cumulative-flow-diagram]] keeps that as a rule for wording. The case, told in Vallet's voice, says the shortfall "was actually easy to spot" (L4192). Vacanti's dissent is partly about language as well: he prefers "Deming's and Shewhart's language of variability to that of Goldratt's language of the Theory of Constraints" (L1944).

This wiki does not read the case as having resolved this by numbers: L4192 credits the chart, and L4184 is a separate instance. Per-column Throughput is itself a slope on the same CFD (Property #6 corollary, L1670), so per-column rates do not escape L1944 by being numbers. The rule is this wiki's caution, and it agrees with [[throughput]]: per-column rates, whether read as CFD slopes or from item history, and per-column Cycle Time from item history raise the question of a constraint and say where items wait; they do not name one. A finding may use the word "constraint" only if it also states how variability was ruled out, which is the condition Vacanti attaches to per-step Throughput, "assuming variability has been taken into account" (L746), and even then it is worded as a hypothesis to check. The Siemens case (L4192) stays the source's counter-voice, and this wiki does not adopt it as the rule. The reason is that a wide band says where items wait and not why.

### Procedure (this wiki's)

1. Look for a queue band, a done sub-state ahead of a limited column, that stays wide over time and does not merely swell once (the bulging-band sign above).
2. Check it against per-column Throughput (the slopes either side of the step) and per-column Cycle Time from item history.
3. Choose where to act. At the team level, Siemens adjusted WIP limits "to ensure flow and prevent the build-up of bottlenecks" (L4192). At the program level, it shifted capacity to the constraint, with test automation.
4. Recheck the band. This wiki reads a band that narrows while downstream Throughput rises as support for the hypothesis, not proof of it.

### What it needs

A band like this appears only if the board has a queue state and the next column has a limit. This wiki reads the converse as well: without them the same queue is hidden inside a column; see [[active-versus-queued]] and [[wip-control]].

### What it does not answer

A wide band says where items wait, not why. Whether testing lacks capacity or was starved or disrupted needs other evidence: the source links its testing bottlenecks to builds and environments as well (L4192). This wiki reads a band that grows while the whole diagram widens as a general arrival problem, for which [[conservation-of-flow]] comes first.

### Trade-offs

Adding capacity at a constraint costs money or attention, and in an unstable system improvement risks sub-optimization: "Continuous improvement in a system that is unstable always runs the risk of improvement initiatives that result in sub-optimizations" (L4260). See [[starting-more-work]]. Which chart answers which question is collected at [[which-chart-for-which-plan-question]].

### Agent executor note

The source's example is a functional split between developers and testers, at enterprise scale. The transfer here is ours: on a board where a few people steer agents, the expected band is work awaiting a person's review. The lever there is the review queue and the cut of the work, and more agent runs would only widen the band.

## Failure modes of the reading

- **Snap judgement.** "you will be tempted to jump to snap judgments the next time you see a Cumulative Flow Diagram. Do not." (L1778) This wiki takes the sign to be a finding that states a cause from the shape alone, with no question to check.
- **Reading the list as complete.** Vacanti offers these as "some of the more common things you will come across", and says all possible patterns would fill a book (L1948).

## What a finding should carry

Vacanti gives no threshold for how steep, how long or how thick a shape must be. This wiki does not invent one. It reads the charter's rule that a sign raises a question ([[smell-is-not-a-finding]]) as requiring a finding to name the shape, its date range, the line or band involved, and what to check next.

The cost of the method follows from that. Without the project's context, a reading yields questions and no conclusions.

## Agents and small teams

This wiki's reading is that the shapes survive an agent executing, because they are arithmetic on counts taken from board history. The causes do not all survive: several of Vacanti's examples are about people, such as holidays and ignored limits, and each section notes which carry over. Vacanti does not discuss scale here. This wiki adds that on a board with few items a single move can change a shape, so a short stretch deserves less weight than the same stretch on a busy board.
