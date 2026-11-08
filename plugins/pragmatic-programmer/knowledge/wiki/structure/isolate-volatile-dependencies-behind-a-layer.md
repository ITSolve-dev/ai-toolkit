---
title: Wrap legacy and platform calls in one class
category: structure
summary: "Calls into the program's own poor-quality legacy code or a non-portable platform API, with their quirks (error codes, sentinel values, odd names) and the workarounds for them, appear at several call sites instead of being translated once inside one wrapper class."
tags: [rule, legacy-code, platform-isolation, information-hiding]
paradigm: any
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

McConnell gives two cases of one move: confine code whose quality or availability you do not control to one place, and let the rest of the program speak its own terms.

## Rule

- **Legacy code.** Put all interaction with poorly designed old code in one place that hides its poor quality and offers newer code a consistent set of services (p. 78, paraphrase). The two gains: «он изолирует плохой код» and, if the old code is later discarded or refactored, «вам не придется изменять новый код за исключением промежуточного уровня» (p. 78).
- **Platform and non-standard features.** Isolate hardware dependencies in a separate class (p. 95, paraphrase); the book also allows a subsystem, and where a subsystem boundary falls is the project's architecture. If you use non-standard language extensions, hide them in a separate class that can be replaced when porting; library routines not available in every environment go behind an interface that supports all the needed environments (p. 95, paraphrase).

Weisfeld's *The Object-Oriented Thought Process* gives the same move for objects. Non-portable (native) code is abstracted out of the class, meaning its isolation in its own class or at least its own overridable method; for a serial port on particular hardware, write a wrapper class that the main class sends messages to, and «Не размещайте зависимый от системы код в своем первичном классе» (ch. 5, p. 107). Behind the wrapper the user deals only with it, and the wrapper sorts out the platform differences and decides which code to call (p. 108). Chapter 6 generalises this as object wrappers: existing legacy code can also be wrapped (p. 128), and a `Sound` class with `beep()` hides a Windows-specific way of beeping, so that on another platform «интерфейс для пользователей останется прежним» (p. 129). His summary: «Основное назначение объектных оберток — обеспечивать согласованные интерфейсы для программистов, использующих соответствующий код» (p. 130). The `beep` wrapper can grow other signal methods as they are needed (pp. 128-129).

McConnell states the legacy case as stratification, a layer of the design (p. 78). This page applies it inside the code, as one class or module of functions; where the project's architecture already assigns such code to a layer, that layer is the place, and this wiki does not prescribe one.

## Sign in code

- Calls into the same legacy routine or type of the program appear at several call sites in new code, so its types and quirks (error codes, nullable sentinels, odd naming) are decoded there.
- A workaround for a legacy or platform quirk is repeated at several call sites rather than handled once.
- Non-portable platform or hardware calls (OS-specific APIs, device access) or non-standard language extensions appear at several call sites in domain logic.
- Platform conditionals around one operation (`if os == A ... else ...`) repeated at several call sites, including several methods of one class (after Weisfeld's serial port, p. 107).
- A supposed wrapper takes or returns the platform's or legacy code's own types in its public signatures, so callers still depend on them. This sign is this wiki's own.

This wiki assigns the neighbouring cases as follows. The program's own legacy code or a non-portable platform API spread over modules is [[isolate-volatile-dependencies-behind-a-layer]]. A vendor's client, query dialect or exception type named outside one adapter class, in code that also holds business logic or in the application's own signatures, is [[hide-third-party-apis]]. A table or record layout known by several modules is [[single-owner-of-data-access]], whatever product stores it. Logic held together with presentation is [[logic-testable-without-ui]]. A single function whose dependency on the file system, database or another mutable resource is hidden from its signature, with no spread across call sites, is [[global-data]].

## When not to apply

These limits are this wiki's own.

- **A dependency used in exactly one place** already has a single point of contact, and this page does not fire. Weisfeld keeps non-portable code out of the primary class even at one site (p. 107) and wraps a one-line `beep` (p. 128); this wiki resolves that by sending the single site to [[global-data]], whose repair, a wrapper passed in, is the one Weisfeld asks for. A single legacy call with no quirk decoded around it needs no wrapper.
- **Small scripts and throwaway tools**, where replacement or porting will not happen, do not repay the wrapper.
- **Portable standard-library calls** need no wrapper; the rule concerns code tied to one platform.
- **A class that is itself the wrapper**, whose only job is to talk to the platform, is the place the platform calls belong.
- Weisfeld's `SomeMath.add(a, b)`, a method wrapping `a + b` (pp. 126-127), only illustrates that a method contains structured code; it does not recommend wrapping trivial expressions the project controls. This reading is this wiki's.
- The wrapper must speak the problem's terms. One that re-exports the legacy API one to one, with its codes and sentinels, only adds indirection, and the leak remains.

## Repair

This wiki's own:

1. List the operations the program actually needs from the legacy code or platform, in the program's own terms: `findCustomer`, `currentUserHome`.
2. Put them in one class or module, implemented once over the legacy code or platform.
3. Where platforms differ, give the wrapper one implementation per platform, or at least an overridable method, as Weisfeld allows (p. 107).
4. Move each direct call site to the wrapper, translating the old code's types, error codes and sentinels into the program's own inside it.

## Before and after

```
// before: two routines call the legacy account code and decode its quirks
// fees
acct = LegacyAcct.read(accountId)
if acct.flg == 3 then return                 // 3 = closed
LegacyAcct.write(accountId, acct.bal + LATE_FEE)

// statements
acct = LegacyAcct.read(accountId)
if acct.flg != 3 then print(acct.bal)
```

```
// after: one wrapper knows the legacy code and its codes
module accounts                               // the only caller of LegacyAcct
    find(accountId) -> Account               // Account { balance, isClosed }
    save(account)

// fees
account = accounts.find(accountId)
account.chargeLateFee(LATE_FEE)               // no-op when closed
accounts.save(account)

// statements
account = accounts.find(accountId)
if not account.isClosed then print(account.balance)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: ch. 5, pp. 107-108 (non-portable code in its own class or overridable method, the serial-port wrapper, the reasoning); ch. 6, pp. 126-130 (structured code inside methods, legacy code wrapped, `Sound.beep`, the purpose of wrappers). The quotations were checked against `raw/`. This wiki's own for that part: the leaky-wrapper sign, the platform-conditional sign as worded, the wrapper-class and `SomeMath` limits, and the resolution of the one-site case by sending it to [[global-data]].

[[code-complete]], ch. 5, Russian edition: section 5.2, p. 78 (stratification, the legacy layer and its two gains); section 5.3, p. 95 (hardware dependencies, non-standard language features, environment-specific library routines). The prescriptions and their benefits are the source's. This wiki's own: applying them as a class or module rather than a design layer, the signs, the assignment of neighbouring cases, the limits, the repair steps and the pair. The former mention of McConnell's UI, database and OS subsystems (pp. 82-83) was dropped as architecture on 2026-11-06.
