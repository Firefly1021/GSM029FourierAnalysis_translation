"""Register this book using existing BookPaths, preserving unrelated dirty files.

The stock new-book command requires an entirely clean main checkout. The user
explicitly authorized leaving unrelated pending edits alone on 2026-11-15.
This one-book registration performs narrower conflict checks, stages only this
new book plus its new registry row, and never changes shared implementation.
"""
from __future__ import annotations

import base64
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "shared/src"))
from mathbook.project import ProjectPaths, directory_manifest_hash, sha256_file
from mathbook.workflow import (
    ProjectRecord, read_projects, update_project_record, _write_json,
    _write_empty_tsv, _book_status_text, TERM_COLUMNS, PROPER_NAME_COLUMNS,
    NOTATION_COLUMNS,
)
from mathbook.template import verify_manifest

BOOK_ID = "an-introduction-to-partial-differential-equations"
SOURCE = Path("D:/BaiduNetdiskDownload/An Introduction to Partial Differential Equations.pdf")


def git(*args: str, data: bytes | None = None) -> bytes:
    result = subprocess.run(["git", "-C", str(ROOT), *args], input=data,
                            capture_output=True, check=True)
    return result.stdout


def register() -> None:
    project = ProjectPaths(ROOT)
    book = project.book(BOOK_ID)
    assert project.consolidated and project.git_branch() == "main"
    assert not git("diff", "--cached", "--name-only").strip(), "Existing staged changes: refuse."
    assert not book.config_file.exists(), "Already registered: refuse."
    assert not any(row.book_id == BOOK_ID for row in read_projects(project))
    assert subprocess.run(["git", "-C", str(ROOT), "show-ref", "--verify", "--quiet",
                           "refs/heads/book/" + BOOK_ID]).returncode != 0
    assert not verify_manifest(), "Shared template manifest mismatch."
    assert SOURCE.read_bytes()[:5] == b"%PDF-"
    before = {}
    entries = git("status", "--porcelain=v1", "-z", "--untracked-files=all").split(b"\0")
    for entry in entries:
        if not entry:
            continue
        name = entry[3:].decode("utf-8")
        if name.startswith(f"books/{BOOK_ID}/"):
            continue
        path = ROOT / name
        if path.is_file():
            before[name] = sha256_file(path)
    registry_before = project.projects_file.read_bytes()
    original_rows = {row.book_id: row.cells() for row in read_projects(project)}
    head_before = git("rev-parse", "HEAD").decode().strip()
    book.ensure_structure()
    digest = sha256_file(SOURCE)
    shutil.copy2(SOURCE, book.source / SOURCE.name)
    assert sha256_file(SOURCE) == sha256_file(book.source / SOURCE.name) == digest
    shutil.copytree(project.template, book.root / "template")
    shutil.copy2(project.config / "template-manifest.json", book.root / "config/template-snapshot-manifest.json")
    defaults = json.loads((project.config / "default.yaml").read_text(encoding="utf-8"))
    config = {
        "schema_version": 1, "book_id": BOOK_ID,
        "title": "An Introduction to Partial Differential Equations",
        "branch": "book/" + BOOK_ID, "active_branch": "main",
        "worktree": str(ROOT), "phase": "registration", "status": "registered",
        "source": {"path": "input/source/" + SOURCE.name, "sha256": digest,
                   "original_path": str(SOURCE)},
        "template_version": defaults["template"]["version"],
        "template_manifest_hash": directory_manifest_hash(book.template), "final_output": "",
    }
    _write_json(book.config_file, config)
    _write_json(book.root / "config/library-binding.json", {
        "mode": "unified", "book_id": BOOK_ID, "book_root": "books/" + BOOK_ID,
        "entry": "tex/main.tex", "checkpoint_branch": "book/" + BOOK_ID,
    })
    for path, columns in [(book.candidates, TERM_COLUMNS), (book.unresolved, TERM_COLUMNS),
                          (book.proper_names, PROPER_NAME_COLUMNS), (book.notation, NOTATION_COLUMNS)]:
        _write_empty_tsv(path, columns)
    book.issues.write_text("", encoding="utf-8")
    _write_json(book.workflow_state, {"book_id": BOOK_ID, "status": "registered",
                                    "completed_units": [], "blocking_issues": []})
    book.status_file.write_text(_book_status_text(BOOK_ID, "registration", "registered", digest, []), encoding="utf-8")
    book.plans_file.write_text("# Sample-only plan\n\n1. Diagnose all source pages.\n2. Restore and verify a representative sample against page images.\n3. Translate the verified sample, compile and run QA.\n4. Stop at awaiting-sample-approval; no full translation or push.\n", encoding="utf-8")
    record = ProjectRecord(BOOK_ID, config["title"], "main", str(ROOT), "registration",
                           "registered", digest, config["template_version"], "", "")
    update_project_record(project, record)
    assert {row.book_id: row.cells() for row in read_projects(project) if row.book_id != BOOK_ID} == original_rows
    changed = [name for name, value in before.items()
               if name != "shared/PROJECTS.md" and sha256_file(ROOT / name) != value]
    assert not changed, changed
    _write_json(book.qa / "registration-integrity.json", {
        "method": "existing BookPaths/workflow helpers with scoped dirty-tree registration",
        "reason": "User authorized unified layout and preserving unrelated pending edits.",
        "stock_command_result": "refused: main worktree not clean",
        "main_head_before": head_before, "pending_files_before": before,
        "registry_working_copy_before_base64": base64.b64encode(registry_before).decode(),
        "other_registry_rows_preserved": True, "unrelated_pending_files_preserved": True,
        "source_sha256": digest, "template_manifest_hash": config["template_manifest_hash"],
        "remote_write": False,
    })
    # Stage the new book, but build the registry index blob from HEAD, not from
    # the working copy: the user's pre-existing FEEC registry edit stays unstaged.
    git("add", "--", "books/" + BOOK_ID)
    head_registry = git("show", "HEAD:shared/PROJECTS.md").decode("utf-8")
    row_text = "| " + " | ".join(record.cells()) + " |\n"
    marker = "|" + "|".join("---" for _ in record.cells()) + "|\n"
    assert head_registry.count(marker) == 1
    staged_registry = head_registry.replace(marker, marker + row_text, 1).encode("utf-8")
    blob = git("hash-object", "-w", "--stdin", data=staged_registry).decode().strip()
    git("update-index", "--cacheinfo", "100644," + blob + ",shared/PROJECTS.md")
    staged = git("diff", "--cached", "--name-only").decode().splitlines()
    assert all(p.startswith("books/" + BOOK_ID + "/") or p == "shared/PROJECTS.md" for p in staged)
    git("commit", "-m", "Register An Introduction to Partial Differential Equations (sample only)")
    git("branch", "book/" + BOOK_ID)
    print(json.dumps({"book_id": BOOK_ID, "active_branch": "main",
                      "checkpoint_branch": "book/" + BOOK_ID, "workspace": str(ROOT),
                      "initial_commit": git("rev-parse", "HEAD").decode().strip(),
                      "source_sha256": digest, "unrelated_changes_preserved": True}, indent=2))


if __name__ == "__main__":
    register()
