"""Tests for repair_compressed: a model error never writes, and a restore never discards newer edits."""

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import repair_compressed as rc  # noqa: E402
from test_verify_compressed import FAIR, READABLE  # noqa: E402

BAD = FAIR.replace("should not copy", "should copy")


def git(tmp_path, *args):
    subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t", *args],
                   check=True, capture_output=True)


@pytest.fixture
def base(tmp_path):
    root = tmp_path / "knowledge"
    page = root / "wiki" / "page.md"
    page.parent.mkdir(parents=True)
    page.write_text(READABLE, encoding="utf-8")
    subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], check=True)
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-qm", "readable")
    git(tmp_path, "tag", "readable")
    return root, page


def model(monkeypatch, *replies):
    calls = iter(replies)

    def fake(prompt, timeout=rc.TIMEOUT):
        r = next(calls)
        if isinstance(r, Exception):
            raise r
        return r
    monkeypatch.setattr(rc, "_claude", fake)


def test_repaired(base, monkeypatch, capsys):
    root, page = base
    page.write_text(BAD, encoding="utf-8")
    model(monkeypatch, FAIR)
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 0
    assert page.read_text(encoding="utf-8") == FAIR and "repaired" in capsys.readouterr().out


def test_error_reply_is_not_a_page_and_writes_nothing(base, monkeypatch, capsys):
    root, page = base
    page.write_text(BAD, encoding="utf-8")
    model(monkeypatch, "API Error: rate limited\n")
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 2
    assert page.read_text(encoding="utf-8") == BAD
    assert "API Error" in capsys.readouterr().err


def test_timeout_writes_nothing(base, monkeypatch):
    root, page = base
    page.write_text(BAD, encoding="utf-8")
    model(monkeypatch, rc.ModelError("claude did not answer in 600 s"))
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 2
    assert page.read_text(encoding="utf-8") == BAD


def test_claude_timeout_is_caught(monkeypatch):
    monkeypatch.setattr(rc.shutil, "which", lambda name: "claude")

    def hang(*a, **kw):
        raise subprocess.TimeoutExpired(cmd="claude", timeout=kw.get("timeout"))
    monkeypatch.setattr(rc.subprocess, "run", hang)
    with pytest.raises(rc.ModelError, match="did not answer"):
        rc._claude("p", timeout=1)


def test_missing_claude_is_exit_2(base, monkeypatch, capsys):
    root, page = base
    page.write_text(BAD, encoding="utf-8")
    monkeypatch.setattr(rc.shutil, "which", lambda name: None)
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 2
    assert "claude" in capsys.readouterr().err and page.read_text(encoding="utf-8") == BAD


def test_restored_when_only_compression_changed_it(base, monkeypatch, capsys):
    root, page = base
    page.write_text(BAD, encoding="utf-8")  # uncommitted: HEAD still holds the ref text
    model(monkeypatch, BAD, BAD)
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 3
    assert page.read_text(encoding="utf-8") == READABLE
    assert "restored" in capsys.readouterr().out


def test_not_restored_when_committed_after_the_ref(base, monkeypatch, capsys):
    root, page = base
    newer = READABLE.replace("## Sign of violation", "## Sign of violation\n\nA newer line.")
    page.write_text(newer, encoding="utf-8")
    git(root.parent, "commit", "-qam", "edit after release")
    page.write_text(newer.replace("should not copy", "should copy"), encoding="utf-8")
    model(monkeypatch, BAD, BAD)
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 1
    assert "should copy" in page.read_text(encoding="utf-8")  # left as is
    assert "not restored" in capsys.readouterr().out


def test_restored_when_the_backup_matches_the_ref(base, monkeypatch):
    root, page = base
    page.write_text(BAD, encoding="utf-8")
    git(root.parent, "commit", "-qam", "compressed")
    page.with_name("page.original.md").write_text(READABLE, encoding="utf-8")
    model(monkeypatch, BAD, BAD)
    assert rc.main(["--root", str(root), "--ref", "readable", str(page)]) == 3
    assert page.read_text(encoding="utf-8") == READABLE


def test_git_error_message_is_text(base, capsys):
    root, page = base
    assert rc.main(["--root", str(root), "--ref", "no-such-tag", str(page)]) == 2
    err = capsys.readouterr().err
    assert "b'" not in err and "no-such-tag" in err
