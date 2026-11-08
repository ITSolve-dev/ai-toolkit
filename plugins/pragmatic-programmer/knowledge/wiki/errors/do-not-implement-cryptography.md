---
title: Do not implement cryptography yourself
category: errors
summary: "A hand-written cipher, a home-made hash or salt scheme, MD5 or SHA-1 for passwords, or login and password storage built from primitives."
tags: [rule, errors, security, cryptography, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This wiki's reasoning is that cryptography fails silently: the code runs, the tests pass, and an expert breaks it, so the usual checks of working software do not show whether it is secure.

## Rule

Common sense fails in cryptography, and the first rule is «никогда не реализуйте ее самостоятельно» (p. 288). The smallest and least visible mistake can compromise everything, and a clever home-grown algorithm may be broken by an experienced attacker in minutes (p. 290). Rely on well-tested, carefully studied, regularly maintained and often updated libraries and frameworks, preferably open source (p. 290).

The same care extends to neighbouring features such as user authentication. Writing your own password or biometric login requires understanding hashes and salt, how attackers use rainbow tables, and why MD5 and SHA-1 must not be used, and you then carry the responsibility for secure storage under new laws and legal duties (p. 290). The pragmatic alternative is to hand that burden to an authentication provider, in-house or third-party, whose job is to keep it secure (p. 290).

## Sign in code

- A function performs its own bit mixing, XOR or substitution to protect data.
- A password is hashed with MD5 or SHA-1.
- A password is hashed with a general-purpose hash and a hand-rolled salt scheme.
- Random values for tokens or keys come from a general-purpose random generator.
- A module implements login, session tokens and password storage from primitives.

## When not to apply

The book's footnote allows an exception: a doctorate in cryptography, and even then only with peer review, extensive field trials with bounties for finding holes, and funding for long-term maintenance (p. 288). Provider-based authentication has its own limit: services from mail, phone or social networks may or may not suit a given application (p. 290). Calling a vetted library's high-level operation is what the rule asks for, so this wiki does not count it as implementing cryptography. This wiki keeps composing low-level primitives inside the rule: choosing a cipher mode, handling nonces or ordering encryption and authentication by hand leaves room for the small mistake the book warns of (p. 290), even with a vetted library underneath.

## Repair

Replace the primitive code with a maintained library's high-level operation. For logins, move to a library's password-hashing function or to an authentication provider, and plan rehashing or migration of stored credentials.

## Before and after

Before:

```
function store_password(user, password):
    user.digest = md5(SALT + password)
```

After:

```
function store_password(user, password):
    user.digest = password_library.hash(password)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 288, 290. This wiki's own: the opening statement, the signs apart from MD5 and SHA-1, the last two sentences of the limits, the repair and the pseudocode. Related: [[keep-secrets-out-of-source]].
