---
title: "Split Phase: separate two stages joined by an intermediate record"
category: functions
summary: "Procedure for a function whose first part works on one set of inputs and whose later part works on another (pricing from product data, then shipping from shipping data; or calculation, then rendering), the halves linked only by a few locals: move the second part into its own function, pass it an intermediate record built by the first, then extract the first."
tags: [method, refactoring, split-phase, separation-of-concerns]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Split Phase** is Fowler's refactoring for code that does two different things in sequence, here calculating a statement's data and formatting it. The code is divided into a first phase that produces an intermediate data structure and a second phase that consumes only that structure. Fowler's aim is "to divide the logic into two parts: one that calculates the data required for the statement, the other that renders it into text or HTML" (ch. 1, PDF p. 32). He refuses to copy the calculation helpers into a second rendering function; he wants "the same calculation functions to be used by the text and HTML versions of the statement" (PDF p. 32).

This wiki assigns the sign as follows. One function both computes a business result and builds its output is [[logic-testable-without-ui]], which owns the sign; [[split-phase]] is the procedure that separates them. A routine whose later part reads a different set of inputs and only a few results of its earlier part has sequential cohesion, which [[routine-cohesion]] owns; [[split-phase]] is the procedure that separates its parts. The decision to restructure before the second format is added, instead of copying, is [[preparatory-refactoring]].

## The general case

The catalogue entry (ch. 6, "Split Phase", PDF pp. 176-182) generalises the chapter 1 example. When code deals with two different things, split it so that each can be changed without holding the other in mind: "If I’m lucky, I may only have to change one module without having to remember the details of the other one at all" (PDF p. 176). Fowler names two typical cases: the input does not fit the model the logic needs, so a first phase massages it into a convenient form; or the logic breaks into sequential steps that each do something significantly different (PDF p. 177). His clue: "The best clue is when different stages of the fragment use different sets of data and functions" (PDF p. 177). His model at large scale is a compiler's chain of tokenizing, parsing, transforming and generating (PDF p. 176); this page applies the refactoring inside a module, at the level of functions, and names no module boundary.

The catalogue's mechanics (PDF pp. 177-178), which the chapter 1 sequence below instantiates:

1. Extract the second-phase code into its own function, passing everything it needs as parameters. Test.
2. Introduce an empty intermediate data structure as an extra argument to that function. Test.
3. For each parameter of the second phase: if the first phase uses or produces it, move it into the intermediate structure and drop the parameter, testing after each move. Fowler's "usual preference … is to move as much as I can to the intermediate data structure" (PDF p. 180); parameters the first phase does not touch (the shipping method) stay as direct arguments of the second phase.
4. Extract the first-phase code into a function that returns the intermediate structure.

```
// before: pricing and shipping interleaved in one function
function priceOrder(product, quantity, shipping)
    basePrice = product.basePrice * quantity
    discount  = max(quantity - product.discountThreshold, 0) * product.basePrice * product.discountRate
    perCase   = basePrice > shipping.discountThreshold ? shipping.discountedFee : shipping.feePerCase
    return basePrice - discount + quantity * perCase
```

```
// after: two phases joined by an explicit intermediate record
function priceOrder(product, quantity, shipping)
    return applyShipping(calculatePricingData(product, quantity), shipping)

function calculatePricingData(product, quantity)
    basePrice = product.basePrice * quantity
    discount  = max(quantity - product.discountThreshold, 0) * product.basePrice * product.discountRate
    return PriceData(basePrice, quantity, discount)

function applyShipping(priceData, shipping)
    perCase = priceData.basePrice > shipping.discountThreshold ? shipping.discountedFee : shipping.feePerCase
    return priceData.basePrice - priceData.discount + priceData.quantity * perCase
```

A first phase may itself be an enriching transform ([[combine-functions-into-transform]]).

## When to run it

This wiki reads Fowler's motive as the condition: a second consumer of the computed values exists or is being added (an HTML statement beside the text one), or the calculations are to be tested apart from the layout. With one output, in a function small enough to read at once, the split buys only the separation and the code grows (see *Trade-offs*); this limit is this wiki's reading, the source does not state it.

The catalogue makes the value of the split conditional in the same way. Fowler calls his pricing example trivial, and the split pays "If I have changes coming up that complicate the pricing and shipping calculations, but they work relatively independently" (PDF p. 178). This wiki reads that as: a short function whose two runs are a few lines each and change together gains little. A further limit of this wiki's own: if the second run reads the first group of inputs throughout, not only a few computed values, the halves are not independent phases, and the intermediate record would carry most of the first phase's inputs and separate nothing.

A single formatting conversion stays with the renderers. Fowler kept `usd` out of the data and moved it to the top level so both renderers could share it (PDF p. 40), rather than putting formatted strings into the intermediate record.

## Procedure

Fowler's sequence, each step followed by compile-test-commit ([[refactor-in-small-tested-steps]]):

1. [[extract-function]] on the whole rendering part into `renderX(...)`; the original function now only calls it.
2. Create an empty intermediate record in the caller and pass it to `renderX` as an extra parameter.
3. Move one input at a time into the record (`customer`, then `performances`) and remove the corresponding parameter from `renderX` as soon as it is no longer read.
4. Enrich each item in the record with the values the renderer computes: copy the item and add the looked-up and calculated fields (`play`, `amount`, `volumeCredits`), moving each calculation function into the first phase. Copy rather than modify the inputs ([[do-not-mutate-input-data]]).
5. Move the totals into the record too. Fowler passes the record to the totals functions as an explicit parameter even though it is in scope: "I prefer to pass the explicit parameter" (PDF p. 38).
6. Extract the first phase into its own function, `createData(inputs)`. The top-level function becomes `render(createData(inputs))`, and a second format is `renderOther(createData(inputs))`.

A side benefit Fowler records: once the phases are split, work on the calculations can ignore formatting "so long as I produce the same output data structure", and tests can probe that intermediate structure directly (PDF pp. 43-44).

## Example

```
function statement(invoice, plays)
    result = "Statement for " + invoice.customer
    for perf in invoice.performances
        play = plays[perf.playId]
        result += play.name + ": " + money(amountFor(perf, play))
    result += "Owed: " + money(totalAmount(invoice, plays))
    return result
```

```
function statement(invoice, plays)
    return renderText(createStatementData(invoice, plays))

function htmlStatement(invoice, plays)
    return renderHtml(createStatementData(invoice, plays))

function createStatementData(invoice, plays)
    function enrich(perf)
        copy = shallowCopy(perf)
        copy.play = plays[perf.playId]
        copy.amount = amountFor(copy)
        return copy

    data = new record
    data.customer = invoice.customer
    data.performances = map(invoice.performances, enrich)
    data.totalAmount = sum(data.performances, p -> p.amount)
    return data

function renderText(data)
    result = "Statement for " + data.customer
    for perf in data.performances
        result += perf.play.name + ": " + money(perf.amount)
    result += "Owed: " + money(data.totalAmount)
    return result
```

In the after, neither renderer calls a calculation or reads `plays`; they read fields of `data` only.

## Trade-offs

The code grows. Fowler counts 70 lines against the original 44 and answers: "If all else is equal, more code is bad—but rarely is all else equal" (PDF p. 42). The gain he names is that the parts can be understood separately and the HTML version needs no duplicated calculation (PDF p. 43). See [[easier-to-change]].

The intermediate structure is also a place to hide a decision. Fowler later fills it from a polymorphic calculator but keeps returning plain data so that the renderers do not learn about the calculator (PDF p. 54). See [[replace-conditional-with-polymorphism]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Split Phase", PDF pp. 176-182: the rule, the two typical cases, the clue of different data and functions, the compiler model, the general mechanics, the preference to move as much as possible into the intermediate structure and the conditional value of the split. This wiki's own for that part: applying it at the level of functions, the dependent-halves limit, the assignment of the sequential shape to [[routine-cohesion]], and the pricing pseudocode. Ch. 1, "Splitting the Phases of Calculation and Formatting" and "Status: Separated into Two Files (and Phases)", PDF pp. 31-44; Split Phase is catalogued as (154). The steps, the explicit-parameter preference, the testing benefit and the line counts are Fowler's. This wiki's own: the reading of the motive as the condition for running it, the one-output limit, the assignment of the sign to [[logic-testable-without-ui]], and the pseudocode.
