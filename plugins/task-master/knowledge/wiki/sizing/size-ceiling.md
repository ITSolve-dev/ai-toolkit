---
title: Size Ceiling
category: sizing
summary: The size above which a task is cut, chosen by whether its scope can still be stated, with the sources' figures kept alongside the setting that produced them; a ratio of the period under iterations, and the likelihood of finishing inside the SLE under a flow setup.
tags: [rule, estimation, decomposition, invest]
sources: [wake-invest, humanizing-work-splitting, scrum-guide-2020, kanban-playbook-right-sizing, kanban-guide, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
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

## The Kanban position: a question and not a size

The Kanban Playbook replaces a ceiling with one question:

> Right-sizing is not estimation. You are not predicting how long something will take. You are asking one question: "Is there a good chance this item will finish within our SLE?" If yes, start it. If no, adjust it before it enters active work.
>
> — [[kanban-playbook-right-sizing]], L30

This wiki takes the question and disagrees with the first two sentences. Asking whether an item has a good chance of finishing within a stated time is a forecast of how long it will take, so it is an estimate with one step. What it does save is a scale and a number per task. The page's worked figure, "85% of items finish in 10 days or less" (L33), is the illustrated team's history and not a target.

The page also has a circle in it. It says "Until your items are right-sized, your SLE is not reliable either." (L22), and it then checks size against the SLE. So the first SLE comes from items that were never checked. This wiki's way out is to start from the Kanban Guide's "best guess" ([[kanban-guide]] L115), treat early answers as provisional, and recompute the [[service-level-expectation]] once checked tasks have finished. A check against an SLE also tightens the history by construction, so a better SLE after right-sizing is not evidence that anything else improved. Both points are ours.

The Playbook's definition adds what a ceiling lacks, which is a floor. Right-sized means "small enough to flow through your system reliably, but still deliver something a customer can use." (L16). The floor is the job of [[vertical-slice]] and [[component-task-masquerading]].

## Which figure applies under which setup

The sources answer different questions, so the setup decides. The resolution is this wiki's.

- **A project with iterations:** use the ratio. The ceiling is the capacity of one iteration divided by 6 to 10, and capacity is read from history. The ratio applies to tasks near the top of the order. The Scrum Guide's bound of one period holds for every task as the outer limit.
- **A project without iterations:** the ratio has no denominator, so ask the Playbook's question against the project's SLE, and apply Wake's scope test on top of it. A project that keeps an estimation scale can use the step fixed at setup in the same place. No source gives a universal figure for this case, and the number comes from the project's own history.
- **Under both:** the scope test overrides the number. A task under the ceiling whose contents cannot be stated still gets cut.
- **Never:** person-weeks as the unit, for the reason in the note below.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The task's estimate | The task, on the project's scale |
| The ceiling | The scale step fixed when the project was set up, or iteration capacity divided by 6 to 10 where iterations exist, or the SLE under a flow setup |
| Iteration capacity | Board history, where iterations exist |
| The SLE | Board history, or a best guess until there is enough of it |
| Whether scope can be stated | The task text: can each thing inside it be listed |

The choice was wrong in one of two ways, and each shows up later. A task kept under the ceiling was too big if its scope grew after work started, if it had to be cut while in progress, or if it passed the SLE question and then outlived the SLE. A task that was cut was cut needlessly if its pieces were always scheduled, done and reviewed together.

## Agent executor note

Person-weeks do not transfer, because they count a human's effort. The mechanism does: an estimator who cannot say what a task contains is in the same position whoever will execute it. Wake's third factor, "the team’s experience" (L66), is a human one, and the sources here do not say what replaces it for an agent. Wake's closing claim that "Smaller stories tend to get more accurate estimates" (L70) concerns human estimators and has not been tested with agents in any source in this wiki.

The ratio's reasons are "frequent feedback" and not "having too many stories to manage" (L121). Both sit with the person reviewing and steering, so this wiki expects them to survive. The count of 6 to 10 was formed on human sprint teams, though, and an agent's throughput can differ from a team's. Treat it as a starting point and re-derive it from how many results the people steering can actually review in a period.

The SLE question survives better than any fixed figure, because it reads the project's own history. It still needs someone to judge "a good chance", and the Playbook assumes a team does that. No source here says how well an agent can.

## Related

A ceiling needs one scale. The study behind [[montgomery-tracker-smells]] lists as a smell that "The “estimate” property is unclear or different scales are used across issues." (L215), with its result in a lost figure. Where that holds, no step on a scale means one thing and this rule cannot be applied. A missing estimate is judged on [[empty-fields]]. A task too poorly understood to size goes to [[spike-as-last-resort]]. A task above the ceiling is cut with [[story-splitting-patterns]]. The signs that a task is too big in its text are on [[compound-task-text-signs]], and what a large task does to the count is on [[hidden-wip-in-large-items]].
