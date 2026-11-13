---
title: All Work to Finished Is in the Plan
category: task-content
summary: A plan names everything between a story and a working, tested, documented result, and nothing that does not add value to this project; work kept off the plan by habit stays there only if the executor really has the habit.
tags: [rule, task-content, acceptance, iterations, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# All Work to Finished Is in the Plan

A plan is complete when following it produces a finished result and when it holds nothing else. Cohn gives both edges, at the level below this wiki's task ([[unit-of-work]]). This wiki carries them to what a task's scope and acceptance must cover.

## The upper edge: everything needed

> All tasks necessary to go from a user story to a functioning, finished product should be identified.
>
> — [[cohn-agile-estimating-planning]], L3180

Cohn includes analysis, design and user interaction design, and adds testing and documentation because each iteration aims at a potentially shippable product ([[potentially-shippable-increment]]). His reason for test tasks is timing: the team must think about how a story will be tested at the start (L3180). Tasks should also stay traceable to their story (L2995).

## The lower edge: only this project's value

Cohn sets the limit as "The iteration plan should only identify those tasks that add immediate value to the current project." (L3184). He excludes "answer email, 1 hour" and a meeting on a new annual review process, because neither is directly about developing the product (L3184-L3186).

Meetings about the project do count: "You should identify, estimate, and include tasks for meetings related to the project." (L3196). The estimate sums all participants plus preparation, so seven people for an hour plus two hours of preparation is nine hours (L3196).

Cohn lists "participating in meetings" among the activities not shown on task cards at L3307, which appears to contradict L3196. This wiki reads the two together: project meetings go on the plan, and meetings unrelated to the project do not. The planned hours on [[iteration-capacity]] follow from that.

## Explicit until it is a habit

Cohn has new teams write unit testing as its own task, then fold it into the coding task once it has become routine: "Once something like unit testing becomes a habit, it can be included within another task. Until then, however, making it explicit helps keep awareness of the task high." (L3192).

## The rule, at this wiki's level

The transfer here is ours. A task's scope and acceptance must reach a finished result, including the tests and documentation the project's standard of done asks for, and must not contain work that serves something other than this project. Whether a defect found along the way belongs to that work is on [[defect-inside-or-outside-the-iteration]].

## Sign of violation

These signs are this wiki's.

- **In task text:** acceptance stops at code being written, with no statement of how it is tested, where tests are part of done.
- **In board history:** tasks reopened or extended for testing or documentation that was foreseeable when they were written.
- **In board state:** items on the board that no task or goal needs, such as recurring administrative work.

## Trade-off

A complete list costs writing and reading time, and the charter's own limits apply: expanding a task into steps is out of scope. The list belongs in what a task must achieve and not in how to do it.

## Failure of the list itself

Cohn's example breakdown contains "Get user interface feedback from coaches" as an ordinary task (L3170). This wiki reads that as a wait sitting inside the work, which its own working test would cut at ([[sequence-versus-wait]]). Cohn does not treat it as a problem, because his tasks are made for a team and not for an executor that must finish without waiting.

## Agent executor note

The habit clause does not transfer. It relies on memory and routine, and an executor guessing from text has neither, unless the project's standing instructions carry them. This wiki therefore reads the default as permanent explicitness: what a human team may stop writing down stays written, in the task or in project instructions. Meeting hours and email belong to people and matter only as a deduction from what the people steering can spend ([[iteration-capacity]]).

## Related

The check at the end of the work is on [[testable-acceptance]]. What the commitment covers is on [[commitment-over-a-period]].
