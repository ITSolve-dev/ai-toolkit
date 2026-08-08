---
title: Architecturally significant
category: decision-records
summary: The entry test for what earns a decision record — a decision affecting structure, non-functional characteristics, dependencies, interfaces, or construction techniques.
tags: [decision-rule, decision-record, criterion]
sources: [web-page-documenting-architecture-decisions, madr]
created: 2026-08-06
updated: 2026-08-06
---

Not every decision deserves a record. [[documenting-architecture-decisions]] draws the boundary by
enumeration:

> We will keep a collection of records for "architecturally significant" decisions: those that
> affect the structure, non-functional characteristics, dependencies, interfaces, or construction
> techniques.
>
> — L30

Five categories, and the enumeration is the definition — there is no separate principle offered
above it. A second, looser statement adds the practical form: "It should be something that has an
effect on how the rest of the project will run" (L73).

## Reading the list

The five are not arbitrary. Each names a decision whose reach extends past the place it is made:

- **Structure** — how the parts are divided, which is exactly the choice
  [[information-hiding]] governs. Reversing it later touches everything.
- **Non-functional characteristics** — the properties nothing points at and everything depends on.
  These are the decisions most often reversed blindly, because the requirement they served is
  invisible in the code.
- **Dependencies** — what the work is now tied to, and cannot easily be untied from.
- **Interfaces** — the commitments others build against; see
  [[abstract-interface-vs-representation]].
- **Construction techniques** — how the work is habitually done, which propagates by imitation
  rather than by reference and is therefore the hardest to reverse.

## Using it as a test

The source's own test is the enumeration plus its looser second statement — does this have "an
effect on how the rest of the project will run" (L73). Run it directly: does the decision fall in
one of the five categories, and does it reach past where it was made?

- **Confined to where it was made** — no record needed. The code carries it.
- **Reaches other work, other teams, or things already built against it** — record it, because the
  reader who wants to reverse it will not otherwise be able to see what they are about to break.

**A reconstruction of this wiki's, offered as such.** What appears to unite the five is *cost of
reversal* rather than importance — a consequential decision that can be undone locally needs no
record, a modest one that has spread does. This reading is not Nygard's; he offers no principle
above the enumeration. It is useful because it extends to categories he did not list, and it should
be treated as a hypothesis rather than as the definition: it fits *structure*, *dependencies* and
*interfaces* well, and fits *non-functional characteristics* less obviously, since those are
recorded because they are invisible rather than because they are costly to undo.

Either way, the test explains the two failure responses the genre exists to prevent: blind
acceptance and blind reversal both come from a reader who cannot see the reach of what they are
looking at.

## The disagreement about where the gate belongs

Not everyone accepts that there should be a gate. The [[madr-template]] argues the opposite
position openly: "Do not take the term 'architecture' too seriously or interpret it too strongly",
and, noting that "there are debates about what is an architecturally-significant decision", offers
its template "to capture any decision" (madr, L94-L98).

Its examples are worth reading carefully, because they are weaker evidence than they look. A choice
between logging libraries is a **dependency** — one of Nygard's five categories, and inside his
gate rather than outside it. The one example that genuinely falls outside is the choice of IDE. So
the disagreement is real but narrow: MADR's position is not that Nygard's categories are wrong, but
that maintaining a gate at all costs more than it saves.

The two positions differ on what the cost of a record is. Nygard treats writing one as effort to be
justified by reach. MADR treats the template as cheap enough that a wrong inclusion costs little,
and a wrong exclusion costs the record you later wanted. Neither is refuted by the other, and the
choice is a local one: the gate matters where records are expensive to write or numerous enough to
search, and matters little where they are neither.

What both agree on is the failure the record prevents — a reader who cannot see why something was
chosen — so the gate is a question of volume, not of purpose.

Related: [[decision-record]] for what to write once the test passes,
[[when-to-write-a-design-doc]] for the parallel entry test in the neighbouring genre — there the
trigger is ambiguity, here it is reach.
