---
title: Decision log
category: decision-records
summary: The accumulated collection of decision records, which becomes an artifact in its own right — with properties, and problems, that no single record has.
tags: [concept, decision-record, collection]
sources: [web-page-architectural-decision-records-adrs, madr, web-page-documenting-architecture-decisions]
created: 2026-08-06
updated: 2026-08-06
---

The **decision log** is the set of decision records a project accumulates. The ADR organisation's
own definitions place it as a distinct thing from the records that compose it:

> An *Architectural Decision Record (ADR)* captures a single AD and its rationale […] The
> collection of ADRs created and maintained in a project constitute its *decision log*.
>
> — web-page-architectural-decision-records-adrs, L17

Its accompanying vocabulary: an **architectural decision** is "a justified design choice that
addresses a functional or non-functional requirement that is architecturally significant", and an
**architecturally significant requirement** is one "that has a measurable effect on the
architecture and quality" of the system (same source, L17). The chain is requirement → decision →
record → log.

## What the collection has that a record does not

**Chained context.** The consequences of one record become the context of the next
([[decision-record]]), so the log carries reasoning no single record states: why the space of
available options had already narrowed by the time a later decision was made.

**A history of reversals.** Because a changed decision is superseded rather than edited
([[superseding-not-editing]]), the log shows which questions the project has answered more than
once — usually the questions worth watching.

## Its failure mode: findability

The problem is scale, and it is acknowledged rather than solved. "Large projects may accumulate
hundreds of decision records over time, and finding them might be hard" (madr, L156).

The symptom is a reader who cannot tell whether a decision exists. They then make it again, and the
log gains a second record contradicting the first with no reference between them — the same blind
change the genre exists to prevent, now committed by someone who did consult the documentation.

The common response is to group records into categories, and it costs the one property that made
cross-references safe: an identifier unique across the whole collection rather than only within a
group (madr, L172). Findability and referential stability trade directly against each other, and no
source here resolves the trade. What the one source addressing it does say is that the choice is "a
meta-decision to be made rather early on" (madr, L172) — and, being a decision with reach, one that
deserves its own record.

How a collection is stored and named is doc tooling, which this wiki's charter excludes; the trade
above is in scope because it is a property of the collection rather than of the tool.

Related: [[architecturally-significant]] — the entry gate exists largely to keep this collection
searchable, which is why the argument about the gate is really an argument about volume.
