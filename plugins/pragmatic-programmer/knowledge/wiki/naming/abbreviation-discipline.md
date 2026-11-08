---
title: Abbreviate only when forced, and then consistently and pronounceably
category: naming
summary: "Shortened words where full words would fit: one word abbreviated two ways (Num/No, cust/customer), a word missing one letter (indx), unpronounceable consonant runs (ndsCmptg), phonetic spellings (hilite, xqt, b4), or a misreading (BEND for end of B)."
tags: [rule, naming, abbreviation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell treats shortening names as largely a relic of languages that capped names at 2-8 characters. Modern languages allow names of almost any length, so he sees almost no reason left to shorten descriptive names (p. 274). When shortening is still needed, he gives rules for doing it without hurting the reader (pp. 274-276).

## Rule

Almost never abbreviate when the language allows the full word. When you must abbreviate:

- **Consistently.** «Всегда используйте один и тот же вариант сокращения» (p. 275). Use only `Num` or only `No`, never both, and do not shorten a word in some names while spelling it out in others.
- **Not by one character.** Saving one letter does not pay for the lost readability, and later you cannot remember whether the letter was dropped. Either drop more than one character or write the whole word (p. 275).
- **Pronounceably.** Write `xPos` and `needsComp`, not `xPstn` and `ndsCmptg`. Apply the telephone test: if you could not read the code to someone over the phone, the names need to be more articulate (p. 275, after Kernighan and Plauger).
- **Not phonetically.** McConnell recommends forgetting spellings like `sk8ing`, `hilite`, `b4` and `xqt` (p. 275).
- **Not as a misspelling.** Do not save three letters by writing `hilite` for *highlight*. The reader then has to remember which of `highlite`, `hilite` or `hilight` you chose (p. 278). Avoid words that people commonly misspell, such as *calender* or *recieve* (p. 278).
- **Without a misreading.** For the end of B, use `ENDB`, not `BEND`. Separating the parts of a name (`BEnd`, `b_end`) removes the problem (p. 275).

His reasoning is that names exist first of all for the people who read the code: «имена создаются в первую очередь для программистов, читающих код» (p. 277). Programmers spend far more time reading code than writing it, so a name that is harder to type but easier to read is the right trade (pp. 277, 281). His suggested test is to reread your own code after six months and note the names you cannot understand at first glance (p. 277).

## Sign in code

- One word shortened two ways in one codebase (`numItems` beside `itemNo`, `cust` beside `customer` for the same entity).
- A word missing exactly one letter (`calend`, `paramtr`, `indx`).
- Runs of consonants that cannot be said aloud (`ndsCmptg`, `xPstn`).
- Phonetic or deliberately misspelled forms (`hilite`, `xqt`, `msg4u`, `nite`).
- An abbreviation that reads as a different word (`BEND` for 'end of B').

This wiki assigns the neighbouring cases as follows. This page owns a shortened word whose form breaks one of the rules above. A name too short for its scope whatever its form (`n`, `ns`) is [[name-length-matches-scope]]. Two abbreviations that collide in look or sound are [[names-differ-by-more-than-a-character]].

## When not to apply

- Abbreviations that are standard in the domain or in ordinary English (`id`, `url`, `max`, `min`, `config`, `html`) are not this sign. McConnell's first shortening tip is to use the standard, dictionary abbreviations (p. 274).
- Dropping inner vowels is one of the book's own shortening techniques (p. 274: computer to `cmptr`, screen to `scrn`). The sign is a result that fails the telephone test, not a missing vowel.
- A conventional short name in a tiny scope, such as a loop index in a one- or two-line loop, is governed by [[loop-index-names]], not by this page (p. 280).
- A hard length limit in the language or platform. McConnell cites a client in 2003 whose RPG program of several hundred thousand lines capped names at 6 characters. Under such a limit, shortening is forced, and his remedy is a translation table in a comment beside the code (p. 276).

## Repair

Spell the word out. If it must stay short, pick one abbreviation per word for the whole project and use it everywhere. McConnell suggests recording each one in a project 'Standard Abbreviations' document sorted by the full word, so that a second programmer reuses an existing abbreviation instead of inventing another (pp. 276-277). A collision between two abbreviations is [[names-differ-by-more-than-a-character]], which carries the book's synonym repair.

## Before and after

```
function updtCust(custNo, ndsCmptg):
    cust = find(custNo)
    if ndsCmptg:
        cust.hilite = true
    totNum = countOrders(customerNumber)   // the same word, spelled two ways
```

```
function updateCustomer(customerId, needsComputing):
    customer = find(customerId)
    if needsComputing:
        customer.highlighted = true
    orderCount = countOrders(customerId)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 274-278, 280-281 ([[code-complete]]). The rules (consistent, not by one letter, pronounceable, no phonetic forms, no misspellings, no misreadings), the telephone test, the six-month reread, the reading-over-writing reasoning, the 'Standard Abbreviations' document and the vowel-dropping technique come from the book. The concrete sign list, the assignment against the neighbouring pages, and the example `calend` are this wiki's own; McConnell's own one-letter example is a month name.
