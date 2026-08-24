---
title: Imprecise terminology
category: statement-quality
summary: A word used for several things at once makes statements containing it unfalsifiable — and the demand for more structure is usually a demand to avoid defining the word.
tags: [failure-mode, terminology, symptom, statement]
sources: [c4-model]
created: 2026-08-06
updated: 2026-08-06
---

[[the-c4-model]] makes an argument its authors reached from a narrow complaint — that four levels
are too few — and it generalises well past its origin.

The complaint: "A database is a database; debating whether it is also a Container or a Component
just isn't worthwhile." The response:

> The problem here is that we're often too imprecise with the terminology that we use in our
> day-to-day work, which leads us to make the wrong decisions when trying to categorise the
> building blocks that make up our software systems. The word "database" is used in the quote
> above, but is it being used to refer to a database server, a database schema, a collection of
> related data, or something else entirely?
>
> — L425

## The worked demonstration

The example given is a single sentence whose truth depends entirely on which meaning is in play:

> "microservices shouldn't share a database"

Under *database server*, this is a deployment claim. Under *schema*, a coupling claim. Under
*collection of related data*, an ownership claim about the domain. The three are not variations of
one statement; they are three different assertions, and a reader cannot tell which was meant.

**This is the symptom in its clearest form: a sentence that cannot be agreed or disagreed with
until a word in it is pinned down.** It is detectable without knowing the subject — substitute each
plausible meaning and see whether the claim changes. If it does, the sentence has not yet said
anything.

## Why the demand for more structure is a symptom of the same thing

The source's sharper claim is that requests for additional levels usually come from one of two
places (L432-L435):

- The levels are being misused, so more seem to be needed.
- What is being modelled is "really organisational constructs or groupings, rather than
  abstractions in their own right — subsystems, bounded contexts, layers, libraries".

In both cases the fix is to define the terms, not to add machinery. And the warning against adding
levels anyway is precise: it can be done, but only "if you're willing to put the effort into
precisely defining those additional levels of abstraction. Failure to do so will ultimately lead
you back to where we are today" (L437).

That is a general property of structural fixes for vocabulary problems. Adding a category to hold
an ill-defined term relocates the imprecision; it does not remove it.

## The constructive form

Forcing the categorisation is what surfaces the ambiguity: "Debating whether a database is a
container or a component forces you to understand exactly what you mean by the word 'database',
before mapping it onto the abstraction levels" (L438). The apparently unproductive argument is the
mechanism that makes the vagueness visible.

Related: [[mixed-levels-of-abstraction]] uses generic vocabulary as the surface signal that a
description has lost its level. That is consistent with this page — the source's stated direction
is vocabulary → confusion — so the repair order is fixed: **define the word first**, and see
whether the level question survives it.

Also related: [[leading-words]], the constructive counterpart — where this page removes a word that
cannot be checked, that one installs a word that names an observable state.
