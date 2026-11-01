---
title: Spike as a Last Resort
category: cutting-work
summary: A time-boxed investigation is the right cut when a task is large because its implementation is poorly understood and no other split applies, and its acceptance criteria are questions; Cohn treats a spike as ordinary and pairs it with a placeholder, and where the unknown is the reach of a change in existing code it need not wait for the other splits.
tags: [decision-rule, decomposition, estimation, splitting, cohn]
sources: [humanizing-work-splitting, wake-invest, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Spike as a Last Resort

A spike is a time-boxed investigation cut out of a task so that the rest of the task can be estimated, implemented or split. Wake describes the move as splitting a story "into a (time-boxed) “spike” that will give the team enough information to make a decent estimate, and the rest of the story that will actually implement the desired feature" (L66). Cohn defines it as work done for knowledge: "A spike is a task included in an iteration plan that is being undertaken specifically to gain knowledge or answer a question." ([[cohn-agile-estimating-planning]] L3238). The Humanizing Work authors add when to do it and how it ends. Cohn adds a pairing and a trigger, and he does not share their last-resort condition.

## The decision

Cut a spike only when both of these hold:

- The task is large because its implementation is poorly understood, not because it is complex. The authors say that "no amount of talking about the business part of the story will allow you to break it up" (L301).
- The other eight [[story-splitting-patterns]] do not apply.

The authors put the second condition strongly, and their reason is the rule's because:

> The spike split is last because it should be your last resort. You probably know enough to build something. Do that, and you’ll know more. So, make every effort to use one of the previous eight patterns before resorting to the spike pattern.
>
> — [[humanizing-work-splitting]], L309

The second condition does not apply to one kind of unknown, which is set out under the section against the last-resort position below.

## Cohn's pairing

Cohn's case is a small change to a legacy feature, at the level below this wiki's task ([[unit-of-work]]). Nobody could think through all its impacts, the certain sections came to four hours, and if the uncertain sections were affected the figure could reach twenty (L3232). They wrote two tasks: "Determine what’s affected, 2 hours" and "Make the changes, 10 hours" (L3234-L3236). The second is "a placeholder with a guess at the duration", and the spike exists so that it can be estimated properly (L3238).

This wiki reads the pairing as useful for planning, because a board keeps showing that follow-on work exists and that its number is unsettled. A spike standing alone hides that. The placeholder should be re-estimated when the spike ends ([[size-ceiling]]).

Cohn's trigger is an impact that cannot be judged without looking at code: "We couldn’t be sure without looking at the code and we didn’t want to stop a planning meeting for that." (L3232). This wiki reads the unknown as the reach of a change, a specific case of the condition that implementation is poorly understood.

## Against the last-resort position

The resolution is this wiki's. Cohn presents the spike as ordinary, while [[humanizing-work-splitting]] puts it last. The two differ in the kind of unknown. Building a thin slice to learn fits new behaviour. It fits badly where the unknown is what an existing change will break, since a thin slice of a change to shared code still needs that answer first. So for reach-of-change unknowns in existing code, a spike need not wait until the splitting patterns are exhausted. For anything else the last-resort rule stands.

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
| What is certain and what is not | The task text and the code it touches |
| Range if the uncertain part is real | The estimator: Cohn's was 4 to 20 hours |
| Whether reading the code now is cheaper than a spike | The planner's own access to the code |
| The questions the spike must answer | The unknowns stated in the task |

The choice was wrong if the answers could have come from building a thin slice, which shows up when the spike's result is code that survives into the implementation. It was also wrong if the spike ended without answering its questions and the task was no easier to size, if the question could have been answered by reading the code during planning, or if the placeholder's estimate did not change after the spike.

## Sign of a malformed spike

- **In task text:** a task named "investigate" or "research" that describes an area to look into and not questions to answer. It has no end.
- **In board history:** a spike that outlives its time-box, which both Wake and the Humanizing Work authors require (Wake L66, Humanizing Work L301).
- **In board state:** a finished spike that produced no implementation task and no decision to drop the work. It may have been a substitute for deciding.
- **In board state:** a placeholder still carrying its first guess after its spike finished.

These signs are this wiki's, the first three drawn from the authors' L307 and the last from Cohn's pairing.

## Agent executor note

The evidence is the practice of human teams, with no measurement. Wake's reason, producing "a decent estimate" (L66), concerns a team that needs a number for planning; the authors' reason, resolving uncertainty, holds for any executor. "You probably know enough to build something" (L309) is said to human developers and is this page's least tested claim for an agent.

Cohn's reason for the spike over looking at the code is that a planning meeting should not stop. That reason falls away when a planner can read the code cheaply. This wiki therefore expects many impact questions to be answered during cutting, leaving a spike for what takes real work to find out. That expectation is this wiki's and is untested.

## Related

A spike that runs past its limit falls under [[overrun-triggers-a-recut]]. The case for a spike usually arises from [[size-ceiling]]. How much planning should find out before stopping is on [[planning-stops-at-guesses]].
