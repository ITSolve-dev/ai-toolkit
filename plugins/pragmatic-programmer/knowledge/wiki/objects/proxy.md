---
title: "Proxy: control access through a surrogate that has the subject's interface"
category: objects
summary: "Two or more call sites of one service repeat the same wrapper around the call (try the remote and fall back to a local copy, check a cache, check a permission), or a client holds a remote and a local implementation of one service and picks between them; move that logic into a proxy that implements the service's interface and holds the real subject."
tags: [rule, gof, proxy, indirection, failover]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Proxy is a GoF pattern. Larman describes it as "an object that implements the same interface as the subject object, holds a reference to the real subject, and is used to control access to it" (35.4, p. 797). Context and problem, as he states them: "Direct access to a real subject object is not desired or possible." Solution: "Add a level of indirection with a surrogate proxy object that implements the same interface as the subject object" and is responsible for "controlling or enhancing access to it" (p. 798).

## Rule

The structure of a proxy is always the same, and the variants differ only in "what the proxy does once called" (p. 797). Larman names three:

- **Remote Proxy**: a local stand-in for a remote object, like an RMI or CORBA stub.
- **Redirection (Failover) Proxy**: his case study. `Register` sends `postSale` to a proxy as if it were the accounting service. If the proxy cannot reach the external service through its adapter, it redirects the call to `LocalAccounting`, which stores sales and forwards them later (p. 798).
- Device classes that wrap drivers, which he says can be called both Adapters and local proxies: "It is not uncommon to be able to classify a design in terms of multiple patterns" (35.6, p. 802).

What the pattern buys, in his summary: a client "does not know that it references a proxy" and "is designed as though it is collaborating with the real subject" (35.4, p. 799). This wiki places it, as a form of Indirection (p. 798), under [[protected-variations]].

### Local first or remote first

Larman solves two failover cases two ways:

- **Product information: local service first.** The factory always returns a local products service. It answers from its cache when it can and otherwise forwards to the adapter for the remote service, and the client `ProductCatalog` does not change (35.2, p. 785). The source calls this local object an "adapter" in quotes and says it "is not really an adapter to another component" (p. 785).
- **Sales posting: remote first, through a redirection proxy**, because "sometimes the external service should be tried first, and a local version second": the business wants sales posted as soon as possible (35.4, p. 797).

This wiki reads the selecting condition as: when a stale local answer is acceptable, the local object sits in front; when the remote copy must be current, the proxy tries the remote first and falls back. This wiki also reads Larman's remark that cached prices go stale (35.2, p. 788) as the cost of the first choice.

## Sign in code

This wiki's reading of the sign:

- Two or more call sites of the same service repeat the same wrapper around the call: try the remote and catch, then call a local fallback; or check a cache, then call and store; or check access, then call.
- A client holds two references to two implementations of one service (remote and local) and picks between them itself.

This wiki assigns the neighbouring cases as follows. A wrapper that changes the interface, so a vendor's API reaches the application in the application's own terms, is [[hide-third-party-apis]]. A wrapper with the subject's interface that may skip the subject or send the call elsewhere (a cache hit, a failover, a refused permission) is [[proxy]]; one that always calls the subject and adds to what goes in or comes out is [[composable-decorators]]. The same access wrapper repeated around calls to one service (a fallback, a cache check, a permission check) is [[proxy]]. Whether a cache is worth having at all is [[cache-must-earn-its-complexity]]; this page owns where its check sits once it is.

## When not to apply

- There is one call site and the access logic is short. A proxy class adds a type and a level of indirection for nothing. This limit is this wiki's own.
- The surrogate would have to change the interface (other arguments, other results). Then it is an adapter, not a proxy; Larman's proxy keeps "the same interface" (p. 797).
- The caller has to know that a fallback happened, for example to tell the user a sale was only stored locally. A transparent proxy hides exactly that, so the information has to come back in the result or an event. This limit is this wiki's own.

## Repair

1. Make sure the subject is reached through an interface (`Accounting`).
2. Create a proxy class that implements that interface, holds the real subject (and the fallback, for a redirection proxy), and contains the access logic once.
3. Have the factory or the wiring code hand out the proxy where it handed out the subject ([[factory-object-for-creation]]). Callers do not change.
4. Remove the duplicated wrapper from the call sites.

## Before and after

```
class Register
  method completeSale(sale)
    try
      sapAccounting.postSale(sale)
    catch ServiceUnavailable
      localAccounting.postSale(sale)

class Refunds
  method refund(sale)
    try
      sapAccounting.postReturn(sale)
    catch ServiceUnavailable
      localAccounting.postReturn(sale)
```

```
class AccountingRedirectionProxy implements Accounting
  field external: Accounting
  field local: Accounting
  method postSale(sale)
    try external.postSale(sale)
    catch ServiceUnavailable
      local.postSale(sale)
  method postReturn(sale)
    try external.postReturn(sale)
    catch ServiceUnavailable
      local.postReturn(sale)

class Register
  field accounting: Accounting        // a proxy, but Register does not know
  method completeSale(sale)
    accounting.postSale(sale)
```

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 35.2, PDF pp. 784-788 (the local service in front of the remote one, the stale-price problem), 35.4, PDF pp. 797-799 (Proxy and Redirection Proxy), 35.6, PDF p. 802 (Adapter and Proxy at once).
- This wiki's own: the placement under [[protected-variations]], the selecting condition between local-first and remote-first, the signs, the owner assignments, the limits, the repair and the pseudocode.

Related: [[abstract-factory]], [[do-not-force-a-design-pattern]].
