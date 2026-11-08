---
title: Reversibility
category: change
summary: "Vendor, deployment or architecture choices wired so deep that changing one means a rewrite: a decision treated as final with no seam left to reverse it."
tags: [concept, reversibility, change, decoupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Reversibility is the property that a decision can be undone later at a bearable cost. This wiki reads the source as locating that cost in how the code commits to a decision, not in the foresight of its authors. The tip reads «Окончательных решений не существует» (p. 81).

## What it changes in a report

The failure the source names is an assumption and not a wrong choice: «Ошибка кроется в допущении, что любое решение принимается окончательно» (p. 81). Choosing a particular vendor's database, an architectural pattern or a deployment model commits the project to a course that can be undone only at great expense (p. 80). This wiki therefore reports such a commitment by how far it has spread through the code, and does not judge whether the choice was good.

This page has no sign of its own. The source's moves are rule pages, which own the signs:

- following [[dry]], [[coupling|decoupling]] and [[parameterize-with-external-configuration|external configuration]], which reduce the number of critical decisions that could be irreversible (p. 80);
- hiding third-party APIs behind layers of your own: [[hide-third-party-apis]] (p. 81);
- splitting code into components even when they ship together (p. 81). How a program is split into components is architecture, which this wiki takes as given and does not prescribe.

The source does not ask for better prediction. It lists the server architectures that were each best practice in turn since the start of the century, asks whether all of them can be planned for, answers that they cannot, and leaves only making change easy (p. 81). This wiki reads that as [[easier-to-change]] applied to a decision already taken.

## Limits

The source states no limit. This wiki reads reversibility as a reason to keep a seam at a decision that has already been made, and not as a licence to build for every conceivable future. The source's argument is that the futures cannot be planned, so this wiki takes a layer per imagined change to contradict that argument as much as a hard commitment does. See [[replaceable-code-over-forecast]]. This wiki adds that a seam has a price: it is one more thing to read and maintain, and it hides what lies behind it.

## Source

[[pragmatic-programmer]], Topic 11, pp. 79-82. The definition's phrasing, the reading of where the cost lies, the way of reporting a commitment, the link to ETC and the Limits section are this wiki's own. This wiki leaves out the chapter's closing challenge (p. 82), because asking which futures are most likely calls for the forecast [[replaceable-code-over-forecast]] rules out.
