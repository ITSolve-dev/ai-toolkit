---
title: Signs of Poor Flow
category: reading-history
summary: Vacanti's checklist of behaviours that point to a lack of flow, turned into what each looks like in task text, board state or board history; each sign is a question for the people steering, and one row can only be asked.
tags: [method, audit, failures, flow, board-history]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Signs of Poor Flow

Vacanti gives a list of questions that a reader should test against their own process, and he calls the behaviours "symptomatic of something seriously wrong with your process" ([[vacanti-actionable-agile-metrics]] L408). His diagnosis is that "the thing that really ails you is a lack of flow" (L408).

The source's questions are put to people, and the plugin reads a board. So this page turns each into a reading. The question column is the source's (L400-L406). The reading column is this wiki's, and none has been tested on a real board.

## Procedure

Run each row against recent history. Treat a hit as a question under [[smell-is-not-a-finding]], and follow the linked page for what to check.

| Source's question | Reading | See |
|---|---|---|
| Asked to start new work before finishing old? | Starts exceed finishes over a span of weeks | [[wip-control]], [[starting-more-work]] |
| Asked to expedite on top of current commitments? | An item enters work ahead of the stated order while the dates and estimates of what it displaced stay unchanged | [[interrupting-started-work]] |
| Features started and then cancelled? Replacements cancelled too? | Items leave a started state without finishing, repeatedly, or a replacement for a cancelled item is itself cancelled | [[mid-period-change]] |
| Blocked work put aside to start something new? | A start happens while an earlier item sits stopped with nobody working on removing the block | [[blocked-work-counts-against-wip]], [[waiting-versus-blocked]] |
| Estimates ignore how many items will be in progress? | Not readable from a board. Ask whether a stated date assumed a level of open work | [[forecast-range-and-probability]] |
| Order of items in progress ignored? | Items started later repeatedly finish before older ones with no recorded reason. Tasks of different size also do this | [[starting-more-work]] |
| Scope or acceptance criteria added to items in progress? | The task's text or acceptance criteria change after its started point | [[related-changes-temptation]], [[testable-acceptance]] |
| “it is just bigger than we thought it was” or “it will get done when it gets done”? | An item's age runs well past the project's usual cycle time with no recut and no note | [[overrun-triggers-a-recut]], [[hidden-wip-in-large-items]] |

The source's ninth question, whether management's first response is overtime (L406), is dropped: it concerns managing people, and a board does not show it.

## Why it is a method and not a set of rules

The source says the list is partial: "I could list many more" (L408). It also gives no weights, so a single hit and five hits are not ranked. This wiki reads several hits on the same theme as stronger than one, and that is a judgement. The source's claim that "yes" to any question means "a good chance you have a large buildup of work" (L426) is a position and has no measurement behind it.

## Inputs

| Input | Read from |
|---|---|
| Start and finish timestamps | Board history |
| Stopped items and how long they stopped | Board state and history |
| Edits to task text after start | Task history, if the tracker keeps it |
| The stated order | Board state or project configuration |
| Declared exceptions and intended patterns | Project configuration, or an earlier answer from the people steering |

## Cost

The scan spends the attention of the people steering. A project with nothing declared gets every hit as a question, as [[smell-is-not-a-finding]] notes.

## Agent executor note

The behaviours are set by whoever starts and changes work, so most survive with the people steering in the source's role. Two take a sharper form with an agent, in this wiki's reading. Changing a task's text during a run alters what the run was given, so it can be compared with what the task said at the start. And a stuck run can be left and a new one launched at almost no cost, which makes the blocked-work row easier to fall into. The question about estimates needs a person's answer under any arrangement.
