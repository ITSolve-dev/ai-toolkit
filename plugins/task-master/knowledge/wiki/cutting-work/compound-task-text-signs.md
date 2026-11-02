---
title: Text Signs of a Compound Task
category: cutting-work
summary: Words in a task's title and text that suggest it holds several units: conjunctions, separators, generic terms, plurals and criteria that could each stand alone; a task named by a broad quality of the whole product is the extreme case, answered by asking for the list and cutting what can stand alone. A sign prompts a check that each part can be delivered on its own, and it does not prove the task must be split.
tags: [rule, decomposition, splitting, task-content, failure-mode, text-sign, cohn]
sources: [kanban-playbook-right-sizing, humanizing-work-splitting, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
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

The Playbook calls them "signals" (L41), and this wiki keeps that strength. A sign is a reason to look. "When" and "if" often state a condition inside one behaviour, and "and" can join two parts of a single result. The test is the one the Playbook applies to criteria at L37, delivered on its own, and the extension of it to the other signs is ours. A title whose substance is one broad adjective hides its parts from these signs altogether, and that case is on *Catch-All Task* (below).

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

## Catch-All Task

A catch-all task names a quality of the whole product and not a piece of work. Its title reads well and it cannot be finished, since nothing says what it contains. The case comes from the fictional story-writing session in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

The card reads "As a player, I’d like the appearance of the game to be aesthetically pleasing" (L5477). The lead architect objects: "It’s kind of vague and it’s big." She names a neighbouring card she does like, the choice of wooden or metal board and pieces, and asks "What else did we mean by ‘aesthetically pleasing’?" (L5481).

### Sign

**In task text:** the title's substance is a broad adjective applied to the whole product, with no named thing it changes, and asking what it means returns a list. The wording of this sign is this wiki's, and it extends the architect's two words, vague and big.

The sign raises a question and does not settle it. A quality with a threshold is a legitimate task ([[testable-acceptance]]).

### What to do

Ask for the list, then sort each item by whether it can stand alone. The product manager's answer contains four things: menus that look good and sit in logical places, a splash screen, the board and pieces, and background art (L5483-L5487). They go three ways.

- **Stands alone:** the splash screen and background art become separate tasks, at 5 points each (L5491-L5493, L5547-L5548).
- **Already a task:** the board and pieces are the existing wooden-or-metal story, at 8 (L5558).
- **Exists only inside other work:** menus are not cut out. "I think the menu items need to be developed in the context of whatever features introduce the need for a new menu or menu item." (L5491).

The original card does not appear in the final list (L5535-L5577).

### The discriminating criterion

The third outcome is the useful one. This wiki reads it as the test separating a piece of a catch-all from a property of other tasks: an item that only comes into being because some other feature needs it travels with that feature, and giving it its own task produces work with no definition of its own. The chapter gives the one example and does not state the test. It leaves a cost: the concern now lives in many tasks at once, and nothing holds menu quality as a whole.

### A catch-all as a task and as a theme

The same words return later in the chapter. The analyst groups the art stories for her questionnaire: "‘aesthetically pleasing’ in that table covers the three stories we had about nice graphics, a splash screen, and the ability to change the board and pieces between a metal look and a wood look." (L5968). This wiki reads that as the line between the two uses. The phrase fails as a task and works as a [[theme]], since a theme is only a name over tasks that exist.

### Why

What breaks is estimating and ending. This wiki reads the architect's objection as saying the task's number would be a guess at a list nobody has written, and its result could not be presented once, which is the charter's test on [[unit-of-work]]. Compare *Text Signs of a Compound Task* (above), for tasks whose parts are visible in the text. The parts of a catch-all are hidden behind one adjective, so its conjunction sign does not fire.

### Agent executor note

This matters more with an agent, in this wiki's reading. A person would ask what was meant. An agent given such a title may choose its own list and stop there ([[underspecified-task]]). The sign reads from text alone, so the plugin can raise it before the task reaches a board. No source tests this.
