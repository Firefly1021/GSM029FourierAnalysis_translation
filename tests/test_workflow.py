"""Git/worktree, path-isolation, terminology, resume, and finish tests."""

from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfWriter

from mathbook.project import ProjectError, ProjectPaths, run_git
from mathbook.terminology import HISTORY_COLUMNS, TERM_COLUMNS, _read_tsv, find_conflicts, promote_candidates
from mathbook.workflow import (
    approve_sample,
    book_status,
    finish_book,
    isolate_book_worktree,
    list_books,
    new_book,
    next_incomplete_unit,
    project_record,
    resume_book,
    start_book,
    update_project_record,
    verify_book_context,
)


def write_tsv(path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class TerminologyTests(unittest.TestCase):
    def test_domain_specific_meanings_coexist_and_exact_key_conflicts(self) -> None:
        base = {column: "" for column in TERM_COLUMNS}
        rows = [
            {**base, "English": "field", "Preferred Chinese": "域", "Domain": "algebra", "Context": "scalar field", "Status": "approved"},
            {**base, "English": "field", "Preferred Chinese": "场", "Domain": "mathematical physics", "Context": "physical field", "Status": "approved"},
        ]
        self.assertEqual(find_conflicts(rows), [])
        rows.append({**rows[0], "Preferred Chinese": "场"})
        self.assertEqual(len(find_conflicts(rows)), 1)

    def test_safe_promotion_deduplicates_without_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = ProjectPaths(root)
            book = project.book("test-book")
            book.ensure_structure()
            write_tsv(project.glossary / "terminology.tsv", TERM_COLUMNS, [])
            write_tsv(project.glossary / "terminology-history.tsv", HISTORY_COLUMNS, [])
            base = {column: "" for column in TERM_COLUMNS}
            candidate = {
                **base, "English": "candidate", "Preferred Chinese": "候选", "Domain": "analysis",
                "Context": "controlled test", "Status": "proposed", "First Source": "test-book",
                "First Location": "unit-1", "Notes": "[safe-to-promote] reviewed fixture",
            }
            write_tsv(book.candidates, TERM_COLUMNS, [candidate, candidate])
            result = promote_candidates(project, book)
            self.assertEqual(result["promoted"], 1)
            self.assertEqual(result["duplicates_removed"], 1)
            self.assertEqual(len(_read_tsv(project.glossary / "terminology.tsv", TERM_COLUMNS)), 1)
            self.assertEqual(len(_read_tsv(project.glossary / "terminology-history.tsv", HISTORY_COLUMNS)), 1)


class WorktreeIsolationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.root = base / "repo"
        self.root.mkdir()
        (self.root / "config").mkdir()
        (self.root / "template" / "style").mkdir(parents=True)
        (self.root / "template" / "reference").mkdir()
        (self.root / "template" / "assets").mkdir()
        (self.root / "template" / "adapter").mkdir()
        (self.root / "glossary").mkdir()
        (self.root / "books").mkdir()
        (self.root / "template" / "style" / "test.sty").write_text("% read-only fixture\n", encoding="utf-8")
        (self.root / "config" / "default.yaml").write_text(json.dumps({
            "template": {"version": "test-v1"},
            "automation": {"sample_processor": [], "translation_processor": [], "finish_processor": []},
        }), encoding="utf-8")
        write_tsv(self.root / "glossary" / "terminology.tsv", TERM_COLUMNS, [])
        write_tsv(self.root / "glossary" / "terminology-history.tsv", HISTORY_COLUMNS, [])
        (self.root / "PROJECTS.md").write_text("# Translation projects\n", encoding="utf-8")
        (self.root / ".gitattributes").write_text("*.pdf binary\n", encoding="utf-8")
        run_git(self.root, ["init", "-b", "main"])
        run_git(self.root, ["config", "user.name", "Test User"])
        run_git(self.root, ["config", "user.email", "test@example.invalid"])
        run_git(self.root, ["add", "."])
        run_git(self.root, ["commit", "-m", "Initial test system"])
        self.sources = base / "sources"
        self.sources.mkdir()
        for name in ("a", "b"):
            writer = PdfWriter()
            writer.add_blank_page(width=72, height=72)
            with (self.sources / f"{name}.pdf").open("wb") as handle:
                writer.write(handle)
        self.project = ProjectPaths(self.root)
        self.a = new_book(self.project, "test-book-a", self.sources / "a.pdf")
        self.b = new_book(self.project, "test-book-b", self.sources / "b.pdf")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_two_branches_worktrees_and_book_data_are_isolated(self) -> None:
        self.assertNotEqual(self.a["branch"], self.b["branch"])
        self.assertNotEqual(self.a["worktree"], self.b["worktree"])
        a_project = ProjectPaths(Path(self.a["worktree"]))
        b_project = ProjectPaths(Path(self.b["worktree"]))
        self.assertEqual(
            run_git(b_project.root, ["config", "--worktree", "--get", "core.sparseCheckout"]).stdout.strip(),
            "true",
        )
        self.assertFalse((b_project.books / "test-book-a").exists())
        self.assertTrue((b_project.books / "test-book-b").is_dir())
        self.assertTrue(
            run_git(b_project.root, ["ls-files", "--", "books/test-book-a"]).stdout.strip(),
            "Sparse checkout must hide the prior book without deleting it from the branch index.",
        )
        a_book, _ = verify_book_context(a_project, "test-book-a", writable=True)
        b_book, _ = verify_book_context(b_project, "test-book-b", writable=True)
        a_label = a_book.assert_write_path(a_book.root / "tex" / "chapters" / "same-label.tex")
        a_label.write_text("\\label{eq:same}\n", encoding="utf-8")
        self.assertFalse((b_book.root / "tex" / "chapters" / "same-label.tex").exists())
        b_label = b_book.assert_write_path(b_book.root / "tex" / "chapters" / "same-label.tex")
        b_label.write_text("\\label{eq:same}\n", encoding="utf-8")
        self.assertEqual(a_label.read_text(encoding="utf-8"), b_label.read_text(encoding="utf-8"))
        with self.assertRaises(ProjectError):
            a_book.assert_write_path(b_book.root / "qa" / "forbidden.json")
        self.assertEqual(
            (a_project.glossary / "terminology.tsv").read_bytes(),
            (b_project.glossary / "terminology.tsv").read_bytes(),
        )
        self.assertEqual({item["book_id"] for item in list_books(b_project)}, {"test-book-a", "test-book-b"})
        hidden_record = project_record(b_project, "test-book-a")
        hidden_record.phase = "completed"
        hidden_record.status = "completed"
        update_project_record(b_project, hidden_record)
        self.assertEqual(book_status(b_project, "test-book-a")["status"], "completed")

    def test_isolation_is_idempotent_and_preserves_current_book_changes(self) -> None:
        a_project = ProjectPaths(Path(self.a["worktree"]))
        changed = a_project.book("test-book-a").root / "tex" / "chapters" / "manual-edit.tex"
        changed.write_text("% manual book-local edit\n", encoding="utf-8")
        before = a_project.git_status()
        result = isolate_book_worktree(a_project, "test-book-a")
        self.assertEqual(result["visible_books"], ["test-book-a"])
        self.assertEqual(a_project.git_status(), before)
        self.assertEqual(changed.read_text(encoding="utf-8"), "% manual book-local edit\n")

    def test_isolation_refuses_foreign_book_changes(self) -> None:
        b_project = ProjectPaths(Path(self.b["worktree"]))
        run_git(b_project.root, ["sparse-checkout", "disable"])
        foreign = b_project.books / "test-book-a" / "PROJECT_STATUS.md"
        foreign.write_text(foreign.read_text(encoding="utf-8") + "foreign edit\n", encoding="utf-8")
        with self.assertRaisesRegex(ProjectError, "another book has uncommitted files"):
            isolate_book_worktree(b_project, "test-book-b")

    def test_mismatch_resume_and_finish_safety(self) -> None:
        with self.assertRaises(ProjectError):
            verify_book_context(self.project, "test-book-a", writable=True)
        a_project = ProjectPaths(Path(self.a["worktree"]))
        a_book, _ = verify_book_context(a_project, "test-book-a", writable=True)
        a_book.chapter_progress.write_text(
            "Unit ID\tQA Status\nunit-1\tpassed\nunit-2\tpending\n", encoding="utf-8"
        )
        state = json.loads(a_book.workflow_state.read_text(encoding="utf-8"))
        state.update({"status": "registered", "completed_units": ["unit-1"]})
        a_book.workflow_state.write_text(json.dumps(state), encoding="utf-8")
        result = resume_book(a_project, "test-book-a")
        self.assertEqual(result["next_unit"], "unit-2")
        self.assertEqual(next_incomplete_unit(a_book), "unit-2")

        a_book.chapter_progress.write_text("Unit ID\tQA Status\nunit-1\tpassed\n", encoding="utf-8")
        run_git(a_project.root, ["add", "--", "books/test-book-a"])
        run_git(a_project.root, ["commit", "-m", "Prepare completed test book"])

        def final_processor(book):
            (book.root / "qa" / "final-report.json").write_text('{"passed": true}\n', encoding="utf-8")
            (book.root / "output" / "book-zh.pdf").write_bytes((self.sources / "a.pdf").read_bytes())

        result = finish_book(a_project, "test-book-a", processor=final_processor)
        self.assertEqual(result["status"], "completed")
        branches = run_git(self.root, ["branch", "--format=%(refname:short)"]).stdout.splitlines()
        self.assertIn("book/test-book-a", branches)
        worktrees = self.project.git_worktree_map()
        self.assertIn(str(Path(self.a["worktree"]).resolve()).lower(), {key.lower() for key in worktrees})

    def test_start_and_approve_sample_use_book_state_only(self) -> None:
        a_project = ProjectPaths(Path(self.a["worktree"]))
        before_projects = (a_project.root / "PROJECTS.md").read_bytes()

        def sample_processor(book):
            sample = book.root / "translation" / "reviewed" / "sample.tex"
            sample.parent.mkdir(parents=True, exist_ok=True)
            sample.write_text("% reviewed test fixture\n", encoding="utf-8")
            (book.root / "qa" / "sample-qa.json").write_text(json.dumps({
                "template": "passed", "formula": "passed", "cross_references": "passed", "compile": "passed"
            }), encoding="utf-8")

        started = start_book(a_project, "test-book-a", processor=sample_processor)
        self.assertEqual(started["status"], "awaiting-sample-approval")
        approved = approve_sample(a_project, "test-book-a")
        self.assertEqual(approved["status"], "ready-for-full-translation")
        self.assertEqual(before_projects, (a_project.root / "PROJECTS.md").read_bytes())

    def test_automation_rejects_remote_push(self) -> None:
        with self.assertRaises(ProjectError):
            run_git(self.root, ["push", "origin", "main"])


if __name__ == "__main__":
    unittest.main()
