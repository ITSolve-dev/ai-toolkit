---
title: Text Signs of a Compound Task
category: cutting-work
summary: Words in a task's title and text that suggest it holds several units; conjunctions, separators, generic terms, plurals and criteria that could each stand alone. A sign prompts a check that each part can be delivered on its own, and it does not prove the task must be split.
tags: [rule, decomposition, splitting, task-content]
sources: [kanban-playbook-right-sizing, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# Text Signs of a Compound Task

A task that holds several units often says so in its own words, so this rule can fire before the task reaches a board. The Kanban Playbook gives the signs:

> Look at the item title. "Build and launch" is two things. Look inside the description too. Words like "and," "or," "when," and "if" are signals. Slashes, commas, and dashes often hide the same problem. "Users can create an account and set notification preferences" is two items.
>
> — [[kanban-playbook-right-sizing]], L41

> The item says "build the onboarding experience." What experience? For which users? Getting specific reveals what is actually hiding inside.
>
> — [[kanban-playbook-right-sizing]], L45

The Playbook's third sign concerns criteria: "The item has four acceptance criteria. Each one can be built, delivered, and tested on its own. Each becomes its own work item." (L37).

## The rule

Read a task's title and text for the signs. When one fires, ask whether each part could be built, delivered and tested on its own. If so, split it with [[story-splitting-patterns]]. If not, keep it whole.

## Sign of violation

All of these are in the task text.

- **Conjunctions in the title or description:** "and", "or", "when", "if".
- **Separators:** slashes, commas and dashes joining things that could be separate.
- **Generic terms and plurals:** a word such as "experience", or a plural that covers several things that have not been named.
- **Criteria that stand alone:** acceptance criteria each of which could be delivered without the others.

The Playbook calls them "signals" (L41), and this wiki keeps that strength. A sign is a reason to look. "When" and "if" often state a condition inside one behaviour, and "and" can join two parts of a single result. The test is the one the Playbook applies to criteria at L37, delivered on its own, and the extension of it to the other signs is ours.

## Why

What breaks if the signs are ignored is the count, as [[hidden-wip-in-large-items]] describes. The Playbook adds a second mechanism:

> Every acceptance criteria you bundle into a single item adds compounding risk. If each AC has an 80% chance of moving through the system cleanly, a single item with three ACs has only a 51% chance of completing without getting stuck.
>
> — [[kanban-playbook-right-sizing]], L37

This wiki keeps the mechanism and not the numbers. An item that needs every one of several conditions to go well has more ways to stick. The arithmetic is correct, since 0.8 cubed is 0.512, but only if the criteria stall independently, which the page does not state. The 80% is a hypothetical with no data behind it, so 51% is not a finding, and neither figure is a threshold.

## Limit

This rule does not ask for fewer acceptance criteria. [[testable-acceptance]] asks a task to state what would show it done, and an agent needs that written down ([[conversation-moves-into-the-task]]). Several criteria describing one behaviour's edges are not a sign, since none could be delivered alone. Only criteria that stand alone are.

## Cost

Splitting too eagerly produces pieces with nothing to show. The Playbook says "Items that are too small deliver nothing on their own." (L16). Each piece has to pass [[vertical-slice]], or it is a [[component-task-masquerading]].

## Agent executor note

The signs are in the text, so they do not depend on who executes, and the plugin can check them directly. The source is unsigned and reports no measurement. An agent also will not object to a compound task, so nothing on the executor's side catches it. The Playbook's claim about risk is about items getting stuck on a human board, and no source here tests it for an agent.
