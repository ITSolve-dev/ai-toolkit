---
title: Testable Acceptance
category: task-content
summary: A task states what would show it done in a form that can be checked; a requester who cannot say how to test it is a sign with three possible diagnoses.
tags: [rule, task-content, acceptance-criteria, invest, smart]
sources: [wake-invest, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# Testable Acceptance

A task is acceptable only if someone could decide from its text whether it is done. Wake's Testable and Measurable criteria make the same demand at two levels, the story and the task under it, so this wiki keeps them on one page.

> A good story is *testable*. Writing a story card carries an implicit promise: “I understand what I want well enough that I *could* write a test for it.”
>
> — [[wake-invest]], L76

For the task level Wake asks: "The key *measure* is, “can we mark it as done?” The team needs to agree on what that means, but it should include “does what it is intended to,” “tests are included,” and “the code has been refactored.”" (L102).

The Humanizing Work authors state what a passing answer looks like: "We should have some way to know we’re done with the story. It can’t just be a vague aspiration, but needs to be a concrete change in system behavior." (L123).

## The rule

The task text states what would show it done, as a concrete change in behaviour. A non-functional requirement states the same thing as a check. Wake says "A team can treat non-functional requirements (such as performance and usability) as things that need to be tested" (L80), and the authors show the form in their deferred-performance split, where the second story ends "(in under 5 seconds)" ([[humanizing-work-splitting]] L293).

A spike is the one exception to the demand for a change in behaviour: its acceptance criteria are questions ([[spike-as-last-resort]]).

## Sign of violation

- **In task text:** the outcome is an adjective with no threshold ("fast", "usable", "secure"), or two readers could disagree on whether it has been met. This wording of the sign is this wiki's, drawn from Wake's L80.
- **In the requester's answer:** asked how the result would be checked, the requester cannot say. Wake supplies this sign, and it has three different causes:

> If a customer doesn’t know how to test something, this may indicate that the story isn’t clear enough, or that it doesn’t reflect something valuable to them, or that the customer just needs help in testing.
>
> — [[wake-invest]], L78

This wiki reads those three causes as three different next steps: clarify the request, question whether it should exist, or propose a check for the requester to confirm.

A criteria field that is merely empty is not a sign under the charter. The two signs above can both fire on a filled-in field.

## Why

What breaks is the ending. Without a check, "done" is whatever the executor stopped at, and the disagreement surfaces at review or later. The authors name the same failure in a sharper form, for work that was split: "It’s easy to get in a habit of calling stories done that aren’t really done, accumulating debt you’ll pay for later." (L297). They also use acceptance criteria as a tool for holding a task's size: "You’ll probably have to define some acceptance criteria on the spot to keep it simple." (L275).

## Agent executor note

This rule survives and matters more with an agent. Wake's team could settle what "done" means by talking; he says the team "needs to agree" (L102). An agent stops at whatever its own reading of the text allows, so the agreement has to be on the page before work starts. Both sources speak from human teams, and neither reports a measurement for it.
