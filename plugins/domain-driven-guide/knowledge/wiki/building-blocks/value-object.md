---
title: Value Object
category: building-blocks
summary: A domain object defined by its attributes rather than an identity; it measures/quantifies/describes a concept, is immutable, compared by value equality, side-effect-free, and replaced rather than mutated.
tags: [concept, pattern, value-object, immutability, value-equality, self-validation, building-blocks, ubiquitous-language, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-ddd-guide-2026, web-page-cosmic-python-book]
created: 2026-07-25
updated: 2026-07-26
---

A **Value Object** (Value) is a tactical DDD building block that models a domain concept by the
*attributes* it carries rather than by a unique identity. Where an [[entity]] is a *thing* with a thread
of continuity, a Value is a *description* of a thing. Money (100 roubles), a point's coordinates
`(x, y)`, an email address — you care *what it is*, not *which one* it is; two Values with the same
attributes are interchangeable ([[web-page-ddd-guide-2026]], raw L66–L70). Vernon argues Values are the
more important and more overlooked building block: "we should strive to model using Value Objects instead
of Entities wherever possible," and even an Entity's design "should be biased toward serving as a Value
container rather than a child Entity container" (raw L5176).

The advantage is concrete, not aesthetic: "Value types that measure, quantify, or describe things are
easier to create, test, use, optimize, and maintain" (raw L5174). A correctly designed Value "can be
created, handed off, and forgotten about" — a consumer cannot corrupt it — which Vernon likens to
"transitioning from a programming language without managed memory facilities to one with garbage
collection" (raw L5198). The canonical definition is Evans': "When you care only about the attributes of
an element of the model, classify it as a VALUE OBJECT. Make it express the meaning of the attributes it
conveys and give it related functionality. Treat the VALUE OBJECT as immutable. Don't give it any
identity and avoid the design complexities necessary to maintain ENTITIES" (raw L5202).

## The characteristics that identify a Value

Model a concept as a Value when it possesses **most** of these six characteristics (raw L5210), all
under the overarching requirement that the Value expresses the [[ubiquitous-language]]:

1. **Measures, quantifies, or describes** a thing in the domain. An age is not a thing; it quantifies
   how many years a person has lived. A name is not a thing; it describes what a person is called.
2. **Immutable** — unchangeable after construction (see below).
3. **Conceptual whole** — its related attributes form one integral measure; see [[whole-value]].
4. **Replaceable** — when the measurement changes, the whole Value is swapped for a new one, not mutated.
5. **Value equality** — two instances are equal when their types and all attributes are equal.
6. **Side-effect-free behavior** — its methods produce output without changing its state; see
   [[side-effect-free-function]].

Evans' rule of thumb, restated as a decision test: "Ask yourself if the concept you are designing must be
an Entity identified uniquely from all other objects or if it is sufficiently supported using Value
equality. If the concept itself doesn't require unique identity, model it as a Value Object" (raw L5415).
If analysis shows the object genuinely must be mutated by its own behavior and cannot use replacement,
that is the signal it should be an [[entity]] instead (raw L5274).

## Immutability, in practice

Instantiation alone does not make an object immutable — "none of its methods, whether public or hidden,
will from that time forward cause its state to change" (raw L5266). Vernon's discipline for guaranteeing
this:

- **All setters are private.** Consumers cannot mutate attributes.
- **Only constructors self-delegate to setters.** "Only the primary constructor(s) use self-delegation
  to set properties/attributes. No other methods shall self-delegate to setter methods" (raw L5854).
- **State is initialized atomically in the constructor** — never built up piece by piece after
  construction (raw L5346); see [[whole-value]].
- Setters can still carry **guard Assertions** (e.g. reject `null`), giving a single well-placed
  validation point even though the setter runs once in the Value's life (raw L5970).

A Value may hold a reference to another Value freely. Holding a reference to an [[entity]] is riskier:
when that Entity changes state, the "immutable" Value effectively changes too. Such references should
exist only "for the sake of compositional immutability, expressiveness, and convenience," not to mutate
the Entity through the Value's interface (raw L5268).

## Worked example — an `Email` value object

Its defining power in practice is **self-validation**: a Value checks its own validity on construction
and refuses to come into existence in an invalid state. All the validation and comparison logic for that
concept lives in **one place**, so the surrounding [[entity]] can hold a well-typed Value instead of a
raw primitive and "garbage" can never get in — the direct antidote to the [[anemic-domain-model]], where
such logic leaks out into service code operating on bare strings ([[web-page-ddd-guide-2026]], raw
L72–L108):

```java
package ru.otus.dddexample.sharedkernel;
public class Email {
    private final String value;
    public Email(String value) {
        if (value == null || !value.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new IllegalArgumentException("Некорректный email: " + value);
        }
        this.value = value;
    }
    public String getValue() { return value; }
    @Override public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Email email = (Email) o;
        return Objects.equals(value, email.value);
    }
    @Override public int hashCode() { return Objects.hash(value); }
}
```

Three properties make it a Value: the field is **`final`** (immutable), the constructor **rejects** any
invalid string, and `equals`/`hashCode` are computed **from the value**, not from an identifier. The
guide places `Email` in a `sharedkernel` package — a Value like `Money` or `Email` is a natural candidate
for a [[shared-kernel]] between contexts, though sharing across a [[bounded-context]] edge is itself a
deliberate coupling decision.

## Value equality

Equality compares the concrete type and then every attribute; two Values of the same type with equal
attributes are equal even though they are distinct objects. A correct `equals()` eliminates `null`,
checks `getClass() == anObject.getClass()`, then compares each property, with a matching `hashCode()`
("all Values that are equal also produce equal hash code values") (raw L5942). Value equality plus
immutability is exactly what makes a Value suitable as an [[aggregate]] unique identity: the identity is
named per the Ubiquitous Language, holds all identifying attributes as a conceptual whole, and never
needs replacement (raw L5411) — see [[entity-identity-generation]].

## Testing: the copy-constructor immutability check

Vernon supplies a second **copy constructor** on each Value specifically to test immutability. The test
creates an instance and an equal copy, asserts they are equal, exercises a side-effect-free method, then
asserts the original and copy are *still* equal — proving the method mutated nothing (raw L5858). Such
tests double as domain documentation: "If we were writing a user's manual for the model, we would provide
these tests as the most appropriate code samples for how clients should use this specific domain object"
(raw L5630), and "Your model tests should have meaning to your domain experts" (raw L5815).

Methods should be named fluently, not with JavaBean `get` prefixes — `valuePercentage()` not
`getValuePercentage()` — so the interface stays faithful to the Ubiquitous Language (raw L5896). If
tooling forces getters, still never expose public setters, which would break immutability (raw L5906).

## Value as Strategy

A Value type can also serve as a **Strategy/Policy**: Vernon's `BusinessPriority` holds a
`BusinessPriorityRatings` and exposes side-effect-free calculation methods (`costPercentage`,
`priority`, `totalValue`) that take a `BusinessPriorityTotals` Value as parameter — encapsulating a
business-priority calculation policy that could later be swapped for alternatives (raw L5825).

## Failure mode: is everything a Value Object?

After internalizing this, the risk flips from entity-think to over-wrapping. Vernon's caution: a truly
simple, self-contained attribute (a Boolean, a lone numeric with no related attributes and no special
behavior) is already a meaningful whole and needs no wrapper — "you could certainly make the 'mistake' of
unnecessarily wrapping a single attribute in a Value type with no special functionality and be better off
than those who never give Value design a nod" (raw L5501). Over-wrapping is cheaply refactored; chronic
entity-think — modeling a Value as an [[entity]] because storage gives it a primary key — is not; see
[[data-model-leakage]].

## Value object vs. entity — the fork

The distinction is the identity question, and it is the fork that decides which building block to reach
for — see [[entity]], which *does* have an identifier that persists across changes. A Value has none:
change any attribute and it is simply a different value.

## The Cosmic Python view — frozen dataclasses and value equality

*Architecture Patterns with Python* states the trigger crisply: "Whenever we have a business concept that
has data but no identity, we often choose to represent it using the *Value Object* pattern" — "any domain
object that is uniquely identified by the data it holds; we usually make them immutable" (raw L787-790).
Its identity test: an order carries a unique *reference*, "but a *line* does not," so an `OrderLine` is a
value object identified by the tuple `(orderid, sku, qty)` — "if we change one of those values, we now
have a new line" (raw L858). Value equality follows real-world intuition: "It doesn't matter *which* £10
note we're talking about, because they all have the same value" (raw L820).

In Python the pattern is a frozen dataclass (or `NamedTuple`), which grants value equality and hashing
for free — "the hash should be based on all the value attributes, and we should ensure that the objects
are immutable. We get this for free by specifying `@frozen=True` on the dataclass" (raw L915):

```python
@dataclass(frozen=True)
class Money:
    currency: str
    value: int
    def __add__(self, other) -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value + other.value)
```

A value object is not a dumb data bag — "it's common to support operations on values; for example,
mathematical operators" (raw L824) — but each operation returns a *new* instance (`fiver + fiver ==
tenner`) rather than mutating in place, and a domain rule is baked into the type (adding different
currencies is an error; multiplying two `Money` values raises `TypeError` because that operation is
meaningless in the domain). This is the same immutable, replace-don't-mutate,
[[side-effect-free-function|side-effect-free]] discipline Vernon describes above — reached via Python's
`frozen=True` instead of private setters.

## Related

- [[whole-value]] — the conceptual-whole characteristic in depth.
- [[side-effect-free-function]] — the behavioral characteristic.
- [[standard-type]] — descriptive Values that indicate the type of a thing.
- [[value-objects-for-integration]] — using Values to model cross-[[bounded-context]] integration.
- [[data-model-leakage]] — the anti-pattern that pushes designers toward Entities.
- [[value-object-persistence]] — persisting Values with their owning [[aggregate]].
- [[entity]] — the counterpart building block; the two together compose an [[aggregate]].
- [[anemic-domain-model]] — what a self-validating Value helps you avoid.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-ddd-guide-2026]], [[web-page-cosmic-python-book]] — source summaries.
