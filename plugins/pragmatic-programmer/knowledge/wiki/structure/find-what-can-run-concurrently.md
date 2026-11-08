---
title: Find what can run concurrently
category: structure
summary: "Sequential statements or awaits in one function, some waiting on a database, a service or a user, some doing independent heavy computation: separate real dependencies from written order, then decide per step between concurrency, parallelism or leaving it sequential."
tags: [method, concurrency, parallelism, ordering]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A procedure for telling apart the order a procedure is written in from the order it actually needs, and for deciding where overlap pays. It rests on the book's distinction: concurrency means pieces of code behave as if they run at the same time, in an environment able to switch between them, while parallelism means they really do run at the same time, on hardware able to do so (p. 213). The book sums this up by calling concurrency a software mechanism and parallelism a hardware concern (p. 217).

## Procedure

1. List the steps as written. The book models a workflow as an activity diagram: actions as rounded boxes, arrows to the action that can start next, a thick synchronisation bar crossed only when every action leading to it has finished. An action with no incoming arrow can start at any time (p. 216).
2. For each step, record what has to finish first, and nothing else. In the book's worked example a twelve-step recipe written as a strict sequence turns out to have five steps that can all start at once and three more that can then run together (p. 216). The book notes that seeing the real dependencies can be a revelation.
3. Do not stop at the diagram. It shows potential only and «ничего не говорят о том, стоит ли использовать параллельность» (p. 216). In the same example a person would need five hands to do all the first steps at once.
4. Look for waiting. The book says what is sought: «При этом мы надеемся найти действия, отнимающие время, но не время для выполнения нашего кода.» (p. 217). Its list is a database query, a call to an external service and waiting for user input. Each is a place for concurrency, because the processor would otherwise sit idle (p. 217).
5. Look for independent heavy computation. With several processors, work can be split up to cut total time. The ideal is pieces that wait for nothing from each other, and the typical pattern splits a large unit into independent parts, processes them in parallel and combines the results (p. 218).
6. Choose per step: waiting gives concurrency, independent heavy computation gives parallelism, and anything else stays sequential. This three-way decision is this wiki's own condensation of steps 4 and 5.

The book gives two cases for step 5. In its own publishing pipeline, each formula conversion took up to 500 ms and depended on no other formula, so conversions ran in separate processes and the results were gathered back into the book. The authors add that doing this exposed a number of concurrency bugs in the pipeline (p. 218). A compiler that builds modules in parallel shows the other shape: a module pauses when it needs another module's result, so dependencies can also surface during the work rather than before it (p. 218).

## Applying it to a function

This section is this wiki's own transfer from a workflow diagram to code. Read a sequence of statements as a data flow: for each statement, which names does it read that an earlier statement wrote? Statements with no such link are candidates. The check is incomplete, because two statements can share something no name shows, such as a file, the current directory or an environment variable. The hidden case is covered in [[shared-state-is-incorrect-state]].

## Limits

- The method finds opportunities and says nothing about safety. The book calls reliable implementation the hard part, which the rest of the chapter addresses (p. 219).
- The book calls pieces that wait for nothing from each other the ideal case, and its compiler still gains with dependent modules (p. 218). This wiki expects the gain to shrink as pieces wait on each other or need coordination.
- This wiki adds that a step whose duration is negligible does not repay the added reasoning, even if the graph allows it to overlap.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: definitions, p. 213; activity diagrams and the worked example, pp. 215-217; concurrency and parallelism opportunities, pp. 217-218; the hard part, p. 219.

This wiki's own: the condensed choice in step 6, the section on applying it to a function, the expectation about dependent pieces, and the last limit. Related: [[temporal-coupling]].
