"""Tests for verify_compressed: each check catches the loss it exists for, and passes a fair compression."""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from verify_compressed import compare, main  # noqa: E402

READABLE = """---
title: WIP Control
sources: [kanban-guide]
---

# WIP Control

A board should limit the number of items in progress, because work that is started and not finished
does not help anyone.

> Controlling WIP is the practice of limiting the items in progress.
>
> — [[kanban-guide]], L58

This wiki reads that as a rule about the moment, not the period. The Guide gives "no number and no
method" for the limit (L60-L62), so a project with 3 people should not copy a limit of 5.

## Sign of violation

- More items in progress than people, as on [[wip-per-executor]].

```text
limit = throughput / replenishments
```
"""

FAIR = """---
title: WIP Control
sources: [kanban-guide]
---

# WIP Control

Board limits items in progress, because started and not finished work does not help anyone.

> Controlling WIP is the practice of limiting the items in progress.
>
> — [[kanban-guide]], L58

This wiki reads that as a rule about the moment, not the period. Guide gives "no number and no
method" for limit (L60-L62); project with 3 people should not copy limit of 5.

## Sign of violation

- More items in progress than people, see [[wip-per-executor]].

```text
limit = throughput / replenishments
```
"""


def test_fair_compression_passes():
    assert compare(READABLE, FAIR) == []


def test_identical_page_passes():
    assert compare(READABLE, READABLE) == []


def test_reworded_blockquote_fails():
    bad = FAIR.replace("the practice of limiting", "limiting")
    assert any("blockquotes" in p for p in compare(READABLE, bad))


def test_changed_sentence_after_blockquote_fails():
    bad = FAIR.replace("This wiki reads that as a rule", "A rule")
    assert any("sentence after a blockquote" in p for p in compare(READABLE, bad))


def test_reworded_inline_quotation_fails():
    bad = FAIR.replace('"no number and no\nmethod"', '"no number or method"')
    problems = compare(READABLE, bad)
    assert any("quotations lost: 'no number and no method'" in p for p in problems)


def test_reflowed_quotation_passes():
    reflowed = FAIR.replace('"no number and no\nmethod"', '"no number and no method"')
    assert compare(READABLE, reflowed) == []


def test_sentence_after_blockquote_is_read_across_lines():
    readable = "> A quote here.\n\nThis wiki reads that\nas a rule. More.\n"
    assert compare(readable, "> A quote here.\n\nThis wiki reads that as a rule. Less.\n") == []
    bad = "> A quote here.\n\nThis wiki reads it as a rule. More.\n"
    assert any("sentence after a blockquote" in p for p in compare(readable, bad))


def test_dropped_wikilink_fails():
    bad = FAIR.replace(", see [[wip-per-executor]]", "")
    assert any("wikilinks lost" in p for p in compare(READABLE, bad))


def test_changed_line_citation_fails():
    bad = FAIR.replace("(L60-L62)", "(L60)")
    problems = compare(READABLE, bad)
    assert any("line citations" in p for p in problems)


def test_changed_number_fails():
    bad = FAIR.replace("limit of 5", "limit of 4")
    assert any("numbers" in p for p in compare(READABLE, bad))


def test_dropped_negation_fails():
    bad = FAIR.replace("should not copy", "should copy")
    assert any("negations lost" in p for p in compare(READABLE, bad))


def test_contraction_is_the_same_negation():
    readable = "It does not hold.\n"
    assert compare(readable, "It doesn't hold.\n") == []


def test_changed_frontmatter_fails():
    bad = FAIR.replace("title: WIP Control", "title: WIP")
    assert "frontmatter changed" in compare(READABLE, bad)


def test_changed_heading_fails():
    bad = FAIR.replace("## Sign of violation", "## Signs")
    assert any("headings" in p for p in compare(READABLE, bad))


def test_changed_code_block_fails():
    bad = FAIR.replace("throughput / replenishments", "throughput")
    assert any("code blocks" in p for p in compare(READABLE, bad))


def test_reordered_sections_are_reported():
    readable = "# A\n\n## One\n\nx\n\n## Two\n\ny\n"
    compressed = "# A\n\n## Two\n\ny\n\n## One\n\nx\n"
    assert any("reordered" in p for p in compare(readable, compressed))


def test_number_inside_a_word_is_not_a_number():
    assert compare("Use the 6x2 plan.\n", "Use 6x2 plan.\n") == []


def test_crlf_does_not_count_as_a_change():
    assert compare(READABLE, FAIR.replace("\n", "\r\n")) == []


def test_pair_cli_reports_failure(tmp_path, capsys):
    a, b = tmp_path / "a.md", tmp_path / "b.md"
    a.write_text(READABLE, encoding="utf-8")
    b.write_text(FAIR.replace("should not copy", "should copy"), encoding="utf-8")
    assert main(["--pair", str(a), str(b)]) == 1
    assert "negations lost" in capsys.readouterr().out


def test_ref_cli_compares_against_git(tmp_path, capsys):
    root = tmp_path / "knowledge"
    page = root / "wiki" / "group" / "page.md"
    page.parent.mkdir(parents=True)
    (root / "SCHEMA.md").write_text("# Schema\n\nNot compressed here.\n", encoding="utf-8")
    page.write_text(READABLE, encoding="utf-8")
    git = ["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(git[:3] + ["init", "-q"], check=True)
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["commit", "-qm", "readable"], check=True)
    subprocess.run(git + ["tag", "readable"], check=True)
    page.write_text(FAIR, encoding="utf-8")
    assert main(["--root", str(root), "--ref", "readable"]) == 0
    page.write_text(FAIR.replace("[[kanban-guide]], L58", "[[kanban-guide]]"), encoding="utf-8")
    assert main(["--root", str(root), "--ref", "readable"]) == 1
    assert "FAIL" in capsys.readouterr().out


def test_missing_ref_is_a_usage_error(tmp_path):
    root = tmp_path / "knowledge"
    (root / "wiki").mkdir(parents=True)
    (root / "SCHEMA.md").write_text("# S\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], check=True)
    assert main(["--root", str(root), "--ref", "no-such-tag"]) == 2
