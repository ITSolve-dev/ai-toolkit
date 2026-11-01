---
title: User Story
category: task-content
summary: A brief description of functionality as a user sees it, kept lightweight by deferring detail to conversation; that deferral is what does not carry over to an agent executor.
tags: [concept, task-content, requirements, human-mechanism]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# User Story

A user story is "a brief description of functionality as viewed by a user or customer of the system." ([[cohn-agile-estimating-planning]] L782). Cohn presents it as a lightweight way of stating requirements, and as one of the best ways to keep work aimed at user-valued features (L782). This wiki's word for the unit is "task"; the mapping between the two is on [[unit-of-work]], and what a good one looks like is on [[invest]].

## Form

Cohn says "User stories are free-form and there is no mandatory syntax." (L782). A useful shape is “As a <type of user>, I want <capability> so that <business value>.”, as in “As a book-buyer, I want to search for a book by ISBN so that I can find the right book quickly.” (L782).

This wiki reads the three slots as naming who it is for, what they can do, and why it matters. It reads the last slot as the one that lets a reader compare stories by value, and as the first to go missing ([[task-must-justify-itself]]).

## Why it is called lightweight

Cohn moves the weight and does not remove it: "the work to gather and document them is not all done upfront." (L784). The card is a beginning, and "each user story is accompanied by as many conversations between the developers and the product owner as needed." (L790). Written documentation may remain, "However, the focus is shifted dramatically from written to verbal communication." (L790).

This wiki reads the benefit as requirements not being over-specified before they are needed, which fits Cohn's point that users cannot know every detail in advance (L722).

## Agent executor note

This is a claim whose mechanism depends on a human executor, and this wiki reads it as not surviving in that form. The story works because a person can ask, and carries context from those conversations in memory. An agent executor works from the text it is given, so a card plus deferred conversation leaves gaps that it fills by guessing. [[conversation-moves-into-the-task]] holds the rule that follows.

What this wiki keeps is the just-in-time part: detail need not exist before the work is near, as in [[planning-horizons]]. What it does not keep is the expectation that detail lives in speech. By the time a story reaches an agent, the conversations' results must be in the task's text, chiefly as [[conditions-of-satisfaction]].

## Boundaries

This wiki reads the template as not being the concept: a task in the "As a…" shape with no real user or no real value is still not a story. It reads such a task as a technical task in costume, the sign on [[component-task-masquerading]] and under [[user-valued-features-over-tasks]].

Cohn's framing assumes a reachable product owner. In a setup of a few people steering an agent, this wiki reads that person as the one holding the answers, and asks that they are written down before execution starts.
