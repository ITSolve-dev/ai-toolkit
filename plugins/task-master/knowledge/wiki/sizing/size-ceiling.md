---
title: Size Ceiling
category: sizing
summary: The size above which a task is cut, chosen by whether its scope can still be stated, with the sources' figures kept alongside the setting that produced them; a ratio of the period under iterations, the likelihood of finishing inside the SLE under a flow setup, and a floor as well as a ceiling. A large item is a placeholder: it is cut when it exceeds any period, exceeds the room left in this one, or sits close enough to a decision that a better estimate would change it, and it is cut before work starts, not when written.
tags: [rule, estimation, decomposition, invest, decision-rule, splitting]
sources: [wake-invest, humanizing-work-splitting, scrum-guide-2020, kanban-playbook-right-sizing, kanban-guide, montgomery-tracker-smells, cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Size Ceiling

The size ceiling is the step of the estimation scale above which a task is cut rather than scheduled. This rule chooses: it decides how big is too big. The reason for a ceiling is that past a certain size an estimate stops being a statement about effort and becomes a statement about not knowing what the work contains.

## The rule

Cut a task when it is above the ceiling, or when whoever estimates it cannot state what is in its scope, whichever comes first.

## Why

Wake gives the mechanism directly:

> Stories typically represent at most a few person-weeks worth of work. (Some teams restrict them to a few person-days of work.) Above this size, and it seems to be too hard to know what’s in the story’s scope. Saying, “it would take me more than a month” often implicitly adds, “as I don’t understand what-all it would entail.”
>
> — [[wake-invest]], L70

This wiki reads that as the claim worth keeping: a large number is a report of missing understanding, so the response is to find out what is inside, not to schedule the number.

Wake also ties estimability to three causes, which tell the plugin what to fix: "Being estimable is partly a function of being negotiated, as it’s hard to estimate a story we don’t understand. It is also a function of size: bigger stories are harder to estimate. Finally, it’s a function of the team: what’s easy to estimate will vary depending on the team’s experience." (L66).

## Figures and their conditions

Wake's "a few person-weeks" and "a few person-days" ([[wake-invest]] L70) describe what XP teams did as of 2003. Wake offers them as typical practice, and nothing was measured. They are denominated in human effort.

The Humanizing Work authors give a ratio and not a size:

> **SMALL**. Our rule of thumb for small enough is, by the time a story makes it to the top of your backlog, you should be able to fit 6 to 10 into a sprint. This is about getting frequent feedback and managing risk without having too many stories to manage. This is a ratio, so it scales with things like sprint length, team size, and velocity.
>
> — [[humanizing-work-splitting]], L121

This wiki notes that the figure's stated condition is "by the time a story makes it to the top of your backlog", so it does not apply to work further out. The authors call it a rule of thumb and report no measurement. They use it as a working test in their own example: "There’s no way 6-10 stories like this would fit in an iteration." (L193).

The Scrum Guide sets an outer bound and no figure: "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event." ([[scrum-guide-2020]] L278). This is a limit, because a task that cannot be Done within a period cannot be finished in it at all. The ratio above is much tighter.

The Guide's other figure is not a ceiling. It says planning "is often done by decomposing Product Backlog items into smaller work items of one day or less." (L226). That is a description of what is often done, in a person's days, one level below this wiki's task ([[unit-of-work]]), and it is at the Developers' "sole discretion" (L226). This wiki does not use it.

### Cohn's 2 to 5 days

Cohn gives a target size and states its conditions around it:

> For teams working in two-week iterations, splitting features such that each can be done in 2–5 days or so is appropriate.
>
> — [[cohn-agile-estimating-planning]], L2717

Cohn ties the figure to two-week iterations, and it moves with length: "Stories will need to be a little smaller for one-week iterations and can, but don’t need to, be a little larger for longer iterations." (L2717). Estimates stay in points, and the days are a translation each team already knows: "by the time a team needs to split stories they will know approximately how many story points or ideal days equates to around 2–5 days" (L2717).

Cohn does not say whose days these are, whether a day means elapsed time or one person's effort, or how many people work on the item. His reason is "Stories of these approximate sizes flow best through the short iterations of an agile project." (L2717). This wiki reads that as an assertion with no measurement.

This wiki's arithmetic: a two-week iteration has about ten working days, so 2 to 5 days is a fifth to a half of the iteration's length. That is a ratio of item to period length. The Humanizing Work ratio is a ratio of item to capacity. A team working in parallel can finish more than five items of that length in a period, so the two figures can both hold and cannot be converted into each other without knowing the team. This wiki keeps the 6 to 10 ratio as the working rule, since its denominator is read from history, and treats Cohn's figure as a cross-check for a human team. Both agree on the shape: the size scales with the period.

Cohn also agrees with the Scrum Guide's outer bound, in stronger words: "if implementing a particular user story will take longer than the length of the iteration there’s no choice but to split the story" ([[cohn-agile-estimating-planning]] L2579). The occasions for cutting are on *When to Split a Task* (below).

### Cohn's sub-story figure

Cohn also gives a size for the level below a story, about one task per developer per day (L3270), and the case study's band of 1 to 16 hours (L5728). It sits one level below this wiki's task and is counted in a person's on-task hours, so this wiki does not use it as a ceiling for tasks on a board or as agent run time ([[unit-of-work]]).

## A large item is a placeholder

The reasoning behind Cohn's figure does transfer, because it says what a larger item means:

> larger tasks should be generally understood to be placeholders for one or more additional task that will be added as soon as they are understood
>
> — [[cohn-agile-estimating-planning]], L3272

Cohn is permissive about creating one: "If you need to create a sixteen-hour task during iteration planning, do so. However, once the task is more adequately understood, augment or replace it." (L3272). The replacement may total more or less than the original sixteen hours (L3272), so the placeholder's number is not preserved. This wiki reads that as agreeing with Wake that a large number reports missing understanding. Cohn adds what to do about it: record the placeholder now and replace it when understanding arrives.

**Sign of violation:** an item kept whole and unchanged after work on it has shown what it contains, including when its pieces are known and listed in comments and not on the board. This sign is this wiki's.

## The Kanban position: a question and not a size

The Kanban Playbook replaces a ceiling with one question:

> Right-sizing is not estimation. You are not predicting how long something will take. You are asking one question: "Is there a good chance this item will finish within our SLE?" If yes, start it. If no, adjust it before it enters active work.
>
> — [[kanban-playbook-right-sizing]], L30

This wiki takes the question and disagrees with the first two sentences. Asking whether an item has a good chance of finishing within a stated time is a forecast of how long it will take, so it is an estimate with one step. What it does save is a scale and a number per task. The page's worked figure, "85% of items finish in 10 days or less" (L33), is the illustrated team's history and not a target.

The page also has a circle in it. It says "Until your items are right-sized, your SLE is not reliable either." (L22), and it then checks size against the SLE. So the first SLE comes from items that were never checked. This wiki's way out is to start from the Kanban Guide's "best guess" ([[kanban-guide]] L115), treat early answers as provisional, and recompute the [[service-level-expectation]] once checked tasks have finished. A check against an SLE also tightens the history by construction, so a better SLE after right-sizing is not evidence that anything else improved. Both points are ours.

The Playbook's definition adds what a ceiling lacks, which is a floor. Right-sized means "small enough to flow through your system reliably, but still deliver something a customer can use." (L16). The floor is the job of [[vertical-slice]] and [[component-task-masquerading]].

Cohn sets a floor of a different kind. He warns against reading his chapter as advice to minimize: "it may be tempting to think that every user story a team is about to work on should be made as small as possible" ([[cohn-agile-estimating-planning]] L2717), and he rejects that. This wiki reads the 2 to 5 days as a band with a lower edge, the size analogue of the Playbook's floor, though Cohn does not connect them. His response to items below it is [[combining-small-tasks]].

## Which figure applies under which setup

The sources answer different questions, so the setup decides. The resolution is this wiki's.

- **A project with iterations and an SLE:** [[flow-metrics-scrum-teams]] asks the SLE question at selection (L1044), and for two-week periods it puts right sizes at 1 to 14 days, "but in reality should probably be a little less than that" (L1038). This wiki has the SLE question replace the ratio for selection, since it reads the project's own history item by item and the ratio needs iteration capacity. The Scrum Guide's one period stays the outer limit.
- **A project with iterations and no SLE:** use the ratio. The ceiling is the capacity of one iteration divided by 6, the size at which six still fit; capacity is read from history. Below capacity divided by 10 an item is small enough that combining it with others becomes a question ([[combining-small-tasks]]). The 10 is the source's preferred upper count, not a cut line. The ratio applies to tasks near the top of the order. The Scrum Guide's bound of one period holds for every task as the outer limit.
- **A project without iterations:** the ratio has no denominator, so ask the Playbook's question against the project's SLE, and apply Wake's scope test on top of it. A project that keeps an estimation scale can use the step fixed at setup in the same place. No source gives a universal figure for this case, and the number comes from the project's own history.
- **Under both:** the scope test overrides the number. A task under the ceiling whose contents cannot be stated still gets cut.
- **Never:** person-weeks as the unit, for the reason in the note below.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The task's estimate | The task, on the project's scale |
| The ceiling | The scale step fixed when the project was set up, or iteration capacity divided by 6 where iterations exist with no SLE, or the SLE wherever one is kept |
| Iteration capacity | Board history, where iterations exist |
| The SLE | Board history, or a best guess until there is enough of it |
| Whether scope can be stated | The task text: can each thing inside it be listed |

The choice was wrong in one of two ways, and each shows up later. A task kept under the ceiling was too big if its scope grew after work started, if it had to be cut while in progress, or if it passed the SLE question and then outlived the SLE. A task that was cut was cut needlessly if its pieces were always scheduled, done and reviewed together. Cohn's figure was wrong for a project if items in the band still failed to finish within the period, or if items outside it finished as reliably; board history shows both.

## Agent executor note

Person-weeks and Cohn's days do not transfer, because they count a human's effort. The mechanism does: an estimator who cannot say what a task contains is in the same position whoever will execute it. Wake's third factor, "the team’s experience" (L66), is a human one, and the sources here do not say what replaces it for an agent. Wake's closing claim that "Smaller stories tend to get more accurate estimates" (L70) concerns human estimators and has not been tested with agents in any source in this wiki. Cohn's reason, flow through short iterations, depends on a team's pace, and this wiki expects it to be replaced by how many results the people steering can review in a period. What survives of his figure is the shape, that the size moves with the period, and its lower edge.

The ratio's reasons are "frequent feedback" and not "having too many stories to manage" (L121). Both sit with the person reviewing and steering, so this wiki expects them to survive. The count of 6 to 10 was formed on human sprint teams, though, and an agent's throughput can differ from a team's. Treat it as a starting point and re-derive it from how many results the people steering can actually review in a period.

The SLE question survives better than any fixed figure, because it reads the project's own history. It still needs someone to judge "a good chance", and the Playbook assumes a team does that. No source here says how well an agent can.

Cohn's one-per-day figure does not transfer: it counts a person's day, and both of its reasons, one developer blocking others and daily status reporting, concern a team of people. This wiki does not use it as a ceiling, and the 1 to 16 hour band falls with it: neither may be applied as agent run time. What may transfer is the purpose of a ceiling, that one result stays small enough to be reviewed at once. The charter's test, that a started task finishes without waiting, is the applicable check, and where the two disagree that test wins for an agent. The placeholder reading survives, because it concerns what is known about the work and not who does it. With an agent executing, the replacement should happen before start, since an executor that guesses will fill a placeholder with its own assumptions ([[recoverable-versus-task-only-facts]]). That last clause is this wiki's reading.

## Related

A ceiling needs one scale. The study behind [[montgomery-tracker-smells]] lists as a smell that "The “estimate” property is unclear or different scales are used across issues." (L215), with its result in a lost figure. Where that holds, no step on a scale means one thing and this rule cannot be applied. A missing estimate is judged on [[empty-fields]]. A task too poorly understood to size goes to [[spike-as-last-resort]]. A task above the ceiling is cut with [[story-splitting-patterns]]. The signs that a task is too big in its text are on [[compound-task-text-signs]], and what a large task does to the count is on [[hidden-wip-in-large-items]]. Why a size does not fix a duration is on [[story-points-do-not-convert-to-hours]].

## When to Split a Task

Cohn gives two occasions for cutting a task, which he calls a story, and divides the first in two, which makes three triggers (L2583, L2591, L2725 of [[cohn-agile-estimating-planning]]). Two are about fit and one is about knowledge. The third is conditional, and that condition is the useful part: size alone is not a reason to cut work that is still far away.

### The triggers

**It does not fit any iteration.** Cohn says "a user story should be split when it is too large to fit within a single iteration" (L2583), and "there’s no choice but to split the story into two or more stories" (L2579). This is the outer bound on *Size Ceiling* (above).

**It does not fit the iteration being planned.** A task may fit an iteration in general and still be too big now, because "it won’t fit within the iteration being planned because there isn’t enough room" (L2583). This wiki adds a limit to that trigger: a piece cut to fill leftover room still has to pass [[unit-of-work]] and be a [[vertical-slice]]. If the only piece that fits has nothing to show, the task waits for a later period and is not cut to fill the room. How much a period takes is on [[filling-a-period]].

**A decision depends on a better estimate.** "it can be useful to split a large user story (an epic) if a more accurate estimate is necessary" (L2591). Cohn's example shows when it is not necessary. A product owner weighing features for customer service representatives at other companies wrote one large story, and the team estimated it at 70 points:

> She knew there was a great deal of uncertainty in the estimate, but even if the estimate were off by 100% these features were still worth doing. If 70 story points had put her on the border of whether or not to include the CSR features in the release, she could have chosen to split the large story and have the team estimate the smaller stories.
>
> — [[cohn-agile-estimating-planning]], L2591

This wiki reads that as the test: stretch the estimate across its uncertainty and see whether the decision changes. If it holds at both ends, a rough number is enough and cutting buys nothing. If it flips, cut, because the cut is what removes the uncertainty.

### Timing

Cohn places splitting late: "As user stories rise to the top of the release plan, meaning they will be implemented soon, they often need to be split." (L2579). This wiki reads that as agreement with [[how-far-to-split-up-front]] and [[estimating-by-horizon]]: a large item further out stays large unless a decision needs otherwise. The third trigger is the exception, and it applies at any distance.

### Cut now or leave it large

A task can be known to be too big long before it has to be cut. The fictional case study in Chapter 23 (L4961) states the position in a coach's voice:

> It’s OK for us to have some big stories, and it’s perfectly fine for us to estimate them with big values. But we need to remember that we’ll have to split them up before working on them so that each fits into an iteration.
>
> — [[cohn-agile-estimating-planning]], L5363

The strong engine story, estimated at 20, is left whole. Asked whether it needs splitting as the weak engine was, the coach says "No, we can do that later, when we’re closer to working on that story" and gives the reason: "We’ll know more then and there’s nothing to gain by splitting it today." (L5451).

**The test.** Cut now if work on the task is close, or if cutting it now gives something usable today. Otherwise record its large estimate and leave it. The deadline is firm in both cases: no task above the ceiling starts. This wording is this wiki's arrangement of the chapter's two reasons.

**A gap in the source.** The same meeting cuts the 20-point weak engine at once (L5385-L5395) and keeps the 20-point strong engine (L5445-L5451), and it states a reason only for keeping one. This wiki's reading is that the weak engine is the earlier work and the strong one depends on what building it teaches. The chapter does not say so, and order has not been discussed at that point.

**Relation to the other rule on timing.** [[how-far-to-split-up-front]] asks how many pieces to enumerate when a large request is cut, and its input is whether starting will teach what the work is. This section asks when to cut at all, and its input is distance from starting. This wiki reads them as agreeing on the mechanism, that work done earlier teaches. The ratio on *Size Ceiling* (above) carries the same condition, since it applies only once a task nears the top of the order. The opposite move, combining entries finer than this stage needs, is on [[initial-task-inventory]].

### Under which setup

The resolution is this wiki's, and Cohn does not address a project without iterations.

- **With iterations:** all three triggers apply as stated.
- **Without iterations:** the first two have no denominator. Use the setup rules on *Size Ceiling* (above) in their place. The third trigger still holds wherever a decision depends on a number.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The task's estimate | The task, on the project's scale |
| Iteration capacity and remaining room | Board history and the current period, where iterations exist |
| The decision resting on the estimate | The request, or the person steering |
| The estimate's uncertainty | The estimator's statement; Cohn gives no figure beyond the 100% in his example |
| Closeness to starting | The task's position in the order |
| Whether a cut now pays | Whether it would change an estimate, an order or a decision someone faces now |

The choice to leave a task whole was wrong if the decision would have gone differently once the real size was known, or if, in board state, a task above the ceiling sits at the top of the order or has already started. The choice to cut for accuracy was wrong if the pieces' estimates led to the same decision the rough number had already supported. A cut was too early if, in history, its pieces were rewritten or thrown away before any of them started, which is the cost "We’ll know more then" (L5451) predicts. These tests are this wiki's.

### Trade-off

Cutting for an estimate spends work on items that may never be done, and Cohn's example avoids that cost: the rough number was "good enough" (L2591). The cost of not cutting is carrying an uncertain number on the plan. A large number stays in any total and it is the least accurate kind (L5363), so a forecast over the list is weakest where the deferred tasks sit. The rule also relies on someone cutting the task when it nears the top.

### Agent executor note

The example is one client anecdote with no measurement. The test sits with whoever decides, so it survives an agent executing. Cohn's assumption that smaller pieces estimate better is a claim about human estimators, and *Size Ceiling* (above) records that no source here tests it with agents.

Deferring concerns what is known when, so this wiki expects it to survive, with two shifts that no source tests. "We’ll know more then" holds only if the results of earlier tasks reach whoever cuts the later one, so a person has to read them, as on [[how-far-to-split-up-front]]. And the deadline is harder with an agent: a person handed an oversized task may stop and ask, while an agent may simply start, so the check belongs before a task can be taken ([[unit-of-work]]).
