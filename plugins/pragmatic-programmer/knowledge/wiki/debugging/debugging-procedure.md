---
title: Debugging procedure
category: debugging
summary: "Use when a failure's cause is unknown and fixes are being tried by guess: an edit made before the failure was reproduced or the wrong value seen, a hypothesis that ignores some observations, a fix chosen while several causes remain open, or a warning-laden build under investigation."
tags: [method, debugging, diagnosis, scientific-method]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Debugging is a search for a cause, and this page sets the order of that search so that cheap evidence is spent before expensive theory.

## Steps

1. **Clean the build.** Start from code that compiles with no compiler warnings. There is no point spending time on a fault the computer can find on its own (p. 126).
2. **Collect exact observations.** Bug reports are imprecise, and coincidence can mislead (p. 126). Precision drops further, as this edition prints it, when a report passes through third-party software, so it may be necessary to watch the reporting user at work (p. 126). The book's example is a crash when a brush stroke went from top right to bottom left (p. 127). See [[test-boundaries-and-realistic-use]].
3. **Reproduce it with one command.** See [[failing-test-before-the-fix]].
4. **Read the error message before reading code.** The tip reads «Внимательно читайте сообщение об ошибке, каким бы отвратительным оно ни было» (p. 128). The authors note how many developers, on seeing an exception, go straight to the source instead (p. 128).
5. **For a bad result rather than a crash, see the wrong value.** Run the test that shows the fault and go to where the value is produced in the debugger (p. 128). The book says «непременно выявите неверное значение в отладчике» before anything else, because both authors have spent hours on a bug only to find that this particular run had succeeded (p. 128).
6. **Walk the call stack.** A value such as `interest_rate` equal to 4.5 where 0.045 was expected is occasionally obvious, but more often the question is why it became wrong, so move up and down the stack and inspect the frames (p. 128). This leads to [[fix-the-root-cause]].
7. **Keep notes.** Write down where a trail began, because a clue often leads nowhere and returning without a note wastes time (p. 128).
8. **Narrow by halves.** For a long stack, a large input or a regression across releases, use [[binary-search-debugging]] (pp. 128-130).
9. **Add traces when the problem has a history.** Use [[trace-statements]] when the state at one moment does not explain the failure (pp. 130-131).
10. **Explain the code step by step.** Say aloud, to a person or to an object, what each step of the code should do. The book calls this the rubber duck method (p. 131). Explaining forces you to state what you would otherwise take for granted, and putting assumptions into words can suddenly change your view of the problem (p. 131). A written note can work the same way: while writing, you may realise the entry you just made is wrong (p. 138).
11. **Eliminate by likelihood.** Suspect your own code before the platform. See [[select-isnt-broken]] (pp. 131-132).
12. **When surprised, stop trusting.** The book says a first reaction of «это невозможно» is simply wrong, since the failure plainly can happen and has, and that no reasoning should start from it (p. 126). See [[prove-dont-assume]] (p. 133).
13. **After the fix, close the gap.** See [[after-a-surprising-bug]] (pp. 133-134).

Version history also answers questions useful to a search: who changed a given line, how the current version differs from last week's, and which files change most often (p. 120).

## Code Complete's version: the scientific method

McConnell frames debugging as the scientific method applied to a defect: gather data from repeatable experiments, form a hypothesis that explains the relevant data, design an experiment that can confirm or refute it, and repeat (p. 529). He sets this against guessing, and notes that finding and understanding the defect is usually the bulk of the work: «Поиск дефекта и его понимание обычно составляют 90% работы» (p. 529). His procedure (pp. 529-530):

1. **Stabilise the error** so it occurs reliably, and reduce the failing test to the simplest one that still fails: [[stabilize-the-error]].
2. **Locate the source:** gather the data that produce the defect, form a hypothesis that explains it, decide how to prove or disprove it (by a test or by reading the code), and do so.
3. **Fix the defect:** [[fix-the-root-cause]], [[one-change-at-a-time]].
4. **Test the fix.**
5. **Look for similar errors:** [[after-a-surprising-bug]].

This wiki reads the two books as compatible: McConnell's step 1 is steps 2-3 above, his step 2 is steps 4-11, and his steps 4-5 are step 13.

### Forming and testing hypotheses

The book's tips for when the source will not show itself (pp. 533-537), beyond those the list above already holds (halving, explaining aloud):

- **Use all the data.** A hypothesis must explain every observation. «Если данные не соответствуют гипотезе, не игнорируйте их» (p. 533): ask why they do not fit and form a new one. A first hypothesis that explains only part of the data may be held as long as it is refined until it explains all of it (p. 533).
- **Refine the failing tests:** vary one parameter over a wider range, or concentrate on one parameter (p. 533).
- **Exercise the code in unit tests:** defects are easier to find in small fragments than in an integrated program (p. 533).
- **Reproduce the error several ways.** The book calls this triangulating the defect: once you think the cause is clear, run a test that should *not* fail but resembles the failing ones. «Если ошибка при этом все же возникает, значит, вы еще не полностью поняли проблему» (p. 534). A cause is often a combination of factors, so one test rarely finds the root.
- **Generate more data** with tests whose results are not already known, and **use negative results**: a refuted hypothesis still narrows the search (p. 534).
- **Brainstorm several hypotheses** before analysing any, and **keep a list of approaches** so a dead end does not swallow the session (p. 534).
- **Suspect classes and routines that had defects before**, and **check recently changed code** (p. 535).
- **Widen the region** when the defect is not found where you are looking (p. 535); see [[mental-set-in-debugging]].
- **Check for common defects** with code-quality checklists (p. 536).
- **Take a break** when nothing works; the book reads anxiety as the sign it is time (p. 536).
- **Time-box the guessing** and keep a list of brute-force methods: [[timebox-quick-debugging]] (p. 537).

### Before touching the code

The book's rules for the fix (pp. 539-540):

- **Understand the problem before fixing it.** Run tests until you can predict correctly, for every case, whether the error will occur (p. 539).
- **Understand the program, not only the problem.** The book cites a study on a 280-line program where programmers who sought to understand the whole program changed it correctly more often (Littman et al., 1986). McConnell does not extend that to a 50,000-line program, but asks for the neighbourhood of the defect: «под «соседством» я понимаю не несколько, а несколько сотен строк» (p. 539).
- **Confirm the diagnosis.** Run tests that prove your hypothesis *and* disprove the competing ones. «Если вы установили только то, что ошибка может быть результатом одной из нескольких причин, к устранению проблемы приступать рано» (p. 539).
- **Relax.** A fix made in a hurry leads to incomplete diagnosis and incomplete fixes (p. 540).
- **Save the original source** so old and new can be compared (p. 540).

The reason the book gives for this caution: at least one study found that first attempts to fix a defect were wrong half the time (Yourdon, 1986b; p. 539).

### Tools

The book treats tools as part of the method, not a substitute for it (pp. 545-548). A diff against the last good version localises a regression. A profile that does not move after an optimisation can expose a defect: McConnell replaced a linear array with a hash table, saw no speed-up, and found a defect in the allocation algorithm that was the real bottleneck (p. 546). On debuggers against reasoning he concludes: «Наиболее эффективная комбинация — ясный ум и хороший отладчик» (p. 548). A memory-overwrite case was solved by a breakpoint on a memory address after analysis had failed (p. 533). Compiler warnings are [[do-not-silence-warnings]].

## Checklist

The book's questions for a debugging session (p. 134), paraphrased:

- Is the fault a direct result of a defect, or only a symptom of a hidden one?
- Is the defect in the framework, the operating system, or your own code?
- What would you say if you had to explain the problem in detail to a colleague?
- If the suspect code passes its unit tests, how complete are they, and what happens when they run with this data?
- Do the conditions behind this defect exist elsewhere in the system, and are other hidden defects waiting there?

## Failure modes

- Investigating a run that actually succeeded, because the wrong value was never observed (p. 128).
- Treating a coincidence as a cause, because the report was imprecise (p. 126).
- Testing a reported defect with a different action from the reporter's and declaring it not a defect (p. 127).
- Fixing while several causes remain possible, or with a hypothesis that leaves some observations unexplained (*Code Complete*, pp. 533, 539).

## Limits

The book states step 1 without exception. This wiki adds a limit: in a build already carrying many warnings, clearing them all cannot be a precondition of a diagnosis. Clear the warnings in the code on the failing path, and leave the rest for separate work.

A build under investigation for a bug that still emits warnings on the failing path is the first step of [[debugging-procedure]], which owns that case; [[do-not-silence-warnings]] owns the suppression constructs and the build settings.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], Topic 20, pp. 124-134, with p. 120 and p. 138. The ordering as a numbered list is this wiki's arrangement of the book's sections. Step 10's placement and step 12's position after elimination are likewise this wiki's. The failure modes list restates the book's examples as things to avoid. The limit on step 1 and the assignment against [[do-not-silence-warnings]] are this wiki's own.

Step 2 reports p. 126 as printed: «стороннее программное обеспечение». This wiki takes the sentence to mean any intermediary between the user and the developer, because the book's remedy that follows is to watch the user at work.

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], chapter 23, pp. 529-548. The scientific-method frame, the five steps, the tips, the rules before fixing and the studies are that book's, paraphrased except where quoted; quotations were transcribed from the extracted text with line-break hyphens joined. The mapping of McConnell's steps onto the numbered list, the grouping into subsections and the added failure mode are this wiki's own.
