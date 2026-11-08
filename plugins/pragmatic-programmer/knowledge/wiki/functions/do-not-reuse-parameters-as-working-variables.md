---
title: Do not reuse parameters as working variables
category: functions
summary: "A routine assigns to its own input parameter (x = x * factor) and reads it again afterwards, so below that line the parameter's name no longer holds what the caller passed."
tags: [rule, parameters, mutation, local-variables]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell calls using a routine's parameters as working variables dangerous and asks for local variables instead (*Code Complete*, p. 173). His example multiplies and adds into the input variable, and his annotation on the line before `return` reads: «Переменная inputVal уже не содержит входного значения.» (p. 173).

## Rule

Keep an input parameter holding the value that was passed in. Do intermediate work in a local variable that starts as a copy. The book's reasoning (pp. 173-174):

- After the reassignment the parameter's name lies. It holds a result partly derived from the input, not the input.
- Someone who later needs the original value elsewhere in the routine will reach for the parameter, assume it still holds the original, and be wrong.
- Renaming does not fix it. `workingVal` hides that the value came from outside, and a name that says both is absurd. The book adds that its own names in the example are only illustrations: «Имена inputVal и workingVal просто ужасны» (p. 174).
- Copying into a working variable shows that the value came from outside and rules out changing the parameter by accident. Where the language can mark a parameter read-only, the compiler enforces this (p. 174).

The opening bad example (p. 158) shows the neighbouring defect, a write into an input record: `inputRec` is changed inside the routine. If it is an input it should not be changed, and in C++ it should have been declared `const`; if changing it is intended, it should not be called `inputRec` (p. 158). That shape is [[mark-input-only-parameters]] and [[do-not-mutate-input-data]], not this page.

Fowler's *Refactoring* covers the same case under Split Variable, which absorbed the first edition's *Remove Assignments to Parameters* (2nd ed., ch. 9, PDF p. 268): an input parameter reassigned so that it doubles as the result means what the caller passed on one line and what the routine will return on the next (PDF p. 272). His repair copies the parameter into a local at the top and names the local for the result, so the parameter keeps the input's name. He then reads the *original input* in conditions that are about the input, not the accumulator, even where the two are coincidentally equal (PDF p. 272). He notes in passing that with JavaScript's call-by-value parameters the caller never sees the assignment (p. 272).

## Sign in code

- An assignment whose target is a parameter of the enclosing routine (`count = count - 1`, `path = normalise(path)`), with the parameter still read after that line.

This wiki assigns the neighbouring case as follows. A function that writes fields of a plain record or element it received as an argument is [[do-not-mutate-input-data]]; a method that calls a mutator on an object it received, or a class whose fields are reassigned after construction, is [[immutable-objects]]. This page owns reassignment of the parameter variable itself. Whether the signature declares a parameter input-only is [[mark-input-only-parameters]].

## When not to apply

- **A parameter not read again.** This wiki adds a limit, and it narrows the book's reason: the book objects that the name itself misleads once the value is no longer the input (p. 173), whether or not it is read again. Reassigning a parameter once at the top to normalise it (`name = trim(name)`) and never using the raw value afterwards leaves nothing to misread. A project or language convention that forbids even this still overrides that permission.
- **An in-out parameter.** Writing to a parameter whose declared role is in-out is its purpose. That is the case the book separates from `inputRec`. Whether the routine should mutate its argument at all is the business of [[command-query-separation]], [[do-not-mutate-input-data]] and [[immutable-objects]].
- **Languages where parameters cannot be reassigned.** This wiki notes the defect cannot arise there and the rule has nothing to check.

## Repair

Introduce a local initialised from the parameter, named for what it holds, and do all the work on it. Then mark the parameter read-only if the language allows.

## Before and after

```
routine Price(amount)
    amount = amount * TaxMultiplier(amount)
    amount = amount + ShippingFor(amount)
    log "price for", amount       // meant the original amount
    return amount
```

```
routine Price(amount)
    price = amount * TaxMultiplier(amount)
    price = price + ShippingFor(price)
    log "price for", amount
    return price
```

Fowler's discount example, in this wiki's pseudocode:

```
function discount(inputValue, quantity)
  if inputValue > 50  then inputValue = inputValue - 2
  if quantity > 100   then inputValue = inputValue - 1
  return inputValue
```

```
function discount(inputValue, quantity)
  result = inputValue
  if inputValue > 50  then result = result - 2
  if quantity > 100   then result = result - 1
  return result
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.5, pp. 173-174; the opening example and its defect list, p. 158 ([[code-complete]]). The rule, its reasoning and the failure of renaming as a fix are the book's.
- Fowler, *Refactoring*, 2nd ed., ch. 9, Split Variable, PDF pp. 268 and 272, via [[fowler-refactoring]]: the parameter case, the copy-and-rename repair, reading the original input in conditions, and the call-by-value setting.
- The sign, the owner split with [[do-not-mutate-input-data]] and [[immutable-objects]], the limits and the pseudocode are this wiki's own.

Related: [[parameter-order]], [[routine-review-checklist]].
