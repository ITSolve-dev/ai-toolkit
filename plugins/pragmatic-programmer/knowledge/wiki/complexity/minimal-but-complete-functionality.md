---
title: Minimal but complete functionality
category: complexity
summary: "In existing code under review: a public operation, overload or endpoint no caller in the codebase reaches, a parameter every caller passes with the same value, or a branch for a mode nothing produces. In a diff, the same shapes belong to know-when-to-stop. Needs a caller search of the repository; published APIs excluded."
tags: [rule, yagni, dead-code, speculative-generality, complexity]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell lists **minimal but complete functionality** among the internal characteristics of a good design: the system has no extra parts (p. 78, citing Wirth 1995). He borrows Voltaire's line that a book is finished not when nothing more can be added but when nothing more can be removed (p. 78, paraphrase).

## Rule

Do not keep functionality the system does not need. McConnell's reasoning is that extra code has to be developed, reviewed, tested and reconsidered whenever other code changes, and that future versions must stay backward compatible with it (p. 78, paraphrase). His warning: «Опасайтесь вопроса: „Эту функцию реализовать легко — почему бы этого не сделать?“» (p. 78; the inner quotation marks are «» in the edition).

Fowler's *Refactoring* gives the test-only caller as the plainest sign of **Speculative Generality**: "Speculative generality can be spotted when the only users of a function or class are test cases", and the repair is to delete the test case and apply Remove Dead Code (2nd ed., ch. 3, Speculative Generality, PDF p. 95). The wider smell and its other shapes are on [[speculative-generality]].

## Sign in code

- A public method, exported function or endpoint with no caller anywhere in the codebase, apart from tests written only for it.
- A parameter or option that every caller passes with the same value, or that no caller sets.
- A branch that handles a mode or type nothing in the codebase produces.
- Convenience variants (`saveAsync`, `saveWithRetry`, `saveBatch`) beside the one actually used, with no callers of their own.
- A layer, other than a named pattern role, around a single implementation, with one call site.

The sign needs a search for callers within the codebase in front of the reader.

This wiki assigns the neighbouring cases as follows. This page owns these shapes in code as it stands. A private or file-local member with no callers, or commented-out code, is [[remove-dead-code]]; a public operation with no caller anywhere is [[minimal-but-complete-functionality]]. A parameter every caller passes with the same value is [[minimal-but-complete-functionality]]; a parameter the body ignores is [[remove-unused-parameters]]. The same shapes introduced by a change under review are [[know-when-to-stop]], which judges the diff. A named pattern role (factory, strategy, observer, visitor) with one occupant is [[do-not-force-a-design-pattern]], in a diff or in code as it stands; any other single-implementation layer is [[know-when-to-stop]] where a change adds it and [[minimal-but-complete-functionality]] in code as it stands. Where a comment or name justifies the extra part by a later need, [[replaceable-code-over-forecast]] owns it. A configuration key set by nobody is [[over-configuration]]. A public operation with no caller anywhere, inside the class or out, is [[minimal-but-complete-functionality]] (delete it). One whose only callers are inside its own class, or that serves one outside caller in that caller's terms, is [[minimize-member-accessibility]] (narrow it). An existing counterpart of an operation in use (`remove` beside a used `add`, `close` beside a used `open`) is kept even with no caller: [[minimal-but-complete-functionality]] does not report it. Whether to add a missing counterpart is [[provide-opposite-operations]], which requires a caller's workaround first.

## When not to apply

These limits are this wiki's own; the source states the rule without exceptions, apart from the word "complete" in its name.

- **Published library or API surfaces**, whose callers are outside the repository, cannot be judged by an in-repository search. Removing a public operation there is a breaking change, which is the compatibility cost the source names.
- **Completeness of an abstraction** is the other half of the rule. An existing counterpart of an operation in use (`remove` beside a used `add`, `close` beside a used `open`) is kept even with no caller. Here "minimal" yields to "complete". Adding a counterpart that does not exist is not this page's question (see [[provide-opposite-operations]]).
- **A test seam.** A member that exists so a collaborator can be substituted in tests has the tests as its purpose, so the test-only caller does not make it unused. This limit is this wiki's own.
- **Extension points** required by a framework, such as a callback the runtime invokes by reflection, have callers a search does not show.

## Repair

This wiki's own:

1. Confirm there are no callers, including reflection, configuration and other repositories if the code is published.
2. Delete the unused operation, parameter or branch, with the tests that exercise only it.
3. Where a parameter always carries the same value, inline the value and drop the parameter.
4. Rely on version control to restore it if a real need appears.

## Before and after

```
class ReportExporter
    export(report, format = "pdf", compress = false, watermark = null)
    exportAll(reports)            // no callers
    exportToFtp(report, host)     // no callers

// every call site:
exporter.export(report)
```

```
class ReportExporter
    export(report)                // writes PDF
```

## Source

[[code-complete]], ch. 5, section 5.2, Russian edition, p. 78. The rule, its reasoning and the warning are the source's. The signs, the split with [[know-when-to-stop]] by whether the shape is in a diff, the split with [[do-not-force-a-design-pattern]], the limits (including the reading of "complete"), the assignments against [[minimize-member-accessibility]], [[provide-opposite-operations]] and [[remove-unused-parameters]], the repair and the pair are this wiki's own. Related: [[managing-complexity]].

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Speculative Generality", PDF p. 95: the test-only caller as a sign and its repair.
