---
title: The caller owns the precondition
category: errors
summary: "A routine clamps, coerces or defaults an out-of-domain argument at entry, or holds the caller's decision about what to do with bad input."
tags: [rule, contracts, responsibility]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A precondition divides labour: the routine states its domain, and the code that calls it decides what to do about a value outside that domain.

## Rule

Express a routine's domain as a precondition and leave what happens to out-of-domain values to the caller. Stating the domain moves «бремя ответственности за правильность на вызывающий код» (p. 147). In the book's square-root example the console program may abort, warn and ask again, make the number positive, or attach an imaginary unit; whichever it picks is no concern of the square root (p. 147). Where a language has no built-in contracts, the called routine carries a preamble that checks the conditions (p. 147).

## Sign in code

- At entry, a routine overwrites an argument outside its domain: `abs(x)`, a clamp, a substituted default, while its stated job is something else. This page owns that shape. Where a bug-fix diff adds the clamp at the failing line and leaves the producer alone, [[fix-the-root-cause]] owns it. Where every form of the argument is inside the domain and only its shape varies, the shape belongs to [[strict-accept-narrow-promise]].
- A routine contains the user-facing reaction to bad input, such as a prompt or a message, next to its computation.
- One call path repeats the same validity check and the same reaction at each level. The book names this as the inefficiency of defensive programming (p. 144). This wiki does not count one handler at the boundary plus one assertion inside as this sign: see [[assertion-or-error-handling]]. The repair for such a path, one validating door and assertions behind it, is laid out on [[barricade]].

This wiki assigns two more neighbouring cases. An assertion on the argument followed in the same routine by a clamp of the same condition is decided on [[assert-then-handle-anyway]]; the condition that selects the page, in the words both pages use: whether the caller is held to the contract by shared code ownership and tests. A substitution where the data first enters the program, or made by the caller that holds the decision, is [[robustness-versus-correctness]], which decides whether substituting is acceptable at all. A clamp or default of an argument already checked upstream on the same path is [[barricade]]; one with no check upstream is [[caller-owns-the-precondition]].

## When not to apply

- A routine that receives data from outside the program. No caller there can be held to a contract, so validation is its job: see [[assertion-or-error-handling]].
- A routine whose stated purpose is normalising, such as a `clamp` or a parser. Repair is then its contract, not a violation of it.
- A public interface whose callers you cannot change. It keeps its checks, but they should fail loudly and never repair the value.

## Repair

Remove the compensation from the routine. State the domain and turn the old code into a failing check. Move the decision to the caller, which is the only place that knows whether to reject, ask again or fall back.

## Before and after

```
# before
function discounted(price, percent):
    if percent < 0: percent = 0
    if percent > 100: percent = 100
    return price * (1 - percent / 100)

function on_coupon_entered(text):
    show(discounted(cart.price, to_number(text)))
```

```
# after
function discounted(price, percent):
    # requires: 0 <= percent <= 100
    assert 0 <= percent and percent <= 100
    return price * (1 - percent / 100)

function on_coupon_entered(text):
    percent = to_number(text)
    if percent is invalid or percent < 0 or percent > 100:
        show_error("Enter a discount from 0 to 100")
        return
    show(discounted(cart.price, percent))
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: p. 147 for the rule, p. 144 for repeated checks, p. 142 for user input. The first two signs, the assignment against [[fix-the-root-cause]], the exclusion of one handler plus one assertion from the third, the split with [[barricade]] on a clamp behind an upstream check, the last two limits, the repair and the example are this wiki's own.
