---
title: Consequences include the negative
category: decision-records
summary: A consequences section listing only benefits has not been written honestly — and the omission disarms the future reader the record exists to serve.
tags: [rule, decision-record, symptom, rationale]
sources: [web-page-documenting-architecture-decisions]
created: 2026-08-06
updated: 2026-08-06
---

The consequences section of a [[decision-record]] "describes the resulting context, after applying
the decision", and the requirement on it is explicit:

> All consequences should be listed here, not just the "positive" ones. A particular decision may
> have positive, negative, and neutral consequences, but all of them affect the team and project in
> the future.
>
> — [[documenting-architecture-decisions]], L64-L67

## The symptom

**A consequences section containing only benefits.** Trivially detectable: read the section and
count the entries that cost something.

**A consequences section with no neutral entry.** Also trivially detectable, and this wiki expects
it to be the more common of the two — the reasoning being that neutral consequences, things that
merely become different, are what someone notices while *describing* an outcome rather than
*defending* a choice. A section with positives and negatives but no neutrals may therefore still be
an argument, balanced for appearance.

That second reading is an inference of this wiki's, not a claim of the source's, and it has not
been measured against any corpus. Treat the count as the finding and the interpretation as a
hypothesis.

## Why the omission is expensive

The record's purpose is to let a future reader decide whether to keep the decision
([[documenting-architecture-decisions]]). That reader needs the costs more than the benefits: the
benefits are visible in the system as built, while the costs are what they are currently
experiencing and cannot attribute. A record that hides them produces exactly the blind acceptance
the genre exists to prevent — the reader sees a decision that sounds unambiguously good, concludes
the pain must come from somewhere else, and leaves it in place.

There is a second effect. Because "the consequences of one ADR are very likely to become the
context for subsequent ADRs" (L75), an under-stated consequence corrupts the context of every
decision made after it. The forces the next record balances will be missing one that is actually
present.

## Distinguishing this from its neighbours

- [[alternatives-considered]] records what *else* could have been chosen. Consequences record what
  follows from what *was*. A record can have honest consequences and still hide that a better
  option existed.
- [[non-goals]] bound what the work is judged on, before the fact. Consequences report what
  happened to be true after the decision, including things nobody wanted and accepted anyway.

One source makes this section optional — see [[a-record-can-be-one-paragraph]], where the collision
with this rule is stated and resolved: the obligation is on the decision, not on the heading.
