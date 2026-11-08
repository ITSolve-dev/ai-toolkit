---
title: Keep interfaces small; put derived convenience methods in a smart class
category: objects
summary: "An interface declares a method that every implementation can compute from another method of the same interface (an overload filling a default argument, a shortcut for a fixed value), so each implementer must rewrite the same convenience logic."
tags: [rule, interfaces, cohesion, duplication, single-responsibility]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

*Elegant Objects* holds that keeping interfaces small matters even more than keeping classes small, because a class may implement several interfaces: two interfaces of five methods each force ten methods on a class that implements both (p. 109). An interface is a contract that every implementing class must honour; the more it demands, the more it pushes implementers toward low cohesion. The book's repair for convenience operations is a **smart class**: a class shipped inside the interface that wraps any implementation and adds methods built only on the interface's own methods (pp. 109-111).

## Rule

An interface declares only what an implementation uniquely has to do. This wiki generalises the book's example to: a method that can be written in terms of the interface's other methods does not belong in it. Put such methods in a smart class shipped with the interface (`Exchange.Smart`), which takes the interface as a constructor argument and knows nothing about how any implementation works (pp. 109-110).

The book's example: an exchange interface with `rate(source, target)` and `rate(target)`, where the second fills in US dollars as the default source. Computing a rate and substituting a default currency are two different functions, so the one-argument method should not be in the interface (p. 109). Fetching rates from a stock exchange is the unique work of one implementation; substituting the default currency can be shared by all of them, and requiring it of each implementer duplicates it (p. 109). As further shortcuts are needed (`eurToUsd()`), the smart class grows while the interface stays at one method, implemented by every rate source (pp. 110-111). The network-calling implementation should do network calls «и на этом все» (p. 111).

## Sign in code

- An interface method whose body in every implementation in the code in view is a call to another method of the same interface, with a constant or a default argument filled in.
- Several implementations of one interface contain the same few lines for the same convenience method.
- An overload in an interface that differs only by omitting an argument that has a default.

This wiki assigns the neighbouring cases as follows. This page owns a derivable method declared in an interface. The number of public methods on a class is [[fewer-than-five-public-methods]]. A public method that implements no interface is [[public-methods-implement-interfaces]], which exempts the smart class itself.

## When not to apply

- **The method is not derivable.** If an implementation can do the operation substantially better than by composing the other methods (a batch fetch that saves round trips), it is part of what implementers uniquely do. This limit is this wiki's own; in that case it is a decorator's or the interface's job, not a smart class's.
- **Default methods in the interface instead.** Readers proposed default (interface-provided) methods; the author prefers smart classes because there can be several smart classes, while default methods are locked into one interface (p. 113). Another reader proposed default methods because, unlike smart classes, they let an implementer override them (p. 113). This wiki resolves it per setting: where the language supports default methods and the project's convention uses them, and there is one obvious set of shortcuts, default methods meet the rule's aim (implementers do not rewrite shared logic); a smart class is the choice when there are several unrelated groups of shortcuts, or when implementers must not be able to override them.

## Repair

1. Remove the derivable method from the interface.
2. Create a final smart class next to the interface (the book nests it inside) that holds an instance of the interface and implements the removed method via the remaining ones.
3. Delete the duplicated bodies from every implementation.
4. At call sites, wrap: `Smart(impl).shortcut()`.

The book's discriminating criterion between a smart class and a decorator (p. 111): a smart class *adds* methods to an object; a decorator *strengthens* existing methods, implementing the same interface and overriding them (see [[composable-decorators]]). A class can be both: the book's `Exchange.Fast` overrides `rate()` to skip the remote call when source and target are equal, and also adds `toUsd()` (pp. 111-112).

**Smart classes are not ideal objects.** A reader pointed out that a smart class has public methods that implement no interface, which breaks the book's own rule that every public method implements an interface; the author agreed and said smart classes are auxiliary tools for building good objects, so that rule does not apply to them (p. 113). This wiki reads this as: the smart class is the place where such methods are tolerated, and nowhere else. This is a limit of [[public-methods-implement-interfaces]], not of this page.

## Before and after

```
// before: every rate source must also implement the default-currency shortcut
interface Rates
  rate(from, to)
  rate(to)                  // = rate("USD", to) in every implementation

class BankRates implements Rates
  rate(from, to) = http.get(...)
  rate(to)       = rate("USD", to)
class FileRates implements Rates
  rate(from, to) = file.lookup(...)
  rate(to)       = rate("USD", to)
```

```
// after: one-method contract; shared shortcuts live in a smart class
interface Rates
  rate(from, to)
  final class Smart
    Smart(origin: Rates)
    fromUsd(to)  = origin.rate("USD", to)
    usdToEur()   = fromUsd("EUR")

class BankRates implements Rates
  rate(from, to) = http.get(...)

r = Rates.Smart(BankRates()).fromUsd("EUR")
```

## Source

- [[elegant-objects]], section 2.9, pp. 109-113: the rule and its reasoning, the exchange example, the smart class, the smart-versus-decorator distinction and `Exchange.Fast`, the author's replies on the `@Override` rule and on default methods. The quotation of p. 111 was checked against the page image.
- This wiki's own: the signs, the assignment of neighbouring cases, the non-derivable limit, the per-setting resolution of smart classes versus default methods, and the pseudocode.
- Related: [[prefer-fakes-over-mocks]] (the fake is the other class the book ships nested in an interface).
