---
title: Decoupling Domain Logic from Infrastructure
category: design-principles
summary: Isolate the business/domain logic from messy I/O so the core has no dependencies on external state and can be tested and extended on its own. This is the rationale behind the Repository and ports-and-adapters; the authors prefer explicit abstractions and dependency injection over mock.patch.
tags: [principle, functional-core-imperative-shell, dependency-injection, testability, mocks, design-principles, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

The central architectural principle behind DDD's [[repository]] and ports-and-adapters style: **keep the business/domain logic free of dependencies on messy I/O**, so the model can be tested and evolved independently of the filesystem, database, or network. *Architecture Patterns with Python* derives that principle from first principles on a small example, then names the tools for achieving it.

## The problem: high-level logic coupled to low-level details

When the domain algorithm ("figure out the difference between two directories") is tangled with I/O, you cannot exercise it without real infrastructure:

> The problem is that our domain logic, "figure out the difference between two directories," is tightly coupled to the I/O code. We can't run our difference algorithm without calling the `pathlib`, `shutil`, and `hashlib` modules. (raw L1640..1643)

The symptoms are the diagnostic: tests need heavy filesystem setup, stay slow, and are hard to read; and the code isn't extensible — you can't add a `--dry-run` flag or sync to a remote server without rewriting it (raw L1651..1656). This is the flip side of the [[anemic-domain-model]]: even *rich* logic is stuck if it can only run against real I/O.

## Functional Core, Imperative Shell (FCIS)

The first remedy is to split stateful I/O from pure logic:

> We'll create a "core" of code that has no dependencies on external state and then see how it responds when we give it input from the outside world (this kind of approach was characterized by Gary Bernhardt as Functional Core, Imperative Shell, or FCIS). (raw L1719..1724)

The top-level function becomes a thin shell — "an imperative series of steps: gather inputs, call our logic, apply outputs" (raw L1728). The pure core takes and returns simple data structures:

```python
def sync(source, dest):
    source_hashes = read_paths_and_hashes(source)   # imperative shell: gather inputs (I/O)
    dest_hashes = read_paths_and_hashes(dest)
    actions = determine_actions(source_hashes, dest_hashes, source, dest)  # functional core
    for action, *paths in actions:                  # imperative shell: apply outputs (I/O)
        ...
```

`determine_actions()` — the business logic — depends on nothing external; it takes two dicts of hash→filename and yields action tuples. Tests act on it directly, with no filesystem (raw L1761..1794). This is the same division a [[repository]] enforces at the model boundary: pure domain on one side, persistence on the other.

## Dependency injection over mocking

FCIS moves the test point down to a lower-level function. An alternative keeps the real top-level entrypoint but **injects the infrastructure** — the authors' preferred approach. `sync(source, dest, filesystem=FileSystem())` receives a `FileSystem` abstraction and calls `filesystem.read/copy/move/delete`. Production passes the real one (which does real I/O); tests pass a `FakeFilesystem` that records actions instead of performing them, serving as both a fake and a spy (raw L1812..1890).

Notably, no abstract base class or explicit interface is required:

> Although we're using dependency injection, there is no need to define an abstract base class or any kind of explicit interface ... Python's dynamic nature means we can always rely on duck typing. (raw L1833)

### Why not just `mock.patch`?

> We avoid using mocks in this book and in our production code too ... our instinct is that mocking frameworks, particularly monkeypatching, are a code smell. (raw L1899)

Three reasons (raw L1907..1914):

1. **Patching doesn't improve the design.** Mocking out a dependency lets you unit-test, but it won't make the code work with a `--dry-run` flag or against an FTP server. "For that, you'll need to introduce abstractions."
2. **Mock tests couple to implementation details.** They verify interactions ("did we call `shutil.copy` with the right arguments?"), which tends to make tests brittle.
3. **Overuse of mocks yields complicated suites that fail to explain the code** — setup noise hides the story that matters.

Instead: identify responsibilities and separate them into small, focused objects that are easy to swap for a test double. This is the design pressure that produces clean [[repository]] and [[application-service|service-layer]] abstractions.

## Trade-offs

- **DI vs. mocks:** DI tests run the exact same function production uses. The cost is that stateful components must be made explicit and threaded through — what David Heinemeier Hansson called *"test-induced design damage"* (raw L1891).
- **Testability is a proxy for extensibility:** "Designing for testability really means designing for extensibility" (raw L1916). The reason to decouple is not just easier tests; it is the ability to admit novel use cases (dry-run, remote, cloud) without touching the core.
- **TDD as design, not just verification:** "We view TDD as a design practice first and a testing practice second" (raw L1918).

## Heuristics

To find where to insert the abstraction, ask the questions in [[abstractions]]: pick a familiar data structure for the messy system's state, separate *what* from *how*, and find the *seam* where the line between systems belongs (raw L1940..1951). The load-bearing one for DDD: *what are the dependencies, and what is the core business logic?* — draw the boundary there.

## Related

- [[coupling-and-cohesion]] · [[abstractions]] — the vocabulary and tool this principle applies.
- [[repository]] — the DDD pattern that enforces this decoupling at the persistence boundary.
- [[anticorruption-layer]] — the same decoupling applied at a context boundary.
- [[anemic-domain-model]] — the opposite failure axis (logic-free objects vs. logic that can't run without I/O).
- [[web-page-cosmic-python-book]] — source summary (Ch. 3, "A Brief Interlude: On Coupling and Abstractions").
