---
title: Time-box quick debugging
category: debugging
summary: "Use when a debugging session has run far longer than the code took to write, or hours have gone into one approach with no progress: set a time limit for the current approach, then brainstorm alternatives and switch, to a brute-force method certain to converge, a rewrite of the fragment, or a design that removes the problem."
tags: [method, debugging, brute-force, time-box]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell observes that everyone prefers a risky guess that might find a defect in five minutes over a reliable method that will find it in half an hour; when the guess fails, finding the bug the easy way becomes a matter of principle, and hours turn into days (p. 537). He asks how often two hours went into debugging code that took 30 minutes to write, and answers that such code should have been rewritten rather than debugged (p. 537).

## Steps

1. **Before debugging a hard error, name one method that is certain to work** if you get stuck, even rewriting the code (p. 537).
2. **Set a time limit for quick-and-dirty debugging.** «Если вы все же решаете попробовать быстрый способ отладки, ограничьте его применение определенным интервалом времени» (p. 537).
3. **When it expires, accept that the defect is harder than it looked and switch to brute force** (p. 537).

## The same limit against stubbornness

Chapter 33 returns to the time limit from the side of character. McConnell counts persistence among the traits less useful in programming than they seem: in software it usually takes the form of mule-headed stubbornness, a persistent effort to make code work with one approach (p. 811). His summary is that if one approach does not work, it is time to try another (p. 811). He adds three points to the steps above:

- **Notice being stuck.** His example interval is 15 minutes («скажем») without progress, after which it is usually better to set the bug aside (p. 812). It is hard to tell when to step away, he says, but important to keep asking, and to ask especially when you feel confused (p. 812).
- **A limit is not a surrender.** Asking usually means setting time parameters. His example: «Если я не решу эту проблему с использованием этого подхода в следующие полчаса», spend ten minutes brainstorming other approaches and try the best of them for the next hour (p. 812).
- **Change the approach, not only the method.** His alternatives are to redesign the class, rewrite the code, or come back later (p. 811); to think of an approach that removes the problem altogether, rewrite the troublesome fragment from scratch, or return with a fresh head and let the subconscious work on it (p. 812). There is nothing noble, he says, in fighting a computer problem; avoiding it is better (p. 812).

The 15-minute and half-hour figures are the book's examples, not thresholds it asks anyone to enforce. This wiki adds that the rewrite option presupposes a fragment small enough to rewrite and a way to check the rewrite. Where neither holds, the change of approach should be a method from [[debugging-procedure]] or [[binary-search-debugging]] rather than a rewrite. This wiki also reads repeated guesses on one theory as the stuck approach itself, so switching from guessing to a systematic method counts as changing the approach.

## Brute-force methods the book lists

Methods that are tedious but certain to converge (pp. 536-537):

- a full review of the design and/or the defective code;
- throwing away a section and redesigning or recoding it, or the whole program;
- compiling with full debug information;
- compiling at the strictest warning level and fixing every warning (see [[do-not-silence-warnings]]);
- unit testing new code in isolation, and building and running an automated test suite;
- stepping through a large loop in the debugger until the error appears;
- adding print, display or logging statements ([[trace-statements]]);
- compiling with another compiler, running in another environment, or linking against libraries and running in environments that warn on suspicious behaviour;
- replicating the end user's full configuration;
- integrating new code in small pieces, each fully tested.

## Trade-off

The book gives the cost of this method: simple defects are found fast and hard ones take a little longer (p. 537). This wiki reads the gain as a bound: without the time limit, the cost of a hard defect has no ceiling.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.2, pp. 536-537. The method, the list and the trade-off are the book's, paraphrased except where quoted; the quotation was transcribed from the extracted text with line-break hyphens joined. Section 33.8, pp. 811-812: persistence as stubbornness, the 15-minute threshold, the half-hour example and the alternatives to one approach; that quotation was also transcribed from the extracted text. The link to [[trace-statements]], the reading of the trade-off, the limit on rewriting and the reading of repeated guesses as the stuck approach are this wiki's own. Related: [[programming-by-coincidence]].
