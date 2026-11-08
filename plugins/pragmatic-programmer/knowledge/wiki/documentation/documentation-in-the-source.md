---
title: Keep documentation in the source
category: documentation
summary: "An exported function or module has no doc comment, its contract lives only in a separate file, or its doc comment names a parameter the signature no longer has."
tags: [rule, docstring, api, documentation, dry]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

**Keeping documentation in the source** is the rule that the description of a module or an exported function lives on it, not in a separate file written later. The book treats documentation as an integral part of development and not as a chore for the end of a project (p. 54). Comments inside an implementation are covered by [[comment-why-not-how]].

## Rule

«Храните исходный код и документацию вместе.» (p. 55). Documentation gets easier when effort is not duplicated and it is kept at hand, in particular in the source itself (p. 54), and the same pragmatic principles apply to it as to code (p. 54). Concretely, «модули и экспортируемые функции рекомендуется снабжать комментариями», to spare the developers who will have to use them (p. 54).

The Russian wording of the tip on this page, «Создавая документацию, не фиксируйте ее навечно» (p. 54), does not match the surrounding argument. This wiki relies on the paragraph and on the summary line on p. 55, not on that wording.

## Sign in code

- An exported function, type or module has no doc comment, and its contract can be learned only from its body.
- An export's behaviour is described in a separate document, and the source neither holds that description nor points to it.
- A doc comment names a parameter, return value or failure the signature or body no longer has.

An exported routine with no doc comment, or one whose doc comment states a contract the names and types cannot, belongs to [[documentation-in-the-source]]. A comment, above a declaration or inside a body, that restates steps, numbers or names the body already holds belongs to [[comment-why-not-how]]; a doc comment that says what a vaguely named class or method is for, without restating its body, belongs to [[tests-instead-of-documentation]]. A missing doc comment on an export, judged by its contract, is [[documentation-in-the-source]]; a file or class header, present or absent, judged by whether it states what the unit hides and why it is built this way, is [[design-notes-in-code-headers]]. *Elegant Objects* disagrees with this page's call for doc comments; [[tests-instead-of-documentation]] resolves the disagreement per setting.

## When not to apply

- Non-exported code. The book explicitly rejects commenting every function, data structure and type (p. 54). A missing precondition there is a different question, and [[state-the-contract]] owns it. This page owns only whether an export carries a doc comment.
- An export whose name and types state its whole contract. A comment there only repeats them, which is the failure on [[comment-why-not-how]]. This limit is this wiki's own.
- A document about the design of a system rather than one interface. That is out of scope here and belongs to `spec-driven-guide`.

## Repair

Move the contract to a doc comment on the export: what it does, what it requires, what it returns, how it fails. If an external document is still needed, generate it from that comment or link to it, so the text exists once. The cost the book names for mechanical commenting applies here too: a change to the contract now has to update the comment as well.

## Before and after

```
// before: the contract is only in docs/payments.md
export function charge(card, amount):
    ...
```

```
// after
// Charges the card once. amount must be positive. Fails with Declined or GatewayDown.
export function charge(card, amount: MinorUnits):
    ...
```

## Source

[[pragmatic-programmer]], Topic 7, pp. 54-55. The rule, the recommendation to comment modules and exports, the rejection of commenting everything and the point about updating both are the book's. The signs, the limit on self-explanatory exports, the split with [[state-the-contract]] and [[design-notes-in-code-headers]], the scope note, the list of what a doc comment holds, the advice to generate or link, and the pseudocode are this wiki's own. So is the reading taken of the tip on p. 54, which is reported as printed: this wiki rests the rule on the surrounding paragraph and the summary line on p. 55. Related: [[doc-examples-from-tested-code]], [[source-code-as-the-authoritative-description]].
