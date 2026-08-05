"""Translation-block interface with explicit review metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class TranslationBlock:
    id: str
    block_type: str
    source_text: str
    translated_text: str | None
    formula_ids: tuple[str, ...]
    confidence: float
    review_status: str


def translate_block(block: TranslationBlock, translator: Callable[[str], str]) -> TranslationBlock:
    """Apply an explicitly supplied translator; no translator is bundled."""
    if block.translated_text is not None:
        raise ValueError("Refusing to overwrite an existing translation.")
    translated = translator(block.source_text)
    if not isinstance(translated, str) or not translated:
        raise ValueError("Translator returned no text.")
    return TranslationBlock(block.id, block.block_type, block.source_text, translated, block.formula_ids, 0.0, "needs-review")

