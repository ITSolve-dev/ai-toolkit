---
title: Find the Core Complexity
category: cutting-work
summary: The meta-pattern behind the splitting patterns, used directly to find a first slice; locate what is most likely to surprise, list what there are many of, and reduce those to one.
tags: [method, decomposition, splitting]
sources: [humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# Find the Core Complexity

This is the move the Humanizing Work authors say underlies their [[story-splitting-patterns]], usable on its own: "focus on the complexity and reduce the variations through it" (L313). The authors recommend it for one job in particular: "This approach works particularly well for the first slice of a new thing because it goes straight for the core complexity and avoids anything else that would make the work bigger." (L321).

## The procedure

1. **Find the core complexity.** The authors ask what part is most likely to surprise you. Their guidance on where to look:

> What’s the part that’s most likely to surprise you or have something emerge? It’s often the part that depends on human preferences or behavior. Sometimes, it’s the part with a new integration or external dependency.
>
> — [[humanizing-work-splitting]], L315

2. **Identify the variations.** The authors list "Business rules, user types, interfaces, data variations, entities, etc." (L316).
3. **Reduce all the variations to one.** The authors define that as "a single, complete slice through the complex part" (L317), which may be a single scenario or a range of scenarios through one business rule variation.

## When to use it

This wiki's use for it is the case [[how-far-to-split-up-front]] marks as complex, where one or two slices are wanted and not a full list. The first slice then runs through the part most likely to surprise, because that is the part that teaches the most.

## What would show it wrong

The first slice was chosen wrongly if the surprise came from somewhere else, that is, if the tasks that had to be rewritten after it were outside the part it covered. That test is this wiki's, and the authors do not state one.

## Agent executor note

The evidence is coaching experience with human teams, with no measurement. The method survives an agent executing, because it reads the request and not the executor. The source of surprise it names, "human preferences or behavior" (L315), lies with the people steering, which makes that part harder for an agent to guess.
