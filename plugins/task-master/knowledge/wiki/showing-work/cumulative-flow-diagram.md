---
title: Cumulative Flow Diagram
category: showing-work
summary: A chart of cumulative arrivals to and departures from a process over time, built from per-item entry dates and not from counts; read vertically for WIP, horizontally (backward, plus one) for an approximate average Cycle Time and by slope for exact average Throughput, but only if it obeys six properties, only about the past, and never as proof of health, a bottleneck or a cause. Its signs of malformation are a falling line, a line that falls once later steps are hidden, an outer line that is not arrivals or departures, a graphed backlog whose time the Cycle Time leaves out, and a plotted projection.
tags: [concept, showing-work, cfd, flow-metrics, board-history, visualization, retrospective-analysis, kanban, failure-mode, method, cycle-time, throughput, wip, bottleneck, flow-debt, arrivals, departures]
sources: [vacanti-actionable-agile-metrics, scrum-guide-2020]
created: 2026-11-02
updated: 2026-11-02
---

# Cumulative Flow Diagram

A Cumulative Flow Diagram (CFD) plots, over time, how many items have arrived at a process and how many have departed from it, and optionally the same for each step in between. Vacanti's first point is that CFDs "are all about arrivals and departures" ([[vacanti-actionable-agile-metrics]] L1164); the earliest reference he found, from the 1960s, called the chart a "Cumulative Arrival and Departures Diagram" (L1164). He presents it as "a concise, coherent visualization of the three metrics of flow" (L1174); see [[flow-metrics]] for what those count.

His claim for it is that one diagram shows WIP, Cycle Time and Throughput together, "albeit sometimes in the form of averages or approximate averages" (L1720). The claim is conditional: "You can only be guaranteed to calculate these metrics, however, if your graph obeys all six properties of a CFD" (L1720).

This page holds what the chart is, how it is built, how numbers are read off it, what makes a chart not a CFD, and what it cannot answer. The qualitative walk over its shapes (mismatched lines, bulges, disappearing bands, flat lines, stair steps, S-curves, a bottleneck) is [[reading-a-cfd]].

## The six properties

> CFD Property #1: The top line of a Cumulative Flow Diagram _always_ represents the cumulative arrivals to a process. The bottom line on a CFD _always_ represents the cumulative departures from a process.
>
> — [[vacanti-actionable-agile-metrics]], L1236

> CFD Property #2: Due to its cumulative nature, no line on a CFD can ever decrease (go down).
>
> — [[vacanti-actionable-agile-metrics]], L1404

The other four concern what can be read from a chart:

- **Property #3.** The vertical distance between any two lines is the work in progress between the two workflow steps those lines represent (L1544).
- **Property #4.** The horizontal distance between any two lines is the Approximate Average Cycle Time for items that finished between those steps (L1584).
- **Property #5.** The chart shows only what has happened. "The data displayed on a CFD depicts only what _has_ happened for a given process. Any chart that shows any type of projection is not a CFD." (L1636)
- **Property #6.** The slope of any line between two reporting intervals is the exact Average Arrival Rate of the state in the succeeding band (L1668). Vacanti's corollary is that the same slope is also the exact average Throughput of the preceding step (L1670).

Vacanti means these strictly: "When I say “always” I mean “always”." (L1242). The properties are a definition as well as a description:

> A CFD is only a CFD if it obeys all six properties because only by following all of these properties can you be guaranteed to derive the correct quantitative metrics of flow off of your graph.
>
> — [[vacanti-actionable-agile-metrics]], L1758

## Anatomy

| Part | Meaning |
|---|---|
| X-axis | "some representation of a progression of time (usually calendar time)" (L1194) |
| Y-axis | "a cumulative count of items in the process" (L1206) |
| Band | "each different colored section on the graph" (L1218); one per workflow step (L1212) |
| Line | "the demarcation boundary of any band" (L1218); a band's bottom line is the next band's top line (L1218) |
| Top line of the CFD | The top line of the top-most band (L1226) |
| Bottom line of the CFD | "the top line of the bottom-most band" (L1226), not the X-axis |

Each intermediate band's top and bottom lines are that state's arrivals and departures (L1242).

## What is free and what is not

The author of the chart chooses the tick labels, the scale, and the reporting interval, which is the "frequency that you choose to add data to your chart" (L1202). Labels and interval need not match: the book's example reports daily and labels monthly (L1202). Interval and scale both change the picture (L1202, L1206), and Vacanti treats that as a tool for sharpening it.

This wiki reads that as a limit on comparison: two CFDs with different intervals or scales cannot be compared by shape, so a reading of a chart states its interval.

The outer lines are chosen once. "[T]he definition of the boundaries of your process is essentially up to you" (L1242), and once chosen they are the top and bottom lines. This wiki reads those boundaries as the project's [[started-and-finished-points]], so a CFD has the same dependency on those points as every other metric.

## How many bands

Two bands, arrivals and departures only, are "a perfectly valid CFD" (L1262). Bands for the steps between are "very advantageous and strongly recommended—but by no means necessary" (L1242). The source poses the trade-off as a question and does not settle it (L1262).

Vacanti also prefers showing "the queuing states or “Done” columns" (L1278) over showing each step as one layer, because "[a] widening of these layers could hint at something going wrong in our process" (L1278). A takeaway of his Chapter 5 repeats the advice: "Consider building CFDs that show both “Active” and “Done” states within workflow steps" (L1760). That is one more reason to separate [[active-versus-queued]] states on the board, and [[reading-a-cfd]] says what a thick queue band raises.

This wiki's rule for the choice, which is not the source's:

| Input | Read from |
|---|---|
| Which states the board distinguishes | Board columns and history |
| The question being asked | The person asking |

Use two bands for "are we taking in more than we finish". Use a band per state, with queues separate, for "where does work wait". The choice was too coarse if the total widens and no band says where. A chart cannot show a state the board does not record.

## Building it: entry dates, not counts

A CFD is derived from the date each item entered each step, and not from counting what sits in each column at intervals. The usual advice is to count the items in each step at regular intervals and plot the counts. Vacanti calls this "building a chart based on counts" and says that "building a chart just by counting items in progress is, in a word, dubious." (L1288). The rule he gives instead: "what we really need to do is track the date that a particular item enters each step of our work flow." (L1418).

This reads oddly against his own anatomy, which says that at each interval we "calculate the total number of items at each step" (L1206). This wiki reads the two as fitting together: the plotted value is a cumulative count, and his objection is to obtaining it by counting what is in progress at that moment.

### Why counts fail

A count cannot represent an item that went somewhere other than forward. His example: reporting hourly, four customers arrive at 9:59 and leave at 10:01 for a non-standard reason, the arrival count is decremented, and the arrival line falls (L1354). That produces "a negative arrival rate", which "violates the whole principle of a _Cumulative_ Flow Diagram" (L1370), and which cannot exist, because "[a]rrivals are binary: either something has arrived or it has not." (L1370).

> This is where building a CFD based on counts breaks down and why it is very difficult—and not at all recommended— to build a CFD just by counting items.
>
> — [[vacanti-actionable-agile-metrics]], L1372-L1378

### When counts are enough

Counts work only if both conditions hold (L1434-L1438):

1. "You never have items that move backward in your workflow"
2. "You never have items that are just completely removed from your process before they are completed"

Vacanti reports at least one of these in every process he has been part of (L1440). The second can be repaired on its own by counting every exit in Done (L1442); see [[non-standard-departure]]. The source says backward moves cause falling lines "if not accounted for properly" (L1450). This wiki reads that as meaning the first cannot be repaired while the chart is built from counts.

### The second reason

Even where counts would draw a correct chart, they stop there. With dates "we also get all the data we need to build an array of other very useful charts" (L1430), and Cycle Time needs them regardless (L1452). The reasoning is short: "So since you can create a CFD from dates, why not just use those?" (L1452).

### How the choice is applied

| Input | Read from |
|---|---|
| Each item's date of entry into each state | Board history |
| Whether any item moved backward or left unfinished | Board history |

This wiki reads the derivation as follows; the source calls it "rather straight forward" (L1424) and does not give it. A line for a state, at a date, counts the items whose entry into that state or any later state is on or before that date. Counting later states as well keeps an item that jumped straight to Done from pushing one line beneath another.

Built this way a line cannot fall, because adding dates only raises a count. This wiki reads that as the real reason dates work: a correction changes the record and redraws the past, instead of subtracting from today.

**Sign of violation:** the chart's data is a table of column sizes per date, with no per-item dates behind it; or a line falls (see the signs below).

**What would show the choice wrong:** a line falls on a chart believed to be date-built, which means the derivation or the data is at fault.

### Cost

The book's data holds one date per item per step. This wiki reads that as a real loss: a second visit to a state has nowhere to go, so the first visit's date is either kept or erased. That is the concrete form of the data problem [[backward-movement]] leaves unspelled, and a reason to draw expected cycles as forward states.

Collecting the dates costs nothing in this setting. They come from board history, in line with the charter's position that the time a task lived is read and not logged. Nobody has to keep them, which removes the human-discipline dependency a manual date table would have.

## Reading numbers off it

Reading flow metrics off a CFD is a three-part procedure against one chart: subtract vertically for WIP, subtract horizontally for Approximate Average Cycle Time, and take a slope for average Throughput or arrival rate. Each reading applies between the top and bottom lines for the whole process, or between any two lines for part of it (L1540, L1622, L1684).

| Question | Where it is read | What the number is |
|---|---|---|
| How much work is in progress at this date, overall or in a step? | Vertical distance | Total WIP between the two lines |
| How long did items finishing on this date take, on average? | Horizontal distance, drawn backward | Approximate average only; see below |
| How fast did work leave, or arrive, over this range? | Slope of a line | Exact average; see [[throughput]] |

Vacanti claims "both quantitative and qualitative insight into problems—or potential problems—in our process" (L1174).

### Inputs

- A chart that obeys all six properties; check this first, because the guarantee depends on it (L1720). See the signs below.
- The date, or date range, in question.
- The reporting interval. The steps are the same whether the interval is days, weeks or months (L1592-L1598).

### WIP: vertical distance

1. Take the date of interest.
2. Read the y-value of the upper line and the lower line at that date.
3. Subtract.

In the book's example, September 1 shows 290 on the top line and 200 on the bottom line, so total WIP is 90 work items (L1558). WIP in one step is the same subtraction across that step's band (L1570). The two lines may be any two: Vacanti's examples include Analysis Active, Development Done, and the span from Analysis Done to Test (L1540).

### Approximate Average Cycle Time: horizontal distance

1. Start at the date of interest on the bottom line.
2. Draw a horizontal line backward until it meets the top line.
3. Read the date at that intersection.
4. Subtract it from the bottom-line date.
5. Add one time unit.

For September 1 the line meets the top line at August 9; the subtraction gives 23 days and the added unit gives 24 (L1600-L1608). The reason for step 5 is on [[cycle-time]].

The same reading works through one step or between any two lines (L1622). The direction is fixed, from the later line backward. The calculation "is only valid for items that have finished", and a line drawn forward may never meet its target (L1632).

### Average Throughput and arrival rate: slope

1. Choose the date range. The number of time units in it is the run.
2. Read the bottom line at both ends. The difference is the rise.
3. Divide rise by run.

From June 21 to November 16 the run is 148 days. The bottom line goes from 0 to 517, so the rise is 517, and average Throughput is 517 / 148 = 3.49 items per day (L1682). Substituting the top line gives the average arrival rate, and any other line gives the rate for that step (L1682-L1684). See [[throughput]].

### Balance of arrivals and departures

"One of the best ways to visualize whether arrivals and departures are balanced is to visualize them via a CFD." (L2206) It replaces the plain comparison of averages in [[throughput]], which the source treats as the weaker method (L2074). The arrival rate is the slope of the top line of the topmost layer, and the departure rate, or Throughput, the slope of the top line of the bottommost band (L2094). Each layer corresponds to one board step (L2094). The arrivals column appears on the chart; a backlog does not (L2028).

The comparison can be made two ways. **Quantitatively,** by calculating the slopes: the source's example board gives 3.72 items per day arriving and 2.74 departing, so items arrive faster than they leave by about one item a day (L2094). Those figures belong to that illustrative chart and are not a benchmark. **Qualitatively,** with no calculation: "we can quite quickly do a qualitative assessment of the health of our system." (L2096) What the diverging and parallel shapes mean is on [[reading-a-cfd]].

### Report each number with its label

| Metric | Reading | Label it as | Applies to |
|---|---|---|---|
| WIP | Vertical | Total between two named lines | One reporting interval |
| Cycle Time | Horizontal, backward, plus one | Approximate average | Items finished at that date |
| Throughput, arrival rate | Slope | Exact average | The stated range |

The labels come from the source's insistence that only the slope is exact and the horizontal is not (L1646, L1656). This wiki adds that dropping them turns a sound reading into a false claim.

### Failure signs of a reading

This list is this wiki's own, drawn from the limits above. Each sign says what to check.

- A Cycle Time read off a chart with no "approximate": check whether the horizontal reading was taken as exact (next section).
- A Cycle Time reported for a date with no finished items, or for work still open: check whether the horizontal line was drawn forward or the number came from elsewhere.
- A Throughput figure with no date range: the average cannot be checked, and a different range can give a different figure.
- Two Cycle Time figures compared across reports: check that both counted the added unit the same way.

### Transfer to this plugin

The book describes reading by eye from a drawn chart. This wiki's reading is that a plugin holding board history can compute the same quantities from the cumulative series, and has item dates besides. The labels still apply to anything derived the chart's way, since the horizontal reading stays approximate however precisely it is computed.

## Approximate Average Cycle Time

**Approximate Average Cycle Time** is what the horizontal distance between two lines gives: an estimate of how long, on average, items that finished at a chosen date took between the two workflow steps (L1574, L1584). Vacanti is emphatic that each word of the name matters, because "there is a lot of misinformation or disinformation about CFDs out there" (L1646). The measure it approximates is [[cycle-time]].

### Three numbers that get confused

| Number | Where it comes from | Readable from the chart alone? |
|---|---|---|
| Cycle Time of an item | That item's own dates | No |
| Exact average Cycle Time | The item data behind the chart | Not without the data, or an understanding of the policies that generated the diagram |
| Approximate Average Cycle Time | Horizontal distance on the CFD | Yes |

### Why it is only approximate

- **Not an exact Cycle Time.** On the claim that the horizontal line gives one, the source says "It does not", because "the items that start on the top line of your Cumulative Flow Diagram (at the beginning of your horizontal line) are not necessarily the items that finish at the bottom line of your Cumulative Flow Diagram (at the end of your horizontal line)" (L1646).
- **Not necessarily an exact average either.** Unless we look at the data, or understand the policies behind the diagram, "the best we can say is that this horizontal calculation will lead to an Approximate Average Cycle Time" (L1646).

Vacanti finds the result remarkable for two reasons: subtracting two dates yields an average at all, and it does so even though the items at the two ends differ (L1618-L1620).

### What its quality depends on

The approximation "can be very good" (L1646), and how good is conditional:

> Interestingly enough, how good an approximation this calculation is will depend on how well we are adhering to the assumptions that make Little’s Law work.
>
> — [[vacanti-actionable-agile-metrics]], L1620

This wiki reads that as saying a reader should check the assumptions before trusting the figure. They are on [[littles-law]]. The book also promises policies that make the approximation excellent, and does not give them at this point (L1646).

### Limit: finished items only

The calculation "is only valid for items that have finished", and the line must be drawn backward (L1632). This wiki reads that as excluding work still open, whose age needs [[work-item-age]] instead.

### Failure mode: the horizontal line read as exact

Vacanti lists "A horizontal line represents an exact Cycle Time or an exact average Cycle Time" among common myths (L1766). The source names it "Approximate Average Cycle Time" in its Chapter 7 as well (L2108).

- **What breaks:** a figure that describes no particular item gets used as though it did, for example as the time a specific item took or as what the next item will take. The second use also conflicts with Property #5, since the chart says nothing about the future.
- **Observable sign:** a report giving a CFD-read Cycle Time without "approximate", attaching it to named items, or calling it the average with no source data behind it.
- **What to check:** compute the exact average from item dates and compare.

The sign and the check are this wiki's derivation from the source's argument.

### The gap is itself information

Vacanti calls this potentially the most important reason to keep the distinction:

> It turns out the comparison of the Approximate Average Cycle Time off of your CFD with the exact average Cycle Time from your real data can give you tremendous insight as to the health of your process.
>
> — [[vacanti-actionable-agile-metrics]], L1652

The specifics of that analysis are deferred to his Chapter 9 (L1652). Chapter 9's comparison, with its rough 10%/50% guide (L2536), is on [[flow-debt]]; nothing in Chapter 5 itself says what a given gap means.

### Trade-off

The reading is cheap, needing one chart and two dates. The cost is that it gives a single approximate average with no spread. This wiki's reading is that a plugin with board history should treat the exact average as the primary figure and the chart reading as the comparison, because item dates are available to it.

## Signs that a chart is not a CFD

A malformed CFD is a chart presented as a CFD that breaks the definition. Vacanti's concern is practical: "an improperly constructed CFD can lead to improper conclusions about process problems", and worse, "improperly constructed CFDs can lead to team or management apathy amid claims that the charts are just not very useful." (L1176). The defect lies in how arrivals and departures are counted, and any reading taken from such a chart is void: "Not accounting for arrivals and departures properly invalidates any resultant analysis of your chart." (L3890). Numbers read from such a chart lose the guarantee (L1758).

Vacanti's checklist has three signs (L1526-L1532). The fourth comes from Property #1 in the body of his Chapter 4. Chapter 16 adds two tests for a chart a tool generated, set out below.

| Sign on the chart | Source | What to check |
|---|---|---|
| A line falls: "If any line on the chart slopes downward on any part of the graph." | L1528 | Whether the chart was built from counts, or a count was decremented (see building, above) |
| A backlog is plotted: "If something that sounds like a “backlog” has been graphed (remember, a visualized backlog may not necessarily be bad—but it usually is!)." | L1530 | Whether backlog items are committed. See [[backlog-versus-commitment]] |
| A projection is plotted: "If some type of projection has been plotted." | L1532 | Whether the viewer is meant to read the future off a chart of the past |
| An outer line is something else: "Any chart that contains additional outside lines that do not represent process arrivals and departures is not a CFD." | L1242 | What the extra line is, such as a target or a scope line |

A falling line is the strongest of these. "You can immediately spot that a CFD has not been constructed properly if you see lines on the chart that go down." (L1406). A proper one has lines that are "either increasing (going up) or are flat" (L1406). Chapter 16 calls it the "telltale sign" (L3884), and this wiki notes that it is close to a proof, unlike most signs on a board: a cumulative count cannot fall.

The backlog sign is softer by the checklist's own wording: it allows that a graphed backlog may be fine. As everywhere here, a sign raises a question and is not a verdict; see [[smell-is-not-a-finding]].

This wiki adds one sign that belongs to the reader and not to the chart: a number read off the chart and labelled an exact Cycle Time. The chart may be sound, but the reading is wrong (see Approximate Average Cycle Time, above).

### Two tests for a tool's chart

**A line falls once later steps are hidden.** A chart with no falling line can still fail. The test is to "try to “turn off” some of the latter workflow steps (if you can) starting from the bottom up. Do you see any of the remaining lines go down now? If so, it is a safe bet that the overall CFD has not been built according to all of the required CFD principles" (L3892).

This wiki reads the mechanism as follows: a correct chart plots, for each step, how many items have reached it so far, so hiding a later step leaves the other lines unchanged. A line that falls only when later steps are hidden suggests that the tool counts items sitting in a state at that moment and stacks those counts. The test requires a tool that can hide steps, so being unable to run it proves nothing.

**A backlog whose time is not counted.** Chapter 16 softens the ban: "Strictly speaking, there is nothing wrong with displaying a backlog on a CFD" (L3894). The source is firmer elsewhere: "For the most part, any diagram that shows a backlog is not a CFD" (L1464), and "CFDs should not have backlogs on them. That is mistake number one." (L3590). It allows a backlog band only if its items count as committed: "If you do want communicate that backlog items have been committed to, then, by all means, display the backlog" (L1482). The issue is what the chart's lines then mean:

> CFD Property #1: The top line of a Cumulative Flow Diagram _always_ represents the cumulative arrivals to a process. The bottom line on a CFD _always_ represents the cumulative departures from a process.
>
> — [[vacanti-actionable-agile-metrics]], L3904

So approximate average Cycle Time runs from the top line to the bottom line, and if the chart "includes a backlog and your tool’s computed Cycle Time does not include the time spent in the backlog" the source says to be skeptical of the calculation (L3906). It also asks whether the tool calls its figure approximate at all, or would "lead you to believe it is an exact Cycle Time" (L3894-L3900).

This wiki's resolution follows L1482, through [[started-and-finished-points]] and [[backlog-versus-commitment]]: if the backlog is inside the arrival point, its items are committed and its time counts as Cycle Time; if it is outside, it does not belong on the chart. A chart that draws it and excludes its time is using two definitions of arrival at once.

### What to do on a sign

Derive the same chart from per-state dates, as [[capturing-flow-data]] sets out for verifying a tool. A falling line needs no further evidence. This wiki reads the other signs as questions to check, because a wrong result may come from the tool or from how the board was used; the same page covers both.

### The check runs one way

This wiki adds a limit the source does not state. No falling line does not prove correct construction. A count-based chart looks clean over any stretch in which nothing moved back or left, so it passes until the first such event, and a chart can pass every sign here and still sit on the wrong boundaries. Absence of the signs clears the chart of these defects and nothing more.

A second limit: a chart passing every test can still fail to show a process problem, since a violated assumption "will not clearly reveal itself on a CFD" many times (L1284).

### What breaks when ignored

The source names the conclusions and the apathy (L1176) but gives no case. This wiki reads the likeliest concrete error from Property #2: a falling line makes arrivals or finished work seem to shrink, so a reader sees flow that recovered, or a process that took in less, when items were only re-labelled or removed.

These are tests of a chart and depend on no executor. This wiki reads them as usable on a chart a tracker supplies, without knowing how the chart was computed, which is their value to a review of someone else's board.

## Which question it cannot ask

A CFD raises questions about flow, and several questions people bring to it are ones it cannot settle.

- **What will happen.** "[I]f you would like to do projections on a graph, then what you want is a something other than a CFD." (L1484). A horizontal line drawn forward "could cause you to never intersect the top line of the bottom-most band" (L1632). Vacanti does not dismiss forecasting. He says projections need "a completely different chart—and more probably a completely different approach (like Monte Carlo Simulation)" (L1638-L1644). See [[throughput-monte-carlo]] and [[which-chart-for-which-plan-question]].
- **How long any particular item took, or the exact average.** The items entering at one end of the line are not necessarily the items leaving at the other (L1646).
- **How long unfinished work has been open.** The Cycle Time calculation "is only valid for items that have finished" (L1632). This wiki reads that as meaning the age of open work has to come from item-level data and not from the chart. See [[work-item-age]]. This wiki also notes that the chart shows averages and bands, not any single item, so it cannot say which items are aging or whether started items finish, which the source raises as a separate violation (L2196).
- **What a shape means, without context.** Vacanti lists as a myth that "It is possible to make a qualitative assessment of a CFD without understanding its context" (L1770).
- **Every broken assumption of [[littles-law]].** "[M]any times an assumption violation will not clearly reveal itself on a CFD." (L1284). Vacanti's remedy is to know the assumptions and "map them to the context in which the data was collected" (L1284). This wiki concludes that a clean chart is not a clean process.
- **What left, or how.** The turnstiles of his shop example "would not track how long each individual spent in the shop, nor would they be able to tell us if a departing individual made a purchase or not" (L1314). This wiki reads that as a general limit: a departure means an item crossed the finish boundary, and says nothing about the result. Tasks that deliver nothing raise the bottom line as well as tasks that deliver, which is the illusion noted on [[flow-metrics]].

### Exact cause and exact fix

"Just like any visualization, a CFD is not going to tell you exactly what is wrong with your process or exactly how to fix it, but it is going to shine a light or a magnifying glass on the places to investigate." (L1776) Vacanti adds: "CFDs are not going to do our jobs for us. They do not replace thinking." (L1778)

The conclusion of his Chapter 6 says a CFD "will also suggest the right actions to take for increased predictability" (L1954). This wiki reconciles the two passages by reading the later one as direction, and takes the first as the limit on what a finding may state.

### Where the bottleneck is

Vacanti leaves bottlenecks out on purpose, and dissents from the usual claim about CFDs: "I believe that the best you can do by just looking at a CFD is to pose some questions about some variability that may be occurring. It is impossible to spot a systemic bottleneck." (L1944) He prefers "Deming's and Shewhart's language of variability to that of Goldratt's language of the Theory of Constraints" (L1944), and defers the argument to his Chapter 13.

This wiki treats that as a rule for wording: a finding from a CFD's shape alone says a step shows variability worth checking, and does not name a step as the bottleneck. The sign of a violation is a finding that says "bottleneck" and rests on the chart's shape alone. A bulge in one step is the closest temptation, and its cause may lie elsewhere. The book's Siemens case credits the CFD with showing where capacity was short (L4192); [[reading-a-cfd]] sets out how this wiki reconciles the two passages.

### Whether the process is healthy

"it is possible to get a very pretty CFD picture but still have a very dysfunctional process underneath" (L1938). Vacanti's best example is the accumulation of [[flow-debt]] (L1938), which he treats in his Chapter 9. Chapter 7 says the same of balanced lines: "[H]aving a pretty CFD is not a guarantee of a healthy system, but it is certainly a pretty decent start." (L2148), and its takeaway is flat: "Pretty CFD pictures could still mask underlying process problems." (L2212). This wiki reads that as saying a balanced chart is necessary and not sufficient, and that a clean chart removes the shape-based questions without clearing the board. This wiki's sign of misreading it is a report that cites balance with no look at item ages or abandoned work.

If a chart truly does look good, Vacanti moves to improvement (L1936):

- Can the lines get closer together by reducing WIP and so improving Cycle Time?
- Can the Throughput line get steeper?

### Forecasts beyond its assumptions

The predictive power of a CFD "depends almost entirely on how well your process obeys the assumptions behind Little's Law" (L1964-L1970). This wiki reads that as a precondition on any figure taken from the chart: when mismatched arrivals and departures or a long flat stretch are present ([[reading-a-cfd]]), the assumptions are in question, and so is the figure. See [[littles-law]] and [[forecast-range-and-probability]].

## Segmenting

Flow data can be viewed whole or as a CFD of one or more subtypes: only user stories, only defects, or stories and maintenance combined (L1712-L1718). Vacanti also names filtering by release and by a custom field relevant to the context, and challenges the reader to think about which attributes to collect and filter on (L1718).

Filtering across teams or at portfolio level (L1718) belongs to another scale and does not apply to a few people steering an agent. This wiki's reading is that filtering by type or release does carry over, provided the attribute is present on the task, since it cannot be recovered from the chart afterwards.

## Myths the book lists

The takeaways of Vacanti's Chapter 5 name four common myths (L1762-L1770).

| Myth | Where it is handled |
|---|---|
| It is always correct to build a CFD from work item count data at each reporting interval | Building it, above |
| A horizontal line represents an exact Cycle Time or an exact average Cycle Time | Approximate Average Cycle Time, above |
| It is always ok to represent a traditional backlog on a CFD | Signs, above, and [[backlog-versus-commitment]] |
| It is possible to make a qualitative assessment of a CFD without understanding its context | [[reading-a-cfd]] |

## Positions

**Vacanti:** the principles "apply regardless of the particular methodology that has been chosen" (L1254), and a board as simple as To Do, Doing, Done qualifies (L1248). Projections are excluded from the chart.

**Scrum Guide:** lists "cumulative flows" among practices "to forecast progress" ([[scrum-guide-2020]] L202).

**Which holds:** this wiki resolves the disagreement by tense. Under any setup the chart itself records what happened, and a forecast is made elsewhere from the same dates. The resolution is ours.

## Scale and agent executor note

The properties and the anatomy are arithmetic over state changes, so they survive an agent executing and hold at any team size. Vacanti's claims about the chart's value come from his experience with human teams, with no measurement behind them.

His running example covers 517 departures over 148 days, about 3.49 items per day, with 90 items in progress on one date (L1558, L1682). That is much larger than a board kept by a few people. A sparse board gives a stepped line, and this wiki's reading is that a horizontal reading from it is coarser than the example suggests. Whether a CFD says much on a board moving a few items a week is untested here.
