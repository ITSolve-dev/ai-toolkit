import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_pages  # noqa: E402

RULE_PAGE = """---
title: Tell, don't ask
category: objects
summary: A caller reads an object's fields and then decides for it.
tags: [rule, encapsulation]
paradigm: oop
sources: [summary-pragmatic]
created: 2026-11-01
updated: 2026-11-01
---

A rather long and quite wordy lead paragraph with filler in it.

## Rule

Give the object the decision. It does not hold for 3 kinds of value.

## Sign in code

A caller branches on data it read from the object.

## When not to apply

Plain data records and generated types have no behaviour to move.

## Repair

Move the branch into the object that owns the data.

## Before and after

```
if account.balance > amount: account.balance -= amount
account.withdraw(amount)
```

## Source

[[summary-pragmatic]], Russian edition, p. 123.
"""


def wiki(base: Path, pages: dict[str, str]) -> Path:
    (base / "wiki").mkdir(parents=True)
    (base / "SCHEMA.md").write_text("# schema\n", encoding="utf-8")
    for relative, text in pages.items():
        path = base / "wiki" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return base


class CheckPage(unittest.TestCase):
    def problems(self, text: str, name: str = "objects/page.md") -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            return check_pages.check_wiki(wiki(Path(tmp), {name: text}))

    def assertReports(self, text: str, fragment: str):
        problems = self.problems(text)
        self.assertTrue(any(fragment in p for p in problems), problems)

    def test_good_rule_page_passes(self):
        self.assertEqual(self.problems(RULE_PAGE), [])

    def test_missing_section_is_reported(self):
        self.assertReports(RULE_PAGE.replace("## When not to apply", "## Limits"), "When not to apply")

    def test_sections_out_of_order_are_reported(self):
        text = RULE_PAGE.replace("## Rule", "## TEMP", 1).replace("## Repair", "## Rule").replace("## TEMP", "## Repair")
        self.assertReports(text, "out of order")

    def test_empty_section_is_reported(self):
        text = RULE_PAGE.replace("A caller branches on data it read from the object.\n", "")
        self.assertReports(text, "token section: Sign in code")

    def test_token_section_is_reported(self):
        for token in ("TODO", "N/A", "See above.", "<!-- later -->", "### Note"):
            text = RULE_PAGE.replace("A caller branches on data it read from the object.", token)
            self.assertReports(text, "token section: Sign in code")

    def test_paradigm_is_required(self):
        self.assertReports(RULE_PAGE.replace("paradigm: oop\n", ""), "paradigm")

    def test_summary_page_needs_no_paradigm(self):
        text = "---\ntitle: T\ncategory: objects\ntags: [summary]\nsources: []\n---\n\nBody.\n"
        self.assertEqual(self.problems(text), [])

    def test_category_must_equal_folder(self):
        self.assertReports(RULE_PAGE.replace("category: objects", "category: naming"), "category")

    def test_block_list_sources_are_reported(self):
        text = RULE_PAGE.replace("sources: [summary-pragmatic]", "sources:\n  - summary-pragmatic")
        self.assertReports(text, "inline list")

    def test_language_tagged_fence_is_reported(self):
        self.assertReports(RULE_PAGE.replace("```\nif account", "```python\nif account"), "names a language: python")

    def test_language_tag_on_indented_or_unclosed_fence_is_reported(self):
        self.assertReports(RULE_PAGE + "\n1. Step:\n\n   ```python\n   x()\n   ```\n", "names a language")
        self.assertReports(RULE_PAGE + "\n```python\nx()\n", "names a language")

    def test_section_heading_inside_code_is_not_a_section(self):
        self.assertEqual(self.problems(RULE_PAGE.replace("account.withdraw(amount)", "account.withdraw(amount)\n## Rule")), [])

    def test_empty_fence_does_not_count_as_a_pair(self):
        text = RULE_PAGE.replace("if account.balance > amount: account.balance -= amount\naccount.withdraw(amount)\n", "")
        self.assertReports(text, "no fenced pseudocode")

    def test_source_without_link_is_reported(self):
        self.assertReports(RULE_PAGE.replace("[[summary-pragmatic]], Russian", "Russian"), "links to no source")

    def test_link_inside_code_does_not_count(self):
        text = RULE_PAGE.replace("[[summary-pragmatic]], Russian", "`[[summary-pragmatic]]`, Russian")
        self.assertReports(text, "links to no source")

    def test_self_authored_page_needs_no_source_link(self):
        text = RULE_PAGE.replace("sources: [summary-pragmatic]", "sources: []").replace(
            "[[summary-pragmatic]], Russian edition, p. 123.", "Written by this wiki: no source treats it yet."
        )
        self.assertEqual(self.problems(text), [])

    def test_nested_group_is_reported(self):
        self.assertTrue(any("flat" in p for p in self.problems(RULE_PAGE, "objects/deep/page.md")))

    def test_loose_page_is_reported(self):
        self.assertTrue(any("group folder" in p for p in self.problems(RULE_PAGE, "loose.md")))

    def test_root_pages_are_exempt(self):
        for name in ("index.md", "overview.md", "synthesis.md"):
            self.assertEqual(self.problems("# no frontmatter\n", name), [])


class ComparePage(unittest.TestCase):
    def changed(self, after: str, before: str = RULE_PAGE) -> list[str]:
        return check_pages.compare_page(before, after)

    def page_with(self, block: str) -> str:
        return RULE_PAGE.replace("A rather long", f"{block}\n\nA rather long")

    def assertCaught(self, before_block: str, after_block: str):
        before, after = self.page_with(before_block), self.page_with(after_block)
        self.assertNotEqual(before, after)
        self.assertNotEqual(check_pages.compare_page(before, after), [], before_block)

    def test_filler_may_be_removed(self):
        after = RULE_PAGE.replace("A rather long and quite wordy lead paragraph with filler in it.", "A lead paragraph.")
        self.assertEqual(self.changed(after), [])

    def test_rewrapped_prose_passes(self):
        self.assertEqual(self.changed(RULE_PAGE.replace("does not hold", "does\nnot hold")), [])

    def test_updated_date_may_change(self):
        self.assertEqual(self.changed(RULE_PAGE.replace("updated: 2026-11-01", "updated: 2026-11-02")), [])

    def test_deleted_updated_line_is_caught(self):
        self.assertIn("frontmatter changed", self.changed(RULE_PAGE.replace("updated: 2026-11-01\n", "")))

    def test_dropped_negation_is_caught(self):
        self.assertIn("guarded sentences changed", self.changed(RULE_PAGE.replace("It does not hold", "It holds")))

    def test_moved_negation_is_caught(self):
        self.assertCaught("Retries are not safe here. Caching is safe here.", "Retries are safe here. Caching is not safe here.")
        self.assertCaught("Never mock the clock. Mock the network.", "Mock the clock. Never mock the network.")

    def test_changed_negative_words_are_caught(self):
        for old, new in (
            ("Neither works.", "Either works."),
            ("Nothing breaks.", "Everything breaks."),
            ("It rarely fails.", "It often fails."),
            ("Это не работает.", "Это работает."),
            ("A non-empty list.", "An empty list."),
        ):
            self.assertCaught(old, new)

    def test_changed_numbers_are_caught(self):
        for old, new in (
            ("Use 3 kinds.", "Use 4 kinds."),
            ("Use three kinds.", "Use four kinds."),
            ("Offset -5 here.", "Offset 5 here."),
            ("Keep ≥ 3 items.", "Keep ≤ 3 items."),
            ("Wait 3 ms now.", "Wait 3 s now."),
            ("Use 50% here.", "Use 50 here."),
            ("Возьмите три шага.", "Возьмите четыре шага."),
        ):
            self.assertCaught(old, new)

    def test_changed_code_is_caught(self):
        self.assertIn("code blocks changed", self.changed(RULE_PAGE.replace("withdraw(amount)", "withdraw(sum)")))

    def test_every_fence_shape_is_protected(self):
        for shape in (
            "1. Step:\n\n   ```\n   foo()\n   ```",
            "````\n```\nfoo()\n```\n````",
            "~~~\n```\nfoo()\n~~~",
            "```\nfoo()\n~~~\nbar\n```",
            "    foo()",
        ):
            self.assertCaught(shape, shape.replace("foo()", "baz()"))

    def test_removed_list_fence_is_caught(self):
        self.assertCaught("1. Run:\n\n   ```\n   git bisect run ./check\n   ```", "1. Run the check.")

    def test_unclosed_fence_is_protected(self):
        before = RULE_PAGE + "\n```\nfoo()\n"
        self.assertIn("code blocks changed", self.changed(before.replace("foo()", "baz()"), before))

    def test_source_section_is_protected(self):
        self.assertIn("protected sections changed", self.changed(RULE_PAGE.replace("Russian edition", "Russian ed.")))

    def test_limit_section_is_protected(self):
        after = RULE_PAGE.replace("records and generated types have", "records have")
        self.assertIn("protected sections changed", self.changed(after))

    def test_source_variants_are_protected(self):
        for heading in ("## Sources", "### Source"):
            before = self.page_with(f"{heading}\n\nSome book, edition one.\n\n## Next")
            self.assertIn("protected sections changed", self.changed(before.replace("edition one", "first ed"), before))

    def test_first_of_two_source_sections_is_protected(self):
        before = RULE_PAGE.replace("## Rule", "## Source\n\nFirst source line.\n\n## Rule", 1)
        self.assertIn("protected sections changed", self.changed(before.replace("First source", "Earlier source"), before))

    def test_wikilink_is_protected(self):
        self.assertCaught("See [[other-page]] now.", "See [[another-page]] now.")

    def test_block_quote_is_protected(self):
        self.assertCaught("> Цитата из книги.", "> Цитата книги.")

    def test_lazy_and_listed_block_quotes_are_protected(self):
        self.assertCaught("> Цитата из книги\nпродолжается здесь.", "> Цитата из книги\nидёт здесь.")
        self.assertCaught("- > Цитата из книги.", "- > Цитата книги.")

    def test_inline_quotations_are_protected(self):
        for shape in ("«{}»", "„{}“", "“{}”", "“{}“", "‘{}’", "'{}'", '"{}"'):
            before = "The book says " + shape.format("плохой код живёт долго") + " here."
            after = "The book says " + shape.format("плохой код живёт дольше") + " here."
            self.assertCaught(before, after)

    def test_wrapped_straight_quotation_is_protected(self):
        self.assertCaught('The book says "плохой\nкод живёт".', 'The book says "плохой\nкод живет".')

    def test_inch_mark_does_not_hide_a_quotation(self):
        self.assertCaught('A wide screen: "плохой код".', 'A wide screen: "плохой кот".')
        self.assertCaught('A 5" screen and "плохой код" here.', 'A 5" screen and "плохой кот" here.')

    def test_spacing_inside_a_quotation_is_protected(self):
        self.assertCaught("Says «плохой код» here.", "Says «плохой код» here.")
        self.assertCaught("Says «плохой  код» here.", "Says «плохой код» here.")

    def test_wrapped_inline_code_is_protected(self):
        self.assertCaught("Run `foo\nbar` here.", "Run `foo\nbaz` here.")

    def test_frontmatter_is_protected(self):
        self.assertIn("frontmatter changed", self.changed(RULE_PAGE.replace("paradigm: oop", "paradigm: any")))


class CompareWiki(unittest.TestCase):
    def test_removed_and_added_pages_are_caught(self):
        with tempfile.TemporaryDirectory() as tmp:
            new = wiki(Path(tmp) / "new", {"objects/b.md": RULE_PAGE})
            old = wiki(Path(tmp) / "old", {"objects/a.md": RULE_PAGE})
            problems = check_pages.compare_wiki(new, old)
        self.assertTrue(any("removed" in p for p in problems))
        self.assertTrue(any("added" in p for p in problems))

    def test_only_the_root_index_is_skipped(self):
        changed = RULE_PAGE.replace("paradigm: oop", "paradigm: any")
        with tempfile.TemporaryDirectory() as tmp:
            new = wiki(Path(tmp) / "new", {"objects/index.md": changed, "index.md": "new\n"})
            old = wiki(Path(tmp) / "old", {"objects/index.md": RULE_PAGE, "index.md": "old\n"})
            problems = check_pages.compare_wiki(new, old)
        self.assertEqual(problems, ["wiki/objects/index.md: frontmatter changed"])


class Usage(unittest.TestCase):
    def test_schema_without_wiki_is_bad_usage(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "SCHEMA.md").write_text("x", encoding="utf-8")
            sys.argv = ["check_pages.py", tmp]
            self.assertEqual(check_pages.main(), 2)


if __name__ == "__main__":
    unittest.main()
