---
title: Pseudocode Programming Process
category: functions
summary: "Procedure for writing a non-trivial routine: state its contract, write intent-level pseudocode, turn it into comments, fill code under each, then desk-check, polish and iterate; the polish step is a short review of a routine just written."
tags: [method, functions, documentation, design]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The **Pseudocode Programming Process** (PPP) is McConnell's procedure for constructing a single routine that is not trivial. Accessors and thin pass-throughs do not need it. He presents it as a way to cut the work of design and of documentation while improving both: the pseudocode is the design, and it later becomes the routine's comments (*Code Complete*, Russian edition, pp. 209, 211). It is one of several methods; test-first development, refactoring and design by contract are named as alternatives or complements (p. 225).

Class construction around it is iterative: rough out the class (its secrets, level of abstraction, inheritance, main public methods), build each routine, then review and test the class as a whole. Building a routine usually turns up the need for further routines, higher or lower level, and that sends you back to the class design (p. 210).

## Steps

### 1. Design the routine

1. **Check prerequisites.** Make sure the routine's job is clearly defined and fits the overall design (p. 214).
2. **State the problem it solves**, at least: what it hides, its inputs, its outputs, its preconditions and its postconditions (pp. 214-215). See [[design-by-contract]] and [[state-the-contract]].
3. **Name it.** A clear, unambiguous name; difficulty finding one is a signal: «Затруднения в выборе имени метода могут свидетельствовать о том, что его назначение не совсем понятно» (p. 215). If the vague name comes from a vague design decision, go back and change the decision. See [[routine-names]].
4. **Decide how it will be tested** while designing it (p. 215). See [[test-is-first-client]].
5. **Look for existing functionality** in the language's, platform's or company's libraries before writing an algorithm; then in the algorithms literature (pp. 215-216). See [[use-existing-components-before-writing-your-own]].
6. **Decide the error-handling approach.** If the architecture fixes a strategy, follow it; otherwise choose one deliberately for this routine (p. 216). See [[consistent-error-handling-strategy]].
7. **Think about efficiency in one of two ways.** In most systems it is not critical: keep the interface abstract and the code readable so a slow part can be replaced behind it later. In the few where it is, the book expects the resource budget per routine or class to come from the architecture, which this wiki takes as given. Micro-tuning a single routine waits until the whole program is shown to need it (p. 216). See [[fastest-algorithm-is-not-always-best]].
8. **Write the pseudocode**, starting with a header comment that states the routine's purpose in a few sentences; if that statement is hard to write, the routine's role is not yet understood (pp. 216-217). Then add high-level steps below it, written at the level of intent; the style rules are on [[comment-why-not-how]].
9. **Think about the data** first when manipulating data is a substantial part of the routine (p. 217).
10. **Check the pseudocode**: explain it to someone, or have a colleague read it. A few lines of pseudocode get reviewed more willingly than a page of code, and they show a wrong intention more plainly (p. 217). The book asks: «Если вы не понимаете его концептуально, на уровне псевдокода, какой же тогда у вас шанс разобраться в нем на уровне языка программирования?» (p. 218).
11. **Try several ideas in pseudocode and keep the best** before coding, because once coding starts you become attached and find it harder to throw a bad design away (p. 218). Refine until each line is simple enough to put one code line or block under it, and stop when further refinement looks like a waste compared with writing the code.

### 2. Code the routine

1. Write the declaration; turn the header into a comment in the language's syntax above it (pp. 218-219).
2. Turn every pseudocode line into a comment inside the body (pp. 219-220).
3. Write code under each comment, like paragraphs under an outline. Each comment usually expands into 2-10 lines of code (p. 222). Declare variables near first use (p. 222).
4. Check whether a block has grown well past that and needs decomposition: see [[extract-routine-to-name-a-step]] (p. 222).

In the book's worked example a five-sentence specification became about 15 lines of pseudocode and then a page of code; McConnell takes this as evidence that coding itself involves low-level design (p. 222).

### 3. Check the code

1. **Desk-check**: execute every path and exceptional condition mentally, alone and with colleagues. That this is hard is, per the book, one reason to keep routines short (p. 223).
2. **Understand why it works.** See [[programming-by-coincidence]].
3. **Compile with the highest warning level, use checking tools, and find the cause of every warning** rather than tolerating a recurring one, which either hides more important warnings or is simply noise; it is usually easier to remove the cause (p. 224). The book also advises delaying the first compile until you believe the code correct, to avoid a hurried "one more compile" loop (p. 223); this wiki records that advice but does not adopt it as a step: unlike the other check steps it changes only when the code is checked, not what is checked.
4. **Step through it in a debugger**, line by line, checking each does what you expect (p. 224).
5. **Run the planned tests**, with scaffolding (drivers that call the routine, stubs it calls) kept out of the product (p. 224).
6. **Remove errors.** If the routine turns out erratic and full of defects, the book prefers starting it over to patching it (p. 224); see [[rewrite-a-method-you-do-not-understand]].

### 4. Polish

The book's checklist for a finished routine (pp. 224-225):

- Interface: every input and output is used, every parameter is used.
- Design: the routine does one thing well, is loosely coupled to others, is defensively written.
- Variables: naming, unused or undeclared objects, wrong initialisation.
- Logic: off-by-one errors, wrong nesting, resource leaks.
- Documentation: the comments that came from pseudocode are still accurate; the algorithm, interface, non-obvious dependencies and unusual choices are documented.
- Redundant comments removed, especially after recursive PPP leaves comments that only restate a call whose name already says it.

The fuller form of this check, applied to existing code, is [[routine-review-checklist]].

### 5. Repeat

If the routine is not good enough, return to the pseudocode (p. 225).

## Comments first, as chapter 32 puts it

Chapter 32 returns to this process as the cheap way to comment. Describe the routine in high-level pseudocode before writing it, turn the pseudocode into comments, and write the code under them (pp. 767, 773). When the code is done the comments are done, no separate time goes into them, and the routine has had the benefit of being designed before it was coded (p. 773). The chapter's dialogue warns that this works only if the comments do not repeat the code (p. 767), which is why step 4 removes those that now restate their line; see [[comment-why-not-how]] and [[comment-kinds]].

The book gives two reasons commenting takes long (pp. 770-771). One is a laborious style, which is fixed by changing the style; see [[maintainable-comment-style]]. The other is trouble putting into words what the program does: «Обычно это говорит о том, что вы не понимаете работу программы» (p. 771). The time spent commenting is really spent understanding the program, and has to be spent whether one comments or not (p. 771). The same reasoning answers the objection that commenting breaks concentration on the code. If code needs so much concentration that writing a comment breaks the train of thought, the fragment should be designed in pseudocode first, because «Код, требующий такой сильной концентрации, — тревожный симптом.» (p. 773). If a design is hard to code, simplify it before writing either comments or code (p. 773).

This wiki turns the difficulty signal into a check for review as well as for writing: when the one-sentence comment for a block cannot be written without describing its statements one by one, treat the block as a candidate for simplification or extraction rather than for a longer comment. The book states the signal for the author, not for a reviewer. This wiki also reads the book's claim that effective commenting takes little time (p. 770) as assuming the author already understands the routine. For exploratory code whose shape is not yet known, pseudocode written up front will be rewritten, and the clean-up in the polish step matters more than the first draft.

## When to use it

The book names the trigger for switching to a systematic method: not knowing what to do next, staring at the screen without knowing where to start, or forgetting to write part of a class or routine (p. 226). This wiki reads the method as most useful when writing a routine whose logic has several branches; for a one-line accessor it adds nothing, which the book also says (p. 211).

## Trade-offs

- The pseudocode-derived comments can become redundant once code is clear or once blocks are extracted into well-named routines; the polish step exists to remove them (p. 225).
- The method front-loads design time. The book justifies this by the cost of a defect at the stage where it is caught: a few lines of pseudocode are cheaper to fix than a page of code (p. 213).
- A footnote of the Russian translation notes that the advice on natural-language pseudocode fits English best, because programming languages are English-based (p. 212). This wiki writes its own pseudocode in English for the same reason.

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 9, pp. 209-227. The step list, the polish checklist and the alternatives are the book's. The cross-links to owning pages, the note on when it adds nothing, and the decision not to adopt the delayed-compile advice are this wiki's own. Chapter 32, sections 32.3 (p. 767) and 32.4 (pp. 770-771, 773): pseudocode as the way to comment, the two reasons commenting is slow, difficulty as a sign of not understanding, the warning about code that needs high concentration, simplifying a hard design first, and the case against commenting at the end (not carried here, as it is process advice with no sign in code); the suggestion of pseudocode and the warning against repeating the code are made by characters in the dialogue (p. 767) and restated by the narrator on p. 773. The review check and the trade-off for exploratory code are this wiki's own. The ch. 32 quotations were transcribed from the extracted text and should be checked against the page image.
