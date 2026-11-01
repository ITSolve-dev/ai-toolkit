---
title: Combining Prioritization Factors
category: ordering
summary: Sort by value against today's cost for a first order, then move items forward or back for learning and risk; the people building may argue an item up, the owner decides, and an item whose result the owner could not be shown needs more than preference. Cohn keeps this informal, while a plugin has to write down each move or the order cannot be checked.
tags: [method, ordering, prioritization, risk, learning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Combining Prioritization Factors

This is Cohn's two-step procedure for turning the four [[prioritization-factors]] into one order ([[cohn-agile-estimating-planning]]). Cost and value set the position, and learning and risk adjust it.

## The procedure

1. Compare value with what the item would cost today: "This gives you an initial priority order for the themes. Those themes with a high value-to-cost ratio are those that should be done first." (L1821).
2. Then "think of the other prioritization factors as moving themes forward or backward." (L1823). Cohn's example is a medium-priority theme, due midway through the release, whose technology is very risky: "This would move the theme forward in priority and on the schedule." (L1827).

The source's summary repeats this: value and cost sort the themes into an initial order, and the other factors move them (L1875). The unit is the [[theme]].

The chapter's first step uses cost "today" (L1821). The way cost shifts over time is a separate judgement ([[cost-now-versus-cost-later]]), so this wiki treats it as one of the things that can move an item in step 2.

Chapter 22 restates the procedure as a guideline:

> Work on features in the order that optimizes the total value of the project. In addition to the value and cost of features when prioritizing consider also the learning that will occur and the risk that will be reduced by developing the feature.
>
> — [[cohn-agile-estimating-planning]], L4933

Its strength is modest. Early elimination of a significant risk "can often justify developing a feature early", and if a feature would give significant knowledge "about the product or their effort to develop it, they should consider developing that feature early." (L4933). This wiki reads the two kinds of knowledge as the two on [[end-and-means-uncertainty]]: about the product is end uncertainty, and about the effort is means uncertainty. Cohn's example fits, since finding out early that a third-party component cannot meet performance requirements (L4899) is cheaper than finding out late. That comparison of cost is this wiki's.

## Which way risk moves an item

Cohn's two statements point in different directions. A medium-priority risky theme moves forward (L1827), yet low-value, high-risk items are deferred "right out of the project" (L1817). The chapter's first discussion question poses this very case, a low-priority feature that might be dropped and needs a language nobody on the team knows, and leaves it for the reader (L1879).

This wiki resolves it with one test, and the test is ours: **will this item be built regardless?** If yes, its risk has to be met at some point, and meeting it early costs less, so risk moves it forward. If it could be dropped, dropping it removes the risk for nothing, so risk moves it back. On this reading the feature in the discussion question moves back. See [[risk-value-quadrants]].

## Who moves an item, and the limit

The fictional case study in Chapter 23 (L4961) splits the two roles. It tells the product manager what happens at the next planning:

> The others may ask you to reconsider and move in one or two that they want to do because they’re risky or because they’ll learn a lot by doing them. But the ultimate prioritization decision will be up to you.
>
> — [[cohn-agile-estimating-planning]], L6211

The same division appears on [[value-order-versus-technical-necessity]], for sequencing. The case then gives its limit, from the other side:

> If the programmers were selecting a bunch of technical mumbo-jumbo or features you wouldn’t be able to see, I would have stopped that and had them work on other stories.
>
> — [[cohn-agile-estimating-planning]], L6215

This wiki reads that as a test with two outcomes. A task argued up for risk or learning, with a result the owner can be shown, goes to the owner to decide. A task with no result the owner can be shown is stopped, and risk or learning alone does not carry it, unless it is cut until it has one ([[vertical-slice]]). The case's first iteration passes that test: the rings story opens because "That’s our biggest risk." (L5686), and the product manager's reaction is "It is great to think that we’ll make so much visible progress so quickly." (L5935).

**The evidence is thin.** The case does not test the rule. The rings story was both the riskiest and a mandatory feature, so risk and value pointed the same way, and the source offers no way to trade one against the other when they diverge. That reading is this wiki's. It is also why the test on [[risk-value-quadrants]] stays a judgement.

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
| Whether its result can be shown | The task's acceptance ([[testable-acceptance]]) |

The source does not say what would show an order wrong, so these tests are this wiki's.

- **A forward move was wrong** if the item was done early and the risk or question named for it never bore on anything else: the risk proved minor, or no task moved, was re-sized or was dropped as a result of what was learned.
- **Failing to move an item was wrong** if a late item revealed a problem that forced finished work to be redone or dropped.
- **A backward move was wrong** if the deferred item turned out to be required and its risk arrived with no time left.

Two candidate signs follow, and both are this wiki's. A task carrying the plan's largest unverified assumption sits late in the order while work resting on it goes first. And a period's selection contains tasks whose results the owner could not be shown. A sign raises a question: the risk may be accepted knowingly.

## Cost

This wiki notes that the method is a judgement with no weights. Two people can apply it and reach different orders, and Cohn gives no rule for how far a factor may move an item. A written reason lets the result be checked, but it does not make it reproducible. A risky item placed early also delivers less value now, and if the risk does not materialise the value was deferred for nothing. Cohn leaves it at "consider" and "often" (L4933), so the weight comes from the case, and [[incomparable-tasks]] applies where it cannot be compared.

## Agent executor note

This wiki reads the procedure as concerning the order of results, so it survives. Writing down each move matters more here, because an agent has no memory of why an order was set unless the reason is on the board. The value input and the build-regardless answer stay with the person steering.

With a few people steering an agent, the owner and the builder may be one person. The split of authority then falls away and the visibility test stays, since an agent left to choose can also prefer invisible technical work. This wiki also expects an agent to make probes cheaper, which would favour trying a risky task early, though the result is only worth what the people steering can verify. No source measures this. Where the question can be answered without building a feature, see [[spike-as-last-resort]].
