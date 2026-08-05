"""Validated structure-block interfaces."""

from __future__ import annotations

from dataclasses import dataclass, field


BLOCK_TYPES = frozenset({
    "chapter", "section", "subsection", "definition", "theorem", "lemma",
    "proposition", "corollary", "proof", "example", "remark", "exercise",
    "equation", "figure", "table", "footnote", "ordinary-paragraph", "unknown",
})


@dataclass(frozen=True)
class StructureBlock:
    id: str
    type: str
    page: int
    bbox: tuple[float, float, float, float] | None = None
    confidence: float = 0.0
    review_status: str = "not-reviewed"
    text_block_ids: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.type not in BLOCK_TYPES:
            raise ValueError(f"Unsupported structure block type: {self.type}")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


def classify_or_unknown(candidate: str | None) -> str:
    """Accept a supported classification and use unknown otherwise."""
    return candidate if candidate in BLOCK_TYPES else "unknown"

