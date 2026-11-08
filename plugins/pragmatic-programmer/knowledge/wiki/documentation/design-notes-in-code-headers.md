---
title: Record key design decisions in file and class headers
category: documentation
summary: "A file or class header only restates its name or lists members, or is missing, while the body holds a choice it never names (a cache, chunked or lazy processing, an unexpected data structure, a departure from sibling units): say what the unit hides, why it is arranged so, and which alternative was rejected."
tags: [rule, header-comment, design-rationale, comments]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell lists several lightweight ways of recording a design. Only one of them lives in the code: documenting the main design aspects in comments, usually in the headers of files or classes. Combined with a documentation extractor such as JavaDoc, this puts the design note next to the code it describes. Programmers working on that code can then reach it easily, and they are more likely to keep it current (p. 114).

## Rule

Put the key design decisions of a unit in its file or class header comment, where the person changing the unit will read it. The book frames this as one option among many (wiki, email summaries, photos of whiteboards, posters, CRC cards, UML), to be mixed per project (pp. 114-115). Recording outside the code is a matter for project documents and the `spec-driven-guide` plugin, not this wiki.

## Sign in code

- A file or class header holds only the unit's name, a restatement of it, or a list of its members, or there is no header, while the body contains a choice the header does not name: a cache, lazy or chunked processing, a data structure other than the obvious one, a deliberate departure from how sibling units are built.
- A header comment describes a design that the code below it no longer follows.

This wiki assigns the neighbouring case as follows. This page owns the header of a file or class; a comment on a routine or a line that restates its code, or omits the reason for a surprise, is [[comment-why-not-how]]. A missing doc comment on an export, judged by its contract, is [[documentation-in-the-source]]; a file or class header, present or absent, judged by whether it states what the unit hides and why it is built this way, is [[design-notes-in-code-headers]].

## When not to apply

- The unit's design is obvious from its name and interface: a plain data holder, a thin adapter, a unit that follows the project's standard pattern. A header that explains nothing non-obvious is noise.
- The decision spans many units and is recorded in a decision record the project keeps. A one-line pointer in the header is enough, and the reasoning is not duplicated.
- The project's convention puts module-level design notes somewhere else that sits next to the code, such as a package README.
- The project records design in formal documents by convention. The header then points to them; the book offers in-code notes as one lightweight option, for an informal approach or small systems (p. 114).

## Repair

Write a header that states what the unit hides (the secret it keeps from its callers, see [[information-hiding]]), why the unit's code is arranged as it is, and any alternative rejected for a reason a future maintainer would otherwise rediscover. Delete header text that only repeats the name or lists members.

## Before and after

```
// before
// ReportFormatter - formats reports.
class ReportFormatter
  ...
```

```
// after
// ReportFormatter hides the report layout: column widths, heading centering, page breaks.
// Callers pass rows only; a change of layout must not reach them.
// Layout is computed per page, not per report, so very large reports stream.
class ReportFormatter
  ...
```

## Source

[[code-complete]], ch. 5.4, "Recording the design process", Russian edition, pp. 114-115. The book states the practice and its reason: close to the code, easy to find, more likely kept current. What a header should state (secret, split, rejected alternative), the signs, the owner assignments and the limits, apart from the lightweight framing of p. 114 in the last one, are this wiki's own. Related: [[source-code-as-the-authoritative-description]], [[documentation-in-the-source]].
