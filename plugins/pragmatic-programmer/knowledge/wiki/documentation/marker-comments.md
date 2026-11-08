---
title: Standardise marker comments
category: documentation
summary: "A to-do marker sits beside a stub result that callers reach, or one codebase mixes several marker notations (TODO, ****, !!!, TBD), so a mechanical search before release misses some."
tags: [rule, comments, todo, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Marker comments** are notes telling the programmer that work is not finished. McConnell counts them among the six kinds of comment and says this kind «предназначен не для того, чтобы оставаться в коде» (p. 769); see [[comment-kinds]]. The rule is that markers share one notation, so that finding them becomes a mechanical step before release.

## Rule

Standardise the style of marker comments (p. 769). If one programmer writes `*******`, another `!!!!!!`, a third `TBD` and a fourth something else, a mechanical search for unfinished code becomes error-prone or impossible. One notation lets that search become an item on the pre-release checklist, and it prevents the "FIX BEFORE RELEASE!!!" problem (pp. 769-770). The book's picture of that problem is a customer's defect report traced in the debugger to `return NULL; // ****** NOT DONE! FIX BEFORE RELEASE!!!` (p. 769). It judges that shipping a defective program is bad, and knowing it was defective is simply awful (p. 769, paraphrased; the sentence breaks across a hyphen in the raw extraction).

The book notes two ways people write markers. Some make them syntactically invalid so the compiler reminds them. Others use a fixed string that compiles and can be searched for (p. 769). Some editors support "to do" tags and searching for them (p. 770).

## Sign in code

- One codebase uses more than one notation for unfinished work: `TODO`, `FIXME`, `XXX`, `TBD`, runs of `*` or `!`.
- A marker sits beside a stub result (`return null`, an empty body, a hard-coded value) that callers will reach.
- A marker's own text says it must be fixed before release.

This wiki assigns the neighbouring case as follows. A marker admitting a defect on a path that runs is [[broken-windows]]; [[marker-comments]] owns the choice of marker notation and a marker beside a stub that has not been written.

## When not to apply

The limits are this wiki's own.

- Work in progress on a branch nobody ships from. Markers are the intended tool there, and the book treats them as temporary, not as forbidden.
- A project whose tooling already defines the marker notation and searches for it. The project's convention is then the standard, and this rule asks only that it be used consistently.
- A marker that records a known, accepted limitation rather than unfinished work. That belongs in a plain why-comment, see [[comment-why-not-how]]. This wiki's reading is that such a comment should then not carry a marker word that a pre-release search would flag.

## Repair

1. Pick one notation, or adopt the project's, and rewrite the others to it.
2. Make the search for that notation a release check, by script or CI step.
3. For a marker beside a stub that callers reach, either finish the work or make the stub fail loudly instead of returning a plausible value. See [[crash-early]].

## Before and after

```
// before
function find_discount(customer):
    return null   // ****** NOT DONE! FIX BEFORE RELEASE!!!

function tax_rate(region):
    return 0.2    // TBD per region
```

```
// after
function find_discount(customer):
    // TODO(release-blocker): discount rules not implemented
    fail("find_discount is not implemented")

function tax_rate(region):
    // Rate is flat across regions until the regional table is supplied.
    return FLAT_TAX_RATE
```

## Source

[[code-complete]], ch. 32, section 32.4, pp. 769-770. The book's parts: the marker as a kind of comment that should not stay, the two ways of writing markers, the call to standardise, the pre-release search, and the `return NULL` example. This wiki's own parts: the signs, the notations `FIXME` and `XXX` beyond the book's examples, the assignment against [[broken-windows]], the limits, the repair that makes a stub fail rather than return a value, the link to [[crash-early]], and the pseudocode.
