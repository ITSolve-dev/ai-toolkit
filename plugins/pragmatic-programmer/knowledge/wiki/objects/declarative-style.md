---
title: Declarative style in objects
category: objects
summary: "Objects that declare what a value is (new Between(5, 9, 13)) rather than computing it at the call (Math.between(5, 9, 13)): evaluation on demand, substitution through constructors, and lines bound into one expression so they cannot be reordered by mistake."
tags: [concept, declarative, imperative, lazy-evaluation, temporal-coupling]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

Bugayenko contrasts thinking "like a computer", where the program gives the processor instructions executed top to bottom, with thinking in terms of what things *are* (*Elegant Objects*, section 3.2, pp. 119-121). In Lisp, `(def x (max 5 9))` binds `x` to the larger number without saying how or when it is computed; the relation "is" is what, in the book's account, separates functional, logical and object-oriented programming from procedural (p. 121). An object expresses the same thing: `new Max(5, 9)` defines `x` as the larger of two numbers without computing it (pp. 121-122). A static method, by contrast, is a subroutine in object syntax (p. 122).

The book borrows the definitions from Wikipedia: imperative programming describes computation in terms of statements that change program state, declarative programming expresses the logic of a computation without describing its control flow (p. 123).

## Four arguments the book gives

1. **Speed through laziness.** Creating `Between` costs more than calling a static `between()` when the path is simple (pp. 124-125). But when a result is computed and then used only under a condition, the static version always computes and the object computes only if asked (p. 125). The author concludes that the declarative version is faster because it is optimal, leaving optimisation to the compiler, the VM or the processor (pp. 125-126).
2. **Polymorphism.** An object can take its collaborators through a constructor, so the algorithm inside `Between` can be replaced by passing a different number object; the static version can only be rewritten (pp. 126-127). The book adds that to decouple an object fully, it must not use `new` in any of its methods or its primary constructor (p. 127); see [[new-only-in-secondary-constructors]].
3. **Results over procedure.** A loop that collects even numbers must be run in the head to know what it yields; `new Filtered(numbers, isEven)` states that `evens` is a filtered collection and hides how (pp. 128-129). The author concedes the loop may feel easier to some readers and calls that habit (p. 129).
4. **Cohesion of the expression.** In the declarative version `evens` is defined by one expression, so the lines that compute it sit together and cannot be separated by mistake; in the imperative version nothing binds the lines, and reordering them breaks the algorithm. In a 50-line imperative fragment it becomes hard to see which lines belong together (p. 129). The book links this to temporal coupling, discussed with immutable objects (see [[temporal-coupling]]).

## No mixing

The author rejects using objects where it makes sense and static methods for quick simple things: the styles cannot be combined technically, because a declarative class built on static helpers must call them directly and so loses constructors and encapsulation for them (p. 130). This wiki reads this as the root of [[no-static-methods]].

## Where it extends

The book pushes the idea to replacing `if`, `for`, `switch` and `while` with classes `If`, `For`, `Switch`, `While`, and shows `rate = new If(new GreaterThan(new AgeOf(client), 65), 2.5, 3.0)` (p. 141). It states the goal outright: «В коде совсем не должно быть процедурных операторов вроде if, for, switch и while. Звучит как утопия, но это не утопия.» (p. 140). The author admits such languages do not exist yet and, as interim advice, asks for short methods and composable micro-classes (p. 142); see [[composable-decorators]]. This wiki records this as the author's direction, not as a rule: there is no sign in code that would make an ordinary `if` a violation, and the book's advice for today's languages (p. 142) does not ask for it.

## The functional comparison

Asked why not use functional programming if objects are small, immutable and free of statics, the author answers that OOP is more expressive because it has objects and methods while FP has only functions, and that Java's lambdas loosen the language away from OOP (p. 139). His ideal is classes holding real functions with a single exit point instead of micro-procedure methods (p. 139). This wiki notes that this is the author's preference, not an argument checkable in code, and that the laziness and substitution arguments above hold equally for functions passed as values (compare [[decompose-into-transformations]]).

## Trade-offs and failure modes

- Readers' comments printed with the section object that the style spreads simple code across many classes and files and adds the cost of throwaway objects (p. 144), and that it ignores memory and performance in constrained systems (pp. 144-145). The author answers that programmer time costs more than hardware and that performance comes after clarity (p. 145).
- This wiki's own observation: laziness moves the cost and any failure of a computation to the point where the value is first asked for, which may be far from where it was declared. A failure in a declared-but-unevaluated pipeline surfaces at the consumer, not at the line that built it.
- This wiki's own observation: a lazily evaluated object that is asked for its value repeatedly recomputes it unless it caches, so the speed argument holds only when values are used once or cached (the caching decorator is on [[constructors-without-code]]).

## Source

- [[elegant-objects]], section 3.2, pp. 119-142, and reader comments pp. 143-145. OCR noise is heavy in these pages. The quotation of p. 140 was transcribed from the OCR text, which is clean there, and not checked against the page image.
- This wiki's own: the decision not to make the `If`-class idea a rule, the note on functions as values, and the two failure modes about deferred failure and recomputation.
