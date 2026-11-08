---
title: Use a comment style that is easy to change
category: documentation
summary: "A comment's decoration has to be realigned by hand when its text changes: dot leaders between a name and its meaning, a right-hand border of asterisks, a dashed rule ending in a plus, or a column of line comments over long prose."
tags: [rule, comments, maintenance, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**A maintainable comment style** is one whose form does not have to be rebuilt each time its words change. McConnell's reason is the one that makes comments lie: «Если комментарии трудно изменять, их просто не будут изменять». An unchanged comment becomes wrong and misleading, which is worse than having none (p. 771). Anything that slows the editing of a comment therefore lets it drift from the code; see [[comment-why-not-how]].

This page sits near mechanical style, which the charter excludes. This wiki keeps it because its reason is the comment's correctness, not its look, and a formatter usually does not remove such decoration.

## Rule

Use styles that do not discourage changing comments (p. 771). Given a choice, and there usually is one, «комментарии лучше сделать правильными, чем красивыми» (p. 771). The book's examples (pp. 771-773):

- A table of variables with dot leaders between each name and its meaning. The dots are what nobody will maintain.
- A boxed header whose right edge is a column of asterisks. Changing any line means realigning the column. A box with only top and bottom borders looks almost as good and is far easier to keep (p. 772).
- Section headings drawn as dashed lines ending in a plus. Every change to the text means adjusting the line so the plus stays in place, and nobody knows what to do when the heading wraps.
- Long prose written as a column of single-line comment markers. That is fine while the text is short and tedious to rewrap once it grows, so the block-comment syntax suits text of several lines better (p. 773).

The book states the limit itself. If an editor realigns the asterisks with one keystroke, the style is fine, because «Проблема не в звездочках, а в том, что их трудно поддерживать» (p. 772). Its broader point is to watch where the time goes: typing or deleting dashes to align pluses is not programming (p. 773).

## Sign in code

- A right-hand border (a column of `*`, `|` or `#`) closes each line of a comment block.
- Dot or dash leaders pad names out to a column before their descriptions.
- A decorative rule's length is tied to the text it underlines or frames.
- Prose of several paragraphs carries a line-comment marker on every line and is broken by hand.

## When not to apply

- A tool keeps the decoration: a formatter, an editor command, a documentation generator. The book allows this (p. 772).
- A rule of fixed width that does not depend on the text, such as the same number of dashes each time, needs no maintenance. The book suggests exactly that for emphasis (p. 773).
- The project's formatter or the language's convention prescribes the comment syntax. That decides at work time, and this page applies only to decoration the convention leaves free. This limit is this wiki's own.

## Repair

1. Remove whatever has to be realigned when the text changes: right borders, leaders, rules matched to the text's length.
2. Keep emphasis that does not depend on the text, such as a top and bottom border.
3. Move long prose into the block-comment form the language offers, or into a doc comment that the tooling reflows.

## Before and after

```
// before
/*****************************************
 * entry point is evaluate(), at the     *
 * end of the file                       *
 *****************************************/
// x_pos ........ X coordinate (metres)
// y_pos ........ Y coordinate (metres)
```

```
// after
/*****************************************
   entry point is evaluate(), at the end of the file
 *****************************************/
// x_pos: X coordinate (metres)
// y_pos: Y coordinate (metres)
```

## Source

[[code-complete]], ch. 32, section 32.4, pp. 770-773. The book's parts: the rule, its reason, the four examples, the easier box, and the limit for alignment a tool maintains. This wiki's own parts: the general wording of the signs, the limit for project formatters, the reason for keeping the page under this charter, and the pseudocode.
