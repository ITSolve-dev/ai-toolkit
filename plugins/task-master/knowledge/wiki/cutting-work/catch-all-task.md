---
title: Catch-All Task
category: cutting-work
summary: A task named by a broad quality is several unrelated pieces of work under one adjective; ask for the list, cut what can stand alone, and leave what only exists inside other work where it arises. The same words can still serve as a theme.
tags: [failure-mode, decomposition, task-content, text-sign, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Catch-All Task

A catch-all task names a quality of the whole product and not a piece of work. Its title reads well and it cannot be finished, since nothing says what it contains. The case comes from the fictional story-writing session in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

The card reads "As a player, I’d like the appearance of the game to be aesthetically pleasing" (L5477). The lead architect objects: "It’s kind of vague and it’s big." She names a neighbouring card she does like, the choice of wooden or metal board and pieces, and asks "What else did we mean by ‘aesthetically pleasing’?" (L5481).

## Sign

**In task text:** the title's substance is a broad adjective applied to the whole product, with no named thing it changes, and asking what it means returns a list. The wording of this sign is this wiki's, and it extends the architect's two words, vague and big.

The sign raises a question and does not settle it. A quality with a threshold is a legitimate task ([[testable-acceptance]]).

## What to do

Ask for the list, then sort each item by whether it can stand alone. The product manager's answer contains four things: menus that look good and sit in logical places, a splash screen, the board and pieces, and background art (L5483-L5487). They go three ways.

- **Stands alone:** the splash screen and background art become separate tasks, at 5 points each (L5491-L5493, L5547-L5548).
- **Already a task:** the board and pieces are the existing wooden-or-metal story, at 8 (L5558).
- **Exists only inside other work:** menus are not cut out. "I think the menu items need to be developed in the context of whatever features introduce the need for a new menu or menu item." (L5491).

The original card does not appear in the final list (L5535-L5577).

## The discriminating criterion

The third outcome is the useful one. This wiki reads it as the test separating a piece of a catch-all from a property of other tasks: an item that only comes into being because some other feature needs it travels with that feature, and giving it its own task produces work with no definition of its own. The chapter gives the one example and does not state the test. It leaves a cost: the concern now lives in many tasks at once, and nothing holds menu quality as a whole.

## A catch-all as a task and as a theme

The same words return later in the chapter. The analyst groups the art stories for her questionnaire: "‘aesthetically pleasing’ in that table covers the three stories we had about nice graphics, a splash screen, and the ability to change the board and pieces between a metal look and a wood look." (L5968). This wiki reads that as the line between the two uses. The phrase fails as a task and works as a [[theme]], since a theme is only a name over tasks that exist.

## Why

What breaks is estimating and ending. This wiki reads the architect's objection as saying the task's number would be a guess at a list nobody has written, and its result could not be presented once, which is the charter's test on [[unit-of-work]]. Compare [[compound-task-text-signs]], for tasks whose parts are visible in the text. The parts of a catch-all are hidden behind one adjective, so its conjunction sign does not fire.

## Agent executor note

This matters more with an agent, in this wiki's reading. A person would ask what was meant. An agent given such a title may choose its own list and stop there ([[underspecified-task]]). The sign reads from text alone, so the plugin can raise it before the task reaches a board. No source tests this.
