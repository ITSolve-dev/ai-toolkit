---
title: Share functionality with mixins
category: objects
summary: "The same finder or helper methods repeated across sibling classes; one class holding every validation, with flags choosing which run in which situation."
tags: [rule, mixins, traits, code-reuse, validation]
paradigm: oop
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

A mixin is a named set of functions that extends a class or object without inheritance, producing something that combines the original abilities with the new ones. This is often possible even without access to the extended class's source (p. 205). The mechanism and its name differ by language, and the book lists mixins, traits, categories and protocol extensions as the same idea (p. 205). It treats the mechanism as independent of any language, so the word mixin below means the idea.

## Rule

«Пользуйтесь миксинами для совместного использования функциональных возможностей» (p. 207).

The book shows two uses:

- **Common methods across classes.** Delegation leaves each record class forwarding the same operations. A mixin with a few standard finders can be added to each one as it is written (pp. 205-206).
- **Validation that depends on situation.** An account may need different checks for a password match, a customer's form, an administrator's update, input from other components, and consistency before saving (p. 206). The book calls gathering all of them in one class, with flags to select them, typical and in its view a «неидеальный подход» (p. 206). It builds specialised classes from validation mixins instead. Passing an instance of the right class then ensures the right checks automatically (pp. 206-207).

## Sign in code

This wiki reads the sign as any of these:

- The same method bodies, or the same forwarding methods, appear in two or more sibling classes.
- One class holds validations for several situations, and a flag, mode or context parameter picks which run.
- A caller must remember to set a flag to get the correct validation, so forgetting it compiles and runs.

This wiki assigns the neighbouring case as follows. This page owns method bodies repeated on sibling classes that share no superclass of the project's own, and [[dry]] sends them here. Classes with no superclass of the project's own that repeat the same fields and a method over them, where every instance of each class would be a valid instance of one shared parent, are [[extract-superclass]]; repeated method bodies on classes whose instances would not be valid instances of one parent, or repeated without shared fields, are [[mixins-share-functionality]]. Overrides of one method on subclasses of a common superclass of the project's own, identical but for one step or wholly identical, are [[shared-behavior-in-superclass-varying-step-polymorphic]]. The same logic repeated in free functions or across unrelated modules stays with [[dry]]. A flag or mode parameter choosing which of one class's validations run is [[mixins-share-functionality]]; a control flag choosing among unrelated actions is [[routine-cohesion]].

## When not to apply

The book says only that each technique suits some circumstances (p. 207). This wiki adds these limits.

- A mixin that reads or writes fields of the class it joins brings back the hidden coupling of [[inheritance-tax]], since a rename there breaks it silently. A validation mixin has to read what it validates, so this wiki has it depend on accessors the class states it provides, and not on its fields.
- The language has no such mechanism. The rule is not transferred. Delegation or plain functions may serve, and that is decided at work time.
- Many mixins on a class make it hard to see where a method comes from, and two may collide on a name.
- One-off validations do not need a family of classes. A plain conditional at the one place it is used is cheaper.

## Repair

For repeated methods:

1. Extract them into one named mixin.
2. Add the mixin to each class and delete the copies.

For flag-selected validation:

1. Group the validations by situation, with common ones in their own mixin.
2. Compose one class for each situation from those mixins.
3. Remove the flag, and have callers receive the class for their situation. The type now selects the validations.

This wiki notes that the book's own specialised classes still extend a parent class, so this repair does not remove inheritance. It moves the variation out of the parent.

## Before and after

```
class Account
    method validate(mode):
        check_common()
        if mode == CUSTOMER: check_customer_form()
        if mode == ADMIN: check_admin_update()

account.validate(ADMIN)
```

```
mixin AccountChecks
    method check_common(): ...

mixin CustomerChecks
    method check_customer_form(): ...

mixin AdminChecks
    method check_admin_update(): ...

class CustomerAccount extends Account with AccountChecks, CustomerChecks
class AdminAccount extends Account with AccountChecks, AdminChecks

function update_as_admin(account: AdminAccount): ...
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 31, pp. 205-207. The definition, the two uses and the judgement on flag-selected validation are the book's. The signs and their assignment against [[dry]], the limits and the repair steps are this wiki's own, including the remark that the book's classes still inherit. The pseudocode is this wiki's. Related: [[choose-an-alternative-to-inheritance]], [[delegate-to-services]].
