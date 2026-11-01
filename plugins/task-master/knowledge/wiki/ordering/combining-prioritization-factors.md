---
title: Combining Prioritization Factors
category: ordering
summary: Sort by value against today's cost for a first order, then move items forward or back for learning and risk; Cohn keeps this informal, while a plugin has to write down each move or the order cannot be checked.
tags: [method, ordering, prioritization, risk, learning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Combining Prioritization Factors

This is Cohn's two-step procedure for turning the four [[prioritization-factors]] into one order ([[cohn-agile-estimating-planning]]). Cost and value set the position, and learning and risk adjust it.

## The procedure

1. Compare value with what the item would cost today: "This gives you an initial priority order for the themes. Those themes with a high value-to-cost ratio are those that should be done first." (L1821).
2. Then "think of the other prioritization factors as moving themes forward or backward." (L1823). Cohn's example is a medium-priority theme, due midway through the release, whose technology is very risky: "This would move the theme forward in priority and on the schedule." (L1827).

The source's summary repeats this: value and cost sort the themes into an initial order, and the other factors move them (L1875). The unit is the [[theme]].

The chapter's first step uses cost "today" (L1821). The way cost shifts over time is a separate judgement ([[cost-now-versus-cost-later]]), so this wiki treats it as one of the things that can move an item in step 2.

## Which way risk moves an item

Cohn's two statements point in different directions. A medium-priority risky theme moves forward (L1827), yet low-value, high-risk items are deferred "right out of the project" (L1817). The chapter's first discussion question poses this very case, a low-priority feature that might be dropped and needs a language nobody on the team knows, and leaves it for the reader (L1879).

This wiki resolves it with one test, and the test is ours: **will this item be built regardless?** If yes, its risk has to be met at some point, and meeting it early costs less, so risk moves it forward. If it could be dropped, dropping it removes the risk for nothing, so risk moves it back. On this reading the feature in the discussion question moves back. See [[risk-value-quadrants]].

## Keeping it on paper

Cohn lets the procedure stay informal: "It can (and often does) take place entirely in the head of the product owner." (L1829). The team may then ask for small changes (L1829). This wiki does not keep that part. An order held in one head cannot be read back when it proves wrong. So the plugin writes, for each item that moved, the factor that moved it and the direction. Running the discussion itself is outside this base.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Value of each item | The person steering, or [[ordering-by-value-and-urgency]] |
| Cost today | The item's size, [[cost-per-story-point]] |
| Whether doing it produces needed knowledge | [[end-and-means-uncertainty]], the task's open questions |
| Whether doing it removes a named risk | [[risk-value-quadrants]] |
| Whether the item is certain to be built | The person steering |

The source does not say what would show an order wrong, so these tests are this wiki's.

- **A forward move was wrong** if the item was done early and the risk or question named for it never bore on anything else.
- **Failing to move an item was wrong** if a late item revealed a problem that forced finished work to be redone or dropped.
- **A backward move was wrong** if the deferred item turned out to be required and its risk arrived with no time left.

## Cost

This wiki notes that the method is a judgement with no weights. Two people can apply it and reach different orders, and Cohn gives no rule for how far a factor may move an item. A written reason lets the result be checked, but it does not make it reproducible.

## Agent executor note

This wiki reads the procedure as concerning the order of results, so it survives. Writing down each move matters more here, because an agent has no memory of why an order was set unless the reason is on the board. The value input and the build-regardless answer stay with the person steering.
