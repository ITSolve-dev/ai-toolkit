---
title: Check the resource balance
category: debugging
summary: "For a suspected leak or a long-running loop: wrap each resource type, count allocations and releases, and assert usage has not grown at a fixed point."
tags: [method, resources, leaks]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Because pragmatic programmers trust no one, themselves included, the book recommends code that verifies resources really are released (p. 162). It complements [[finish-what-you-start]], which arranges release but does not prove it.

## Procedure

1. Create a wrapper for each type of resource (p. 162).
2. Have the wrappers record every allocation and release (p. 162).
3. Find the points where the program's logic dictates a particular resource state (p. 162).
4. Check that state there. The book's example is the top of a long-running server's main loop, usually the single point where it waits for the next request. That is a convenient place to confirm that resource use has not grown since the last pass (p. 162).
5. At a lower level, which the book calls less useful, use tools that check running programs for memory leaks (p. 162).

## Reading the result

This wiki reads a count that rises across iterations as a leak in the code that ran during those iterations, so the wrapper's records narrow the search to one resource type. A count that rises and then levels off may be a cache or pool, and needs a look at its limit before calling it a leak.

## Limits

The book calls this check always worthwhile (p. 162). This wiki adds two limits. A short-lived process that does one pass and exits has no repeating point to check, and its resources go back at exit, so the wrappers buy nothing. A resource whose use is meant to grow with each request, such as a store of accepted records, has no fixed state to assert, so the check there is against its stated bound.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: p. 162. The sections on reading the result and on limits are this wiki's own, apart from the book's word on when the check is worth writing.
