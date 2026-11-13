---
title: Starting More Work
category: moving-work
summary: One mechanism behind several failures — starting more items while started ones are unfinished raises WIP, and work behind the queue waits longer. It shows by trigger, as starting more when Cycle Time is long, starting the next item when one is blocked, adding hours or capacity to an over-started system, a buildup of stuck work, expediting past the queue, and defects hidden in unfinished work. The first lever is to lower WIP; the law fixes a relation and not a direction, so the rule is a strong default with a stated falsifier, not a theorem.
tags: [failure-mode, wip, cycle-time, pull, board-rules, decision-rule, throughput, littles-law, capacity, blocked, queues, flow, board-health, quality, batch-size, flow-metrics, signs]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Starting More Work

Starting more work while started work is unfinished raises [[work-in-progress]], and on average every item then takes longer. Vacanti's general statement is that, on average, the more things worked on at once, the longer each takes to finish ([[vacanti-actionable-agile-metrics]] L906). Cohn states the same queue: "The more work in process there is, the longer any new feature will take to develop as the new feature must follow along behind the already started work." ([[cohn-agile-estimating-planning]] L4879).

The sources describe one mechanism reached by different triggers. This page holds it once and then each trigger with its sign. The preventive rule, a bound on WIP, is on [[wip-control]]; the arithmetic is [[littles-law]].

## How firm the mechanism is

This wiki qualifies the source here. Vacanti calls the link "simple, incontrovertible mathematical fact" ([[vacanti-actionable-agile-metrics]] L916), but what the law guarantees is narrower. In his forecasting section he says: "All Little’s Law will say is that an increase in average WIP will result in a change to one or both of average Cycle Time and average Throughput" (L1086). This wiki reads the two passages together as follows: the mathematics fixes the relation, not a direction, while the direction of the advice is a claim that Throughput will not fall as far as WIP does. That is a strong default for a process limited by concurrency, not a theorem.

He also names a case where lowering a limit does nothing: changing a WIP limit may leave total average WIP unchanged, for example after "a clear systemic bottleneck" (L1046). See [[work-in-progress]].

The relation is the arithmetic of average WIP, Throughput and Cycle Time, so it holds at any team size, within the assumptions of [[littles-law]].

## Trigger 1: Cycle Time is long, so start more

The response to long [[cycle-time]] of starting additional items sooner, which raises WIP and lengthens the very thing it was meant to shorten. Vacanti calls it "the exact opposite intervention of what they should do: they start more work" ([[vacanti-actionable-agile-metrics]] L906).

**Mechanism.** The reasoning Vacanti attributes to such managers: items take so long that new ones must start as soon as possible in order to finish on time, regardless of what is already in progress. Items then take longer still, so the pressure to start sooner grows, and the cycle feeds itself (L906).

**Sign.** This wiki's reading of where it shows in board history: over consecutive windows, the open-item count and Cycle Time rise together, and new starts continue while existing items are ageing or blocked. As with any sign here, it raises a question ([[smell-is-not-a-finding]]). It is not a verdict.

**The rule.** "[I]f Cycle Times are too long then the first thing you should consider is lowering WIP" (L906). Vacanti concedes that this "feels uncomfortable" (L906).

- **Inputs:** average WIP and average Cycle Time across recent windows, and starts against finishes. All are read from board history.
- **What would show it wrong:** WIP fell, and Cycle Time did not improve or Throughput dropped in proportion.

**Trade-off.** Lowering WIP means saying no to starting something now, so requests wait longer before entry even as items move faster once started. This wiki notes that lowering WIP moves waiting out of the process; it does not remove demand.

## Trigger 2: an item is blocked, so start the next

The habit of answering a stalled item by opening another. It feels productive and it keeps a points chart moving, but it adds to WIP while the stalled item stays unfinished.

At Siemens HS ([[vacanti-actionable-agile-metrics]]), two habits fed it. One was a hedge: "It had been common practice to start multiple features at one time to mitigate possible risks." (L4026). The other was the reaction to a block:

> whenever a story or feature was blocked (for a variety of reasons such as waiting for a dependency from another team, waiting for customer validation, inability to test because of environmental or build break issues, etc.), teams would simply start the next story or feature so that we could claim the points which we had committed to achieve.
>
> — [[vacanti-actionable-agile-metrics]], L4026

This wiki reads the hedge as self-defeating on the source's own arithmetic: when arrivals outrun departures, each extra start raises average Cycle Time, the hedged items included ([[conservation-of-flow]]).

**Signs.** These are this wiki's reading of the passage above.

- In board history, an item enters a blocked state and a new item starts with no finish in between.
- Blocked count and in-progress count rise together.
- Items stay blocked for a long time while the team's points look normal; see [[velocity-masks-unfinished-work]].

These raise a question. A new start can be legitimate if the limit allows it and the blocked item truly cannot be helped.

**What stops it.** The source's remedy is a pull system with WIP limits and not a stated rule about blocks: Siemens "instituted a policy of limiting WIP across all teams" (L4120). This wiki links that to [[blocked-work-counts-against-wip]]: only if a blocked item still occupies a slot does the limit stop the reflex. A limit that excludes blocked items gives no pressure to clear the block.

**Trade-off.** Holding to the limit means capacity can sit unused while a block persists. The chapter does not price this, and it does not say how long a team should wait. This wiki's reading is that the case supports the direction and not a threshold.

## Trigger 3: Cycle Time is long, so add hours or capacity

When Cycle Times are too long, a simplified reading of [[littles-law]] leaves two levers open: decrease WIP, or increase Throughput. The source's position, in the Siemens case ([[vacanti-actionable-agile-metrics]]), is that the first comes first.

> The problem with trying to impact Throughput in these ways is that most organizations actually end up increasing WIP faster than they increase Throughput.
>
> — [[vacanti-actionable-agile-metrics]], L4090

The levers it means are longer hours, mandatory weekends, borrowed staff and hiring (L4090). The source calls cutting WIP the "much more sensible and economical" choice (L4092). Siemens' managers reached the same view from the other direction: the overtime "may actually have been elongating the release completion date" (L4034). Overtime as a people practice is out of scope here, and only its flow effect is kept.

**The rule.** When Cycle Time is too long or rising, check whether work is entering faster than it leaves. If it is, stop starting work and hold a limit. Do not add capacity to a system that is already over-started.

**Inputs and where they are read.**

- Cycle Time percentiles and their trend, from board history; see [[cycle-time-scatterplot]].
- Arrival and departure rates, from the two boundary lines of a [[cumulative-flow-diagram]] or from counts of starts and finishes in history; see [[throughput]].
- Current open item count, from board state.

**What would show the choice wrong.** The limit is held, arrivals match departures, and Cycle Time keeps growing or Throughput falls sharply. Then this wiki reads the constraint as sitting elsewhere: read the persistent queue band on [[reading-a-cfd]] and the items themselves. Siemens' result was stabilization after limits; the chapter does not show a case where limits failed, so it offers no counter-example.

**Reasoning.** If WIP rises faster than Throughput, average Cycle Time rises (L4090). This wiki reads the practical step as follows: adding a person or a resource often adds new starts first and output later.

This does not mean capacity never matters. Once flow was stable, Siemens did add capacity, and in a specific place: test automation, where the chart showed the shortfall (L4192), and a Tester instead of two Programmers in a what-if (L4224). This wiki reads the order as the rule: limit first, then add capacity only at the constraint the charts expose.

**Trade-offs.** Stopping starts means visibly unstarted requests and people or agents with nothing new to do. It also goes against habit: at Siemens "mandating limits on work went against the grain of the then current beliefs" (L4100). See [[filling-a-period]].

## The result: a buildup of stuck work

A queue is a buildup of started work that is not finishing. Vacanti treats it as the main sign that flow, which he defines as "the movement and delivery of customer value through a process" (L412), has gone wrong: "A telltale sign of a suboptimal flow is a large buildup of work somewhere in your process." and "Large queues generally mean no flow." (L414).

**Signs.** The source gives the shape and leaves the reading to the reader. The signs below are this wiki's derivation.

- **On the board:** many items between the started and finished points, with ages growing and few finishing.
- **On the board:** one state holding far more items than those after it, which is where the buildup sits.
- **In history:** starts exceed finishes over a span of weeks.

A pile-up that the project declared intended, or one that clears on a known cycle, is not this failure. The source's word "large" has no number, so this wiki reads the sign as a trend against the project's own history and not as a threshold.

**How work gets stuck.** The source says queues form "when work items that have been started just get stuck" (L416), and it lists four causes (L416-L422):

1. No resources are free to continue the item.
2. A manager mandates starting new work before current work has finished.
3. The people doing the work are pulled in several directions and cannot focus on one thing.
4. The item depends on "some external team or vendor".

The list is not exhaustive: "Work may get stuck for all of those reasons and more." (L424). Cause 4 is treated on [[waiting-versus-blocked]] and [[parking-lot]].

**Why it goes unseen.**

> Unfortunately, your project management framework makes you blind to queues. You are blind to them because you are never asked to look for them in the first place.
>
> — [[vacanti-actionable-agile-metrics]], L426

The author says what is felt instead is that "work takes too long to complete" (L428). This wiki reads that as the diagnostic trap: the complaint is about duration, so the response goes to duration, and the count of open work is never read. [[active-versus-queued]] covers the related case where a column hides waiting work.

**Responses that miss.**

> Traditional project management responses to elongated completion times might be to constantly refigure project plans, to continuously revisit resource assignments, and to force teams to work overtime. Not only do those actions not solve the core problem, but in most instances they tend to make things worse.
>
> — [[vacanti-actionable-agile-metrics]], L428

The source gives no measurement for "make things worse", so this wiki keeps the mechanism only: none of the three reduces what is open.

**What to do.** The source gives two moves in sequence. Once stuck work exists, "Management of flow, therefore, usually begins by attempting to “unstick” stuck work." (L424). The better move is earlier: "The best way to fix the problem of large queues is not to allow them to form in the first place." (L434). The preventive rule is on [[wip-control]]. The cost falls on requesters: new work waits while old work finishes (L234).

## Cohn's account: the queue, and expediting past it

Cohn defines the measure and the cause together. "On a software project, cycle time is the time from when the team begins work on a feature until it delivers value to users. The shorter the cycle time the better." ([[cohn-agile-estimating-planning]] L4873). Work in process "exists on any feature that the team has started developing but has not yet finished" (L4879).

> High amounts of work in process slow down a team. [...] The more work in process there is, the longer any new feature will take to develop as the new feature must follow along behind the already started work.
>
> — [[cohn-agile-estimating-planning]], L4879

This wiki reads the reasoning as a queue: capacity is occupied by what was started first, so what starts later waits. Cohn draws on queuing theory through Poppendieck and Reinertsen and gives no figures here (L4873). The other named influence on cycle time is variability ([[size-spread]]). Chapter 19 states the same effect as its leading reason against partial credit ([[all-or-nothing-counting]]).

**Expediting does not escape it.** The obvious way past the queue is to jump it. Cohn rules that out in a parenthesis: "(Or, the new feature needs to be expedited, jumping ahead of the work in process but that just compounds the problem for the next feature that cannot be expedited.)" (L4879). This wiki reads it as saying that an expedited item adds to work in process and leaves the queue as it was, so the delay moves to whatever comes next. [[interrupting-started-work]] covers the expediting decision, and [[expedite-lane]] the lane that makes it a policy.

**Signs.** These are this wiki's derivation, and each raises a question: tasks of very different size also finish out of order.

- **On the board:** many items started and few finishing, with ages growing.
- **In history:** tasks started later finish before tasks started earlier, repeatedly, which is what expediting looks like.
- **In history:** cycle time rises while the size of tasks stays the same.

**Reading the definition.** Cohn's end point is delivered value, which is later than a "done" column on many boards. This wiki notes that board history can give his cycle time only if a state marks delivery. [[started-and-finished-points]] and [[flow-metrics]] cover how the points are chosen. Time between done and delivered is invisible otherwise.

## A later cost: defects found late

Pushing work in large amounts lets faults sit undetected inside items that are not yet finished. The Siemens HS chapter contrasts this with a pull system.

> “pushing” a large batch of requirements and/or starting too many requirements will delay discovery of defects and other issues; as defects are hidden in incomplete requirements and code.
>
> — [[vacanti-actionable-agile-metrics]], L4170

The source credits managing queues, limiting WIP and batch size, and building a cadence through pull with the opposite effect: "we were able to expose more defects and execute more timely resolutions" (L4170). It also reports continued clean builds, stable testing environments and "the clearing of previously persistent testing bottlenecks" (L4192-L4198).

**Signs.** Each raises a question.

- The gap between defects created and defects resolved widens during a release; the source reports that gap narrowing under Kanban (L4170).
- Defects cluster late, near the end of the release. This sign is this wiki's reading of the mechanism.
- Low first pass yield, "the percentage of formal integration and regression tests passing the first time they are executed" (L4200).
- Testing is rushed at period end (L4026); see [[end-of-period-crunch]].

**Numbers and their conditions.** First pass yield went from 75% before Kanban to 86% and then 95% (L4200), in a regulated product with a dedicated test role in each team (L4002, L4014). The chapter does not isolate WIP as the cause. It states that "Along with the gains we achieved through managing WIP; we had placed significant focus on reinforcing and improving our CI and quality management practices." (L4262). This wiki therefore keeps the mechanism, late feedback on unfinished work, and treats the percentages as one confounded result; the charter grades a practitioner source on mechanisms for this reason.

**Trade-off.** This wiki reads the cost as more frequent integration and test runs, which Siemens could afford because CI and TDD were already in place (L4006-L4012). The source does not say how far the effect holds without them. See also [[hidden-wip-in-large-items]] and [[wip-per-executor]].

## Which setup this applies under

The mechanism holds under both setups. The source says iterations do not protect a project: "you might assume that iterations or sprints insulate you from large queues" (L426), and it says that assumption fails if the symptoms on [[signs-of-poor-flow]] are present. This wiki reads Cohn's iteration setup as clearing work in process at the period's end, provided unfinished work is returned ([[unfinished-at-period-end]]).

The resolution is this wiki's. Both can hold, because they concern different queues.

- **Iteration setup:** the period's end limits how long a queue lives only if unfinished work is actually returned and not rolled into the next period ([[unfinished-at-period-end]]). Inside the period a queue can still form, so read the count mid-period as well.
- **Flow setup:** no calendar clears anything, so the bound on [[wip-control]] is the only thing that limits the queue.

## Agent executor note

This wiki's reading, not the sources', unmeasured and stated once for every trigger above. The queue in Cohn's sentence, and in Vacanti's causes 1 and 3, is a team's capacity and attention; an agent can run in parallel and has no focus to lose, so at execution those do not survive. What survives is where the constraint sits:

- If a person's review is the constraint, launching another agent is the modern form of adding staff or starting the next item: it raises WIP at once and adds nothing to Throughput, and every rule above holds as stated. The queue forms at review, where finished runs wait for the few people steering.
- If execution is the constraint, parallel runs may raise Throughput for a while, and the failure appears only once review saturates. Long Cycle Time with results sitting unreviewed is then the same failure in a new place.

So the input to check first is where finished work is waiting. Causes 2 and 4 of the buildup survive unchanged: a person steering can launch one more run as easily as a manager can mandate a start, and outside dependencies do not change. The block trigger's motive in the source, claiming committed points, is human and does not survive; its structure does, when the person steering starts a second agent because the first is idle on a wait. The plugin's own test, that a started task can finish without waiting, treats a block inside a task as a possible bad cut; that test comes from the plugin's design, not from these sources ([[waiting-versus-blocked]], [[sequence-versus-wait]]). The late-defect mechanism rests on when verification happens and not on human memory, so it survives: several unfinished agent results waiting for one person's review are the same hidden stock. The sources' figures do not transfer in any case.
