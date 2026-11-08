---
title: Tracer code or prototype
category: change
summary: "A production path reads canned input or imports a spike folder: a prototype that shipped. Absent error checks or a single route only support that. A trivial routine behind a final interface is not one."
tags: [decision-rule, prototype, throwaway-code, incremental]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

[[tracer-code]] and a prototype both start as a small, incomplete piece of code, so one is easily taken for the other. This page decides which to write, and how to tell which one is in front of the reader.

## Rule

The two look alike and differ in fate. «Прототипирование приводит к генерации одноразового кода» (p. 88); tracer code is «скудный, но завершенный» (p. 88) and forms the skeleton of the final system. A prototype is a cheap experiment aimed at a few questions, and the source's case for it rests on one sentence: «Его ценность состоит не в производимом коде, а в извлекаемых уроках» (p. 90). The tip is «Создавайте прототипы для обучения» (p. 90). Decide by this test:

- The question is about specific properties of the final system, and details can be ignored: write a prototype, then throw it away (pp. 87-88, 90). Candidates are whatever carries risk, is untried, is critical to the final system, or is unproven or doubtful (p. 90).
- The question is how the whole application hangs together, and the code is meant to remain: write [[tracer-code]] (p. 88).
- Details cannot be ignored in your setting: the source says to ask whether a prototype is warranted at all; tracer code may suit better (p. 90).
- The purpose of prototype code is likely to be misunderstood in your environment: choose tracer code, and you end with a solid framework (p. 92).

Before any prototype in code, the source says to make sure everyone concerned knows the code is disposable (p. 92). The reasoning is that a prototype's apparent completeness misleads, and sponsors may insist on deploying it (p. 92). Prototype code is, in the source's words, «данный код одноразовый, незавершенный и непригодный для завершения» (p. 92). A prototype omits correctness, completeness, robustness and style on purpose (p. 91), so this wiki reads what breaks when it ships as those omissions. Which details may go depends on the question: a UI prototype can use inexact data, and a performance prototype can do with almost no UI (p. 90). For a prototype of a whole system, run the questions in [[architecture-prototype-questions]].

## Sign in code

One of these, in a production path, is required:

- canned or dummy data where a real input should be read, including a request argument that goes unused;
- a module from a `spike`, `poc` or `prototype` folder imported by shipped code.

Two more support that reading and establish nothing alone, because plain careless code shows them too:

- a single working route: one fixed input or one menu entry, with nothing behind the others;
- external calls and parsing with no failure handling, which is otherwise a matter for the `errors` group.

This wiki takes the canned data, the single route and the missing failure handling from the source's omissions of correctness, completeness and robustness. The source's fourth omission, style, is not used, because it does not separate a prototype from other code. The folder name is this wiki's own.

This wiki assigns the neighbouring case as follows. Prototype code reached from the production path (an import of a spike folder, `Table1`-style placeholders or canned rows in shipped code) belongs to this page; prototype code read on its own, grown past its question or stating none, belongs to [[throwaway-prototype]].

The discriminating test separates the two: in tracer code the stand-in sits behind the final interface and the code around it handles errors; in a prototype the surroundings are faked along with the routine.

## When not to apply

- A trivial routine behind the final interface with real error handling is tracer code. Its simplicity is not a defect, as the first-come-first-served packer in the source shows (p. 88).
- A prototype that never reaches a production path may omit all four properties. That is correct (p. 91).
- Prototypes that are not code at all, such as sticky notes or a whiteboard, do not raise this question (pp. 89-90).
- This wiki adds that a one-off script finished in its purpose is not a prototype and is not owed a rewrite.

## Repair

- If the code is a prototype still outside production: keep the lessons and discard the code. The source says that once the decision is made, you start again and program in the final environment (p. 88).
- If the code is a prototype that shipped: this wiki extends the source here, which speaks of a prototype before it ships. First pin what the prototype taught in tests. Then rewrite the parts whose surroundings are faked, and repair the rest in place behind an interface, because production code has users that a discarded experiment does not.
- If the code is a skeleton built to stay: keep it, and replace the stand-in with the real routine behind the same interface (p. 88).
- If a stand-in has no interface of its own yet: introduce the interface first, so the replacement does not touch the callers.

## Before and after

```
// before: a prototype that drifted into production
function pack_handler(request):
    boxes = [Box(10, 20), Box(30, 40)]    // canned, request ignored
    return render(demo_layout(boxes))     // any other shape crashes
```

```
// after: tracer code, trivial algorithm, real surroundings
interface Packer:
    pack(boxes) -> Layout or PackError

class FirstComePacker implements Packer:   // to be replaced behind this interface
    pack(boxes): ...

function pack_handler(request, packer):
    boxes = parse_boxes(request)
    if boxes is invalid: return bad_request(boxes.errors)
    result = packer.pack(boxes.value)
    if result is PackError: return unprocessable(result)
    return render(result)
```

## Source

[[pragmatic-programmer]], Topics 12-13, pp. 87-92: the distinction, the decision conditions, the four omissions and the reasons. The reading of what breaks, the use of three omissions as signs and the split into required and supporting signs, the folder-name sign, the discriminating test as worded, the one-off script limit, the second repair for a prototype that shipped, pinning lessons in tests, the fourth repair and the pseudocode are this wiki's own.
