---
title: Kinds of comments
category: documentation
summary: "Concept: every comment repeats the code, explains it, marks unfinished work, summarises, states intent, or holds what code cannot; only the last three belong in finished code, and the test is whether the comment restates the lines it sits on one by one, at their own level, or says in a sentence what several lines together achieve."
tags: [concept, comments, intent, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**The kinds of comments** are McConnell's six-way classification of what a comment does (pp. 769-770). The comment pages of this wiki use it as their vocabulary when deciding whether a comment stays, goes, or calls for a change to the code.

## The six kinds

1. **Repetition of the code.** It restates the code in other words, so the reader reads more and learns nothing new (p. 769). Owned by [[comment-why-not-how]].
2. **Explanation of the code.** It explains complicated, tricky or fragile code. The book says such comments help there, but usually only because the code is unclear: «Если код настолько сложен, что требует объяснения, почти всегда разумнее улучшить код, а не добавлять комментарии.» (p. 769). Its order is to make the code clearer first and then add a summary or intent comment (p. 769). See [[self-documenting-code]] and [[rewrite-tricky-code]].
3. **Marker in the code.** A note that work is not done, «не для того, чтобы оставаться в коде» (p. 769). Owned by [[marker-comments]].
4. **Summary of the code.** It distils a few lines into one or two sentences. It beats a repeating comment because a reader scans it faster than the code, and it helps most when someone other than the author will change the program (p. 770).
5. **Description of the code's intent.** It states the author's intention at the level of the problem rather than of its solution (p. 770). The book's pair: "get current employee information" is an intent comment, and "update employeeRecord object" is a summary phrased in the solution's terms (p. 770).
6. **Information the code cannot express.** Copyright and confidentiality notices, version numbers, notes on the structure of the code, references to requirements or architecture documents and to web resources, notes on optimisation, and comments a documentation tool needs (p. 770).

The book accepts only three kinds in finished code: summary comments, intent comments and information the code cannot express (p. 770, paraphrased).

## Why intent matters most

The book cites a six-month IBM study in which maintenance programmers «чаще всего говорили, что труднее всего было понять цель автора кода» (Fjelstad and Hamlen, 1979; p. 770). The chapter's dialogue makes the same point. A good comment neither repeats nor explains the code but states its purpose, one level of abstraction above the code. A reader uses such comments like a book's table of contents, finding the section to change before reading the code (p. 765). The book adds that the line between intent and summary comments is often unclear and usually does not matter (p. 770).

## Using the classification on code

This wiki's test for a given comment, which the book does not state in this form, is whether the comment restates the lines it sits on one by one, at their own level (kind 1), or says in a sentence what several lines together achieve (kind 4 or 5).

- If it restates them, it is kind 1, to delete, or, where it explains how tricky lines work, kind 2, where the repair is to improve the code and then delete or replace the comment.
- If it names what the lines achieve in the problem's terms, it is kind 5 and stays.
- If it names what they do in the solution's terms, it is kind 4. It may stay, and rewording it into the problem's terms is the cheaper improvement.
- If it states a fact absent from the code, such as an outside constraint or a reference, it is kind 6 and stays.

```
// before
// update employee_record object
id = session.user_id
record = repository.load(id)
record.manager = directory.lookup(record.manager_id)
```

```
// after
// get information about the current employee
id = session.user_id
record = repository.load(id)
record.manager = directory.lookup(record.manager_id)
```

This wiki notes a limit of the pair. Once a name states the intent (`current_employee = ...`), the intent comment repeats the code and becomes kind 1. The classification is therefore applied after names have been improved, not before.

## Source

[[code-complete]], ch. 32, sections 32.3-32.4 (pp. 765, 769-770). The book's parts: the six kinds and their verdicts, the three kinds acceptable in finished code, the intent/summary pair, the IBM study, and the table-of-contents image. This wiki's own parts: the restatement test, the observation that a good name turns an intent comment into a repetition, and the pseudocode.
