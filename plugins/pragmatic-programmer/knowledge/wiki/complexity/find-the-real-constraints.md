---
title: Find the real constraints
category: complexity
summary: "A method for code that turned out harder than expected, with a growing pile of special cases: list what was tried, state what ruled out each path, and test whether each constraint is real. With no cause you can write down, use prototype-when-code-resists."
tags: [method, constraints, problem-solving, accidental-complexity]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Find the real constraints is a method for a problem that seems unsolvable, or for «фрагмент кода, написать который оказалось труднее, чем вы думали» (p. 307). *The Pragmatic Programmer* holds that such difficulty often comes from a constraint nobody checked, and that the way out lies in sorting real limits from assumed ones, not in harder attempts along the same path.

This wiki selects the method by whether the difficulty can be written down. Special cases that each serve a constraint make it this page. A change that keeps fighting back with no cause anyone can name is [[prototype-when-code-resists]].

## The idea

The authors state the secret of any puzzle as being to «выявить настоящие (а не мнимые) ограничения и найти решение с их учетом» (p. 308). Some constraints are absolute and must be honoured however awkward they are. Others are only preconceptions (p. 308). People keep repeating an approach that has plainly failed (p. 307).

The book rejects the fashionable slogan about thinking outside the box. If the box is the boundary of constraints and conditions, the task is to locate it, and it may be much larger than it first seems (p. 308). Its tip reads: «Вместо того чтобы мыслить нешаблонно, находите шаблон» (p. 308).

## Procedure

The first four steps are the book's (pp. 308-310).

1. List every path already tried or considered, dismissing none, however useless or absurd it looks.
2. Go through the list and explain why each path cannot be taken. Then ask: «Насколько вы в этом уверены и сможете ли вы это доказать?» (p. 308).
3. Sort the constraints by category and priority. As a carpenter cuts the longest piece first, «требуется выявить сначала самые жесткие ограничения и подогнать под них все остальные» (p. 309).
4. Ask the questions a colleague would ask, among them: why this problem is being solved at all, what solving it gains, «Связаны ли возникшие у вас трудности с крайними случаями? Можно ли их исключить?» (p. 310) and «Есть ли более простая родственная задача, которую вы могли бы решить?» (p. 310).

The book treats the last set as an instance of the rubber duck technique (p. 310); this wiki records that technique in [[debugging-procedure]].

## Running it on code

The application to code is this wiki's own.

When a function collects special cases, write down the constraint each case serves. Typical candidates are a signature that must not change, an order that must be kept, a call that must be synchronous, or data that must stay in its present shape. For each one, look for its evidence: a test, a caller, a contract, an external format. A constraint with evidence is absolute for this change. A constraint with none is a candidate preconception, and removing it often removes the cases that depend on it.

The proof the book asks for has a cheap form here: delete the assumption in a throwaway change and run the tests. See [[small-steps-with-feedback]].

## Limits and failure modes

The points below are this wiki's own.

- A constraint can be real without showing in the code, as with a regulator's demand or an unstated expectation of a caller outside the repository. Absence of evidence in the repository makes a constraint questionable, not false, so the expert reports it and does not silently remove it.
- Listing paths has a cost. For a problem that yields to a direct attempt, the method is overhead; it is meant for the moment after the obvious fix has failed.
- The method can find that the real answer is to narrow the task, as with excluding an edge case. That is a decision for whoever owns the requirement.

## Source

[[pragmatic-programmer]]: Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, pp. 307-310. The book's advice to step away from the problem and let the unconscious work (p. 309) is left out: it has no sign in code. This wiki's own: the condition selecting between this page and [[prototype-when-code-resists]], the section *Running it on code*, and the limits and failure modes.
