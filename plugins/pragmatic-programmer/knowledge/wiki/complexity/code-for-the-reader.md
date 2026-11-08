---
title: Code written for the reader
category: complexity
summary: "Concept: code a reader must decode rather than read, kept that way on the ground that nobody else will use it; once code is shared, imported or scheduled it is public, and the book's readability work is owed before that."
tags: [concept, readability, maintenance, private-vs-public-programs]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell names readability as one of the threads running through his book. Computers do not care how readable code is, so readable code is written for people (p. 821). He lists what readability affects: comprehensibility, ease of review, error rate, ease of debugging, ease of change, and, as consequences of all of these, development time and external quality (p. 821).

## Why the writer's convenience loses

The book claims readable code takes no longer to write than confusing code, at least in the long run. Code is read when its author checks that it works, and again during review, defect fixing, modification, and reuse in a similar program (p. 822). Readability is therefore not an optional part of development, and convenience at writing time bought with reading time is hardly a good trade (p. 822). «Лучше один раз написать хороший код, чем раз за разом читать плохой.» (p. 822)

The book backs this with figures: one study found the average program was maintained by 10 generations of programmers before being rewritten (Thomas, 1984; p. 822), and maintainers spend 50 to 60% of their time trying to understand code (Parikh and Zvegintzov, 1983; p. 823). Both figures are decades old; this wiki keeps them as the book's support, not as current measurements.

## Private and public programs

The book borrows Douglas Comer's distinction (Comer, 1981; p. 822). A *private* program is used only by its author: nobody else uses it, changes it, or even knows it exists. Such programs are usually trivial and rare. A *public* program is used or changed by someone besides the author. A private program may be badly written and full of limitations, and that affects only its author. A public program must be written more carefully: its limitations documented, the code made reliable and modifiable (p. 822).

The failure the book warns about is a private program turning public, which happens fairly often. The conversion should happen *before* the program goes into circulation, and improving readability is part of it (p. 822). Even code meant only for its author is likely to be changed by someone else, and the author who wants to reuse last week's class in another program will need to read it too (p. 822).

## How it is achieved

No single technique makes a confusing program readable, the book says, but the sum of many small improvements is substantial: good names for classes, methods and variables, careful formatting, short methods, complex logical tests hidden in boolean functions, and intermediate results of complex calculations assigned to named variables (p. 823). These are owned by [[name-describes-what-the-variable-represents]], [[routine-length]], [[name-complex-conditions]], [[explaining-variable]] and [[self-documenting-code]]. Its closing caution: if you think some code need not be readable because nobody else will touch it, check that you are not confusing cause and effect (p. 823).

The book allows that standards for private and public programs may differ (p. 822), but calls justifying unreadable code by sole authorship dangerous, since habits carry over, and ends: «Профессиональные программисты пишут удобочитаемый код, и точка» (p. 822). This wiki therefore does not read privacy as an exemption from the readability rules here, only as the point at which the book's conversion step is due. Once code is committed to a shared repository, imported by another module, or scheduled to run, it is public, and the conversion is owed before that. That operational test is this wiki's own.

The chapter's test for when code has failed the reader, decoding instead of reading, is on [[design-warning-signs]]; rewriting such code is [[rewrite-tricky-code]].

## Source

[[code-complete]], ch. 34.3, pp. 821-823. The list of readability effects, the write-once argument, the Comer distinction, the 10-generation and 50-60% figures, and the list of techniques are the book's. The warning against justifying unreadable code by sole authorship is the book's too; its quotation was transcribed with a line-break hyphen joined and needs the page-image check. The reading of privacy as the point the conversion is due rather than an exemption, the operational test for when code counts as public, and the caution about the figures' age are this wiki's own.
