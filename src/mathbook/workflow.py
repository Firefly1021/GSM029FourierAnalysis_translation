"""High-level, local-only orchestration for isolated book workflows."""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence

from .project import (
    BookPaths,
    ProjectError,
    ProjectPaths,
    directory_manifest_hash,
    load_json_yaml,
    run_git,
    sha256_file,
    validate_book_id,
)
from .terminology import HISTORY_COLUMNS, TERM_COLUMNS, initialize_tsv, promote_candidates, review_candidates


PROJECT_COLUMNS = (
    "Book ID", "Title", "Branch", "Worktree", "Phase", "Status", "Source Hash",
    "Template Version", "Final Output", "Blocking Issues",
)
PROPER_NAME_COLUMNS = (
    "Source Form", "Canonical Form", "Category", "First Occurrence", "Language or Script",
    "Preserve Exactly", "Review Status", "Notes",
)
NOTATION_COLUMNS = (
    "Source Notation", "Canonical Notation", "Meaning", "Scope", "First Occurrence",
    "Preserve Exactly", "Review Status", "Notes",
)


@dataclass
class ProjectRecord:
    book_id: str
    title: str
    branch: str
    worktree: str
    phase: str
    status: str
    source_hash: str
    template_version: str
    final_output: str
    blocking_issues: str

    def cells(self) -> list[str]:
        return [
            self.book_id, self.title, self.branch, self.worktree, self.phase, self.status,
            self.source_hash, self.template_version, self.final_output, self.blocking_issues,
        ]


def _escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def read_projects(project: ProjectPaths) -> list[ProjectRecord]:
    if not project.projects_file.exists():
        return []
    rows: list[ProjectRecord] = []
    for line in project.projects_file.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or "Book ID" in line:
            continue
        cells = [item.strip().replace("\\|", "|") for item in line.strip().strip("|").split("|")]
        if len(cells) != len(PROJECT_COLUMNS):
            continue
        rows.append(ProjectRecord(*cells))
    return rows


def write_projects(project: ProjectPaths, rows: Iterable[ProjectRecord]) -> None:
    ordered = sorted(rows, key=lambda row: row.book_id)
    lines = [
        "# Translation projects",
        "",
        "This registry is authoritative for book identity and lifecycle metadata. Absolute worktree paths are local and are never interpreted as remote configuration.",
        "",
        "| " + " | ".join(PROJECT_COLUMNS) + " |",
        "|" + "|".join("---" for _ in PROJECT_COLUMNS) + "|",
    ]
    lines.extend("| " + " | ".join(_escape_cell(value) for value in row.cells()) + " |" for row in ordered)
    temporary = project.projects_file.with_suffix(".md.tmp")
    temporary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    temporary.replace(project.projects_file)


def project_record(project: ProjectPaths, book_id: str) -> ProjectRecord:
    validate_book_id(book_id)
    matches = [row for row in read_projects(project) if row.book_id == book_id]
    if len(matches) != 1:
        raise ProjectError(f"Book {book_id!r} is not registered exactly once in PROJECTS.md.")
    return matches[0]


def update_project_record(project: ProjectPaths, updated: ProjectRecord) -> None:
    rows = read_projects(project)
    found = False
    for index, row in enumerate(rows):
        if row.book_id == updated.book_id:
            rows[index] = updated
            found = True
            break
    if not found:
        rows.append(updated)
    write_projects(project, rows)


def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _write_empty_tsv(path: Path, columns: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle, delimiter="\t", lineterminator="\n").writerow(columns)


def _pdf_signature_is_valid(path: Path) -> bool:
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def _pdf_page_data(path: Path) -> tuple[int | None, list[dict[str, object]]]:
    """Inspect every page when pypdf is available; never fabricate a count."""
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None, []
    reader = PdfReader(str(path))
    pages = []
    for number, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        resources = page.get("/Resources") or {}
        xobjects = resources.get("/XObject") if hasattr(resources, "get") else None
        image_count = len(xobjects) if xobjects else 0
        if text.strip() and image_count:
            kind = "mixed"
        elif text.strip():
            kind = "native"
        elif image_count:
            kind = "scanned"
        else:
            kind = "unknown"
        pages.append({"pdf_page": number, "kind": kind, "text_characters": len(text), "image_objects": image_count})
    return len(reader.pages), pages


def _workflow_state(book: BookPaths) -> dict[str, object]:
    if not book.workflow_state.exists():
        return {"book_id": book.book_id, "status": "registered", "completed_units": [], "blocking_issues": []}
    return json.loads(book.workflow_state.read_text(encoding="utf-8"))


def _save_workflow_state(book: BookPaths, state: dict[str, object]) -> None:
    book.assert_write_path(book.workflow_state)
    _write_json(book.workflow_state, state)


def _book_status_text(book_id: str, phase: str, status: str, source_hash: str, blocking: Sequence[str]) -> str:
    lines = [
        f"Book ID: {book_id}",
        f"Phase: {phase}",
        f"Status: {status}",
        f"Source SHA-256: {source_hash}",
        "Blocking issues: " + ("; ".join(blocking) if blocking else "None"),
    ]
    return "\n".join(lines) + "\n"


def verify_book_context(project: ProjectPaths, book_id: str, *, writable: bool) -> tuple[BookPaths, ProjectRecord]:
    book = project.book(book_id)
    record = project_record(project, book_id)
    if not book.root.is_dir():
        raise ProjectError(f"Book directory is missing: {book.root}")
    if writable:
        expected_branch = f"book/{book_id}"
        branch = project.git_branch()
        if branch != expected_branch:
            raise ProjectError(f"Writable book command requires branch {expected_branch!r}; current branch is {branch!r}.")
        current_root = os.path.normcase(str(project.root.resolve()))
        registered = os.path.normcase(str(Path(record.worktree).resolve())) if record.worktree else ""
        if not registered or current_root != registered:
            raise ProjectError("branch/book-id/worktree/path mismatch; refusing book-specific writes.")
        worktrees = project.git_worktree_map()
        entry = worktrees.get(current_root)
        if not entry or entry.get("branch") != f"refs/heads/{expected_branch}":
            raise ProjectError("Git worktree registration does not match the selected book branch.")
    return book, record


def _copy_source(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise ProjectError(f"Source destination already exists: {destination}")
    shutil.copy2(source, destination)


def new_book(project: ProjectPaths, book_id: str, source: Path) -> dict[str, object]:
    """Register a new book on main, commit locally, then create its branch/worktree."""
    validate_book_id(book_id)
    project.require_clean_main()
    source = source.resolve(strict=True)
    if not source.is_file() or source.suffix.lower() != ".pdf" or not _pdf_signature_is_valid(source):
        raise ProjectError("--source must identify a readable PDF file with a valid PDF signature.")
    if any(row.book_id == book_id for row in read_projects(project)):
        raise ProjectError(f"Book {book_id!r} is already registered.")
    book = project.book(book_id)
    if book.root.exists():
        raise ProjectError(f"Book path already exists: {book.root}")
    branch = f"book/{book_id}"
    if run_git(project.root, ["show-ref", "--verify", "--quiet", f"refs/heads/{branch}"], check=False).returncode == 0:
        raise ProjectError(f"Book branch already exists: {branch}")
    worktree = (project.worktrees / book_id).resolve()
    if worktree.exists():
        raise ProjectError(f"Worktree path already exists: {worktree}")

    book.ensure_structure()
    source_hash = sha256_file(source)
    destination = book.source / source.name
    _copy_source(source, destination)
    template_version = str(load_json_yaml(project.config / "default.yaml")["template"]["version"])
    template_hash = directory_manifest_hash(project.template)
    config = {
        "schema_version": 1,
        "book_id": book_id,
        "title": "",
        "branch": branch,
        "worktree": str(worktree),
        "phase": "registration",
        "status": "registered",
        "source": {"path": f"input/source/{source.name}", "sha256": source_hash},
        "template_version": template_version,
        "template_manifest_hash": template_hash,
        "final_output": "",
    }
    _write_json(book.config_file, config)
    _write_empty_tsv(book.candidates, TERM_COLUMNS)
    _write_empty_tsv(book.unresolved, TERM_COLUMNS)
    _write_empty_tsv(book.proper_names, PROPER_NAME_COLUMNS)
    _write_empty_tsv(book.notation, NOTATION_COLUMNS)
    book.issues.write_text("", encoding="utf-8")
    state = {"book_id": book_id, "status": "registered", "completed_units": [], "blocking_issues": [], "next_unit": None}
    _save_workflow_state(book, state)
    book.status_file.write_text(_book_status_text(book_id, "registration", "registered", source_hash, []), encoding="utf-8")
    book.plans_file.write_text(
        f"# Plan for {book_id}\n\n1. Run `python -m mathbook start-book {book_id}` in its dedicated worktree.\n2. Review the representative sample.\n3. Approve the sample before full translation.\n",
        encoding="utf-8",
    )
    (book.root / "tex" / "main.tex").write_text(
        "\\documentclass[a4paper,UTF8,12pt]{ctexart}\n"
        "\\usepackage{Mystyle}\n\\usepackage{translation-adapter}\n"
        "\\input{translation-macros.tex}\n\\begin{document}\n\\end{document}\n",
        encoding="utf-8",
    )
    for relative in BookPaths.REQUIRED_DIRECTORIES:
        directory = book.root / relative
        if not any(directory.iterdir()):
            (directory / ".gitkeep").write_text("\n", encoding="utf-8")
    record = ProjectRecord(book_id, "", branch, str(worktree), "registration", "registered", source_hash, template_version, "", "")
    update_project_record(project, record)
    run_git(project.root, ["add", "--", f"books/{book_id}", "PROJECTS.md"])
    run_git(project.root, ["commit", "-m", f"Register book {book_id}"])
    run_git(project.root, ["branch", branch])
    worktree.parent.mkdir(parents=True, exist_ok=True)
    run_git(project.root, ["worktree", "add", str(worktree), branch])
    main_head = project.git_head()
    branch_head = run_git(project.root, ["rev-parse", branch]).stdout.strip()
    if main_head != branch_head:
        raise ProjectError("New book branch does not point to the latest local main commit.")
    worktree_source = worktree / "books" / book_id / "input" / "source" / source.name
    if not worktree_source.is_file() or sha256_file(worktree_source) != source_hash:
        raise ProjectError("Source PDF hash changed after worktree creation; binary Git attributes must be corrected.")
    return {"book_id": book_id, "branch": branch, "worktree": str(worktree), "source_sha256": source_hash, "status": "registered"}


def _run_processor(command: Sequence[str], project: ProjectPaths, book: BookPaths, action: str) -> None:
    if not command:
        raise ProjectError(
            f"No {action} processor is configured. Mechanical setup is complete, but mathematical content "
            "must be produced by an explicit Codex/agent processor; the system will not fabricate it."
        )
    environment = os.environ.copy()
    environment["MATHBOOK_BOOK_ID"] = book.book_id
    completed = subprocess.run(list(command), cwd=project.root, env=environment, check=False)
    if completed.returncode:
        raise ProjectError(f"Configured {action} processor failed with exit code {completed.returncode}.")


def main_worktree_project(project: ProjectPaths) -> ProjectPaths:
    for entry in project.git_worktree_map().values():
        if entry.get("branch") == "refs/heads/main":
            return ProjectPaths(Path(entry["worktree"]))
    raise ProjectError("No registered main worktree is available for a shared-state operation.")


def promote_terminology_safely(project: ProjectPaths, book: BookPaths) -> dict[str, object]:
    """Promote through the clean main worktree and synchronize main back locally."""
    if project.git_status().strip():
        raise ProjectError("Book worktree must be clean before terminology promotion.")
    main_project = main_worktree_project(project)
    if main_project.git_branch() != "main" or main_project.git_status().strip():
        raise ProjectError("Main worktree must be clean before terminology promotion.")
    before_candidates = book.candidates.read_bytes() if book.candidates.exists() else b""
    result = promote_candidates(main_project, book, commit=project.git_head())
    after_candidates = book.candidates.read_bytes() if book.candidates.exists() else b""
    if before_candidates != after_candidates:
        run_git(project.root, ["add", "--", f"books/{book.book_id}/glossary/candidates.tsv"])
        staged = run_git(project.root, ["diff", "--cached", "--quiet"], check=False)
        if staged.returncode == 1:
            run_git(project.root, ["commit", "-m", f"Review terminology candidates for {book.book_id}"])
    main_changes = run_git(
        main_project.root,
        ["status", "--porcelain=v1", "--", "glossary/terminology.tsv", "glossary/terminology-history.tsv"],
    ).stdout.strip()
    if main_changes:
        run_git(main_project.root, ["add", "--", "glossary/terminology.tsv", "glossary/terminology-history.tsv"])
        run_git(main_project.root, ["commit", "-m", f"Promote terminology from {book.book_id}"])
    if project.git_head() != main_project.git_head():
        run_git(project.root, ["merge", "--no-edit", "main"])
    return result


def start_book(
    project: ProjectPaths,
    book_id: str,
    *,
    processor: Callable[[BookPaths], None] | None = None,
) -> dict[str, object]:
    book, record = verify_book_context(project, book_id, writable=True)
    source = book.require_source_pdf()
    source_hash = sha256_file(source)
    if source_hash != book.load_config()["source"]["sha256"]:
        raise ProjectError("Source PDF hash differs from the registered hash.")
    page_count, pages = _pdf_page_data(source)
    inspection = {
        "book_id": book_id,
        "source": book.project.relative(source),
        "source_sha256": source_hash,
        "page_count": page_count,
        "classification_method": "pypdf text and image-object inspection" if pages else "unavailable",
        "pages": pages,
    }
    _write_json(book.root / "qa" / "pdf-inspection.json", inspection)
    categories: dict[str, int] = {}
    for page in pages:
        categories[str(page["kind"])] = categories.get(str(page["kind"]), 0) + 1
    sample_pages = []
    for kind in ("native", "scanned", "mixed", "unknown"):
        match = next((int(page["pdf_page"]) for page in pages if page["kind"] == kind), None)
        if match is not None and match not in sample_pages:
            sample_pages.append(match)
    if pages and not sample_pages:
        sample_pages = [1]
    sample_plan = {
        "book_id": book_id,
        "page_count": page_count,
        "page_classification_counts": categories,
        "representative_pages": sample_pages,
        "required_stages": [
            "extraction", "structure", "formula-registration", "terminology-candidates",
            "proper-names", "faithful-translation", "latex", "qa", "compile",
        ],
    }
    _write_json(book.root / "qa" / "sample-plan.json", sample_plan)
    state = _workflow_state(book)
    state.update({"status": "sample-processing", "sample_pages": sample_pages, "blocking_issues": []})
    _save_workflow_state(book, state)
    if processor:
        processor(book)
    else:
        command = load_json_yaml(project.config / "default.yaml").get("automation", {}).get("sample_processor", [])
        _run_processor(command, project, book, "sample")
    required = [book.root / "translation" / "reviewed" / "sample.tex", book.root / "qa" / "sample-qa.json"]
    if not all(path.is_file() for path in required):
        raise ProjectError("Sample processor completed without the required reviewed sample and QA result.")
    state["status"] = "awaiting-sample-approval"
    _save_workflow_state(book, state)
    book.status_file.write_text(_book_status_text(book_id, "sample", "awaiting-sample-approval", source_hash, []), encoding="utf-8")
    return {"book_id": book_id, "status": state["status"], "sample_pages": sample_pages}


def _blocking_issues(book: BookPaths) -> list[dict[str, object]]:
    issues = []
    if not book.issues.exists():
        return issues
    for line in book.issues.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        issue = json.loads(line)
        if issue.get("severity") == "blocking" and issue.get("review_status") not in {"resolved", "rejected"}:
            issues.append(issue)
    return issues


def approve_sample(project: ProjectPaths, book_id: str) -> dict[str, object]:
    book, record = verify_book_context(project, book_id, writable=True)
    state = _workflow_state(book)
    if state.get("status") != "awaiting-sample-approval":
        raise ProjectError("The book is not awaiting sample approval.")
    blockers = _blocking_issues(book)
    qa_path = book.root / "qa" / "sample-qa.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8")) if qa_path.exists() else {}
    required_checks = ("template", "formula", "cross_references", "compile")
    failed = [name for name in required_checks if qa.get(name) != "passed"]
    if blockers or failed:
        raise ProjectError(f"Sample approval refused; blocking issues={len(blockers)}, failed checks={failed}.")
    state["status"] = "ready-for-full-translation"
    _save_workflow_state(book, state)
    config = book.load_config()
    book.status_file.write_text(_book_status_text(book_id, "translation", "ready-for-full-translation", config["source"]["sha256"], []), encoding="utf-8")
    return {"book_id": book_id, "status": state["status"]}


def _progress_rows(book: BookPaths) -> list[dict[str, str]]:
    if not book.chapter_progress.exists():
        return []
    with book.chapter_progress.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def next_incomplete_unit(book: BookPaths) -> str | None:
    rows = _progress_rows(book)
    for row in rows:
        status = row.get("QA Status", row.get("Status", "")).strip().lower()
        if status not in {"passed", "complete", "completed"}:
            return row.get("Unit ID") or row.get("Unit")
    return None


def translate_book(
    project: ProjectPaths,
    book_id: str,
    *,
    processor: Callable[[BookPaths, str], None] | None = None,
) -> dict[str, object]:
    book, record = verify_book_context(project, book_id, writable=True)
    state = _workflow_state(book)
    if state.get("status") not in {"ready-for-full-translation", "translating"}:
        raise ProjectError("Full translation requires an approved sample.")
    state["status"] = "translating"
    processed: list[str] = []
    while True:
        blockers = _blocking_issues(book)
        if blockers:
            state["blocking_issues"] = [str(issue.get("id", "unknown")) for issue in blockers]
            state["next_unit"] = next_incomplete_unit(book)
            _save_workflow_state(book, state)
            return {"book_id": book_id, "status": "blocked", "processed": processed, "blocking": state["blocking_issues"]}
        unit = next_incomplete_unit(book)
        if unit is None:
            state["status"] = "translation-complete"
            state["next_unit"] = None
            _save_workflow_state(book, state)
            return {"book_id": book_id, "status": "translation-complete", "processed": processed}
        completed_before = set(state.get("completed_units", []))
        if unit in completed_before:
            raise ProjectError(f"Progress inconsistency: completed unit {unit!r} is still selected as incomplete.")
        if processor:
            processor(book, unit)
        else:
            command = load_json_yaml(project.config / "default.yaml").get("automation", {}).get("translation_processor", [])
            _run_processor([*command, unit] if command else [], project, book, "translation")
        if next_incomplete_unit(book) == unit:
            raise ProjectError(f"Translation processor did not mark natural unit {unit!r} as passed.")
        completed = list(state.get("completed_units", []))
        completed.append(unit)
        state["completed_units"] = completed
        processed.append(unit)
        _save_workflow_state(book, state)
        run_git(project.root, ["add", "--", f"books/{book_id}"])
        run_git(project.root, ["commit", "-m", f"Translate {book_id} {unit}"])


def resume_book(
    project: ProjectPaths,
    book_id: str,
    *,
    processor: Callable[[BookPaths, str], None] | None = None,
) -> dict[str, object]:
    book, _ = verify_book_context(project, book_id, writable=True)
    state = _workflow_state(book)
    next_unit = next_incomplete_unit(book)
    if next_unit and next_unit in set(state.get("completed_units", [])):
        raise ProjectError("Resume refused to repeat a completed unit.")
    if state.get("status") in {"ready-for-full-translation", "translating"}:
        return translate_book(project, book_id, processor=processor)
    return {"book_id": book_id, "status": state.get("status"), "next_unit": next_unit, "resumed": False}


def finish_book(
    project: ProjectPaths,
    book_id: str,
    *,
    processor: Callable[[BookPaths], None] | None = None,
) -> dict[str, object]:
    book, record = verify_book_context(project, book_id, writable=True)
    if next_incomplete_unit(book) is not None:
        raise ProjectError("finish-book refused: at least one natural unit has not passed QA.")
    blockers = _blocking_issues(book)
    if blockers:
        raise ProjectError(f"finish-book refused: {len(blockers)} blocking QA issue(s) remain.")
    if processor:
        processor(book)
    else:
        command = load_json_yaml(project.config / "default.yaml").get("automation", {}).get("finish_processor", [])
        _run_processor(command, project, book, "finish")
    final_report = book.root / "qa" / "final-report.json"
    final_pdf = book.root / "output" / "book-zh.pdf"
    if not final_report.is_file() or not final_pdf.is_file():
        raise ProjectError("Final processor did not produce the required final report and PDF.")
    config = book.load_config()
    config["phase"] = "completed"
    config["status"] = "completed"
    config["final_output"] = "output/book-zh.pdf"
    _write_json(book.config_file, config)
    state = _workflow_state(book)
    state["status"] = "completed"
    _save_workflow_state(book, state)
    book.status_file.write_text(_book_status_text(book_id, "completed", "completed", config["source"]["sha256"], []), encoding="utf-8")
    run_git(project.root, ["add", "--", f"books/{book_id}"])
    run_git(project.root, ["commit", "-m", f"Complete translation of {book_id}"])
    promotion = promote_terminology_safely(project, book)
    main_project = main_worktree_project(project)
    if main_project.git_status().strip():
        raise ProjectError("Main worktree became dirty before completed-book integration.")
    run_git(main_project.root, ["merge", "--ff-only", f"book/{book_id}"])
    main_record = project_record(main_project, book_id)
    main_record.phase = "completed"
    main_record.status = "completed"
    main_record.final_output = f"books/{book_id}/output/book-zh.pdf"
    main_record.blocking_issues = ""
    update_project_record(main_project, main_record)
    run_git(main_project.root, ["add", "--", "PROJECTS.md"])
    run_git(main_project.root, ["commit", "-m", f"Record completion of {book_id}"])
    run_git(project.root, ["merge", "--ff-only", "main"])
    return {"book_id": book_id, "status": "completed", "terminology": promotion}


def book_status(project: ProjectPaths, book_id: str) -> dict[str, object]:
    book = project.book(book_id)
    record = project_record(project, book_id)
    state = _workflow_state(book)
    effective_status = str(state.get("status") or record.status)
    effective_phase = (
        "sample" if effective_status in {"sample-processing", "awaiting-sample-approval"}
        else "translation" if effective_status in {"ready-for-full-translation", "translating", "translation-complete"}
        else "completed" if effective_status == "completed"
        else record.phase
    )
    return {
        "book_id": record.book_id,
        "title": record.title,
        "branch": record.branch,
        "worktree": record.worktree,
        "phase": effective_phase,
        "status": effective_status,
        "progress": {
            "completed_units": state.get("completed_units", []),
            "next_unit": None if effective_status == "completed" else next_incomplete_unit(book),
        },
        "blocking_issues": state.get("blocking_issues", []),
        "final_output": record.final_output,
        "source_hash": record.source_hash,
        "template_version": record.template_version,
    }


def list_books(project: ProjectPaths) -> list[dict[str, object]]:
    return [book_status(project, row.book_id) for row in read_projects(project)]


def terminology_action(project: ProjectPaths, action: str, book_id: str | None = None) -> object:
    if action in {"review", "promote"} and not book_id:
        raise ProjectError("terminology review/promote requires an explicit book-id.")
    if action == "review":
        return review_candidates(project, project.book(str(book_id)))
    if action == "promote":
        book, _ = verify_book_context(project, str(book_id), writable=True)
        return promote_terminology_safely(project, book)
    if action == "conflicts":
        from .terminology import _read_tsv, find_conflicts
        return find_conflicts(_read_tsv(project.glossary / "terminology.tsv", TERM_COLUMNS))
    if action == "history":
        from .terminology import _read_tsv
        return _read_tsv(project.glossary / "terminology-history.tsv", HISTORY_COLUMNS)
    raise ProjectError(f"Unsupported terminology action: {action}")
