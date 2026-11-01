---
title: Service Level Expectations by Work Item Type
category: periods
summary: Cycle time data can be filtered by type and different SLEs offered, but each subtype must then obey Little's Law separately. Start with one global SLE; split only once the whole system is predictable and the split is needed.
tags: [decision-rule, estimation, cycle-time, segmentation, class-of-service]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Service Level Expectations by Work Item Type

Cycle time scatterplots can be filtered by work item type the same way cumulative flow diagrams can, and any such cut is valid as analysis ([[vacanti-actionable-agile-metrics]] L3084). Using a cut to offer a different [[service-level-expectation]] per type is a separate decision, and Vacanti treats it as advanced.

## Two reasons to segment

1. **To see a kind of outcome.** Items that did not finish normally, such as abandoned ones, can be tagged and shown alone. "Displaying only the abandoned items would give you a good visualization as to the time wasted on those activities." (L3086). See [[accounting-for-abandoned-work]].
2. **To offer different SLEs.** Stories and defects probably have very different percentiles (L3094), so "our SLA for user stories might be 14 days at 85% but for defects it might be five days at 85%" (L3094).

The first reason commits to nothing. The second makes a promise per subtype, which is where the condition below applies.

## The rule

> If you are going to offer different SLAs for different work items types, then you have to ensure that all the assumptions for Little’s Law for each and every subtype are adhered to.
>
> — [[vacanti-actionable-agile-metrics]], L3096

> If you are just starting out with flow principles, I would highly recommend just setting one global SLA for all your work items types and get predictable that way first.
>
> — [[vacanti-actionable-agile-metrics]], L3098

Vacanti's order is global first, then subtypes only on need: "Get predictable at an overall system level first. You may find that is good enough. Only optimize for subtypes later if you really need to." (L3098). He calls the advice to design [[class-of-service]] up front misguided (L3098); the full case is on [[when-to-use-class-of-service]]. The checks per subtype are on [[littles-law-assumptions]], and [[littles-law]] says the law holds for each type as well as for the whole.

## Inputs and what would show the choice wrong

- **Whether the global SLE is met:** the share of finished items within it, from board history.
- **Whether a subtype has its own stable data:** finished items of that type alone, read against the data needed in [[choosing-a-service-level-expectation]].
- **Whether a split is needed:** a receiver who actually asks for a different promise per type.

This wiki reads the later fact as follows: per-type SLEs were premature if the types' percentiles drift or the types' finished counts stay too thin to read. A global SLE was too coarse if a type's items consistently sit far from the line for the rest, and the receiver cares about that difference.

## Failure sign

This sign is the wiki's phrasing of the warning at L3096: separate SLEs per type on a board whose global SLE is not yet being met, or whose subtypes have too few finished items for a percentile to mean anything. As with every sign here, it raises a question, not a verdict ([[smell-is-not-a-finding]]).

## Scale note

This note is the wiki's own. A few people's board finishes few items, so splitting by type spreads the count thin faster than on a larger team. The source's data-point range of about 11 to 30 applies per promise, so the global SLE is the natural default for this setting.
