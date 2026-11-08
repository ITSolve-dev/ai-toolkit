---
title: "Test scaffolding: stubs, mocks, drivers, dummy files"
category: testing
summary: "Concept: stand-ins below the unit (stubs, mock objects), drivers above it and small dummy files that isolate the unit under test; the way to test code buried deep in a program or too slow to reach through its callers."
tags: [concept, scaffolding, mocks, stubs, test-doubles]
paradigm: any
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Scaffolding is code built only to make other code testable, named after the building trade, where scaffolds give workers access to parts of a building (p. 513). McConnell names three kinds.

**Stand-ins below the unit.** An object the unit under test uses, called a mock object or stub object, or a low-level stub routine (p. 513). Depending on the realism needed, it may (p. 514): return at once doing nothing; check the data it receives; log its inputs; ask the programmer for a return value; return a canned answer regardless of input; burn the time the real one would take; act as a slower, larger, simpler or less accurate version of the real thing.

**Drivers above the unit.** A fake routine that calls the real one, also called a test harness. It may pass fixed data, take data from the programmer, the command line or a file, or call the unit repeatedly with predefined input sets (p. 514).

**Dummy files.** A small version of a real file. Its size lets the tester hold the whole content in mind, and because it is made for the test it can be designed so that any misuse stands out: «вы можете спроектировать его так, чтобы любая ошибка в его использовании бросалась в глаза» (p. 514).

**Stubs for an interface not yet implemented.** Weisfeld's *The Object-Oriented Thought Process*, after Gilbert and McCarthy, uses a stub to test an interface before its implementation exists (p. 112). His `DataBaseReader` keeps the full public interface (`open`, `close`, `goToFirst`, `goToLast`, `howManyRecords`, `getRecord`, `getNextRecord`) over an internal array of five strings instead of a database that may not exist yet; once the database is integrated it replaces the array (pp. 112-113). The reason: interfaces exist for their users, and building the full implementation before the interface settles can waste effort, since the interface shapes the implementation; when interface design runs into problems, change it and repeat (pp. 112-113).

## Why it pays

Scaffolding removes a class's interaction with other classes during its test, and it lets code buried inside another block be tested directly rather than through slow, indirect runs: a few minutes of scaffolding for code deep in the program can save hours of debugging (p. 514). It can be reused even after a defect is found in the class (p. 514). McConnell's encryption example adds that modular design is what made the driver cheap, since the crypto code could be run apart from the UI (p. 516); see [[property-based-testing]]. This wiki reads that as the design-side lesson: a unit that cannot be reached without its whole surroundings is a coupling problem before it is a testing problem (see [[coupling]] and [[logic-testable-without-ui]]).

## Which stand-in

McConnell lists the kinds of stand-in neutrally. Bugayenko, in [[prefer-fakes-over-mocks]], rejects stubbing and call verification through a mocking framework and prescribes a working fake shipped with the interface. This wiki resolves the two per setting: a stand-in that records or checks the calls it receives pins how the unit uses its collaborator, so it suits the setting where the unit's only observable effect is a call on a port (sending a message, writing an audit record) and there is no state to read back; a test about the unit's visible result is better served by a fake that behaves like a simplified real implementation, which is the brittleness argument of [[brittle-tests]].

## Cost and limits

Scaffolding is work, and a stand-in is only as faithful as its author made it. The book lists the "simpler or less accurate version" as an option; this wiki reads that as the trade-off: the less realistic the stand-in, the more the test pins the author's assumption about the collaborator rather than the collaborator, and integration still has to be tested ([[test-levels]]).

The book also suggests leaving scaffolding in the file, disabled by preprocessor directives or comments (pp. 514-515). This wiki does not transfer that: it is a language and tooling matter, and test frameworks keep scaffolding in the suite.

Weisfeld goes further: «Когда заглушки сделают свое дело, не удаляйте их», keep them hidden from users for later use, and «встраивайте функциональность для осуществления тестирования прямо в класс!» (p. 113). This wiki resolves that by setting. Keeping a stub is sound when it is a separate class implementing the same interface (an in-memory reader beside the database reader), kept with the tests or as a named fake. Building test behaviour into the production class, as a flag, mode or `if testing` branch, is not adopted: the class then carries code production never runs, behind a switch a caller can set wrongly. That branch is the sign of [[test-environment-matches-production]], which owns it. A stub also drifts: Weisfeld's `howManyRecords` returns a fixed 5 and `goToLast` a fixed position, so tests pass against a contract the real class may no longer meet.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 513-516, via [[code-complete]]; the dummy-file quotation (p. 514) is transcribed from `raw/` across a line-break hyphen and needs the page-image check. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 5, pp. 112-113, after Gilbert and McCarthy: the stub for an interface not yet implemented, `DataBaseReader`, the reasons, and the advice to keep stubs and build testing into the class; the quotations were checked against `raw/`. This wiki's own: the coupling reading, the per-setting resolutions (stand-ins against [[prefer-fakes-over-mocks]], kept stubs against test code built into the class), the routing of that branch to [[test-environment-matches-production]], the drift observation, the fidelity trade-off and the decision not to transfer in-file scaffolding.
