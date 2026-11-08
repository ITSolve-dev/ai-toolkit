---
title: Logic testable without the UI
category: structure
summary: "A test of a calculation or decision has to open a form and simulate clicks, an event handler computes and branches while reading widget fields directly, one function both computes a business result and builds its output, domain code calls a dialog to report to the user, or other code reaches the logic through a hidden form or a parallel copy of it."
tags: [rule, coupling, separation, testability]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

When reaching a calculation requires building a screen, the calculation and the screen are one unit. Difficulty in testing here reports a structural fault, not a testing problem. See [[test-is-first-client]].

## Rule

The book raises this only as a challenge: «Если так трудно протестировать логику приложения независимо от GUI, то что это говорит о самом GUI и связывании?» (p. 338). This wiki states that question as a rule: application logic should be testable without the user interface, and when it is not, the two are coupled and the repair belongs in the code, not in the test.

*Code Complete* states the rule outright, as an architectural requirement: the architecture should be modular, so that the user interface can be changed without touching the business rules or the modules that produce output (p. 44). McConnell's test is that a group of interactive-interface classes could be replaced fairly easily by a group of command-line classes, and he values this partly because a command-line interface is convenient for testing at the level of units or subsystems (p. 44). This page takes that architecture as a setting and applies it inside the code. Where storage access belongs, and which modules may import which, is the project's architecture; this page reports logic and presentation held in one unit, not a layer boundary.

In chapter 4 McConnell shows what happens when the tool decides instead: a Visual Basic environment pushed code into the form files, and other code that needed a form's validation either loaded the form, kept it hidden and called its methods, or copied the code elsewhere and maintained it in parallel (pp. 65-66). His convention: a form only moves data between the screen and storage, all other logic lives in an associated non-UI class, and the form's one public method, `IsFormCompleted()`, reports whether it saved its data (p. 66). See [[program-into-the-language]] for the distinction this example illustrates.

Fowler's *Refactoring* reaches the same shape from a third end, the second output format. His `statement` computed charges and totals inline while building the text; to add an HTML version without copying the calculations, he wanted "the same calculation functions to be used by the text and HTML versions of the statement" and divided the logic into a part that calculates the data and a part that renders it (2nd ed., ch. 1, PDF p. 32). The procedure is [[split-phase]]. He adds that once the phases are split, the calculations can be tested through the intermediate data structure, apart from the formatting (PDF pp. 43-44).

This wiki notes that the books reach one shape from different ends: *The Pragmatic Programmer* from the test that is hard to write, McConnell from the interface that should be swappable.

## Sign in code

- A test of a calculation or a decision has to construct a window or form, or simulate a click, to reach it.
- An event handler computes or branches on business conditions instead of passing values on.
- A function holding logic reads widget fields directly.
- One function both computes a business result and builds presentation output, such as markup concatenated beside data access.
- A diff that changes only an output format touches functions that hold business decisions.
- A second output format (HTML beside text, a report beside a screen) whose function repeats the calls to the calculation helpers, or copies them, instead of rendering from data computed once. This sign is this wiki's wording of Fowler's case (PDF p. 32).
- Domain code calls a presentation routine or dialog in the middle of a computation, or to report a failure (`showErrorDialog(...)` inside a business rule), instead of returning a result or raising a failure.
- Other code reaches the logic only by creating or loading a UI object, such as a hidden form kept alive to call its validation method, or the same validation is copied out of the UI unit and maintained in parallel. McConnell names both workarounds (p. 66).

This wiki assigns the neighbouring cases as follows. This page owns logic and presentation held in one unit, and a second consumer forced through or around that unit. Domain code that calls a presentation routine or dialog in the middle of a computation, or to report a failure, is [[logic-testable-without-ui]]; a reusable module that reaches a UI handle it was not given is [[do-not-rely-on-unguaranteed-context]]. Where the class reads widget fields or builds presentation output (a UI event handler, code-behind, a template), [[logic-testable-without-ui]] owns the sign; where it receives requests or system operations and holds no widgets (a web or command handler, a use-case controller), [[controller]] owns it. A cycle of calls between two classes is [[circular-dependency]]. A test's setup that is large for any other reason is [[test-is-first-client]]. Units of one kind exposing different ad-hoc public methods is [[coding-conventions]]. An import against a layer order the project declares is a conflict with the given architecture, which this wiki does not prescribe. Domain code that calls a dialog or reads widgets in the middle of a computation is [[logic-testable-without-ui]]; a model that pushes a finished state change into a concrete reacting object it holds is [[observer-publisher-knows-only-interface]].

One function both computes a business result and builds its output is [[logic-testable-without-ui]], which owns the sign; [[split-phase]] is the procedure that separates them. A routine whose later part reads a different set of inputs and only a few results of its earlier part has sequential cohesion, which [[routine-cohesion]] owns; [[split-phase]] is the procedure that separates its parts.

## When not to apply

- Tests of the interface itself: layout, event wiring, what a screen shows. Those need the UI.
- Presentation logic: formatting, layout, enabling a control, converting input text to a typed value. It belongs in the UI.
- A check the UI repeats for quick feedback, while the authoritative check also lives in the domain code.
- A thin handler with no decision in it. There is nothing to extract.
- One output, no second consumer of the computed values, and a function small enough to read at once. Fowler's motive for the split was the HTML version, and the split grew his code from 44 to 70 lines (PDF p. 42); this limit is this wiki's reading, the source does not state it.
- A throwaway screen whose logic is one line. Extraction adds a seam and a name that nothing pays for. With no second consumer, the hidden-form and copied-validation signs cannot appear.
- A domain routine that calls the UI through an interface it defines itself, such as a callback or a notifier passed in, does not depend on the presentation; the call is not this page's sign.

The cost of following the rule is one more seam and one more name for each extraction.

## Repair

1. Extract the logic into a function or object that takes plain values and returns plain values.
2. Leave the handler to read fields, call the logic and write the result.
3. Test the logic directly, and keep at most a small number of tests through the UI for the wiring.
4. Where domain code calls the UI to report, have it return a result or raise a failure, and let the UI code decide what to show.
5. Where other code borrows a form, point it at the extracted non-UI routine and delete the hidden form and any parallel copy (p. 66).

## Before and after

Before:

```
on_click(submit_button):
    price = to_number(price_field.text)
    if discount_box.checked:
        price = price * 0.9
    total_label.text = format(price)

test "discount":
    form = open_form()
    form.price_field.text = "100"
    form.discount_box.check()
    form.submit_button.click()
    assert form.total_label.text == "90.00"
```

After:

```
function final_price(price, discounted):
    if discounted:
        return price * 0.9
    return price

on_click(submit_button):
    price = to_number(price_field.text)
    total_label.text = format(final_price(price, discount_box.checked))

test "discount":
    assert final_price(100, true) == 90
```

Domain code reporting through the UI, before:

```
function check(invoice)
    if invoice.total < 0
        showErrorDialog("Negative total")
```

After:

```
function check(invoice)
    if invoice.total < 0
        return failure("negative_total")
    return ok()

// in the screen's handler
result = check(invoice)
if result.failed
    showErrorDialog(message_for(result))
```

A second consumer borrowing a form, before:

```
form OrderForm
    on_save():
        if quantity <= 0 or customer.blocked: show_error(...)
        db.insert("orders", {...})
    validate_order(draft): ...

// elsewhere, to reuse the rule:
f = load OrderForm hidden
ok = f.validate_order(draft)
```

After:

```
form OrderForm
    on_save():
        draft = read_fields()
        result = order_rules.validate(draft)
        if result.failed: show_errors(result); return
        order_store.save(draft)

module order_rules
    validate(draft) ...

// elsewhere:
ok = order_rules.validate(draft)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]], p. 338, a challenge at the end of Topic 51.

This wiki's own, as far as *The Pragmatic Programmer* goes: everything except the quoted question. The book poses the question and draws no rule, sign, limit or repair from it.

[[code-complete]], ch. 3, section 3.5 («Пользовательский интерфейс»), Russian edition, p. 44: modularity so the UI can change without touching business rules, the swap test between interactive and command-line classes, and the testing reason. Ch. 4, section 4.3, pp. 65-66: the Visual Basic forms, the hidden-form and parallel-code workarounds, the form convention and `IsFormCompleted()`. [[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Splitting the Phases of Calculation and Formatting", PDF pp. 32, 42-44: the calculation-against-rendering split, shared calculations for two formats, the line counts and the testing benefit. This wiki's own for that part: the second-format sign as worded and the one-output limit.

This wiki's own: the domain-calls-UI sign and its callback limit (carried over from the former layering page, which rested on *The Pragmatic Programmer*, Topic 10, pp. 72-73), the generalisation of McConnell's Visual Basic case to UI units of any kind, the limits on presentation logic and repeated feedback checks, repair steps 4-5, the assignment of neighbouring cases, and all pseudocode.
