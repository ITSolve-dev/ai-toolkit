---
title: Superseding, not editing
category: decision-records
summary: A reversed decision is marked superseded and kept — because what was decided at the time is itself the information a later reader needs.
tags: [rule, decision-record, immutability, status]
sources: [web-page-documenting-architecture-decisions]
created: 2026-08-06
updated: 2026-08-06
---

A [[decision-record]] is not revised when the decision changes. It is left standing and marked, and
a new record carries the new decision:

> If a decision is reversed, we will keep the old one around, but mark it as superseded. (It's
> still relevant to know that it *was* the decision, but is *no longer* the decision.)
>
> — [[documenting-architecture-decisions]], L40

The status field carries this: "proposed" before agreement, "accepted" after, and "deprecated" or
"superseded" with a reference to the replacement once a later record changes it (L58).

Numbering supports the same property: records are "numbered sequentially and monotonically. Numbers
will not be reused" (L38). An identifier that always denotes the same record is what makes a
reference from elsewhere safe.

## Why the history is the content

An edited record answers "what do we do?" A superseded one answers "what did we believe, and what
changed?" — and the second question is the one a reader facing a puzzling decision is actually
asking. Deleting the old record destroys the only evidence that the current decision is a
*revision*, and a revision carries information an original does not: that the first answer was
tried and found wanting.

There is a practical consequence too. Records chain — the consequences of one become the context of
the next ([[decision-record]]). A record deleted rather than superseded silently invalidates the
context of every record that was written against it, with no trace of where the break happened.

## The symptom

**A record whose content no longer matches its date.** If a record describes current practice but
was written two years ago and nothing supersedes it, either nothing changed — possible — or it has
been quietly edited. The second is detectable by asking whether any record explains the change; a
practice that visibly differs from what earlier records established, with no superseding record
anywhere, means the chain was broken rather than extended.

A second, milder symptom: a status of "accepted" on a record whose decision the team no longer
follows. The status field is only load-bearing if it is maintained; where it is decorative, the
whole mechanism is.

## Its limit

Superseding preserves history at the cost of making the current state harder to read: the set of
records no longer states what is true, only what was decided when. Anyone consulting them must
follow the chain. This is the same trade that produces the amendment drift noted for design docs in
[[design-doc]], and it is the reason the collection needs an entry point of its own once it grows.
