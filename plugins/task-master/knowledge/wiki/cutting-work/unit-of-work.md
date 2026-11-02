---
title: Unit of Work
category: cutting-work
summary: What this wiki means by a task, how that maps onto the sources' words story and task, and the two working tests a unit has to pass; Cohn's user story, a brief description of functionality as a user sees it with detail deferred to conversation, is the source form, and its deferral is the part that does not carry over to an agent.
tags: [concept, decomposition, vocabulary, task-content, requirements, human-mechanism]
sources: [wake-invest, humanizing-work-splitting, radzikowska-waiting-blocked, kanban-guide, scrum-guide-2020, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Unit of Work

A unit of work is the thing this wiki calls a **task**: the piece that goes on a board, is taken by one executor, and comes back as one result. The sources do not use the word that way, so every page in this wiki that reports a source keeps the source's word and every page that prescribes uses "task" in this sense.

## Vocabulary

| This wiki | Wake | Humanizing Work | What it is |
|---|---|---|---|
| task, unit of work | story | story, vertical slice | The unit that carries a result someone other than the implementer can look at |
| (not produced) | task | task, component | A piece of a story, made for the implementer's benefit, or an item with no observable result of its own |

The Humanizing Work authors define their unit by what it changes: a user story is "*a description of a change in system behavior from the perspective of a user*" (L53). Their use of "task" is pejorative where Wake's is neutral, which is why the two sources should not be merged by word: for Wake a task is a legitimate piece of a story, and for the authors a task "pretending to be a story" is a defect ([[component-task-masquerading]]).

The two guides use the same phrase at different levels, so the phrase cannot be carried over between them. The Kanban Guide's "work item" is "the individual units of value that are moving through the workflow" ([[kanban-guide]] L110). This wiki reads that as its own task, since it is what crosses the [[started-and-finished-points]]. The Scrum Guide's unit is the Product Backlog item, and its "work items" are the smaller pieces below that: it speaks of "decomposing Product Backlog items into smaller work items of one day or less." ([[scrum-guide-2020]] L226). This wiki reads a Product Backlog item as its own task, and the Scrum "work item" as Wake's task, which the plugin does not produce.

Wake separates the two levels plainly:

> Stories are broken into tasks for the benefit of developers, but a customer should still be able to expect that every task can be explained and justified.
>
> — [[wake-invest]], L110

This wiki reads the first half as a boundary on the plugin. Expanding a task into step-by-step instructions is outside the charter, so the plugin stops at the level Wake calls a story. Wake's task-level criteria are kept only where they transfer to that level, and each page that uses one says so.

## The working tests

The charter states two tests for a unit: once started, the task can be finished without waiting, and its result is presented once. These tests are the charter's own, written before any source was ingested. No source in this wiki states them in those words, so a page citing them cites the charter and not a source.

The second test has a close source statement in the Humanizing Work definition of a slice: "When you call the slice “done,” the system is observably more valuable to a user." (L133). This wiki reads a result that can be presented as a result of that kind. See [[vertical-slice]].

The first test has no source statement. This wiki reads board history as its evidence: a task that reached a parked or blocked state after starting did not meet it ([[sequence-versus-wait]], with the states defined on [[waiting-versus-blocked]]). A stop for a decision from the person steering counts too, which makes [[conversation-moves-into-the-task]] part of the same test. A planned review of the finished result does not count, because it is a handoff at the end of the executor's part and not a wait inside the task ([[sequence-versus-wait]]). That review is where the result is presented, which is the second test.

## A task that fails

- It has no result of its own: combine it, per [[component-task-masquerading]].
- It is too big: cut it, per [[size-ceiling]] and [[story-splitting-patterns]].
- It is too unknown to cut: see [[spike-as-last-resort]] and [[how-far-to-split-up-front]].
- It contains a known wait: cut at the wait, per [[sequence-versus-wait]].

## User Story

A user story is "a brief description of functionality as viewed by a user or customer of the system." ([[cohn-agile-estimating-planning]] L782). Cohn presents it as a lightweight way of stating requirements, and as one of the best ways to keep work aimed at user-valued features (L782). This wiki's word for the unit is "task"; the mapping between the two is on *Unit of Work* (above), and what a good one looks like is on [[invest]].

### Form

Cohn says "User stories are free-form and there is no mandatory syntax." (L782). A useful shape is “As a <type of user>, I want <capability> so that <business value>.”, as in “As a book-buyer, I want to search for a book by ISBN so that I can find the right book quickly.” (L782).

This wiki reads the three slots as naming who it is for, what they can do, and why it matters. It reads the last slot as the one that lets a reader compare stories by value, and as the first to go missing ([[task-must-justify-itself]]).

### Why it is called lightweight

Cohn moves the weight and does not remove it: "the work to gather and document them is not all done upfront." (L784). The card is a beginning, and "each user story is accompanied by as many conversations between the developers and the product owner as needed." (L790). Written documentation may remain, "However, the focus is shifted dramatically from written to verbal communication." (L790).

This wiki reads the benefit as requirements not being over-specified before they are needed, which fits Cohn's point that users cannot know every detail in advance (L722).

### Agent executor note

This is a claim whose mechanism depends on a human executor, and this wiki reads it as not surviving in that form. The story works because a person can ask, and carries context from those conversations in memory. An agent executor works from the text it is given, so a card plus deferred conversation leaves gaps that it fills by guessing. [[conversation-moves-into-the-task]] holds the rule that follows.

What this wiki keeps is the just-in-time part: detail need not exist before the work is near, as in [[planning-horizons]]. What it does not keep is the expectation that detail lives in speech. By the time a story reaches an agent, the conversations' results must be in the task's text, chiefly as [[conditions-of-satisfaction]].

### Boundaries

This wiki reads the template as not being the concept: a task in the "As a…" shape with no real user or no real value is still not a story. It reads such a task as a technical task in costume, the sign on [[component-task-masquerading]] and under [[vertical-slice]].

Cohn's framing assumes a reachable product owner. In a setup of a few people steering an agent, this wiki reads that person as the one holding the answers, and asks that they are written down before execution starts.
