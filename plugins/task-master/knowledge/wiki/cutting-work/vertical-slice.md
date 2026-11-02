---
title: Vertical Slice
category: cutting-work
summary: A task cut through the architectural layers so that finishing it changes something a person can observe, as opposed to a task that changes one layer; Cohn's tracer bullet, which may show progress without yet being useful to its end user. Work is completed and counted as features a user values, not as isolated tasks; a plan that lists and counts activities can finish on paper with nothing received.
tags: [concept, decomposition, invest, rule, vertical-slice, value, failure-mode, planning]
sources: [wake-invest, humanizing-work-splitting, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Vertical Slice

A vertical slice is a task cut across the architectural layers so that finishing it delivers a change someone can observe. The Humanizing Work authors define both shapes:

> Vertical slice is a shorthand for “a work item that delivers a valuable change in system behavior such that you’ll probably have to touch multiple architectural layers to implement the change.” When you call the slice “done,” the system is observably more valuable to a user.
>
> — [[humanizing-work-splitting]], L133

> This is in contrast with a horizontal slice, which refers to a work item representing changes to one component or architectural layer that will need to be combined with changes to other components or layers to have observable value to users.
>
> — [[humanizing-work-splitting]], L135

This wiki reads "observably" as the operative word. It is what connects the slice to the charter's test that a result is presented once ([[unit-of-work]]). A work item of the horizontal shape is the failure described on [[component-task-masquerading]].

Wake gives the image the term comes from:

> Think of a whole story as a multi-layer cake, e.g., a network layer, a persistence layer, a logic layer, and a presentation layer. When we split a story, we’re serving up only part of that cake. We want to give the customer the essence of the whole cake, and the best way is to slice vertically through the layers.
>
> — [[wake-invest]], L60

Wake's reason is value, and the same line gives the counter-example: "a full database layer (for example) has little value to the customer if there’s no presentation layer." This wiki reads the rule as a consequence of the charter's second working test in [[unit-of-work]]: a piece with nothing to show cannot be presented, so its result has to be presented later together with something else, and it is not a unit.

## The tracer bullet

Cohn's term for the same shape is the tracer bullet, which he takes from Hunt and Thomas:

> A tracer bullet travels through all layers of a feature. That may mean delivering a partial user interface, a partial middle tier, and a partial database. Delivering a cohesive subset of all layers of a feature is almost always better than delivering all of one layer.
>
> — [[cohn-agile-estimating-planning]], L2701

His guideline follows: "Don’t split a large story into tasks. Instead, try to find a way to fire a tracer bullet through the story." ([[cohn-agile-estimating-planning]] L2707). This wiki notes that "almost always" is an unmeasured judgement, and that he gives no reason in the chapter. He leaves the question to the reader: "What problems do you think are caused by splitting a story into tasks and then treating the tasks as user stories?" (L2737). The reason on this page therefore stays Wake's and the one from [[unit-of-work]].

## Valuable does not mean shippable

The authors separate value from release: "Stories don’t need to provide enough value by themselves to be worth shipping. You might need to accumulate several stories to move from valuable to marketable." (L117). This wiki reads that as a limit on the test: a slice has to be observable, and it does not have to be releasable alone.

Cohn's search screen is the sharpest example this wiki has of how thin a slice may be, and it goes further. At the end of the first iteration the results area showed only a line such as "this search found 312 matches" ([[cohn-agile-estimating-planning]] L2627):

> This certainly wasn’t very useful for a user who wanted to know what those 312 matches contained. However, it represented significant progress and made that progress visible to all project stakeholders.
>
> — [[cohn-agile-estimating-planning]], L2627

This wiki reads that as a further step on the same ladder: a slice has to be observable, it need not be releasable, and Cohn adds that it need not yet be useful to its end user. That is weaker than "observably more valuable to a user" in the definition above, so this wiki keeps the weaker test for a piece inside one cut: what the slice has to do is run through the layers and show something a reviewer can judge. The count of matches proves that the fields and the query builder work together, which a finished form with no query behind it would not.

Cohn's login example makes the same point about release: "You probably would not choose to release the product with only the first story supported, but there may be value in splittng the stories in this way." (L2657). The cost of that latitude is on [[story-splitting-patterns]].

## Width is a separate question

A vertical slice can still be too big. The authors say "Sometimes those vertical slices are pretty wide" (L141), and thin ones are found inside wide ones by [[story-splitting-patterns]]. They also state the cost of the shape: "As stories get smaller, for example, it becomes harder to make them independent and valuable." (L125).

## Agent executor note

All three sources speak from human teams, and none reports a measurement. Wake explains the opposite habit by a human preference: "Developers often have an inclination to work on only one layer at a time (and get it “right”)" (L60). Cohn gives a like cause: splitting by activity is such a habit that "we often do it without even being aware of it" ([[cohn-agile-estimating-planning]] L2695). Those explanations do not carry over to an agent. The reason for the rule does, because it sits with the person reviewing the result and not with the executor: a person steering an agent can only judge a result that shows behaviour. A line reading "312 matches" can be checked by someone steering, and a finished layer cannot.

## User-Valued Features Over Isolated Tasks

This rule says the unit of completion that counts is a feature a user or customer would value, not a piece of work that has meaning only once combined with others.

> agile teams focus on completing and delivering user-valued features rather than on completing isolated tasks
>
> — [[cohn-agile-estimating-planning]], L782

Cohn lists this as the second of two ways a team shows commitment to business priorities (L780-L782), and calls user stories "One of the best ways to do this" (L782); see [[unit-of-work]]. He gives no separate reason. This wiki reads one from the same passage: order is set on features by what they return (L780), so a piece with no value of its own cannot be ordered on that basis, and finishing it delivers nothing to compare.

### A note on terms

Cohn's "task" is not this plugin's unit of work. In his iteration planning, tasks are the pieces "needed to transform a feature request into working and tested software." (L839). This wiki reads the plugin's unit, finished without waiting and presented once, as closer to his feature than to his task ([[unit-of-work]]). Pieces smaller than that are the executor's business and do not belong on the board as separate results. The "finished without waiting" test has no source; it comes from the plugin's design.

### Signs to check

The source gives none. This wiki reads the following as questions to ask of a task's text or a board.

- Items titled by a technical layer or an activity, such as "add table" or "write endpoint", with nothing a user could notice. The same sign at the level of a whole plan is on *Activity-Based Plan* (below), and at the level of one item on [[component-task-masquerading]].
- Several items closed and no change visible to anyone until a later one closes.
- A story's "so that" clause that restates the capability, or names only a technical benefit.

A technical item is not automatically a defect: the sign raises a question about whether it should be folded into the feature that needs it, which is the *Vertical Slice* (above) remedy.

### Trade-offs

The source does not state one. This wiki notes the likely one: cutting by user-visible result can make a single item touch several layers and grow, which then has to be checked against [[size-ceiling]].

### Relation to dependencies

This wiki notes that pieces with no value of their own usually come with an order among them, which is the shape Cohn's case against feature dependencies warns about ([[independent-tasks]], L780). Fixing one tends to help the other.

### Agent executor note

The rule concerns what a receiver gets and does not depend on who executes, so this wiki reads it as surviving. An agent will carry out a technical item as readily as a feature, so nothing on the executor's side pushes back on a bad cut, and the check has to happen before a task reaches it.

Related: [[unit-of-work]], [[potentially-shippable-increment]], [[order-by-value-not-convenience]].

## Activity-Based Plan

An activity-based plan lists the work to be performed rather than the results to be delivered, and measures progress by the activities completed. Cohn names it the first cause of planning failure, in the setting of a traditionally managed project tracked with a Gantt chart or work breakdown structure ([[cohn-agile-estimating-planning]] L543). A board can take the same shape: the unit it counts is then something someone does, and not something anyone receives.

> A first problem with activity-based planning is that customers get no value from the completion of activities. Features are the unit of customer value. Planning should, therefore, be at the level of features, not activities.
>
> — [[cohn-agile-estimating-planning]], L543

This wiki reads "feature" here as the level at which a plan is stated and counted. Cohn does not say in this chapter how large a feature is, so this page sets no size, and [[size-ceiling]] does that work.

Chapter 22 returns to the rule as a reason agile planning works: "A traditional plan in the form of a Gantt chart, PERT chart, or work breakdown structure focuses on the tasks needed to create a product. An agile plan focuses instead on the features that will be needed in the product." (L4863).

**Terminology.** Cohn's "task" is an activity one level below a feature or story. This wiki's task ([[unit-of-work]]) sits at the level of his feature. So his rule says that a plan's units are this wiki's tasks, and that his tasks do not belong in it. A Gantt chart can meet the rule if it stops at features ([[which-chart-for-which-plan-question]], Cohn L4607-L4609).

### The rule

State the plan and count progress in results someone can receive. Activities may exist inside a unit, but they are not what the plan counts. Each item in a plan names something the product will do or be, and an item that names an activity is either inside another item or a sign that the work was cut by discipline. This wording is this wiki's, from Cohn's rule above.

### Observable signs

- **In task text:** the title names an act of building and not a result. Cohn's Figure 2.1 has four such items: "Add tables to database", "Code middle tier", "Code the user interface" and "Test" (L586).
- **Across tasks:** a request is cut by role or phase, with a closing "Test" item that everything else feeds into.
- **In a report:** progress is given as activities finished. Cohn says of the activity list "This becomes how we measure the progress of the team." (L543).
- **In a review of the plan:** the question asked is what has been left off the to-do list. Cohn's wording is "When we review a schedule showing activities we do so looking for forgotten activities rather than for missing features." (L545).
- **After an overrun:** quality is reduced to save time, or a change-control policy appears. Cohn says such policies are "designed to constrain product changes, even highly valuable changes." (L547).
- **In a plan:** the titles would be unchanged for a different product. Cohn's observation is the basis: "At a task level, many project plans look the same; every agile plan is specific to the product being developed." (L4869). Turning that into a test, by swapping the product's name and seeing whether the plan still reads, is this wiki's.

The signs in task text and across tasks are this wiki's reading of Cohn's figure. The report, review and overrun signs are Cohn's.

### Why

Four things break.

- **Progress stops meaning anything.** Every activity can be finished with nothing delivered, because activities carry no value of their own (L543).
- **Review looks in the wrong place.** A reviewer checks the list for completeness as a list of steps, so a missing feature is not looked for (L545).
- **Overruns become likely.** Cohn gives three reasons: "Activities don’t finish early", "Lateness is passed down the schedule" and "Activities are not independent" (L549-L553). Each has its own page: [[parkinsons-law]], [[lateness-passes-down-the-schedule]] and [[re-estimate-when-relative-size-changes]].
- **A plan can look complete without understanding.** Cohn quotes Highsmith: “It is easy to plan an entire project using standard tasks without really understanding the product being built. When planning by feature, the team has a much better understanding of the product.” (L4869). This wiki reads the breakage as a plan nobody can question, since no one can say what the product gains from it.

### Relation to a component task

[[component-task-masquerading]] describes one item that has nothing to present. This wiki reads the activity-based plan as the same defect at the level of the whole plan. The two signs do not fully overlap: "Test" is neither a layer nor an artifact, so a phase item is caught here and not by the component test. The remedy is the one on that page, which is to combine the pieces into a vertical slice (the definition at the top of this page) and not to cut them smaller.

### Cost

Cohn names no cost in this chapter. This wiki's reading is that a plan stated in results hides the order of steps inside each result, and that work serving several results has no natural home. Combining pieces also makes items larger, which can push them against [[size-ceiling]]. Activities that belong to no feature, such as upgrades and infrastructure, have no natural place in such a plan, and Chapter 22 does not address them. *Vertical Slice* (above) and [[component-task-masquerading]] treat the neighbouring cases.

### Agent executor note

Cohn's central reason concerns what a receiver gets and does not depend on who executes, so it survives. This wiki adds that an agent will carry out an activity item as readily as any other, so nothing on the executor's side pushes back on the cut. The overrun mechanisms survive to different degrees, and each linked page says how far.

Half of Chapter 22's argument depends on a human executor:

> When features are developed iteratively there is less need for upfront thinking about the specific tasks necessary. The work of an iteration emerges and the team will think of or discover all of the tasks as they are needed.
>
> — [[cohn-agile-estimating-planning]], L4869

This wiki reads the survival of that passage in two parts. Planning at feature level survives, because it concerns what the plan is about. Leaving the rest to emerge survives only for the steps. An executor that guesses where a person would recall does not fill gaps from context, so purpose, boundaries and acceptance have to be in the text ([[underspecified-task]], [[recoverable-versus-task-only-facts]]). Expanding a task into steps is out of scope for this wiki either way.
