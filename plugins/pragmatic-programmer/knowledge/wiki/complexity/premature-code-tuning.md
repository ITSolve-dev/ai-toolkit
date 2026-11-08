---
title: Do not tune code without a measurement
category: complexity
summary: "Statement-level tricks for speed (pointer walking instead of indexing, a hand-unrolled loop with a tail fix-up, a loop duplicated per branch of an invariant test, a sentinel written past an array's end, a running accumulator instead of index multiplication, a precomputed table or bit trick in place of a plain computation, juggled loop indexes) with no profile naming it a hot spot and no resource target on it, while the algorithm itself is unchanged."
tags: [rule, performance, premature-optimization, code-tuning, readability, measurement, loops]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Code tuning, in McConnell's sense, means small changes to code that is already correct, made to make it faster or smaller: one class, one routine, more often a few lines. Large design changes are not tuning (p. 576). Chapter 26 sets it against refactoring: refactoring improves a program's internal structure, while tuning is better called «антирефакторингом», because its changes worsen the structure to gain performance (p. 596). McConnell says this holds by definition: a change that did not worsen the structure would not count as an optimization at all, it would simply be standard practice (p. 596). This page covers tuning that has no measurement behind it, whether it was done during first writing or later.

Its neighbour is [[fastest-algorithm-is-not-always-best]], which covers *choosing* an algorithm. The two share a selection condition: if the speed-motivated change replaces one algorithm or data structure with another, [[fastest-algorithm-is-not-always-best]] owns it; if the algorithm stays the same and only its statements are rewritten for speed, this page owns it. A precomputed table standing in for a closed-form computation counts as a statement-level rewrite, because the algorithm's result and order are unchanged.

## Rule

Write clear, correct, modular code first. Tune only after the program works and a measurement shows where it is slow, and keep each tuned form only if a measurement shows that it helps. The book says so directly: «Не оптимизируйте ее, пока не убедитесь, что это на самом деле нужно» (p. 581). It also calls the belief that you should optimise as you write a myth: «Оптимизацию следует выполнять по мере написания кода — НЕВЕРНО!» (p. 579). Chapter 26 adds that every technique must be measured: «чтобы с уверенностью говорить о результатах любого вида оптимизации, вы должны их оценить. Никаких исключений.» (p. 603). No rule of thumb replaces it: «Единственным надежным практическим правилом является оценка результатов каждого вида оптимизации в конкретной среде» (p. 596). McConnell therefore presents his catalogue of techniques as «вещей, которые стоит попробовать», many of which will give nothing in a given environment (p. 596). His closing argument: an optimization that does not justify profiling cannot justify the loss of readability, because the effect of an unmeasured optimization on performance is at best theoretical, «тогда как ее влияние на удобочитаемость столь же определенно, сколь пагубно» (p. 630). He calls the requirement of measurable improvement a good way to resist premature optimization (p. 630).

The reasoning the book gives:

- **Programmers guess hot spots badly.** Less than 4% of code usually takes more than half the run time (Knuth, cited on p. 577). Tuning everything as you write spends about 96% of the effort on code that did not need it (p. 579). In the author's own charting program, far less than 1% of the code took 90% of the time (p. 581).
- **Intuition about cost is unreliable.** Fewer source lines are not faster: ten explicit assignments ran at least 60% faster than the equivalent three-line loop in the book's tests (p. 578). Rewriting matrix summation with pointer increments gave no gain at all, because the compiler already turned array indexing into pointer arithmetic. The book's conclusion is that the only result of tuning you can be sure of without measurement is harder reading: «единственным результатом оптимизации, в котором можно быть полностью уверенным без измерения производительности, является затруднение чтения кода» (p. 589).
- **One technique, opposite results.** Chapter 26's own figures: loop unswitching saved 19-28% in three languages and under 1% in Visual Basic (p. 603); loop unrolling saved 16-43% but made Python 27% slower, and a second unrolling added nothing in Java (pp. 605-606); loop interchange, predicted to save 16% by counting iterations, saved 4-34% (p. 609); flattening a two-dimensional array saved 66% in Visual Basic and 9% in C# (p. 612); hoisting an array reference out of a loop made C++ 7% slower (p. 613); an integer `Log2` built from comparisons ran 15-20 times faster in C++ and Java but 41% slower in PHP (p. 619). Without testing a technique in the specific circumstances, «ни в чем нельзя быть уверенным» (p. 612). McConnell adds that results were less predictable in his second edition than ten years earlier, since they depend on the language, the compiler and its version, the libraries and the compiler options (p. 629).
- **Tricky code defeats the compiler.** Optimising compilers do better on simple code. Juggling loop indexes makes their job harder, and the book puts a good compiler's gain at 40% or more, against 15-30% for many hand techniques (p. 582).
- **Tuning ties code to one environment.** A trick that helps on one compiler, library version or machine can hurt on another, and every tuned fragment has to be re-profiled after each such change (p. 579).
- **It displaces other qualities.** Correctness, information hiding and readability become secondary, and the book says they are harder to improve later than performance, which after completion usually touches under 5% of the code (p. 580). Tuning always trades complexity, readability, simplicity and maintainability against performance (pp. 629-630).

## Sign in code

Both together, in this wiki's reading:

1. A routine uses a lower-level or less direct form than its neighbours, and the only reason for it is speed. The shapes the two chapters name:
   - walking a pointer instead of indexing (p. 589), or juggling loop indexes (p. 582);
   - **unswitched loop:** two or more loops with the same header and nearly the same body, each inside one branch of a condition that does not change during the loop (pp. 602-603);
   - **unrolled loop:** a body repeating one statement for `i`, `i + 1`, `i + 2`, a step greater than 1, and one or more `if` statements after the loop handling the leftover elements (pp. 604-606);
   - **sentinel:** the searched value written into the slot just past the logical end of an array, the original saved beforehand, and a loop whose only test is equality with that value (pp. 607-609);
   - **strength reduction:** a running accumulator advanced by a constant each iteration, standing in for an expression that multiplies by the loop index (pp. 609-610);
   - a closed-form computation replaced by a precomputed table and an index calculation such as `round((rate - LOWEST) * GRANULARITY * 100)` (p. 622), or a library call replaced by a ladder of comparisons or bit shifts (pp. 619-620).
2. No profile, benchmark or stated resource target in the code, tests or commit history for that routine.

Often a comment or commit message claims the form is faster with no figure beside it; that corroborates the sign but is not needed for it. The first alone is not the sign: a low-level form may be the project's normal idiom, and every shape above is legitimate once a measurement backs it.

This wiki assigns the neighbouring shapes as follows. A cache of remembered results is [[cache-must-earn-its-complexity]]. A small routine's body copied by hand into its callers is [[do-not-hand-inline-for-speed]], when speed is the stated reason. Two unrelated jobs merged into one loop because they share bounds ("loop jamming", pp. 603-604) is [[one-loop-one-job]]. The order of `case` arms or an `if` chain is [[order-branches-by-frequency]]. A slow path whose cost lies in I/O, a lookup or a system call rather than in the statements is [[fix-performance-at-the-right-level]]. Where the same path also carries statement-level tweaks for speed, the mismatch is [[fix-performance-at-the-right-level]]. Statement tricks with no measured slowness at all are [[premature-code-tuning]]. Changes that are faster *and* clearer are not tuning by McConnell's definition and need no measurement: naming an invariant chain before a loop ([[explaining-variable]]), naming a repeated subexpression ([[name-repeated-subexpression]]), leaving a search loop at the first hit ([[stop-loop-once-answer-known]]), and replacing a logic chain with a documented table ([[drive-repeated-dispatch-from-a-table]]).

A structural improvement declined or reverted for speed with no measurement (a loop kept fused, a temp kept for one lookup) is [[refactor-first-tune-afterwards]]; a statement-level trick written for speed with no measurement is [[premature-code-tuning]].

## When not to apply

- A resource target is set for this routine in the specification. The book allows tuning during writing when individual routines carry explicit size and speed goals (p. 580).
- A profile or measurement names this code as a hot spot, and a measurement in the target environment shows the tuned form helps there.
- The faster form is no harder to read than the slow one. The book calls indexing a frequently used database table plain good practice (p. 586); this wiki reads traversing a two-dimensional array in the order it is laid out in memory (p. 584) the same way. This boundary is this wiki's reading of those examples.
- The project is one of the few where speed or size is a primary requirement. The book says such cases are rarer than most people think and should be met by design up front, not by tuning as you write (p. 581). Embedded and real-time systems are the setting where McConnell says developers still need these techniques, while for many common desktop programs they have become irrelevant (p. 629); there the measurement is still owed, but a tuned shape is expected rather than suspect.
- The language does the transformation already. Short-circuit evaluation makes hand-splitting `if (a and b)` into nested tests pointless where the language supports it (p. 596). This wiki extends the point to compilers that unroll, unswitch or reduce strength themselves; the extension is ours, not the book's.

## Repair

1. Rewrite the routine in its plainest form, the one a reader expects: re-merge unswitched loops, roll an unrolled loop back up, drop the sentinel.
2. Keep the tuned form only if a measurement on the current build shows it is faster, and put the figure and the environment next to it. Keep it as small and local as possible.
3. When a tuned form stays, check the failure mode that comes with it: an off-by-one in an unrolled loop's tail (p. 605), every later change to an unswitched loop made twice (p. 603), a sentinel needing a reserved slot past the end and a carefully chosen value (pp. 608-609).
4. If speed matters, run [[code-tuning-procedure]] once the program works.

## Before and after

```
// before: written this way 'for speed', never measured
function sumMatrix(m, rows, cols):
    p = addressOf(m[0][0])
    last = addressOf(m[rows - 1][cols - 1]) + 1
    sum = 0
    while p < last:
        sum = sum + read(p)
        p = p + 1
    return sum
```

```
// after
function sumMatrix(m, rows, cols):
    sum = 0
    for row in 0 .. rows - 1:
        for col in 0 .. cols - 1:
            sum = sum + m[row][col]
    return sum
```

The before has the page's sign (lower-level form, no measurement). The after has none, and stays clear of [[fastest-algorithm-is-not-always-best]] because the algorithm did not change.

An unswitched loop with no measurement: renaming `count` now means editing two places.

```
if sumType == NET:
    for i in 0 .. count-1:
        netSum = netSum + amount[i]
else:
    for i in 0 .. count-1:
        grossSum = grossSum + amount[i]
```

```
for i in 0 .. count-1:
    if sumType == NET:
        netSum = netSum + amount[i]
    else:
        grossSum = grossSum + amount[i]
```

If a measurement does justify the first form, it stays, with a comment naming the measured saving and the environment.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]].

- Chapter 25: definition of code tuning p. 576; Pareto figures p. 577; line-count myth pp. 578-579; portability and re-profiling p. 579; tuning while writing pp. 579-580; when to tune and the charting program p. 581; compilers and simple code p. 582; matrix-summation case p. 589.
- Chapter 26: tuning as anti-refactoring, the only reliable rule, «вещей, которые стоит попробовать» and short-circuit evaluation p. 596; unswitching and «Никаких исключений» pp. 602-603; jamming pp. 603-604; unrolling pp. 604-606; sentinel pp. 607-609; loop interchange p. 609; strength reduction pp. 609-610; per-technique figures pp. 612, 613, 619; table and bit-trick shapes pp. 619-622; unpredictability, constrained systems and the trade-off p. 629; the readability argument p. 630.
- Quotations were transcribed from the extracted text with line-break hyphens joined, and need the page-image check.
- This wiki's own: the selection condition against [[fastest-algorithm-is-not-always-best]] and its reading of precomputed tables, the composite sign (a tuned shape *without a stated measurement*), the assignment of the neighbouring shapes, the 'no harder to read' limit, the extension to compilers that apply these transformations themselves, repair step 2's recording of the figure beside the code, and the pseudocode; the first pair follows the shape of the book's example without reproducing its listing.
