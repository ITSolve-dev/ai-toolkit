---
title: Context pointer
category: writing-for-agents
summary: The reference by which a reader reaches material held outside the document — and the wording of the reference, not the quality of the target, decides whether it is ever reached.
tags: [concept, agent-reader, structure, symptom]
sources: [web-page-writing-for-agents]
created: 2026-08-08
updated: 2026-08-08
---

A **context pointer** is "a reference held in the agent's context that names some out-of-context
material and encodes the condition for reaching it" ([[writing-for-agents-reference]], L30). A
line in an index naming a document is one; so is a cross-reference at the foot of a section.

The claim that makes it a concept rather than a formatting note is about where the failure lives:

> The pointer's *wording*, not its target, decides when the agent reaches the material — and how
> reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the
> wording first, and inline the material only if sharpening fails.
>
> — L30

This wiki reads the repair order as the load-bearing part. The instinct on discovering that a
reader missed something is to move the material closer — into the document, into the section that
needed it. The source puts that last: the cheap fix is to rewrite the sentence that points at it,
and inlining is what you do when rewriting has failed.

## What a pointer must carry

Two jobs, per L32: **state what the material is**, and **list the branches that should trigger
reaching it** — a branch being "a distinct case the document handles, so different runs take
different paths through it".

Three rules follow, each stated as an edit (L34-L36):

| Rule | What it removes |
|---|---|
| Front-load the leading word | Words before the one that does the triggering |
| One trigger per branch | Synonyms that rename a single branch — "one branch written twice" |
| Cut identity the body already carries | Restatement of what the target obviously is |

The source's reason for the extra severity is that a pointer is always loaded while its target is
not, so "every word of an always-loaded pointer costs on every turn" and "it earns even harder
pruning than the body" (L32). See [[the-two-loads]].

## The symptom

**A pointer whose triggering word is not in its first clause**, and **two pointers whose triggers
are synonyms.** Both are visible in the text without knowing anything about the target: read only
the opening words of every cross-reference in a document and ask what each one would fire on. A
pointer that needs its second sentence to say what it is for will be reached late or not at all.

A third, harder symptom: material that is demonstrably needed and demonstrably unread. That is the
variance bug above, and the check is the repair order — try sharpening the pointer before
concluding the material belongs inline.

## Where this bites in an ordinary document

The wiki's own experience is the example. [[minimal-is-not-short]] is the floor under every cutting
rule here, and a review of the link graph found it unreachable from most groups — a must-have
target behind pointers too weak to fire. The material was never at fault.

Related: [[the-information-hierarchy]], which decides whether a piece of material should be behind
a pointer at all; [[unresolvable-references]], for the pointer that names something the reader
cannot obtain.
