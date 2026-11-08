---
title: Avoid falling through case arms
category: complexity
summary: "In a C-style switch, an arm with statements but no break/return/throw that runs on into the next label with no comment or marker, or a block or loop opened under one case label and closed under another: end every arm; where fall-through is intended, mark it and say why."
tags: [rule, conditionals, switch, fall-through, control-flow]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

In languages with a C-style `switch`, an arm that does not end explicitly runs on into the next one. McConnell treats this as a source of errors under modification and asks for it to be avoided, and, where it is meant, to be marked unmistakably (pp. 356-357).

## Rule

- Avoid code that falls through the end of a case. The book's worst example opens an `if` in case `'A'` and closes it inside case `'B'`, so the control structures overlap. Nested control structures are hard to understand; overlapping ones are nearly impossible, and changing case `'A'` or `'B'` would be «посложнее хирургической операции на головном мозге» (p. 356), likely ending in a rewrite that could have been done from the start (p. 356).
- If you deliberately write code that runs through several cases in a row, comment the place where it happens clearly and explain why it has to be written that way. The book's example prints full, summary or number-only error documentation, each level falling through to the next, with a comment at each fall-through point (p. 357).
- Even so, the book says such code invites errors when it is modified and should usually be avoided (p. 357). The checklist asks whether each case in C, C++ or Java ends with an exit (p. 358).

## Sign in code

- A `case` arm whose last statement is not `break`, `return`, `throw`, `continue` or a call that never returns, followed by another label, with no comment or marker at the fall-through point.
- A block or loop opened under one `case` label and closed under another.

This is a rule of C-family `switch` semantics, as the book states it (p. 356). In a language whose `switch` or `match` ends each arm on its own, or forbids implicit fall-through, there is nothing to apply.

## When not to apply

- The book's own: deliberate fall-through, clearly commented with its reason (p. 357), though the book still advises avoiding it.
- This wiki's own: several labels stacked on one shared body with no statements between them (`case A: case B: body; break;`) is not the shape the book warns about. Nothing runs before the shared body, so a change to one label cannot alter the other.
- This wiki's own: where the language offers an explicit fall-through marker (an attribute or keyword), use it instead of a comment; the compiler then checks it. Where the project's compiler or linter already rejects unmarked fall-through, the tool owns the finding and this page adds only the overlapping-block case.

## Repair

1. End every arm explicitly.
2. If two arms share work, move the shared work into a routine and call it from both, instead of falling through.
3. If fall-through is kept on purpose, mark each point with a comment or the language's marker, saying what runs next and why.
4. Never let a block span two labels; restructure so each arm is self-contained.

## Before and after

```
switch level:
    case FULL:
        showDetails(err)
    case SUMMARY:
        showSummary(err)
    case NUMBER_ONLY:
        showNumber(err)
        break
    default:
        internalError("unexpected documentation level")
```

```
switch level:
    case FULL:        showFull(err);    break
    case SUMMARY:     showSummary(err); break
    case NUMBER_ONLY: showNumber(err);  break
    default:          internalError("unexpected documentation level")

showFull(err):
    showDetails(err)
    showSummary(err)

showSummary(err):
    printSummary(err)
    showNumber(err)
```

The book's own alternative keeps the fall-through and marks each point with a comment (p. 357). That is acceptable; the version above is this wiki's preferred repair.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.2, pp. 356-357; checklist, p. 358. The stacked-labels limit, the explicit-marker and tooling limit, the call-a-routine repair and the pseudocode are this wiki's own; the pseudocode is modelled on the book's documentation-level example.
