---
title: Data-flow testing
category: testing
summary: "Procedure adding tests for every definition-use pair of a variable that branch-based tests miss, e.g. x set in branch A of one if and used in branch B of a later if."
tags: [method, testing, data-flow, coverage]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Data-flow testing** derives tests from how data moves through a routine rather than from its control flow. Its premise, per McConnell, is that data usage is as error-prone as control flow; Beizer claims at least half of all code is data declarations and initialisations (p. 500). It is applied after [[structured-basis-testing]], which covers some but not all data flows (p. 503).

## Vocabulary

A variable is **defined** (given a value), **used** (as an operand, an argument and so on) or **killed** (made invalid: memory freed, a loop index out of scope, a file record pointer invalidated by closing the file). Two more terms name actions right after **entry** to a routine and right before **exit** from it (pp. 500-501). Before writing data-flow tests the code is checked for suspicious sequences of these states; that check is [[variable-state-anomalies]] (p. 502).

## Strategies, weak to strong

- **All definitions:** test every place any variable receives a value. The book calls it weak, because testing every line already does it (p. 502).
- **All definition-use combinations:** test every pair where a variable is defined in one place and used in another. Stronger, because testing every line does not guarantee every pair (p. 502).

## The example that shows the gap

```
if p: rate = low
else: rate = high
if q: fee = rate * 2
else: fee = rate + 1
```

Two tests, (p true, q true) and (p false, q false), satisfy basis testing and all-definitions. They miss two definition-use pairs: `rate = low` reaching `fee = rate + 1`, and `rate = high` reaching `fee = rate * 2`. Two more tests, (true, false) and (false, true), cover them (pp. 502-503). In the payroll example the book adds three tests for `companyRetirement`: defined at line 12 and used at 26, defined at 12 and used at 31, defined at 17 and used at 31 (p. 503).

## Procedure

1. Run [[structured-basis-testing]] first.
2. For each variable, list its definitions and its uses; pair every definition with every use it can reach.
3. Mark the pairs the existing tests already exercise; add a test for each remaining pair.

McConnell notes that with practice one senses which pairs are already covered, and that when in doubt listing all pairs is laborious but guarantees finding every case basis testing missed (p. 503).

## Limits

This wiki adds two. The pair count grows with sequential independent decisions that feed one another, so a routine with many such pairs is a candidate for decomposition before testing. In code with few mutable variables (single assignment, values passed through function results) most variables have exactly one definition, and the method collapses into ordinary path coverage.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.3, pp. 500-503, via [[code-complete]]. The procedure list condenses the book's text; the two limits are this wiki's own. The example is this wiki's own rewording of the book's two-decision example on pp. 502-503.
