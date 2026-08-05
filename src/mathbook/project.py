"""Project paths, configuration, hashing, and validation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PDF_MESSAGE = "Source PDF has not been supplied. Phase 2 cannot begin."


class ProjectError(RuntimeError):
    """Raised when project state is incomplete or inconsistent."""


def resolve_project_path(value: str | Path) -> Path:
    """Resolve a repository-relative path without requiring it to exist."""
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def load_config(name: str) -> dict[str, Any]:
    """Load a JSON-compatible YAML configuration file.

    JSON is a strict subset of YAML 1.2, which keeps parsing dependency-free and
    deterministic for the project commands and tests.
    """
    path = ROOT / "config" / name
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectError(f"Cannot load configuration {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ProjectError(f"Configuration must contain a mapping: {path}")
    return data


def sha256_file(path: Path) -> str:
    """Return a lowercase SHA-256 digest without modifying the file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(directory: Path) -> Iterable[Path]:
    """Yield all files below a directory in stable relative-path order."""
    return sorted((item for item in directory.rglob("*") if item.is_file()), key=lambda item: item.as_posix())


def source_pdf_files() -> list[Path]:
    """List supplied PDF files, excluding directory markers."""
    source_dir = ROOT / "input" / "source"
    return sorted(path for path in source_dir.glob("*.pdf") if path.is_file())


def require_source_pdf() -> Path:
    """Return the only source PDF or fail safely before Phase 2."""
    files = source_pdf_files()
    if not files:
        raise ProjectError(SOURCE_PDF_MESSAGE)
    if len(files) > 1:
        raise ProjectError("Multiple source PDFs are present; select one explicitly before Phase 2 begins.")
    return files[0]


REQUIRED_PATHS = (
    "config/project.yaml", "config/translation.yaml", "input/template/style",
    "input/template/reference", "input/template/assets", "input/source",
    "schemas/text-block.schema.json", "schemas/structure-block.schema.json",
    "schemas/formula.schema.json", "schemas/terminology.schema.json",
    "schemas/qa-issue.schema.json", "glossary/terminology.tsv",
    "glossary/proper-names.tsv", "glossary/notation.tsv", "glossary/unresolved.tsv",
    "tex/main.tex", "tex/translation-adapter.sty", "qa/template",
)


def validate_project_structure() -> list[str]:
    """Return missing required paths; an empty list means the scaffold is complete."""
    return [item for item in REQUIRED_PATHS if not (ROOT / item).exists()]

