---
title: Binding time
category: change
summary: "A value that can change only between runs (read from a file, registry or environment) re-read at each object creation, call or redraw instead of once at load: bound later than its source changes. A load-time key with one value everywhere is over-configuration; a bare literal is named-constants-over-literals."
tags: [decision-rule, binding-time, magic-number, named-constant, flexibility, configuration, trade-offs]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Binding time is the moment a variable and its value are bound together. *Code Complete* introduces it in the design chapter with the trade-off «Раннее связывание обычно упрощает код, но и снижает его гибкость.» (p. 104), and with a set of questions to ask of a design: what if these values were bound earlier, or later? what if this table were initialised here? what if this value were read from the user at run time? (p. 104). Section 10.6 gives the fuller treatment. It credits the term to Thimbleby (1988) and calls it an aspect of initialization that strongly affects maintainability and modifiability (p. 246). With the book's title-bar colour example, the binding points are (p. 247):

1. when the code is written: a magic number, `titleBar.color = 0xFF`;
2. at compile time: a named constant, `TITLE_BAR_COLOR`;
3. at load time: read from the registry or a properties file when the program starts;
4. at object creation: read each time a window is created;
5. on demand: read on each redraw.

The section restates the trade-off: «В целом чем раньше время связывания, тем ниже гибкость и ниже сложность кода.» (p. 247)

## Rule

The book's decision has two parts (pp. 246-247):

- **Between 1 and 2, almost always choose 2** (p. 246). A hard-coded literal is usually a poor choice, because when one `0xFF` changes, other `0xFF`s used for the same purpose can fall out of step with it (p. 246). A named constant reads better, changes in one place, and costs nothing at run time (p. 246). The flexibility of a named constant comes from good practice alone (p. 247).
- **From 3 onward, bind as late as the requirements need and no later.** Each later point adds code to support the flexibility, and with it complexity and the chance of errors. The book's conclusion: «опытный программист будет обеспечивать такой уровень гибкости, какой нужен для удовлетворения требований, но не более того.» (p. 247)

## Sign in code

A value that can change only between runs, because its source is a file, the registry or the environment, is read, parsed and validated again at each object creation, call or redraw (binding points 4 and 5) instead of once at load (point 3). The code binds it later than its source can change, and pays the reading code on every pass.

Whether a requirement asks for a value to change while the program runs is not in the code. Where the source can change at run time (a user setting edited in a dialog), ask before reporting.

This wiki assigns the neighbouring cases as follows. This page owns the choice of how late to bind a value, and the value bound later than its source changes. A configuration key read once at load that holds one value everywhere is [[over-configuration]]; the same value re-read at object creation or on each call or redraw is [[binding-time]]. A bare literal in source that encodes a decision, and a constant mixed with its own literal, is [[named-constants-over-literals]]. A host, port, credential or tax rate in source, or a branch on environment or customer name, is [[parameterize-with-external-configuration]]. A literal that grants access is [[keep-secrets-out-of-source]]. The same literal repeated because two pieces of knowledge merely happen to coincide is a question for [[coincidental-duplication]] and [[dry]]. A named constant whose name spells its value is [[constant-names-abstract-not-value]].

## When not to apply

The limits below are this wiki's own:

- A value that is a fact of the problem, such as seconds in a minute, stays a named constant even when someone proposes making it configurable. [[parameterize-with-external-configuration]] gives the same limit.
- A late binding the requirements ask for, such as user-adjustable colours, is the point of the code and not this sign. The book's own run-time example is of this kind (pp. 246-247).

## Repair

Move the read to the binding point the source needs: read the value once at load and pass or keep the result, and delete the per-creation or per-call reading code. If the value then also holds one value everywhere and nobody outside the code sets it, [[over-configuration]] turns it into a named constant. Keep the per-call read only where a requirement says the value must change while the program runs.

## Before and after

Before:

```
function draw(window):
    settings = read_file("ui.cfg")              // file edited only between runs
    window.border = parse_int(settings["border_width"])
    render(window)
```

After:

```
function start():
    settings = read_file("ui.cfg")
    ui_style = UiStyle(border = parse_int(settings["border_width"]))

function draw(window, ui_style):
    window.border = ui_style.border
    render(window)
```

## Source

McConnell, *Code Complete*, Russian edition, via [[code-complete]]: section 5.3, p. 104, for the first statement of the trade-off and the design questions; section 10.6, pp. 246-247, for the definition (after Thimbleby, 1988), the five binding points, the named constant preferred to the magic number, the trade-off between flexibility and complexity, and "as much flexibility as the requirements need, no more". The checklist on p. 251 repeats the balance. The book gives the five points, including reading on each window creation or redraw (p. 247), but names no sign. This wiki's own: the sign as worded (a value re-read later than its source changes), the assignment against the configuration and naming pages, the limits, the repair steps and the pseudocode.
