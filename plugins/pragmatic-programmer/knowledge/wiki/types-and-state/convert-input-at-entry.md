---
title: Convert input to its type at the moment of input
category: types-and-state
summary: "A raw input string such as \"yes\", \"red\" or \"42\" is stored or passed through several routines and compared as text far from where it was read, instead of being parsed into a boolean, enum or number on entry."
tags: [rule, validation, types, parsing]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Input usually arrives as a string or a number even when it means a boolean ("yes"/"no") or one value of an enumeration (red, green, blue). McConnell's rule is to give it that meaning at once: «Преобразуйте входные данные в надлежащую форму как можно раньше.» (p. 199)

## Rule

Convert input data to its proper type at the moment it is read. Keeping data of undetermined type for an unknown period complicates the program and raises the chance that someone breaks it by entering "Yes" as a colour (p. 199).

This wiki reads the rule as the type-level half of [[barricade]]: the door both checks a value and changes its representation, so that code inside can no longer receive the invalid form.

## Sign in code

- A routine several calls away from where the input is read compares a parameter against string literals (`if colour == "red"`, `if flag == "yes" or flag == "Y"`).
- The same textual normalisation (trim, lower-case, parse) appears in more than one routine for one input.
- A record or object holds a field as text that is parsed, or compared against literals, at each place it is read.

This wiki assigns the neighbouring cases as follows. One routine that opens by normalising several shapes of the same argument is [[strict-accept-narrow-promise]]; a raw input string carried past the point where it was read and compared there, instead of being parsed into a boolean, enum or number, is [[convert-input-at-entry]]. Input that crosses the door still as raw text is [[convert-input-at-entry]]; raw external values that reach internal routines unchecked, with no door at all, are [[barricade]]. Text encoding and string-type conversions scattered through core logic are [[one-internal-string-format]]. A value stored in a type that fits it only by chance (a phone number in an integer) is [[representation-that-fits-by-coincidence]]. A raw text value such as `"yes"` or `"42"` carried and compared as text is [[convert-input-at-entry]]; an identifier carried as a bare value and looked up repeatedly is [[ids-to-objects]].

## When not to apply

- Pass-through data the program never interprets, such as a free-text comment stored and shown back as entered.
- Text whose exact original form must be kept (an audit record of what the user typed). This wiki adds: keep the raw text beside the converted value rather than instead of it.
- Where the project's input layer (form binding, a schema or deserialization library) already converts on entry, the sign is only a raw string that bypasses it. This limit is this wiki's own.

## Repair

At the point of input, parse the value into the narrowest type that fits (boolean, enumeration, number with a unit, a domain value type) and reject what does not parse. Change the internal signatures to take that type, and delete the string comparisons and repeated normalisation downstream. [[wrap-values-between-transformations]] covers how the parse reports failure.

## Before and after

```
# before
function on_form(form):
    paint(form.get("colour"))

function paint(colour):
    if colour.lower() == "red": use(RGB(255, 0, 0))
    else if colour.lower() == "green": use(RGB(0, 255, 0))
    else: use(RGB(0, 0, 255))      # "Yes" is painted blue
```

```
# after
enum Colour { RED, GREEN, BLUE }

function on_form(form):
    colour = parse_colour(form.get("colour"))
    if colour is failure:
        return reject(form, "colour must be red, green or blue")
    paint(colour)

function paint(colour: Colour):
    use(rgb_of(colour))
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 199 for the rule and its reasoning. The reading as part of the barricade, the signs, the split with neighbouring pages, the limits, the repair and the example are this wiki's own.
