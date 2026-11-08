---
title: Prototype when code resists
category: change
summary: "Method for a change that keeps fighting back with no cause you can name: set the code aside and write a throwaway version until the doubt becomes a clear question. A cause you can list as constraints is find-the-real-constraints."
tags: [method, prototyping, stuck, design-feedback]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book treats resistance while coding as information about the code. When every step costs great effort and you keep sliding back, it says: «Ваш код пытается вам что-то подсказать» (p. 242). The message may be that the code could be simpler, that the structure or architecture was chosen wrongly, or that the wrong problem is being solved (p. 242). The book's objection to pushing on regardless is that this is probably just what you should not do (p. 242).

This method runs when a change has stalled and no cause can be named. It is a way to find the cause of the resistance, not to finish the change. Where the difficulty has a shape you can write down, such as special cases that each serve a constraint, run [[find-the-real-constraints]] instead.

## Procedure

1. **Set the code aside.** With existing code that resists, save it somewhere and prototype something that does the same job (p. 244). With nothing written yet, pick some aspect of the project that needs exploring, such as a new framework or an algorithm at its edge cases (pp. 243-244).
2. **Treat it as a prototype.** Prototypes are «обречены на неудачу и выбрасывание» (p. 244) even when they succeed.
3. **State what it is for.** Write a one-sentence comment saying what you need to learn or do (p. 244).
4. **Program.** If the doubt turns into a clear question, answer it (p. 244).
5. **Finish.** If you are still uneasy at the end, start again. Once you know what needs doing, delete the prototype and write the real code (p. 244).

## What keeps it honest

This wiki reads the deletion as the working part of the method. The prototype's output is an answer, and if its code survives, the throwaway licence that made quick work possible has shipped.

## Limits

The book gives no limits here. This wiki adds three.

- Resistance is not proof of a design defect. A change may be hard because the problem is hard. The prototype is what tells these apart.
- The method needs the existing code preserved, so it is safe only when that code is committed or stored aside.
- A difficulty with a known cause, such as a missing dependency, needs fixing and not this method.

The cost is the time of a discarded attempt. The book's exercise suggests a limit of one or two hours, with a promise to delete everything when the time is up (p. 245).

## Source

[[pragmatic-programmer]], Topic 37, pp. 241-245. See also [[tracer-code-vs-prototype]] (Topic 13). The reading of deletion, the limits and the condition separating this method from [[find-the-real-constraints]] are this wiki's own. This wiki leaves out the book's earlier moves, stepping away from the code and explaining the problem aloud (p. 243), as personal practice that changes no report on code.
