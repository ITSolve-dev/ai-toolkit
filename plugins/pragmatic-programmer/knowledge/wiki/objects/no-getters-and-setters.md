---
title: No getters and setters
category: objects
summary: "A class whose public surface is getX()/setX(v) pairs over its private fields, with no method that works with those fields, is a data structure dressed as an object."
tags: [rule, encapsulation, data-structure, accessors, immutability]
paradigm: oop
sources: [elegant-objects, code-complete, object-oriented-thought-process, fowler-refactoring]
created: 2026-11-03
updated: 2026-11-07
---

Bugayenko's *Elegant Objects* (section 3.5) calls the getter/setter pair an anti-pattern of object-oriented code: a private field plus `getX()` and `setX()` turns a class back into a passive data structure, so the encapsulation the private field promised is not delivered. The book is deliberately radical here and disagrees with mainstream conventions (IDE-generated accessors, Ruby's `attr_reader`/`attr_writer`); this page states where its rule holds and where a project convention wins.

## Rule

The book's claims, paraphrased (pp. 172-179):

- An object and a data structure differ in what the caller does with them. A data structure is a transparent box: the caller reaches its field and works on the value (`cash.dollars`). An object is a black box: the caller asks it to do something (`cash.print()`) and does not know which fields exist (p. 173). See [[object-as-representative]].
- The reason is maintainability: every paradigm simplifies by narrowing what one has to understand at a time. Once objects pass bundles of bare data between each other, the code drifts back to procedures and statements manipulating that data, the procedural style OOP was meant to replace (pp. 174-177). The book's phrasing: data must never be left naked, «Никто не должен видеть их голыми или трогать их» (p. 176).
- Getters and setters are a disguise for that bare access. Adding validation or changing storage behind them does not matter, because from the caller's side they still look like points of access to data: «Независимо от способа реализации геттеры и сеттеры являются данными и представляют данные, а не поведение» (p. 178).
- The vicious part is the `get`/`set` prefix (p. 179). A method returning data is acceptable when it is named as the thing asked about: `dollars()` asks the object how many dollars it has, without assuming a field holds them; `getDollars()` says «Залезь в свои данные, найди там поле dollars и верни его значение» (p. 179).
- Setters go further than naming: the book's ideal is to drop them and make the object immutable (author's reply, p. 185; see [[immutable-objects]]). A commenter, Sagiri, says that in object terms one does not set a name or a size but renames or resizes (p. 182). The author, answering another commenter, draws the same line: «Кличку можно поменять, но устанавливать ее не стоит» (p. 183).

Fowler and Beck's chapter on smells in *Refactoring* names the shape **Data Class**: "classes that have fields, getting and setting methods for the fields, and nothing else", dumb data holders that other classes often manipulate in far too much detail (2nd ed., ch. 3, Data Class, PDF p. 97). Their reading is the same as this page's: "Data classes are often a sign of behavior in the wrong place" (PDF p. 97), so the progress comes from moving behaviour from the clients into the data class.

## Sign in code

- A class whose public methods are *only* accessors: each `getX()` returns field `x` and each `setX(v)` assigns it, and no method does work with the fields. This is the data-structure shape the book attacks.

This wiki assigns the neighbouring cases as follows. A class whose public methods are only accessors over its fields is [[no-getters-and-setters]]; [[tell-dont-ask]] keeps the call-site read followed by a write back, and comes first when both fire, and its repair (move the decision into the object) is also step 1 here. Methods that only return or set one field are not counted by [[fewer-than-five-public-methods]]. [[builder-and-manipulator-names]] takes a get-prefixed name only on a class that has behaviour of its own. A setter as a field reassigned after construction is [[immutable-objects]]. On a class whose public methods are only accessors, the setter itself is also reported on [[immutable-objects]]; an object built empty and completed by setters at the call site is [[temporal-coupling]]. A bare read or write of a public field is [[uniform-access]]. *Code Complete* offers an alternative repair for the same class (p. 152): where a search shows one class holds all the logic about its data, fold the fields into that class instead of moving behaviour into the data class; that repair is recorded on [[class-with-only-data-or-only-behaviour]], and this page still owns the finding. A class that does the other classes' work through their accessors is [[god-class]].

## When not to apply

The book gives no limits of its own; the author answers every objection by holding the line (DTOs: «Не делайте этого», p. 181). The limits below are this wiki's reading, setting by setting:

- **A framework or tool that requires the convention.** Serializers, ORMs, UI binding and bean introspection often locate properties by `get`/`set` names. Where the project depends on that, the project convention overrides the book. Keep such classes at the boundary and do not give them domain behaviour.
- **Plain data crossing a boundary**: a request/response record, a row, a message. Commenters raise forms with many fields (p. 181) and DTOs (p. 180); the book rejects them. This wiki resolves it per setting: a record whose only job is to carry data across a process or layer boundary may be a data structure; a class that is also given behaviour or is passed around the domain should not.
- **A language where accessors are the idiom for read-only properties** (properties, records). The prefix argument then has no surface form; the remaining question is the caller-side one on [[tell-dont-ask]].
- ***Code Complete* disagrees on accessor pairs.** McConnell holds a `Point` with `GetX()`/`SetX()` well encapsulated, because the caller cannot tell how the values are stored (p. 136). This wiki resolves it on [[uniform-access]]: accessors hide how a value is stored, not who may change it. Where the question is only stored versus computed, *Code Complete*'s reading holds; where the class is accessors and nothing else, this page's.
- **Weisfeld recommends accessors, for control.** *The Object-Oriented Thought Process* takes the side opposite to *Elegant Objects*: other objects reach a private attribute through `setName`/`getName` (p. 94), so the owner decides what happens, and another object has to ask: «Supervisor сам по себе не сможет извлечь информацию; ему придется запросить сведения у объекта Cabbie» (p. 95). His setters are usually there to ensure some level of integrity, as a `setAge()` that refuses 0 or less, and accessors to passwords or payroll data let the class apply validation (p. 95). He also presents getter/setter pairs and language properties as one mechanism of controlled access (pp. 29-30). This wiki resolves the two books by the setter's body. A setter that checks or refuses a value keeps an invariant of the class; it is an operation that happens to be named `set`, Weisfeld's argument holds for it, and what remains is only whether a domain name says more ([[access-routines-at-domain-level]]). A setter that only assigns, as his own `setName(iName) { name = iName; }` (p. 94), gives none of the integrity he argues for; all it keeps is one point every write passes, the debugging benefit on [[uniform-access]]. A class made of such pairs is this page's sign, and Weisfeld's argument does not defend it. Weisfeld himself does not separate the two cases. A plain setter on a field that a rule binds is [[class-invariant]], which owns that shape whatever the rest of the class looks like.
- **An immutable result record.** Fowler and Beck name one of the best exceptions to the Data Class smell: a record used as the result of a distinct function invocation, such as the intermediate data structure after Split Phase ([[split-phase]]). Its key property is that it is immutable, at least in practice, and "Immutable fields don’t need to be encapsulated"; information derived from immutable data can then be fields rather than getters (PDF p. 98). This wiki reads that as: a mutable data holder that other classes manipulate carries the sign, and an immutable record passed between phases does not.
- **Renaming alone fixes nothing.** Commenters note that `dog.weight()` is the same call as `dog.getWeight()` (Matt and bedobl, p. 185). This wiki agrees: dropping the prefix while callers keep doing the object's work with its data removes the word, not the problem.

## Repair

1. Look at what callers do with the getter's value. If they compute something the object could compute, move that computation into the object as a method named for its result (`total()`, `print()`), then delete the getter. See [[tell-dont-ask]].
2. If a value genuinely has to leave the object, keep the method but name it as the thing asked about (`dollars()`), not `getDollars()` (p. 179).
3. Replace a setter with either a constructor argument on an immutable object (a new instance carries the new value), or a domain verb describing the change (`rename(n)`), per [[immutable-objects]].
4. When many places must see a change to one shared object (the book's example: a brush whose colour sliders recolour three chickens at once, p. 185), the author's suggestion is a `Brushes` registry that returns the brush by its id; the pictures hold only the id and fetch the brush on demand. For a performance-critical reused object (Android `ListView`), the author would keep «неизменяемые объекты, но на основе изменяемого хранилища в памяти» (p. 186): immutable views over a mutable store, the immutable-but-not-constant kind on [[immutable-versus-constant-object]].

Their order for a data class (PDF p. 97): public fields first get Encapsulate Record "before anyone notices"; Remove Setting Method goes on any field that should not change; then find where other classes use the accessors and Move Function to bring that behaviour in, using Extract Function first where a whole function cannot move ([[move-function]]).

## Before and after

```
class Cash
  private dollars
  getDollars() -> return this.dollars
  setDollars(v) -> this.dollars = v

// caller does the object's work
cash.setDollars(cash.getDollars() * rate)
print("Cash value is " + cash.getDollars())
```

```
class Cash
  private final dollars
  Cash(dollars) -> this.dollars = dollars
  times(rate) -> return new Cash(this.dollars * rate)
  print() -> return "$" + this.dollars

print("Cash value is " + cash.times(rate).print())
```

The "before" is the shape of the book's opening example (p. 172) with a call site added by this wiki; it is not a framework-bound record, so the limits above do not exempt it. The "after" has no accessor and no setter, and is immutable.

## Source

- [[elegant-objects]], section 3.5, pp. 172-187: the object/data-structure distinction (p. 173), the maintainability argument (pp. 174-177), getters as data (p. 178), the prefix argument and `dollars()` vs `getDollars()` (p. 179), DTOs and forms in the comments (pp. 180-181), renaming versus setting (pp. 182-183), dropping setters and the `Brushes` registry (p. 185), immutable views over a mutable store (p. 186). The quotations from pp. 176, 183 and 186 were checked against the page images; the others are transcribed from a noisy OCR layer.
- This wiki's own: the sign as worded, the assignment of neighbouring cases, every item under *When not to apply*, repair step 1, the constructor-argument half of step 3, and the before/after pair (pseudocode).
- [[code-complete]], Russian edition, p. 152: demoting a data-only class into the classes that use it; p. 136: accessor pairs as good encapsulation. This wiki's own: the condition for choosing that repair, and the per-setting resolution of the p. 136 disagreement.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: pp. 29-30 (accessors and properties as controlled access), p. 94 (`setName`/`getName`), p. 95 (the `Supervisor` must ask the `Cabbie`, `setAge` refusing values of 0 or less, setters for integrity, validation of sensitive data). The quotation was checked against `raw/`. This wiki's own for that part: the resolution by the setter's body and the split with [[class-invariant]].

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Data Class", PDF pp. 97-98: the smell, behaviour in the wrong place, the order of repairs and the immutable result record. This wiki's own for that part: the selecting sentence between a mutable holder and an immutable record.
