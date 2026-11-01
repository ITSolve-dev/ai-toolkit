---
title: Vertical Slice
category: cutting-work
summary: A task cut through the architectural layers so that finishing it changes something a person can observe, as opposed to a task that changes one layer.
tags: [concept, decomposition, invest]
sources: [wake-invest, humanizing-work-splitting]
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

## Valuable does not mean shippable

The authors separate value from release: "Stories don’t need to provide enough value by themselves to be worth shipping. You might need to accumulate several stories to move from valuable to marketable." (L117). This wiki reads that as a limit on the test: a slice has to be observable, and it does not have to be releasable alone.

## Width is a separate question

A vertical slice can still be too big. The authors say "Sometimes those vertical slices are pretty wide" (L141), and thin ones are found inside wide ones by [[story-splitting-patterns]]. They also state the cost of the shape: "As stories get smaller, for example, it becomes harder to make them independent and valuable." (L125).

## Agent executor note

Both sources speak from human teams, and neither reports a measurement. Wake explains the opposite habit by a human preference: "Developers often have an inclination to work on only one layer at a time (and get it “right”)" (L60). That explanation does not carry over to an agent. The reason for the rule does, because it sits with the person reviewing the result and not with the executor: a person steering an agent can only judge a result that shows behaviour.
