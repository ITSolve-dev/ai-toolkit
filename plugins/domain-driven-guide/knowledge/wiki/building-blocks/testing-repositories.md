---
title: Testing Repositories
category: building-blocks
summary: Two testing concerns — prove the Repository itself works (requires the full production implementation) and test client code that uses Repositories (production or a simple in-memory HashMap edition), which is fast and enables asserting save() usage.
tags: [guide, repository, testing, in-memory, persistence-oriented-repository, aggregate]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

There are two distinct testing concerns around a [[repository]], and they call for different implementations.

> "You have to test the Repositories themselves in order to prove that they work correctly. You also must test code that uses Repositories to store the Aggregates that they create and to find preexisting ones. For the first kind of test you must use the full production-quality implementations ... For the second kind of test, either you can use your production implementations, or you can use in-memory implementations instead." (raw L11267)

## 1. Testing the Repository itself — production implementation

To know your production code will actually work, test the real implementation (Hibernate, Coherence, MongoDB, etc.). A typical test:

- **Setup** constructs the real Repository and a fake tenant identity; **teardown** cleans the store. For a Data Fabric this cleanup is essential: "If you don't remove all cached instances, they will remain during subsequent tests, which may cause failure for certain assertions such as persisted instance counts" (raw L11306).
- **Save-and-find** proves persistence: a successful `save()` with no exception is *not* proof — "there is only one way to know for certain. We have to find the instance and compare it to the original" (raw L11336), asserting each attribute of the read-back [[aggregate]] equals the stored one. Repeat for `saveAll()` + `allProductsOfTenant()`, asserting the returned collection size.

## 2. Testing clients — in-memory implementation

When the full implementation is hard or slow to set up, or the schema/persistence mechanism does not yet exist during early modeling, back the Repository interface with a `HashMap`:

> "The simple part is creating a `HashMap` to back your interface. It is straightforward to `put()` entries to and `remove()` them from the `Map`. We just use the globally unique identity of each Aggregate instance as the key. The Aggregate instance itself serves as the value." (raw L11405)

```java
public class InMemoryProductRepository implements ProductRepository {
    private Map<ProductId,Product> store = new HashMap<>();
    public void save(Product p)   { store.put(p.productId(), p); }
    public void remove(Product p) { store.remove(p.productId()); }
    public Product productOfId(Tenant t, ProductId id) {
        Product p = store.get(id);
        if (p != null && !p.tenant().equals(t)) p = null;  // multitenancy guard
        return p;
    }
}
```

The one subtlety is the multitenancy guard in `productOfId()`: after fetching by identity you must still verify the Aggregate's tenant matches, else return `null` (raw L11468). The test class is a near-identical copy of the production test — "The only change that needs to be made is in `setUp()`" (raw L11470): instantiate the in-memory Repository instead of the real one; every assertion is otherwise identical.

### Two extra payoffs

- **Asserting save() discipline.** With a [[persistence-oriented-repository]] you can count `save()` invocations in the in-memory edition and, after a test, "assert that the invocation count matches the number required by the client" (raw L11491) — useful for verifying [[application-service]]s that must explicitly save mutated Aggregates.
- **Hard finders.** Complex criteria are the difficult part of an in-memory edition; a workaround is to prepopulate the store in `setUp()` so the finder returns known instances (raw L11489).

## Related

[[repository]] · [[persistence-oriented-repository]] · [[collection-oriented-repository]] · [[application-service]] · [[aggregate]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
