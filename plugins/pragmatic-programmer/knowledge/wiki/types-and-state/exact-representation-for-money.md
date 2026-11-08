---
title: "Keep money and other balancing quantities out of floating point"
category: types-and-state
summary: "A monetary amount, or another quantity that must balance to the last unit, held in a float or double with cents as its fractional part, often with round(x, 2) calls scattered after arithmetic to make totals come out right."
tags: [rule, money, floating-point, rounding, domain-types, formatting]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

Floating values round (see [[floating-point-precision]]). For most quantities the rounding is tolerable; for dollars and cents, and for anything else that must balance exactly, *Code Complete* says it is not, and lists representations that avoid it (Russian edition, p. 288).

## Rule

Hold quantities that must balance exactly in a representation without binary rounding. The book lists these remedies for rounding errors in general, in this order, and ties exact balance to the decimal option (p. 288); this wiki applies the whole list to exact quantities:

- **A higher-precision floating type.** This wiki adds that it reduces the error without removing it.
- **A decimal type** (the book's binary-coded decimal). Usually slower and larger, it prevents many rounding errors, which the book says matters most for dollars and cents and other quantities that must balance.
- **Integers in the smallest unit.** Count cents in an integer, possibly a 64-bit one, and treat dollars as multiples of 100 cents. The book calls this efficient in both speed and accuracy, and suggests hiding it behind a class such as `DollarsAndCents` that keeps the integer representation private and offers the numeric operations needed.
- **A built-in type made for this.** If the language or its libraries offer a currency or decimal type, use it (p. 288).

Fowler's *Refactoring* adds a practice for the integer option. He calls storing money as integer cents a common approach: it avoids the dangers of fractional monetary values in floats and still allows ordinary arithmetic. Whenever such an amount is displayed a decimal is needed, so his formatting function performs the division (2nd ed., ch. 1, PDF p. 24). This wiki reads that as: the conversion from the smallest unit belongs in one formatting function, not at each call site.

## Sign in code

- A field, parameter or variable named for an amount, price, balance or fee, declared with a binary floating type.
- Rounding calls (`round(x, 2)`) scattered after arithmetic on amounts to make totals come out right.
- A comparison of totals with a tolerance where the domain requires exact balance.
- Amounts held in integer cents with the division by 100 repeated at each place they are formatted (`format(amount / 100)`, `format(total / 100)`) (Fowler, PDF pp. 23-24).

This wiki assigns neighbouring cases as follows. This page owns the choice of representation for exact quantities. Comparisons and accumulation on values that are legitimately approximate are [[floating-point-precision]]. A bare number with no unit is [[representation-that-fits-by-coincidence]]; once the amount has its own type, [[define-domain-types]] owns how that type is named and declared. Conversion from the smallest unit repeated at each formatting site is [[exact-representation-for-money]]; other knowledge written twice is [[dry]].

## When not to apply

The book states no limits here. The limits below are this wiki's own:

- **Estimates, statistics and forecasts** expressed in money, which are never booked or balanced, tolerate floating values.
- **Multi-currency or fractional-unit amounts** (fractions of a cent in interest, currencies with three decimals) need a decimal type or a per-currency scale; a plain integer of cents is then wrong, and so is a fixed division by 100 in the formatter. The unit has to travel with the amount.
- **A project convention or a library money type** decides the representation; the page fires only where none is used.
- **Cost when followed:** decimal arithmetic is slower and larger, and an integer-of-cents scheme needs explicit rules for division and rounding (splitting 100 into three), which the representation does not decide for you.

## Repair

1. Choose one representation: the platform's decimal or money type if it exists, otherwise integers in the smallest unit.
2. Wrap it in one type for the amount, so that construction, arithmetic and rounding live in one place.
3. Make division and allocation explicit operations of that type with a stated rounding rule.
4. Convert to and from text or floating values only at input and output, in one formatting function that takes the smallest unit (Fowler's `usd(aNumber)`, PDF p. 24), and pass it raw cents everywhere.

## Before and after

```
price = 19.99
total = price * 3
if total == 59.97
  ...
share = round(total / 3, 2)
```

```
price = Money.cents(1999)
total = price.times(3)
if total == Money.cents(5997)
  ...
shares = total.split(3)
```

Fowler's case, the division moved into the formatter:

```
text += format(amountFor(perf) / 100)
text += "Amount owed is " + format(total / 100)
```

```
function usd(cents): return currencyFormatter("USD")(cents / 100)
text += usd(amountFor(perf))
text += "Amount owed is " + usd(total)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12, p. 288: rounding repairs, the decimal type for dollars and cents, integers of cents and the `DollarsAndCents` class, and language-provided currency types. This wiki's own: the application of the whole list to exact quantities, the remark that higher precision does not remove the error, the signs, all limits, the split with neighbouring pages, repair steps 3 and 4, and the pseudocode.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Removing the format Variable", PDF pp. 23-24: the integer-cents practice and the division inside the formatter. This wiki's own for that part: the reading as one formatting function, the fourth sign as phrased and its split with [[dry]], and the fixed-division limit on currencies.
