---
title: Know when to stop
category: complexity
summary: "A change adds an option, parameter or layer no caller needs and cites no future need, or rewrites working code with no defect and no requirement behind the rewrite."
tags: [rule, overengineering, feature-bloat, polish, good-enough]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

**Knowing when to stop** is the rule against spoiling a working program by adding to it past what it needs. The book compares it to a painter who loses the painting under layer after layer of paint (p. 42). What separates stopping from sloppiness is on [[good-enough-versus-broken-window]].

## Rule

«Старайтесь не испортить грамотно написанную программу чрезмерными украшательствами и усовершенствованиями.» (p. 42). The book adds that the program will never be perfect anyway (p. 42). This wiki reads that as ruling out perfection as a stopping point.

This wiki adds two reasons from nearby passages, which the book does not give for this rule. An exercise on feature bloat notes that «каждое функциональное средство может стать источником программных ошибок и брешей в защите», and that the more features there are, the harder each is to find when needed (p. 43). And in its section on compromising with users, the book remarks that what may be needed a year from now will turn out different anyway (p. 41), which this wiki takes to undercut polishing toward it today.

## Sign in code

The book gives none. The list below is this wiki's own, and each item is a count or a relation a reader can check:

- an option, flag, parameter or branch added by the change that no caller in the repository reaches;
- a parameter every caller passes with the same value;
- a behaviour-preserving rewrite inside a change whose stated purpose is something else, of code on which no page of this wiki has a finding;
- a layer, other than a named pattern role, added around a single implementation, with one call site.

For a published interface, the first two need knowledge of callers outside the repository, which the code does not hold. They are not signs there, and a finding would need that usage data. That code could merely be shorter is not a sign.

A comment or name that justifies the addition by a later need selects [[replaceable-code-over-forecast]], which owns that sign and asks for more before a verdict. With no stated need, the count here decides. A named pattern role (factory, strategy, observer, visitor) with one occupant is [[do-not-force-a-design-pattern]], in a diff or in code as it stands; any other single-implementation layer is [[know-when-to-stop]] where a change adds it and [[minimal-but-complete-functionality]] in code as it stands. A configuration key belongs to [[over-configuration]]. The same unused shapes in code as it stands, outside a change under review, are [[minimal-but-complete-functionality]]. A rewrite mixed into a behavioural edit is split under [[do-not-refactor-while-adding-features]], and this page decides only whether the moved part stays.

## When not to apply

- High-stakes software. For a pacemaker, an autopilot or a low-level library meant for wide distribution, the book says «требования будут более строгими» and the choice narrower (p. 41). This wiki reads that as more work on tests and failure paths, not as room for more features.
- The floor is not met. Good-enough does not cover sloppy code (p. 40), so a rewrite that removes a real finding is a repair, not polish.
- The rewrite is preparation for a requirement in the same change, and the requirement needs it. This limit is this wiki's own.
- An extension point exists for outside users, and the project says so. This limit is this wiki's own.
- The layer confines a third-party product or wraps an external resource. [[hide-third-party-apis]] and [[global-data]] own those shapes, and one implementation is normal there. This limit is this wiki's own.

## Repair

Delete the addition no caller reaches. Inline the single-implementation layer. Move an unrelated rewrite out of the change, or drop it. Keep what a stated requirement needs and nothing more. The cost is that a need arriving later has to be built then, which this rule accepts as cheaper than carrying unused code until it does.

## Before and after

```
// before: the request was a CSV export; only "csv" is ever passed
function export(rows, format = "csv", delimiter = ",", quote_all = false):
    writer = Writer(format, delimiter, quote_all)
    return writer.write(rows)
```

```
// after
function export_csv(rows):
    return rows.map(to_csv_line).join("\n")
```

## Source

[[pragmatic-programmer]], Topic 5, pp. 40-43. The rule, the painter analogy, the point about perfection, the feature-bloat exercise, the year-from-now remark and the high-stakes limit are the book's. Setting those two remarks under this rule as its reasons, the reading of perfection and of the year-from-now remark, the signs, the splits with [[replaceable-code-over-forecast]], [[do-not-force-a-design-pattern]] and [[do-not-refactor-while-adding-features]], the limits marked as such, the repair, the reading of the cost and the pseudocode are this wiki's own.
