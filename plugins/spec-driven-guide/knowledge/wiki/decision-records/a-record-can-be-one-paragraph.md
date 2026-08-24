---
title: A record can be one paragraph
category: decision-records
summary: One source holds that a decision record is a title and one to three sentences, with every named section optional — a position that contests the templates and that this wiki resolves rather than reports.
tags: [position, decision-record, ceiling, symptom]
sources: [web-page-matt-pocock-skills-formats, madr, web-page-documenting-architecture-decisions]
created: 2026-08-08
updated: 2026-08-08
---

The whole format, quoted in full ([[skills-for-real-engineers-formats]], L44-L49):

> ```md
> # {Short title of the decision}
>
> {1-3 sentences: what's the context, what did we decide, and why.}
> ```
>
> That's it. An ADR can be a single paragraph. The value is in recording *that* a decision was made
> and *why* — not in filling out sections.

Status, considered options and consequences are demoted to optional, "only include these when they
add genuine value. Most ADRs won't need them" (L53).

## The disagreement, stated

This wiki holds [[consequences-include-the-negative]] as a rule, on Nygard's ground that a record
omitting them misleads. The source above makes consequences optional. Both cannot stand as written.

**The resolution this wiki adopts: the sections are obligations on the decision, not on the file.**
A record must state what was decided, why, and what it costs — and where a decision genuinely costs
nothing beyond itself, the third obligation is discharged in the same sentence as the second rather
than by a heading. What the minimal format removes is the *heading*; a reader still owes the cost.
Where the cost is non-obvious, [[consequences-include-the-negative]] applies in full and the
paragraph is no longer sufficient.

That reading is consistent with the source's own qualifier — sections belong "when they add genuine
value" — and it makes the two positions differ on presentation rather than on content. The
remaining live disagreement is narrow: this source would accept a record for a decision whose
consequences were never examined, and [[decision-record]] would not.

## What the position gets right

**Recording that a decision exists is most of the value.** That much is the source's own claim: "The
value is in recording *that* a decision was made and *why*" (L49).

This wiki adds the reason it matters, and the addition is ours: [[decision-log]] identifies
findability as the collection's failure mode, and an unwritten record is the worst case of it — so a
format cheap enough to always use beats a format good enough to sometimes use.

**It is not alone in noticing this.** MADR ships "bare" and "minimal" templates and describes itself
as "a template allowing to craft short, medium-sized, and large decision records" (madr, L264, L77);
[[architecturally-significant]] already records that MADR "treats the template as cheap enough that
a wrong inclusion costs little". The difference is where the floor sits, not whether a short record
is legitimate — this source removes the headings, MADR keeps them and lets each be brief.

## The entry gate, which is the sharper contribution

Three conditions, all required (L65-L69):

1. **Hard to reverse** — "the cost of changing your mind later is meaningful"
2. **Surprising without context** — "a future reader will look at the code and wonder 'why on earth
   did they do it this way?'"
3. **The result of a real trade-off** — "there were genuine alternatives and you picked one for
   specific reasons"

Each is given with its own failure: "If a decision is easy to reverse, skip it — you'll just
reverse it. If it's not surprising, nobody will wonder why. If there was no real alternative,
there's nothing to record beyond 'we did the obvious thing'" (L71).

The neighbouring test is [[architecturally-significant]], which works from Nygard's enumeration of
what a decision must touch — structure, non-functional characteristics, dependencies, interfaces,
construction techniques. This wiki reads the difference as one of form rather than of strictness:
that test names categories to match a decision against, this one asks three questions about the
decision in front of you. They select overlapping but different sets, and the second condition —
whether a future reader would be surprised — has no counterpart in the enumeration.

## The symptom

**A record whose sections are filled but whose paragraph would be empty.** Compress any record to
title plus three sentences — what was the context, what was decided, why. Where the compression
loses nothing, the sections were furniture; where it cannot be done at all, the record is carrying
more than one decision.

**A record for a decision that had no alternative.** Its "Considered Options" section names one real
option and one straw one. That is the third gate condition failing, and the repair is deletion.
