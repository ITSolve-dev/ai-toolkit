---
title: Degree of constraint
category: altitude
summary: How tightly the solution space is bounded decides what a document has to do — an open space needs rules that narrow it, a closed one needs a defence of the least-bad combination.
tags: [concept, altitude, design-doc, shape]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

The shape of a design document is set less by its subject than by **how constrained its solution
space is**. [[design-docs-at-google]] names this "one of the primary factors that would influence
the shape of a software design and hence the design doc" (L89), and describes the two extremes.

**An open space.** A greenfield project, "where all we know are the goals, and the solution can be
whatever makes the most sense". Such a document "may be wide-ranging, but it also needs to quickly
define a set of rules that allow zooming in on a manageable set of solutions" (L91).

**A closed space.** A legacy system that resists change, or a design bounded by its host language:
"you may be able to enumerate all the things you can do relatively easily, but you need to
creatively put those things together to achieve the goals. There may be multiple solutions, and
none of them are really great, and hence such a document should focus on selecting the best way
given all identified trade-offs" (L93-L95).

## What each demands of the writer

| | Open space | Closed space |
|---|---|---|
| The hard part | Narrowing | Combining |
| What the document must produce early | Rules that eliminate most of the space | An honest enumeration of what is available |
| Where the argument sits | In the constraints chosen | In the comparison of imperfect combinations |
| The failure | Surveying options without committing | Presenting the only reachable answer as though it were the best one |

## Why it belongs to altitude

The two cases put the document's centre of gravity in different places. In an open space, the
load-bearing content is the self-imposed constraints — decisions about what will *not* be
explored, which is the same work [[non-goals]] does at the level of outcomes. In a closed space,
the constraints are given, and the document's work is entirely in
[[alternatives-considered]]: everything is on the table, nothing is good, and the argument is
comparative.

Misjudging which case you are in produces a recognisable defect. A closed-space problem written as
though open reads as a survey that never lands. An open-space problem written as though closed
presents an arbitrary starting point as an inherited constraint, and the reader cannot tell that
the space was never explored.

Related: [[when-to-write-a-design-doc]] — a fully closed space with one obvious combination has no
ambiguity left, and needs no document.
