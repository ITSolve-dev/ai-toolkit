---
title: A Task Must Justify Itself
category: task-content
summary: A task states why it exists and how it contributes to the larger result; a reason that only restates the action, or pieces that do not add up, is the sign it does not.
tags: [rule, task-content, purpose, smart]
sources: [wake-invest, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# A Task Must Justify Itself

Every task has to be explainable in terms of the result it serves. This page takes Wake's "Relevant" and "Specific" task criteria up one level, from his sub-story tasks to this wiki's unit ([[unit-of-work]]). The transfer is this wiki's, and Wake applies them only to tasks inside a story.

> Every task should be *relevant,* contributing to the story at hand. Stories are broken into tasks for the benefit of developers, but a customer should still be able to expect that every task can be explained and justified.
>
> — [[wake-invest]], L110

Wake gives the matching test for a set of pieces under "Specific". His reason for being specific is: "This helps keep other tasks from overlapping, and helps people understand whether the tasks add up to the full story." (L98).

The Humanizing Work authors ask the same of a story with three questions:

> 1. **Who** is it for?
> 2. **What** do they want to do—or have the system do—that’s not possible today?
> 3. **Why** do they want this?
>
> — [[humanizing-work-splitting]], L85-L87

## The rule

A task states what it contributes to, and the tasks cut from one request add up to that request. A reader must be able to answer who it is for, what changes and why. Those answers need not be in a template or in separate fields, and the authors are explicit on both counts:

> The important thing isn’t the template, though. It’s answering the three questions.
>
> — [[humanizing-work-splitting]], L89

The authors then show that an answer may live outside the task. A title can carry the "what", and "The “who” is often provided by a product or release vision that describes a core target customer. If the story is for the target customer, we won’t repeat ourselves." (L91). Their short form is a title plus a reason, as in "**Find by Exact Title**" with "because I know the specific book I want, and I want to avoid noise in the search results" (L101-L103).

This wiki reads that as support for the charter's rejection of a missing field as a sign: the authors' good story has no "who" field on purpose.

## Sign of violation

- **In task text:** the stated reason restates the action ("add caching in order to have caching"), so removing it would lose nothing.
- **In task text:** the template is filled and the beneficiary is the implementer, as in "As a developer, I want a database diagram" (L105), which the authors call "magic words" (L105). See [[component-task-masquerading]].
- **Across tasks:** the tasks cut from one request, all finished, would still leave part of the request undone, or would do something the request did not ask for.

Apart from the authors' "magic words", the wordings of the sign are this wiki's, drawn from Wake's L98 and L110. An empty purpose field is not on the list, since the charter does not accept a missing field as a sign.

## Why

What breaks is the executor's ability to resolve small choices the task did not foresee. A reader who knows why the task exists can decide them; a reader who has only the action cannot. This reasoning is this wiki's. Wake's stated reason is that a customer can expect an explanation (L110).

## Agent executor note

Wake's audience for the justification is a customer. An agent is a second reader of the same sentence, and it reads nothing else, so the claim survives with a wider audience. One allowance does not transfer directly: the authors can omit the "who" because a human team has absorbed the product vision (L91). An agent has absorbed nothing, so the vision has to be readable by it from somewhere. Neither source reports a measurement.
