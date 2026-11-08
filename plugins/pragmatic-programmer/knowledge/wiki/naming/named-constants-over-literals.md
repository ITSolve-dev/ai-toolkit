---
title: "Name every literal except 0 and 1"
category: naming
summary: "A bare number, character or string literal in logic or a loop bound (99, 12, 0x1B, 'Gigamatic'), or one value written as a named constant in one place and as the literal (or literal±1) in another."
tags: [rule, magic-numbers, constants, literals, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A *magic number* is a literal such as 100 or 47524 that appears in code with no explanation; a magic character or string is the same thing for text (*Code Complete*, Russian edition, pp. 283, 289). McConnell's rule is to replace them with named constants, and his limit is narrow: «используйте в программе как константы только 0 и 1, а любые другие числа определите как литералы с понятными именами» (p. 283).

## Rule

Give every literal that carries meaning a name, and use that name everywhere the meaning occurs. The book gives three reasons (p. 283):

- **Changes are safer.** With a name, nobody hunts for every 100 and accidentally changes a 100 that means something else.
- **Changes are easier.** When the maximum goes from 100 to 200, a literal forces a search for 100, and also for the derived 101 and 99. A named constant changes in one place.
- **Code reads better.** `for i = 0 to 99` invites a guess; `for i = 0 to MAX_ENTRIES-1` does not.

The book extends this to values that will never change: «Даже если вы считаете, что литеральное значение безопасно, используйте вместо него именованную константу.» (p. 301). Its example is a loop to 12 over monthly profit: the number of months will not change, but the reader still has to guess what 12 is. Its last step goes past the constant to a meaningful loop index and, where possible, an enumerated range (`for month = Month_January to Month_December`), see [[enum-instead-of-codes-and-flags]].

The book also forbids mixing: one entity named by a constant in one place and by its literal in another. «Некоторые приемы программирования напрашиваются на ошибки, а этот просто доставляет вам ошибки на дом.» (p. 301). Whoever changes the constant believes the change is complete, and the forgotten literal produces a defect that is hard to trace.

For literal strings the book adds reasons of its own (p. 289): user-visible text such as a product name changes between versions, text kept in one resource is far easier to translate than text scattered through code, and on memory-constrained systems text independent of code is easier to manage.

## Sign in code

- A numeric literal other than 0 or 1 in a condition, a loop bound, an array size or an arithmetic expression: `if count > 37`, `for i = 1 to 12`, `buffer[256]`.
- A literal derived by hand from another value: `size + 1` is fine, but a bare 101 or 99 beside a 100 is the same knowledge written three times.
- A character code compared directly: `if input_char == 0x1B`.
- A user-visible or protocol string literal inside logic rather than in one named place.
- A named constant whose value also appears as a bare literal elsewhere for the same purpose. This is the most dangerous form on the page.

This wiki assigns neighbouring cases as follows. This page owns a bare literal and the constant-versus-literal mix. Where a literal bounds a loop that indexes an array, [[array-index-discipline]] owns it and the repair takes the bound from the array; a literal elsewhere is [[named-constants-over-literals]]. A constant that exists but is named for its value (`FIVE`, `TWELVE`) is [[constant-names-abstract-not-value]]. A meaningful literal written bare, once or repeatedly, is [[named-constants-over-literals]]; a literal repeated inside a repeated expression or decision, and a fact restated in any other form, is [[dry]]. A literal that must differ between deployments or customers is [[parameterize-with-external-configuration]], and the choice of binding a value later than compile time, or a value bound later than any requirement needs, is [[binding-time]]. A named constant made public and read by unrelated classes that each wrap it, or passed in to select behaviour, is [[no-public-constants]]. A set of related integer codes (1 = red, 2 = green) is [[enum-instead-of-codes-and-flags]]; a status variable named `flag` and tested against such numbers is [[status-variable-not-flag]] for its name. Where user-visible text should live for translation is [[one-internal-string-format]].

## When not to apply

The book's own exception is 0 and 1 used to start a loop, increment, decrement or address the first element (p. 283). The items below are this wiki's own:

- **A value whose meaning is the value itself** and is fixed by mathematics or an outside specification inside a formula whose name already explains it (`2` in `radius * 2` inside `diameter()`, `100` in a function named `toPercent`). A name such as `TWO` adds nothing.
- **Test data.** A literal input and its expected output in a test are the specification of that case; naming them hides the case from the reader.
- **A literal used once, inside a well-named function whose whole body explains it.** The book would still name it; this wiki treats it as a judgement call when the name could only restate the function's name.
- **A project convention** on where constants live overrides the placement advice. The book's fallback to global variables where a language lacks constants (p. 283) is a language matter and is not carried here.

## Repair

1. Name the literal after what it means in the problem, not after its value (`MAX_ENTRIES`, not `ONE_HUNDRED`).
2. Declare it in the narrowest scope that covers all its uses; the book gives the order local, then class, then global for constants imitated with variables or classes (p. 301), and this wiki applies it generally.
3. Replace every occurrence that carries this meaning, including derived values (`MAX_ENTRIES - 1`, not 99). Leave alone occurrences of the same digits that mean something else.
4. Search for the old literal once more before finishing; the book suggests a text search for the digits 2 to 9 to catch stray ones (p. 301).

## Before and after

```
for i = 1 to 12
  profit[i] = revenue[i] - expense[i]

if input_char == 0x1B
  cancel()

if attempts >= 5
  giveUp()
remaining = 5 - attempts
```

```
for month = FIRST_MONTH to LAST_MONTH
  profit[month] = revenue[month] - expense[month]

if input_char == CANCEL_KEY
  cancel()

if attempts >= MAX_ATTEMPTS
  giveUp()
remaining = MAX_ATTEMPTS - attempts
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: magic numbers, the three reasons and the 0-and-1 rule, p. 283; magic characters and strings, p. 289; named constants as parameterization and in declarations, pp. 299-300; even safe literals, the 12-months loop and the mixing warning, pp. 300-301; scope order, p. 301. The quotations are transcribed from `raw/` and need the page-image check. This wiki's own: the sign list as worded, the split with neighbouring pages, the limits other than 0 and 1, the general use of the scope order, and the pseudocode.
