"""Text and layout extraction interfaces; no extractor is selected in Phase 1."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class BoundingBox:
    x0: float
    y0: float
    x1: float
    y1: float


@dataclass(frozen=True)
class ExtractedText:
    page: int
    text: str
    bbox: BoundingBox | None
    confidence: float
    review_status: str = "not-reviewed"


class NativeTextExtractor(Protocol):
    def extract(self, pdf: Path) -> list[ExtractedText]: ...


class ScannedTextExtractor(Protocol):
    def extract(self, page_images: list[Path]) -> list[ExtractedText]: ...


class LayoutExtractor(Protocol):
    def extract(self, pdf: Path) -> list[ExtractedText]: ...

