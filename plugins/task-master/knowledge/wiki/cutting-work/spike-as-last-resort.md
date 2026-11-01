---
title: Spike as a Last Resort
category: cutting-work
summary: A time-boxed investigation is the right cut only when a task is large because its implementation is poorly understood and no other split applies; its acceptance criteria are questions.
tags: [decision-rule, decomposition, estimation, splitting]
sources: [humanizing-work-splitting, wake-invest]
created: 2026-11-01
updated: 2026-11-01
---

# Spike as a Last Resort

A spike is a time-boxed investigation cut out of a task so that the rest of the task can be estimated, implemented or split. Wake describes the move as splitting a story "into a (time-boxed) “spike” that will give the team enough information to make a decent estimate, and the rest of the story that will actually implement the desired feature" (L66). The Humanizing Work authors add when to do it and how it ends.

## The decision

Cut a spike only when both of these hold:

- The task is large because its implementation is poorly understood, not because it is complex. The authors say that "no amount of talking about the business part of the story will allow you to break it up" (L301).
- The other eight [[story-splitting-patterns]] do not apply.

The authors put the second condition strongly, and their reason is the rule's because:

> The spike split is last because it should be your last resort. You probably know enough to build something. Do that, and you’ll know more. So, make every effort to use one of the previous eight patterns before resorting to the spike pattern.
>
> — [[humanizing-work-splitting]], L309

## How a spike is written

> In the “investigate” story, the acceptance criteria should be questions you need answered. Do just enough investigation to answer the questions and stop; it’s easy to get carried away doing research.
>
> — [[humanizing-work-splitting]], L307

This wiki reads that as the difference between a spike and a vague task: a spike has a stated end, which is that the questions have answers.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Why the task is large | The task text: does anyone know how it would be built |
| Whether another pattern applies | A pass through [[story-splitting-patterns]] |
| The questions the spike must answer | The unknowns stated in the task |

The choice was wrong if the answers could have come from building a thin slice, which shows up when the spike's result is code that survives into the implementation. It was also wrong if the spike ended without answering its questions and the task was no easier to size.

## Sign of a malformed spike

- **In task text:** a task named "investigate" or "research" that describes an area to look into and not questions to answer. It has no end.
- **In board history:** a spike that outlives its time-box, which both sources require (Wake L66, Humanizing Work L301).
- **In board state:** a finished spike that produced no implementation task and no decision to drop the work. It may have been a substitute for deciding.

These signs are this wiki's, drawn from the authors' L307.

## Agent executor note

The evidence is the practice of human teams, with no measurement. Wake's reason, producing "a decent estimate" (L66), concerns a team that needs a number for planning; the authors' reason, resolving uncertainty, holds for any executor. "You probably know enough to build something" (L309) is said to human developers and is this page's least tested claim for an agent.

## Related

A spike that runs past its limit falls under [[overrun-triggers-a-recut]]. The case for a spike usually arises from [[size-ceiling]].
