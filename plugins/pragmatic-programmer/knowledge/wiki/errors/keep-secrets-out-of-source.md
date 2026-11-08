---
title: Keep secrets out of source and plain text
category: errors
summary: "A key, token or password appears as a literal in source or a committed config, or a credential column stores readable text."
tags: [rule, errors, security, secrets, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This wiki's reasoning is that a secret in version control is readable by everyone with repository access and stays in the history after removal, and that a secret in plain-text storage is exposed by any read of that storage.

## Rule

Identity data, financial data, passwords and other credentials must not be kept as plain text, whether in a database or any other external file. They should be encrypted for an extra layer of protection (pp. 287-288). The book's advice to put everything under version control has one important exception: secrets, API keys, SSH keys, encrypted passwords and other credentials are not checked in with the source. They are managed separately, through configuration files or environment variables, as a separate stage of build and deployment (p. 288).

## Sign in code

- A string literal in source or in a committed config file is a key, token, password or connection string with embedded credentials.
- A column or field named for a password or a token is written with the value as received.
- A file of keys, even encrypted ones, is tracked in the repository.

This wiki assigns the neighbouring case as follows. This page owns a literal that grants access, such as a password, token, API key, license key or a connection string with credentials. Any other deployment value written as a literal, such as a host, a port or a tax rate, is [[parameterize-with-external-configuration]].

## When not to apply

These limits are this wiki's own.

- An obviously fake value in a test fixture is not a secret, provided nothing real accepts it. A scanner may still flag it, and a name such as `not_a_real_key` helps the next reader.
- A value public by design, such as a public key or a publishable client key, is not a secret.
- A credential the program itself presents, kept in a configuration file outside the repository. The book names that route (p. 288), and this wiki reads its ban on plain text (pp. 287-288) as covering credentials the program stores for others.
- The book keeps encrypted credentials out of the repository as well (p. 288). A project that commits them through a deliberate tool and holds the decryption key elsewhere departs from the book, and this wiki reports that as a departure and not as a leak.

## Repair

1. Read the secret at startup from the environment, a secret store or a configuration file outside the repository, and fail at startup if it is missing.
2. Revoke and replace any secret that was ever committed. This wiki's reasoning is that removal alone leaves it in the history.
3. Store passwords as salted hashes through an established library; see [[do-not-implement-cryptography]]. The book speaks of encryption here, and its later passage on logins names hashes and salt (p. 290). This wiki reads a password as something to verify and never to recover.

## Before and after

Before:

```
API_KEY = "live-7f3a9c..."
client = PaymentClient(API_KEY)
```

After:

```
client = PaymentClient(required_env("PAYMENT_API_KEY"))
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 287-288, 290. This wiki's own: the opening reasoning, the signs, the assignment of the neighbouring case, the limits, repair steps 1 and 2, the reading of hashing against encryption, and the pseudocode. Related: [[attack-surface]], [[parameterize-with-external-configuration]].
