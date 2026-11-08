---
title: "DRY: one representation for each piece of knowledge"
category: complexity
summary: "The same fact written in two places: a literal or format repeated inside a repeated expression, a copy-pasted branch differing by one operand, or a value tied to another with nothing in code linking them."
tags: [rule, duplication, knowledge, maintenance]
paradigm: any
sources: [pragmatic-programmer, object-oriented-thought-process, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

DRY (Don't Repeat Yourself) is about duplicated knowledge and intent, not about repeated lines of text. The authors say the first edition misled readers into hearing only "do not copy and paste", which they call the small and simple part of the principle (pp. 61-62).

## Rule

The book's formulation: «У каждого фрагмента знаний должно быть единственное, недвусмысленное, непререкаемое представление в системе» (p. 61).

The reasoning is that knowledge is unstable: a client meeting, a changed regulation or a failed algorithm can each overturn it. The authors argue that developers are therefore always in maintenance mode, and that maintenance is a normal stage of development which begins well before release (pp. 60-61). Two copies mean a change must be remembered in both, and on that they write: «И вопрос не в том, чтобы вспомнить об изменениях, а в том, когда они забудутся» (p. 61).

The book's touchstone: if one property of the code has to change, does that force edits in many places, in different formats, such as code and documentation, or a schema and the structure holding it (p. 62)?

Weisfeld's *The Object-Oriented Thought Process* (ch. 8) traces how the copy-and-paste kind drifts. Reuse «часто оказывается результатом операций вырезания, копирования и вставки» (p. 170): most of a copy stays the same, but it still has to be changed a little for its new home (p. 170). Under deadline a fix goes into the one copy that needs it now, may quietly harm the others, and «изначально совместно используемый код может разниться и приходится сопровождать отдельные кодовые базы» (p. 171). In his story the pizza site's copy becomes "version 2.01papa", and the copies multiply until merging them back would cost too much (p. 171). His repair is to factor out as much commonality as possible into one `Shop` that every application honours (pp. 171-172). He notes that code often ends up tightly bound to the application it was written for (p. 170).

Fowler's *Refactoring* puts **Duplicated Code** first among the smells: "If you see the same code structure in more than one place, you can be sure that your program will be better if you find a way to unify them" (2nd ed., ch. 3, Duplicated Code, PDF p. 86). He names two costs. Every time the copies are read, they have to be read carefully to see whether there is any difference, and a change to the duplicated code has to find and catch each copy (PDF p. 86).

## Sign in code

- A branch repeated with only the operand changed, such as the same negative-number handling for two fields (p. 62).
- A literal repeated across calls as part of one repeated expression, such as one field width in every print call (p. 63). This wiki does not count `0`, `1` or an empty string, whose repetition states no fact by itself. A meaningful literal written bare, once or repeatedly, is [[named-constants-over-literals]]; a literal repeated inside a repeated expression or decision, and a fact restated in any other form, is [[dry]].
- A value tied to another value with nothing in code expressing the link, such as a separator whose length is tied to a column width, which the book counts as a remaining violation (p. 64). This wiki requires a name, a comment or a requirement in hand to confirm the tie, because two values that merely agree show nothing.
- One fact stated in two forms in front of the reader: a function body and a comment, see [[comment-why-not-how]]; a field and the fields it derives from, see [[stored-derived-data]]; a hand-written structure and the schema it mirrors, see [[representational-duplication]].
- Two or more classes or functions with the same structure and mostly identical lines, differing in small local edits, often tagged per client or variant in names or comments (`...Papa`, `v2.01papa`); confirmed when a fix sits in one copy and the same defect remains in its twin. This wording is this wiki's, after Weisfeld (pp. 170-171).
- The same check in several modules, where the function falls outside any module's clear responsibility (p. 68). The book's anecdote is over ten thousand US government programs with different versions of social security number validation.

This wiki assigns the neighbouring cases as follows. This page owns a restated fact. Conversion from the smallest unit repeated at each formatting site is [[exact-representation-for-money]]; other knowledge written twice is [[dry]]. Functions whose bodies differ only in literal values are [[parameterize-function]]; functions that share opening and closing lines and differ in the algorithm between them are [[similar-functions-varying-middle]]. Method bodies repeated on sibling classes that share no superclass of the project's own are [[mixins-share-functionality]]. Overrides of one method on subclasses of a common superclass of the project's own, identical but for one step or wholly identical, are [[shared-behavior-in-superclass-varying-step-polymorphic]]. One condition naming concrete parties or limits at two sites is [[business-rules-are-metadata]]. One call path repeating a check and its reaction is [[caller-owns-the-precondition]], and the last sign above covers unrelated modules. The same literal declared as a constant in two unrelated classes, where the temptation is a shared public constant, is [[no-public-constants]]. A representation decision visible at use sites whose code differs, such as a primitive id type declared and compared across modules, is [[hide-secrets-behind-one-access-point]]; the same production step repeated stays here. A non-trivial subexpression repeated within one statement or routine is [[name-repeated-subexpression]]; a repeated block of statements is [[dry]]. Two call sequences of the same shape that differ only in which third-party product's API they call are [[hide-third-party-apis]], and [[dry]] defers to it. The same access wrapper repeated around calls to one service (a fallback, a cache check, a permission check) is [[proxy]]. A repeated sequence of one object's own public calls at several call sites is [[abstract-intent-revealing-interface]], whose repair moves it into that class; any other fragment repeated verbatim at several call sites is [[dry]]. A fragment repeated verbatim at several call sites is [[dry]], which owns it; a fragment that is not repeated is [[extract-routine-to-name-a-step]]. An expression computing an index into a lookup table is [[isolate-table-key-computation]]'s, wherever it repeats; [[dry]] and [[name-repeated-subexpression]] defer to it. Identical statements at the same end of every branch of one conditional are [[identical-code-in-every-branch]]; a copy-pasted branch or block that differs from another by one operand is [[dry]]. The same statements adjacent to every call of one function are [[move-statements-across-call-boundary]]; the same fact restated elsewhere, not tied to a call, is [[dry]].

Two copies already standing in code are [[dry]]; a copy a diff adds as the route for a feature or fix, beside the function it copies, is [[preparatory-refactoring]].

## When not to apply

- Identical code that encodes different knowledge is a coincidence, not a violation. See [[coincidental-duplication]].
- A defect found in one copy need not exist in the other, and porting the fix may be the greater danger: «исправление кода, как в системе для Papa’s Pizza, окажется более опасным для Dad’s Donuts, чем первоначальный дефект» (Weisfeld, p. 171). Before porting a fix or merging copies, check that the other copy has the problem. Where copies are already forked and in production, merging is a cost decision, not a finding on sight (p. 171).
- A deliberate cache for performance is a permitted violation when kept local. See [[stored-derived-data]].
- Duplication at a boundary with an external system is unavoidable and can only be reduced. See [[representational-duplication]].
- The book's separator example shows how far the sign reaches. The book says the violation remains, and also that the match is inexact: the separator is one character short, which it gives as the client's intent, different from the amount format (p. 64). This wiki reads that as: where a requirement sets two tied values apart, deriving one from the other would lose that difference, so the tie is reported and the values are not merged.

## Repair

- Extract the repeated decision into one function (p. 62).
- Prefer reusing an existing function over introducing a constant for one of its details. The book removes the repeated width by routing all amounts through the formatting function, not by naming the width (p. 63).
- For copied classes, move the shared part into one place (a common base, a composed class or a function), turn each varying part into an abstract method or parameter, and point every user at it (Weisfeld, pp. 171-172; the steps are this wiki's). See [[contract-via-abstract-methods]].
- Fowler grades the repair by where the copies live (PDF pp. 86-87). In one class, Extract Function and call it from both places. For similar but not identical fragments, Slide Statements to bring the similar lines together, then extract. In sibling subclasses, Pull Up Method into the parent, which avoids calling one sibling from another; that shape is owned by [[shared-behavior-in-superclass-varying-step-polymorphic]].
- Keep splitting until each kind of change has one home: amount format in one function, label format in another (p. 64).

Where the finding sits beside a change on other lines, [[refactor-early-and-often]] rules on when to act.

## Before and after

Before:

```
function print_receipt(order)
    print "Net:" + pad_left(to_fixed(order.net, 2), 10)
    if order.discount < 0
        print "Discount:" + pad_left(to_fixed(-order.discount, 2), 10) + "-"
    else
        print "Discount:" + pad_left(to_fixed(order.discount, 2), 10) + " "
    if order.total < 0
        print "Total:" + pad_left(to_fixed(-order.total, 2), 10) + "-"
    else
        print "Total:" + pad_left(to_fixed(order.total, 2), 10) + " "
```

After:

```
function format_money(value)
    text = pad_left(to_fixed(abs(value), 2), 10)
    if value < 0
        return text + "-"
    return text + " "

function receipt_line(label, value)
    print pad_right(label + ":", 10) + format_money(value)

function print_receipt(order)
    receipt_line("Net", order.net)
    receipt_line("Discount", order.discount)
    receipt_line("Total", order.total)
```

A change to the money format now touches `format_money`, and a change to label layout touches `receipt_line`.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 8, pp. 169-172: copy-paste reuse, drifting copies and forked code bases, the defect-tracking side box, factoring into `Shop`. Weisfeld frames it at the level of whole applications for different clients; narrowing it to classes and functions inside a module is this wiki's reading, as are the copied-classes sign, the check-before-porting limit as worded and the repair steps. The quotations were checked against `raw/`.

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 9, pp. 60-64 and 68, via [[pragmatic-programmer]]. The book's team-level remedies for duplication between developers are left out as process advice. This wiki's own: the list form of the signs, the requirement that a tie be confirmed, the exclusion of trivial literals, the split of literals with [[named-constants-over-literals]], the assignment of neighbouring cases, the reading of the separator example, and the pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Duplicated Code", PDF pp. 86-87: the rule as a smell, the two costs, and the repairs graded by where the copies live. This wiki keeps [[coincidental-duplication]] as the limit on Fowler's rule, which states none.
