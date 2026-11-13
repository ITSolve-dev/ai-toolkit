---
title: INVEST in Good Stories, and SMART Tasks (Wake)
category: task-content
summary: Bill Wake's 2003 article naming six characteristics of a good story and five of a good task; the origin of INVEST, with no measurement behind it.
tags: [summary, invest, smart, user-stories, extreme-programming]
sources: [wake-invest]
created: 2026-11-01
updated: 2026-11-01
---

# INVEST in Good Stories, and SMART Tasks (Wake)

This is the article in which Bill Wake introduced the INVEST acronym for user stories and applied the SMART acronym to the tasks under a story. Wake states the origin himself: "I developed the INVEST acronym, and wrote this article in April and August, 2003" (L120), with a postscript dated 2-16-2011 (L124). The raw file's `authors` field is empty; the name comes from the mail address at L31 and from [[humanizing-work-splitting]] L109, which credits "Extreme Programming pioneer Bill Wake".

## Thesis

Wake offers the two acronyms as memory aids, not as tests:

> The **INVEST** and **SMART** acronyms can remind teams of the good characteristics of each.
>
> — [[wake-invest]], L29

This wiki treats that wording as the limit of the source's authority. Wake gives a sign for few letters and a figure only for Small. The signs on the pages below are Wake's only where this wiki cites a line for them, and are otherwise this wiki's own.

## The setting the article assumes

Wake writes for an Extreme Programming team with a customer available during development. He cites Ron Jeffries for the three components of a story: "Cards (their physical medium), Conversation (the discussion surrounding them), and Confirmation (tests that verify them)" (L33). Every page drawn from this source therefore inherits a human executor who can talk to the customer while working. This wiki's executor is an agent steered by a few people, so each page says whether the claim survives that change.

The word "task" also means something different here. Wake's task is a piece a story is broken into "for the benefit of developers" (L110), which is smaller than this wiki's unit of work. [[unit-of-work]] fixes the vocabulary.

## What this wiki took from it

- The six letters and what each claims: [[invest]].
- Vertical slicing, the multi-layer cake: [[vertical-slice]].
- Size as a statement about understanding, and the figures with their setting: [[size-ceiling]].
- Independence and its visible sign in a conditional estimate: [[independent-tasks]].
- Testability, "can we mark it as done?", and non-functional requirements as things to test: [[testable-acceptance]].
- Relevance and whether the pieces add up: [[task-must-justify-itself]].
- Time-boxing as the trigger for a recut: [[overrun-triggers-a-recut]].
- The conversation his story depends on, and what happens to it with an agent: [[conversation-moves-into-the-task]].

## What this wiki dropped, and why

- "Several teams have reported that by requiring customer tests before implementing a story, the team is more productive" (L76). It asserts a size of effect with no mechanism and no observable, so it fails the practitioner-source test in the charter.
- **Achievable** (L106). It concerns whether a task owner is "up to the job" and XP's rule that anyone can ask for help, which is managing people.
- Wake's "change players" as a response to a hard task (L114). It is the same topic.
- The pidgin-language framing (L35). It describes what stories are for between customers and programmers and changes nothing the plugin outputs.
- The history of how the acronym was assembled (L126-L141). It records how a word was chosen, not what it means.

## How to read it

Read it as the origin of the vocabulary and for the reasoning behind each letter. It is not evidence that any letter improves outcomes, because it reports no data. The figures in it, "a few person-weeks" and "a few person-days" (L70), are descriptions of XP teams in 2003, not measurements.
