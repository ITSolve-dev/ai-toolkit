---
title: All-or-Nothing Counting
category: reading-history
summary: A task counts toward velocity at its full estimate if complete at period end and not at all otherwise, because only not started and done can be known and partial credit hides growing unfinished work; the one exception, when the remainder will not be done next period, replaces the task with two re-estimated stories that need not sum to the original. The rule needs a done that can pass or fail.
tags: [rule, velocity, retrospective-analysis, definition-of-done, iterations, board-history, cohn, decision-rule, re-estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# All-or-Nothing Counting

The rule that keeps [[velocity]] usable: a task is either complete or it contributes nothing.

> The most important rule is that a team counts points toward velocity only for stories or features that are complete at the end of the iteration.
>
> — [[cohn-agile-estimating-planning]], L4290

The chapter summary states the split explicitly: a finished story counts its full estimate, and "If a story is partially completed during an iteration, it is not counted at all when determining velocity." (L4425). The narrow exception for work being deferred, which replaces the task with two rather than crediting a fraction, is on *Partial Credit for Unfinished Tasks* (below).

## What complete means

The source excludes "the coding is done but it hasn’t been tested" and "it’s coded but needs to be integrated", and then gives its bar:

> Complete means code that is well written and well factored, checked-in, clean, complies with coding standards, and passes all tests.
>
> — [[cohn-agile-estimating-planning]], L4290

This wiki reads that bar as one instance of the project's own standard of done ([[started-and-finished-points]], [[unfinished-at-period-end]]), not as a universal list. Chapter 7 words the same bar as "coded, tested, and accepted by the product owner" (L1496). This wiki keeps the acceptance, since a result awaiting its verdict has not yet earned its points.

## Sign of violation

- **In a period's report:** a percentage or a fraction of an estimate against a task, or a period total that is not the sum of whole estimates.
- **In board history:** a period total that does not equal the sum of estimates of tasks past the finished point at period end.
- **In board history:** one task's points reported in two periods, or a task split at period end so the part already worked on can be counted while its result was never presented.
- **In board history:** a task's progress is taken from sub-steps closed, and it is credited before its acceptance check passes.
- **In a task's text:** the remaining work is described as nearly nothing while the acceptance check has not been run.

These signs are this wiki's derivation from L4290, L4425 and L4939. They raise a question for checking, and the last in particular has legitimate forms: [[narrowing-a-task-mid-period]] allows a split that leaves a complete, presentable piece, and *Partial Credit for Unfinished Tasks* (below) allows one when the remainder is deferred.

## Why

The rule protects the reading of progress: "Opening the door to counting partially finished work, perhaps giving partial credit, makes it impossible to know exactly where we are." (L4290). The source then gives three reasons (L4292-L4298).

1. **Partial work cannot be measured.** It asks which is further along, a story programmed with no tests run, or one partly programmed and partly tested. Then:

> We’re good at knowing when something hasn’t been started and we’re fairly good at knowing when it’s done. We should assess work to be in one of those two states and leave it at that.
>
> — [[cohn-agile-estimating-planning]], L4292

Chapter 22 states the same two ends, under its guideline to base plans on facts (L4935):

> It’s easy to tell when a feature is 0% done (we haven’t started it) and it’s relatively easy to tell when we’re 100% done (all tests pass for all of the product owner’s conditions of satisfaction). It’s hard to measure anywhere in between—is this task 50% done or 60% done? Because that question is so hard, stick with what you can know, 0% and 100%.
>
> — [[cohn-agile-estimating-planning]], L4939

This wiki reads a reported percentage as an estimate presented as an observation.

2. **It weakens trust between developers and the customer side.** The stated remedy is resolving a story that cannot be finished as soon as that is discovered (L4296), and that is what [[narrowing-a-task-mid-period]] takes up.

3. **It builds up work in process, and this is the reason the source ranks first.**

> The more work-in-process a team allows to build up, the longer it will take new features to be transformed from raw ideas into functioning software.
>
> — [[cohn-agile-estimating-planning]], L4298

The source adds that throughput of the whole team falls over time and that feedback, and so learning, comes later (L4298). It gives no figures. The mechanism is what this wiki keeps; see [[wip-control]].

## Precondition: a done that can fail

The rule needs a done that can pass or fail. Cohn's 100% is defined by conditions of satisfaction with tests (L4939, [[conditions-of-satisfaction]]). This wiki reads a task without [[testable-acceptance]] as having no such end, so the rule cannot apply to it until that is fixed.

## Cohn's case: 16 and not 17

The fictional case study in Chapter 23 (L4961) runs the rule on a small figure. The team planned 18 points and left a 2-point story partly done, and the product manager asks whether half of it earns 1 point (L6259). The coach answers:

> In general we want to apply an all-or-nothing approach to the story points. It’s too hard to give ourselves partial credit because we really don’t know how much work is left. Rather than guessing, we don’t get any credit until we get it all.
>
> — [[cohn-agile-estimating-planning]], L6261

Velocity is 16 (L6263), and the forecast is recomputed from 16 and not from a negotiated 17 (L6267). This wiki reads the mechanism as follows: a credited fraction puts a guess into a number otherwise made of agreed estimates, and that number feeds every later forecast ([[velocity-range-forecast]]).

The story returns in the next iteration at its full 2 points (L6287), although the team says it has "a bit of a headstart" on it (L6300). This wiki reads the effect as a shift and not a loss: the points move to the period the story finishes in, so velocity understates one period and overstates the next, and an average absorbs it. What became of the story itself, dropped so that its programmer could help on work held to matter more for the demonstration (L6223-L6225), is on [[unfinished-at-period-end]].

## Discriminating criterion: measure versus board

This wiki reads the two states of L4292 as a rule for **counting progress**, not as a rule for **board columns**. A board may distinguish many states ([[distinguishable-work-states]]) while only the started and finished boundary feeds the count. The source does not address columns here.

## Cost

Chapter 19 names no cost. Chapter 7 does: velocity dips in one iteration and rises in the next, and Cohn accepts that because the interest lies in the average over time (*Partial Credit for Unfinished Tasks* (below), L1496). This wiki adds that the larger the tasks, the larger the steps, which is another argument for small tasks and not for partial credit ([[size-spread]]). A large task shows nothing for a long time and then its whole size at once, and a nearly finished one counts as zero. The case study's swing was 2 points in 18.

## Softening in the source

After the firm rule, the source says "How they count such a story is less important than that they determine why it happened and how they can prevent it from happening again." (L4302). This wiki does not read that as permission to give partial credit, since the summary repeats the rule flatly (L4425). It reads it as priority: the diagnosis in [[diagnosing-unfinished-work]] matters more than bookkeeping.

## Agent executor note

The measurement argument survives and strengthens. An agent's report that work is mostly done is even less measurable than a person's, and a stopped run leaves only what is in the repository ([[unfinished-at-period-end]]). Done is read from whether the tests and conditions pass, and from nothing the executor says about itself ([[agent-silence-is-not-completeness]]). The trust mechanism is human and, with a few people steering, reduces to one thing: the person steering must not be handed a false status. The work-in-process reason survives in the feedback half: unreviewed results still delay learning, whatever executes them. This assessment is this wiki's.

## Partial Credit for Unfinished Tasks

This rule decides what a task left unfinished at the close of an iteration contributes to velocity, and what happens to its estimate. The default is all-or-nothing. Splitting with partial credit is the exception for work that is being deferred.

### Default: all or nothing

"if a story is done (coded, tested, and accepted by the product owner) then the team earns all the points, but if anything on the story isn’t done, they earn nothing" ([[cohn-agile-estimating-planning]] L1496). The source's reason is that this is the easiest case to assess at the end of an iteration (L1496).

The cost is that velocity dips in one iteration and rises in the next, when all the points land for work partly done earlier. The source accepts that because "we’re mostly interested in the team’s average velocity over time, not in whether velocity jumped up or down in a given iteration" (L1496).

### Exception: the remainder is not coming next

"in some cases the unfinished portion of a story may not be done in the next iteration. In these cases it can be appropriate to allow the team to take partial credit" (L1498). The procedure:

1. Treat what was finished as a story in its own right and estimate it relative to other stories.
2. Rewrite what is left as a new story describing only the remaining work.
3. Estimate that story relative to other stories, with current knowledge.

In the source's example, a five-point story to recommend who swims in each event finished individual events but not relays. The done part is judged equivalent to 3 points, and the rest becomes "As a coach I can have the system recommend who should swim in each relay" (L1498).

The two estimates are independent: "The combined estimates would not need to equal the original estimate of five" (L1498), and the summary repeats that the sum "does not need to equal the initial estimate" (L1514). This wiki reads that as following from size being judged against other stories, not divided out of the original figure. The story was "deceptively complex" (L1486), so forcing a sum of five would carry the earlier mistake forward.

### The choice

**Inputs.**
- Whether anything on the task is unfinished at the period's close: read from board state.
- Whether the remainder will be taken in the next period: read from the next period's plan or its ordering.

**Decision.** Remainder taken next: count nothing now and everything on completion. Remainder deferred: split, re-estimate both parts, and credit the finished part.

**What later fact shows the choice wrong** (this wiki's derivation): a task left at nothing because the remainder was expected next is still open a period later, so its completed work stayed out of velocity for longer than the default assumes.

The source's guidance is less firm than this choice implies. The chapter body says partial credit "can be appropriate", while the summary says "I do not recommend giving partial credit" yet allows that a team "may choose" to re-estimate (L1498, L1514). This wiki reads them together as a default with a narrow exception.

### Against the Scrum Guide's rule

[[unfinished-at-period-end]] has an item that missed the Definition of Done return to the backlog and count for nothing. Cohn's default agrees. His exception looks like a conflict, and this wiki resolves it as follows; the resolution is ours. The exception does not credit a fraction of an open task, because it replaces the task with two. Under a setup following the Scrum Guide, the split is allowed only if the finished part meets the standard of done as an item in its own right, so what is counted is a finished item. The remainder then goes back to be ordered like anything else, with no claim on the next period. A task counted at a percentage stays the sign of violation on that page.

### The better answer is upstream

"the two best solutions to allocating points for incomplete stories are first not to have any incomplete stories and second to use sufficiently small stories that partial credit isn’t an issue" (L1500). This wiki reads a task repeatedly crossing a period boundary as raising a question about how it was cut, not about how to credit it. That reading fits the plugin's working test that a started task can be finished without waiting, though that test has no source and comes from the plugin's design.

### Observable signs

Derived by this wiki from the rule; each raises a question.

- A period's velocity includes points from tasks not in a done state.
- A split pair sums exactly to the original estimate, which may mean the parts were apportioned arithmetically and not estimated against other tasks.
- The same remainder is carried over more than one period.

### Settings and executors

The rule exists only where velocity is counted over a period. In this wiki's reading, a project with no iterations has no boundary at which to divide credit, and a task simply counts when it closes.

Being "accepted by the product owner" (L1496) is a condition on earning, so a task whose result is presented and awaiting a verdict has earned nothing yet. This wiki takes that to carry over to a person reviewing an agent's result: the executor's part may have ended, while the points have not been earned. The all-or-nothing rule does not depend on a human executor.

Related: [[velocity]], [[re-estimate-when-relative-size-changes]], [[unfinished-at-period-end]].
