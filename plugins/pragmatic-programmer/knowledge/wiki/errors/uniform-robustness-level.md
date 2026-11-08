---
title: Guard peer routines to one robustness level
category: errors
summary: "Peer routines or classes in one module calling the same dependency are guarded very unevenly (one wraps the call in retries, timeouts and a fallback, its neighbour calls it bare), with no requirement or comment behind the difference."
tags: [rule, robustness, defensive-code, gold-plating, consistency]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls *robustness* a system's ability to keep working after an error is detected, and notes that architects often specify a more robust system than the requirements ask for (p. 48). One reason is that a system made of many parts, each meeting the minimum, can end up less robust than needed as a whole: «В мире ПО цепь не так крепка, как слабейшее звено; она так слаба, как все слабые звенья, вместе взятые» (p. 48).

The book places that decision in the architecture specification: it should say whether programmers may build extra robustness into their parts or should build the simplest thing that works (p. 48). Many programmers add robustness automatically, out of professional pride; stating the expectation avoids some classes being exceptionally robust while others only meet the requirements (p. 48). Which level is chosen is architecture, out of this wiki's scope; this page takes it as given from the project or the brief.

## Rule

Where the project or its architecture sets a robustness level, peer code inside a module meets it uniformly, rather than each author's taste deciding how much guarding a routine gets (p. 48).

## Sign in code

This wiki reads the following as the sign. Two routines or classes in one module that call the same dependency differ sharply in guarding, with nothing in the requirements or the code to explain why:

- one wraps the call in retries, timeouts and a fallback;
- the other calls the same dependency bare.

This wiki assigns the neighbouring cases as follows. Uneven validation of the same input is [[consistent-error-handling-strategy]]; uneven retry, timeout and fallback around the same dependency is [[uniform-robustness-level]]. A mismatch in how peers *signal* a failure (codes against exceptions) is [[consistent-error-handling-strategy]]. Whether a given check belongs at all is decided by [[distrust-external-input]] and [[caller-owns-the-precondition]]. A network call with no timeout in a reusable module, without a guarded peer to compare, is [[do-not-rely-on-unguaranteed-context]].

## When not to apply

This wiki's own limits:

- **Different exposure.** Code at a trust boundary or facing hostile input ([[distrust-external-input]]) is meant to be more guarded than code behind it.
- **No level is set.** Where neither the project nor the brief states a level, there is nothing to be uniform with; report the unevenness as a question, not a finding.
- **Different stated reliability.** The requirements set different reliability for different functions.
- **A comment that states the reason.** Unevenness the code explains is not this sign.

## Repair

This wiki's own: apply the project's level to the peer group. Either raise the weak routine to it or strip the extra machinery from the gold-plated one. Better, move the shared guarding (retry policy, timeouts, fallback) into one place all peers use, so the level is set once.

## Before and after

```
// before: two clients of the same rate service
function priceInEur(amount):
    for attempt in 1..5:
        try: return amount * rates.get("EUR", timeout=2s)
        catch Timeout: sleep(backoff(attempt))
    return amount * cachedRate("EUR")

function priceInUsd(amount):
    return amount * rates.get("USD")         // no timeout, no fallback
```

```
// after: one agreed policy, applied in one place
function rate(currency):
    return withRetry(policy=RATE_POLICY,
                     call=() -> rates.get(currency, timeout=2s),
                     fallback=() -> cachedRate(currency))

function priceInEur(amount): return amount * rate("EUR")
function priceInUsd(amount): return amount * rate("USD")
```

In the "after", the two peers can no longer differ in guarding. Whether the cached fallback is acceptable at all is a choice of availability over correctness; see [[fault-tolerance-techniques]].

## Source

[[code-complete]], ch. 3, section 3.5 («Избыточная функциональность»), Russian edition, p. 48: the definition of robustness, the chain metaphor, the explicit decision on extra robustness, and professional pride as the cause of unevenness. The narrowing of the book's architecture-level decision to peer code inside a module, the rule as worded, the sign, the assignment of neighbouring cases, the limits, the repair (moving shared guarding into one place included) and the pseudocode are this wiki's own.
