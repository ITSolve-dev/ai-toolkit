---
title: "Hold text in one internal format; convert at input and output"
category: structure
summary: "Encoding or string-type conversions (to/from bytes, wide strings, legacy charsets) scattered through core logic, one value passed through core functions sometimes as bytes and sometimes as text, or user-visible strings written as literals in code that already looks up other messages by key."
tags: [rule, strings, encoding, internationalization, boundaries]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Where a program uses several string types or encodings, *Code Complete* recommends a single policy: «хранение всех строк программы в одном формате и преобразование их в другой формат как можно ближе к операциям ввода и вывода» (Russian edition, p. 290). It pairs this with deciding the internationalization strategy early, including whether all strings live in external resources (p. 290).

## Rule

- Choose one internal representation for text and convert to any other only at input and output.
- Keep user-visible strings the way the program's internationalization strategy decides: in external resources or in code, one build per language or the language chosen at run time. The book asks for that strategy to be settled early (p. 290).

## Sign in code

- Calls that encode or decode text, or convert between string types, inside business logic rather than in the code that reads or writes files, network messages or the user interface.
- The same value passed through core functions sometimes as bytes and sometimes as text, so each function has to know which it received.
- User-visible messages written as literals in code of a program that already looks up other messages by key from resources. The book's reason: strings gathered in one resource file are far easier to translate than strings scattered through the program (p. 289).

This wiki assigns neighbouring cases as follows. This page owns where text encoding and string-type conversion happen. A raw input string carried past the point where it was read and compared there, instead of being parsed into a boolean, enum or number, is [[convert-input-at-entry]]. Code that processes a value and also knows where it came from is [[process-values-not-their-source]]. A literal string that is not user-visible text is [[named-constants-over-literals]].

## When not to apply

The book's choice between ISO 8859 and Unicode and its advice on particular languages are language and platform matters and are not carried here. The limits below are this wiki's own:

- **A program that is not and will not be translated** need not move its messages into resources; the boundary rule for encodings still holds.
- **Code whose job is conversion** (a codec, a protocol parser) is the boundary; conversions inside it are expected.
- **Streaming or zero-copy processing of large data** may keep bytes deliberately; then bytes are the one internal format and the rule still holds.

## Repair

1. Name the internal text format for the program.
2. Move every decode to the point where text enters, and every encode to the point where it leaves.
3. Change core function signatures to accept and return only the internal format.
4. Where translation is needed, move user-visible strings into a resource looked up by key.

## Before and after

```
function greet(user_bytes)
  name = decode(user_bytes, "latin-1")
  msg = "Hello, " + name
  return encode(msg, "utf-8")

function log_greeting(user_bytes)
  log(decode(greet(user_bytes), "utf-8"))
```

```
function greet(name: Text): Text
  return messages.get("greeting").format(name)

on_request(raw)
  name = decode(raw, request.charset)
  reply = greet(name)
  log(reply)
  send(encode(reply, "utf-8"))
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: magic strings and resources for translation, p. 289; Unicode, the internationalization strategy and one string format converted at input and output, pp. 289-290. This wiki's own: the signs, all limits, the split with neighbouring pages, the repair steps and the pseudocode.
