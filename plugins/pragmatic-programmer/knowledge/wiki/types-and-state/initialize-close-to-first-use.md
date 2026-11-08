---
title: Initialize close to first use
category: types-and-state
summary: "A variable set at the top of a routine or in a one-off Startup() and first read far below, inside a loop or repeated block that never resets it; a counter or accumulator reused without reset; a value assumed to survive between calls; a read with no initialization visible nearby, though one precedes it on every path."
tags: [rule, initialization, accumulator, re-initialization, persistence, proximity]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

McConnell calls improper data initialization one of the most fertile sources of programming errors (p. 233). The variable ends up holding a starting value other than the one the code expects. The book gives three ways this happens: no value was ever assigned, the assigned value has gone stale, or only some parts were assigned, such as some members of an object or a pointer that was never given memory (pp. 233-234). This page owns the case where the initialization sits in the wrong place relative to the code that depends on it. The reader then cannot tell whether the value is fresh.

## Rule

«Инициализируйте каждую переменную при ее объявлении» (p. 234). Where the language allows it, declare and define in one place: «В идеальном случае сразу объявляйте и определяйте каждую переменную непосредственно перед первым обращением к ней» (p. 235). Where it does not allow it, initialize at the place of first use (p. 234). The book's related rules (pp. 236-237):

- «Проверяйте необходимость повторной инициализации» (p. 236). If the variable will be used in a loop or reset between calls, the initializing statement must be inside the repeated part.
- Counters and accumulators (`i`, `j`, `sum`, `total`) need special care, because programmers «забывают обнулить счетчик или аккумулятор перед его использованием в очередной раз» (p. 236).
- Initialize class members in the constructor, and release what the constructor allocated in the destructor (p. 236). This wiki gives that case its own page: [[initialize-every-member-in-every-constructor]].
- Initialize named constants once at startup, and initialize real variables in executable code near their use. A routine first called once is often called many times after a change, and «Переменные, которые инициализируются в методе Startup() уровня программы, не будут инициализироваться повторно.» (p. 236)
- «Объявляйте переменные по мере возможности как final или const» (p. 236). This stops a value changing after initialization.
- Check input parameters before assigning them to anything (p. 237). For that, see [[distrust-external-input]] and [[caller-owns-the-precondition]].

On persistence (p. 245), the book's advice is to assume data is not persistent. A value a routine held when it returned is not assumed to be there on the next call, unless a language feature such as `static` guarantees it. After freeing memory with `delete`, set the pointer to null; this wiki extends that to other released resources. «Если видите обращение к данным, но не можете найти поблизости команду их инициализации, отнеситесь к этому с подозрением!» (p. 245)

The book gives three reasons for preferring initialization next to use over initialization at the top (p. 235):

1. By the time execution reaches the use, something may have changed the value, and later edits make that likelier.
2. Initializing everything in one place suggests that every variable is used throughout the routine.
3. If the code that uses the variable is later wrapped in a loop, the variable must be re-initialized on each pass. The near version needs a small change, and the far version silently does not reset.

The book names this the «Принцип Близости»: keep related actions together (p. 235).

Chapter 16 applies the same rule to loops: «Размещайте инициализационный код непосредственно перед циклом» (p. 366). It names two failures when the setup sits elsewhere: the loop is later wrapped in a bigger loop and its initialization is not moved with it, or the loop is moved or copied into another routine without its initialization (p. 366). Where the loop's per-pass updates belong is [[loop-housekeeping-at-one-end]].

## Sign in code

- A variable is assigned at the top of a routine, or in a startup or init routine that runs once, and is first read inside a loop or a block that runs more than once. No statement inside that repeated code resets it.
- A counter, flag or accumulator (`total`, `count`, `done`, `found`) is reset before the first loop and not before a second use of the same variable.
- An accumulator or counter that a loop updates is given its initial value many lines above the loop, with unrelated statements in between, so moving or copying the loop would leave the setup behind (p. 366).
- A routine reads a local or field that only an earlier call of the same routine assigned, and no `static` or similar guarantee is visible in the code.
- A local or static variable is read and no assignment to it is visible above it in the same routine (the book's own test on p. 245, narrowed by this wiki: fields set by the constructor and parameters do not count).

This wiki assigns the neighbouring cases as follows. This page owns an initialization placed outside the repeated code that must reset it, or placed where a reader cannot see it from the first read. Where nothing repeats, and the complaint is only distance or interleaved references to unrelated variables, [[keep-variable-live-time-short]] owns it; both pages read the same top-of-routine block by that condition. A field a constructor leaves unassigned is [[initialize-every-member-in-every-constructor]]. A field written by one method only so that a later method can read it is [[pass-state-dont-hoard-it]]. An object built empty and completed by setters before use is [[temporal-coupling]]. Reassigning a field after construction is [[immutable-objects]]. A local read on a path where no assignment precedes it is [[variable-state-anomalies]]; a local assigned on every path but far above its first read, or not reset before a repeated block, is [[initialize-close-to-first-use]].

## When not to apply

The limits below are this wiki's own, except where a page is cited:

- A value deliberately carried across iterations, such as a running total over the whole loop, belongs before the loop. Resetting it inside the loop would be the bug. The rule moves the initialization next to the scope the value must cover, not next to the first textual use.
- A named constant, or a variable that stands in for one, is initialized once at startup. The book allows this on p. 236.
- In code with only single-assignment bindings, such as functional code or `final` locals, a stale value cannot arise from reassignment, and only the placement question is left.
- Some languages require declarations at the top of a block. There the book's fallback is to initialize at first use (p. 234), not to move the declaration.
- A value that is expensive to compute and used in a hot loop may be hoisted out on purpose, if nothing inside the loop changes it. That is an optimization, not this sign.

## Repair

1. Move each declaration and initialization down to just above the first use. Where the language allows it, merge them into one statement.
2. If the use is inside a loop or a routine called many times, put the initialization inside that loop or routine, directly before the use.
3. Move per-run variables out of startup code and into the code that uses them.
4. Mark as `final`/`const` every binding that does not change after it is initialized.

The procedure for moving a declaration down to its first use without changing behaviour, with its interference checks, is [[slide-statements]].

## Before and after

Before:

```
function report(batches)
    total = 0
    done = false
    for batch in batches
        while not done
            total = total + next_amount(batch)
            if total > LIMIT
                done = true
        print(batch.id, total)
```

The second batch starts with `done` already true and `total` carried over. Neither was reset when the loop over batches was added.

After:

```
function report(batches)
    for batch in batches
        total = 0
        done = false
        while not done
            total = total + next_amount(batch)
            if total > LIMIT
                done = true
        print(batch.id, total)
```

## Source

McConnell, *Code Complete*, Russian edition, via [[code-complete]]: section 10.3, pp. 233-237, for the three causes, the placement rules, re-initialization, counters, constructors, Startup() and `final`/`const`; section 10.5, p. 245, for persistence and the "suspect a read with no initialization nearby" test; p. 235 for the three reasons and the Principle of Proximity; section 16.2, p. 366, for initialization directly before a loop and its two failure modes. The book's examples are in Visual Basic, C++ and Java. This wiki's own: the wording of the signs, the extension of the null-after-release advice beyond memory, the assignment against [[keep-variable-live-time-short]], [[variable-state-anomalies]] and the neighbouring pages, every limit except the startup-constant one, the order of the repair steps, and the pseudocode, which adds the outer loop the book warns about on p. 235.
