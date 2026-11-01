---
title: Choosing Between Splits
category: cutting-work
summary: When a task can be cut several ways, prefer the cut that exposes something to throw away, then the cut that gives more equal pieces.
tags: [decision-rule, decomposition, splitting]
sources: [humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
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

The choice was wrong if every piece of the chosen split turned out to be needed and was done in the order cut, when a rejected split would have exposed a piece to drop. It was also wrong if the pieces estimated as equal lived very different times, which board history shows.

## Agent executor note

The evidence is coaching experience with human teams, with no measurement. Both tests concern a decision made by whoever steers, so they survive an agent executing. The authors' "Product Owner" here is the person steering.
