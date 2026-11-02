---
title: Cost Now Versus Cost Later
category: ordering
summary: A feature that would cost more later is not automatically cheaper now; the early price must include later changes, a simpler version discovered afterwards, and complexity carried by all other work. On the cost of change alone Cohn leans late, which this wiki takes as its default; infrastructure takes its position from value and moves earlier only for a named reason: a net cost saving, knowledge a decision waits for, or the risk of the component failing.
tags: [decision-rule, ordering, prioritization, estimation, dependencies, risk]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
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

Cohn gives no reason for calling the last one hidden. This wiki reads "hidden" as meaning that it does not appear in any single task's estimate.

## The default and what overrules it

On the cost of change alone, Cohn leans late:

> The best way to reduce the cost of change is to implement a feature as late as possible—effectively when there is no more time for change.
>
> — [[cohn-agile-estimating-planning]], L1738

This conflicts on its face with doing high-risk work first ([[prioritization-factors]], its risk-value quadrants). This wiki resolves it as follows, and the resolution is ours: the sentence above speaks only about the cost of change, and on the price of adding it Cohn says early is often cheaper for infrastructure, before asking that later change and added complexity be counted (L1839). This wiki takes the late lean as its default only when the cost of change is the only factor in play. Knowledge and risk are separate factors and can move an item earlier in spite of it, as the combining procedure there does. An argument for going early therefore has to name the knowledge or the risk. A claim that it will be harder later is not enough unless the three additions were counted.

Cohn adds that cost can really be lower early, and that "This is true for many infrastructure elements" (L1839). This wiki's rule does not deny this. It asks that the figure be net of the additions. See *Prioritizing Infrastructure* (below).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Size if done now | The task's estimate |
| Size if done later | An estimate of what will have been built on top by then; the person steering or the design |
| How settled the requirement is | [[ordering-for-early-user-feedback]]: open questions on the task |
| Which later work would carry the complexity | The remaining tasks in the same area |

The later fact is readable from history, though these tests are this wiki's, not the source's.

- **Going early was wrong** if the early work was reworked or replaced by follow-up tasks that add up to more than the saving claimed, or if tasks touching the same area grew after it landed.
- **Waiting was wrong** if the late addition forced changes across finished work well beyond its estimate.

## Cost

This wiki notes that the rule needs two estimates and a guess about change, and the guess cannot be checked until afterwards. Followed literally, leaning late also postpones the learning that doing the work would have produced.

## Agent executor note

This wiki reads the mechanism as surviving. Rework comes from what was unknown at build time, whoever did the building. Cohn's magnitudes do not transfer: they are invented, and they describe people's weeks. This wiki expects an agent to change the ratio between building and changing, but no source here measures it, so the plugin should compare the additions by name and should not import the figures.

## Prioritizing Infrastructure

This rule orders work that no user asks for, such as an architectural element, against work users do ask for. These two are hard to compare directly ([[incomparable-tasks]]). Cohn ([[cohn-agile-estimating-planning]]) compares them by running the item through each of the four [[prioritization-factors]] (L1833-L1847), using a security framework as his example.

### The four questions

| Factor | Cohn's reasoning | Direction in his example |
|---|---|---|
| Value | "The application must do something before security is relevant." (L1837) | Late |
| Cost | Cheaper to add now, which is "the basis for many arguments in favor of developing them early", but it may change by the end, and it may add complexity (L1839) | Unclear until the additions are counted (the comparison at the top of this page) |
| New knowledge | Unlikely to teach anything about the product, but it may teach something about the project (L1841) | Depends |
| Risk | "Perhaps not in this example." (L1847) | Depends on the component |

The worked example is on knowledge. A team that had to authenticate through an LDAP server had no one who had done it, so nobody could say what it would take. To remove that doubt, the stories "were moved up to around the middle of a project rather than being left near the end" (L1841-L1845). This wiki notes the size of the move: the middle, not the start. An item needs to come early enough to act on what it reveals, not as early as possible.

On risk, Cohn's general claim is that "the failure of a framework, key component, or other infrastructure is often a significant risk to a project. This may be enough to warrant moving development sooner than would be justified solely on the basis of value." (L1847).

### The rule

This statement of it is this wiki's reading of the worked example. Infrastructure takes its position from value, which is usually late, and moves earlier only for a reason that can be named as one of these:

1. Cost now is lower after counting later change and carried complexity.
2. The work produces knowledge that a decision is waiting for.
3. The component's failure would stop the project, and doing the work shows whether it fails.

This wiki adds that dependencies still apply: a feature that needs the component cannot start without it ([[sequence-versus-wait]]). That sets a floor on the position and is separate from these three.

This wiki also pairs the rule with cutting: where possible, the item is built thin and with a feature that uses it ([[vertical-slice]]), because infrastructure with no feature attached is the way the risk-driven failure happens ([[prioritization-factors]]). This pairing comes from the base and not from this chapter.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which features use it | The tasks that depend on it |
| Stated reason for moving it | The move recorded by [[prioritization-factors]] |
| What failure of the component would stop | The design, or the person steering |
| Whether the requirement behind it is settled | Open questions on those tasks |

These tests are this wiki's.

- **Moved too early** if the component was reworked once its first real user arrived, or if the features it supported were dropped.
- **Left too late** if its arrival forced changes across finished work, or if a failure surfaced with too little time left to respond.

### Cost

This wiki notes that early infrastructure spends capacity before anything is shown to users, and that delays the feedback argued for in [[ordering-for-early-user-feedback]]. Late infrastructure accepts the chance of retrofit.

### Agent executor note

Cohn's LDAP case rests on unfamiliarity: "None of the developers had done this before" (L1841). That trigger depends on human experience. This wiki reads the surviving version as whether the integration has been shown to work in this system, whoever is executing. Reasons 1 and 3 survive unchanged. Reason 2 needs its finding recorded ([[ordering-for-early-user-feedback]]).
