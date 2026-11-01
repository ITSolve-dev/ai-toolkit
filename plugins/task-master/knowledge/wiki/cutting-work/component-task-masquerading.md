---
title: Component Task Masquerading as a Unit
category: cutting-work
summary: A work item that changes one layer or produces an artifact, presented as a unit of value; the remedy is to combine it with its neighbours, because cutting it smaller cannot help.
tags: [failure-mode, decomposition, vertical-slice]
sources: [humanizing-work-splitting, wake-invest]
created: 2026-11-01
updated: 2026-11-01
---

# Component Task Masquerading as a Unit

A component task is a work item that changes one layer or produces an artifact, written as though it were a unit of value. It fails the charter's second working test ([[unit-of-work]]): it has nothing to present on its own. The opposite shape is a [[vertical-slice]].

## Observable signs

- **In task text:** the wanted thing is a layer, a component or a document and not a change in behaviour. Wearing the story template does not help:

> Sometimes we come across tasks or components pretending to be a story. Even if you use magic words like, “As a developer, I want a database diagram, so that I know what the structure of the database is going to be,” it’s still a task.
>
> — [[humanizing-work-splitting]], L105

- **Across tasks:** a request is cut by layer. The authors say "one story for the UI, another for the database, etc. This may satisfy small, but it fails at independent and valuable." (L143).
- **At cutting time:** the item cannot be split. The authors report that "When people bring us their “unsplittable” stories, they turn out to be tasks or components masquerading as stories." (L183).

## What to do with one

Do not cut it further. Combine it:

> If you start with something that isn’t an increment of value, there’s no way to slice it smaller and get an increment of value. In this case, the next move is to combine the non-story with the other pieces such that, together, they represent an increment of value.
>
> — [[humanizing-work-splitting]], L183

This wiki reads that as the rule's central move, because it runs against the plugin's default direction: a task that fails the cut gets bigger, not smaller, and the [[size-ceiling]] then decides whether the combined result needs a different cut.

## Limit

Wake does not forbid technical work. He says "Developers may have (legitimate) concerns, but these framed in a way that makes the customer perceive them as important." (L58). This wiki reads that as: a technical need is valid when it is stated in terms of the result it serves, which is also how [[task-must-justify-itself]] tests it.

## Agent executor note

The evidence comes from coaching human Scrum teams, with no measurement. The defect survives an agent executing, for a reason on the reviewer's side: a person steering an agent has nothing to judge in a result that shows no behaviour. This wiki also notes that an agent will complete a component task as readily as any other, so nothing on the executor's side will push back on the cut.
