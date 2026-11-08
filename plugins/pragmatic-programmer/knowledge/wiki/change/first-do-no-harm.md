---
title: First, do no harm
category: change
summary: "An added line handles a concern worse than its neighbours do: a dropped error, a bypassed check, a hard-coded value, a pasted copy, a reach across a layer."
tags: [rule, entropy, deadline, hotfix, collateral-damage]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

**First, do no harm** is the rule that urgency does not license collateral damage to code that is in good order. The book tells it through firefighters who stopped to roll out a mat so their hoses would not spoil a carpet (p. 36). The rule concerns what a change adds; for defects already present, see [[broken-windows]].

## Rule

Software is handled the same way as that carpet, «не нанося ему сопутствующий ущерб лишь потому, что оно находится в каком-то критическом состоянии» (p. 36). In clean code the care increases: even with a deadline, a release date or a demo pressing, «вы не должны стать первым, кто испортит все дело или нанесет дополнительный ущерб» (p. 36).

## Sign in code

The book gives none. This wiki takes the sign to be a relation between an added line and its neighbours: the region handles a concern one way, and the added line handles it another, worse way.

- a catch-all that drops an error, in a module where errors propagate;
- a check, validation or test bypassed by a flag or by a special case for one value;
- a literal where the neighbours read a setting;
- a pasted copy of a function with one line changed, where the neighbours take a parameter;
- a direct reach across a layer where the neighbours go through its interface.

A commit message saying hotfix or temporary often accompanies these, but the comparison with the neighbours is the sign. If the region has no consistent way of doing the thing, this sign does not fire, and the region is a case for [[broken-windows]].

This wiki assigns the neighbouring cases as follows. This page owns the comparison: an added line that departs from how its region handles the concern, in a diff. The same constructs in standing code, or in a region with no consistent way, are the named pages': [[crash-early]], [[parameterize-with-external-configuration]] and [[dry]]. A bug-fix diff that adds a guard at the failing line is [[fix-the-root-cause]].

## When not to apply

- The fire is not yet under control. The book concedes that a firefighter's first duty is to put the fire out regardless of collateral damage, and says this crew took care because they had judged the situation and were sure they could handle it (p. 36). The book does not carry that concession over to software: it names deadlines, a release date and a demo as the fire, and still says not to add damage (p. 36). This limit is therefore this wiki's own and goes past the book's wording. It covers only a crude line that stops live production damage now, on condition that it becomes a boarded window at once. A deadline never qualifies.
- The added line differs because it is better. Raising a region's standard is not harm. This limit is this wiki's own.
- The concern really differs for this path, and a comment says why. This limit is this wiki's own.

## Repair

Make the same change inside the region's standard: let the error propagate or handle it where it occurs, add a parameter instead of a copy, read the value from where the neighbours read it. If that does not fit the time, do not let the shortcut blend in; mark it as a board as [[broken-windows]] describes. The careful version usually takes longer, and that is the rule's cost under a deadline.

## Before and after

```
// before: added for the demo, in a module whose neighbours let parse errors propagate
function load_orders(path):
    try:
        return parse(path).map(to_order)
    catch any:
        return []
```

```
// after: parse errors propagate, as they do in the neighbouring functions
function load_orders(path):
    return parse(path).map(to_order)
```

## Source

[[pragmatic-programmer]], Topic 3, p. 36. The rule, the firefighter story and the concession about the fire are the book's. The sign, its reading as a relation to neighbouring code, the assignment of neighbouring cases, the limit for live production damage, which goes past the book's wording, the two other limits, the repair and the pseudocode are this wiki's own.
