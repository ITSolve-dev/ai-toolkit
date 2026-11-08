---
title: Comment why, not how
category: documentation
summary: "A comment restates the code under it in language terms ('if flag is zero'), explains a literal a named constant could carry, lists the same steps or numbers as the body, contradicts it, or sits as a template on every function, while a surprising delay, ordering, workaround or deliberate non-obvious technique has no stated reason."
tags: [rule, comments, dry, naming, documentation, pseudocode]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-07
---

**Commenting why, not how** is the rule that a comment on non-API code gives what the code cannot say: the reason, the purpose, the trade-off. A comment that repeats the code states the same intent twice, once for the reader and once for the machine, and only one of them is executed, so it is a case of [[dry]]. Comments on an interface are a separate matter, see [[documentation-in-the-source]].

## Rule

Outside the API, the book recommends limiting comments to «указанием причин, назначения и целей написания кода» (p. 54). Its reason is that «сам исходный код уже ясно показывает, как он написан», so saying it again breaks DRY (p. 54). Comments are the ideal place for what can be recorded nowhere else: «инженерные компромиссы, причины принятия конкретных решений и отвержения альтернативных решений» (p. 54).

The book rejects the policy that every function, data structure and type declaration must carry a comment. «Такой механичный подход к составлению комментариев на самом деле усложняет сопровождение кода», because each change then has to update both the code and the comment (p. 54). It returns to this under DRY and calls the belief that every function needs a comment a myth (p. 64). In its example the purpose of a function is given twice, so a changed fee policy has to be applied in both places, and the authors guarantee that the comment will drift out of step with time (p. 65). This wiki adds what follows when the second update is skipped: nothing fails, and the comment goes on stating something false.

The book's position on p. 65 is stronger than the one on p. 54: «комментарии лишь возмещают неудачное именование и компоновку». Clear names show purpose, and whoever needs details finds them in the code (p. 65). Taken alone, that sentence would remove the reason comments p. 54 asks for. This wiki resolves the two by what a comment holds: a comment whose content the code could carry is covering for naming or layout, and one holding a fact no name or line can contain is the kind p. 54 recommends.

*Code Complete* reaches the same place from the other end, the comment written before the code. In the [[pseudocode-programming-process]] each pseudocode line becomes a comment, so McConnell's rules for pseudocode are rules for comments: wording that describes each action precisely, no constructs of the programming language, the level of intent, and low enough that code follows almost automatically (pp. 211-212). The central one: «Пишите псевдокод на уровне намерений.» (p. 212). Pseudocode with language constructs drops the author to code level, and turned into comments it repeats what the code says (pp. 211-212). His bad example holds a library allocation call, a pointer dereference and the literal return codes 1 and 0; McConnell's verdict, paraphrased, is that it shows how the code will be written rather than what it is for. The good version speaks of tracking the number of resources in use and returning true or false depending on whether a resource was created (p. 212). After code is filled in, a comment that only restates a call whose name already says it is to be removed (p. 225).

Chapter 32 of *Code Complete* gives a verdict on three ways a comment can stand over code. McConnell shows three "mystery routines" (pp. 768-769). The first claims in its comment to print sums of the numbers 1..n and actually computes Fibonacci numbers, so a reader who trusts the comment goes the wrong way. The second comments every line ("assign base to product", "loop from 2 to num"). Its comments are correct, but they say nothing the code does not. The third carries one comment, that it computes a square root by the Newton-Raphson approximation, and it is the only one of the three whose comment earns its place. The book concludes that bad comments are worse than none, and that the first two routines would be better with no comments at all (p. 769, paraphrased; the sentence breaks across a line-break hyphen in the raw extraction). On a comment that disagrees with the code, a character in the chapter's dialogue says that treating comments as sacred and code as suspect is a serious mistake, and that a mismatch usually means both are wrong; the narrator adopts that view at the end (p. 767, paraphrased). The six-way classification of comments the chapter goes on to give is [[comment-kinds]].

McConnell then works at the level of a *paragraph* of code, a group of statements with one purpose. Most comments in a well-documented program, he says, are one or two sentences describing such a paragraph (p. 777). His rules (pp. 777-783):

- **Comment at the level of intent.** A comment stating a paragraph's purpose survives a fix inside it: if the code that swaps two roots has a bug, the comment "swap the roots" stays true (p. 777). The book improves a comment over a search loop in three steps. The first only repeats the loop, the second says it searches for `$`, and only the third, which says it looks for the character that ends a command word, tells the reader something the listing does not (pp. 777-778). Its test is to treat the comment as the name of a method doing the same thing: «Опишите суть кода как имя соответствующего метода, не используя сокращений и аббревиатур» (p. 778).
- **Look at the code first.** In the same example the literal `$` should become a named constant, the variables should get informative names, and a separate result variable should keep the loop index apart from the loop's result (pp. 778-779). In the end the paragraph should become a method such as `FindCommandWordTerminator()`, because comments go out of date and turn wrong more often than method names do (p. 779).
- **Answer why, not how.** `// if account flag is zero` over `if (accountFlag == 0)` works at the level of the language and adds nothing, while `// if establishing a new account` does. Once `0` is a named enumerator and the variable is renamed, the comment is redundant; it may still be kept as a heading over the whole block (pp. 779-780).
- **Document surprises.** Where a non-obvious technique was chosen over a simple one for speed, the comment names the simple one and the gain. The book's example uses a right shift to divide by 2 and records that the loop is 75% faster because this compiler does not make the substitution itself (pp. 780-781). Without the comment a reader would grumble that the code is complicated for no reason. Since such grumbling is usually justified, «документировать исключения из правил важно» (p. 781).
- **Comment workarounds** for defects or undocumented features of the language or environment. In the book's example a library call misbehaves only when its block size is 500, and the guard before the call says why the special case exists (pp. 782-783). **Justify violations of good style**, so that a well-meaning programmer learns that "improving" the code would break it (p. 783).
- **Tell major comments from minor ones by structure, not by typography.** The book rejects underlining or capitals for major comments, because one underline forces underlining everywhere else. Its better option than underlining is to start each minor comment with an ellipsis (p. 782). The one that often works best is to extract the code under the major comment into its own method, because a method that mixes general and detailed actions is not logically flat (pp. 781-782).

This wiki reads the surprise and workaround rules of chapter 32 as the source for the missing-reason sign below, which the first ingest stated as this wiki's own.

## Sign in code

- The comment restates the lines it sits on one by one, at their own level.
- A comment names the operators and variables of the next line in words: "if flag equals zero", "increment i", "loop until done" (*Code Complete*, p. 779).
- A comment explains what a literal in the code means (`$` ends a command word) where a named constant could say it (pp. 778-779).
- A comment over a paragraph would make a poor method name: it lists the mechanics (`CheckEachCharacterUntilDollarOrEnd`) instead of the effect (`FindCommandWordTerminator`) (p. 778).
- Consecutive paragraphs of one method carry comments some of which are marked as subordinate to others by underlining or capitals (p. 781). An ellipsis is the book's acceptable form (p. 782); this wiki reports it only as a pointer to extraction, the book's better option.
- A comment above a function enumerates the steps of the body below it, in the same order.
- A comment above a block names a library function, an operator, pointer or index syntax, or a literal status code that the block below also contains (`// call alloc, if null return -1`). This wiki's discriminating test: blank out every identifier and literal in the comment; if it no longer says anything, it was written at implementation level.
- A comment directly above a single call says the same as the call's name (`// log the message` over `log_message(msg)`), typically left over after a commented block was extracted into a routine named from the comment.
- The same number or threshold appears in a comment and in the code under it.
- A comment, above a declaration or inside a body, sits over short or abbreviated names and restates what the body does with them, so the comment is the only place their meaning is stated.
- A comment on a non-API function restates parameter names and types the signature already gives.
- The same template of comment sits on every function or type in a file, whatever its interest.
- A comment contradicts the code under it, which is the cost above already paid.
- A delay, an ordering or a workaround that cannot be derived from the code around it has no comment giving the reason. This includes a deliberate non-obvious technique (a shift for a division, a hand-unrolled loop) with no comment naming the plain alternative and the gain, and a guard that special-cases one value before a library call with no comment naming the defect it avoids (*Code Complete*, pp. 780-783).

This wiki treats the last sign apart from the others. They report a comment to remove; this one reports a comment that is missing, whose content the code does not hold, so it goes out as a question for whoever knows the reason. It applies only where no other page explains the delay: [[select-isnt-broken]] owns a delay blamed on a dependency, [[temporal-coupling]] a delay before reading a result something else produces, and [[remove-calls-you-cannot-justify]] a delay beside overlapping calls. Those pages repair the code, so a comment there would dress up what should go.

An exported routine with no doc comment, or one whose doc comment states a contract the names and types cannot, belongs to [[documentation-in-the-source]]. A comment, above a declaration or inside a body, that restates steps, numbers or names the body already holds belongs to [[comment-why-not-how]]; a doc comment that says what a vaguely named class or method is for, without restating its body, belongs to [[tests-instead-of-documentation]]. A comment heading a block whose result has a nameable meaning is [[extract-routine-to-name-a-step]]; a comment that restates steps, numbers or names the body already holds is [[comment-why-not-how]].

This wiki also assigns a comment that restates a routine's name, over a body that fails or returns a special value unless a condition holds that neither its name nor its signature states, to [[state-the-contract]]: the comment is replaced by the condition and not deleted.

This wiki assigns the neighbouring case as follows. The header of a file or class, and what it owes about the unit's design, is [[design-notes-in-code-headers]].

This wiki assigns the neighbours from chapter 32 by one question: could the code be rewritten so that the comment is no longer needed? Where a comment warns that the code is tricky or must not be touched, or explains a trick a plain construct would avoid, and the answer is yes, [[rewrite-tricky-code]] owns it and the repair rewrites the code. Where the trick is forced from outside, this page owns it and the comment stays. A comment to the right of a statement is [[end-of-line-comments]], which owns its placement; what the comment says is judged by [[comment-why-not-how]]. A to-do marker is [[marker-comments]]. A fixed-field header template on a routine is [[routine-header-comment]]. A declaration lacking a unit, range or bit layout is [[comment-data-declarations]].

## When not to apply

- Interface comments. The book wants modules and exported functions commented, see [[documentation-in-the-source]].
- A comment that explains a non-obvious *how* (a workaround, an unusual choice, a dependency the code cannot show) may legitimately name a construct. McConnell's polish checklist lists documenting non-obvious dependencies and non-standard approaches as a separate duty (p. 225).
- A comment over a call that adds what the name cannot say, such as a precondition or a reason for the order, is not redundant and stays.
- A comment carrying what the code cannot say is not a duplicate: the reason for a choice, a constraint imposed from outside such as a dependency's documented limit, a warning about a non-obvious consequence. The test, which is this wiki's own, is whether deleting the comment loses a fact that no name or line in the code contains.
- A stated contract on code with distant callers. No name or signature carries it, and a line of the body shows only what the code does now, so [[state-the-contract]] owns that comment.
- Code that cannot be made plain, such as a dense expression or a hand-tuned algorithm. *The Pragmatic Programmer* does not treat this case. *Code Complete* keeps exactly such a comment, the one naming the Newton-Raphson method over a square-root routine (p. 769). This wiki allows a how-comment there, preferably one naming the algorithm, once renaming and extraction have failed to make it clear.
- A summary comment heading a whole block is legitimate even once the code reads well (*Code Complete*, p. 780).
- Comments inside indented loops and conditionals are exempt from the advice on major and minor comments, because the indentation already shows the levels (p. 782).
- When a comment contradicts the code, it is not simply deleted. The mismatch suggests the code may be wrong too, so the intended behaviour is established first (p. 767).
- A project whose tooling requires a comment template. Project conventions decide that at work time.

## Repair

1. Rename the function and its parameters so they state the purpose, and rearrange the body so the steps read in order.
2. Delete the comment, or the part of it, that the code now states. If deleting it loses meaning, the name is still at fault.
3. Where a reason exists, write the reason: what was chosen, over what, and why.
4. Where a comment contradicts the code, find out which one is right before touching either.
5. For a comment written at implementation level, rewrite it to say what the step is for, in terms of the problem, and move literal values and call names out of it. If the intent cannot be stated, the step itself is not yet understood (*Code Complete*, pp. 216, 218).
6. Replace each literal the comment explains with a named constant or enumerator, and rename the variables the comment translates. Then phrase what remains as the name of a method. If the paragraph has one purpose, extract it under that name and delete the comment (pp. 778-779).
7. Where a method holds paragraphs at two levels of abstraction, extract the lower-level ones (pp. 781-782).
8. For a deliberate surprise or workaround, write the reason together with the plain alternative and the measured gain, or the defect being avoided (pp. 780-783).

The cost is that a why-comment takes knowledge of the decision, which the author of a later change may no longer have.

## Before and after

A comment that repeats the code, beside a delay that has no reason:

```
// before
// loop over the orders
for order in orders:
    // add the total to the sum
    sum += order.total
// wait 200 ms
sleep(200)
```

```
// after
for order in orders:
    sum += order.total
// gateway docs, rate limits: a second call inside 150 ms is rejected;
// polling was tried and dropped because it doubled the load
sleep(200)
```

A comment that repeats the body, covering for abbreviated names:

```
// before
// Compute the delivery charge.
// * Each parcel costs 4.
// * Orders over 30 kg pay a surcharge of 15.
// * Members pay half.
function chg(o):
    c = 4 * o.parcels
    if o.weight > 30:
        c = c + 15
    if o.member:
        c = c / 2
    return c
```

```
// after
function delivery_charge(order):
    charge = PARCEL_RATE * order.parcels
    if order.weight > HEAVY_ORDER_KG:
        charge = charge + HEAVY_SURCHARGE
    if order.member:
        charge = charge * MEMBER_SHARE
    return charge
```

A comment written at implementation level, rewritten at the level of intent:

```
// before
function loadSettings(path)
    // open file with openRead(), if handle == null return -2
    handle = openRead(path)
    if handle == null then return -2
    // d["timeout"] -> cfg.t
    cfg.t = parseJson(readAll(handle))["timeout"]
    return 0
```

```
// after
function loadSettings(path)
    // a missing settings file is reported to the caller, not defaulted
    handle = openRead(path)
    if handle == null then return LOAD_FAILED
    cfg.requestTimeout = parseJson(readAll(handle))["timeout"]
    return LOAD_OK
```

A comment that translates a coded value, after *Code Complete*, pp. 779-780:

```
// before
// if the account flag is zero
if account_flag == 0:
    open_account(customer)
```

```
// after
if account_type == AccountType.NEW:
    open_account(customer)
```

A workaround that reads as an arbitrary special case, after pp. 782-783:

```
// before
size = optimal_block_size(count, item_size)
if size == 500:
    size = 512
write_data(file, data, size)
```

```
// after
size = optimal_block_size(count, item_size)
// write_data() corrupts output when the block size is exactly
// WRITE_DATA_BROKEN_SIZE; any other size works
if size == WRITE_DATA_BROKEN_SIZE:
    size = WRITE_DATA_WORKAROUND_SIZE
write_data(file, data, size)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 211-213 for the style rules of pseudocode, the bad and good pair and the reasoning; pp. 216, 218 for intent that cannot be stated; p. 225 for documenting non-obvious dependencies and removing comments that restate a call. The implementation-level and restated-call signs, the blank-out test, the limits on how-comments and on calls, step 5 of the repair as worded and the third pair are this wiki's own.

[[code-complete]], ch. 32: section 32.3, p. 767, for the mismatch remark, made by a character in the dialogue whose view the narrator adopts; section 32.4, pp. 768-769, for the three mystery routines and the verdict that bad comments are worse than none; section 32.5, pp. 777-783, for commenting at the level of intent, the search-loop example, the method-name test, the preference for names because comments go stale faster, the why-not-how example, documenting surprises and workarounds, justifying style violations, and major and minor comments with logically flat methods. This wiki's own: the chapter-32 signs as worded, the reading of an ellipsis as a pointer to extraction, the named constants in the second pair, the boundary against [[rewrite-tricky-code]] and the other chapter-32 pages, the reading of the missing-reason sign as sourced, the order of repair steps 6-8, and the fourth and fifth pairs, including the value 512. The quotations from ch. 32 were transcribed from the extracted text and should be checked against the page image.

[[pragmatic-programmer]], Topic 7, p. 54, and Topic 9, pp. 64-65. The rule, the reason from DRY, the rejection of mechanical commenting, the list of what a comment should record and the view that comments cover for poor naming are the book's. The remark on stale comments, the reconciliation of p. 54 with p. 65, the signs, the separate treatment of the last sign, the assignments against neighbouring pages, the test for a comment the code cannot replace, the limits on contracts, dense code and project tooling, the documented limit as an example of an outside constraint, the order of the repair and the pseudocode are this wiki's own.
