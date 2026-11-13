---
title: Component Task Masquerading as a Unit
category: cutting-work
summary: A work item that changes one layer or produces an artifact, presented as a unit of value; it is often made when a feature resists splitting and gets cut into its development activities, and the remedy is to combine it with its neighbours, because cutting it smaller cannot help.
tags: [failure-mode, decomposition, vertical-slice]
sources: [humanizing-work-splitting, wake-invest, kanban-playbook-right-sizing, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Component Task Masquerading as a Unit

A component task is a work item that changes one layer or produces an artifact, written as though it were a unit of value. It fails the charter's second working test ([[unit-of-work]]): it has nothing to present on its own. The opposite shape is a [[vertical-slice]].

## How it gets made

Cohn describes the failure from the moment it is made, which is when a feature resists cutting:

> Sometimes we come across a feature that is difficult to split. In these cases it is tempting to split the feature into its constituent tasks.
>
> — [[cohn-agile-estimating-planning]], L2695

His word "task" means a development activity inside a story, so his warning is against promoting those activities to the level of this wiki's task. His own summary names that level: "the development tasks that will be necessary to implement the feature" (L2729). The wording is what can be misread: in this wiki a task is the unit on the board, and Cohn is not arguing against that.

## Observable signs

- **In task text:** the wanted thing is a layer, a component or a document and not a change in behaviour. Wearing the story template does not help:

> Sometimes we come across tasks or components pretending to be a story. Even if you use magic words like, “As a developer, I want a database diagram, so that I know what the structure of the database is going to be,” it’s still a task.
>
> — [[humanizing-work-splitting]], L105

- **Across tasks:** a request is cut by layer. The authors say "one story for the UI, another for the database, etc. This may satisfy small, but it fails at independent and valuable." (L143). Cohn's examples of what not to write are "Code the user interface" and "Write the middle tier" ([[cohn-agile-estimating-planning]] L2697, L2699). This wiki reads a list of cut tasks named after activities or layers as this defect.
- **At cutting time:** the item cannot be split. The authors report that "When people bring us their “unsplittable” stories, they turn out to be tasks or components masquerading as stories." (L183). This wiki reads an item cut by activity because nothing else seemed possible as the same case.
- **In board history:** tasks close fast and the numbers look healthy, while nothing usable reaches anyone. The Kanban Playbook describes this: "Small items create the opposite illusion. Work closes quickly and your Cycle Time looks great. But if nothing on your board delivers something a customer can actually use, feedback never arrives." ([[kanban-playbook-right-sizing]] L20). This wiki reads that as the same defect seen in the metrics, and it means [[flow-metrics]] cannot detect it alone, since short cycle times and high throughput are what the defect produces.

## What to do with one

Do not cut it further. Combine it:

> If you start with something that isn’t an increment of value, there’s no way to slice it smaller and get an increment of value. In this case, the next move is to combine the non-story with the other pieces such that, together, they represent an increment of value.
>
> — [[humanizing-work-splitting]], L183

This wiki reads that as the rule's central move, because it runs against the plugin's default direction: a task that fails the cut gets bigger, not smaller, and the [[size-ceiling]] then decides whether the combined result needs a different cut.

Cohn's remedy comes earlier in time: "Don’t split a large story into tasks. Instead, try to find a way to fire a tracer bullet through the story." ([[cohn-agile-estimating-planning]] L2707), which is a [[vertical-slice]]. This wiki reads his remedy and the combine move as one instruction seen from two points: before a cut, cut across the layers; after a cut was made by layer, combine the pieces and cut again with [[story-splitting-patterns]].

## Limit

Wake does not forbid technical work. He says "Developers may have (legitimate) concerns, but these framed in a way that makes the customer perceive them as important." (L58). This wiki reads that as: a technical need is valid when it is stated in terms of the result it serves, which is also how [[task-must-justify-itself]] tests it.

## Agent executor note

The evidence comes from coaching human Scrum teams, with no measurement. The defect survives an agent executing, for a reason on the reviewer's side: a person steering an agent has nothing to judge in a result that shows no behaviour. This wiki also notes that an agent will complete a component task as readily as any other, so nothing on the executor's side will push back on the cut.

Cohn's cause is a human habit: decomposing a feature into activities "is such a habit that we often do it without even being aware of it" ([[cohn-agile-estimating-planning]] L2695). Nothing in the chapter says an agent shares it. This wiki notes that the habit matters at the cut, which may be made by the plugin, so the sign has to be checked on the plugin's own output as much as on a person's.
