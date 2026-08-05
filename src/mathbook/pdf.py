"""Source-PDF classification and rendering interfaces for Phase 2."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Protocol

from .project import require_source_pdf


class PDFKind(str, Enum):
    NATIVE = "native"
    SCANNED = "scanned"
    MIXED = "mixed"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class PDFInspection:
    path: Path
    kind: PDFKind
    page_count: int
    confidence: float
    review_status: str


class PDFInspector(Protocol):
    def inspect(self, path: Path) -> PDFInspection: ...


class PageRenderer(Protocol):
    def render(self, path: Path, output_directory: Path, dpi: int = 300) -> list[Path]: ...


def source_pdf_path() -> Path:
    """Fail safely until the user supplies exactly one PDF."""
    return require_source_pdf()

