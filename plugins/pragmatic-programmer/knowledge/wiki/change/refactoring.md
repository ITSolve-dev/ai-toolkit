---
title: Refactoring
category: change
summary: "A change is refactoring only if working code keeps its observable behaviour, its internal quality rises, and it proceeds in small steps that leave the code working after each; a broad rewrite, code broken for days, a behaviour change, a change for speed at the cost of clarity, or poking at broken code under that name is not."
tags: [concept, refactoring, change, behaviour-preservation, software-evolution, small-steps]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Refactoring is a disciplined restructuring of existing code that leaves its external behaviour unchanged. The book takes its definition from Martin Fowler: «дисциплинированная методика перестройки структуры существующего тела кода, изменение его внутренней структуры без изменения его внешнего поведения» (p. 260).

## What the definition excludes

The book picks out two parts as essential (p. 260):

- The activity is disciplined, not chaotic.
- External behaviour does not change, so no new features go in.

Rewriting, reworking and re-architecting code are together called restructuring, and refactoring is a practical subset of it (p. 260). This wiki draws a test from that: if observable behaviour changes, the work is not refactoring, and a diff mixing the two is [[do-not-refactor-while-adding-features]]. A changed meaning behind an unchanged signature is [[break-the-build-on-interface-change]].

The book says refactoring is not an occasional ceremony. It is a day-to-day activity, in small low-risk steps, using a targeted approach that makes the code easier to change, instead of a global rewrite (p. 261). The book also holds that refactoring is in essence redesign: anything designed can be redesigned in light of new facts, deeper understanding or changed requirements (p. 263).

*Code Complete* takes the same definition from Fowler (1999) and traces the word to Larry Constantine's "factoring", the fullest possible decomposition of a program into its parts (p. 553). It adds three exclusions:

- **Any change at all.** McConnell objects that the word is used for fixing defects, adding features and redesign alike; purposeful change can stop the entropy spiral, «но само по себе изменение достоинств не имеет» (p. 558).
- **Hacking on broken code.** «Рефакторинг — это изменение работоспособного кода, не влияющее на поведение программы» (p. 568). Programmers who poke at code that does not work yet, hoping it starts to, «занимаются хакерством» (p. 568). Refactoring is not an excuse to write bad code now and fix it later; the chapter quotes John Manzo against implementing a feature partially with the plan of finishing it through refactoring (p. 568).
- **A substitute for rewriting.** Some code cannot be improved in small steps and must be thrown away and redesigned. The book treats a large-scale refactoring as the signal to ask whether a rewrite is the honest choice, and quotes Kent Beck that large-scale refactoring is a road to disaster (p. 568).

## Fowler's own account

Fowler's 2nd edition gives the term two senses (ch. 2, PDF p. 56). The noun: "a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior". The verb: "to restructure software by applying a series of refactorings without changing its observable behavior". A named refactoring such as [[extract-function]] is one instance of the noun; a couple of hours of work stringing a few dozen of them together is the verb.

**Refactoring versus restructuring.** Fowler too treats refactoring as one kind of restructuring (PDF p. 57). What sets it apart is the size of the step: each refactoring is small or a combination of small steps, so the code spends little time broken and the work can stop at any moment. His test: "If someone says their code was broken for a couple of days while they are refactoring, you can be pretty sure they were not refactoring" (PDF p. 57). He claims the tiny steps are faster, not slower, because they compose and because no time goes into debugging (PDF p. 57). The step discipline itself is [[refactor-in-small-tested-steps]].

**What "observable behavior" allows.** Fowler calls the phrase deliberately loose (PDF p. 57). The call stack and the performance profile may change; Extract Function alters the call stack. Interfaces between modules often change, through Change Function Declaration or [[move-function]]. Bugs noticed during refactoring should still be present afterwards, though he allows fixing latent bugs nobody has observed yet. This wiki reads the last point as a practical rule: a bug found mid-refactoring is noted and fixed as a separate, behaviour-changing step, under the other hat ([[do-not-refactor-while-adding-features]]).

**Refactoring versus performance optimization.** Both manipulate code without changing what the program does. The difference is the purpose: refactoring always aims at code that is easier to understand and cheaper to modify, and may make it faster or slower; optimization aims only at speed and accepts harder code if the speed is really needed (PDF p. 57). How the two meet is on [[refactor-first-tune-afterwards]], [[code-tuning-procedure]] and [[premature-code-tuning]].

**The economic argument.** Fowler lists four benefits: design does not decay, code is easier to understand, bugs become visible, and development gets faster (PDF pp. 58-61). On duplication he notes that less code rarely makes a system faster but makes a big difference to modifying it correctly, because a change made in one place misses the near-copy elsewhere (PDF p. 58); see [[dry]]. On bugs: clarifying structure clarifies assumptions, "to a point where even I can't avoid spotting the bugs" (PDF p. 59). The last benefit he names the Design Stamina Hypothesis: effort put into good internal design lets a team go faster for longer; he calls it a hypothesis because he cannot prove it (PDF p. 61). He insists the justification is economic, not moral: "The point of refactoring isn't to show how sparkly a code base is—it is purely economic" (PDF p. 69). This wiki takes from that a review consequence: a refactoring proposed for code nobody needs to change or understand has no payoff to cite, whatever its aesthetic merit. The criterion he applies to the result is ease of change ([[easier-to-change]]).

**When it is not worth it.** Messy code that does not need modifying: "Some ugly code that I can treat as an API may remain ugly" (PDF p. 67); only the need to understand how it works makes refactoring pay. Code easier to rewrite than to refactor: Fowler often cannot tell without trying for a while, and says the call needs judgement he cannot reduce to simple advice (PDF p. 67). Clean code is not exempt in the other direction: "excellent code needs plenty of refactoring too" (PDF p. 64), because trade-offs right for yesterday's features may be wrong for today's. The occasions are on [[when-to-refactor]]; what makes it safe without a person checking is [[self-testing-code]] and [[automated-refactoring]].

## The Main Rule of Software Evolution

McConnell rejects the picture of coding as a single linear pass followed by maintenance. Significant changes happen during the first version too: requirements drift by roughly 1-4% a month even on well-run projects (Jones, 2000), and code-centred methods expect more change during construction, not less (pp. 551-552). His test for any change: «Главное Правило Эволюции ПО состоит в том, что эволюция должна повышать внутреннее качество программы» (p. 553). Fixing symptoms by superstition lowers quality; treating a change as a chance to improve the original design raises it (p. 552). Refactoring is the main strategy for meeting the rule (p. 553), and the book calls construction the best moment to make the changes one would want to make later anyway (p. 571).

This wiki reads the rule as a check on a diff: after the change, is the touched code at least as cohesive, as well named and as free of duplication as before? A fix that adds a special case beside an existing one fails it ([[fix-the-root-cause]]). The same decay seen from outside is [[software-entropy]].

## What it depends on

Guaranteeing that external behaviour is unchanged requires good automated unit tests that check that behaviour (p. 261). The book calls Fowler's advice on good regression tests decisive for safe refactoring (p. 264). See [[refactor-in-small-tested-steps]]. *Code Complete* names three conditions for success (p. 571): attention to the warning signs ([[refactoring-warning-signs]]), knowing many specific refactorings, and a safe strategy ([[refactor-in-small-tested-steps]], [[scale-review-to-refactoring-risk]], [[where-to-refactor]]).

## What triggers it

The book says you refactor when you have learned something, when you understand something better than you did last year, yesterday or ten minutes ago (p. 261). It lists these reasons (p. 261):

- **Duplication:** a breach of DRY has been found.
- **Non-orthogonal design:** something could be made more orthogonal.
- **Outdated knowledge:** circumstances, requirements or your understanding have changed, and the code must catch up.
- **Usage:** real use shows that some features matter more than expected, and others less.
- **Performance:** functionality needs to move from one part of the system to another.
- **Passing tests:** once code passes a new test, it is a good moment to tidy what you just wrote.

This wiki notes that only the first two and the last can be read from the code. Outdated knowledge, usage and performance need facts from outside it, so an inspector can raise them only when those facts are in hand.

## Why it is resisted

The book calls refactoring the management of pain: the code worked, so there is a wish to leave it alone, and developers are reluctant to return to something only because it is not quite right (p. 262). For when to act despite that, see [[refactor-early-and-often]].

## Tools

The book notes that many IDEs now rename variables and methods, split long routines, propagate changes and move code automatically (p. 264). How far such tools can be trusted without tests is [[automated-refactoring]].

## Related

- [[do-not-refactor-while-adding-features]]
- [[refactor-in-small-tested-steps]]
- [[refactor-early-and-often]]
- [[prototype-when-code-resists]], for a change that keeps fighting back with no known cause
- [[refactoring-warning-signs]], [[where-to-refactor]], [[scale-review-to-refactoring-risk]]
- [[replaceable-code-over-forecast]]
- [[when-to-refactor]], [[preparatory-refactoring]], [[parallel-change]], [[self-testing-code]]
- [[mechanical-code-transformation]], for output of a restructurer, translator or generator that people now maintain

## Source

[[pragmatic-programmer]], Topic 40, pp. 259-264, quoting Fowler's *Refactoring*. The discriminating test drawn from the definition, and which triggers can be read from code, are this wiki's own.

[[code-complete]], McConnell, 2nd ed., Russian edition, chapter 24, pp. 551-553, 558, 568 and 571, citing Fowler (1999), Yourdon and Constantine (1979), Jones (2000), Manzo and Beck. The exclusions, the Main Rule and the conditions for success are that book's, paraphrased except where quoted. The reading of the Main Rule as a check on a diff is this wiki's own.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2 "Principles in Refactoring", PDF pp. 56-59, 61, 64, 67, 69: the two senses, the step-size test against restructuring, the looseness of observable behaviour, the contrast with optimization, the four benefits and the Design Stamina Hypothesis, the economic justification and the cases not worth it. This wiki's own for that part: the reading of a mid-refactoring bug as a separate step and the review consequence of the economic argument.
