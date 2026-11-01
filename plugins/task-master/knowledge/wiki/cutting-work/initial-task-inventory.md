---
title: Initial Task Inventory
category: cutting-work
summary: A first pass that writes every likely task at a coarse level so that people see the shape of the work, walks the user's timeline to find them, and expects the list to grow; an entry is not yet a task.
tags: [method, decomposition, task-content, inventory, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Initial Task Inventory

An initial task inventory is a coarse list of the work a project is likely to need, written before anything is estimated or ordered. The method is from the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961). The session itself is a meeting and is out of scope. What this page keeps is what the list is for and how it is built.

## What "all" means

Asked whether the team must write all the stories, the coach answers "Yes. Kind of." (L5153). The purpose is a shared view and not a complete specification:

> The purpose of writing ‘all’ the stories today is so that we’re all aware—again, just at a high level—of what features are likely. This especially helps Sasha and Allan as they think about the architecture of the game and even how they’ll design the move engine.
>
> — [[cohn-agile-estimating-planning]], L5175

A list that never grows is treated as a warning: "Hopefully we do think of some additional stories later. Otherwise it means we’re not thinking creatively enough about the game." (L5175).

## How it is built

1. **Walk the user's timeline.** The team asks what a user wants before a game, during it and after it (L5179). In the chapter this produced 9, 13 and 4 entries (L5195-L5203, L5223-L5231, L5247-L5253), figures that belong to the fiction.
2. **Throw the frame away.** When someone notes that background music was listed under the wrong phase, the coach answers: "We won’t keep track of which stories happen before the game starts and which are during it. I’m just using that approach to help us think through what we need in the game." (L5213). The frame is for finding tasks and is not a property of them.
3. **Write first, estimate after.** "It will be easier if we write a bunch of stories first and then estimate them at the same time" (L5127-L5129). The reason is on [[story-points]].

## How fine to write

The list stays coarse on purpose, and coarseness is enforced in the opposite direction from usual. Undo and redo are written as two stories, and the coach says "Undo and redo are pretty small. We don’t need our stories to be that small. In fact, we should probably combine undo and redo." (L5153). The two cards are torn up and replaced by one (L5157-L5159).

This wiki reads the sign as follows. At the inventory stage, two entries so closely paired that one has no use without the other show writing too fine. Cutting comes later, on the schedule in [[when-to-split-a-task]], and the general move is [[combining-small-tasks]].

## What an entry carries

The template offered is "As a <user type>, I want to <goal> so that <reason>" (L5113), and the reason is optional: "we don’t always need a ‘so that’ clause. If it helps make the story more clear, use one. But it’s not worth worrying about, especially on a story like this one where it’s obvious why a user would want to do that." (L5167). This wiki reads that as agreeing with [[task-must-justify-itself]], which also rejects the missing field as a sign. That page's test still applies once an entry becomes a task someone will execute.

## Failure mode: an entry taken for a task

This wiki adds a failure the chapter does not name. Entries here are deliberately coarse and rely on conversation to fill in, as the estimating session shows when "What do we mean by this story" (L5285) has to be asked of a card written earlier in the same meeting. The sign is an inventory entry taken for execution unchanged.

## Trade-off

The list costs an up-front pass, and it invites treating coarse entries as a plan. The chapter pays the first cost to inform architecture. [[how-far-to-split-up-front]] gives the case where enumerating is the wrong move, because starting will teach what the work is.

## Agent executor note

These readings are this wiki's. The purpose survives for the people steering, since it is about seeing the shape of the work. The architecture reason also carries over: an agent working on one task sees none of the others, so the inventory has to be available to it as text if it is to inform design. The expectation that gaps get filled by talk does not transfer ([[recoverable-versus-task-only-facts]]), so what is fine as an entry is not yet fine as a task.
