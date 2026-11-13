---
title: Choosing Between Splits
category: cutting-work
summary: When a task can be cut several ways, prefer the cut that exposes something to throw away, then the cut that gives more equally sized pieces; for the first slice of a new or complex thing, cut through the core complexity, the part most likely to surprise, with its variations reduced to one.
tags: [decision-rule, decomposition, splitting, method]
sources: [humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-02
---

# Choosing Between Splits

A task can usually be cut in several ways with the [[story-splitting-patterns]], and the choice matters because a poor cut hides low-value work inside each piece. This rule chooses. It comes from the Humanizing Work authors' "two rules of thumb" (L325).

## The tests

> **Choose the split that lets you deprioritize or throw away a story.** The 80/20 principle says that most of the value of a user story comes from a small share of the functionality. When one split reveals low-value functionality and another doesn’t, it suggests that the latter split hides waste inside each of the small stories. Go with the split that lets you throw away the low-value stuff.
>
> — [[humanizing-work-splitting]], L327

> **Choose the split that gets you more equally sized small stories.** The split that turns an 8 point story into four 2 point stories is more useful than the one that produces a 5 and a 3. It gives the Product Owner more freedom to prioritize parts of the functionality separately.
>
> — [[humanizing-work-splitting]], L328

The authors give no priority between the two tests. This wiki applies them in the order the authors list them, because a piece dropped is work avoided, while equal sizes only widen the choice of order. "80/20" is the authors' appeal to a principle, and nothing in the source measures it.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The candidate splits | The output of [[story-splitting-patterns]] |
| The value of each piece | The purpose stated in the request, and the person steering when that is not enough |
| The size of each piece | An estimate on the project's scale |

The choice was wrong if, once the pieces were done, part of the functionality inside a kept piece was dropped or went unused as low-value: the split hid waste inside a piece, which is what the first test exists to prevent. This test is this wiki's. Pieces estimated as equal that lived very different times show an estimating error, not a wrong split, so they are not a test here.

Equal size here breaks a tie between splits of a task that is already too big; it is not a reason to split, which is the same-sizing failure on [[size-spread]].

## Agent executor note

The evidence is coaching experience with human teams, with no measurement. Both tests concern a decision made by whoever steers, so they survive an agent executing. The authors' "Product Owner" here is the person steering.

## Find the Core Complexity

This is the move the Humanizing Work authors say underlies their [[story-splitting-patterns]], usable on its own: "focus on the complexity and reduce the variations through it" (L313). The authors recommend it for one job in particular: "This approach works particularly well for the first slice of a new thing because it goes straight for the core complexity and avoids anything else that would make the work bigger." (L321).

### The procedure

1. **Find the core complexity.** The authors ask what part is most likely to surprise you. Their guidance on where to look:

> What’s the part that’s most likely to surprise you or have something emerge? It’s often the part that depends on human preferences or behavior. Sometimes, it’s the part with a new integration or external dependency.
>
> — [[humanizing-work-splitting]], L315

2. **Identify the variations.** The authors list "Business rules, user types, interfaces, data variations, entities, etc." (L316).
3. **Reduce all the variations to one.** The authors define that as "a single, complete slice through the complex part" (L317), which may be a single scenario or a range of scenarios through one business rule variation.

### When to use it

This wiki's use for it is the case [[how-far-to-split-up-front]] marks as complex, where one or two slices are wanted and not a full list. The first slice then runs through the part most likely to surprise, because that is the part that teaches the most.

### What would show it wrong

The first slice was chosen wrongly if the surprise came from somewhere else, that is, if the tasks that had to be rewritten after it were outside the part it covered. That test is this wiki's, and the authors do not state one.

### Agent executor note

The evidence is coaching experience with human teams, with no measurement. The method survives an agent executing, because it reads the request and not the executor. The source of surprise it names, "human preferences or behavior" (L315), lies with the people steering, which makes that part harder for an agent to guess.
