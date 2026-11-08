---
title: Mechanical code transformation keeps bad logic
category: change
summary: "Concept: output of a restructuring tool, a language translator or a code generator kept and hand-maintained as if finished, though its logic is as tangled as the original's (flag variables standing in for removed jumps, meaningless names, long uniform blocks); such output is a starting point for manual refactoring, unless it is regenerated and never edited."
tags: [concept, restructuring, code-generation, legacy-code, translation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Automated transformation changes the *form* of code, not the *thought* in it. McConnell makes this point about three kinds of tools: restructurers, language translators and code generators (pp. 699-702).

## What the source says

- **Restructurers** turn goto-laden spaghetti into structured code, and Capers Jones reports that they can raise maintenance productivity by 25-30% (p. 699). But the tool has to make many assumptions, and if the original logic was terrible, the converted version keeps it: «если логика оригинала была ужасной, она останется такой и в сконвертированной версии» (p. 699).
- **Translators** move a large volume of code to another language, but a translator simply carries bad code into the new language (pp. 699-700).
- **Generators** rarely produce code as good as a programmer's, though many applications do not need hand-crafted code at all (p. 702). Their most common drawback is that the code they produce is usually practically unreadable, and whoever maintains it may wish it had been written by hand from the start (p. 702).

## How the source uses the tools anyway

For restructuring it gives two workable modes (p. 699): when converting by hand, let the tool take the simple cases and handle the complex sections yourself; or run the code through the restructurer and treat the output as a **starting point** for manual conversion, not as the finished product.

For generators it names the setting where poor output does not matter: prototypes and design experiments (p. 702). A generator can produce in a few hours a prototype that shows the key aspects of a user interface, or try several design approaches, where coding by hand would take weeks: «Если вы просто экспериментируете, почему бы не делать это наиболее дешевым способом?» (p. 702). Keeping such code out of production is [[throwaway-prototype]].

```
// before: restructured mechanically, goto removed, logic unchanged
function find_first_overdue(items):
    i = 0
    found = -1
    done = false
    while not done:
        if i >= length(items):
            done = true
        else:
            if items[i].overdue:
                found = i
                done = true
            else:
                i = i + 1
    return found

// after: the same output used as a starting point, the loop re-derived by hand
function find_first_overdue(items):
    for i in 0 .. length(items) - 1:
        if items[i].overdue: return i
    return -1
```

## Reading this for code at hand

This wiki draws the following conclusions; the source does not state them as signs. Flag-variable loops standing in for removed jumps, numbered or meaningless names, and long uniform blocks with no domain vocabulary often mark tool output. Such code is not repaired by passing it through another tool: once people are to maintain it, it calls for the ordinary manual work of [[refactoring]], in small steps ([[refactor-in-small-tested-steps]]). A done flag threaded through a loop, wherever it came from, is the shape [[break-and-continue]] owns.

Output that is regenerated from a source of truth and never edited by hand is a different case, also in this wiki's reading. Its readability matters less, and edits belong in the generator's input, not in the generated file.

How far a tool-made refactoring can be trusted without running tests is [[automated-refactoring]]; this page owns tool output that people keep and maintain by hand.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 30.2, pp. 699-702 ([[code-complete]]): restructurers, translators, code generators and the prototyping use. Quotations were transcribed from the extracted text with line-break hyphens joined. This wiki's own: the pseudocode pair, the signs of tool output, the routing to neighbouring pages, and the exception for regenerated code.
