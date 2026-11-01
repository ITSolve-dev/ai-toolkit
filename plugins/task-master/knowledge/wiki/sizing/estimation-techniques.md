---
title: Estimation Techniques
category: sizing
summary: The three ways of deriving an estimate, expert opinion, analogy and disaggregation, what each is good and bad at, and why Cohn combines them; which applies depends on whether comparable estimated work exists.
tags: [concept, estimation, expert-opinion, analogy, disaggregation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Estimation Techniques

Cohn names three common ways of deriving an estimate: expert opinion, analogy and disaggregation. "Each of these techniques may be used on its own but they should be combined for best results." ([[cohn-agile-estimating-planning]] L1270). This page situates them. The working procedures are on [[triangulation]] and [[over-disaggregation]].

## Expert opinion

An expert is asked how long something will take or how big it will be. "The expert relies on her intuition or gut feel and provides an estimate." (L1274).

**Strength:** speed, with a developer reading a story, perhaps asking a question or two, and answering (L1278). Cohn also reports that "There is even evidence that says this type of estimating is more accurate than other, more analytical approaches (Johnson et al. 2000)." (L1278). This wiki has not read the cited study.

**Weakness:** one person may not cover the work. Cohn writes: "Developing this functionality is likely to require a variety of skills normally performed by more than one person. This makes it difficult to find suitable experts who can assess the effort across all disciplines." (L1276).

Cohn draws the discriminating line by what is being estimated: "On a traditional project for which estimates are associated with tasks this is not as significant of a problem because each task is likely performed by one person." (L1276). This wiki notes that "task" there means a one-person piece of work, not this wiki's [[unit-of-work]]. A [[vertical-slice]] crosses disciplines, so the weakness applies to the tasks this wiki favours. That mapping is ours.

## Analogy

The item is compared with already-estimated items, and "this story is a little bigger than that story" is an analogy (L1282). If it is twice the size, it gets twice the estimate (L1288). The supporting claim is "There is evidence that we are better at estimating relative size than we are at estimating absolute size (Lederer 1998; Vicinanza 1991)." (L1288), again held on Cohn's report. The procedure is [[triangulation]].

## Disaggregation

The item is split into smaller pieces that are easier to estimate (L1294). Cohn's reason is that "Not only are large things notoriously more difficult to estimate, but in this case there will be very few similarly sized stories to compare to." (L1294). This wiki reads disaggregation as serving analogy: it brings an item back into the range where a comparison means something. Its limit is on [[over-disaggregation]].

## Choosing among them

The source says to combine them and gives no rule for which leads. This wiki's reading:

- **Comparable estimated work exists:** analogy.
- **No comparable work because the item is too big:** disaggregate until it is comparable, or cut it for real under [[size-ceiling]].
- **No comparable work because the project is new:** expert opinion, which needs no reference set, and later estimates correct it through analogy.
- **Nobody can say what is inside:** none of the three applies. That is a question to answer first, on [[spike-as-last-resort]] and [[unknowns-surfaced-by-estimating]].

The source's combined form is planning poker. Its meeting mechanics are out of scope for this wiki. What makes it work is kept on [[independent-estimates]] and [[who-estimates]].

## Agent executor note

This wiki reads expert opinion's speed as coming from intuition built by a person's own past work, and the sources here do not say what plays that role for an agent. Analogy has the most direct transfer, because a reference set can be read from board history rather than remembered, though no source here tests it. The evidence quoted above concerns human estimators.
