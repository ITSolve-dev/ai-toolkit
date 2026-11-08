---
title: Order multi-way branches deliberately
category: complexity
summary: "A switch or if-else-if chain of about ten or more arms whose labels follow no discernible order (not alphabetic or numeric, not by frequency, the one normal case buried among error codes), so finding one label means reading them all; an if chain testing a rare case first."
tags: [rule, conditionals, switch, if-else, readability, performance]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

In a short branch the order of arms barely matters. In a long one, such as a `case` handling dozens of events in an event-driven program, McConnell says it does, and offers three orders (p. 353). The key points sum up: for `if`-`then`-`else` chains and `case` statements, choose the order that improves readability (p. 358).

## Rule

- **Most likely first.** In an `if`-`then`-`else` chain, test the most frequent cases first: a reader looking for the usual case reads less code about exceptional ones, and the code runs fewer tests in most cases (p. 351). The book's example moves the letter test ahead of punctuation and the rare control-character test to the end (pp. 351-352).
- **For a `case`, one of three orders** (p. 353):
  - alphabetical or numerical, when all cases are equally important, so the reader can find the one wanted;
  - the normal case first, when there is one correct case and several exceptions, with a comment marking which is normal;
  - by frequency, so readers see the common cases first and a linear scan finds them sooner.

## Sign in code

- A `switch` or chain of roughly ten or more arms (this wiki's threshold) where the labels follow neither alphabetical nor numeric order, nor any stated order, so finding one label means reading them all.
- A chain in which the one normal outcome sits somewhere in the middle of a list of error codes.
- An `if`-`else if` chain of mutually exclusive tests that tests first a case the code itself marks as rare (a comment, an internal-error or control-character arm, a counter or profile figure) before the common one, as in the book's example (pp. 351-352).

This wiki assigns the neighbouring cases as follows. This page owns the order of arms in a multi-way `if`-`else if` chain or a `case` whose arms do different work. An `if`-`else if` chain whose every arm only assigns a category from one input compared with literal lists or ranges is [[drive-repeated-dispatch-from-a-table]]; once it is a table, the order of arms is moot. The order of the two branches of one `if`/`else` in nested status checks is [[nominal-path-first]].

## When not to apply

The book's own: with three cases and three lines it hardly matters (p. 353). This wiki's own limits:

- **Reordering an `if` chain can change its meaning.** If the conditions overlap, the first true test wins, and moving a test changes which arm runs. Reorder only when the tests are mutually exclusive, or after making them so. A `case` with distinct labels has no such risk.
- The performance half of the argument needs evidence. This wiki notes that many compilers turn a dense `switch` into a jump table, where order costs nothing, and an `if` chain rarely shows in a profile. Order for the reader unless a measurement says otherwise.
- The tuning chapter measured the speed half and found it unreliable: reordering `case` arms by frequency saved 7% in Visual Basic, nothing in Java, and made C# 18% slower; the same reordering of an `if`-`then`-`else` chain saved 26-50%, and which of `case` and `if`-`then`-`else` was faster flipped between languages with no logical explanation (pp. 598-600). This wiki takes from those figures that frequency order is chosen for the reader who looks for the common case, and that speed is never its justification without a measurement; see [[premature-code-tuning]].
- Frequency is a forecast about the data. Where nobody knows it, alphabetical or numeric order is the one a reader can check.

## Repair

1. Decide which order serves this branch: lookup (alphabetical or numeric), one normal case (normal first), or a skewed distribution (frequency).
2. For an `if` chain, confirm the tests do not overlap before moving any.
3. Reorder, and say in a comment which order is used when it is not self-evident.

## Before and after

```
# tokenizer loop body
if isControl(c):            # rare: control characters
    log.warn("control char", pos)
    skip()
else if isPunct(c):
    flush(word)
    emit(PUNCT, c)
else if isDigit(c):
    number = number * 10 + digit(c)
else if isLetter(c):
    word.append(c)
else:
    internalError("unexpected character type")
```

```
# tokenizer loop body
if isLetter(c):             # most common
    word.append(c)
else if isPunct(c):
    flush(word)
    emit(PUNCT, c)
else if isDigit(c):
    number = number * 10 + digit(c)
else if isControl(c):       # rarest
    log.warn("control char", pos)
    skip()
else:
    internalError("unexpected character type")
```

The tests are mutually exclusive, so the order can follow frequency. The arms do different work, so the chain is not a table candidate.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, pp. 351-352 (most likely first); section 15.2, p. 353 (three orders for `case`); key points, p. 358; section 26.1, pp. 598-600: the measured effect of frequency ordering. The arm-count threshold, the overlap warning, the jump-table caution, the reading of the chapter 26 figures, the forecast limit, the wording of the rare-case sign, the hand-off of constant-assigning chains to [[drive-repeated-dispatch-from-a-table]] and the pseudocode are this wiki's own; the pair keeps the book's four character classes but gives the arms different work.
