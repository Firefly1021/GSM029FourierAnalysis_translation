"""Stable formula registry without formula rewriting."""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class FormulaRecord:
    id: str
    source_latex: str
    tokens: tuple[str, ...]
    page: int
    bbox: tuple[float, float, float, float] | None
    confidence: float
    review_status: str
    label: str | None = None
    number: str | None = None


class FormulaRegistry:
    """Register immutable source formulas under deterministic IDs."""

    def __init__(self) -> None:
        self._records: dict[str, FormulaRecord] = {}

    @staticmethod
    def stable_id(source_latex: str, page: int, bbox: tuple[float, float, float, float] | None) -> str:
        payload = f"{page}\0{bbox!r}\0{source_latex}".encode("utf-8")
        return "formula-" + hashlib.sha256(payload).hexdigest()[:16]

    def register(
        self,
        source_latex: str,
        tokens: tuple[str, ...],
        page: int,
        bbox: tuple[float, float, float, float] | None,
        confidence: float,
        review_status: str = "not-reviewed",
        label: str | None = None,
        number: str | None = None,
    ) -> FormulaRecord:
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if confidence < 1.0 and review_status == "approved":
            raise ValueError("An uncertain formula cannot be approved without review.")
        identifier = self.stable_id(source_latex, page, bbox)
        record = FormulaRecord(identifier, source_latex, tokens, page, bbox, confidence, review_status, label, number)
        existing = self._records.get(identifier)
        if existing is not None and existing != record:
            raise ValueError(f"Formula ID collision with different content: {identifier}")
        self._records[identifier] = record
        return record

    def records(self) -> list[dict[str, object]]:
        return [asdict(self._records[key]) for key in sorted(self._records)]

