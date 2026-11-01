---
title: Handling a Sequence Dependency
category: ordering
summary: When one task's size depends on another being done, leave the dependency if the wanted order already satisfies it and state the assumption; remove it with a stub only when the later task is really wanted first, and keep a zero-point task for the wiring.
tags: [decision-rule, dependencies, estimation, stub, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Handling a Sequence Dependency

A task can have two sizes, depending on whether something else already exists. This page decides whether to leave such a dependency in place or to remove it. The case is from the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

A story asks for a hint on request. "If we’ve done the move engine, this story is really simple." Without the engine, "this story has to be at least as big as writing the whole move engine." (L5501).

## The test

Compare the order the dependency forces with the order you want anyway.

**They agree: leave it.**

> Developing the move engine before the hint feature seems like the natural way to program those stories. The dependency won’t be in our way. We can ignore it. Or, if we’re worried about forgetting this dependency, we can note it on the card. Either way, the story can be estimated with the assumption that the move engine exists.
>
> — [[cohn-agile-estimating-planning]], L5505

The story is estimated at 1 (L5507).

**They disagree: remove it.** The coach says "Most of the time, however, you can get rid of it." (L5511). The removal is a stub: build everything in the hint task, with a `HintGenerator` that returns "either the first open space or a random open space", and connect it to the engine later (L5511). This wiki reads that as the scaffold on [[independent-tasks]] and the enabling work on [[natural-order-of-work]].

**It cannot be removed: live with it.** "Sometimes you can’t get rid of a dependency and you have to live with it, just like before you started using an agile process" (L5511). The chapter gives this branch no further treatment. How such a dependency constrains order is on [[sequence-versus-wait]].

In the chapter the team takes the first branch: "we’ll just keep that as a one-point story" (L5529). The stub only answers what they would have done otherwise.

## The zero-point task

A stub leaves work behind. The follow-up is real and tiny, "probably a one line change" (L5517), and at 1 point it would make the split look pointless (L5517-L5521). So the scale gains a zero:

> Because we have to come back and hook HintGenerator up to the right code, we want a story card so that we don’t forget. On the other hand, it really is so simple that we want to call it a zero.
>
> — [[cohn-agile-estimating-planning]], L5523

This wiki reads a zero as separating two things a number usually joins: that work must be remembered, and that it costs effort worth counting. The limits of zeros are on [[estimation-scale]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The dependency | The task text, or two estimates that differ by whether something exists |
| The wanted order | The order on the board |
| The natural order | The dependency's direction, and whether the prerequisite is planned earlier |

The table is this wiki's arrangement. The choice to leave a dependency was wrong if the order later changed and the task's estimate stopped being true, which is the risk on [[independent-tasks]]. The choice to stub was wrong if the zero-point task never ran, which shows as a stub still in the code after its follow-up was dropped or forgotten.

## Relation to independent tasks

[[independent-tasks]] treats an estimate that depends on order as a sign. The chapter's position agrees with that page's weaker test, that the defect is the unstated dependency. An estimate made "with the assumption that the move engine exists" (L5505) is order-dependent and acceptable only when the assumption is stated. This wiki therefore reads the chapter's "We can ignore it" (L5505) narrowly. For a team that talks daily, ignoring it may be safe. For this wiki's setting, noting it is the branch to take.

## Trade-off

A stub makes a task finishable early at the price of a task that delivers less than its title promises. Hints from a random open space are not useful hints, so the chapter names the follow-up "As a player, I want to get good hints" (L5515). This wiki notes that the coach's claim, "you’d be done with the hint story before even starting the move engine" (L5511), holds only for the interface part. Whether a stubbed result is presentable is a question for [[vertical-slice]]. The stub also costs code that will be replaced.

## Agent executor note

The structure survives. The memory does not: "we want a story card so that we don’t forget" (L5523) states why the zero-point task exists, and an agent recalls nothing between tasks, so with an agent the card is the only memory. This wiki also reads a stub as a hazard with an agent, because a stub that passes its checks looks finished, so the task's conditions should say that it is one ([[conditions-of-satisfaction]]). No source tests this.
