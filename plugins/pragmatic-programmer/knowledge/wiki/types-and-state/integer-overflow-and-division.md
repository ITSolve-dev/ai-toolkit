---
title: "Check integer division, overflow and zero divisors"
category: types-and-state
summary: "An integer division before a multiplication (10 * (7/10)), a product or sum of integers with no bound on the inputs, an intermediate product that exceeds the type even though the result fits, a division whose divisor can be zero, or an integer compared with a float without an explicit conversion."
tags: [rule, integers, overflow, division, arithmetic]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Integer arithmetic differs from arithmetic on paper in three ways that *Code Complete* treats as routine sources of defects: division truncates, values have a maximum, and a divisor can be zero (Russian edition, pp. 283-286). Each shows as a specific expression shape.

## Rule

- **Order integer division last.** On paper 10 * (7/10) equals (10*7)/10; in integers «10 * (7/10) равно 0, потому что целочисленное деление (7/10) равно 0» (p. 284). What 7/10 yields at all depends on the language. The book's simplest repair is to rearrange so divisions happen last.
- **Bound every term of an integer expression.** The book's procedure: for `m = j * k`, take the largest value each operand can hold and multiply. With j ≤ 200 and k ≤ 25 the product fits; with j ≤ 200 000 and k ≤ 100 000 it is 20 000 000 000 and exceeds a 32-bit integer, so a wider type is needed (p. 285). It adds that expected growth over the program's life counts.
- **Check intermediate results, not only the final one.** The book's Java example computes `1000000 * 1000000 / 1000000` and prints 727, because the intermediate product overflowed before the division (pp. 285-286). The repair is the same as for overflow: a wider integer or a floating type for the computation.
- **Think about zero at every division.** Wherever a divisor can be 0, write code that prevents the failure (p. 283).
- **Make conversions between numeric types explicit, and do not compare values of different types.** Different compilers convert differently; an explicit conversion says what the writer meant. Comparing an integer with a floating value, such as `if i = x`, almost never behaves as intended (p. 284).

## Sign in code

- An integer division whose result is then multiplied: `a / b * c` with integer operands.
- A multiplication or sum of integers whose operands come from input, counts or accumulated values, with no stated bound and no wider type for the result.
- An expression whose final value fits the type but which multiplies before it divides (`a * b / c`), with a and b large.
- A division by a variable with no check or contract excluding zero before it.
- An equality or ordering comparison between an integer variable and a floating one, or an expression that mixes them without an explicit conversion.

This wiki assigns neighbouring cases as follows. This page owns integer range and truncation, and mixed integer-floating comparisons. Equality and accumulated error on floating values is [[floating-point-precision]]. Money stored as a floating value is [[exact-representation-for-money]]. Logic that assumes `a + 1 > a` is already owned by [[assert-the-impossible]].

## When not to apply

The book states no limits here. The limits below are this wiki's own:

- **A language with arbitrary-precision integers by default** removes the overflow sign; truncating division and zero divisors remain.
- **Bounds proven by the code in view**, such as an index into a fixed-size array multiplied by a small constant, need no wider type. The sign is an unbounded operand, not every multiplication.
- **Deliberate wraparound** in hashing, checksums or modular arithmetic is the intended behaviour; it should be named as such where it happens.
- **A divisor guaranteed non-zero by a contract checked earlier** needs no second check; see [[caller-owns-the-precondition]].
- **Cost when followed:** a wider type costs memory and sometimes speed in bulk data; the book's procedure is to widen only where the bounds require it.

## Repair

1. For each integer division, move it after the multiplications, or compute in a type that keeps the fraction if the fraction matters.
2. For each product or sum, write down the largest value of each operand, compute the largest result and every intermediate, and widen the type of the computation if any exceeds the range.
3. For each division by a variable, establish that it cannot be zero, either by a check with a defined outcome or by a precondition stated and checked at the boundary.
4. Replace implicit mixed-type arithmetic and comparisons with an explicit conversion to the type the comparison should happen in.

## Before and after

```
percent = done / total * 100
scaled = big_a * big_b / SCALE
if count == ratio
  ...
```

```
if total == 0
  return NO_PROGRESS
percent = (wide(done) * 100) / total
scaled = wide(big_a) * wide(big_b) / SCALE
if count == to_int(round(ratio))
  ...
```

In the last line the writer chose to compare in integers, converting the float explicitly; the conversion target is a decision the writer has to make, and the book's point is that the writer, not the compiler, makes it.

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: division by zero, p. 283; explicit conversions and mixed-type comparisons, p. 284; integer division, p. 284; overflow and the bounding procedure with the integer ranges table, pp. 284-285; intermediate overflow and the 727 example, pp. 285-286. The quotation of p. 284 is transcribed from `raw/` and needs the page-image check. This wiki's own: the signs as worded, all limits, the splits with neighbouring pages, and the pseudocode.
