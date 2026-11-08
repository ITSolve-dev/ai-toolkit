---
title: Rewrite tricky code instead of commenting it
category: documentation
summary: "A comment warns that the code below is tricky, fragile or must not be touched ('IMPORTANT', 'do not change', 'clever'), explains a trick a plain construct would avoid, or carries the only statement of a lifetime dependency between two objects."
tags: [rule, comments, complexity, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Rewriting tricky code instead of commenting it** is McConnell's rule that a comment cannot rescue code that is hard to understand. He calls the common belief that tricky or unstable fragments are exactly what comments are for one of the most widespread and dangerous misconceptions, and a bad idea (p. 783).

## Rule

The book's example is a warning comment from a real project. A constructor takes a reference to one object, and the comment says in capitals that this object must not be destroyed before another one, or the program dies a martyr's death (p. 783). The book's reply: «Комментарии не могут спасти сложный код» (p. 783). It follows with Kernighan and Plauger: «не документируйте плохой код — перепишите его» (p. 783).

Its evidence is a study by Lind and Vairavan (1989). The fragments with the most comments tended to hold the most defects and to take the largest share of development effort, which the researchers explained by programmers commenting difficult code generously (p. 783). The book's test for trickiness is the author's own doubt: if you ask yourself whether something is tricky, it is. A trick that seems simple to its author looks convoluted to someone who has not met it, and a simpler solution can always be found. The order is to make the code good enough that it needs no comments, and then to comment it to make it better (p. 783).

## Sign in code

- A comment over code warns rather than informs: `IMPORTANT`, `DO NOT`, `careful`, `magic`, `do not touch`, or a forecast of a crash if something is changed.
- A comment explains how a construct works where a plain construct would do the same job: an XOR swap, a bit trick standing in for arithmetic, a variable reused with two meanings.
- A dependency of lifetime or ownership between two objects is stated only in a comment, and nothing in the types or the construction enforces it.

This wiki sets the boundary against [[comment-why-not-how]] by one question: could the code be rewritten so that the comment is no longer needed? If it could, this page owns the comment and the repair is to rewrite. If it could not, because the trick is forced from outside, such as a measured speed-up the compiler does not give or a workaround for a library defect, that page owns it and the comment stays. An order of destruction or ownership between two objects stated only in a comment is [[rewrite-tricky-code]]; an order of calls or of reading a result is [[temporal-coupling]]. A comment admitting a defect (`HACK`, `FIXME`) is [[broken-windows]]. A method patched with special-case branches for particular inputs belongs to [[rewrite-a-method-you-do-not-understand]].

## When not to apply

- Maintenance without the freedom to rewrite. The book limits the rule to code being written for the first time: «Если вы сопровождаете программу и не имеете возможности переписывать плохой код, комментирование хитрых фрагментов — хороший подход» (p. 784).
- A non-obvious technique kept on purpose for a stated, measured reason. The book itself asks for such a comment, under documenting surprises (pp. 780-781). The comment names the plain alternative and the gain; see [[comment-why-not-how]].
- An order of calls or of reading a result, which [[temporal-coupling]] owns.

## Repair

1. Name what the trick achieves.
2. Replace the trick with the plain construct that achieves it, or move it behind a function whose name states the effect.
3. Where the warning guards a dependency between objects, make the dependency structural, for example by having the dependent object own or receive the other. This step is this wiki's own; the book says only to rewrite.
4. Delete the warning. Keep a comment only for what the rewritten code still cannot say.

The rewrite costs time on code that works, and it can introduce a defect. That is why the book exempts code under maintenance that cannot be rewritten.

## Before and after

```
// before
// TRICKY: swaps a and b without a temporary.
// Do not reorder these three lines!
a = a xor b
b = a xor b
a = a xor b
```

```
// after
temp = a
a = b
b = temp
```

## Source

[[code-complete]], ch. 32.5, pp. 783-784. The book's parts: the rule, the warning-comment example, the Kernighan and Plauger quotation, the Lind and Vairavan study, the self-doubt test, and the limit for maintained code. This wiki's own parts: the signs, the boundaries against [[comment-why-not-how]], [[temporal-coupling]], [[broken-windows]] and [[rewrite-a-method-you-do-not-understand]], step 3 of the repair, and the pseudocode. The quotations were transcribed from the extracted text and should be checked against the page image.
