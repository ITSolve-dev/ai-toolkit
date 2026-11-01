---
title: Theme
category: ordering
summary: A set of stories or features grouped because together they give a user or customer something of value; it is the unit compared when the value of one small task cannot be estimated.
tags: [concept, ordering, prioritization, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Theme

A theme is a set of stories or features grouped because together they give a user or customer something of value. Cohn ([[cohn-agile-estimating-planning]]) uses it as the unit of comparison when the value of one small task cannot be estimated. Chapter 6 uses the same word for a unit of estimating ([[estimating-by-horizon]]); this page is about the value side.

## Why the unit exists

Cohn's reason is a limit on what can be judged:

> Unfortunately, it is generally difficult to estimate the value of small units of functionality, such as a single user story.
>
> — [[cohn-agile-estimating-planning]], L1688

His answer is to aggregate, and then compare stories and themes together: "Stories and themes are then prioritized relative to one another for the purpose of creating a release plan." (L1688). This wiki reads two things from that. Value is estimated at the size where a person can say what it is worth. And one list may hold both sizes, so a single task does not have to be forced into a group to be compared.

## What makes a good theme

Cohn gives one test: "Themes should be selected such that each defines a discrete set of user- or customer-valued functionality." (L1688). His SwimStats examples include tracking and viewing personal records, assigning swimmers to events and predicting a meet's score, and integration with handheld computers at the pool (L1690-L1696). This wiki notes that each one says what someone gets, and none of them names a part of the system.

A theme can be given a money value. Cohn's illustration sets ¤150,000 of new sales from handheld support against ¤200,000 from scoring a meet (L1706). These figures are invented for the example, and ¤ is his generic currency sign (L1728). His next sentence is the warning: "There is more to prioritizing, however, than simply considering the monetary return from each new set of features." (L1706). See [[prioritization-factors]], and [[financial-measures-for-themes]] for the comparison when money figures exist.

## Signs of a bad grouping

The source states no signs, so these are this wiki's derivation from the test above. Each raises a question and is not a verdict.

- A theme is named after a layer or component. Check whether it delivers anything by itself ([[component-task-masquerading]]).
- Most tasks in a theme could be dropped and its stated value would still arrive. The value then belongs to a smaller group.
- A value rating sits on many small tasks and the ratings all read alike. They were probably rated at a size where no difference could be seen, which is the difficulty Cohn names.

## Scale and agent executor note

Cohn writes for a team led by a product owner (L1688). With a few people steering, that role falls to the person steering. This wiki reads the concept as concerning the result and not the executor, so it survives an agent executing. A plugin can propose groupings from task texts, but what a theme is worth is a task-only fact ([[recoverable-versus-task-only-facts]]), so the person confirms it.
