---
title: Ports and Adapters
category: architecture
summary: Abstract an external dependency behind an interface (a port) owned by the application and supply concrete implementations (adapters) from outside — the general form of a Repository, with a decision rule for when a plain function suffices versus when an abstract base class is warranted.
tags: [pattern, architecture, ports-and-adapters, adapter, hexagonal, abstraction, fakes, testing, repository, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Ports and Adapters

**Ports and adapters** is the technique of abstracting every external dependency — email, pub/sub, object storage, a database session — behind an interface (a *port*) that the application owns, and supplying the concrete implementation (an *adapter*) from the outside via injection. A [[repository]] and a [[unit-of-work]] are the persistence-specific instances of this same pattern; this page is the general form that covers all the other integrations a domain needs. It is [[dependency-inversion-principle|dependency inversion]] made concrete, and the implementation-level companion to the whole-system [[hexagonal-architecture]] style (of which "Ports and Adapters" is Cockburn's original name).

## Two shapes of dependency: function vs ABC

The key decision rule is *how heavy the port should be*, and it turns on the complexity of the dependency's API. Cosmic Python contrasts its two dependency styles:

> The UoW has an abstract base class. This is the heavyweight option for declaring and managing your external dependency. We'd use this for the case when the dependency is relatively complex. (raw L6355)

> Our email sender and pub/sub publisher are defined as functions. This works just fine for simple dependencies. (raw L6357)

So:

- **Simple dependency (one operation)** → a plain `Callable` is the port. `send_mail: Callable` or `publish: Callable` needs no class.
- **Complex dependency (multi-method API)** → an **abstract base class**. Real-world examples the authors inject at work are an S3 filesystem client, a key/value store client, and a `requests` session — and "Most of these will have more-complex APIs that you can't capture as a single function: read and write, GET and POST, and so on" (raw L6368).

Don't reach for a heavyweight ABC when a function models the port faithfully; don't cram a genuinely multi-method integration into a single `Callable`.

## Worked example: promoting `send_mail` to a proper adapter

The book walks a simple dependency up into a "proper" adapter to show the full shape. First, generalize the port beyond its current concrete meaning:

> We'll imagine a more generic notifications API. Could be email, could be SMS, could be Slack posts one day. (raw L6374)

The port is an ABC that names the capability, not the technology:

```python
class AbstractNotifications(abc.ABC):
    @abc.abstractmethod
    def send(self, destination, message):
        raise NotImplementedError

class EmailNotifications(AbstractNotifications):
    def __init__(self, smtp_host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.server = smtplib.SMTP(smtp_host, port=port)
        self.server.noop()
    def send(self, destination, message):
        ...
```

The concrete adapter is then injected at the composition root instead of the old function (`notifications: AbstractNotifications = EmailNotifications()`), so nothing in the domain or handlers changes.

## Real and fake implementations (the testing payoff)

The port's real value is that it supports parallel implementations — a production adapter and an in-memory fake — swapped by injection, with no monkeypatching:

```python
class FakeNotifications(notifications.AbstractNotifications):
    def __init__(self):
        self.sent = defaultdict(list)
    def send(self, destination, message):
        self.sent[destination].append(message)
```

This gives a testing pyramid across the same seam:

- **Unit tests** inject `FakeNotifications()` and assert against its recorded `sent` messages — fast, no I/O.
- **Integration / end-to-end tests** inject the real `EmailNotifications`, pointed at a real-ish server (the book uses MailHog in Docker) and read the message back out.

Because the fake honours the same ABC, the fake and the real adapter stay contractually aligned. This is the same heuristic the [[repository]] page states: if the fake is hard to build, the abstraction is probably too complicated.

## Trade-offs

- **Gain**: the domain and handlers depend only on the port, so they are unit-testable, framework-agnostic, and unaffected when the concrete technology changes (email → SMS → Slack).
- **Cost**: an extra abstraction plus a construction/wiring point. For a one-method dependency this may be more ceremony than a function warrants — hence the function-vs-ABC decision rule above.
- **Framework caution**: manual injection at one place (the composition root — see [[dependency-inversion-principle]]) is usually enough; a DI framework only pays off with chained multi-level dependencies.

## Failure modes

- **Over-abstracting a trivial dependency**: wrapping a single operation in an ABC when a `Callable` port would do — heavyweight machinery for no gain.
- **Under-abstracting a complex one**: forcing a multi-method integration (read/write, GET/POST) through a single function, which leaks the concrete API and blocks clean faking.
- **Naming the port after the technology** (`EmailPort`) rather than the capability (`AbstractNotifications`), which quietly re-couples the application to one implementation and defeats the point of the abstraction.
- **Skipping the fake**: keeping the port but still monkeypatching the concrete adapter in tests reintroduces the coupling ports-and-adapters exists to remove (see [[dependency-inversion-principle]]).

## Related

- [[hexagonal-architecture]] — the whole-system architectural style this is the per-dependency technique of.
- [[dependency-inversion-principle]] — the principle it makes concrete, plus the composition-root wiring.
- [[repository]] · [[unit-of-work]] — the persistence-specific ports/adapters.
- [[decoupling-domain-logic-from-infrastructure]] — the broader isolation goal.
