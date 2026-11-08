# Overview

A working reference of rules for writing good code in any language. It serves the agents of the plugin that bundles it, which apply a rule to a piece of code and cite it, and the people who open a cited page to check that decision. The model already knows these rules by name, so a page earns its place by supplying the judgement on a specific piece of code: is the rule broken here, does it apply, what exactly changes.

Seven books and two web articles have been ingested, five books read in Russian and the rest in English: [[pragmatic-programmer]], Thomas and Hunt's *The Pragmatic Programmer*, 20th Anniversary Edition; [[elegant-objects]], Bugayenko's *Elegant Objects*; [[code-complete]], McConnell's *Code Complete*, 2nd edition; [[object-oriented-thought-process]], Weisfeld's *The Object-Oriented Thought Process*, 4th edition; [[automata-based-programming]], Polikarpova and Shalyto's *Automata-Based Programming*; [[larman-applying-uml-and-patterns]], the GRASP and GoF chapters of Larman's *Applying UML and Patterns*, 3rd edition, read in English; [[fowler-refactoring]], Fowler's *Refactoring*, 2nd edition, read in English; and two articles by Wlaschin, [[railway-oriented-programming]] (2013) and its author's own critique [[against-railway-oriented-programming]] (2019). The first spreads across every group. The second is concentrated in `objects`, with rules on null, exceptions and resources in `errors`, on immutability in `types-and-state`, and on mocks in `testing`. The third is the largest and also spreads across every group; it supplies most of the pages on routines, variables, control structures, class interfaces, defensive programming, test design, debugging and comments, and its organising idea is [[managing-complexity]]. The fourth is an introductory book on objects; it adds few pages of its own and mostly joins pages already in place in `objects`, `structure` and `types-and-state`, on interface against implementation, minimal interfaces, private attributes, constructors, composition and the cardinality of associations, with a few claims on exchanged and persisted data in `errors` and `objects`. The fifth is a textbook on programming with explicit states; nearly all its pages sit in `types-and-state`, where it now owns the shapes of state-machine code (flags holding history, the switch mirroring the graph, transition checks, control logic kept apart from data, events, the automated class), with one page each in `errors` and `debugging`. The sixth sits mostly in `objects` and `structure`: it owns the pages on where a responsibility goes (the GRASP principles [[information-expert]], [[creator]], [[controller]], [[low-coupling]], [[pure-fabrication]], [[protected-variations]]) and on the GoF patterns read as their specializations ([[patterns-as-specializations-of-grasp]], [[proxy]], [[abstract-factory]], [[strategy-for-varying-algorithms]], [[composite-same-interface-as-part]], [[observer-publisher-knows-only-interface]], [[facade-single-entry-point]]), and joins pages already in place on coupling, cohesion, polymorphism and exceptions. The seventh, the core source on changing code safely, spreads across every group but `debugging` and `documentation`: its principles and procedures sit in `change` ([[refactor-in-small-tested-steps]], [[preparatory-refactoring]], [[parallel-change]], [[change-function-declaration]], [[move-function]]), its smells join the owners already in place through [[refactoring-warning-signs]], its chapter on tests sits in `testing` ([[self-testing-code]]), and its catalogue gives `functions` and `objects` most of their extract, inline, parameter and inheritance refactorings ([[extract-function]], [[parameter-or-query]], [[function-or-command-object]], [[pull-up-method]], [[replace-type-code-with-subclasses]], [[replace-subclass-with-delegate]]). The two articles sit in `errors`: they join the pages on carrying failures as values ([[wrap-values-between-transformations]], [[handle-errors-in-stages-or-in-the-pipeline]]) with the plumbing of the first and the limits of the second, and add one page, [[collect-independent-validation-failures]]. The charter is `SCHEMA.md`, the full catalogue is [[index]], and what the pages add up to is [[synthesis]].

## How the wiki is organised

Pages are grouped by the problem someone arrives with in the code, not by book or paradigm. Each group is also one review dimension: one inspector runs per group, searches its summaries and opens the pages the code calls for. A `summary` line therefore names the sign in code and not the topic.

Page kinds, given by the first tag:

- `rule`: a prescription with its sign in code, limits, repair and a pseudocode before and after.
- `decision-rule`: a test deciding between two courses.
- `concept`: an idea the rules rest on.
- `method`: a procedure to run against code.
- `summary`: one per source.

Every page marks what is the source's and what is this wiki's own reasoning, in `## Source`. Most signs and limits are the wiki's, because the books rarely state them. Where the books disagree, the page resolves it per setting rather than recording the disagreement.

## The groups

| Group | Problem it answers | Start at |
|---|---|---|
| `change` | How to alter code without making the next change harder | [[easier-to-change]], [[refactoring]], [[refactor-in-small-tested-steps]], [[refactoring-warning-signs]], [[software-entropy]] |
| `complexity` | Code doing more than its job needs | [[managing-complexity]], [[design-warning-signs]], [[dry]], [[know-when-to-stop]], [[coincidental-duplication]], [[tame-deep-nesting]] |
| `structure` | How classes and functions inside a module depend on one another | [[coupling]], [[information-hiding]], [[near-decomposability]], [[global-data]], [[orthogonality]], [[circular-dependency]], [[event-driven-code]] |
| `objects` | Responsibilities, inheritance and interfaces | [[object-as-representative]], [[responsibility-driven-design]], [[information-expert]], [[interface-and-implementation]], [[inheritance-tax]], [[final-or-abstract]], [[tell-dont-ask]], [[constructors-without-code]], [[class-interface-coherent-abstraction]], [[containment-or-inheritance]], [[aggregation-vs-association]] |
| `functions` | Shape and composition of routines | [[routine-cohesion]], [[routine-length]], [[pass-what-the-routine-uses]], [[programs-transform-data]], [[decompose-into-transformations]], [[finish-what-you-start]] |
| `errors` | Failure, contracts, assertions and trust at the boundary | [[design-by-contract]], [[crash-early]], [[recover-only-at-entry-points]], [[never-return-null]], [[assertion-or-error-handling]], [[distrust-external-input]], [[barricade]], [[consistent-error-handling-strategy]] |
| `types-and-state` | What a value can be and who may change it, and behaviour that depends on history | [[immutable-objects]], [[shared-state-is-incorrect-state]], [[class-invariant]], [[complex-behavior]], [[replace-flags-with-explicit-states]], [[state-machine-as-switch-on-state]], [[automated-object]] |
| `testing` | What a test should pin and whether it can fail | [[self-testing-code]], [[test-levels]], [[test-state-coverage-not-line-coverage]], [[sabotage-your-tests]], [[structured-basis-testing]], [[boundary-value-analysis]] |
| `debugging` | Finding a cause by method | [[debugging-procedure]], [[fix-the-root-cause]], [[programming-by-coincidence]] |
| `naming` | Names that carry meaning | [[name-by-role]], [[one-name-per-concept]], [[name-describes-what-the-variable-represents]], [[name-length-matches-scope]] |
| `documentation` | What a comment owes the reader | [[comment-why-not-how]], [[self-documenting-code]], [[state-the-contract]] |

## Pairs worth knowing

Some neighbouring pages look alike and give different answers. Each draws the line itself.

- A method chain: [[train-wreck]] when it navigates held objects, [[transformation-pipeline-over-method-chain]] when it does work on data.
- An impossible state: [[assert-the-impossible]] for a bug, [[assertion-or-error-handling]] for what can occur and for telling which.
- Two like pieces of code: [[dry]] when they state one fact, [[coincidental-duplication]] when they do not.
- A flaw in working code: [[broken-windows]] or [[good-enough-versus-broken-window]].
- Experimental code: [[tracer-code]] is kept and a prototype is thrown away; [[tracer-code-vs-prototype]] tells them apart.
- Reacting to events: [[state-machine-or-event-stream-or-pubsub]] decides between the strategies.
- History in flags: [[replace-flags-with-explicit-states]] when one entity's handlers test the flags, [[finite-state-machine]] when one loop over a sequence does, [[finite-memory-folds-into-states]] for flags beside an existing state variable.
- The form of a state machine: [[state-machine-as-switch-on-state]] for the shape of the switch, [[state-machine-table-or-switch]] for table against code, [[switch-on-state-vs-state-pattern]] for the object form; a switch over a fixed type code is [[polymorphism-or-type-switch]] instead.
- A missing fallback: [[transition-conditions-consistent-and-complete]] among one state's guards, [[default-branch-catches-the-unexpected]] on the switch over the state itself.
- Inline work in a case arm: [[separate-control-object-from-state-logic]] inside a state machine's step function, [[keep-case-arms-short]] elsewhere.
- Several state machines: [[state-machines-communicate-through-an-explicit-interface]] for how they see each other, [[called-vs-nested-state-machines]] for how one runs another, [[decompose-state-machine-by-modes-or-by-controlled-objects]] for how to split one.
- A bug fix and its test: [[find-bugs-once]] when no test came with the fix, [[failing-test-before-the-fix]] when a test exists and proves nothing.
- A catch that does not rethrow: [[crash-early]] when only a bug can produce the failure, [[recover-only-at-entry-points]] when a correct program can meet it; a catch that throws anew is [[chain-exceptions]], one that logs and rethrows is [[log-and-rethrow]].
- A subclass of a concrete class: [[final-or-abstract]] when it overrides an implemented method, [[inheritance-tax]] when it reuses without overriding.
- Absence: [[never-return-null]] for a returned null, [[no-null-arguments]] for one passed in, [[null-object-or-optional]] for what replaces it.
- A value that does not change: [[immutable-objects]], and [[immutable-versus-constant-object]] for whether it also returns the same answer each time.
- Failure reporting across a codebase: [[consistent-error-handling-strategy]] when peers or the functions of one module mix mechanisms; [[exceptions-for-the-exceptional]] for whether an expected outcome may throw.
- Assertions in shipped code: [[defensive-code-in-production]] decides between McConnell's compiled-out view and *The Pragmatic Programmer*'s leave-them-on, with [[leave-assertions-on]].
- A metric over its threshold: [[design-warning-signs]] for the code in front of you, [[metric-outlier-review]] for choosing where to look, [[refactoring-warning-signs]] for what to refactor.
- Data arriving from outside: [[barricade]] for where the check stands (on the side that owns the data, never only in the client), [[validate-exchanged-data-against-a-declared-schema]] for checking a document's structure, [[convert-input-at-entry]] for raw text past the door.
- A design pattern: [[design-pattern]] for what one is, [[patterns-as-specializations-of-grasp]] for the variation each one pays for, [[do-not-force-a-design-pattern]] when its problem is absent; Singleton is [[no-singletons]], Adapter [[hide-third-party-apis]], Iterator [[iterator]], Proxy [[proxy]], Abstract Factory [[abstract-factory]].
- Method bodies repeated on sibling classes: [[shared-behavior-in-superclass-varying-step-polymorphic]] when they override one method of a common project superclass, [[mixins-share-functionality]] when they share no superclass of the project's own, [[similar-functions-varying-middle]] for functions that override nothing.
- Where a responsibility goes: [[information-expert]] first, [[creator]] for creation, [[controller]] for a system operation, [[pure-fabrication]] when the expert would gain coupling or lose cohesion.
- Duplicated members in a hierarchy: [[pull-up-method]] for methods or fields the superclass does not declare, [[shared-behavior-in-superclass-varying-step-polymorphic]] for overrides of one it does, [[extract-superclass]] when there is no superclass yet, [[mixins-share-functionality]] when their instances would not be valid instances of one parent.
- A subclass that does little: [[collapse-hierarchy]] when one class of the pair is empty, [[subclass-that-differs-only-in-data]] when it overrides only constants, [[base-class-with-one-subclass]] when both hold code.
- A type code: [[polymorphism-or-type-switch]] for the switches on it, [[replace-type-code-with-subclasses]] for fields valid only for some codes and for subclassing the class or a type object.
- Inheritance that rubs: [[replace-subclass-with-delegate]] for a second axis or a run-time change of kind, [[replace-superclass-with-delegate]] for an instance extending its kind.
- A value in the parameter list: [[parameter-or-query]] when the callee could derive it, [[pass-what-the-routine-uses]] for the whole record or its parts, [[semantic-coupling]] when a literal selects the callee's branch.
- A small class built and called once: [[function-or-command-object]].
- A missing language feature or a convenience feature: [[program-into-the-language]], with the general case of conventions on [[coding-conventions]].
