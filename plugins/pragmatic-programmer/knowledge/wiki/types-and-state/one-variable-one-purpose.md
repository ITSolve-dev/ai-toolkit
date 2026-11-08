---
title: One variable, one purpose
category: types-and-state
summary: "One local variable, often named temp, x, acc or tmp, given two plain assignments (x = ..., not x = x + ...) with values of different meaning in the same routine, such as a discriminant reused as the swap slot or one acceleration overwritten by another; the reuse forces a name that fits neither job."
tags: [rule, variables, reuse, temp, naming]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

When one variable is used for two unrelated jobs, the code suggests the two jobs are related when they are not. McConnell's other argument is about names: such a variable ends up with a name that fits one purpose only, or with a "temporary" name such as `x` or `temp` that fits neither (p. 249).

## Rule

«Используйте каждую переменную только с одной целью» (p. 249). In the book's example, `temp` holds `Sqrt(b*b - 4*a*c)` for the roots of a quadratic equation and later holds a root during a swap. The book asks what links the first `temp` to the second and answers: nothing (p. 249). Splitting it into `discriminant` and `oldRoot` makes the code clearer (p. 249). The book makes the same point about variables with hidden meaning (p. 250): the clarity two variables give is worth far more than the resources they cost. Its cross-reference extends the rule to routine parameters, which should also have only one purpose (p. 249); this wiki keeps that case on [[do-not-reuse-parameters-as-working-variables]].

Fowler's *Refactoring* catalogues the repair as **Split Variable** (formerly *Split Temp* and *Remove Assignments to Parameters*; 2nd ed., ch. 9, PDF p. 268). A variable that holds the result of a piece of computation for later reference should be set once: "If they are set more than once, it is a sign that they have more than one responsibility within the method", and "Any variable with more than one responsibility should be replaced with multiple variables, one for each responsibility" (PDF p. 269). His reason is the reader's: "Using a variable for two different things is very confusing for the reader" (p. 269). His example is `acc`, which holds the acceleration from the primary force and is then reassigned to the acceleration from both forces (p. 270).

## Sign in code

- Within one routine, a local variable is assigned and then reassigned with a value of a different meaning, and no read in between links the two values.
- A generic name (`temp`, `tmp`, `x`, `val`, `result`) covers two separate stretches of a routine with unrelated values.
- A local with two or more plain assignments (`x = ...`, not `x = x + ...`) whose right-hand sides compute different quantities, so that a reader can name the first use or the second, not both. This wording is this wiki's, after Fowler's `acc` (p. 270).

This wiki assigns the neighbouring cases as follows. This page owns a local variable reassigned to an unrelated meaning. A generic name on a variable with a single purpose is [[temporary-variable-names]]; where both apply, split here first, then name each part. Reassignment of a routine's own parameter is [[do-not-reuse-parameters-as-working-variables]]. A single variable whose value ranges encode different meanings at the same time (-1 means an error, values above 500 000 mean an account) is [[hybrid-coupling]]. Reassigning an object's field after construction is [[immutable-objects]].

## When not to apply

The limits below are this wiki's own, except the loop and collecting-variable exception, which is Fowler's (PDF p. 269):

- A variable updated step by step towards one meaning, such as an accumulator, a cursor or a value refined in stages, has one purpose however often it is assigned. Fowler states the same two exceptions: loop variables, which change on each iteration by design, and collecting variables. If the later assignments have the form `i = i + something`, "that is a collecting variable, so don't split it": sums, string concatenation, writing to a stream, adding to a collection (PDF p. 269).
- A loop variable reused across consecutive loops of the same kind, such as `i` over two arrays, is a convention most readers expect. Report it only when the loops differ in meaning.
- In languages and styles with single-assignment bindings, such as functional code or `final`/`const` locals, the shape cannot arise. Shadowing a name with a new binding of a different meaning is the same problem in another form and gets the same repair.

## Repair

Declare a separate variable for each purpose, named for that purpose, and give each the smallest scope that covers its uses ([[smallest-scope-first]]). Where the language allows it, mark both `final`/`const` so that a third reuse cannot creep in.

Fowler's mechanics for doing it safely (PDF pp. 269-270):

1. Rename the variable at its declaration and first assignment, choosing a name for that first use only.
2. Declare the new variable immutable where the language allows, so a further assignment is a compile error.
3. Change every reference up to the second assignment; declare the variable afresh there. Test.
4. Repeat stage by stage until the final assignment; the original name disappears.

## Before and after

Before:

```
temp = sqrt(b*b - 4*a*c)
root[0] = (-b + temp) / (2*a)
root[1] = (-b - temp) / (2*a)
...
temp = root[0]
root[0] = root[1]
root[1] = temp
```

After:

```
discriminant_root = sqrt(b*b - 4*a*c)
root[0] = (-b + discriminant_root) / (2*a)
root[1] = (-b - discriminant_root) / (2*a)
...
old_root = root[0]
root[0] = root[1]
root[1] = old_root
```

Fowler's example, in this wiki's pseudocode; `result` stays, because its later assignment is `+=`, a collecting variable:

```
function distance(scenario, time)
  acc = scenario.primaryForce / scenario.mass
  primaryTime = min(time, scenario.delay)
  result = 0.5 * acc * primaryTime^2
  secondaryTime = time - scenario.delay
  if secondaryTime > 0
    primaryVelocity = acc * scenario.delay
    acc = (scenario.primaryForce + scenario.secondaryForce) / scenario.mass
    result += primaryVelocity * secondaryTime + 0.5 * acc * secondaryTime^2
  return result
```

```
function distance(scenario, time)
  final primaryAcceleration = scenario.primaryForce / scenario.mass
  primaryTime = min(time, scenario.delay)
  result = 0.5 * primaryAcceleration * primaryTime^2
  secondaryTime = time - scenario.delay
  if secondaryTime > 0
    primaryVelocity = primaryAcceleration * scenario.delay
    final secondaryAcceleration = (scenario.primaryForce + scenario.secondaryForce) / scenario.mass
    result += primaryVelocity * secondaryTime + 0.5 * secondaryAcceleration * secondaryTime^2
  return result
```

## Source

McConnell, *Code Complete*, Russian edition, via [[code-complete]], section 10.8, pp. 249-250: the rule, the poor-name argument, the quadratic-root example with `temp` split into `discriminant` and `oldRoot`, the extension to parameters (cross-reference on p. 249), and the remark, made in the book about variables with hidden meaning, that two variables waste nothing (p. 250). The book's example is C++. The pseudocode follows the book's example closely, with `discriminant_root` in place of the book's `discriminant` for the reason given on [[temporary-variable-names]]; the signs, the assignment against the neighbouring pages, the limits and the `final` step of the repair are this wiki's own.

Fowler, *Refactoring*, 2nd ed., ch. 9, Split Variable, PDF pp. 268-272, via [[fowler-refactoring]]: the rule, the reader's reason, the loop and collecting-variable exceptions, the mechanics and the `acc` example. This wiki's own for that part: the wording of the double-assignment sign and the pseudocode, after the book's JavaScript.
