---
title: Be either final or abstract
category: objects
summary: "A subclass overrides a method that its parent, concrete or abstract, implements and does not mark final, typically one the parent's other methods call, so the parent's method changes behaviour without its code changing; also a class with a subclass, overridable methods its own methods call, and no documented inheritance policy."
tags: [rule, inheritance, overriding, composition, decorator, design-for-extension]
paradigm: oop
sources: [elegant-objects, code-complete]
created: 2026-11-03
updated: 2026-11-07
---

The book does not blame inheritance itself for tangled hierarchies. It blames virtual methods (p. 230). Its example is a `Document` whose `length()` returns `content().length`. A subclass `EncryptedDocument` overrides `content()` to decrypt, and `length()` silently starts returning the decrypted size instead of the size on disk, although nobody touched `length()` (pp. 230-231). To understand `length()`, a reader of the parent must remember that some of the methods it calls live in children. The book calls this upside-down reading counter-intuitive, because inheritance is expected to run from parent to child (p. 232).

## Rule

Make every class either final or abstract: «Просто делайте свои классы и методы либо константными, либо абстрактными» (p. 232). ("Константный" is the translation's word for `final`.) A final class is a black box that nobody can change by inheritance. An abstract class is an unfinished box with some parts missing, and its implemented methods are final. The third state, concrete and open, is the one the book opposes: the class assumes it is whole while others may replace its parts (pp. 232-233).

Inheritance stays, but only to **refine** behaviour, never to **extend** it: «Не расширить, а уточнить.» (p. 234). Refining makes an incompletely defined behaviour fully defined, as when a subclass supplies an abstract method. Extending adds to or changes behaviour that already exists, which the book calls an intrusion: «Расширение класса есть вторжение.» (p. 235).

*Code Complete* reaches a milder form of the same rule. McConnell quotes Bloch: design and document classes for inheritance, or prohibit it (p. 141). His reason is that inheritance adds complexity to a program and is dangerous in that sense (p. 141). A class decided not to support inheritance should not declare its members overridable; in Java, its members are declared final (p. 141). The chapter checklist asks whether the class documentation describes the inheritance strategy (p. 154). This wiki reads the two books as agreeing on the closed class and differing on the open one: *Elegant Objects* allows only abstract override points, while *Code Complete* also allows an overridable method with a default implementation (p. 142) provided the class documents it.

## Sign in code

- A class that is neither final nor abstract has a method that calls another of its own implemented, overridable methods, and some subclass overrides the callee.
- More broadly, a subclass overrides a method that its parent implements and does not mark final, whether the parent is concrete or abstract (p. 233).
- *Code Complete*'s sign, as this wiki reads it: a class with at least one subclass in the code at hand, whose overridable methods (by default or by marker) are called by its own other methods, and whose documentation says nothing about which may be overridden or what an override must keep.

This wiki assigns the neighbouring cases as follows. This page owns a subclass that overrides a method the parent implements with a body that does something. An override left empty, or returning only a neutral value, is [[override-that-does-nothing]]; one that throws "not supported", narrows the inputs the base method accepts, changes what the result means, or does something other than what the inherited method's name says is [[liskov-substitution-principle]]. [[inheritance-tax]] owns a subclass that reuses a concrete parent by reading its fields or calling its methods without overriding them, or whose callers invoke, through it, methods declared only in a concrete parent. A final subclass that only supplies the abstract methods of an abstract parent whose implemented methods are final is refinement. [[final-or-abstract]] accepts it and [[inheritance-tax]] does not fire on it. A subclass that does both earns findings on both pages, with this page's repair applied first. Whether the `extends` should stay at all is asked on [[choose-an-alternative-to-inheritance]].

## When not to apply

The book names refinement of an abstract class as the legitimate use (pp. 234-235). The other limits are this wiki's own.

- **Tools that need open classes.** Some mocking libraries, persistence proxies and frameworks subclass at run time and fail on final classes. The project's convention then overrides the `final` keyword, but not the ban on overriding implemented methods by hand.
- **A parent designed for extension**, whose override points are abstract and all other methods final. That is refinement, which the book accepts.
- **The language root class's protocol methods.** Overriding the language root class's protocol methods (equality, hashing, string form) is not this sign; it is how the language asks for them.
- **The two books disagree on documented override points.** This wiki resolves it per setting: in a project that follows *Elegant Objects* conventions, an overridable method with a default implementation is still the sign; elsewhere, a default override point whose documentation states what an override must preserve and when the base calls it meets *Code Complete*'s rule and is not a finding.
- **Closed by default.** This wiki adds: where the language makes methods non-overridable by default, an undocumented class is already closed, and the documentation half of *Code Complete*'s rule applies only to the members marked overridable.

## Repair

Two repairs, chosen by whether the parent has a meaningful default. The rule for choosing is this wiki's own.

1. **The parent's version is a complete object in its own right:** extract an interface, rename the class to a default implementation and mark it final. Rebuild the subclass as a final decorator that holds an instance of the interface and forwards to it (pp. 233-234). See [[composable-decorators]] and [[public-methods-implement-interfaces]].
2. **The parent's version is incomplete without a part:** make the parent abstract, declare the varying method abstract, mark the shared method final, and write each variant as a final subclass that supplies only the abstract method (pp. 235-236).

For *Code Complete*'s sign, either mark the class or its members closed, or document per overridable method what an override must preserve and when the base calls it (pp. 141, 154).

In the book's example, the decorator also fixes the behaviour. `length()` forwards to the plain document and returns the size in storage again (p. 234).

Trade-offs, as this wiki states them: the composition route needs an interface and a forwarding method for each operation the wrapper does not change, as `EncryptedDocument.length()` forwards to the wrapped document (p. 234). The refinement route keeps the ambiguity of `length()` meaning the decrypted size. The book accepts that, because both subclasses now visibly refine the same abstract method (pp. 236-237).

In a language where classes are closed by default, this wiki reads the sign as an explicit `open` or `virtual` on an implemented method.

## Before and after

```
# before
class Document:
    method length():
        return size_of(this.content())
    method content():
        return read_bytes_from_disk()

class EncryptedDocument extends Document:
    override method content():
        return decrypt(read_bytes_from_disk())
```

```
# after: composition
interface Document:
    length()
    content()

final class DiskDocument implements Document:
    method length(): return size_of(this.content())
    method content(): return read_bytes_from_disk()

final class EncryptedDocument implements Document:
    field plain: Document
    method length(): return this.plain.length()
    method content(): return decrypt(this.plain.content())
```

```
# after: refinement
abstract class Document:
    abstract method content()
    final method length(): return size_of(this.content())

final class DiskDocument extends Document:
    method content(): return read_bytes_from_disk()

final class EncryptedDocument extends Document:
    method content(): return decrypt(read_bytes_from_disk())
```

## Source

- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, section 4.3, pp. 230-237. Summary page: [[elegant-objects]].
- The quotations are OCR text and have not been checked against the page image.
- This wiki's own parts are: the signs as worded; the condition dividing this page from [[inheritance-tax]]; the limits for tools, designed-for-extension parents and root-class protocol methods; the trade-offs paragraph and the closed-by-default reading; and the rule for choosing between the two repairs.
- McConnell, *Code Complete*, 2nd edition, Russian edition, p. 141 (Bloch's rule and the reason), p. 142 (kinds of inherited methods), p. 154 (checklist). Summary page: [[code-complete]]. This wiki's own: the reading of the sign, the per-setting resolution between the two books, the closed-by-default limit, and the documentation wording of the repair.
