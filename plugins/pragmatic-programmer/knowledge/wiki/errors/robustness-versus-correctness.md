---
title: Robustness versus correctness
category: errors
summary: "A bad value is replaced by a neutral value, the last value, the nearest legal value or the next record in code whose wrong output is costly (a dose, an account, a tax figure); a guard swaps an illegal operand for one chosen only so the next operation succeeds (if hours == 0, hours = 1); or cosmetic code aborts the program on a glitch it could absorb."
tags: [decision-rule, error-handling, fail-fast, robustness, silent-failure]
paradigm: any
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Once a possible error is detected, code must react, and McConnell lists the reactions available: return a neutral value, substitute the next valid piece of data, return the same answer as last time, substitute the closest legal value, log a warning, return an error code, call a central error handler, display a message where the error occurs, handle it locally however suits, or shut down; several may be combined (p. 189). Which one is right depends on whether the program leans towards correctness or towards robustness (p. 192). [[fault-tolerance-techniques]] lists the related options for surviving a fault.

## Rule

Correctness means never returning an inaccurate result: no result is better than a wrong one. Robustness means always trying something that lets the program go on, even at the price of partly wrong results. The two are opposite ends of a scale (p. 192). Safety-critical applications often favour correctness, consumer applications favour robustness (p. 192).

The book's examples set the line:

- Neutral value: a game's drawing routine given a bad colour may use the background colour, but a routine drawing an X-ray of a cancer patient should rather stop than show a wrong image (pp. 189-190).
- Next valid data: skip a corrupt database record; wait 1/100 s for the next thermometer reading (p. 190).
- Same as last time: fine for a thermometer read 100 times a second, wrong for authorising ATM transactions: «ведь это будет номер счета предыдущего клиента!» (p. 190).
- Closest legal value: reasonable for calibrated instruments, such as clamping a 0-100 °C reading, or a speedometer showing 0 when reversing (p. 190).
- Log a warning: combinable with the substitutions; consider whether the log file may be public or must be protected (p. 190).
- Shutdown: right when software controlling radiation therapy receives a bad dose; restarting the machine beats risking a wrong dose (p. 191).
- Robustness in a text editor: a partly drawn last line that the next Page Up redraws does not justify quitting (p. 192).

This wiki reads the test as: what does a wrong value cost the person relying on this output, compared with no output? A substitution is acceptable only where the cost of a slightly wrong result is lower than the cost of stopping.

Weisfeld's *The Object-Oriented Thought Process* gives a shorter list of strategies, after Tyma et al. and Gilbert and McCarthy: ignore the problem, check for it and stop the program, check for it and try to fix it, or throw an exception, which he often prefers (p. 74). On the first: «Игнорирование проблем — плохая идея!» (p. 74). A quiet wrong answer is the worst outcome, because «вы, возможно, даже не будете знать, что получаете неверные результаты, а это может оказаться намного хуже аварийного завершения программы» (p. 75). Stopping cleanly at least closes files and tells the user something failed (p. 75). He ranks checking and trying to fix the problem as much better than checking and stopping, and says it works well in certain situations (p. 75). On self-repair, his own example guards a division with `if (a == 0) a = 1;` and warns that «присвоение значения 1 не обязательно поможет, поскольку результат может оказаться неверным» (p. 75); for input, «Оптимальное решение состоит в том, чтобы предложить пользователю заново ввести правильное входное значение» (p. 75). He also notes that exceptions can carry real overhead, which keeps structured checks in play where performance matters (p. 75). This wiki reads Weisfeld's ranking against McConnell's scale this way: a substitute that has meaning in the domain (the background colour, the nearest legal reading) is a robustness choice that the cost test decides; a substitute chosen only so the next operation does not fail, like his `a = 1`, makes the result wrong at either end of the scale, and the cost test never licenses it.

## Sign in code

- A substitution (zero, empty string, default, previous value, clamp, skip) on bad input in code whose output is a measurement, a payment, an identity, a dose, a legal or financial figure.
- A "same as last time" cache returned on failure where the previous value belongs to another user, request or account.
- A guard just before an operation that replaces an illegal operand with a value picked only so the operation succeeds (`if divisor == 0: divisor = 1`, an empty list given a placeholder element), and the result flows on as if it were real (Weisfeld's `a = 1`, p. 75), where the operand first enters the program.
- The reverse: an abort, an unrecoverable exception or a process exit triggered by a defect whose only effect is cosmetic or self-correcting.

This wiki assigns the neighbouring cases as follows. Where the state can only arise from a bug, [[crash-early]] and [[assertion-or-error-handling]] own the shape; this page decides the reaction to a possible error in data. A substitution inside a routine whose argument comes from an internal caller is [[caller-owns-the-precondition]]. A substitution where the data first enters the program, or made by the caller that holds the decision, is [[robustness-versus-correctness]], which decides whether substituting is acceptable at all. A default for a missing required field of a structured document from another system is [[validate-exchanged-data-against-a-declared-schema]]; a substitute for a present but invalid value is [[robustness-versus-correctness]]. A catch below an entry point that substitutes a value for an I/O or parse failure is [[recover-only-at-entry-points]], whose limit on specified degradation this page's test decides.

## When not to apply

- A state only a bug can produce: that is not a choice of reaction to bad data but an assertion. See [[assertion-or-error-handling]].
- The reaction is fixed project-wide by an error-handling strategy; the routine follows it and does not choose locally ([[consistent-error-handling-strategy]]).
- The substitute is correct in the domain, not just harmless to the arithmetic: a documented default for an omitted optional setting, a total of zero for an empty list. This wiki takes "correct" to mean that a caller who knew of the substitution would accept the result.
- A hot path where throwing costs too much (Weisfeld, p. 75): a structured check may replace the exception, but it still reports the failure to the caller rather than substituting.

## Repair

Take from the project's architecture or brief which end of the scale this code is on; the book places that choice there (p. 192, checklist p. 206). If none is stated, report that rather than choose. At the correctness end replace the substitution with a refusal: return a failure, reject the record or stop. At the robustness end keep the substitution but log it, and mark the substituted value in what the routine returns. Where the input comes from a person at the point of reading, ask for it again, Weisfeld's preferred option (p. 75). A substitute picked only to let the next operation succeed is removed at either end: refuse the input instead.

## Before and after

```
# before: the prescription enters the program here, from the ordering system
function dose_for(order_message):
    prescription = parse(order_message)
    dose = prescription.dose
    if dose is invalid or dose > MAX_DOSE:
        dose = last_dose          # "same as last time"
    return dose
```

```
# after
function dose_for(order_message):
    prescription = parse(order_message)
    dose = prescription.dose
    if dose is invalid or dose > MAX_DOSE:
        return failure("prescription dose out of range", prescription.id, dose)
    return success(dose)

# robustness end of the scale: a substitution is right here
function pixel_colour(requested):
    if requested is invalid:
        log_warning("invalid colour", requested)
        return BACKGROUND
    return requested
```

A substitute chosen only to make the operation succeed:

```
# the trip log enters the program here, from the user's form
function averageSpeed(form):
    distance = to_number(form.distance)
    hours = to_number(form.hours)
    if hours == 0:
        hours = 1              # avoid division by zero
    return distance / hours
```

```
function averageSpeed(form):
    distance = to_number(form.distance)
    hours = to_number(form.hours)
    if hours == 0:
        return failure("hours must be positive", hours)
    return success(distance / hours)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 189-191 for the list of reactions and their examples, p. 192 for robustness versus correctness, p. 206 for the checklist. The cost test, the signs, the split with neighbouring pages, the limits, the repair and the example are this wiki's own.

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 3, pp. 74-75: the four strategies, ignoring as a bad idea, wrong results worse than a crash, clean termination, the `a = 1` warning, asking again as the best option, the preference for exceptions and their overhead. The quotations were checked against `raw/`. His p. 77 handler assigns a fallback `count` inside a `catch` for a division the code makes by zero and continues, a shape [[crash-early]] owns. This wiki's own for that part: the split with [[validate-exchanged-data-against-a-declared-schema]], the reading of his ranking against McConnell's scale, the operand-swap sign as worded, the domain-correct-substitute and hot-path limits, and the `averageSpeed` pseudocode.
