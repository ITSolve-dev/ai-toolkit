---
title: Entity
category: building-blocks
summary: A domain object modelled for its unique identity and continuity through change rather than its attributes; it stays the same thing even as its state churns, and owns only the data and logic tied to that identity and lifecycle.
tags: [concept, pattern, entity, identity, lifecycle, building-blocks, ubiquitous-language, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-ddd-guide-2026, web-page-cosmic-python-book]
created: 2026-07-25
updated: 2026-07-26
---

An **Entity** is a domain object modelled for its **individual identity** and **continuity through
change**, not for its attributes. You reach for an Entity when distinguishing one instance from every
other is a mandatory constraint, and the thing must be tracked as "the same thing" even as its state
changes across a long life.

> "We design a domain concept as an Entity when we care about its individuality, when distinguishing
> it from all other objects in a system is a mandatory constraint. An Entity is a unique thing and is
> capable of being changed continuously over a long period of time." (raw L3833)

A user may change their name yet remains the same user, because the identity is carried by an ID, not
by any attribute (raw L110–L114, [[web-page-ddd-guide-2026]]).

## Entity vs Value Object — the fork

Two characteristics separate an Entity from a [[value-object]]: **unique identity** and
**mutability**. "It is the unique identity and mutability characteristics that set Entities apart from
Value Objects." (raw L3835) A Value is defined by its attributes and is immutable — you replace it
wholesale when it must "change"; an Entity keeps its identity while its attributes churn. The
discriminating test during modelling is the word *change*: if a person's telephone number changing
does not warrant replacing the whole object, that object is an Entity, not a Value (raw L4582).

| | **[[entity]]** | **[[value-object]]** |
|---|---|---|
| Defined by | a persistent identifier | its attributes |
| Equality | same ID = same thing | same attributes = same thing |
| Mutability | attributes change, identity endures | immutable; a change is a new value |
| Example | `User`, `Order` | `Email`, `Money`, a coordinate |

Evans' guidance: "When an object is distinguished by its identity, rather than its attributes, make
this primary to its definition in the model. Keep the class definition simple and focused on life
cycle continuity and identity." (raw L3857)

## When NOT to use an Entity (and when not to use DDD)

Misappropriating Entities "happens far more often than many are aware" (raw L3837) — often a concept
should be a Value. And sometimes the whole domain does not warrant DDD at all:

> "Often a concept should be modeled as a Value. If this is a disagreeable notion, it might be that
> DDD doesn't fit your business needs." (raw L3837)

When CRUD genuinely fits, frameworks like Grails or Rails save time and money (raw L3839). The trap is
applying CRUD to complex domains that "deserve the precision of DDD," where "CRUD systems can't
produce a refined business model by only capturing data" (raw L3853). The failure that results when
data-thinking wins *inside* a DDD project is the [[anemic-domain-model]]. See [[when-to-use-ddd]] for
the decision.

## Discovering Entities from the Ubiquitous Language

Entities are driven out of the [[ubiquitous-language]], not from database tables. Two linguistic cues
signal an Entity (raw L4416):

- **Change** — different forms of the word *change* in the requirements point to a mutable thing with
  continuity. "As soon as they saw/heard different forms of the word change used, they were pretty
  sure that they were dealing with at least one Entity."
- **Search / match** — a need to *find one among many* implies unique identity: "If you have a bunch
  of things, and one of the things needs to be found out of many, you need unique identity to
  distinguish the one from all others."

Focus first only on the **intrinsic characteristics** — the attributes that identify it or are used
to find/match it — and defer everything else: "strip the Entity object's definition down to the most
intrinsic characteristics… Add only behavior that is essential to the concept" (raw L3865). The
discipline the guide stresses is **cohesion around identity**: an entity should hold *only* the data
and logic that belong to its identity and lifecycle — "don't mix everything into one heap."

## Behaviour: Intention-Revealing Interfaces over setters

Model behaviour in the words of domain experts. Prefer `activate()` / `deactivate()` over
`setActive(boolean)` — an **Intention-Revealing Interface** that matches the Language (raw L4505).
Public setters "should be used only when the Language allows for them, and usually only when you won't
have to use multiple setters to fulfill a single request" (raw L4501); multiple setters make intent
ambiguous and complicate publishing a single meaningful [[domain-event]] as the outcome of one logical
command. Keeping that logic *on* the entity, rather than in a service mutating a bag of setters, is
what keeps the model out of the [[anemic-domain-model]] trap.

## Construction

A newly instantiated Entity's constructor should capture enough state to fully identify it and make it
findable (raw L4742) — the unique identity itself coming from one of four
[[entity-identity-generation|identity-generation strategies]]. If the Entity holds an **invariant** — "a
state that must stay transactionally consistent throughout the Entity life cycle" (raw L4744) — the state
satisfying it must arrive through constructor parameters. The constructor delegates to
**self-encapsulating** setters, each asserting its own guard (non-null, etc.), so no path can leave the
object in an insane state (raw L4802); these guards are the first of the three levels covered in
[[entity-validation]]. Complex instantiation belongs in a **Factory**; in Vernon's example the `User`
constructor is `protected` and reachable only via `Tenant.registerUser(...)`, making the owning
[[aggregate]] root a factory that guarantees the `TenantId` on both `User` and `Person` is always correct
(raw L4804).

An ORM may impose its own primary-key identity distinct from the domain identity above; that second,
hidden identity is a [[surrogate-identity]]. And when one Entity must present different faces to
different use cases or clients, model that with [[object-roles]] rather than blending everything into one
interface.

## Change tracking

By definition an Entity need not track its own change history — only support continuously changing
state (raw L5138). When domain experts care about occurrences over time, the practical mechanism is
[[domain-event]]s plus an Event Store: publish a distinct event per state-altering command and save
each to the store. When the technical team (not domain experts) needs the full history in order to
*reconstruct* the Entity's state, that is [[event-sourcing]] (raw L5142).

## Entities inside an aggregate

An entity rarely stands alone. It is composed with value objects and, often, with other entities into
an [[aggregate]] — a consistency boundary with one entity as its root. The `Order` / `OrderItem`
example on [[aggregate]] shows an entity (`Order`) acting as the aggregate root that guards the whole
cluster's invariants.

## The Cosmic Python view — identity equality and the `Batch` entity

*Architecture Patterns with Python* gives the same building block a sharp Python treatment: "We use the
term *entity* to describe a domain object that has long-lived identity" (raw L864). Its distinguishing
behavior is **identity equality**: "Entities, unlike values, have *identity equality*. We can change
their values, and they are still recognizably the same thing" (raw L890-891). The human example makes it
vivid — a `Name` is a [[value-object]] (change a letter and `Harry Percival` becomes a *different* name),
but a *person* who changes their name is still the same person, because "humans, unlike names, have a
persistent *identity*" (raw L877). Entities usually get an explicit `__eq__`/`__hash__` keyed on the
identity attribute, not the data:

```python
class Batch:
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference
    def __hash__(self):
        return hash(self.reference)
```

**Hashing is the tricky part.** "For entities, the simplest option is to say that the hash is `None`,
meaning that the object is not hashable and cannot, for example, be used in a set" (raw L919). If you do
need set/dict membership, base the hash only on the (read-only) attribute that defines identity over
time, and heed the firm rule shared with value objects: "you shouldn't modify `__hash__` without also
modifying `__eq__`" (raw L926).

**Behavior lives on the entity.** The `Batch` evolves from a naive integer counter into one that tracks
which lines it has allocated, so it can enforce its own rules — using a `set` for `_allocations` makes
allocation idempotent for free (allocating the same line twice leaves `available_quantity` unchanged):

```python
class Batch:
    def allocate(self, line):
        if self.can_allocate(line):
            self._allocations.add(line)
    def deallocate(self, line):
        if line in self._allocations:
            self._allocations.remove(line)
    @property
    def available_quantity(self):
        return self._purchased_quantity - self.allocated_quantity
    def can_allocate(self, line) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
```

Even so, in the simplest version "both `allocate()` and `deallocate()` can fail silently" (raw L749) — a
reminder that guarding invariants inside an entity still needs deliberate error signaling (see
[[domain-exception]]). Stripping this behavior out into services instead produces the
[[anemic-domain-model]].

## Related

- [[value-object]] — the identity-free counterpart; the two together compose an [[aggregate]].
- [[aggregate]] — how entities and value objects are clustered behind a consistency boundary.
- [[entity-vs-aggregate]] — the head-to-head distinction: an aggregate root is an entity, but not every entity is an aggregate.
- [[entity-identity-generation]] — the four strategies for creating an Entity's unique identity.
- [[surrogate-identity]] — the second, ORM-only identity kept hidden from the domain.
- [[entity-validation]] — the three levels of validation kept out of the Entity itself.
- [[object-roles]] — presenting one Entity as different faces per use case.
- [[ubiquitous-language]] — the source of the linguistic cues (*change*, *search*) that reveal
  Entities.
- [[anemic-domain-model]] — the trap avoided by keeping behaviour on the entity.
- [[event-sourcing]] — full-history reconstruction of an Entity's state.
- [[domain-exception]] — how an entity signals a broken invariant instead of failing silently.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-ddd-guide-2026]], [[web-page-cosmic-python-book]] — source summaries.
