---
title: Anemic Domain Model
category: anti-patterns
summary: A domain model in name only — objects that expose data via getters/setters but hold no behaviour, so business logic leaks into procedural service code; you pay a domain model's full cost and get none of its benefit.
tags: [anti-pattern, failure-mode, anemic-domain-model, domain-model, transaction-script, service-layer, domain-service, mini-layer, layering]
sources: [book-implementing-ddd-vaughn-vernon, web-page-bliki-anemic-domain-model, web-page-ddd-guide-2026]
created: 2026-07-25
updated: 2026-07-26
---

The **Anemic Domain Model** is a domain model in name only: its objects *look* like a real model —
named after the domain's nouns, wired together with rich relationships — but they carry hardly any
behaviour. They are "little more than bags of getters and setters," and the business logic ends up in
procedural code elsewhere (typically an [[application-service]] shaped like a Transaction Script). The
term was coined by Martin Fowler in 2003 (in conversation with Eric Evans) and "it wasn't meant to be
a complimentary term" (raw L946) — yet the pattern is widespread and often mistaken for healthy
design.

> "The catch comes when you look at the behavior, and you realize that there is hardly any behavior on
> these objects… there are a set of service objects which capture all the domain logic… These
> services live on top of the domain model and use the domain model for data."
> — [[web-page-bliki-anemic-domain-model]] (raw L22)

## Why it is an anti-pattern

It is **procedural design wearing an object-oriented costume.** It contradicts the basic idea of OO —
combining data and process in the same place — and fools people into thinking these data-holders are
real objects. (raw L24)

The decisive argument is cost/benefit:

> "an Anemic Domain Model is a bad thing because you pay most of the high cost of developing a domain
> model, but you get little or none of the benefit." (raw L962)

- **The cost you pay anyway:** because of object-relational impedance mismatch you still spend heavily
  mapping objects to and from storage — a whole O/R mapping layer. That cost is only worthwhile *if*
  you use OO to organise complex logic.
- **The benefit you throw away:** by pulling all behaviour out into services you end up with
  Transaction Scripts in all but name. What you actually have "is not a domain model at all, but just
  a data model projected from a relational model (or other database) into objects" — an impostor
  closer to **Active Record** (raw L962).

The symptom that reveals it: "the more behavior you find in the services, the more likely you are to
be robbing yourself of the benefits of a domain model. If all your logic is in services, you've robbed
yourself blind." (raw L67, [[web-page-bliki-anemic-domain-model]])

## Why anemia happens

Not mainly a procedural mindset, but industry habit (raw L964–986):

- **Sample-code following.** Tutorials demonstrate an API "in the simplest possible way, without
  concern for good design principles" — getters-and-setters classes copied "without a second thought
  about design."
- **A getter/setter lineage.** Visual Basic property sheets → the JavaBean standard → frameworks
  adopting it wholesale. Early **Hibernate**, introduced to persist domain models, "had to expose
  public getters and setters for every persistent simple attribute and complex association" (raw
  L978), so even developers who wanted behaviour-rich objects had to expose internals. Web frameworks
  and form binding reinforced the same expectation.

The result is "anemia everywhere" (raw L986). Historical caveat: modern ORMs (Hibernate included) now
support hidden accessors and direct field access, so persistence no longer *forces* anemia (raw L982).

Vernon's Chapter 5 names a further, upstream cause: **data-thinking over domain-thinking.** "There is a
tendency for developers to focus on data rather than the domain… Instead of designing domain concepts
with rich behaviors, we might think primarily about the attributes (columns) and associations (foreign
keys) of the data" (raw L3815); code-generation tools then reflect the data model straight into
accessor-laden objects. SaaSOvation's CollabOvation team "got caught in the trap of doing a lot of
entity-relationship (ER) modeling in Java code," over-focusing on tables and columns, which "led to a
largely Anemic Domain Model composed of a lot of getters and setters" (raw L4392). This is the same
data-first mindset that drives the sibling anti-pattern [[data-model-leakage]] — there the data model
wrongly dictates *which building block* to use; here it wrongly drains the model of *behaviour*. And for
genuinely simple domains a plain CRUD approach is cheaper and correct; the failure is applying it to
complex domains that "deserve the precision of DDD," where "CRUD systems can't produce a refined business
model by only capturing data" (raw L3853).

## Another cause: overusing Domain Services

Vernon's Chapter 7 names a further, active cause distinct from industry habit — treating the
[[domain-service]] as a modeling silver bullet. Behaviour that truly belongs on an [[entity]] or
[[value-object]] gets promoted to a Service instead, and the model hollows out: "Don't lean too
heavily toward modeling a domain concept as a Service... Using Services overzealously will usually
result in the negative consequences of creating an Anemic Domain Model" (raw L6443). This is why the
deliberate caution *"Make Sure You Need a Service"* exists — recognizing a *legitimate* need for a
Service is what keeps the model rich (raw L6969–6971). The chapter's wrap-up restates it plainly:
"overuse of Domain Services leads to Anemic Domain Model, an anti-pattern" (raw L6971).

**The mini-layer trap.** A specific slippery slope is building a "'mini-layer' of Domain Services
above the rest of your domain model Entities and Value Objects... this will often lead down the
precarious path of Anemic Domain Model, which should be considered an anti-pattern" (raw L6835).

**When a mini-layer is NOT anemic.** The verdict is contextual, not absolute: "there are some
systems where designing in the mini-layer of Domain Services makes more sense than in others and
will not lead to Anemic Domain Model. It depends on the characteristics of the domain model, and in
the case of the *Identity and Access Context* this is actually quite helpful" (raw L6837). What keeps
even a mini-layer healthy is that its Domain Services still hold genuine business logic and "are
always different from Application Services in the Application Layer. Address transactions and security
as application concerns in Application Services, not in Domain Services" (raw L6839). Contrast that
with the separate `domain.service` package warned about in [[module-naming-conventions]], which
"can quickly lead to Anemic Domain Model" when it becomes a place to drain behaviour into.

## Anemia-induced memory loss

Vernon's worked example is a versatile `saveCustomer(...)` service that takes a dozen string parameters
and pushes them through setters onto a `Customer` DAO:

```java
@Transactional
public void saveCustomer(String customerId, String firstName, ... ) {
    Customer customer = customerDao.readCustomer(customerId);
    if (customer == null) { customer = new Customer();
                            customer.setCustomerId(customerId); }
    customer.setCustomerFirstName(firstName);
    // ... a dozen more setters ...
    customerDao.saveCustomer(customer);
}
```

It "saves a Customer no matter whether it is new or preexisting" and under a dozen unrelated business
situations — but nobody remembers *why* it exists or which uses are correct (raw L1038–1040). A later
revision wraps every setter in an `if (x != null)` check, so every parameter becomes optional and the
method saves a Customer "under at least a dozen business situations, and more" — with no way to test
that it does *not* save under the *wrong* ones (raw L1104). Vernon names this **anemia-induced memory
loss** (raw L1126).

The three big problems (raw L1118–1124):

1. There is little intention revealed by the `saveCustomer()` interface.
2. The implementation adds hidden complexity (buried null-checks, implicit business logic).
3. The `Customer` "domain object" is not an object at all — "It's really just a dumb data holder."

Domain experts cannot help review it, because reading it requires being a programmer — breaking the
whole point of a [[ubiquitous-language]].

## The distinction that is *not* the anti-pattern — layering

Anemia is often confused with legitimate layering. Putting behaviour into domain objects does **not**
mean abandoning layers. The **domain logic** that belongs *in* the domain object is validations,
calculations, and business rules; a thin **Application/Service Layer** on top is fine — but its
advocates use it *with* a behaviourally rich model, not to hollow the model out. (raw L39–L58,
[[web-page-bliki-anemic-domain-model]]) Fowler quotes Evans' own rule of thumb: "the more common
mistake is to give up too easily on fitting the behavior into an appropriate object, gradually
slipping toward procedural programming." See [[application-service]] for where the coordination-only
line is drawn.

## The cure: behaviour that names intent

Redesign the model so each business goal is an explicit, intention-revealing method, and narrow each
[[application-service]] method to a single use case (raw L1222):

```java
public interface Customer {
    void changePersonalName(String firstName, String lastName);
    void relocateTo(PostalAddress changedPostalAddress);
    void changeHomeTelephone(Telephone telephone);
    void disconnectHomeTelephone();
    // ...one method per real business goal...
}

@Transactional
public void changeCustomerPersonalName(String customerId,
        String firstName, String lastName) {
    Customer customer = customerRepository.customerOfId(customerId);
    if (customer == null)
        throw new IllegalStateException("Customer does not exist.");
    customer.changePersonalName(firstName, lastName);
}
```

Now the code reads as the business goal, no longer needs ten trailing nulls, and can be tested to
confirm it does exactly what it should and nothing it should not (raw L1243). The concrete antidotes:

- A [[value-object]] that validates itself in its constructor and refuses an invalid state.
- An [[entity]] that owns the logic tied to its identity and lifecycle.
- An [[aggregate]] whose root enforces its business rules in its own methods rather than exposing
  setters for a service to mutate. The `BacklogItem.commitTo()` example on [[ubiquitous-language]] is
  the same medicine on a richer domain — and it additionally publishes a [[domain-event]] the anemic
  version could not.

The present-day guide restates it bluntly: "forget about the anemic domain model, where a class is
just a setter/getter over a DB table. That is not object-oriented programming, it is working with data
through a pretty façade." (raw L64, [[web-page-ddd-guide-2026]])

## Self-check and trade-off

Anemia is *cheap and fast* up front and framework-friendly, which is exactly why it spreads. Its cost
is deferred: lost intent, untestable branches, and rules that can only be reconstructed by reading many
clients and database constraints over "several hours or days" (raw L1108). Symptom to watch for: the
model exposes attributes and accessors (its *shape*) rather than behaviours, forcing clients to know
how to correctly assemble state. A fat [[application-service]] is the tell that behaviour has drifted
up out of the model.

## Related

- [[domain-model]] — what a real (behaviour-rich) model buys you.
- [[value-object]], [[entity]], [[aggregate]] — the behaviour-rich building blocks that avoid anemia.
- [[application-service]] — the thin coordinator; a fat one signals anemia.
- [[domain-service]] — legitimate where behaviour has no home on an Entity/Value; overused, it drains the model.
- [[ubiquitous-language]] — behaviour that names intent is how the Language reaches the code.
- [[data-model-leakage]] — the sibling anti-pattern, also rooted in data-thinking.
- [[ddd-lite]] — the strategic-design shortcut that keeps company with anemia.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-bliki-anemic-domain-model]] — source summaries.
