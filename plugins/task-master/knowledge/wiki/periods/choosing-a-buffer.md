---
title: Choosing a Buffer
category: periods
summary: Buffer only where uncertainty or the cost of a wrong date is high and the plan has at least about ten items; match the unit to what is uncertain (time for a date, features for scope), combine them where both are firm. A schedule buffer moves local safety off 50% estimates into one visible line sized by the square root of summed squared 50-90 spreads (or half the 50% sum); a feature buffer adds 25-40% optional work built last (DSDM caps Must at 70%); a running plan that loses its margin names about one period's velocity of droppable stories. Padding is hidden, underived safety.
tags: [decision-rule, planning-a-date, buffer, uncertainty, setup-dependent, concept, estimation, human-executor-mechanism, what-an-estimate-promises, failure, method, numbers, scope, dsdm, moscow, rule, release-planning, priority, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Choosing a Buffer

Whether to buffer a plan, and with what, follows from two questions: what is firm, and what is it worth to be wrong. Cohn treats buffering as risk management: useful "In cases where there is significant uncertainty or the cost of being wrong is significant" ([[cohn-agile-estimating-planning]] L3843), and otherwise not worth doing.

## When to buffer

The source names these situations (L3821-L3829, L4061):

- planned far in advance
- a firm deadline with a reasonably firm set of functionality
- contracted from one organization to another
- requirements understood only superficially
- significant cost, financial or otherwise, of being wrong about a date

Each brings either more uncertainty or heavier consequences (L3831). Conversely, where "a precise deadline with a precise set of delivered functionality is not needed" and the team simply delivers as fast as it can over a sustained period, "don’t take on the small extra work of adding buffers to your project" (L4053).

## Which buffer: match the unit

The rule is "we buffer feature uncertainty with features and schedule uncertainty with time" (L4020). Cohn's shoulder belts and air bags make the point that different buffers cover different collisions (L4016). This wiki resolves the choice by project setup; the first three rows follow Figure 17.5 (L4022), and the setup column is ours.

| Setup | Buffer | Why |
|---|---|---|
| Scope fixed, date may move | None needed for the date, or a larger *Schedule Buffer* (below) if a date is promised anyway | Figure 17.5(a): delivers when the set is done |
| Date fixed, scope open | *Feature Buffer* (below) | Figure 17.5(b): the date holds, contents vary |
| Date and core scope both firm | Both, each smaller | Figure 17.5(c) |
| Neither precise, continuous delivery | None | The caveat at L4053 |

Combining is usually the better answer: "this is usually a good idea as it allows the size of each to be smaller" (L4067).

When one constraint cannot flex, the load moves. "When we cannot buffer a constraint appropriately, we are forced to increase the size of other buffers" (L4045). Guaranteed functionality means a larger schedule buffer. This wiki reads the mirror case as following: a date with no room means a larger feature buffer.

## Inputs and the fact that would show the choice wrong

- **Firmness of date and of scope:** from the person who owns them; a board does not show this, and it is the setup decision the plugin must ask about ([[fitting-stories-into-a-release]]). That a date is written down does not make it firm: see [[a-date-is-not-urgency]].
- **Size of the plan:** at least ten items for a formula-sized buffer (*Project Buffer Sizing* (below)). Below that, the source advises against buffering at all (L4010).
- **Uncertainty:** the spread between items' 50% and 90% estimates ([[completion-time-distribution]]).

This wiki reads these as the disproving facts. A buffer was unnecessary if the date slipped with no consequence, or if the same buffer goes untouched across several plans. It was the wrong kind if the date was met by dropping work that turned out to be mandatory, or if time ran out with optional items already built.

## Scale

The budget or personnel buffer the chapter also describes (L4031-L4035) is dropped from this wiki: Cohn himself says it is seen less on small projects, and "It is difficult to buffer anything in small numbers" (L4035). This wiki reads the ten-item floor as meaning that for a few people, buffers belong to a release-sized plan and not to a handful of tasks.

## Local Safety

Local safety is the protection attached to each individual task instead of to the plan as a whole: "The additional time between the 50% and the 90% estimate is called local safety" ([[cohn-agile-estimating-planning]] L3922). People add it to any estimate they want to be sure of meeting. It is a sensible move for one task and a costly one for a plan.

### Why it does not sum

Cohn's warning is that estimating every story at its 90% point to get a 90% schedule means "the project schedule will almost certainly be too long" (L3920). His airport trip (L3931-L3935) gives the size of the effect.

| Step | 50% estimate (min) | Local safety (min) |
|---|---|---|
| Find keys | 1 | 5 |
| Drive | 45 | 30 |
| Park | 10 | 5 |
| Check in | 7 | 30 |
| Security | 7 | 30 |
| **Total** | **70 (1:10)** | **170 with safety (2:50)** |

The 50% sum leaves no room for the slightest delay, and the 90% sum over-protects because "there’s very little chance that everything will go wrong" (L3935). The numbers are an illustration, not data.

The second reason is what is being protected. Only one date matters, and "Because it isn’t important if any one task on my way to airport finishes late, I do not need to buffer the on-time completion of the tasks" (L3937). The remedy in *Schedule Buffer* (below) takes local safety off the tasks and puts a fraction of it into one shared buffer (L3943).

### The behavioural argument, and whether it survives

Cohn adds that moving safety off tasks defeats two effects: [[parkinsons-law]], that work expands to fill the time available, and student syndrome, starting at the last moment that still allows success (L3954). His conclusion is that "a shorter schedule that includes a schedule buffer is more likely to be met than is a longer schedule" (L3954).

Both mechanisms depend on a human executor. This wiki reads them as not transferring directly: an agent has no reason to stretch work to fill an allowance or to delay its start. The aggregation argument above is statistical and stands regardless of who executes, within the assumption stated on *Project Buffer Sizing* (below). So for an agent the case for moving safety rests on the shorter plan alone, and the claim that a shorter plan is more likely to be met has no support here. The person steering may still show both effects when reviewing.

### Trade-off

Removing local safety means individual tasks overrun about half the time, on purpose. That is only workable if an overrun of a 50% figure is not treated as a fault. Cohn notes that people pad "if they expect to be beaten up if they are wrong" (L4041). This wiki reads that as the way local safety returns: chase task-level overruns and the estimates quietly drift back to 90%, and *Buffer Versus Padding* (below) then stacks a buffer on them.

### Sign

A plan whose date is the plain sum of task estimates, where those estimates were given as numbers someone felt safe with. This sign is this wiki's. The question to ask is which point on the [[completion-time-distribution]] the numbers name.

## Buffer Versus Padding

Padding and a buffer both add time, and only one of them is sound. Padding is "excess time arbitrarily added to an estimate" ([[cohn-agile-estimating-planning]] L4041): Cohn's case is thinking three days and saying five, just in case. By contrast, "A schedule buffer is a necessary margin of safety added to the sum of estimates from which local safety has been removed" (L4041).

### The test

This wiki puts the source's distinction as three questions; all three must pass for the extra to be a buffer.

| Question | Buffer | Padding |
|---|---|---|
| Where does it sit? | One line on the whole plan | Inside individual estimates |
| Where did the amount come from? | Derived from the spreads, *Project Buffer Sizing* (below) | A feeling, "just in case" |
| What are the estimates under it? | 50% figures | Already safe, 90% or thereabouts |

The last row is the costly one: "Adding a schedule buffer on top of already pessimistic, 90% estimates will result in an overly long schedule" (L4051). Cohn's caveat allows single-value estimates only if they "represent estimates at the 50% point" (L4051).

### Why padding appears

"Individuals add padding to an estimate if they expect to be beaten up if they are wrong" (L4041). This mechanism belongs to a human estimator. This wiki reads the transfer as follows: an agent has no fear of blame, but an agent or a person steering can still produce pessimistic numbers, by reasoning towards a safe answer or by being trained on what got punished. So the test applies to estimates from either, though the motive may not.

### Presenting a buffer

A buffer looks like padding to anyone who sees only the number: "a buffer (especially a schedule buffer) can appear to be padding" (L4055). The instruction is not to hide it: "You should not hide their existence or how they are used" (L4055). What must be shown is how the estimates and buffer were derived and that the result is a schedule everyone can hold "90–95%" confidence in (L4055).

Nor is a buffer idle time that can be reclaimed. Cohn's car-following analogy says "you fully expect to use up most of that buffer if forced to brake suddenly" (L4043). This wiki reads that as the reply to any proposal to trim a buffer because it looks unused at the start of a plan.

### Signs

These signs are this wiki's. Each raises a question to check.

- A plan with no buffer line but estimates that nobody will say are 50% figures, so the safety is hidden in them.
- A buffer line with no derivation from item spreads and no stated rule.
- In history, where estimates are in time or convert to it, nearly all items finishing at or under their estimate. This suggests they were not 50% figures; see [[completion-time-distribution]].

The opposite failure is cutting real *Local Safety* (above) from the estimates without adding any buffer back: that is the 1:10 airport plan, where "the slightest delay will cause me to miss my flight" (L3935).

### Trade-off

A visible buffer invites someone to negotiate it away, and hidden padding does not. Cohn accepts this cost by requiring disclosure. This wiki reads his reason as being that a padded plan cannot be read: nobody can tell how much protection it holds or where.

## Schedule Buffer

A schedule buffer is a block of time added once, at the end of a plan, to protect a date. "A buffer is a margin for error around an estimate" ([[cohn-agile-estimating-planning]] L3843); this kind is denominated in time and sits on the whole plan rather than on any task. It is the time-side counterpart of *Feature Buffer* (below), and the choice at the top of this page says when either applies.

### What it answers

A fixed date changes the question. Cohn's flight leaves regardless: "My expected arrival time and my rate of progress don’t matter to the airline" (L3871). Where the deadline does not move, reporting a forecast of arrival does not protect it. Only margin built in before starting does.

The plan protects "the only deadline that matters—the overall project deadline" (L3937). Whether any one activity runs long does not matter, only whether the chain does (L3873).

### Procedure

1. Give every item two estimates, 50% and 90%, before moving to the next item (L3956). Story points or ideal days both work (L3968). See [[completion-time-distribution]].
2. Sum the 50% estimates. This is the plan without *Local Safety* (above).
3. Size one project buffer from the spreads: *Project Buffer Sizing* (below).
4. Duration = sum of 50% estimates + buffer. Divide by forecast velocity to get iterations ([[velocity-range-forecast]]).
5. Show the buffer as its own line and say how it was derived: *Buffer Versus Padding* (above).

In Table 17.2's six stories, 17 + 9 = 26 points. At a velocity of 9 per iteration that is three iterations rather than two (L3974, L3992). Adding a buffer "may or may not add one or more iterations", and "Most often it will" (L3992).

### Inputs and the fact that would show the choice wrong

- **Two estimates per item:** from the task or the estimation step.
- **Forecast velocity:** from board history, or a forecast where there is none ([[choosing-velocity-estimate-approach]]).
- **The date's firmness:** from whoever owns the date; the board does not show it.

This wiki reads the following as the disproving facts, which the chapter does not list. The buffer is expected to be consumed: Cohn's car-length analogy says "you fully expect to use up most of that buffer" (L4043). A date missed with the buffer gone suggests the estimates or the spreads were too narrow. A buffer left largely unused across several plans suggests the 50% figures were really pessimistic ones.

### Trade-offs and failure modes

- **Cost:** a second estimate per item and usually a later stated date. Cohn calls this "small extra work" (L4053), and does not spend it where no date needs protecting.
- **Applied to safe estimates:** "Adding a schedule buffer on top of already pessimistic, 90% estimates will result in an overly long schedule" (L4051).
- **Task-level chasing:** treating a task's 50% figure as a due date undoes the method; see *Local Safety* (above).
- **Too few items:** see the guidelines in *Project Buffer Sizing* (below).

### Limits

The chapter buffers a release date. It says nothing about holding capacity back inside one iteration; filling a period, and the margin kept there, are on [[filling-a-period]]. Its summary (L4065) reads "feature buffer" and "a team’s size" in the sentences describing this method; the body of the chapter shows it means a schedule buffer and the size of the work.

The statistical case survives an agent executing, in this wiki's reading; the behavioural case does not transfer directly, as *Local Safety* (above) explains.

## Project Buffer Sizing

The size of a *Schedule Buffer* (above) comes from how far each item's 90% estimate sits above its 50% estimate. The spread is the measure of risk: "the numbers very clearly point out the degree of schedule risk associated with each item" ([[cohn-agile-estimating-planning]] L3962). Two stories both starting at 3 are not the same if one tops out at 5 and the other at 10.

### Square root of the sum of the squares

Buffer = √( (w₁−a₁)² + (w₂−a₂)² + … + (wₙ−aₙ)² ), where w is the 90% estimate and a the 50% estimate (L3966, L3968). In Cohn's words, "The schedule buffer is the square root of the sum of these squares" (L3968). The technique goes back to Reinertsen (1997), Newbold (1998) and Leach (2000) (L3970).

Table 17.2 (L3978-L3986):

| Story | 50% | 90% | (90%−50%)² |
|---|---|---|---|
| Authentication | 1 | 3 | 4 |
| Practice schedule | 3 | 5 | 4 |
| League pool locations | 5 | 8 | 9 |
| National records | 2 | 5 | 9 |
| Personal records | 5 | 13 | 64 |
| Meet results | 1 | 1 | 0 |
| **Total** | **17** | **35** | **90** |

The source gives √90 as 9.4 and rounds it to 9, so the plan is 17 + 9 = 26 (L3968, L3974). This wiki notes that √90 is closer to 9.5, which leaves the rounding unchanged. The widest item dominates and a certain item adds nothing (L3990). The printed text calls the widest item "the first story"; the table shows it is the personal-records row.

### The simpler calculation

With only one estimate per item, "Estimate each story at the 50% level and then set the buffer at half the size of the sum of the 50% estimates" (L4000). Its price is "the serious flaw of not being influenced by the actual uncertainty around the specific user stories in the project" (L4002): two 5-point stories add 2.5 each even if one could reach 100 and the other 10. Cohn prefers the formula, since asking for two estimates is easy (L4004). This wiki notes that the simple rule always yields a buffer of one third of total duration, whatever the risk.

The simple rule is only valid if the estimates really are 50% ones (L4051).

### Guidelines and their conditions

Both come from Leach (2000), via Cohn, as advice with no data given (L4008):

- The formula is most reliable from ten items up. Below that, "you probably shouldn’t be planning with a buffer anyway" (L4010).
- "The project buffer should represent at least 20% of the total project duration" (L4012).

This wiki notes that both of Cohn's worked examples break the first guideline, at six stories and five airport steps. They illustrate the arithmetic only. The second guideline binds on large plans: the formula grows with the square root of the item count, so with identical items whose spread equals their 50% estimate it reaches exactly 20% at 16 items and falls below after that.

### What the formula assumes

The sections below are this wiki's reading.

- **Independence.** The reduction relies on items not going wrong together, which is Cohn's "very little chance that everything will go wrong" (L3935). If many items share one cause, such as one unproven integration or one review gate, the spreads add rather than pool. Table 17.2 would then need up to 18 (35 − 17), not 9. The sign is several wide items whose risk names the same thing. Cohn himself says earlier in the book that software durations are often not independent and that "variations in completion time will not balance out" (L610), which the formula in this chapter does not revisit. This wiki resolves the two by the items: the formula applies to items of unlike kinds, and for a set of similar items ([[re-estimate-when-relative-size-changes]]) the plan treats their spreads as one risk and adds them.
- **The two-sigma label.** Cohn says the 50-90 gap "is about two standard deviations" (L3964). On a normal curve it is about 1.28. The result is unaffected: whatever multiple is used, it cancels, because the same multiple converts the spread into σ and the total σ back into a buffer. The label is loose; the formula stands.
- **Median versus average.** Table 17.2 calls the 50% figure the "average case". On a right-skewed [[completion-time-distribution]] the median sits below the mean, so a sum of 50% figures slightly understates the likely total. The claimed 90% level is an approximation; L4055 says "90–95%" of the same thing.

### A printed discrepancy

Figure 17.4 shows a 53-minute buffer on 70 minutes of 50% estimates and a total of 1:58 (L3948), and the text repeats 1:58 as "nearly an hour shorter" than 2:50 (L3952). The formula on Figure 17.3's spreads gives √2750 ≈ 52.4, which supports 53, but 70 + 53 is 2:03, or 47 minutes shorter. This wiki takes 2:03 as the consistent figure.

## Feature Buffer

A feature buffer protects a date with scope rather than time: the plan contains more than must ship, and the excess is what gets dropped. The promise is "we’ll get you all of the functionality in this pile and hopefully some of the functionality in that pile" ([[cohn-agile-estimating-planning]] L3849). It suits work where the date is firmer than the exact contents ([[fitting-stories-into-a-release]]); the choice at the top of this page covers the choice, and *Schedule Buffer* (above) is the time-side counterpart. The same move made late, on a running plan that has lost its margin, is *Droppable Stories on a Running Plan* (below).

### Procedure

1. The customer selects the absolutely mandatory work and its estimates are summed. "This represents the minimum that can be released" (L3849).
2. The customer selects another 25–40% more work, toward the top of the range when uncertainty is higher or tolerance for schedule risk lower (L3849).
3. Plan as normal for the whole set.
4. Build the optional work last: "The optional work is developed last, only after the mandatory work is complete" (L3853).

Cohn's example: 100 mandatory points plus 30 optional is 130; at 10 points per one-week iteration that is 13 iterations, with mandatory work done after ten if all goes well (L3855). If time runs short, "the schedule can still be met by dropping items in the feature buffer" (L4063).

### DSDM's position

DSDM sorts requirements into Must, Should, Could and Won't Have (MoSCoW), and "No more than 70% of the planned effort for a project can be targeted at Must Have requirements" (L3857). Cohn calls this consistent with his process. This wiki notes that the two figures are measured differently: Cohn's 25–40% is on top of mandatory work, so the optional share of the plan is 20–29%, while DSDM's 30% is of the whole, which is about 43% on top of Must Have. In this wiki's reading, a project set up with DSDM uses the 70% cap, which is the larger buffer, and any other setup uses Cohn's range, stating which base the percentage is taken from.

### Inputs and the fact that would show the choice wrong

- **Which items are mandatory:** from the person who owns what ships. This wiki maps Cohn's customer to the person steering; it is not a judgement for an agent to make.
- **Estimates and velocity:** from the items and board history.
- **Uncertainty and tolerance for schedule risk:** from the plan's setting, and they place the figure in the 25–40% range.

This wiki reads the optional part as too small if mandatory work overran into the date and the optional items were already gone. It was not a buffer at all if the optional items proved unshippable to leave out when the date came.

### Signs

These signs are this wiki's. Each raises a question to check, not a verdict.

- An optional item in progress while a mandatory item has not started. This breaks the order that makes the buffer work, and this wiki reads it as the sign most visible on a board.
- Every item in a plan with a firm date is marked mandatory, so there is nothing to drop.
- Must-level items exceed 70% of planned effort on a DSDM setup.
- Items move from optional to mandatory during the plan, shrinking the buffer without any item being dropped.

### Trade-offs

The customer accepts that some selected work may not arrive, and the team plans work it may never build. Cohn presents the setup as simple on an agile project (L3849), since prioritized, independently deliverable work is what makes dropping cheap. This wiki reads that as the condition: the buffer depends on items that can be left out, which is a cutting question ([[vertical-slice]]) and an ordering one ([[ordering-by-value-and-urgency]]).

### Agent executor note

This method depends on plan order, not on any human mechanism, so this wiki expects it to survive an agent executing unchanged.

## Droppable Stories on a Running Plan

A release forecast that lands right on its date can be protected by naming, in advance, the stories that will be given up to hold it. In this wiki's vocabulary that is a *Feature Buffer* (above) named late: scope protects the date, and no reserve of time is added as on *Schedule Buffer* (above). In the fictional case study of [[cohn-agile-estimating-planning]], the coach puts the choice as two branches.

> If we want to keep the schedule at ten iterations, though, we should make sure we’re willing to drop some low priority stories if we start to run out of time. If you’re not willing to do that, we should convey the expectation that it may take longer than ten iterations.
>
> — [[cohn-agile-estimating-planning]], L6372

The bottom of the priority list now carries the weight:

> This is a time when it’s important to know those at the bottom.
>
> — [[cohn-agile-estimating-planning]], L6376

### Inputs and where each is read from

- **The margin of the forecast:** from [[velocity-range-forecast]]. The case had a ratio of 7.8 against 8 periods available.
- **Velocity:** board history. The case's threshold was "at least 17 points of stories" (L6376), and its velocity was 17. This wiki reads the threshold as one period's velocity; the source does not state that derivation.
- **Which stories can go:** the person who owns value. The case's product manager named 8 + 8 + 6 = 22 points (L6378-L6382).
- **Whether a date matters:** the project's setup. This wiki reads a release with nothing tied to its date as having less to protect, and the case's release "isn’t tied to any specific date" (L6271), so what it protects there is the expectation already given to people.

### The rule

The named stories are ordered last.

> So you should work on those last. If you start to run out of time by the tenth iteration, drop one or more of those
>
> — [[cohn-agile-estimating-planning]], L6384

They stay in the plan until dropped. The product manager kept them because "they’re probably worth two additional weeks" (L6390). The same list also prices an earlier release: 133 − 22 = 111 points gives 7 more periods, 18 weeks rather than 20 (L6386-L6388).

### Against the feature buffer

Chapter 17's *Feature Buffer* (above) is set up when the plan is made, with 25-40% on top of mandatory work (L3849). The case's list is smaller. By this wiki's arithmetic its 22 points are 20% on top of the other 111, and the 17-point threshold would have been 15% on top of 116.

This wiki resolves the difference by when the question arises. While a plan is being built, the feature buffer applies and its range sets the size. Once a running plan has lost its margin, this section applies and one period's velocity is the minimum worth naming, because a reserve smaller than a period cannot absorb a period's shortfall. Neither figure is a measurement.

### What later fact would show the choice wrong

These are this wiki's readings.

- The date arrives with named stories finished and stories ranked above them unfinished: the order was not honoured.
- The date is missed although the buffer was spent: the buffer was too small for the error in the estimates.
- Time runs short and the owner refuses to drop what was named: the buffer existed only on paper.

The case does not settle this. It does not report whether the named stories were built, and its team delivered at 22 weeks for a different reason ([[chosen-delay-versus-slip]]).

### What it costs

The stories are real value held at risk, and the plan's headline scope cannot be promised whole. The rule also needs a person willing to name what they would give up, which is the step that can fail. Where nobody will, the source's second branch applies, and people are told the date may move.

### Agent executor note

This wiki reads nothing here as depending on a human executor. The person steering names the stories, and an agent can follow the order directly, provided the mark is on the board and not in a conversation ([[conversation-moves-into-the-task]]). Compare [[ordering-by-value-and-urgency]].
