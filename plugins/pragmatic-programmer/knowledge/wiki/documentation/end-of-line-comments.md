---
title: Avoid end-of-line comments
category: documentation
summary: "A trailing comment restates its own line, sits on a block header so it is unclear how many lines it covers, records a bug number, date and initials, or marks the end of a long nested block."
tags: [rule, comments, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**End-of-line comments** are comments written to the right of a statement. By *Code Complete*'s account they are mostly harmful outside a few named cases: they are hard to keep aligned, they turn cryptic for lack of room, and they usually restate a single line (pp. 775-777).

## Rule

The book's practical objections come first. Such comments have to be aligned to the right of the code, or the listing looks shredded. Lengthening one line pushes its comment out and forces the rest to be realigned, and «Стили, которые трудно поддерживать, никто не поддерживает» (p. 775). After a few changes the comments make the code worse. There is little room at the right edge, so the comment aims to be as short as possible rather than as clear as possible (p. 775).

Its objections of principle (pp. 776-777):

- **Not for single lines.** It is hard to say anything meaningful about one line, so most such comments repeat it (p. 776).
- **Not for several lines.** A comment like "compute discounted rates" on a loop header leaves the reader to work out from the code whether it covers the statement or the whole loop (p. 776).
- **Not for maintenance notes.** A bug number, a date and the programmer's initials belong in version control: «Комментарии должны объяснять, почему код работает сейчас, а не почему он когда-то не работал» (p. 777).

The book allows them for data declarations, where a long enough line leaves room for a meaningful note (pp. 776-777), and to mark the ends of long blocks (p. 777), and later for parameters at their declaration (p. 789). It ties the last case to a warning of its own. An end-of-loop comment helps in long nested loops, but needing one shows the code is too complex (p. 786): «Если цикл настолько сложен, что в его конце нужен комментарий, подумайте, не упростить ли цикл» (p. 787). The book says the same holds for complex `if` statements and `case` blocks.

## Sign in code

- A trailing comment whose words can be derived from its own line (`free(p)  // free the memory`).
- A trailing comment on the opening line of a loop or conditional, with the block's body below it.
- A trailing comment holding a ticket number, a date or initials.
- A trailing comment full of abbreviations a reader has to decode (p. 781).
- A closing brace or `end` carrying `// end while` or `// end if processing`, where the block is long or nested.

This wiki assigns the neighbouring cases as follows. A comment to the right of a statement is [[end-of-line-comments]], which owns its placement; what the comment says is judged by [[comment-why-not-how]]. The repair here also moves comments. End-of-line *alignment of code*, statements aligned under a keyword in the line above, is [[layout-must-tell-the-same-story-as-the-logic]]. An end marker on a block that [[loop-length-and-nesting]] finds too long is that page's finding; [[end-of-line-comments]] reports an end marker only on a block below that page's limits.

## When not to apply

- Data declarations and parameter lists, where a trailing note states units, range or direction that the name does not carry. See [[comment-data-declarations]] and [[routine-header-comment]].
- End markers on long or deeply nested blocks that cannot reasonably be shortened. The book finds them worth their cost there (p. 787). Short blocks with no nesting do not need them.
- A project convention or tool that requires a trailing form, such as a linter suppression pragma. This case is this wiki's own; the book does not treat it.

## Repair

1. Delete a trailing comment that restates its line.
2. Move a trailing comment on a block header to its own line before the block, phrased as the block's intent; see [[comment-why-not-how]].
3. Move change notes to the commit message and delete them from the code.
4. Where a block needs an end marker, first try to shorten it by extracting its body or reducing nesting. Keep the marker only if that fails.

## Before and after

```
// before
for i in 1 .. rate_count             // compute discounted rates
    regular = lookup_regular_rate(i)  // look up the rate
    rate[i] = regular * discount[i]
for i in 1 .. max_elements - 1       // fixed bug #A423 01.10.05 (scm)
    ...
```

```
// after
// compute discounted rates
for i in 1 .. rate_count
    regular = lookup_regular_rate(i)
    rate[i] = regular * discount[i]
for i in 1 .. max_elements - 1
    ...
```

## Source

[[code-complete]], ch. 32.5, pp. 775-777, 781 and 786-787; p. 789 for parameters. The book's parts: the practical objections and those of principle, the ban on maintenance notes, the allowed uses, and the reading of end-of-loop comments as a warning of complexity. This wiki's own parts: the signs, the assignments against neighbouring pages, the limit for tool pragmas, the order of the repair, and the pseudocode. The quotations were transcribed from the extracted text and should be checked against the page image.
