---
title: Keep variable live time short
category: complexity
summary: "References to one variable spread over many lines with unrelated statements between them, nothing repeating; a block of declarations at the top of a routine far from each first use, or one long enough to need sorting; statements on two independent sets of variables interleaved (getA, getB, sumA, sumB, printA, printB) where each set could run as its own block, so a box drawn round one object's statements overlaps another's; a block of aligned assignments setting up different objects in alternation."
tags: [rule, span, live-time, proximity, grouping, extract-method]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell gives two countable measures of how far a variable's references spread (pp. 238-242). The **span** between two references is the number of lines between them, and a variable's average span is the mean of its spans. The **live time** is the number of lines from the first reference to the last, both included, however many references fall in between. A variable used only on lines 1 and 25 has a live time of 25 and an average span of 23. One used on every line from 1 to 25 has a span of 0 and still a live time of 25 (p. 239). The book calls the code between references an «окном уязвимости»: the wider the window, the likelier that new code placed there corrupts the value, and the harder the value is to track while reading (p. 238).

## Rule

«Локализуйте обращения к переменным» (p. 238). «Делайте время жизни переменных как можно короче» (p. 239). The book gives four reasons (pp. 239-240):

- A smaller window of vulnerability leaves less room for a wrong or accidental change between the references that matter.
- The code gives a true picture. If a variable is set on line 10 and read on line 45, the gap implies it is used in between, and if it is set on line 44 and read on line 45, it plainly is not.
- There are fewer initialization errors. As code changes, straight-line code tends to turn into loops, and initialization done far from the loop gets forgotten.
- The code is easier to read and to split. When all the references fit on one screen, editing and debugging are easier, and a tight cluster of references is easy to extract into its own routine.

The book's worked example puts the measure into numbers: average live times of 54 and 7 lines for the same logic (pp. 241-242). It also admits that no threshold is known yet, so both span and live time are simply to be minimized (p. 242). Seen through this measure, global variables have an enormous span and live time, which the book counts as one more reason to avoid them (p. 242). See [[global-data]].

The concrete practices the book gives (pp. 242-243):

- «Группируйте связанные команды» (p. 242). Put statements that work on the same variables next to each other.
- Split groups of related statements into separate routines. Other things being equal, a variable in a shorter routine has a smaller span and live time (p. 243).
- Do not assign a value until it is needed, and declare at the point of assignment (p. 242). See [[initialize-close-to-first-use]].

Chapter 31, on laying out declarations, returns to the same point. McConnell prefers declaring each variable near its first use over declaring all of them in one block, because that shortens span and live time and makes the code easier to split into routines; he refers back to section 10.4 (p. 746). On ordering a block of declarations, he says grouping by type usually makes sense, since variables of one type often take part in similar operations, and alphabetical order is not worth the effort. His point is a sign: if the list is so long that alphabetical order helps, the routine is probably too big and should be split into smaller routines with few variables each (p. 746). The same section's case for one declaration per line is layout, which this charter leaves to the formatter.

Chapter 14 returns to the same shape from the side of statement order (section 14.2). When statements have no order dependency among them, their order is still a design choice, and McConnell lets secondary criteria decide it, governed by the Principle of Proximity: «Располагайте взаимосвязанные действия вместе» (p. 342). A reader should be able to read the code from top to bottom rather than jumping around in it (pp. 342-343). «Размещайте взаимосвязанные выражения вместе» (p. 343): statements are related when they work on the same data, perform a similar task, or depend on each other's order. He names three gains for the grouped form (p. 343): the references to each variable are localised, each object is live across few lines, and the grouping shows that the code can be split into separate routines, one per kind of data, which the interleaved version gave no hint of.

His check is to print the routine and draw a box around each set of related statements. In well-organised code the boxes do not overlap, though they may nest; overlapping boxes mean the code should be regrouped (pp. 343-344). After grouping, a group whose statements are strongly related to each other and have no meaningful relation to the code around it may belong in its own routine (p. 344).

Chapter 31, on layout, reaches the same shape a third time. A paragraph of code, McConnell says, should hold only related statements that perform one task: «абзац кода должен содержать только взаимосвязанные операторы, выполняющие одно задание» (p. 720), and unrelated statements are kept apart (p. 720). His reason is that a program is denser than a book and must give the reader more hints about its organisation; where it does not, the reader has to reconstruct the organisation and may never learn it (p. 720). His example interleaves assignments that set up a text window with assignments that set cursor parameters, and the poor ordering, the lack of separation and the aligned equals signs made the statements look more closely connected than they were; regrouped, the code shows two separate jobs (pp. 730-731). Where statements can run in any order, the order still tells a reader which statements must run in sequence and which merely stand side by side, and sorting them forces the writer to think about which really belong together (p. 731). The blank lines themselves are layout, which this charter leaves to the project's formatter; this wiki keeps from chapter 31 only the grouping, and reads it as a cohesion test a reader can run on a routine body: a group whose heading comment has to say "and" describes two tasks.

## Sign in code

- Two or more independent sets of variables are processed in interleaved statements: fetch A, fetch B, sum A, sum B, print A, print B. The book's `SummarizeData` example makes the reader track six variables where two blocks of three would do (pp. 242-243).
- The same shape by the box test of chapter 14 (pp. 343-344): draw a box around all the statements that touch one object, and that box overlaps the box of another object instead of nesting with it or following it. Typically all objects are created first, then each gets its first step, then each its second.
- A long run of assignments with aligned `=` columns, forming one visual block, in which consecutive lines set up different objects with no dependency between them, as in chapter 31's window-and-cursor example (p. 731).
- A variable is assigned and then first read many lines later, with statements in between that do not touch it.
- A routine-level variable is referenced only at the routine's start and end.
- A routine opens with a block of declarations, and some of those variables are first used many lines below (p. 746).
- The declaration list is long enough that it has been sorted alphabetically, or would have to be, for a reader to find a variable. The book reads this as a routine that is too big (p. 746); this wiki hands the size verdict to [[routine-length]], and the repair here is the same extraction.

The interleaved statements have to be independent for this sign. If one object's step reads another object's result, the interleaving may be the real order: a field carrying that result between ordered calls is [[pass-state-dont-hoard-it]], and an order imposed by timing or turn-taking is [[temporal-coupling]].

This wiki assigns the neighbouring cases as follows. This page owns distance and interleaving where nothing repeats. Where the interleaved independent statements sit in one loop body and each group could run as its own loop, [[one-loop-one-job]] owns it; interleaving in straight-line code is [[keep-variable-live-time-short]]. Where an initialization sits outside a loop or repeated block that must reset it, [[initialize-close-to-first-use]] owns it; both pages read the same top-of-routine block by that condition. A variable whose declared scope is wider than its uses (a field used inside one method, a routine local used in one loop) is [[smallest-scope-first]]. A routine too long to read as a whole is [[routine-length]]; extracting the blocks this page produces is the repair both pages share ([[extract-routine-to-name-a-step]]).

## When not to apply

McConnell's own limit is order dependency: the Principle of Proximity governs only statements whose order does not matter, and where order matters the dependency comes first (pp. 342, 345). The limits below are this wiki's own:

- **Phases that are the point.** Code that gathers all its input before computing anything, or validates every field before mutating anything, keeps a phase order on purpose, typically so as not to leave work half done after a failure. The phases are then the related groups.
- **Measured performance.** Batching similar operations across objects, such as one pass over a shared resource or one round trip, can be the reason for the interleaving. The book names performance as one of the secondary criteria (p. 342). Regroup only after checking that the batching is not doing work.
- **Very short routines.** When the whole routine fits on a few lines, the reader already sees every mention of a variable at once, and nothing is gained by regrouping.
- Statements whose order is fixed by an outside protocol, such as a transaction that must open both resources before using either, cannot be regrouped. Interleaving there is required, and a comment should say why. See [[temporal-coupling]].
- A value that must outlive a stretch of code, such as an accumulator over a whole loop, has a long live time by nature. The rule asks for the shortest live time the logic allows, not a short one at any cost.
- A language or project convention that requires declarations at the top of a block or routine overrides where declarations go. The sign of an oversized routine still holds there.
- A variable that must be set before a loop and read after it belongs outside the loop, even if its first meaningful write is inside: near its first use means the smallest scope that covers every use.
- The counts are a reading aid. The book gives no threshold (p. 242), so a finding names the interleaving or the gap and does not quote a number as a limit.

## Repair

1. Regroup the statements so that each set of variables is handled in one contiguous block, from its declaration to its last use (p. 343). Run the box test again: the boxes should now follow each other or nest. Drop column alignment that ties unrelated lines into one block (p. 731).
2. Move each assignment, and each declaration from a block at the top, down to just before its first read, in the narrowest scope that holds all its uses. Do not sort a long declaration list to make it searchable; shorten the routine instead (p. 746).
3. If a block now stands alone, extract it into a routine named for its purpose. Its variables become locals of that routine.

## Before and after

Before:

```
function summarize()
    old = load_old()
    new = load_new()
    old_total = sum(old)
    new_total = sum(new)
    print_summary("old", old, old_total)
    print_summary("new", new, new_total)
    save_summary("old", old_total)
    save_summary("new", new_total)
```

After:

```
function summarize()
    summarize_set("old", load_old())
    summarize_set("new", load_new())

function summarize_set(label, data)
    total = sum(data)
    print_summary(label, data, total)
    save_summary(label, total)
```

## Source

McConnell, *Code Complete*, Russian edition, via [[code-complete]], section 10.4: span and the window of vulnerability (pp. 238-239), live time and its four benefits (pp. 239-240), the worked example with averages of 54 and 7 (pp. 240-242), the lack of a threshold and the remark on globals (p. 242), and grouping and splitting into routines (pp. 242-243). Section 14.2: secondary criteria for statements in arbitrary order and the Principle of Proximity (p. 342), reading top to bottom (pp. 342-343), the three gains of the grouped form (p. 343), the box test (pp. 343-344), extracting a strongly related group (p. 344), and the checklist and key points (pp. 344-345); section 31.2, p. 720: paragraphs of code holding one task and the density argument; section 31.4, pp. 730-731: the window-and-cursor regrouping, aligned equals signs and what order tells a reader; section 31.5, p. 746: declaring near first use, grouping declarations by type, and the alphabetically sorted list as a sign of an oversized routine. The book credits the measures to Conte, Dunsmore and Shen, *Software Engineering Metrics and Models* (1986). The order-dependency limit is McConnell's (pp. 342, 345), and the performance limit rests on his naming performance as a secondary criterion (p. 342). This wiki's own: the wording of all signs, the independence condition, the box-test and aligned-assignment signs as worded, the two declaration-block signs, the other limits, the cohesion-test reading of chapter 31, the assignment against the neighbouring pages, the declaration part of repair step 2, the third repair step's naming, and the pseudocode, which is a rewrite of the book's `SummarizeData` that goes one step further by extracting the routine the book only suggests.
