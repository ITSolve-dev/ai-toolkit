---
title: Pass state along instead of hoarding it
category: types-and-state
summary: "A field written by one method only for a later method to read; zero-argument void methods that must run in a fixed order, such as one of several parallel ComputeX() calls that also initialises the shared data; objects handing results over by setting each other's fields."
tags: [rule, state, mutation, temporal-coupling, transformation, order-dependency]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-07
---

State that exists only to carry a result from one step to the next belongs in the arguments and return values of those steps, not in fields. Thomas and Hunt set this against the object-oriented reflex of hiding data in objects that exchange it by changing each other's state. They hold that this reflex introduces coupling and is a strong reason object-oriented systems are hard to change (p. 193). That is the authors' judgement of a paradigm. The rule below is narrower.

McConnell makes the same point from the order of statements rather than from the flow of data (*Code Complete*, section 14.1). Statements are hard to organise only when their order matters, and the trouble comes when that order is hidden. He places the hidden case at the end of a scale. In `data = ReadData(); results = Calculate(data); Print(results)` the dependency can be seen in the code. In `revenue.ComputeMonthly(); revenue.ComputeQuarterly(); revenue.ComputeAnnual()` it is visible only to someone who knows accounting. A run of parameterless `ComputeMarketingExpense`, `ComputeSalesExpense`, ... `DisplayExpenseSummary`, where the first one also initialises the class's member data, hides it completely: the reader cannot know the order for certain from the code (pp. 338-339).

## Rule

«Не накапливайте состояние, а передавайте его по кругу» (p. 193). Picture data as a river rather than as small pools spread across the system (pp. 193-194). Each function receives what it needs and hands on what it produced.

McConnell's order of preference agrees: first, code with no order dependency; then code whose dependencies are obvious, «Организуйте код так, чтобы зависимости были очевидными» (p. 339); only after both, documenting the order (p. 341). His tools, in the book's order; the book ranks the first three, and offers flags separately where the order is critical (p. 341):

1. **Data flow.** Pass the shared data as a parameter. Better still, turn each procedure into a function that takes the data and returns the updated value, so each line consumes what the line before it produced (p. 340).
2. **Responsibility and naming.** Initialisation does not belong inside one of several parallel routines. The book calls it an accident there and moves it to a routine named for it, `InitializeExpenseData()`, whose name says it must run first. If no separate routine is made, the name must state everything the routine does (`ComputeMarketingExpenseAndInitializeMemberData`). The book does not count that long name as the defect: «Ужасен сам метод!» (p. 340).
3. **A comment** stating the order and the shared data, as a fallback (p. 341).
4. **Status flags or assertions**, such as `isExpenseDataInitialized` set by the initialiser and checked by every dependent routine, where the order is critical enough to justify them (p. 341).

Data flow also works in the other direction. Routines that take separate, unshared data (`ComputeMarketingExpense(marketingData)`, `ComputeSalesExpense(salesData)`) say that their order does not matter, and a final call that takes all of them says it must come last (pp. 340-341).

This wiki reads the damage as McConnell's example shows it. Someone who adds a call above the initialiser, or reorders the computations, gets wrong totals and no error, because nothing in the call sequence states the order.

## Sign in code

The Pragmatic Programmer names the reflex but not a pattern to look for. This wiki reads the sign as any of these:

- A field assigned in one method and read only in another, holding an intermediate result. It is not meaningful before the first runs or after the second finishes.
- Methods with no parameters and no return value that callers must invoke in a fixed order on the same object, such as `load()`, `parse()`, `summarize()`.
- A method that fails or returns nonsense unless another named method ran first, because it reads a field that only an earlier method sets and that holds an intermediate result.
- One object passing a result to another by calling its setter, then calling a parameterless method that reads it.
- One of a set of routines with parallel names (`ComputeX`, `ComputeY`, `ComputeZ`) also does setup that the rest depend on, such as initialising members or opening the shared state, and nothing in its name says so. The shape is McConnell's example (p. 339).

This wiki assigns the neighbouring cases as follows. This page owns order held in a field that only carries a result between steps, which a parameter removes. Fields that only carry intermediate results between the methods of one algorithm, set when it starts and read by nothing else, are [[pass-state-dont-hoard-it]]; fields valid only in one circumstance, which other code tests for being set before it acts, are [[null-field-hides-another-class]]. Order imposed by timing, waiting or turn-taking, with no field carrying a result, is [[temporal-coupling]]. An object built with a no-argument constructor and completed by setters before its first use belongs to [[temporal-coupling]]; an object already in use whose setter carries an intermediate result to a later method belongs to this page. Where a field carries a result between the ordered calls, [[pass-state-dont-hoard-it]] owns the finding even when a comment states the order. [[temporal-coupling]] owns an order stated in a comment only where no such field exists. A routine the project cannot change, whose order a caller relies on, and a field that outlives the steps, such as a connection, are [[rely-only-on-documented-behaviour]]. A field written and read only within a single call of a single method is [[smallest-scope-first]]; a field written by one method only so that a later method can read it is [[pass-state-dont-hoard-it]].

For the parallel-routines case, the order belongs to this page and the name that hides the extra job belongs to [[rename-when-meaning-drifts]]. One fragment can therefore earn both findings, with compatible repairs: the setup moves into a routine named for it, and that routine's result is passed on. Independent statements interleaved by phase, where no order dependency exists, are [[keep-variable-live-time-short]].

## When not to apply

The Pragmatic Programmer states no limit beyond admitting that some coupling remains (p. 194). Code Complete supplies the last two below. The rest are this wiki's own.

- The state is the subject and not a stage: a connection, a cache, a counter, a session, anything whose value outlives one pass through the code.
- A field guards an invariant across many operations. Encapsulation that protects a rule is not hoarding, and passing such data around would expose it to every caller. See [[class-invariant]].
- A measured cost makes copying or re-deriving a value too expensive on a hot path. The field is then a recorded trade-off.
- The value is read by several independent operations during the object's life. It is not an intermediate result, so it does not meet the sign.
- A framework fixes the signatures. The project owns the bodies and no parameter can be added, so this is a routine the project cannot change.
- **Code the project may not restructure.** For code under strict change control, or code that cannot be improved for another reason, McConnell accepts a comment that states the order and the shared data: «используйте документирование для компенсации недостатков кодирования» (p. 341). This wiki reads that as: there the shape is not this page's finding, and a missing comment stating the order is.
- **Status flags have a cost.** Checking the order with flags such as `isExpenseDataInitialized` means new variables, new initialisation code and new error checks, which in the book's words «увеличивает возможность добавления ошибок» (p. 342). The book weighs the benefit against the added complexity. This wiki reads that as: use flags only where a wrong order would do real damage and data flow cannot carry the order.

## Repair

1. Turn each ordered step into a function whose inputs are its parameters and whose result is its return value.
2. Delete the fields that only carried results between steps.
3. Replace the ordered calls with one expression or sequence in which each step takes the previous result. The order is now enforced by the data, because a step cannot be called without its input.
4. If a step can fail, carry that through the chain: [[wrap-values-between-transformations]].
5. Where one of the steps also does setup the others depend on, move the setup into a routine named for it and pass its result on (*Code Complete*, p. 340).
6. Where the steps work on separate data, give each step only its own data, so the code shows they can run in any order (pp. 340-341).
7. If the code cannot be changed, state the order and the shared data in a comment above the sequence. If the order is critical and must be checked at run time, set a flag in the initialiser and assert on it in every dependent routine, and accept the extra code that costs (p. 341).

The model behind this is [[programs-transform-data]].

## Before and after

```
class ReportJob
    field raw
    field rows
    field total

    method load(): raw = read_file(path)
    method parse(): rows = parse_rows(raw)
    method sum(): total = add_up(rows)

job.load()
job.parse()
job.sum()
print(job.total)
```

```
function report_total(raw):
    rows = parse_rows(raw)
    return add_up(rows)

print(report_total(read_file(path)))
```

The second pair has the shape of McConnell's example, where one of the parallel steps also clears the shared totals:

```
computeShipping()        // also clears this.totals, so it must run first
computeTax()             // adds into this.totals
computeDiscount()        // adds into this.totals
printInvoice()           // reads this.totals
```

```
totals = newTotals()
totals = addShipping(totals, order)
totals = addTax(totals, order)
totals = addDiscount(totals, order)
printInvoice(totals)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 30, pp. 193-194, for the tip and its reasoning. The narrowing of the tip to state that only carries a result between steps, the signs, the assignment of the neighbouring cases, the limits and the repair steps are this wiki's own, as is the pseudocode.

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 14.1, pp. 338-342: the three levels of visible dependency (pp. 338-339), organising code and naming routines so that dependencies are obvious (pp. 339-340), parameters and functions that return the updated data, and separate data that signals no order (pp. 340-341), the comment fallback and the strictly controlled code limit (p. 341), status flags (p. 341) and their cost (p. 342); the chapter's key points repeat these (p. 345). This wiki's own for this source: the reading of the damage, the wording of the parallel-routines sign, the assignment against [[rename-when-meaning-drifts]] and [[keep-variable-live-time-short]], the readings of both limits, and the second pseudocode pair.
