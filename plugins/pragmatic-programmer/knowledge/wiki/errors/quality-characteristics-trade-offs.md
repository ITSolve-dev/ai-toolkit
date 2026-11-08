---
title: Quality characteristics and their trade-offs
category: errors
summary: "Concept: quality goals conflict; code tuned for correctness halts on bad input, code tuned for robustness carries on, and code written with no stated priority optimizes whatever the request happened to stress."
tags: [concept, quality, correctness, robustness, trade-off]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Quality characteristics** are the properties by which software is judged good. McConnell splits them into **external** characteristics, which the user sees, and **internal** ones, which only programmers see, and shows that some of them work against each other. This wiki keeps the concept because an agent writing or reviewing code is choosing among these characteristics whether it says so or not. The conflict that shows most often in code is **correctness versus robustness**.

## The two lists

External characteristics (pp. 456-457): correctness, usability, efficiency, reliability, integrity, adaptability, accuracy, robustness. Two pairs are easy to confuse.

- *Correctness* (корректность) means no defects in specification, design or implementation. *Accuracy* (правильность) means how free of error the outputs are, especially numeric ones. The book says accuracy concerns whether the system does its job well, not whether it was built correctly (p. 457).
- *Robustness* (живучесть) is defined as the system's ability to keep working on invalid input or under stress: «способность системы продолжать работу при вводе недопустимых данных или в напряженных условиях» (p. 457).

Internal characteristics (pp. 457-458): maintainability, flexibility, portability, reusability, readability, testability, understandability. The book separates *readability*, which works at the level of individual statements, from *understandability*, which also covers how the whole system hangs together (p. 458).

The line between the two kinds is blurred. Code that is hard to understand or maintain is hard to fix, and that lowers correctness and reliability, which are external (p. 458). Users care only about the external list: «Пользователей беспокоит легкость работы с ПО, а не легкость его изменения» (p. 457).

## Characteristics interact in three ways

Figure 20-1 (pp. 458-459) shows that focusing on one characteristic can help another, hurt it, or leave it alone. The book's own example: «Стремление повысить корректность приводит к снижению живучести и наоборот» (p. 459). Adaptability and robustness, by contrast, help each other. The figure shows only typical relations, and a particular project can differ, so the book advises thinking about the specific target characteristics and whether each one helps or hinders the others (p. 459).

This wiki reads the correctness/robustness conflict as the source-level reason why one routine cannot both halt on invalid input and carry on past it. A routine has to pick one, and the right pick depends on the system. That choice in code is owned by [[robustness-versus-correctness]], with [[uniform-robustness-level]] and [[consistent-error-handling-strategy]] for keeping it consistent; this page supplies the general frame they rest on.

## People optimize what they are told to optimize

Weinberg and Schulman (1974, reported on pp. 461-462) gave five teams the same program and the same five objectives, but told each team to optimize a different one: minimum memory, clearest output, most readable code, most compact code, or least development time. Four teams came first on their own objective and the fifth came second. No team did well on every objective: the team told to minimise memory came fourth on code readability, and the team told to finish fastest came fifth on it (Table 20-1). The book concludes: «люди на самом деле делают то, о чем вы их просите» (p. 462), and that conflicting goals make it nearly impossible to excel at all of them.

The following application is this wiki's own, not the book's. An agent working on code is under the same pressure. If nobody states the priority (readability, speed, memory, or time to finish), the agent optimizes whatever its prompt happened to stress. This wiki reads it as: a review judges code against the priority that the brief or the project states, not against every characteristic at once. Code that was explicitly traded for speed is not a readability failure in itself; it owes the reader a comment saying that it made the trade and why ([[comment-why-not-how]]).

## Limits

- The relations in Figure 20-1 are typical, not laws. The book itself says a specific project can show a different relation (p. 459).
- The Weinberg-Schulman result comes from one 1974 experiment with five teams. This wiki reads it as showing that goals steer behaviour, not as a ranking of the goals.
- The book does not say which characteristic should win. This wiki takes that to be decided per system, for example by how much a wrong answer would cost compared with stopping.

## Related

- [[robustness-versus-correctness]] owns the choice of whether a routine halts or carries on.
- [[defect-detection-techniques-are-complementary]] covers how defects that lower these characteristics get found.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 20, via [[code-complete]]: definitions on pp. 456-458; Figure 20-1 and the correctness/robustness relation on pp. 458-459; the Weinberg-Schulman experiment and Table 20-1 on pp. 461-462. This wiki's own: the application to agents and stated priorities, the link to the error-handling pages, the reading that traded-off code should state its trade, and the limits other than the first.
