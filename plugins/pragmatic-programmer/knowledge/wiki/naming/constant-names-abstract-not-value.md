---
title: A constant is named for what it stands for, not for its value
category: naming
summary: "A named constant whose name spells its value (FIVE, TWELVE, TEN_PERCENT, HEX_80) or a well-known quantity (BAKERS_DOZEN) rather than its role, so a change of value would make the name lie."
tags: [rule, naming, constants]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell: a constant's name should describe the abstract thing the constant represents, not the particular number (*Code Complete*, Russian edition, p. 263). «Имя FIVE — плохое имя константы» (p. 263), whatever its value, while `CYCLES_NEEDED` is a good one. `CYCLES_NEEDED` can be 5.0, 6.0 or anything else, but `FIVE = 6.0` would be absurd. In the same way `BAKERS_DOZEN` is bad and `DONUTS_MAX` is fine (p. 263).

## Rule

Name the constant for its role in the program (a limit, a count required, a default, a code), so that a new value never makes the name false.

## Sign in code

- A constant whose name is a number word or the literal spelled out: `FIVE`, `ONE_HUNDRED`, `HEX_80`, `TEN_PERCENT`.
- A constant whose name is a well-known quantity rather than its purpose here (`BAKERS_DOZEN`, `SECONDS_IN_MINUTE` used as a timeout).
- A constant declared with a value that contradicts its name: the name has outlived a change.

This wiki assigns the neighbouring case as follows. This page owns the name of a constant that already exists. Whether a bare literal should become a named constant at all is [[named-constants-over-literals]]; whether it should instead be bound later, from configuration, is [[binding-time]].

## When not to apply

- A true mathematical or physical constant is its own role (`PI`, `SPEED_OF_LIGHT`), and so is a unit conversion whose meaning is the conversion (`SECONDS_PER_MINUTE` used to convert). This wiki's limit; the book does not discuss it.

## Repair

Find each use and state what the value means there. If all uses share one meaning, rename the constant after it. If uses differ (the same `FIVE` is a retry limit in one place and a column count in another), split it into one constant per meaning.

## Before and after

```
const TWELVE = 12
for attempt from 1 to TWELVE
    ...
boxes = ceil(donuts / TWELVE)
```

```
const MAX_ATTEMPTS = 12
const DONUTS_PER_BOX = 12
for attempt from 1 to MAX_ATTEMPTS
    ...
boxes = ceil(donuts / DONUTS_PER_BOX)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.2, p. 263 ([[code-complete]]): the rule and the `FIVE`/`CYCLES_NEEDED` and `BAKERS_DOZEN`/`DONUTS_MAX` pairs. Splitting a constant shared by different meanings, the assignment against [[binding-time]] and the limit for true constants are this wiki's own. The pseudocode is this wiki's own.
