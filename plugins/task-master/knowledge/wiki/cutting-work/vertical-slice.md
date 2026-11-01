---
title: Vertical Slice
category: cutting-work
summary: A task cut through the architectural layers so that finishing it changes something a person can observe, as opposed to a task that changes one layer; Cohn's tracer bullet, which may show progress without yet being useful to its end user.
tags: [concept, decomposition, invest]
sources: [wake-invest, humanizing-work-splitting, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
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

Cohn's login example makes the same point about release: "You probably would not choose to release the product with only the first story supported, but there may be value in splittng the stories in this way." (L2657). The cost of that latitude is on [[deferred-concern-slice]].

## Width is a separate question

A vertical slice can still be too big. The authors say "Sometimes those vertical slices are pretty wide" (L141), and thin ones are found inside wide ones by [[story-splitting-patterns]]. They also state the cost of the shape: "As stories get smaller, for example, it becomes harder to make them independent and valuable." (L125).

## Agent executor note

All three sources speak from human teams, and none reports a measurement. Wake explains the opposite habit by a human preference: "Developers often have an inclination to work on only one layer at a time (and get it “right”)" (L60). Cohn gives a like cause: splitting by activity is such a habit that "we often do it without even being aware of it" ([[cohn-agile-estimating-planning]] L2695). Those explanations do not carry over to an agent. The reason for the rule does, because it sits with the person reviewing the result and not with the executor: a person steering an agent can only judge a result that shows behaviour. A line reading "312 matches" can be checked by someone steering, and a finished layer cannot.
