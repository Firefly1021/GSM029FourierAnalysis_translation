"""Terminology registration and exact personal-name protection."""

from __future__ import annotations

from dataclasses import dataclass


APPROVED_STATUS = "approved"
EPONYM_NOUNS = {
    "space": "空间",
    "inequality": "不等式",
    "theorem": "定理",
}


@dataclass(frozen=True)
class TerminologyRecord:
    source_form: str
    canonical_form: str | None
    context: str | None
    review_status: str = "unreviewed"

    def __post_init__(self) -> None:
        if self.review_status == APPROVED_STATUS and not self.canonical_form:
            raise ValueError("An approved term requires a confirmed canonical form.")


class TerminologyRegistry:
    """Register controlled terms without silently approving proposals."""

    def __init__(self) -> None:
        self._records: dict[tuple[str, str | None], TerminologyRecord] = {}

    def register(
        self,
        source_form: str,
        canonical_form: str | None,
        context: str | None,
        review_status: str = "unreviewed",
        *,
        confirmed: bool = False,
    ) -> TerminologyRecord:
        if review_status == APPROVED_STATUS and not confirmed:
            raise ValueError("An unconfirmed terminology proposal cannot be approved.")
        record = TerminologyRecord(source_form, canonical_form, context, review_status)
        key = (source_form, context)
        existing = self._records.get(key)
        if existing is not None and existing != record:
            raise ValueError("A different controlled term already exists for this source form and context.")
        self._records[key] = record
        return record

    def records(self) -> tuple[TerminologyRecord, ...]:
        return tuple(self._records[key] for key in sorted(self._records, key=lambda item: (item[0], item[1] or "")))


def name_is_preserved(source: str, candidate: str) -> bool:
    """Require byte-for-byte Unicode string equality for personal names."""
    return source == candidate


def assert_name_preserved(source: str, candidate: str) -> None:
    if not name_is_preserved(source, candidate):
        raise ValueError(f"Personal name changed: {source!r} -> {candidate!r}")


def translate_eponym_term(term: str) -> str:
    """Translate only a recognized trailing ordinary mathematical noun."""
    for english, chinese in EPONYM_NOUNS.items():
        suffix = " " + english
        if term.endswith(suffix):
            return term[: -len(suffix)] + " " + chinese
    return term
