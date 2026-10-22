"""Shared terminology library, per-book candidates, and audited promotion."""

from __future__ import annotations

import csv
import datetime as dt
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .project import BookPaths, ProjectError, ProjectPaths


APPROVED_STATUS = "approved"
ALLOWED_STATUSES = {"approved", "proposed", "ambiguous", "rejected", "needs-review"}
TERM_COLUMNS = (
    "English", "Preferred Chinese", "Domain", "Context", "Forbidden Alternatives",
    "Status", "First Source", "First Location", "Last Verified Source",
    "Last Verified Location", "Notes",
)
HISTORY_COLUMNS = (
    "Timestamp UTC", "Action", "Book ID", "English", "Domain", "Context",
    "Previous Status", "New Status", "Source Location", "Commit", "Notes",
)
EPONYM_NOUNS = {"space": "空间", "inequality": "不等式", "theorem": "定理"}


@dataclass(frozen=True)
class TerminologyRecord:
    source_form: str
    canonical_form: str | None
    context: str | None
    review_status: str = "needs-review"

    def __post_init__(self) -> None:
        if self.review_status == APPROVED_STATUS and not self.canonical_form:
            raise ValueError("An approved term requires a confirmed canonical form.")


class TerminologyRegistry:
    """In-memory controlled terms used by lower-level translation code."""

    def __init__(self) -> None:
        self._records: dict[tuple[str, str | None], TerminologyRecord] = {}

    def register(
        self,
        source_form: str,
        canonical_form: str | None,
        context: str | None,
        review_status: str = "needs-review",
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


def _read_tsv(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != columns:
            raise ProjectError(f"Unexpected TSV schema in {path}; expected {columns!r}.")
        return [{key: row.get(key, "") for key in columns} for row in reader]


def _write_tsv(path: Path, columns: tuple[str, ...], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in columns})
    temporary.replace(path)


def term_key(row: dict[str, str]) -> tuple[str, str, str]:
    return row["English"].strip(), row["Domain"].strip(), row["Context"].strip()


def find_conflicts(rows: Iterable[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(term_key(row), []).append(row)
    conflicts = []
    for key, items in sorted(grouped.items()):
        translations = sorted({item["Preferred Chinese"].strip() for item in items if item["Preferred Chinese"].strip()})
        if len(translations) > 1:
            conflicts.append({"key": key, "translations": translations, "rows": len(items)})
    return conflicts


def review_candidates(project: ProjectPaths, book: BookPaths) -> dict[str, object]:
    global_rows = _read_tsv(project.glossary / "terminology.tsv", TERM_COLUMNS)
    candidate_rows = _read_tsv(book.candidates, TERM_COLUMNS)
    global_by_key = {term_key(row): row for row in global_rows}
    duplicate = 0
    compatible = 0
    needs_review = 0
    promotable = 0
    for row in candidate_rows:
        if row["Status"] not in ALLOWED_STATUSES:
            raise ProjectError(f"Unsupported terminology status {row['Status']!r} in {book.candidates}.")
        existing = global_by_key.get(term_key(row))
        if existing:
            duplicate += 1
            if existing["Preferred Chinese"] == row["Preferred Chinese"]:
                compatible += 1
            else:
                needs_review += 1
        elif row["Status"] == "proposed" and "[safe-to-promote]" in row["Notes"]:
            promotable += 1
        else:
            needs_review += 1
    return {
        "book_id": book.book_id,
        "candidates": len(candidate_rows),
        "duplicates": duplicate,
        "compatible": compatible,
        "promotable": promotable,
        "needs_review": needs_review,
        "global_conflicts": find_conflicts(global_rows),
        "candidate_conflicts": find_conflicts(candidate_rows),
    }


def promote_candidates(
    project: ProjectPaths,
    book: BookPaths,
    *,
    commit: str = "",
) -> dict[str, object]:
    """Promote only explicitly safe, non-conflicting proposals; never overwrite."""
    global_path = project.glossary / "terminology.tsv"
    history_path = project.glossary / "terminology-history.tsv"
    global_rows = _read_tsv(global_path, TERM_COLUMNS)
    candidate_rows = _read_tsv(book.candidates, TERM_COLUMNS)
    history_rows = _read_tsv(history_path, HISTORY_COLUMNS)
    global_by_key = {term_key(row): row for row in global_rows}
    kept: list[dict[str, str]] = []
    promoted: list[dict[str, str]] = []
    duplicate = 0
    needs_review = 0
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    for row in candidate_rows:
        key = term_key(row)
        existing = global_by_key.get(key)
        if existing:
            if existing["Preferred Chinese"] == row["Preferred Chinese"]:
                duplicate += 1
                continue
            row["Status"] = "needs-review"
            kept.append(row)
            needs_review += 1
            continue
        complete = all(row[column].strip() for column in ("English", "Preferred Chinese", "Domain", "Context"))
        safe = row["Status"] == "proposed" and "[safe-to-promote]" in row["Notes"]
        same_english = [item for item in global_rows if item["English"] == row["English"]]
        same_domain_different = any(item["Domain"] == row["Domain"] and term_key(item) != key for item in same_english)
        if not complete or not safe or same_domain_different:
            row["Status"] = "needs-review"
            kept.append(row)
            needs_review += 1
            continue
        promoted_row = dict(row)
        promoted_row["Status"] = "approved"
        global_rows.append(promoted_row)
        global_by_key[key] = promoted_row
        promoted.append(promoted_row)
        history_rows.append({
            "Timestamp UTC": timestamp,
            "Action": "promote",
            "Book ID": book.book_id,
            "English": row["English"],
            "Domain": row["Domain"],
            "Context": row["Context"],
            "Previous Status": row["Status"],
            "New Status": "approved",
            "Source Location": row["First Location"],
            "Commit": commit,
            "Notes": "Promoted from an explicit [safe-to-promote] proposal after duplicate and domain checks.",
        })
    if find_conflicts(global_rows):
        raise ProjectError("Promotion would create a conflicting English + Domain + Context key.")
    _write_tsv(global_path, TERM_COLUMNS, sorted(global_rows, key=term_key))
    _write_tsv(history_path, HISTORY_COLUMNS, history_rows)
    _write_tsv(book.candidates, TERM_COLUMNS, kept)
    return {"promoted": len(promoted), "duplicates_removed": duplicate, "needs_review": needs_review}


def name_is_preserved(source: str, candidate: str) -> bool:
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


def initialize_tsv(path: Path, columns: tuple[str, ...]) -> None:
    if not path.exists():
        _write_tsv(path, columns, [])


def migrate_legacy_terminology(path: Path, history_path: Path, *, book_id: str, commit: str) -> int:
    """Losslessly map the first-book legacy terminology columns into the shared schema."""
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        legacy = list(reader)
    expected = {
        "Source Term", "Chinese Translation", "Mathematical Context", "Definition or Scope",
        "Source Reference", "First Occurrence", "Review Status", "Reviewer", "Notes",
    }
    if set(reader.fieldnames or ()) != expected:
        raise ProjectError("Legacy terminology schema was not recognized; refusing a lossy migration.")
    rows: list[dict[str, str]] = []
    history: list[dict[str, str]] = []
    timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    for item in legacy:
        status = item["Review Status"] or "needs-review"
        if status == "unreviewed":
            status = "needs-review"
        notes = item["Notes"]
        if item["Reviewer"]:
            notes = f"{notes} Reviewer: {item['Reviewer']}.".strip()
        row = {
            "English": item["Source Term"],
            "Preferred Chinese": item["Chinese Translation"],
            "Domain": item["Mathematical Context"],
            "Context": item["Definition or Scope"],
            "Forbidden Alternatives": "",
            "Status": status,
            "First Source": item["Source Reference"],
            "First Location": item["First Occurrence"],
            "Last Verified Source": item["Source Reference"],
            "Last Verified Location": item["First Occurrence"],
            "Notes": notes,
        }
        rows.append(row)
        history.append({
            "Timestamp UTC": timestamp,
            "Action": "initial-import",
            "Book ID": book_id,
            "English": row["English"],
            "Domain": row["Domain"],
            "Context": row["Context"],
            "Previous Status": item["Review Status"],
            "New Status": status,
            "Source Location": row["First Location"],
            "Commit": commit,
            "Notes": "Imported from the completed first-book terminology control file without approval changes.",
        })
    _write_tsv(path, TERM_COLUMNS, rows)
    _write_tsv(history_path, HISTORY_COLUMNS, history)
    return len(rows)
