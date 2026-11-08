---
title: Substitute an algorithm
category: change
summary: "Procedure for replacing a whole convoluted algorithm, or one duplicating a library function, with a clearer one: isolate it in one function, pin its behaviour with tests, swap, and compare outputs."
tags: [method, refactoring, algorithms, testing]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's *Refactoring* (2nd ed., ch. 7, "Substitute Algorithm") covers the case where small steps are not enough and the whole algorithm is replaced: "If I find a clearer way to do something, I replace the complicated way with the clearer way" (PDF p. 222). He names three occasions: learning more about the problem and seeing an easier way; adopting a library that duplicates the code; and wanting to change the algorithm slightly, when it is easier to replace it first with one that makes the change straightforward (p. 222).

Whether a hand-written part duplicates a library is decided on [[use-existing-components-before-writing-your-own]]; inline statements that an existing function already computes are [[replace-inline-code-with-function-call]]. This page is the procedure for swapping a whole algorithm once that decision is made.

## Precondition

Decompose first. "Replacing a large, complex algorithm is very difficult; only by making it simple can I make the substitution tractable" (p. 222). The chapter introduction names the pairing: wrap the algorithm in a function with Extract Function ([[extract-function]]), then substitute (p. 183).

## Procedure

1. Arrange the code to be replaced so that it fills one complete function.
2. Prepare tests that exercise only this function, to capture its behaviour.
3. Write the alternative algorithm.
4. Run static checks.
5. Run the tests to compare the output of the old algorithm with the new one. If they agree, the substitution is done. If not, keep the old algorithm as a reference for testing and debugging (p. 223).

This wiki reads step 5 as a differential test: the old function stays callable until the new one matches it on the same inputs, which makes a mismatch a concrete input to debug rather than a guess.

## Failure modes

These are this wiki's own reading of the steps above. Substituting an algorithm that still spans several functions or shares state with its caller makes step 2 impossible, so the swap lands without a reference. Tests written against the caller rather than the isolated function pin unrelated behaviour and fail for reasons other than the algorithm.

## Example

```
// before: isolated, but convoluted
foundPerson(people)
  for p in people
    if p == "Don" then return "Don"
    if p == "John" then return "John"
    if p == "Kent" then return "Kent"
  return ""
```

```
// after: same outputs on the pinned inputs
foundPerson(people)
  candidates = ["Don", "John", "Kent"]
  return people.find(p -> candidates.contains(p)) or ""
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 7, "Substitute Algorithm" (PDF pp. 222-223), and the chapter introduction (p. 183), via [[fowler-refactoring]]. The occasions, the decompose-first precondition, the procedure and the shape of the example are Fowler's. The differential-test reading, the failure modes, the pointers to neighbouring pages and the pseudocode are this wiki's own.

Related: [[refactor-in-small-tested-steps]], [[extract-routine-to-name-a-step]].
