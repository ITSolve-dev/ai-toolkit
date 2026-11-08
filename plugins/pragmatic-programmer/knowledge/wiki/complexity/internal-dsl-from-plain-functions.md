---
title: Build an internal DSL from plain functions
category: complexity
summary: "Metaprogramming, macros or dynamic dispatch hooks whose only product is a nicer call surface, where every generated name could be written as an ordinary function."
tags: [rule, dsl, metaprogramming, abstraction-cost]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

## Rule

When it does not matter that the host language shows through («просачивание синтаксиса базового языка», p. 98), the source offers a shortcut: «вместо усердного метапрограммирования достаточно написать функции, выполняющие все необходимые действия» (p. 98). Its evidence is that the words of a well-known test notation, such as `describe`, `it` and `expect`, are just methods of the host language (p. 98). The book also says this library and a framework's router rest on fairly elaborate code with metaprogramming and macros (p. 96), and that object passing stays hidden inside the notation (p. 98). This wiki therefore reads the example as showing the call surface, not an absence of machinery. An exercise repeats the point: «Постарайтесь не делать ничего заумного», and write one function per command (p. 99).

This wiki reads the reasoning as follows: metaprogramming is cost spent on the notation itself, whereas plain functions give nearly the same reading at the cost of a few visible host-language marks.

## Sign in code

All of these together:

- generation of names at runtime or compile time: method-missing hooks, macros, reflection, attribute generators;
- the generated names form a fixed set known when the code is written;
- the generating machinery has no job besides producing that call surface.

## When not to apply

- The host syntax showing through does matter, which is the source's own condition. This wiki adds an example: the authors of the text are not programmers.
- The set of names is not fixed, because it comes from a schema or other data at run time. This wiki adds that functions cannot be written by hand for such a set.
- This wiki adds that the mechanism may be the established way of the project's tooling; how the rule applies in a given language is decided at work time.

## Repair

The source gives the direction; the steps are this wiki's own.

1. List the words of the notation.
2. Write one ordinary function or method for each word.
3. Pass the shared context as an argument or a small object, and delete the generating machinery.
4. Accept the host language's punctuation that now shows through.

## Before and after

```
// before: names synthesised to read nicely
class Turtle:
    on_missing_method(name, args):
        if name matches "go_(north|south|east|west)":
            self.move(direction_from(name), args[0])
        else if name in ["pen_up", "pen_down"]:
            self.pen = name
```

```
// after: the same words, as functions
function go_north(turtle, cm): turtle.move(NORTH, cm)
function go_south(turtle, cm): turtle.move(SOUTH, cm)
function go_east(turtle, cm): turtle.move(EAST, cm)
function go_west(turtle, cm): turtle.move(WEST, cm)
function pen_up(turtle): turtle.pen = UP
function pen_down(turtle): turtle.pen = DOWN
```

## Source

[[pragmatic-programmer]], Topic 14, pp. 96, 98-99: the rule, its condition, the test notation evidence and the exercise. The reading of that evidence, the reasoning sentence, the sign, the limits marked as added, the repair steps and the pseudocode are this wiki's own. The pseudocode borrows the idea of the source's turtle-graphics exercise, not its text. See [[internal-vs-external-dsl]] for when an internal language is the right form.
