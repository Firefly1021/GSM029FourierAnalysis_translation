"""Repository and per-book paths for the multi-book translation system."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
BOOK_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_PDF_MESSAGE = "A source PDF is required for the selected book."


class ProjectError(RuntimeError):
    """Raised when repository or book state is unsafe or inconsistent."""


def _resolved(path: Path) -> Path:
    return path.resolve(strict=False)


def _is_within(path: Path, parent: Path) -> bool:
    try:
        _resolved(path).relative_to(_resolved(parent))
    except ValueError:
        return False
    return True


def validate_book_id(book_id: str) -> str:
    """Validate a filesystem- and branch-safe explicit book identifier."""
    if not book_id or not BOOK_ID_PATTERN.fullmatch(book_id):
        raise ProjectError(
            "Invalid book-id. Use lowercase ASCII letters, digits, and single hyphens; "
            "path separators and traversal components are forbidden."
        )
    return book_id


def sha256_file(path: Path) -> str:
    """Return a lowercase SHA-256 digest without modifying the file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


_MANIFEST_TEXT_SUFFIXES = {".bib", ".cls", ".json", ".jsonl", ".md", ".sty", ".tex", ".tsv", ".yaml", ".yml"}


def manifest_file_fingerprint(path: Path) -> tuple[int, str]:
    """Return a worktree-portable size and SHA-256 for manifest metadata.

    Git may materialize text files with LF or CRLF in different Windows
    worktrees. Manifest fingerprints use the repository's canonical LF form
    for declared text inputs while leaving binary assets byte-exact.
    """
    data = path.read_bytes()
    if path.name == ".gitkeep" or path.suffix.lower() in _MANIFEST_TEXT_SUFFIXES:
        data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return len(data), hashlib.sha256(data).hexdigest()


def iter_files(directory: Path) -> Iterable[Path]:
    """Yield files below a directory in stable relative-path order."""
    return sorted(
        (item for item in directory.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(directory).as_posix(),
    )


def directory_manifest_hash(directory: Path) -> str:
    """Hash relative paths, sizes, and file hashes for a stable directory manifest."""
    digest = hashlib.sha256()
    for path in iter_files(directory):
        relative = path.relative_to(directory).as_posix()
        size, file_hash = manifest_file_fingerprint(path)
        digest.update(f"{relative}\0{size}\0{file_hash}\n".encode("utf-8"))
    return digest.hexdigest()


def run_git(
    root: Path,
    arguments: Sequence[str],
    *,
    check: bool = True,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Run one local Git operation without invoking a shell."""
    forbidden = (
        arguments and arguments[0] == "push",
        len(arguments) >= 2 and arguments[0] == "remote" and arguments[1] in {"set-url", "remove", "rename"},
        arguments and arguments[0] in {"filter-branch", "replace"},
    )
    if any(forbidden):
        raise ProjectError("Remote writes and history-rewriting Git operations are forbidden by project automation.")
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=capture_output,
        check=False,
    )
    if check and completed.returncode:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise ProjectError(f"Git command failed: git {' '.join(arguments)}\n{detail}")
    return completed


@dataclass(frozen=True)
class ProjectPaths:
    """All shared paths and guarded access to book roots."""

    root: Path = ROOT

    def __post_init__(self) -> None:
        object.__setattr__(self, "root", _resolved(self.root))

    @property
    def config(self) -> Path:
        return self.root / "config"

    @property
    def books(self) -> Path:
        return self.root / "books"

    @property
    def glossary(self) -> Path:
        return self.root / "glossary"

    @property
    def template(self) -> Path:
        return self.root / "template"

    @property
    def style(self) -> Path:
        return self.root / "style"

    @property
    def projects_file(self) -> Path:
        return self.root / "PROJECTS.md"

    @property
    def worktrees(self) -> Path:
        return self.root.parent / f"{self.root.name}-worktrees"

    def book(self, book_id: str) -> "BookPaths":
        validated = validate_book_id(book_id)
        path = _resolved(self.books / validated)
        if not _is_within(path, self.books):
            raise ProjectError("Resolved book path escaped books/.")
        return BookPaths(self, validated, path)

    def relative(self, path: Path) -> str:
        if not _is_within(path, self.root):
            raise ProjectError(f"Path is outside the repository: {path}")
        return _resolved(path).relative_to(self.root).as_posix()

    def git_branch(self) -> str:
        return run_git(self.root, ["branch", "--show-current"]).stdout.strip()

    def git_head(self) -> str:
        return run_git(self.root, ["rev-parse", "HEAD"]).stdout.strip()

    def git_status(self) -> str:
        return run_git(self.root, ["status", "--porcelain=v1", "--untracked-files=all"]).stdout

    def require_clean_main(self) -> None:
        branch = self.git_branch()
        if branch != "main":
            raise ProjectError(f"This operation must run in the main worktree; current branch is {branch!r}.")
        status = self.git_status().strip()
        if status:
            raise ProjectError("The main worktree is not clean; refusing to create or register a book.")

    def git_worktree_map(self) -> dict[str, dict[str, str]]:
        """Return worktrees keyed by normalized absolute path."""
        output = run_git(self.root, ["worktree", "list", "--porcelain"]).stdout
        result: dict[str, dict[str, str]] = {}
        current: dict[str, str] = {}
        for line in [*output.splitlines(), ""]:
            if not line:
                if current.get("worktree"):
                    key = os.path.normcase(str(_resolved(Path(current["worktree"]))))
                    result[key] = current
                current = {}
                continue
            key, _, value = line.partition(" ")
            current[key] = value
        return result


@dataclass(frozen=True)
class BookPaths:
    """All writable state for exactly one explicitly selected book."""

    project: ProjectPaths
    book_id: str
    root: Path

    REQUIRED_DIRECTORIES = (
        "config", "input/source", "glossary", "workspace/pages", "workspace/raw-text",
        "workspace/layout", "workspace/formula-images", "workspace/temporary",
        "structured/source", "structured/reviewed", "formulae", "translation/draft",
        "translation/reviewed", "translation/final", "tex/chapters", "tex/figures",
        "tex/generated", "qa", "logs", "output",
    )

    @property
    def config_file(self) -> Path:
        return self.root / "config" / "book.yaml"

    @property
    def source(self) -> Path:
        return self.root / "input" / "source"

    @property
    def candidates(self) -> Path:
        return self.root / "glossary" / "candidates.tsv"

    @property
    def unresolved(self) -> Path:
        return self.root / "glossary" / "unresolved.tsv"

    @property
    def proper_names(self) -> Path:
        return self.root / "glossary" / "proper-names.tsv"

    @property
    def notation(self) -> Path:
        return self.root / "glossary" / "notation.tsv"

    @property
    def status_file(self) -> Path:
        return self.root / "PROJECT_STATUS.md"

    @property
    def plans_file(self) -> Path:
        return self.root / "PLANS.md"

    @property
    def issues(self) -> Path:
        return self.root / "qa" / "issues.jsonl"

    @property
    def workflow_state(self) -> Path:
        return self.root / "qa" / "workflow-state.json"

    @property
    def chapter_progress(self) -> Path:
        return self.root / "qa" / "chapter-progress.tsv"

    @property
    def main_tex(self) -> Path:
        return self.root / "tex" / "main.tex"

    def ensure_structure(self) -> None:
        if not _is_within(self.root, self.project.books):
            raise ProjectError("Book root escaped the repository books directory.")
        for relative in self.REQUIRED_DIRECTORIES:
            (self.root / relative).mkdir(parents=True, exist_ok=True)

    def assert_write_path(self, path: Path) -> Path:
        resolved = _resolved(path)
        if not _is_within(resolved, self.root):
            raise ProjectError(f"Cross-book or shared-state write refused: {path}")
        return resolved

    def source_pdfs(self) -> list[Path]:
        return sorted(path for path in self.source.glob("*.pdf") if path.is_file())

    def require_source_pdf(self) -> Path:
        files = self.source_pdfs()
        if not files:
            raise ProjectError(SOURCE_PDF_MESSAGE)
        if len(files) != 1:
            raise ProjectError(f"Book {self.book_id!r} must contain exactly one source PDF.")
        return files[0]

    def load_config(self) -> dict[str, Any]:
        return load_json_yaml(self.config_file)


def load_json_yaml(path: Path) -> dict[str, Any]:
    """Load the project's JSON-compatible YAML files without a YAML dependency."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectError(f"Cannot load configuration {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ProjectError(f"Configuration must contain a mapping: {path}")
    return data


def load_config(name: str) -> dict[str, Any]:
    return load_json_yaml(ProjectPaths().config / name)


def resolve_project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def source_pdf_files(book_id: str | None = None) -> list[Path]:
    if not book_id:
        raise ProjectError("A book-id is required; implicit book selection is forbidden.")
    return ProjectPaths().book(book_id).source_pdfs()


def require_source_pdf(book_id: str | None = None) -> Path:
    if not book_id:
        raise ProjectError("A book-id is required; implicit book selection is forbidden.")
    return ProjectPaths().book(book_id).require_source_pdf()


SHARED_REQUIRED_PATHS = (
    "AGENTS.md", "README.md", "PROJECTS.md", "config/default.yaml",
    "config/translation.yaml", "glossary/terminology.tsv",
    "glossary/terminology-history.tsv", "glossary/terminology-schema.md",
    "template/style", "template/reference", "template/assets", "template/adapter",
    "style/chinese-mathematical-style.md", "src/mathbook", "scripts", "schemas", "tests", "books",
)


def validate_project_structure() -> list[str]:
    project = ProjectPaths()
    missing = [item for item in SHARED_REQUIRED_PATHS if not (project.root / item).exists()]
    if project.books.exists():
        for directory in sorted(path for path in project.books.iterdir() if path.is_dir()):
            try:
                book = project.book(directory.name)
            except ProjectError as exc:
                missing.append(str(exc))
                continue
            for relative in (*BookPaths.REQUIRED_DIRECTORIES, "PROJECT_STATUS.md", "PLANS.md", "config/book.yaml"):
                if not (book.root / relative).exists():
                    missing.append(f"books/{book.book_id}/{relative}")
    return missing
