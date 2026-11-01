---
title: Cost Now Versus Cost Later
category: ordering
summary: A feature that would cost more later is not automatically cheaper now; the early price must include later changes, a simpler version discovered afterwards, and complexity carried by all other work; cost alone favours late, while learning and risk can overrule it.
tags: [decision-rule, ordering, prioritization, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Cost Now Versus Cost Later

This rule decides whether a higher cost later is a reason to do something now. Cohn ([[cohn-agile-estimating-planning]]) says the cost of a feature is not fixed: "An important, yet often overlooked, aspect of cost is that the cost can change over time." (L1738).

## The comparison

Cohn's example is invented for illustration. Internationalization takes four weeks today and six weeks in six months. If the early work then takes three more weeks of changes, because of what was learned in those six months, waiting would have been better (L1738). This wiki states the arithmetic that sits under it: early is 4 + 3 = 7 weeks and late is 6.

This wiki notes that the early side of the comparison carries three additions that the plain argument for going now leaves out.

| Addition to the early price | Source |
|---|---|
| Changing the first version as knowledge arrives | "The cost of these changes needs to be considered in any now/later decision." (L1839) |
| Discovering that a simpler version would have done | "a simpler and faster implementation would have been adequate" (L1738) |
| Complexity paid by everything built afterwards | "introducing the security framework early may add complexity that will be a hidden cost on all future work" (L1839) |

The last one does not appear in any single task's estimate, which is why Cohn calls it hidden.

## The default and what overrules it

On cost alone Cohn leans late:

> The best way to reduce the cost of change is to implement a feature as late as possible—effectively when there is no more time for change.
>
> — [[cohn-agile-estimating-planning]], L1738

This conflicts on its face with doing high-risk work first ([[risk-value-quadrants]]). This wiki resolves it as follows, and the resolution is ours: the sentence above speaks only about the cost of change. It sets the default when cost is the only factor in play. Knowledge and risk are separate factors and can move an item earlier in spite of it, as [[combining-prioritization-factors]] does. An argument for going early therefore has to name the knowledge or the risk. A claim that it will be harder later is not enough unless the three additions were counted.

Cohn adds that cost can really be lower early, and that "This is true for many infrastructure elements" (L1839). This wiki's rule does not deny this. It asks that the figure be net of the additions. See [[prioritizing-infrastructure]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Size if done now | The task's estimate |
| Size if done later | An estimate of what will have been built on top by then; the person steering or the design |
| How settled the requirement is | [[end-and-means-uncertainty]]: open questions on the task |
| Which later work would carry the complexity | The remaining tasks in the same area |

The later fact is readable from history, though these tests are this wiki's, not the source's.

- **Going early was wrong** if the early work was reworked or replaced by follow-up tasks that add up to more than the saving claimed, or if tasks touching the same area grew after it landed.
- **Waiting was wrong** if the late addition forced changes across finished work well beyond its estimate.

## Cost

This wiki notes that the rule needs two estimates and a guess about change, and the guess cannot be checked until afterwards. Followed literally, leaning late also postpones the learning that doing the work would have produced.

## Agent executor note

This wiki reads the mechanism as surviving. Rework comes from what was unknown at build time, whoever did the building. Cohn's magnitudes do not transfer: they are invented, and they describe people's weeks. This wiki expects an agent to change the ratio between building and changing, but no source here measures it, so the plugin should compare the additions by name and should not import the figures.
