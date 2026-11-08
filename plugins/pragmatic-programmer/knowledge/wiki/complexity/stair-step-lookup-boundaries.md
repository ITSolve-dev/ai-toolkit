---
title: Stair-step lookup boundaries
category: complexity
summary: "A range-to-category lookup loop over a bounds array where the comparison (< vs <=) does not match the stated ranges, the top range has no bound or sentinel, or values at the boundaries are untested."
tags: [rule, table-driven, boundary-conditions, off-by-one]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A stair-step table maps a value to the range it falls in by comparing it with each range's upper bound (see [[choose-table-access-scheme]]). The scheme moves the ranges into data, but the comparison that walks them stays in code, and that is where McConnell locates its errors.

## Rule

Make the comparison match the ranges' stated boundaries, and handle the top range on purpose. The book says to make sure the upper bound of every range is accounted for. Write the search so it finds every range except the top one, let the rest fall into the top one, and sometimes add an artificial upper bound for the last range (p. 421). Its warning: «Не ошибитесь с операциями < или <=!» Make sure the loop ends correctly for values in the top range and that range boundaries are handled right (p. 421). A binary search used instead must find where the value falls, not the value, and must treat the boundary points as a special case (pp. 421-422). The search itself belongs in its own routine (p. 422).

The book's grading table states B as "< 90.0%" and A as "≥ 90.0%" (p. 420). Its loop tests `studentScore < rangeLimit(gradeLevel)`, so a score of exactly 90.0 falls to A, which agrees with the spec (p. 420).

## Sign in code

- A loop over a bounds array whose comparison operator does not match how the ranges are written down. Example: ranges stated as "below 90 is B" but the code tests `score <= bound[i]`.
- No bound, no sentinel and no explicit fallback for the top range, so a value above the last bound leaves the result unset or reads past the array.
- The "not found yet" marker is also a valid result. This is this wiki's observation on the book's own listing, which starts with `studentGrade = "A"` and loops while it is still "A". That works only because A is the top grade.
- Tests that do not exercise a value exactly on each bound, and one above the top bound.

## When not to apply

- The ranges come from a library routine that already searches sorted bounds, such as a bisect or lower-bound function. This wiki's view is that the check then shrinks to whether the routine's side convention (left or right) matches the ranges.
- The ranges are of equal width, so a transformation such as integer division gives a direct key. This wiki points to [[isolate-table-key-computation]] for that case.

## Repair

1. Write down each range with its closed or open ends, and choose `<` or `<=` from that.
2. Give the top range an explicit fallback after the loop, or a sentinel bound, instead of an initial value that doubles as the answer.
3. Put the search in one routine with the bounds and results as parameters.
4. Test a value just below, on and just above every bound, plus values below the first and above the last (see [[test-boundaries-and-realistic-use]], [[check-loop-boundaries-by-hand]]).

## Before and after

Before: `<=` puts 90.0 in B though the spec says A, and the top grade doubles as "not found".

```
bounds = [50, 65, 75, 90]
grades = ["F", "D", "C", "B"]
grade = "A"
i = 0
while grade == "A" and i < len(bounds):
    if score <= bounds[i]: grade = grades[i]
    i = i + 1
```

After: the comparison matches "below the bound", and the top range is an explicit fallback.

```
function gradeFor(score, bounds, grades, top):
    for i in 0 .. len(bounds) - 1:
        if score < bounds[i]: return grades[i]
    return top

grade = gradeFor(score, [50, 65, 75, 90], ["F", "D", "C", "B"], "A")
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 18.4, pp. 420-422. The boundary advice, the `<`/`<=` warning, the binary search caution and the separate-routine rule are the book's. The signs, the observation on the listing's marker value, the limits, the test list and the pseudocode are this wiki's own. Related: [[choose-table-access-scheme]].
