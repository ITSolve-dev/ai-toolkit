---
title: Handling a Sequence Dependency
category: ordering
summary: When one task depends on another: leave the dependency if the wanted order already satisfies it and state the assumption; go out of the natural order only when what going early gains outweighs the enabling work or stub it costs, adding that work explicitly; promote a prerequisite that sits below the cut line; and keep a zero-point task for the wiring of a stub. Working out of order rarely lengthens a project, and when it does, the reason for reordering is what justifies it.
tags: [decision-rule, dependencies, estimation, stub, cohn, rule, ordering]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Handling a Sequence Dependency

A task can have two sizes, depending on whether something else already exists. This page decides whether to leave such a dependency in place or to remove it. The case is from the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

A story asks for a hint on request. "If we’ve done the move engine, this story is really simple." Without the engine, "this story has to be at least as big as writing the whole move engine." (L5501).

## Which remedy, when

Two pages of this wiki handle one situation, a wanted item that depends on one that is unwanted or later: enabling work and a stub (both on this page; enabling work under *Natural Order of Work*, below), and promoting the prerequisite ([[value-order-versus-technical-necessity]]). This wiki decides between them as follows, and the arrangement is ours.

1. **The wanted order already satisfies the dependency:** leave it and state the assumption (the first branch below).
2. **The wanted order goes against it, and the prerequisite is planned in the same release:** compare the enabling work, or the stub and its follow-up, with what going early is meant to gain, a named risk settled or earlier feedback. Go out of order only when the gain is larger; then add the enabling work or the stub explicitly. This gate is Cohn's cost argument from L3212-L3228, made into a test by this wiki.
3. **The prerequisite sits outside the release, below the cut line:** promote it and drop enough to stay within capacity ([[value-order-versus-technical-necessity]]), or stub it if a stubbed result would still be presentable ([[vertical-slice]]).
4. **It cannot be removed:** live with it (the last branch below).

## The test

Compare the order the dependency forces with the order you want anyway.

**They agree: leave it.**

> Developing the move engine before the hint feature seems like the natural way to program those stories. The dependency won’t be in our way. We can ignore it. Or, if we’re worried about forgetting this dependency, we can note it on the card. Either way, the story can be estimated with the assumption that the move engine exists.
>
> — [[cohn-agile-estimating-planning]], L5505

The story is estimated at 1 (L5507).

**They disagree: remove it.** The coach says "Most of the time, however, you can get rid of it." (L5511). The removal is a stub: build everything in the hint task, with a `HintGenerator` that returns "either the first open space or a random open space", and connect it to the engine later (L5511). This wiki reads that as the scaffold on [[independent-tasks]] and the enabling work on *Natural Order of Work* (below).

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

## Natural Order of Work

The natural order of a set of stories is the sequence "that makes sense to both developers and the product owner" ([[cohn-agile-estimating-planning]] L3210), and it is usually the sequence assumed when they were estimated (L3212). Cohn's claim is that dependencies following that order are not a problem, and that departing from it has a cost that can be read in advance.

### What leaving the order costs

> When stories are worked on in a sequence other than what was assumed when estimating, during iteration planning the team will often have to include additional tasks that make it possible to work on stories in the new order.
>
> — [[cohn-agile-estimating-planning]], L3212

Cohn's example shows a swimmer's fastest times before building the screens that add swimmers. The team must design the tables earlier and put a swimmer into the database directly (L3214-L3216). This wiki reads that as a dependency that is a sequence and not a wait: nobody is blocked, the prerequisite can be stood in for, and the price is extra work ([[sequence-versus-wait]]).

### Does it take longer

Cohn's answer is "Two answers: Probably not and it doesn’t matter." (L3218).

- **Probably not:** "all we’ve done is shift some tasks from one user story to another" (L3220). The later story gets cheaper by what the earlier one absorbed. Any shift of estimate between the two usually washes out, and Cohn has seen it lean slightly pessimistic, because the extra point is done but not credited, slightly understating velocity (L3222-L3226).
- **It doesn't matter:** the order was chosen for a reason, such as addressing a technical risk earlier or getting earlier feedback, which can "potentially save a month or two of rework near the end of the project" (L3228).

Both answers are coaching judgement, unmeasured. The second depends on a good reason existing: Cohn says "presumably" (L3228).

### The rule

This statement of the rule is this wiki's. Order by value and risk, and let a dependency change the order only when the enabling work costs more than the gain from going early. When going out of order, add the enabling work explicitly. Cohn's own condition covers the estimates: if the shift is significant, "re-estimate the stories involved as soon as you decide to work on them in other than the natural order" (L3226).

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The assumed order | Dependencies stated in task text, and what each estimate assumed |
| The enabling work | What the later task needs that does not exist yet |
| The reason to go early | Risk or feedback named on the task |

The choice was wrong if the risk named for the reordering was not one that, had it occurred, would have changed other work, or if nobody was placed to react to the early result. A risk that was retired with no surprise is what going early was for, and is not by itself a sign. It was also wrong if the enabling work was thrown away instead of being absorbed by the later task, which breaks Cohn's first answer.

### Trade-off

Going out of order spends work earlier and asks for stand-ins, such as hand-entered data. That is accepted in exchange for learning sooner. The stand-ins need removing or absorbing later.

### Agent executor note

A natural order is understood by people who share a picture of the product. An executor that guesses does not recall what the estimate assumed. This wiki therefore reads the assumed order as a fact the task must state, including what it expects to exist already ([[recoverable-versus-task-only-facts]]). The accounting about velocity concerns a team's numbers and carries over unchanged.

### Related

Tasks with no ordering constraint are on [[independent-tasks]]. Ranking itself is on [[ordering-by-value-and-urgency]]. A low-ranked story that has to move up because something needs it is on [[value-order-versus-technical-necessity]].
