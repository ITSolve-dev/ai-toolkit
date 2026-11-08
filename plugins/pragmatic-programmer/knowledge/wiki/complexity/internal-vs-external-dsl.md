---
title: Internal or external DSL
category: complexity
summary: "A hand-written tokenizer or parser in the repository whose input is flat or nested key-values that YAML, JSON or CSV already express, or step matchers that only turn sentences back into calls."
tags: [decision-rule, dsl, parser, abstraction-cost]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

This page settles the form of the notation that [[program-close-to-the-domain]] calls for.

## Rule

The source's overall advice is «не тратить усилий больше, чем можно сэкономить» (p. 98). A domain-specific language adds cost to a project, so you must be sure it pays back, potentially over the long term (p. 98). The order it gives (p. 98):

1. Use an off-the-shelf external language such as YAML, JSON or CSV where possible.
2. Otherwise look for an internal language.
3. Use an external language of your own only where it will be written by the users of your application.

The two forms differ in how they run. An internal language is written in its host language and compiles and runs as ordinary code, such as a test library or a framework's router. An external language is its own language, read by the application's code and converted to a form the code can use, such as a behaviour test format or a configuration specification (pp. 96-97).

The trade-off behind the order (pp. 97-98):

| | Internal | External |
|---|---|---|
| Gains | host language features for free, such as generating cases with a loop | no constraints from a host language |
| Costs | bound to host syntax and semantics; a compromise between the language you want and the one you can implement | needs a parser, which may mean new libraries or tools, and a good parser is hard to write |

Macros give an internal language more room, but syntax remains syntax (p. 97). Using a third-party parser, as a configuration tool does with YAML, brings the compromise back (p. 97). If a parser must be written, parser generators or PEG frameworks are the source's suggestion (p. 98).

This wiki reads the source's remark on customers as a warning that a stated audience is not enough to justify an external language. The source notes that test formats written for customers to read are rarely read by them, since business users know their goals but not the details, and approving such text is like proofreading Sumerian. It advises giving them working code to try instead (p. 95).

## Sign in code

- A hand-written tokenizer or parser in the repository whose input is flat or nested keys, values and lists, which YAML, JSON or CSV already express.
- A custom text format whose only samples sit in the repository beside the parser.
- A layer of step matchers that exists only to turn sentences back into calls the tests could make directly.

Who writes or reads the input cannot be seen in code. These signs say the question is worth asking; settling it needs knowledge of who authors or reads these files. The third sign is this wiki's own and no verdict on the form, because the book lists such a test format among its examples of the tip (pp. 94-95).

A hand-written parser for a configuration or data language the project defines is [[internal-vs-external-dsl]]; re-parsing an existing standard format that a library already reads is [[use-existing-components-before-writing-your-own]].

## When not to apply

- The language is written by the users of the application. This is the case the source allows.
- The format is an existing standard with a maintained parser. This wiki adds that parsing it with that parser is not the sign, even if the parser is large.
- The input has real grammar: expressions, nesting with precedence, operators. This wiki adds that such a language cannot be flattened into keys and values, and forcing it there hides a grammar in string fields.
- This wiki adds a limit from the other side: a YAML or JSON file that has grown conditions and loops has become an unplanned language, and the ready format no longer excuses it.

## Repair

1. If the input fits a ready format, replace the custom syntax with it, and validate the structure after loading. The validation step is this wiki's own.
2. If the input is written only by developers and needs logic, move it into the host language as an internal language, preferably [[internal-dsl-from-plain-functions]].
3. If a custom language stays, replace a hand-written parser with a generator or a PEG framework (p. 98), and keep its grammar separate from what the commands do. The separation is this wiki's own.

## Before and after

```
// before: a private syntax and its parser
// rules.txt:  limit api 100 per minute; limit upload 5 per hour
function parse_rules(text):
    for chunk in text.split(";"):
        words = chunk.trim().split(" ")
        if words[0] != "limit": raise SyntaxError
        rules.add(Rule(words[1], to_int(words[2]), words[4]))
```

```
// after: a ready format, and only validation remains
// rules.json:  [{"name": "api", "count": 100, "per": "minute"}, ...]
function load_rules(path):
    return validate(RULE_SHAPE, read_json(path))
```

## Source

[[pragmatic-programmer]], Topic 14, pp. 94-98: the order of preference, the definitions, the trade-off and the note on customers not reading test formats. The reading of that note as a limit on stated audiences, all signs, the split with [[use-existing-components-before-writing-your-own]], the limits marked as added, the validation and separation steps and the pseudocode are this wiki's own.
