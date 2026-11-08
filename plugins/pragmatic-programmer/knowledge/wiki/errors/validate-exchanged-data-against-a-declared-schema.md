---
title: Validate exchanged data against a declared schema and reject it, rather than guess
category: errors
summary: "Code reading a document from another system (file, message, payload) only parses it and then reads fields off the result, or fills a missing required field with a default (`or \"\"`, `.get(key, 0)`), instead of checking it against one declared structure and rejecting a non-conforming document with an error naming what is missing."
tags: [rule, validation, data-exchange, boundaries, fail-fast]
paradigm: any
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

When two independent applications exchange data, the receiving code holds the incoming document to an explicit, shared description of its structure and refuses one that does not conform. Weisfeld makes the point in chapter 11 by contrasting HTML with XML checked against a document type definition (DTD). The book states it about a data format; carrying it into receiving code is this wiki's own move.

## Rule

Weisfeld contrasts two ways of handling a malformed document. A browser reading HTML with a missing closing tag still loads the page, with unpredictable results: «В случае с HTML будет сделано наиболее вероятное предположение и работа продолжится» (p. 212). An XML document checked against a DTD fails instead: an error message is produced «и этот документ не будет считаться валидным» (p. 212). He ties the benefit to data: passing validation gives the much greater reliability that data needs (p. 212).

He separates two levels of checking. Without a DTD a document is checked only for being well formed, that is, for parsing (p. 211). With one it is also checked for validity: the declared elements in the declared nesting. A misspelled `<PurchasOrder>` for `<PurchaseOrder>` is caught only at the second level (p. 211). In his worked example a supplier document with the company name removed is still well formed; a validator rejects it and names the missing element, while a browser opens and shows it anyway (pp. 218-220). One shared definition serves every producer: each new supplier writes against the same `supplier.dtd`, and the receiver checks all of them the same way (p. 218). Company Alpha publishes an XML specification every supplier must follow, and both sides use the agreed standard (pp. 212-213); this wiki calls it the contract between the parties.

## Sign in code

These signs are this wiki's reading of the source, which shows a data format and not receiving code.

- A function that takes data from outside the process (a file, a request body, a queue message, a partner's export) parses it and then reads fields straight off the result, with no step checking that required fields are present and correctly nested.
- A missing required field is replaced with a default (`?? ""`, `.get(key, 0)`, `or None`) and the record goes on into storage or business logic instead of being rejected.
- The consumer reads a key the producer never writes because one side misspelled it, and silently gets null or empty: the code-level counterpart of `<PurchasOrder>`.
- Several producers of one format each get their own ad hoc checks scattered through the consumer, instead of one declared structure all of them are checked against.

This wiki assigns the neighbouring cases as follows. A missing or misnamed required field of a structured document from another system is [[validate-exchanged-data-against-a-declared-schema]]; the range or format of a present value, and where on the path the check stands, is [[barricade]]. A default for a missing required field of a structured document from another system is [[validate-exchanged-data-against-a-declared-schema]]; a substitute for a present but invalid value is [[robustness-versus-correctness]]. A value that passes the door still as raw text and is compared or converted later is [[convert-input-at-entry]]. A routine that normalises several shapes of one argument is [[strict-accept-narrow-promise]]. This page owns a structured document whose required fields and nesting are not checked against one declared structure, and required data replaced by a default.

## When not to apply

The source states none of these limits; they are this wiki's own.

- Display-only or best-effort consumption, where a partial result is more useful than none and nothing is stored or acted on: a viewer, a log pretty-printer, a preview. The browser behaviour Weisfeld describes is right for a browser.
- Data produced and consumed inside one module under a type the language already enforces: a second schema check repeats the type checker.
- A deliberately tolerant reader that ignores unknown fields so producers can evolve. Rejecting a missing required field and ignoring an unknown one are separate decisions, and this rule covers only the first.
- A parse into a declared typed model that rejects missing or misnamed fields is the validation step; the first sign does not fire.
- The choice of schema technology (DTD, XML Schema, JSON Schema, a validation library) is taken from the project's tooling.

## Repair

The steps are this wiki's own; the source shows only an external validator run on a file.

1. Declare the expected structure once: required fields, nesting, how many times each may occur, types. Keep it where every producer and the consumer can see it.
2. Validate where the data enters, before any field is read for business use, and convert textual numbers and dates there ([[convert-input-at-entry]]).
3. On failure reject the whole document with an error naming the missing or misnamed element. Do not substitute defaults for required data.
4. Downstream code works with the validated, typed result and needs no defensive checks of its own. What the program does once a contract is broken is [[crash-early]] and [[assertion-or-error-handling]].

## Before and after

```
function importSupplier(text):
    doc = parse(text)                        // only checks that it parses
    name = doc.get("companyname") or ""      // a missing name becomes empty
    price = toDecimal(doc.get("product").get("price"))
    save(Supplier(name, price))
```

```
SUPPLIER_SCHEMA = {
    name:    { companyname: text, required },
    address: { street: text, min 1; city: text; state: text; zip: text },
    product: { type: text; price: decimal; count: integer }
}

function importSupplier(text):
    doc = parse(text)
    result = validate(doc, SUPPLIER_SCHEMA)
    if result.failed:
        raise InvalidDocument(result.missingOrWrong)   // e.g. "name expected"
    save(Supplier(result.value.name.companyname, result.value.product.price))
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 11, via [[object-oriented-thought-process]]: well formed against valid, the misspelled tag (p. 211); HTML's best guess against XML's rejection, reliability for data (p. 212); the specification every supplier follows (pp. 212-213); one DTD for every supplier (p. 218); the invalid document a browser still shows (pp. 218-220). The quotations were checked against `raw/`. This wiki's own: calling the specification a contract, carrying the rule from a document format into receiving code, every sign, the owner assignments, all limits, the repair and the pseudocode. The rest of the chapter is format and tool documentation (DTD syntax, CSS for XML, XML Notepad, an online validator, JSON syntax), which this charter leaves out; its one-sentence remark that some developers avoid `eval()` for parsing JSON (p. 224) gives no reasoning and was not made into a page.
