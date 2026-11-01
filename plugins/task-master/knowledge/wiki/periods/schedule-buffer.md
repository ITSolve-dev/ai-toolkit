---
title: Schedule Buffer
category: periods
summary: Protecting a firm date by planning from 50% estimates and adding one shared project buffer of time, so that the plan guards the overall deadline rather than each task.
tags: [method, planning-a-date, buffer, estimation, uncertainty]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Schedule Buffer

A schedule buffer is a block of time added once, at the end of a plan, to protect a date. "A buffer is a margin for error around an estimate" ([[cohn-agile-estimating-planning]] L3843); this kind is denominated in time and sits on the whole plan rather than on any task. It is the time-side counterpart of [[feature-buffer]], and [[choosing-a-buffer]] says when either applies.

## What it answers

A fixed date changes the question. Cohn's flight leaves regardless: "My expected arrival time and my rate of progress don’t matter to the airline" (L3871). Where the deadline does not move, reporting a forecast of arrival does not protect it. Only margin built in before starting does.

The plan protects "the only deadline that matters—the overall project deadline" (L3937). Whether any one activity runs long does not matter, only whether the chain does (L3873).

## Procedure

1. Give every item two estimates, 50% and 90%, before moving to the next item (L3956). Story points or ideal days both work (L3968). See [[completion-time-distribution]].
2. Sum the 50% estimates. This is the plan without [[local-safety]].
3. Size one project buffer from the spreads: [[project-buffer-sizing]].
4. Duration = sum of 50% estimates + buffer. Divide by forecast velocity to get iterations ([[deriving-duration-from-velocity]]).
5. Show the buffer as its own line and say how it was derived: [[buffer-versus-padding]].

In Table 17.2's six stories, 17 + 9 = 26 points. At a velocity of 9 per iteration that is three iterations rather than two (L3974, L3992). Adding a buffer "may or may not add one or more iterations", and "Most often it will" (L3992).

## Inputs and the fact that would show the choice wrong

- **Two estimates per item:** from the task or the estimation step.
- **Forecast velocity:** from board history, or a forecast where there is none ([[choosing-velocity-estimate-approach]]).
- **The date's firmness:** from whoever owns the date; the board does not show it.

This wiki reads the following as the disproving facts, which the chapter does not list. The buffer is expected to be consumed: Cohn's car-length analogy says "you fully expect to use up most of that buffer" (L4043). A date missed with the buffer gone suggests the estimates or the spreads were too narrow. A buffer left largely unused across several plans suggests the 50% figures were really pessimistic ones.

## Trade-offs and failure modes

- **Cost:** a second estimate per item and usually a later stated date. Cohn calls this "small extra work" (L4053), and does not spend it where no date needs protecting.
- **Applied to safe estimates:** "Adding a schedule buffer on top of already pessimistic, 90% estimates will result in an overly long schedule" (L4051).
- **Task-level chasing:** treating a task's 50% figure as a due date undoes the method; see [[local-safety]].
- **Too few items:** see the guidelines in [[project-buffer-sizing]].

## Limits

The chapter buffers a release date. It says nothing about holding capacity back inside one iteration; filling a period is [[filling-a-period]], and the margin there is [[utilization-versus-slack]]. Its summary (L4065) reads "feature buffer" and "a team’s size" in the sentences describing this method; the body of the chapter shows it means a schedule buffer and the size of the work.

The statistical case survives an agent executing, in this wiki's reading; the behavioural case does not transfer directly, as [[local-safety]] explains.
